#!/usr/bin/env python3
"""Genera la web estática de la guía a partir del Markdown de contenido/.

Uso: python3 construir.py
Necesita pandoc. No hay dependencias en el lado del navegador: el resultado es
HTML, una hoja de estilos, un script pequeño y la tipografía, todo dentro del
repositorio. Decisiones registradas en docs/adr/0004 y 0005.

Páginas por idioma:
  index.html          la lista de diez recomendaciones (00-lista.md)
  presentacion.html   qué es, por qué y cómo se utiliza (01-presentacion.md)
  herramientas.html   familias de herramientas y los dos niveles (02-herramientas.md)
"""
import html, re, subprocess, unicodedata
from pathlib import Path

RAIZ = Path(__file__).parent
IDIOMAS = ["es"]                      # se amplía al añadir contenido/<idioma>/
URL_SITIO = "https://vibe-coding-educativo.github.io/vibe-responsable/"
REPO = "https://github.com/Vibe-Coding-Educativo/vibe-responsable"
COMUNIDAD = "https://vibe-coding-educativo.github.io/"   # mismo dominio: se abre en la misma pestaña
ICONOS = ["book-check", "shield-check", "creative-commons", "bot", "messages-square",
          "unplug", "accessibility", "quote", "notebook-pen", "download"]

