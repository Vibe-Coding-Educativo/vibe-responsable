#!/usr/bin/env python3
"""Genera la web estática de la guía a partir del Markdown de contenido/.

Uso: python3 construir.py
Necesita pandoc. No hay dependencias en el lado del navegador: el resultado es
HTML, una hoja de estilos y un script pequeño, todo dentro del repositorio.
Decisión registrada en docs/adr/0004.
"""
import html, re, subprocess
from pathlib import Path

RAIZ = Path(__file__).parent
IDIOMAS = ["es"]                      # se amplía al añadir contenido/<idioma>/
URL_SITIO = "https://vibe-coding-educativo.github.io/vibe-responsable/"
REPO = "https://github.com/Vibe-Coding-Educativo/vibe-responsable"
ICONOS = ["book-check", "shield-check", "creative-commons", "bot", "messages-square",
          "unplug", "accessibility", "quote", "notebook-pen", "download"]

UI = {
    "es": {
        "guia": "Guía para publicar materiales educativos creados con vibe coding",
        "saltar": "Saltar al contenido",
        "borrador": "Borrador. La guía está en elaboración: los capítulos que desarrollan cada recomendación y la lista preparada para la IA se publicarán en esta misma web.",
        "infografia_alt": "Infografía con las diez recomendaciones. Su contenido es el de la lista que aparece a continuación.",
        "infografia_pie": "Las diez recomendaciones, de un vistazo. La imagen se amplía al pulsarla.",
        "indice": "Las diez recomendaciones",
        "cumple": "Se cumple",
        "resultado_titulo": "Resultado de la revisión",
        "resultado_ayuda": "Las marcas se guardan solo en este navegador. No se envía nada a ningún servidor.",
        "resultado_de": "{n} de {total} recomendaciones cumplidas",
        "copiar": "Copiar el resultado",
        "copiado": "Copiado",
        "borrar": "Borrar las marcas",
        "copia_cabecera": "Revisión con la lista «Antes de publicar: diez recomendaciones»",
        "cerrar": "Cerrar la imagen ampliada",
        "niveles": {"Lo mínimo.": "minimo", "Lo recomendado.": "recomendado", "En todos los casos.": "todos"},
        "pie_licencias": 'Código bajo <a href="https://www.gnu.org/licenses/agpl-3.0.html">AGPL v3</a> · Contenidos bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">CC BY-SA 4.0</a>',
        "pie_iconos": 'Iconos de <a href="https://lucide.dev/">Lucide</a> (licencia ISC)',
        "pie_codigo": "Código fuente y registro de decisiones",
    },
}


def pandoc(md):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def enlaces_externos(h):
    """Los enlaces externos no cambian de pestaña; solo se marcan para los estilos."""
    return re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener"', h)


