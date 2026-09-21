#!/usr/bin/env python3
"""Genera la infografía de las diez recomendaciones en SVG (original editable).

Uso: python3 generar.py [idioma]      -> lista-iconos.<idioma>.svg
Los textos están en TEXTOS; para otro idioma basta con añadir su bloque.
Los iconos son de Lucide (licencia ISC) y están en iconos/.
"""
import re, sys, textwrap, html
from pathlib import Path

AQUI = Path(__file__).parent
ANCHO = 1080
CREMA, PIZARRA, VERDE, NARANJA, BLANCO, GRIS = "#f7f4ee", "#1f2a37", "#0f766e", "#c2410c", "#ffffff", "#5b6472"

TEXTOS = {
    "es": {
        "titulo": ["Antes de publicar:", "diez recomendaciones"],
        "subtitulo": "Materiales educativos creados con vibe coding",
        "esencial": "Lo esencial",
        "recomendable": "Y además",
        "puntos": [
            ("book-check", "El contenido es correcto y lo ha revisado una persona"),
            ("shield-check", "No recoge datos personales, o los datos no salen del dispositivo"),
            ("creative-commons", "Lleva una licencia libre a la vista"),
            ("bot", "Indica que se ha hecho con IA y qué ha comprobado la persona"),
            ("messages-square", "Se puede explicar qué hace en dos frases"),
            ("unplug", "No depende de servicios que pueden desaparecer"),
            ("accessibility", "Puede usarse con teclado, con lector de pantalla y en un móvil"),
            ("quote", "Acredita lo que toma de otras personas"),
            ("notebook-pen", "Conserva el rastro de cómo se hizo"),
            ("download", "Otra persona puede descargarlo, modificarlo y mejorarlo"),
        ],
        "pie1": "jjdeharo · CC BY-SA 4.0",
        "pie2": "vibe-coding-educativo.github.io/vibe-responsable",
        "pie3": "Iconos: Lucide (licencia ISC) · Maquetación generada con IA y revisada por el autor",
        "pie3_ilustrada": "Ilustraciones generadas con IA · Maquetación generada con IA y revisada por el autor",
        "desc": "Infografía con las diez recomendaciones para publicar de forma responsable materiales educativos creados con vibe coding.",
    },
}

def icono(nombre):
    """Devuelve los trazos interiores del SVG de Lucide."""
    s = (AQUI / "iconos" / f"{nombre}.svg").read_text(encoding="utf-8")
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    return re.search(r"<svg[^>]*>(.*)</svg>", s, flags=re.S).group(1).strip()

def generar(idioma="es"):
    T = TEXTOS[idioma]
    y = 0
    out = []
    # Cabecera
    alto_cab = 330
    out.append(f'<rect x="0" y="0" width="{ANCHO}" height="{alto_cab}" fill="{PIZARRA}"/>')
    out.append(f'<text x="70" y="125" font-size="68" font-weight="800" fill="{BLANCO}">{html.escape(T["titulo"][0])}</text>')
    out.append(f'<text x="70" y="205" font-size="68" font-weight="800" fill="{BLANCO}">{html.escape(T["titulo"][1])}</text>')
    out.append(f'<text x="70" y="272" font-size="34" font-weight="500" fill="#d6dde6">{html.escape(T["subtitulo"])}</text>')
    y = alto_cab + 30

    def banda(texto, color):
        nonlocal y
        out.append(f'<rect x="70" y="{y}" width="{ANCHO-140}" height="52" rx="26" fill="{color}"/>')
        out.append(f'<text x="{ANCHO/2}" y="{y+36}" font-size="28" font-weight="700" fill="{BLANCO}" text-anchor="middle" letter-spacing="1.5">{html.escape(texto.upper())}</text>')
        y += 52 + 22

    ALTO_FILA = 128
    for i, (ic, texto) in enumerate(T["puntos"], start=1):
        if i == 1: banda(T["esencial"], NARANJA)
        if i == 4:
            y += 10
            banda(T["recomendable"], VERDE)
        color = NARANJA if i <= 3 else VERDE
        # tarjeta
        out.append(f'<rect x="70" y="{y}" width="{ANCHO-140}" height="{ALTO_FILA-16}" rx="20" fill="{BLANCO}" stroke="#e4ded2" stroke-width="2"/>')
        # número
        out.append(f'<text x="128" y="{y+76}" font-size="58" font-weight="800" fill="{color}" text-anchor="middle">{i}</text>')
        # icono
        out.append(f'<rect x="186" y="{y+16}" width="80" height="80" rx="18" fill="{color}"/>')
        out.append(f'<g transform="translate(198 {y+28}) scale(2.3333)" fill="none" stroke="{BLANCO}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icono(ic)}</g>')
        # texto (una o dos líneas)
        lineas = textwrap.wrap(texto, width=41)
        if len(lineas) == 1:
            out.append(f'<text x="296" y="{y+68}" font-size="33" font-weight="600" fill="{PIZARRA}">{html.escape(lineas[0])}</text>')
        else:
            out.append(f'<text x="296" y="{y+48}" font-size="33" font-weight="600" fill="{PIZARRA}">{html.escape(lineas[0])}</text>')
            out.append(f'<text x="296" y="{y+90}" font-size="33" font-weight="600" fill="{PIZARRA}">{html.escape(" ".join(lineas[1:]))}</text>')
        y += ALTO_FILA

    # Pie
    y += 14
    out.append(f'<line x1="70" y1="{y}" x2="{ANCHO-70}" y2="{y}" stroke="#d9d2c3" stroke-width="2"/>')
    out.append(f'<text x="70" y="{y+52}" font-size="30" font-weight="700" fill="{PIZARRA}">{html.escape(T["pie1"])}</text>')
    out.append(f'<text x="70" y="{y+94}" font-size="27" font-weight="600" fill="{VERDE}">{html.escape(T["pie2"])}</text>')
    out.append(f'<text x="70" y="{y+134}" font-size="22" fill="{GRIS}">{html.escape(T["pie3"])}</text>')
    alto = y + 166

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto}" width="{ANCHO}" height="{alto}" '
           f'font-family="Inter, \'Open Sans\', Arial, sans-serif" role="img" aria-labelledby="t d" lang="{idioma}">\n'
           f'<title id="t">{html.escape(" ".join(T["titulo"]))}</title>\n<desc id="d">{html.escape(T["desc"])}</desc>\n'
           f'<rect width="{ANCHO}" height="{alto}" fill="{CREMA}"/>\n' + "\n".join(out) + "\n</svg>\n")
    destino = AQUI / f"lista-iconos.{idioma}.svg"
    destino.write_text(svg, encoding="utf-8")
    return destino, alto

