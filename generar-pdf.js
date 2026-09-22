#!/usr/bin/env node
// Imprime a PDF la guía completa: la página que construir.py deja en es/completo.html
// (portada, índice y todas las páginas seguidas). Lo llama `python3 construir.py --pdf`.
//
//   node generar-pdf.js es/completo.html es/vibe-responsable-es.pdf
//
// Usa el Chromium de Playwright, instalado de forma global (npm i -g playwright), y sirve
// el repositorio por HTTP en un puerto libre mientras dura la impresión, porque con
// file:// el navegador no carga la tipografía. El pie de cada página (texto y número)
// sale del atributo data-pie del <body>, para que los textos vivan solo en construir.py.
"use strict";
const fs = require("fs");
const http = require("http");
const path = require("path");
const { execSync } = require("child_process");

const [entrada, salida] = process.argv.slice(2);
if (!entrada || !salida) {
  console.error("Uso: node generar-pdf.js <entrada.html> <salida.pdf>");
  process.exit(1);
}
const raiz = path.resolve(__dirname);
const { chromium } = require(path.join(execSync("npm root -g").toString().trim(), "playwright"));

const tipos = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript",
  ".woff2": "font/woff2", ".png": "image/png", ".svg": "image/svg+xml", ".ico": "image/x-icon", ".pdf": "application/pdf" };

const servidor = http.createServer((req, res) => {
  let ruta = decodeURIComponent(req.url.split("?")[0]);
  if (ruta.endsWith("/")) { ruta += "index.html"; }
  const archivo = path.join(raiz, ruta);
  if (!archivo.startsWith(raiz) || !fs.existsSync(archivo) || fs.statSync(archivo).isDirectory()) {
    res.writeHead(404); res.end(); return;
  }
  res.writeHead(200, { "Content-Type": tipos[path.extname(archivo)] || "application/octet-stream" });
  fs.createReadStream(archivo).pipe(res);
});

servidor.listen(0, "127.0.0.1", async () => {
  const puerto = servidor.address().port;
  const navegador = await chromium.launch();
  try {
    const pagina = await navegador.newPage();
    await pagina.goto(`http://127.0.0.1:${puerto}/${entrada}`, { waitUntil: "networkidle" });
    await pagina.evaluate(() => document.fonts.ready);
    const pie = await pagina.evaluate(() => document.body.dataset.pie || "");
    const escapar = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    await pagina.pdf({
      path: salida, format: "A4", printBackground: true,
      margin: { top: "16mm", bottom: "18mm", left: "17mm", right: "17mm" },
      displayHeaderFooter: true,
      headerTemplate: "<span></span>",
      footerTemplate: `<div style="width:100%;margin:0 17mm;font-family:Arial,Helvetica,sans-serif;font-size:7.5px;color:#555;display:flex;justify-content:space-between;">`
        + `<span>${escapar(pie)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    });
    const kb = Math.round(fs.statSync(salida).size / 1024);
    console.log(`${salida}: ${kb} KB`);
  } finally {
    await navegador.close();
    servidor.close();
  }
});