UI = {
    "es": {
        "guia": "Guía para publicar materiales educativos creados con vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Saltar al contenido",
        "nav": "Secciones de la guía",
        "nav_lista": "Recomendaciones",
        "borrador": "Borrador",
        "borrador_ayuda": "La guía está en elaboración. Los capítulos que desarrollan cada recomendación y la lista preparada para la IA se publicarán en esta misma web.",
        "col_recomendacion": "Recomendación",
        "cumple": "Se cumple",
        "cumple_punto": "Se cumple la recomendación {n}",
        "infografia_titulo": "Resumen gráfico",
        "infografia_texto": "La infografía reúne las diez recomendaciones en una sola imagen, pensada para compartirla.",
        "infografia_pista": "Al seleccionar una recomendación de la lista, su explicación se muestra en este espacio.",
        "infografia_alt": "Infografía con las diez recomendaciones, las mismas que aparecen en la lista.",
        "ampliar": "Ampliar la infografía",
        "descargar": "Descargar la imagen",
        "volver": "Volver al resumen gráfico",
        "anterior": "Anterior",
        "siguiente": "Siguiente",
        "niveles_ayuda": "Qué significan «Lo mínimo» y «Lo recomendado»",
        "resultado_de": "{n} de {total} cumplidas",
        "resultado_ayuda": "Las marcas se guardan solo en este navegador. No se envía nada a ningún servidor.",
        "copiar": "Copiar el resultado",
        "copiado": "Resultado copiado",
        "borrar": "Borrar las marcas",
        "copia_cabecera": "Revisión con la lista «Antes de publicar: diez recomendaciones»",
        "cerrar": "Cerrar",
        "acercar": "Ver a tamaño de lectura",
        "alejar": "Ajustar a la pantalla",
        "nueva_pestana": "(se abre en una pestaña nueva)",
        "niveles": {"Lo mínimo.": "minimo", "Lo recomendado.": "recomendado", "En todos los casos.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Código bajo <a href="https://www.gnu.org/licenses/agpl-3.0.html">AGPL v3</a> y contenidos bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">CC BY-SA 4.0</a>.',
        "pie_2": 'Iconos de <a href="https://lucide.dev/">Lucide</a> (licencia ISC). Tipografía <a href="https://www.brailleinstitute.org/freefont/">Atkinson Hyperlegible</a> (licencia OFL). <a href="{repo}">Código fuente y registro de decisiones</a>.',
    },
}
PAGINAS = [("index.html", "00-lista.md"), ("presentacion.html", "01-presentacion.md"), ("herramientas.html", "02-herramientas.md")]


def pandoc(md):
    r = subprocess.run(["pandoc", "-f", "markdown-auto_identifiers", "-t", "html5", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def ancla(texto):
    s = unicodedata.normalize("NFD", texto.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def enlaces_externos(h, aviso):
    """Los enlaces a otras webs se abren en una pestaña nueva, y se avisa de ello a los lectores de pantalla."""
    h = re.sub(r'<a href="(https?://(?!vibe-coding-educativo\.github\.io/)[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    return re.sub(r'(<a href="https?://[^"]+" target="_blank" rel="noopener"[^>]*>)(.*?)</a>',
                  lambda m: f'{m.group(1)}{m.group(2)}<span class="oculto"> {aviso}</span></a>', h, flags=re.S)


def icono(nombre):
    s = (RAIZ / "infografia" / "iconos" / f"{nombre}.svg").read_text(encoding="utf-8")
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    trazos = re.search(r"<svg[^>]*>(.*)</svg>", s, flags=re.S).group(1).strip()
    return ('<svg class="icono" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" '
            'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
            f"{trazos}</svg>")


def titulo_de(md):
    return re.match(r"#\s+(.*)", md).group(1).strip()


def marco(idioma, archivo, titulo, cuerpo, clase):
    """Cabecera, navegación y pie comunes a todas las páginas."""
    T = UI[idioma]
    titulos = {a: titulo_de((RAIZ / "contenido" / idioma / m).read_text(encoding="utf-8")) for a, m in PAGINAS}
    nav = []
    for a, _ in PAGINAS:
        rotulo = T["nav_lista"] if a == "index.html" else titulos[a]
        destino = "./" if a == "index.html" else a
        actual = ' aria-current="page"' if a == archivo else ""
        nav.append(f'<li><a href="{destino}"{actual}>{html.escape(rotulo)}</a></li>')
    pag = f"""<!DOCTYPE html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} | {html.escape(T["guia"])}</title>
<meta name="description" content="{html.escape(T["guia"])}. {html.escape(titulo)}.">
<meta name="author" content="Juan José de Haro">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
<meta property="og:title" content="{html.escape(titulos["index.html"])}">
<meta property="og:description" content="{html.escape(T["guia"])}">
<meta property="og:image" content="{URL_SITIO}infografia/lista-iconos.{idioma}.png">
<meta property="og:type" content="article">
<link rel="preload" href="../recursos/fuentes/atkinson-hyperlegible-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../recursos/estilos.css">
<script src="../recursos/guia.js" defer></script>
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">{html.escape(T["saltar"])}</a>
<header class="pizarra">
<div class="ancho pizarra-int">
<p class="sitio"><a class="sitio-comunidad" href="{COMUNIDAD}">{html.escape(T["comunidad"])}</a>
<a class="sitio-guia" href="./">{html.escape(T["guia"])}</a>
<span class="estado" tabindex="0">{html.escape(T["borrador"])}<span class="globo">{html.escape(T["borrador_ayuda"])}</span></span></p>
<nav aria-label="{html.escape(T["nav"])}"><ul>{"".join(nav)}</ul></nav>
</div>
</header>
<main id="contenido" class="ancho">
{cuerpo}
</main>
<footer class="pie">
<div class="ancho">
<p>{T["pie_1"]}</p>
<p>{T["pie_2"].format(repo=REPO)}</p>
</div>
</footer>
</body>
</html>
"""
    return enlaces_externos(pag, T["nueva_pestana"])


def pagina_lista(idioma):
    T = UI[idioma]
    md = (RAIZ / "contenido" / idioma / "00-lista.md").read_text(encoding="utf-8")
    titulo = titulo_de(md)
    brutas = re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]
    puntos = []
    for b in brutas:
        cab, resto = b.split("\n", 1)
        m = re.match(r"(\d+)\\?\.\s+(.*)", cab.strip())
        puntos.append((int(m.group(1)), m.group(2).strip(), resto.strip()))
    total = len(puntos)

    filas = []
    for (n, t, cuerpo), ic in zip(puntos, ICONOS):
        h = pandoc(cuerpo)
        for etiqueta, clase in T["niveles"].items():
            h = h.replace(f"<li><strong>{etiqueta}</strong>", f'<li class="nivel {clase}"><strong>{etiqueta}</strong>')
        corte = h.find("<ul>")
        explicacion, niveles = h[:corte], h[corte:].replace("<ul>", '<ul class="niveles">', 1)
        ant = f'<button type="button" class="paso" data-ir="{n-1}">{html.escape(T["anterior"])}</button>' if n > 1 else "<span></span>"
        sig = f'<button type="button" class="paso" data-ir="{n+1}">{html.escape(T["siguiente"])}</button>' if n < total else "<span></span>"
        filas.append(
            f'<li class="punto" id="recomendacion-{n}">'
            f'<div class="fila"><a class="abrir" href="#detalle-{n}" aria-controls="detalle-{n}">'
            f'<span class="numero" aria-hidden="true">{n}</span>{icono(ic)}'
            f'<span class="rotulo"><span class="oculto">{n}. </span>{html.escape(t)}</span></a>'
            f'<label class="casilla" title="{html.escape(T["cumple"])}"><input type="checkbox" data-punto="{n}" data-texto="{html.escape(t)}">'
            f'<span class="oculto">{html.escape(T["cumple_punto"].format(n=n))}</span></label></div>'
            f'<article class="detalle" id="detalle-{n}" data-punto="{n}" aria-labelledby="t-{n}"><div class="detalle-int"><div class="detalle-caja">'
            f'<header class="detalle-cab"><span class="cifra" aria-hidden="true">{n}</span>'
            f'<h2 id="t-{n}" tabindex="-1"><span class="oculto">{n}. </span>{html.escape(t)}</h2>'
            f'<button type="button" class="cerrar-detalle solo-js" aria-label="{html.escape(T["volver"])}" title="{html.escape(T["volver"])}"><span aria-hidden="true">×</span></button></header>'
            f'<div class="detalle-cuerpo"><div class="explicacion">{explicacion}</div>{niveles}</div>'
            f'<footer class="detalle-pie solo-js">{ant}<a class="ayuda-niveles" href="herramientas.html#{ancla("Lo mínimo y lo recomendado")}">{html.escape(T["niveles_ayuda"])}</a>{sig}</footer>'
            f'</div></div></article></li>')

    img = f"../infografia/lista-iconos.{idioma}.png"
    # Las medidas salen del SVG original, para que el visor no dependa de un número escrito a mano
    svg = (RAIZ / "infografia" / f"lista-iconos.{idioma}.svg").read_text(encoding="utf-8")
    an, al = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg).groups()
    medidas = f'style="--ig-an:{an};--ig-al:{al}"'
    cuerpo = f"""<h1>{html.escape(titulo)}</h1>
<div class="tablero">
<section class="hoja" aria-label="{html.escape(titulo)}">
<div class="hoja-cab" aria-hidden="true"><span>{html.escape(T["col_recomendacion"])}</span><span>{html.escape(T["cumple"])}</span></div>
<ol class="diez">{"".join(filas)}</ol>
<div class="resultado solo-js">
<p class="cuenta" aria-live="polite" data-plantilla="{html.escape(T["resultado_de"])}" data-total="{total}" title="{html.escape(T["resultado_ayuda"])}"></p>
<button type="button" id="copiar" data-hecho="{html.escape(T["copiado"])}" data-cabecera="{html.escape(T["copia_cabecera"])}" data-url="{URL_SITIO}">{html.escape(T["copiar"])}</button>
<button type="button" id="borrar" class="discreto">{html.escape(T["borrar"])}</button>
</div>
</section>
<div class="panel" {medidas}>
<section class="resumen" aria-labelledby="t-resumen">
<a class="miniatura ampliar" href="{img}" aria-label="{html.escape(T["ampliar"])}"><img src="{img}" width="{an}" height="{al}" alt="{html.escape(T["infografia_alt"])}"></a>
<div class="resumen-texto">
<h2 id="t-resumen">{html.escape(T["infografia_titulo"])}</h2>
<p>{html.escape(T["infografia_texto"])}</p>
<p class="acciones"><a class="boton ampliar" href="{img}">{html.escape(T["ampliar"])}</a>
<a class="boton discreto" href="{img}" download>{html.escape(T["descargar"])}</a></p>
<p class="pista solo-js">{html.escape(T["infografia_pista"])}</p>
</div>
</section>
</div>
</div>
<dialog class="visor" {medidas} aria-label="{html.escape(T["infografia_titulo"])}">
<div class="visor-barra"><button type="button" class="visor-zoom" data-acercar="{html.escape(T["acercar"])}" data-alejar="{html.escape(T["alejar"])}">{html.escape(T["acercar"])}</button>
<button type="button" class="visor-cerrar">{html.escape(T["cerrar"])}</button></div>
<div class="visor-lienzo"><img alt="{html.escape(T["infografia_alt"])}" width="{an}" height="{al}"></div>
</dialog>"""
    return marco(idioma, "index.html", titulo, cuerpo, "pagina-lista")


def pagina_texto(idioma, archivo, fuente):
    md = (RAIZ / "contenido" / idioma / fuente).read_text(encoding="utf-8")
    titulo = titulo_de(md)
    apartados = re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]
    secciones = []
    for a in apartados:
        cab, resto = a.split("\n", 1)
        cab = cab.strip()
        h = pandoc(resto.strip())
        h = h.replace("<ul>", '<ul class="familias">', 1)
        secciones.append(f'<section class="apartado" id="{ancla(cab)}" aria-labelledby="h-{ancla(cab)}">'
                         f'<h2 id="h-{ancla(cab)}">{html.escape(cab)}</h2><div class="texto">{h}</div></section>')
    cuerpo = f'<h1>{html.escape(titulo)}</h1>\n' + "\n".join(secciones)
    return marco(idioma, archivo, titulo, cuerpo, "pagina-texto")


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
        (destino / "index.html").write_text(pagina_lista(idioma), encoding="utf-8")
        for archivo, fuente in PAGINAS[1:]:
            (destino / archivo).write_text(pagina_texto(idioma, archivo, fuente), encoding="utf-8")
        print("generado", idioma, [a for a, _ in PAGINAS])
    (RAIZ / "index.html").write_text(portada(), encoding="utf-8")
    (RAIZ / ".nojekyll").write_text("", encoding="utf-8")