def icono(nombre):
    s = (RAIZ / "infografia" / "iconos" / f"{nombre}.svg").read_text(encoding="utf-8")
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    trazos = re.search(r"<svg[^>]*>(.*)</svg>", s, flags=re.S).group(1).strip()
    return ('<svg class="icono" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            f"{trazos}</svg>")


def leer(idioma):
    md = (RAIZ / "contenido" / idioma / "00-lista.md").read_text(encoding="utf-8")
    titulo = re.match(r"#\s+(.*)", md).group(1).strip()
    cuerpo = md.split("\n", 1)[1]
    partes = re.split(r"^## ", cuerpo, flags=re.M)
    intro, brutas = partes[0].strip(), partes[1:]
    secciones, cierre = [], ""
    for k, b in enumerate(brutas):
        cab, resto = b.split("\n", 1)
        m = re.match(r"(\d+)\\?\.\s+(.*)", cab.strip())
        if k == len(brutas) - 1:                      # lo que sigue a la última lista es el cierre
            lineas = resto.rstrip().split("\n")
            ult = max(i for i, l in enumerate(lineas) if l.startswith("- "))
            resto, cierre = "\n".join(lineas[:ult + 1]), "\n".join(lineas[ult + 1:]).strip()
        secciones.append((int(m.group(1)), m.group(2).strip(), resto.strip()))
    return titulo, intro, secciones, cierre


def pagina(idioma):
    T = UI[idioma]
    titulo, intro, secciones, cierre = leer(idioma)
    total = len(secciones)

    # Introducción, con la infografía y el índice tras el párrafo que presenta la lista
    h_intro = enlaces_externos(pandoc(intro))
    figura = (f'<figure class="infografia"><a class="ampliar" href="../infografia/lista-iconos.{idioma}.png">'
              f'<img src="../infografia/lista-iconos.{idioma}.png" width="1080" height="1820" loading="lazy" alt="{html.escape(T["infografia_alt"])}"></a>'
              f'<figcaption>{html.escape(T["infografia_pie"])}</figcaption></figure>')
    indice = (f'<nav class="indice" aria-labelledby="t-indice"><h2 id="t-indice">{html.escape(T["indice"])}</h2><ol>'
              + "".join(f'<li><a href="#recomendacion-{n}">{html.escape(t)}</a></li>' for n, t, _ in secciones)
              + "</ol></nav>")
    vista = f'<div class="vista-rapida">{figura}{indice}</div>'
    parrafos = h_intro.split("\n")
    pos = next((i for i, p in enumerate(parrafos) if "diez recomendaciones de la guía" in p), None)
    if pos is None:
        h_intro = h_intro + vista
    else:
        parrafos.insert(pos + 1, vista)
        h_intro = "\n".join(parrafos)

    # Recomendaciones
    h_secs = []
    for (n, t, cuerpo), ic in zip(secciones, ICONOS):
        h = enlaces_externos(pandoc(cuerpo))
        for etiqueta, clase in T["niveles"].items():
            h = h.replace(f"<li><strong>{etiqueta}</strong>", f'<li class="nivel {clase}"><strong>{etiqueta}</strong>')
        h = h.replace("<ul>", '<ul class="niveles">', 1)
        h_secs.append(
            f'<section class="recomendacion" id="recomendacion-{n}" aria-labelledby="t-{n}">'
            f'<header><span class="numero" aria-hidden="true">{n}</span><span class="insignia">{icono(ic)}</span>'
            f'<h2 id="t-{n}"><span class="oculto">{n}. </span>{html.escape(t)}</h2></header>'
            f'{h}'
            f'<label class="cumple"><input type="checkbox" data-punto="{n}" data-texto="{html.escape(t)}"> {html.escape(T["cumple"])}</label>'
            f'</section>')

    resultado = (f'<section class="resultado" aria-labelledby="t-res" hidden>'
                 f'<h2 id="t-res">{html.escape(T["resultado_titulo"])}</h2>'
                 f'<p class="cuenta" aria-live="polite" data-plantilla="{html.escape(T["resultado_de"])}" data-total="{total}"></p>'
                 f'<p class="ayuda">{html.escape(T["resultado_ayuda"])}</p>'
                 f'<div class="botones"><button type="button" id="copiar" data-hecho="{html.escape(T["copiado"])}" '
                 f'data-cabecera="{html.escape(T["copia_cabecera"])}" data-url="{URL_SITIO}">{html.escape(T["copiar"])}</button>'
                 f'<button type="button" id="borrar" class="secundario">{html.escape(T["borrar"])}</button></div></section>')

    h_cierre = enlaces_externos(pandoc(cierre)) if cierre else ""

    return f"""<!DOCTYPE html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} · {html.escape(T["guia"])}</title>
<meta name="description" content="{html.escape(T["guia"])}. {html.escape(titulo)}.">
<meta name="author" content="Juan José de Haro">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{html.escape(T["guia"])}">
<meta property="og:image" content="{URL_SITIO}infografia/lista-iconos.{idioma}.png">
<meta property="og:type" content="article">
<link rel="stylesheet" href="../recursos/estilos.css">
<script src="../recursos/guia.js" defer></script>
</head>
<body>
<a class="saltar" href="#contenido">{html.escape(T["saltar"])}</a>
<header class="cabecera">
<div class="ancho">
<p class="guia">{html.escape(T["guia"])}</p>
<h1>{html.escape(titulo)}</h1>
</div>
</header>
<main id="contenido" class="ancho">
<p class="borrador" role="note">{html.escape(T["borrador"])}</p>
<div class="intro">
{h_intro}
</div>
{"".join(h_secs)}
{resultado}
<div class="cierre">
{h_cierre}
</div>
</main>
<footer class="pie">
<div class="ancho">
<p>© 2026 <a href="https://bilateria.org">Juan José de Haro</a> · {T["pie_licencias"]}</p>
<p>{T["pie_iconos"]} · <a href="{REPO}">{html.escape(T["pie_codigo"])}</a></p>
</div>
</footer>
<dialog class="lightbox" aria-label="{html.escape(T["infografia_alt"])}">
<button type="button" class="cerrar" aria-label="{html.escape(T["cerrar"])}">×</button>
<img alt="{html.escape(T["infografia_alt"])}">
</dialog>
</body>
</html>
"""


def portada():
    """La raíz envía al idioma del navegador si existe, y si no al castellano."""
    disponibles = ",".join(f'"{i}"' for i in IDIOMAS)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(UI["es"]["guia"])}</title>
<meta http-equiv="refresh" content="0; url=es/">
<link rel="canonical" href="{URL_SITIO}es/">
<script>
var d=[{disponibles}],n=(navigator.languages||[navigator.language||"es"]).map(function(x){{return x.slice(0,2);}});
var e=n.filter(function(x){{return d.indexOf(x)>-1;}})[0]||"es";location.replace(e+"/");
</script>
</head>
<body><p><a href="es/">{html.escape(UI["es"]["guia"])}</a></p></body>
</html>
"""


if __name__ == "__main__":
    for idioma in IDIOMAS:
        destino = RAIZ / idioma
        destino.mkdir(exist_ok=True)
        (destino / "index.html").write_text(pagina(idioma), encoding="utf-8")
        print("generado", destino / "index.html")
    (RAIZ / "index.html").write_text(portada(), encoding="utf-8")
    (RAIZ / ".nojekyll").write_text("", encoding="utf-8")
    print("generado index.html")
