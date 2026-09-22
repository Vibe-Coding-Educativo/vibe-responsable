#!/usr/bin/env python3
"""Genera la web estática de la guía a partir del Markdown de contenido/.

Uso: python3 construir.py          genera la web
     python3 construir.py --pdf    además, la guía completa en PDF (necesita node y Playwright
                                   instalado de forma global, ver generar-pdf.js)
Necesita pandoc. No hay dependencias en el lado del navegador: el resultado es
HTML, una hoja de estilos, un script pequeño y la tipografía, todo dentro del
repositorio. Decisiones registradas en docs/adr/0004 y 0005.

Páginas por idioma, en el orden en que se leen:
  index.html          presentación: qué es, por qué y cómo se utiliza (00-presentacion.md)
  guia.html           la guía: las diez recomendaciones (01-guia.md)
  herramientas.html   familias de herramientas y los dos niveles (02-herramientas.md)
  para-la-ia.html     los textos para dar a la IA (04-para-la-ia.md)
  creditos.html       créditos y licencias, enlazada desde el pie (03-creditos.md)

Los capítulos que desarrollan cada recomendación están en contenido/<idioma>/capitulos/
y se publican como capitulo-N.html. Se enlazan desde su recomendación en la guía; los
que aún no están escritos no muestran enlace.
"""
import html, re, subprocess, sys, unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent
IDIOMAS = ["es"]                      # se amplía al añadir contenido/<idioma>/
URL_SITIO = "https://vibe-coding-educativo.github.io/vibe-responsable/"
REPO = "https://github.com/Vibe-Coding-Educativo/vibe-responsable"
COMUNIDAD = "https://vibe-coding-educativo.github.io/"   # mismo dominio: se abre en la misma pestaña
CLAVE_TEMA = "vibe-responsable:tema"   # única entrada en localStorage; la misma en recursos/guia.js
PDF = "vibe-responsable-{idioma}.pdf"  # la guía completa, generada con --pdf y publicada junto a las páginas
ICONOS = ["book-check", "shield-check", "creative-commons", "bot", "messages-square",
          "unplug", "accessibility", "quote", "notebook-pen", "download"]

