#!/usr/bin/env python3
"""Genera la infografía de las diez recomendaciones en SVG (original editable).

Uso: python3 generar.py [idioma]      -> lista-iconos.<idioma>.svg
Los textos están en TEXTOS; para otro idioma basta con añadir su bloque.
Los iconos son de Lucide (licencia ISC; los derivados de Feather, MIT) y están en
iconos/, con el texto de las licencias en iconos/LICENSE.
"""
import re, sys, html
from pathlib import Path

AQUI = Path(__file__).parent
ANCHO = 1080
# Misma paleta y tipografía que la web (recursos/estilos.css)
PAPEL, PIZARRA, TINTA, VERDE, BLANCO, GRIS, RAYA = "#fbfbf8", "#17453b", "#16232b", "#0f766e", "#ffffff", "#4d5b63", "#dde3df"

TEXTOS = {
    "es": {
        "titulo": ["Antes de publicar:", "diez recomendaciones"],
        "subtitulo": "Vibe coding responsable · Materiales educativos",
        "puntos": [
            ("book-check", "Revisar el contenido sin delegarlo en la IA"),
            ("shield-check", "No enviar datos personales a servicios ajenos al centro"),
            ("messages-square", "Entender qué hace el material"),
            ("unplug", "No depender de servicios que pueden desaparecer"),
            ("accessibility", "Hacerlo accesible a cualquier persona"),
            ("quote", "Citar la autoría de lo que se toma de otras personas"),
            ("notebook-pen", "Guardar el rastro de cómo se hizo"),
            ("bot", "Declarar el uso de IA y lo que se ha comprobado"),
            ("creative-commons", "Publicar con una licencia libre a la vista"),
            ("download", "Ofrecer el código para que otras personas lo adapten"),
        ],
        # Las fases de la vida del material: el número de la primera recomendación de cada una.
        # Nombran lo que se hace, no la importancia: las diez tienen el mismo rango.
        "grupos": {1: "Proteger al alumnado", 3: "Construir el material",
                   6: "Documentar el trabajo", 9: "Compartir el material"},
        "pie1": "@jjdeharo, CC BY-SA 4.0",
        "pie2": "vibe-coding-educativo.github.io/vibe-responsable",
        "pie3": ["Iconos: Lucide (ISC y MIT). Tipografía: Atkinson Hyperlegible (OFL).", "Maquetación generada con IA y revisada por el autor."],
        "desc": "Infografía con las diez recomendaciones para publicar de forma responsable materiales educativos creados con vibe coding, agrupadas en cuatro fases: proteger al alumnado, construir el material, documentar el trabajo y compartir el material.",
    },
}


ATONAS = {"a", "al", "con", "de", "del", "el", "en", "la", "las", "lo", "los", "o", "para", "por",
          "que", "se", "sin", "su", "un", "una", "y"}


