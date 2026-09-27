#!/usr/bin/env node
// Graba una animación en vídeo: vibe-responsable.<idioma>.mp4 (animacion.<idioma>.html) o
// vibe-responsable-<página>.<idioma>.mp4 (<página>.<idioma>.html, por ejemplo zoom).
// Uso, desde la raíz del repositorio: node animacion/grabar.js [idioma] [página]
// Necesita el Chromium de Playwright instalado de forma global (npm i -g playwright) y ffmpeg.
// Sirve el repositorio en un puerto libre, pinta cada fotograma con window.fijar(t),
// obtiene la banda sonora con window.audioWav() y lo une todo con ffmpeg.
// SPDX-License-Identifier: AGPL-3.0-or-later
"use strict";
const path = require("path"), fs = require("fs"), http = require("http"), os = require("os");
const { execSync, spawn } = require("child_process");
const { chromium } = require(path.join(execSync("npm root -g").toString().trim(), "playwright"));

const idioma = process.argv[2] || "es";
const pagina = process.argv[3] || "animacion";
const raiz = path.resolve(__dirname, "..");
const FPS = 30, LADO = 1080;
const tipos = { ".html": "text/html", ".woff2": "font/woff2", ".svg": "image/svg+xml", ".css": "text/css", ".js": "text/javascript", ".png": "image/png" };

const servidor = http.createServer((req, res) => {
  const f = path.join(raiz, decodeURIComponent(new URL(req.url, "http://x").pathname));
  if (!f.startsWith(raiz) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "Content-Type": tipos[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});

(async () => {
  await new Promise(r => servidor.listen(0, "127.0.0.1", r));
  const puerto = servidor.address().port;
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "animacion-"));
  const wav = path.join(tmp, "sonido.wav"), mp4 = path.join(__dirname, pagina === "animacion" ? `vibe-responsable.${idioma}.mp4` : `vibe-responsable-${pagina}.${idioma}.mp4`);
  const nav = await chromium.launch();
  try {
    const pag = await nav.newPage({ viewport: { width: LADO, height: LADO } });
    await pag.goto(`http://127.0.0.1:${puerto}/animacion/${pagina}.${idioma}.html?grabar`);
    await pag.evaluate(() => document.fonts.ready);
    const dur = await pag.evaluate(() => window.DURACION);
    fs.writeFileSync(wav, Buffer.from(await pag.evaluate(() => window.audioWav()), "base64"));
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-i", "-", "-i", wav,
      "-c:v", "libx264", "-preset", "slow", "-crf", "22", "-pix_fmt", "yuv420p", "-tune", "animation",
      "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", mp4], { stdio: ["pipe", "inherit", "inherit"] });
    const fin = new Promise((ok, mal) => ff.on("close", c => c ? mal(new Error("ffmpeg " + c)) : ok()));
    const n = Math.round(dur * FPS);
    for (let i = 0; i <= n; i++) {
      await pag.evaluate(s => window.fijar(s), i / FPS);
      const img = await pag.screenshot({ type: "png", clip: { x: 0, y: 0, width: LADO, height: LADO } });
      if (!ff.stdin.write(img)) await new Promise(r => ff.stdin.once("drain", r));
      if (i % (FPS * 10) === 0) process.stdout.write(`${Math.round(i / FPS)} s de ${Math.round(dur)}\n`);
    }
    ff.stdin.end(); await fin;
    console.log(`${path.relative(raiz, mp4)}: ${(fs.statSync(mp4).size / 1e6).toFixed(1)} MB, ${dur} s`);
  } finally {
    await nav.close(); servidor.close(); fs.rmSync(tmp, { recursive: true, force: true });
  }
})();