UI = {
    "es": {
        "guia": "Guía para publicar materiales educativos creados con vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Saltar al contenido",
        "nav": "Secciones de la guía",
        "nav_guia": "Guía",
        "borrador": "Borrador",
        "borrador_ayuda": "La guía está completa, pero su autor la está revisando y el texto puede cambiar.",
        "imprimir": "Imprimir esta página",
        "imprimir_desc": "Solo lo que se ve en esta página",
        "imprimir_menu": "Imprimir o descargar",
        "pdf": "Descargar la guía completa en PDF",
        "pdf_desc": "Todas las páginas en un solo documento",
        "tema": "Modo claro u oscuro",
        "citar": "Cómo citar",
        "cita": 'De Haro, J. J. (2026). <i>Guía para publicar materiales educativos creados con vibe coding</i> (borrador). Vibe Coding Educativo. <a href="https://vibe-coding-educativo.github.io/vibe-responsable/">https://vibe-coding-educativo.github.io/vibe-responsable/</a>',
        "subtitulo": "Guía ética y de responsabilidad, no técnica, para la comunidad educativa",
        "autor": "Juan José de Haro",
        "borrador_pdf": "Borrador del {fecha}. La guía está completa, pero su autor la está revisando y el texto puede cambiar. La versión al día está en {url}.",
        "contenido": "Contenido",
        "capitulo": "Capítulo {n}",
        "pie_pdf": "Guía para publicar materiales educativos creados con vibe coding · Juan José de Haro · CC BY-SA 4.0 · Borrador, {fecha}",
        "meses": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "infografia_titulo": "Resumen gráfico",
        "infografia_alt": "Infografía con las diez recomendaciones, las mismas que aparecen en la lista.",
        "ampliar": "Ampliar la infografía",
        "descargar": "Descargar la imagen",
        "anterior": "Anterior",
        "siguiente": "Siguiente",
        "niveles_ayuda": "Qué significan «Lo mínimo» y «Lo recomendado»",
        "leer_capitulo": "Leer el capítulo",
        "que_hacer": "Qué hay que hacer",
        "volver_guia": "Volver a la guía",
        "cerrar": "Cerrar",
        "copiar": "Copiar el texto",
        "copiado": "Texto copiado",
        "acercar": "Ver a tamaño de lectura",
        "alejar": "Ajustar a la pantalla",
        "niveles": {"Lo mínimo.": "minimo", "Lo recomendado.": "recomendado", "En todos los casos.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Código bajo <a href="https://www.gnu.org/licenses/agpl-3.0.html">AGPL v3</a> y contenidos bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">CC BY-SA 4.0</a>.',
        "pie_2": '<a href="creditos.html">Créditos y licencias</a>.',
    },
}
PAGINAS = [("index.html", "00-presentacion.md"), ("guia.html", "01-guia.md"),
           ("herramientas.html", "02-herramientas.md"), ("para-la-ia.html", "04-para-la-ia.md")]


def pandoc(md):
    r = subprocess.run(["pandoc", "-f", "markdown-auto_identifiers+link_attributes", "-t", "html5", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def ancla(texto):
    s = unicodedata.normalize("NFD", texto.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def enlaces_externos(h):
    """Los enlaces a otras webs se abren en una pestaña nueva."""
    return re.sub(r'<a href="(https?://(?!vibe-coding-educativo\.github\.io/)[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)


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
        rotulo = T["nav_guia"] if a == "guia.html" else titulos[a]
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
<meta property="og:title" content="{html.escape(titulos["guia.html"])}">
<meta property="og:description" content="{html.escape(T["guia"])}">
<meta property="og:image" content="{URL_SITIO}infografia/lista-iconos.{idioma}.png">
<meta property="og:type" content="article">
<link rel="icon" href="../recursos/logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="../recursos/logo/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="../recursos/logo/apple-touch-icon.png">
<link rel="preload" href="../recursos/fuentes/atkinson-hyperlegible-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../recursos/estilos.css">
<script>(function(){{try{{var t=localStorage.getItem("{CLAVE_TEMA}");if(t!=="light"&&t!=="dark"){{t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";}}document.documentElement.dataset.theme=t;}}catch(e){{}}}})();</script>
<script src="../recursos/guia.js" defer></script>
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">{html.escape(T["saltar"])}</a>
<header class="pizarra">
<div class="ancho pizarra-int">
<p class="sitio"><a class="sitio-guia" href="./" aria-label="{html.escape(T["guia"])}"><img class="marca" src="../recursos/logo/logo.svg" alt="" width="30" height="30"><span>{html.escape(T["guia"])}</span></a>
<a class="sitio-comunidad" href="{COMUNIDAD}">{html.escape(T["comunidad"])}</a>
<span class="estado" tabindex="0">{html.escape(T["borrador"])}<span class="globo">{html.escape(T["borrador_ayuda"])}</span></span></p>
<nav aria-label="{html.escape(T["nav"])}"><ul>{"".join(nav)}</ul></nav>
<div class="utiles">
<button type="button" class="tema" title="{html.escape(T["tema"])}" aria-label="{html.escape(T["tema"])}"><span class="luna">{icono("moon")}</span><span class="sol">{icono("sun")}</span></button>
<div class="desplegable">
<button type="button" class="imprimir" title="{html.escape(T["imprimir_menu"])}" aria-label="{html.escape(T["imprimir_menu"])}" aria-haspopup="menu" aria-expanded="false">{icono("printer")}</button>
<div class="menu" role="menu" hidden>
<button type="button" role="menuitem" class="menu-imprimir">{icono("printer")}<span><b>{html.escape(T["imprimir"])}</b><small>{html.escape(T["imprimir_desc"])}</small></span></button>
<a role="menuitem" href="{PDF.format(idioma=idioma)}" download>{icono("download")}<span><b>{html.escape(T["pdf"])}</b><small>{html.escape(T["pdf_desc"])}</small></span></a>
</div>
</div>
</div>
</div>
</header>
<main id="contenido" class="ancho">
{cuerpo}
</main>
<footer class="pie">
<div class="ancho">
<p>{T["pie_1"]} {T["pie_2"]}</p>
</div>
</footer>
</body>
</html>
"""
    return enlaces_externos(pag)


def puntos_de_la_guia(idioma):
    """Las recomendaciones de 01-guia.md: [(número, título, explicación en HTML, niveles en HTML)]."""
    T = UI[idioma]
    md = (RAIZ / "contenido" / idioma / "01-guia.md").read_text(encoding="utf-8")
    puntos = []
    for b in re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]:
        cab, resto = b.split("\n", 1)
        m = re.match(r"(\d+)\\?\.\s+(.*)", cab.strip())
        h = pandoc(resto.strip())
        for etiqueta, clase in T["niveles"].items():
            h = h.replace(f"<li><strong>{etiqueta}</strong>", f'<li class="nivel {clase}"><strong>{etiqueta}</strong>')
        corte = h.find("<ul>")
        puntos.append((int(m.group(1)), m.group(2).strip(), h[:corte], h[corte:].replace("<ul>", '<ul class="niveles">', 1)))
    return puntos


def capitulos(idioma):
    """Capítulos escritos, por número de recomendación: {1: (archivo, título)}."""
    carpeta = RAIZ / "contenido" / idioma / "capitulos"
    encontrados = {}
    for md in sorted(carpeta.glob("*.md")) if carpeta.is_dir() else []:
        n = int(md.name.split("-")[0])
        encontrados[n] = (f"capitulo-{n}.html", titulo_de(md.read_text(encoding="utf-8")), md)
    return encontrados


def infografia(idioma):
    """Ruta y medidas de la infografía. Las medidas salen del SVG original, no de un número escrito a mano."""
    svg = (RAIZ / "infografia" / f"lista-iconos.{idioma}.svg").read_text(encoding="utf-8")
    an, al = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg).groups()
    return f"../infografia/lista-iconos.{idioma}.png", an, al, f'style="--ig-an:{an};--ig-al:{al}"'


def visor(idioma):
    T = UI[idioma]
    img, an, al, medidas = infografia(idioma)
    return f"""<dialog class="visor" {medidas} aria-label="{html.escape(T["infografia_titulo"])}">
<div class="visor-barra"><a class="visor-descarga" href="{img}" download>{html.escape(T["descargar"])}</a>
<button type="button" class="visor-zoom" data-acercar="{html.escape(T["acercar"])}" data-alejar="{html.escape(T["alejar"])}">{html.escape(T["acercar"])}</button>
<button type="button" class="visor-cerrar">{html.escape(T["cerrar"])}</button></div>
<div class="visor-lienzo"><img alt="{html.escape(T["infografia_alt"])}" width="{an}" height="{al}"></div>
</dialog>"""


def pagina_presentacion(idioma):
    """Portada: dos columnas de texto y, al lado, el resumen gráfico con el paso a la guía."""
    T = UI[idioma]
    md = (RAIZ / "contenido" / idioma / "00-presentacion.md").read_text(encoding="utf-8")
    titulo = titulo_de(md)
    apartados = []
    for a in re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]:
        cab, resto = a.split("\n", 1)
        apartados.append((cab.strip(), pandoc(resto.strip())))
    img, an, al, medidas = infografia(idioma)

    def bloque(i, clase):
        cab, h = apartados[i]
        return f'<section class="{clase}" aria-labelledby="h-{ancla(cab)}"><h2 id="h-{ancla(cab)}">{html.escape(cab)}</h2>{h}</section>'

    tarjeta = (f'<div class="tarjeta"><a class="miniatura ampliar" href="{img}" aria-label="{html.escape(T["ampliar"])}" title="{html.escape(T["ampliar"])}">'
               f'<img src="{img}" width="{an}" height="{al}" alt="{html.escape(T["infografia_alt"])}"></a>'
               f'<a class="descarga" href="{img}" download>{icono("download")}{html.escape(T["descargar"])}</a></div>')
    notas = "".join(bloque(i, "nota") for i in range(3, len(apartados)))
    # La tarjeta y «Cómo se utiliza» van juntas en el HTML; en pantalla, el CSS las
    # separa (pantalla alta) o las apila en la misma columna (portátil bajo).
    cuerpo = f"""<h1>{html.escape(titulo)}</h1>
<div class="entrada" {medidas}>
{bloque(0, "columna")}
{bloque(1, "columna")}
<aside class="paso-guia">{tarjeta}{bloque(2, "utiliza")}</aside>
{notas}
</div>
{visor(idioma)}"""
    return marco(idioma, "index.html", titulo, cuerpo, "pagina-presentacion")


def pagina_lista(idioma):
    T = UI[idioma]
    md = (RAIZ / "contenido" / idioma / "01-guia.md").read_text(encoding="utf-8")
    titulo = titulo_de(md)
    puntos = puntos_de_la_guia(idioma)
    total = len(puntos)

    caps = capitulos(idioma)
    filas = []
    for (n, t, explicacion, niveles), ic in zip(puntos, ICONOS):
        ayuda = (f'<a class="leer-capitulo" href="{caps[n][0]}">{html.escape(T["leer_capitulo"])}</a>' if n in caps
                 else f'<a class="ayuda-niveles" href="herramientas.html#{ancla("Lo mínimo y lo recomendado")}">{html.escape(T["niveles_ayuda"])}</a>')
        ant = f'<button type="button" class="paso" data-ir="{n-1}">{html.escape(T["anterior"])}</button>' if n > 1 else "<span></span>"
        sig = f'<button type="button" class="paso" data-ir="{n+1}">{html.escape(T["siguiente"])}</button>' if n < total else "<span></span>"
        filas.append(
            f'<li class="punto" id="recomendacion-{n}">'
            f'<div class="fila"><a class="abrir" href="#detalle-{n}" aria-controls="detalle-{n}">'
            f'<span class="numero" aria-hidden="true">{n}</span>{icono(ic)}'
            f'<span class="rotulo"><span class="oculto">{n}. </span>{html.escape(t)}</span></a></div>'
            f'<article class="detalle" id="detalle-{n}" data-punto="{n}" aria-labelledby="t-{n}"><div class="detalle-int"><div class="detalle-caja">'
            f'<header class="detalle-cab"><span class="cifra" aria-hidden="true">{n}</span>'
            f'<h2 id="t-{n}" tabindex="-1"><span class="oculto">{n}. </span>{html.escape(t)}</h2>'
            f'</header>'
            f'<div class="detalle-cuerpo"><div class="explicacion">{explicacion}</div>{niveles}</div>'
            f'<footer class="detalle-pie solo-js">{ant}{ayuda}{sig}</footer>'
            f'</div></div></article></li>')

    cuerpo = f"""<h1>{html.escape(titulo)}</h1>
<div class="tablero">
<section class="hoja" aria-label="{html.escape(titulo)}">
<ol class="diez">{"".join(filas)}</ol>
</section>
<div class="panel"></div>
</div>"""
    return marco(idioma, "guia.html", titulo, cuerpo, "pagina-lista")


def pagina_texto(idioma, archivo, fuente):
    T = UI[idioma]
    md = (RAIZ / "contenido" / idioma / fuente).read_text(encoding="utf-8")
    titulo = titulo_de(md)
    apartados = re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]
    secciones = []
    for a in apartados:
        cab, resto = a.split("\n", 1)
        cab = cab.strip()
        h = pandoc(resto.strip())
        h = h.replace("<ul>", '<ul class="familias">', 1)
        h = re.sub(r"<pre[^>]*>",
                   f'<div class="copiable"><p class="copiable-cab solo-js">'
                   f'<button type="button" class="copiar discreto" data-hecho="{html.escape(T["copiado"])}">{html.escape(T["copiar"])}</button></p><pre>',
                   h)
        h = h.replace("</pre>", "</pre></div>")
        secciones.append(f'<section class="apartado" id="{ancla(cab)}" aria-labelledby="h-{ancla(cab)}">'
                         f'<h2 id="h-{ancla(cab)}">{html.escape(cab)}</h2><div class="texto">{h}</div></section>')
    if archivo == "creditos.html":
        # La cita, la misma que lleva la portada del PDF; el DOI se añadirá con la versión definitiva.
        secciones.append(f'<section class="apartado" id="{ancla(T["citar"])}" aria-labelledby="h-{ancla(T["citar"])}">'
                         f'<h2 id="h-{ancla(T["citar"])}">{html.escape(T["citar"])}</h2><div class="texto"><p>{T["cita"]}</p></div></section>')
    cuerpo = f'<h1>{html.escape(titulo)}</h1>\n' + "\n".join(secciones)
    return marco(idioma, archivo, titulo, cuerpo, "pagina-texto")


def pagina_capitulo(idioma, n, archivo, md):
    """Un capítulo: texto seguido, con vuelta a la guía y paso al anterior y al siguiente."""
    T = UI[idioma]
    caps = capitulos(idioma)
    texto = md.read_text(encoding="utf-8")
    titulo = titulo_de(texto)
    cuerpo_md = texto.split("\n", 1)[1]
    # El recuadro repite lo mínimo y lo recomendado de la lista: hay una sola fuente, 01-guia.md
    niveles = next(p[3] for p in puntos_de_la_guia(idioma) if p[0] == n)
    recuadro = (f'<aside class="que-hacer" aria-labelledby="h-que-hacer"><h2 id="h-que-hacer">{html.escape(T["que_hacer"])}</h2>'
                f'{niveles}</aside>')
    previo = re.split(r"^## ", cuerpo_md, flags=re.M)[0].strip()
    previo = f'<div class="previo">{pandoc(previo)}</div>' if previo else ""
    secciones = []
    for a in re.split(r"^## ", cuerpo_md, flags=re.M)[1:]:
        cab, resto = a.split("\n", 1)
        secciones.append(f'<section class="apartado" id="{ancla(cab.strip())}" aria-labelledby="h-{ancla(cab.strip())}">'
                         f'<h2 id="h-{ancla(cab.strip())}">{html.escape(cab.strip())}</h2>'
                         f'<div class="texto">{pandoc(resto.strip())}</div></section>')
    ant = (f'<a class="paso" href="{caps[n-1][0]}">{html.escape(T["anterior"])}</a>' if n - 1 in caps else "<span></span>")
    sig = (f'<a class="paso" href="{caps[n+1][0]}">{html.escape(T["siguiente"])}</a>' if n + 1 in caps else "<span></span>")
    cuerpo = (f'<p class="migas"><a href="guia.html">{html.escape(T["volver_guia"])}</a></p>'
              f'<h1><span class="cifra-cap" aria-hidden="true">{n}</span>{html.escape(titulo)}</h1>'
              + recuadro + previo + "\n".join(secciones)
              + f'<nav class="entre-capitulos" aria-label="{html.escape(T["nav"])}">{ant}'
                f'<a href="guia.html">{html.escape(T["volver_guia"])}</a>{sig}</nav>')
    return marco(idioma, "guia.html", titulo, cuerpo, "pagina-texto pagina-capitulo")


def pagina_completa(idioma, paginas):
    """Todas las páginas seguidas, con portada e índice, para imprimirlas a PDF (generar-pdf.js).

    Orden de lectura: presentación, guía, los capítulos que la desarrollan, herramientas,
    instrucciones para la IA y créditos. Los enlaces entre páginas pasan a ser anclas."""
    T = UI[idioma]
    hoy = date.today()
    fecha = f"{hoy.day} de {T['meses'][hoy.month - 1]} de {hoy.year}"
    caps = capitulos(idioma)
    titulos = {a: titulo_de((RAIZ / "contenido" / idioma / m).read_text(encoding="utf-8")) for a, m in PAGINAS}
    titulos["creditos.html"] = titulo_de((RAIZ / "contenido" / idioma / "03-creditos.md").read_text(encoding="utf-8"))
    orden = [("index.html", titulos["index.html"]), ("guia.html", titulos["guia.html"])]
    orden += [(a, f"{T['capitulo'].format(n=n)}. {t}") for n, (a, t, _) in sorted(caps.items())]
    orden += [(a, titulos[a]) for a in ("herramientas.html", "para-la-ia.html", "creditos.html")]
    partes, indice = [], []
    for archivo, titulo in orden:
        clave = archivo[:-5]
        cuerpo = re.search(r'<main id="contenido" class="ancho">(.*)</main>', paginas[archivo], flags=re.S).group(1)
        cuerpo = re.sub(r'href="[a-z0-9-]+\.html#', 'href="#', cuerpo)
        cuerpo = re.sub(r'href="([a-z0-9-]+)\.html"', r'href="#pagina-\1"', cuerpo)
        cuerpo = cuerpo.replace('href="./"', 'href="#pagina-index"')
        partes.append(f'<section class="pdf-pagina" id="pagina-{clave}">{cuerpo}</section>')
        indice.append(f'<li><a href="#pagina-{clave}">{html.escape(titulo)}</a></li>')
    return f"""<!DOCTYPE html>
<html lang="{idioma}" data-theme="light">
<head>
<meta charset="utf-8">
<title>{html.escape(T["guia"])}</title>
<link rel="stylesheet" href="../recursos/estilos.css">
<style>
/* Solo para la impresión a PDF de la guía completa */
.pdf {{ background: #fff; color: #000; }}
.pdf .ancho {{ max-width: none; padding: 0; }}
.pdf-portada {{ break-after: page; min-height: 240mm; display: flex; flex-direction: column; }}
.pdf-portada .marca {{ width: 3.2rem; height: 3.2rem; margin-bottom: 1.2rem; }}
.pdf-portada .pdf-comunidad {{ margin: 0; font-weight: 700; color: var(--verde); }}
.pdf-portada h1 {{ font-size: 2.4rem; margin: 0.4rem 0 0.6rem; }}
.pdf-portada .pdf-sub {{ font-size: 1.15rem; margin: 0 0 1.6rem; color: #333; }}
.pdf-portada .pdf-autor {{ font-size: 1.15rem; font-weight: 700; margin: 0 0 3rem; }}
.pdf-portada .pdf-borrador {{ border: 1.5px solid #000; border-radius: 6px; padding: 0.7rem 0.9rem; margin: 0 0 2rem; }}
.pdf-portada .pdf-cita {{ margin-top: auto; }}
.pdf-portada .pdf-cita h2 {{ font-size: 1.05rem; margin: 0 0 0.3rem; }}
.pdf-portada .pdf-cita p {{ margin: 0 0 1.2rem; }}
.pdf-portada .pdf-licencia {{ margin: 0; font-size: 0.9rem; color: #333; }}
.pdf-indice {{ break-after: page; }}
.pdf-indice h2 {{ font-size: 1.4rem; }}
.pdf-indice ol {{ padding-left: 1.4rem; line-height: 1.9; }}
.pdf-pagina {{ break-before: page; }}
.pdf-pagina h1 {{ margin-top: 0; }}
.pdf .paso-guia {{ display: contents; }}
.pdf .tarjeta {{ border: 0; box-shadow: none; padding: 0; margin: 1rem 0; break-before: page; }}
.pdf .tarjeta .miniatura {{ width: 12cm !important; height: auto !important; margin: 0 auto; border: 1px solid #bbb; }}
.pdf .descarga, .pdf .cita {{ display: none; }}
.pdf a {{ color: inherit; text-decoration: none; }}
.pdf .pdf-indice a, .pdf .texto a[href^="http"], .pdf .explicacion a[href^="http"] {{ color: var(--verde); }}
</style>
</head>
<body class="pdf" data-pie="{html.escape(T["pie_pdf"].format(fecha=fecha))}">
<section class="pdf-portada">
<img class="marca" src="../recursos/logo/logo.svg" alt="" width="54" height="54">
<p class="pdf-comunidad">{html.escape(T["comunidad"])}</p>
<h1>{html.escape(T["guia"])}</h1>
<p class="pdf-sub">{html.escape(T["subtitulo"])}</p>
<p class="pdf-autor">{html.escape(T["autor"])}</p>
<p class="pdf-borrador">{html.escape(T["borrador_pdf"].format(fecha=fecha, url=URL_SITIO))}</p>
<div class="pdf-cita"><h2>{html.escape(T["citar"])}</h2><p>{T["cita"]}</p>
<p class="pdf-licencia">{T["pie_1"]}</p></div>
</section>
<nav class="pdf-indice" aria-label="{html.escape(T["contenido"])}"><h2>{html.escape(T["contenido"])}</h2><ol>{"".join(indice)}</ol></nav>
{"".join(partes)}
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
<link rel="icon" href="recursos/logo/favicon.svg" type="image/svg+xml">
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


def comprobar_enlaces_internos(idioma):
    """Revisa que cada enlace interno de las páginas generadas lleve a un archivo y a un ancla que existen."""
    base, rotos = RAIZ / idioma, []
    ids = {p.name: set(re.findall(r'id="([^"]+)"', p.read_text(encoding="utf-8"))) for p in base.glob("*.html")}
    for p in sorted(base.glob("*.html")):
        for href in re.findall(r'href="([^"]+)"', p.read_text(encoding="utf-8")):
            if re.match(r"(https?:|mailto:)", href):
                continue
            ruta, _, fragmento = href.partition("#")
            destino = p if not ruta else (base / ruta / "index.html" if ruta.endswith("/") or ruta == "./" else base / ruta)
            if not destino.resolve().exists():
                rotos.append(f"{p.name}: {href} (no existe)")
            elif fragmento and destino.suffix == ".html" and fragmento not in ids.get(destino.name, set()):
                rotos.append(f"{p.name}: {href} (ancla inexistente)")
    return rotos


if __name__ == "__main__":
    con_pdf = "--pdf" in sys.argv
    for idioma in IDIOMAS:
        destino = RAIZ / idioma
        destino.mkdir(exist_ok=True)
        paginas = {"index.html": pagina_presentacion(idioma), "guia.html": pagina_lista(idioma)}
        for archivo, fuente in PAGINAS[2:]:
            paginas[archivo] = pagina_texto(idioma, archivo, fuente)
        for n, (archivo, _, md) in capitulos(idioma).items():
            paginas[archivo] = pagina_capitulo(idioma, n, archivo, md)
        paginas["creditos.html"] = pagina_texto(idioma, "creditos.html", "03-creditos.md")
        for archivo, contenido in paginas.items():
            (destino / archivo).write_text(contenido, encoding="utf-8")
        viejo = destino / "presentacion.html"
        if viejo.exists():
            viejo.unlink()
        print("generado", idioma, [a for a, _ in PAGINAS])
        if con_pdf:
            # La guía completa: una página sin publicar (completo.html, en .gitignore) que
            # generar-pdf.js imprime con Chromium. Se publica solo el PDF resultante.
            (destino / "completo.html").write_text(pagina_completa(idioma, paginas), encoding="utf-8")
            subprocess.run(["node", str(RAIZ / "generar-pdf.js"), f"{idioma}/completo.html",
                            f"{idioma}/{PDF.format(idioma=idioma)}"], cwd=RAIZ, check=True)
        rotos = comprobar_enlaces_internos(idioma)
        if rotos:
            print("ENLACES INTERNOS ROTOS:")
            for r in rotos:
                print("  ", r)
            raise SystemExit(1)
    (RAIZ / "index.html").write_text(portada(), encoding="utf-8")
    (RAIZ / ".nojekyll").write_text("", encoding="utf-8")