def partir(texto, cabe=45):
    """Una línea si cabe; si no, dos líneas lo más parecidas posible, para no dejar
    una palabra sola en la segunda (caben unos 45 caracteres a 33 px entre el icono y el borde)."""
    if len(texto) <= cabe:
        return [texto]
    palabras = texto.split()
    cortes = [(" ".join(palabras[:i]), " ".join(palabras[i:])) for i in range(1, len(palabras))]
    validos = [c for c in cortes if len(c[0]) <= cabe and len(c[1]) <= cabe]
    # Una línea no termina en una palabra átona (artículo, preposición, conjunción, pronombre)
    buenos = [c for c in validos if c[0].split()[-1].lower() not in ATONAS] or validos
    return list(min(buenos, key=lambda c: abs(len(c[0]) - len(c[1]))))

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
    out.append(f'<text x="70" y="125" font-size="68" font-weight="700" fill="{BLANCO}">{html.escape(T["titulo"][0])}</text>')
    out.append(f'<text x="70" y="205" font-size="68" font-weight="700" fill="{BLANCO}">{html.escape(T["titulo"][1])}</text>')
    out.append(f'<text x="70" y="272" font-size="34" font-weight="400" fill="#bcd2c9">{html.escape(T["subtitulo"])}</text>')
    y = alto_cab + 30

    ALTO_FILA = 128
    DX = 102            # margen izquierdo para las fases en vertical
    SEP = 26           # separación entre fases
    tramos = []        # (y inicial, y final, rótulo) de cada fase
    for i, (ic, texto) in enumerate(T["puntos"], start=1):
        color = VERDE
        if i in T["grupos"]:
            if i > 1:
                y += SEP
            tramos.append([y, None, T["grupos"][i]])
        x0 = 70 + DX
        out.append(f'<rect x="{x0}" y="{y}" width="{ANCHO-140-DX}" height="{ALTO_FILA-16}" rx="20" fill="{BLANCO}" stroke="{RAYA}" stroke-width="2"/>')
        out.append(f'<text x="{128+DX}" y="{y+76}" font-size="58" font-weight="700" fill="{color}" text-anchor="middle">{i}</text>')
        out.append(f'<rect x="{186+DX}" y="{y+16}" width="80" height="80" rx="18" fill="{color}"/>')
        out.append(f'<g transform="translate({198+DX} {y+28}) scale(2.3333)" fill="none" stroke="{BLANCO}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icono(ic)}</g>')
        lineas = partir(texto, 40)
        xt = 296 + DX
        if len(lineas) == 1:
            out.append(f'<text x="{xt}" y="{y+68}" font-size="33" font-weight="400" fill="{TINTA}">{html.escape(lineas[0])}</text>')
        else:
            out.append(f'<text x="{xt}" y="{y+48}" font-size="33" font-weight="400" fill="{TINTA}">{html.escape(lineas[0])}</text>')
            out.append(f'<text x="{xt}" y="{y+90}" font-size="33" font-weight="400" fill="{TINTA}">{html.escape(" ".join(lineas[1:]))}</text>')
        y += ALTO_FILA
        tramos[-1][1] = y - 16
    # Fases en vertical, leídas de abajo arriba, con una llave que abarca sus tarjetas
    for y0, y1, rotulo in tramos:
        xl = 70 + DX - 22
        out.append(f'<path d="M{xl+12} {y0} H{xl} V{y1} H{xl+12}" fill="none" stroke="{VERDE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
        verbo, _, resto = rotulo.upper().partition(" ")
        cy = (y0 + y1) / 2
        for k, linea in enumerate((verbo, resto)):
            xk = 70 + 27 + k * 40
            out.append(f'<text transform="translate({xk} {cy:.0f}) rotate(-90)" font-size="31" font-weight="700" letter-spacing="1.8" fill="{VERDE}" text-anchor="middle">{html.escape(linea)}</text>')

    # Pie
    y += 14
    out.append(f'<line x1="70" y1="{y}" x2="{ANCHO-70}" y2="{y}" stroke="{RAYA}" stroke-width="2"/>')
    out.append(f'<text x="70" y="{y+52}" font-size="30" font-weight="700" fill="{TINTA}">{html.escape(T["pie1"])}</text>')
    out.append(f'<text x="70" y="{y+94}" font-size="27" font-weight="400" fill="{VERDE}">{html.escape(T["pie2"])}</text>')
    for k, linea in enumerate(T["pie3"]):
        out.append(f'<text x="70" y="{y+134+k*30}" font-size="22" fill="{GRIS}">{html.escape(linea)}</text>')
    alto = y + 166 + 30 * (len(T["pie3"]) - 1)

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto}" width="{ANCHO}" height="{alto}" '
           f'font-family="\'Atkinson Hyperlegible\', Inter, Arial, sans-serif" role="img" aria-labelledby="t d" lang="{idioma}">\n'
           f'<title id="t">{html.escape(" ".join(T["titulo"]))}</title>\n<desc id="d">{html.escape(T["desc"])}</desc>\n'
           f'<rect width="{ANCHO}" height="{alto}" fill="{PAPEL}"/>\n' + "\n".join(out) + "\n</svg>\n")
    destino = AQUI / f"lista-iconos.{idioma}.svg"
    destino.write_text(svg, encoding="utf-8")
    return destino, alto

if __name__ == "__main__":
    idioma = sys.argv[1] if len(sys.argv) > 1 else "es"
    d, alto = generar(idioma)
    print(d.name, f"{ANCHO}x{alto}")