def generar_ilustrada(idioma="es"):
    """Misma lista, con las ilustraciones generadas por IA (codex/01.png … 10.png)."""
    T = TEXTOS[idioma]
    out, defs = [], []
    alto_cab = 330
    out.append(f'<rect x="0" y="0" width="{ANCHO}" height="{alto_cab}" fill="{PIZARRA}"/>')
    out.append(f'<text x="70" y="125" font-size="68" font-weight="800" fill="{BLANCO}">{html.escape(T["titulo"][0])}</text>')
    out.append(f'<text x="70" y="205" font-size="68" font-weight="800" fill="{BLANCO}">{html.escape(T["titulo"][1])}</text>')
    out.append(f'<text x="70" y="272" font-size="34" font-weight="500" fill="#d6dde6">{html.escape(T["subtitulo"])}</text>')
    y = alto_cab + 30
    LADO, ALTO_FILA = 148, 180

    def banda(texto, color):
        nonlocal y
        out.append(f'<rect x="70" y="{y}" width="{ANCHO-140}" height="52" rx="26" fill="{color}"/>')
        out.append(f'<text x="{ANCHO/2}" y="{y+36}" font-size="28" font-weight="700" fill="{BLANCO}" text-anchor="middle" letter-spacing="1.5">{html.escape(texto.upper())}</text>')
        y += 52 + 22

    for i, (_, texto) in enumerate(T["puntos"], start=1):
        if i == 1: banda(T["esencial"], NARANJA)
        if i == 4:
            y += 10
            banda(T["recomendable"], VERDE)
        color = NARANJA if i <= 3 else VERDE
        out.append(f'<rect x="70" y="{y}" width="{ANCHO-140}" height="{ALTO_FILA-16}" rx="20" fill="{BLANCO}" stroke="#e4ded2" stroke-width="2"/>')
        defs.append(f'<clipPath id="c{i}"><rect x="78" y="{y+8}" width="{LADO}" height="{LADO}" rx="14"/></clipPath>')
        out.append(f'<image href="codex/{i:02d}.png" x="78" y="{y+8}" width="{LADO}" height="{LADO}" clip-path="url(#c{i})" preserveAspectRatio="xMidYMid slice"/>')
        out.append(f'<circle cx="276" cy="{y+82}" r="30" fill="{color}"/>')
        out.append(f'<text x="276" y="{y+95}" font-size="36" font-weight="800" fill="{BLANCO}" text-anchor="middle">{i}</text>')
        lineas = textwrap.wrap(texto, width=36)
        y0 = y + 94 - (len(lineas)-1)*21
        for k, l in enumerate(lineas):
            out.append(f'<text x="326" y="{y0+k*42}" font-size="33" font-weight="600" fill="{PIZARRA}">{html.escape(l)}</text>')
        y += ALTO_FILA

    y += 14
    out.append(f'<line x1="70" y1="{y}" x2="{ANCHO-70}" y2="{y}" stroke="#d9d2c3" stroke-width="2"/>')
    out.append(f'<text x="70" y="{y+52}" font-size="30" font-weight="700" fill="{PIZARRA}">{html.escape(T["pie1"])}</text>')
    out.append(f'<text x="70" y="{y+94}" font-size="27" font-weight="600" fill="{VERDE}">{html.escape(T["pie2"])}</text>')
    out.append(f'<text x="70" y="{y+134}" font-size="22" fill="{GRIS}">{html.escape(T["pie3_ilustrada"])}</text>')
    alto = y + 166
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto}" width="{ANCHO}" height="{alto}" '
           f'font-family="Inter, \'Open Sans\', Arial, sans-serif" role="img" aria-labelledby="t d" lang="{idioma}">\n'
           f'<title id="t">{html.escape(" ".join(T["titulo"]))}</title>\n<desc id="d">{html.escape(T["desc"])}</desc>\n'
           f'<defs>{"".join(defs)}</defs>\n<rect width="{ANCHO}" height="{alto}" fill="{CREMA}"/>\n' + "\n".join(out) + "\n</svg>\n")
    destino = AQUI / f"lista-ilustrada.{idioma}.svg"
    destino.write_text(svg, encoding="utf-8")
    return destino, alto

if __name__ == "__main__":
    idioma = sys.argv[1] if len(sys.argv) > 1 else "es"
    d, alto = generar(idioma)
    print(d.name, f"{ANCHO}x{alto}")
    if (AQUI / "codex" / "01.png").exists():
        d, alto = generar_ilustrada(idioma)
        print(d.name, f"{ANCHO}x{alto}")
