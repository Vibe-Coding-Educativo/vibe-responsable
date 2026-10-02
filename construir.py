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
  para-la-ia.html     instrucciones para crear con IA: cómo se entrega el archivo para crear,
                      que se muestra en la página y se publica aparte (04-para-la-ia.md)
  vcer.html           la evaluación VCER: qué es, cómo se lee el resultado, cómo evaluar un
                      recurso, con el archivo para evaluar, y la rúbrica (06-evaluacion-vcer.md);
                      arriba muestra el resultado que trae el enlace de la mención, que llega
                      a través de vcer/index.html (ADR 21)
  referencias.html    todo lo citado en el texto (05-referencias.md)
  creditos.html       créditos y licencias, enlazada desde el pie (03-creditos.md)

Los capítulos que desarrollan cada recomendación están en contenido/<idioma>/capitulos/
y se publican como capitulo-N.html. Se enlazan desde su recomendación en la guía; los
que aún no están escritos no muestran enlace.
"""
import hashlib, html, json, re, subprocess, sys, unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent
# Los idiomas de la guía (ADR 20). El castellano es el original y el idioma por omisión;
# cada idioma tiene su carpeta en contenido/<idioma>/ y su bloque en UI.
IDIOMAS = ["es", "ca", "gl", "eu", "en"]
NOMBRES_IDIOMAS = {"es": "Castellano", "ca": "Català", "gl": "Galego", "eu": "Euskara", "en": "English"}
URL_SITIO = "https://vibe-coding-educativo.github.io/vibe-responsable/"
REPO = "https://github.com/Vibe-Coding-Educativo/vibe-responsable"
# La versión publicada de la guía (ADR 19). Cambia con el texto, no con los ajustes de la web;
# cada una lleva su etiqueta en el repositorio (v1.0) y su depósito en Zenodo, con su DOI.
VERSION = "2.0"
FECHA_VERSION = date(2026, 10, 2)
DOI = "10.5281/zenodo.23105801"            # el de esta versión
DOI_CONCEPTO = "10.5281/zenodo.23081517"   # el de todas las versiones: lleva siempre a la última
CLAVE_TEMA = "vibe-responsable:tema"   # única entrada en localStorage; la misma en recursos/guia.js
PDF = "vibe-responsable-{idioma}.pdf"  # la guía completa, generada con --pdf y publicada junto a las páginas
# Los archivos para la IA: cada uno está en contenido/<idioma>/ y se publica con otro nombre para
# descargarlo; para-la-ia.html lo muestra entero en el lugar de su marca (<!-- instrucciones -->).
ARCHIVOS_IA = {"instrucciones": ("instrucciones-ia.md", "instrucciones-vibe-responsable.md"),   # para crear
               "evaluacion": ("evaluacion-ia.md", "evaluacion-vibe-responsable.md")}         # para evaluar
ICONOS = ["book-check", "shield-check", "messages-square", "unplug", "accessibility",
          "quote", "notebook-pen", "bot", "creative-commons", "download"]

MESES = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "ca": ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre"],
    "gl": ["xaneiro", "febreiro", "marzo", "abril", "maio", "xuño", "xullo", "agosto", "setembro", "outubro", "novembro", "decembro"],
    "eu": ["urtarrilaren", "otsailaren", "martxoaren", "apirilaren", "maiatzaren", "ekainaren", "uztailaren", "abuztuaren", "irailaren", "urriaren", "azaroaren", "abenduaren"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
}

UI = {
    "es": {
        "nombre": "Vibe coding responsable",   # nombre corto: cabecera, pestaña, portada del PDF y cita
        "guia": "Guía para publicar materiales educativos creados con vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Saltar al contenido",
        "nav": "Secciones de la guía",
        "nav_capitulos": "Capítulo anterior y siguiente",
        # rótulos del menú más cortos que el título de su página
        "nav_cortos": {"guia.html": "Guía", "para-la-ia.html": "Crear con IA", "vcer.html": "Evaluación VCER", "referencias.html": "Referencias", "creditos.html": "Créditos"},
        "imprimir": "Imprimir esta página",
        "imprimir_desc": "Solo lo que se ve en esta página",
        "imprimir_menu": "Imprimir o descargar",
        "pdf": "Descargar la guía completa en PDF",
        "pdf_desc": "Todas las páginas en un solo documento",
        "tema": "Modo claro u oscuro",
        "idioma": "Idioma",
        "citar": "Cómo citar",
        "cita": f'De Haro, J. J. (2026). <i>Vibe coding responsable: guía para publicar materiales educativos creados con vibe coding</i> (versión {VERSION}). Vibe Coding Educativo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a>',
        "cita_nota": f'Para citar la guía sin fijar la versión: <a href="https://doi.org/{DOI_CONCEPTO}">https://doi.org/{DOI_CONCEPTO}</a>, que lleva siempre a la última.',
        "version_fecha": "Versión {version}, {fecha}",
        "autor": "Juan José de Haro",
        "contenido": "Contenido",
        "capitulo": "Capítulo {n}",
        "pie_pdf": "Vibe coding responsable · Juan José de Haro · CC BY-SA 4.0 · {fecha}",
        "fecha": lambda d: f"{d.day} de {MESES['es'][d.month - 1]} de {d.year}",
        "infografia_titulo": "Resumen gráfico",
        # Fases de la vida del material (ADR 15): primera recomendación de cada una, con el verbo
        # y el complemento, que forman las dos líneas del rótulo vertical. Los mismos que la infografía.
        "fases": {1: ("Proteger", "al alumnado"), 3: ("Construir", "el material"),
                  6: ("Documentar", "el trabajo"), 9: ("Compartir", "el material")},
        "infografia_alt": "Infografía con las diez recomendaciones, las mismas que aparecen en la lista, agrupadas en cuatro fases: proteger al alumnado, construir el material, documentar el trabajo y compartir el material.",
        "ampliar": "Ampliar la infografía",
        "descargar": "Descargar la imagen",
        # La animación de la guía (ADR 16), que la portada abre en una ventana
        "ver_animacion": "Ver la animación",
        "volver_a_ver": "Volver a ver",
        "animacion_titulo": "La guía en una animación",
        "anterior": "Anterior",
        "siguiente": "Siguiente",
        "niveles_ayuda": "Qué significan «Lo mínimo» y «Lo recomendado»",
        "leer_capitulo": "Más información",
        "que_hacer": "Qué hay que hacer",
        "volver_guia": "Volver a la guía",
        "cerrar": "Cerrar",
        "copiar": "Copiar el texto",
        "copiado": "Texto copiado",
        "descargar_archivo": "Descargar el archivo",
        "ver_archivo": {"instrucciones": "Ver las instrucciones para crear", "evaluacion": "Ver las instrucciones para evaluar"},
        # Las ventanas de la portada que ofrecen cada archivo sin salir de ella
        "ventana_ia": {
            "instrucciones": ("Instrucciones para crear un material",
                              "Al empezar, adjuntar el archivo en la conversación con la IA, o pegar el texto al principio, junto con la descripción del material que se quiere crear."),
            "evaluacion": ("Instrucciones para evaluar el material",
                           "Al terminar, adjuntar el archivo en la misma conversación, o pegar el texto, y pedir «evalúa el material según las instrucciones»."),
        },
        "mas_informacion": "Más información",
        "copiar_titulo": "Copiar el texto para pegarlo en la conversación con la IA",
        "descargar_titulo": "Descargar el archivo para adjuntarlo en la conversación con la IA",
        "mas_informacion_titulo": {"instrucciones": "Ir a la página de instrucciones para crear con IA, con el texto completo",
                                   "evaluacion": "Ir a la página de la evaluación VCER, con el texto completo"},
        "rubrica": "Rúbrica VCER: 2, se cumple; 1, en parte; 0, no se cumple",
        "punto": "Recomendación",
        "acercar": "Ver a tamaño de lectura",
        "alejar": "Ajustar a la pantalla",
        "niveles": {"Lo mínimo.": "minimo", "Lo recomendado.": "recomendado", "En todos los casos.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Contenidos bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">CC BY-SA 4.0</a>.',
        "pie_2": f'<a href="creditos.html">Créditos y licencias</a>. <a href="creditos.html#versiones">Versión {VERSION}</a>. <a href="https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues">Sugerencias y correcciones</a>.',
    },
    "ca": {
        "nombre": "Vibe coding responsable",
        "guia": "Guia per publicar materials educatius creats amb vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Salta al contingut",
        "nav": "Seccions de la guia",
        "nav_capitulos": "Capítol anterior i següent",
        "nav_cortos": {"guia.html": "Guia", "para-la-ia.html": "Crear amb IA", "vcer.html": "Avaluació VCER", "referencias.html": "Referències", "creditos.html": "Crèdits"},
        "imprimir": "Imprimir aquesta pàgina",
        "imprimir_desc": "Només el que es veu en aquesta pàgina",
        "imprimir_menu": "Imprimir o descarregar",
        "pdf": "Descarregar la guia completa en PDF",
        "pdf_desc": "Totes les pàgines en un sol document",
        "tema": "Mode clar o fosc",
        "idioma": "Llengua",
        "citar": "Com citar",
        "cita": f'De Haro, J. J. (2026). <i>Vibe coding responsable: guia per publicar materials educatius creats amb vibe coding</i> (versió {VERSION}). Vibe Coding Educativo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a>',
        "cita_nota": f'Per citar la guia sense fixar la versió: <a href="https://doi.org/{DOI_CONCEPTO}">https://doi.org/{DOI_CONCEPTO}</a>, que porta sempre a la darrera.',
        "version_fecha": "Versió {version}, {fecha}",
        "autor": "Juan José de Haro",
        "contenido": "Contingut",
        "capitulo": "Capítol {n}",
        "pie_pdf": "Vibe coding responsable · Juan José de Haro · CC BY-SA 4.0 · {fecha}",
        "fecha": lambda d: f"{d.day} {'d’' if MESES['ca'][d.month - 1][0] in 'ao' else 'de '}{MESES['ca'][d.month - 1]} de {d.year}",
        "infografia_titulo": "Resum gràfic",
        "fases": {1: ("Protegir", "l'alumnat"), 3: ("Construir", "el material"),
                  6: ("Documentar", "la feina"), 9: ("Compartir", "el material")},
        "infografia_alt": "Infografia amb les deu recomanacions, les mateixes que apareixen a la llista, agrupades en quatre fases: protegir l'alumnat, construir el material, documentar la feina i compartir el material.",
        "ampliar": "Ampliar la infografia",
        "descargar": "Descarregar la imatge",
        "ver_animacion": "Veure l'animació",
        "volver_a_ver": "Tornar a veure",
        "animacion_titulo": "La guia en una animació",
        "anterior": "Anterior",
        "siguiente": "Següent",
        "niveles_ayuda": "Què signifiquen «El mínim» i «El recomanat»",
        "leer_capitulo": "Més informació",
        "que_hacer": "Què cal fer",
        "volver_guia": "Tornar a la guia",
        "cerrar": "Tancar",
        "copiar": "Copiar el text",
        "copiado": "Text copiat",
        "descargar_archivo": "Descarregar el fitxer",
        "ver_archivo": {"instrucciones": "Veure les instruccions per crear", "evaluacion": "Veure les instruccions per avaluar"},
        "ventana_ia": {
            "instrucciones": ("Instruccions per crear un material",
                              "En començar, adjuntar el fitxer a la conversa amb la IA, o enganxar el text al principi, juntament amb la descripció del material que es vol crear."),
            "evaluacion": ("Instruccions per avaluar el material",
                           "En acabar, adjuntar el fitxer a la mateixa conversa, o enganxar el text, i demanar «avalua el material segons les instruccions»."),
        },
        "mas_informacion": "Més informació",
        "copiar_titulo": "Copiar el text per enganxar-lo a la conversa amb la IA",
        "descargar_titulo": "Descarregar el fitxer per adjuntar-lo a la conversa amb la IA",
        "mas_informacion_titulo": {"instrucciones": "Anar a la pàgina d'instruccions per crear amb IA, amb el text complet",
                                   "evaluacion": "Anar a la pàgina de l'avaluació VCER, amb el text complet"},
        "rubrica": "Rúbrica VCER: 2, es compleix; 1, en part; 0, no es compleix",
        "punto": "Recomanació",
        "acercar": "Veure a mida de lectura",
        "alejar": "Ajustar a la pantalla",
        "niveles": {"El mínim.": "minimo", "El recomanat.": "recomendado", "En tots els casos.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Continguts amb llicència <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ca">CC BY-SA 4.0</a>.',
        "pie_2": f'<a href="creditos.html">Crèdits i llicències</a>. <a href="creditos.html#versions">Versió {VERSION}</a>. <a href="https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues">Suggeriments i correccions</a>.',
    },
    "gl": {
        "nombre": "Vibe coding responsable",
        "guia": "Guía para publicar materiais educativos creados con vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Saltar ao contido",
        "nav": "Seccións da guía",
        "nav_capitulos": "Capítulo anterior e seguinte",
        "nav_cortos": {"guia.html": "Guía", "para-la-ia.html": "Crear con IA", "vcer.html": "Avaliación VCER", "referencias.html": "Referencias", "creditos.html": "Créditos"},
        "imprimir": "Imprimir esta páxina",
        "imprimir_desc": "Só o que se ve nesta páxina",
        "imprimir_menu": "Imprimir ou descargar",
        "pdf": "Descargar a guía completa en PDF",
        "pdf_desc": "Todas as páxinas nun só documento",
        "tema": "Modo claro ou escuro",
        "idioma": "Idioma",
        "citar": "Como citar",
        "cita": f'De Haro, J. J. (2026). <i>Vibe coding responsable: guía para publicar materiais educativos creados con vibe coding</i> (versión {VERSION}). Vibe Coding Educativo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a>',
        "cita_nota": f'Para citar a guía sen fixar a versión: <a href="https://doi.org/{DOI_CONCEPTO}">https://doi.org/{DOI_CONCEPTO}</a>, que leva sempre á última.',
        "version_fecha": "Versión {version}, {fecha}",
        "autor": "Juan José de Haro",
        "contenido": "Contido",
        "capitulo": "Capítulo {n}",
        "pie_pdf": "Vibe coding responsable · Juan José de Haro · CC BY-SA 4.0 · {fecha}",
        "fecha": lambda d: f"{d.day} de {MESES['gl'][d.month - 1]} de {d.year}",
        "infografia_titulo": "Resumo gráfico",
        "fases": {1: ("Protexer", "o alumnado"), 3: ("Construír", "o material"),
                  6: ("Documentar", "o traballo"), 9: ("Compartir", "o material")},
        "infografia_alt": "Infografía coas dez recomendacións, as mesmas que aparecen na lista, agrupadas en catro fases: protexer o alumnado, construír o material, documentar o traballo e compartir o material.",
        "ampliar": "Ampliar a infografía",
        "descargar": "Descargar a imaxe",
        "ver_animacion": "Ver a animación",
        "volver_a_ver": "Volver ver",
        "animacion_titulo": "A guía nunha animación",
        "anterior": "Anterior",
        "siguiente": "Seguinte",
        "niveles_ayuda": "Que significan «O mínimo» e «O recomendado»",
        "leer_capitulo": "Máis información",
        "que_hacer": "Que hai que facer",
        "volver_guia": "Volver á guía",
        "cerrar": "Pechar",
        "copiar": "Copiar o texto",
        "copiado": "Texto copiado",
        "descargar_archivo": "Descargar o ficheiro",
        "ver_archivo": {"instrucciones": "Ver as instrucións para crear", "evaluacion": "Ver as instrucións para avaliar"},
        "ventana_ia": {
            "instrucciones": ("Instrucións para crear un material",
                              "Ao comezar, achegar o ficheiro na conversa coa IA, ou pegar o texto ao principio, xunto coa descrición do material que se quere crear."),
            "evaluacion": ("Instrucións para avaliar o material",
                           "Ao rematar, achegar o ficheiro na mesma conversa, ou pegar o texto, e pedir «avalía o material segundo as instrucións»."),
        },
        "mas_informacion": "Máis información",
        "copiar_titulo": "Copiar o texto para pegalo na conversa coa IA",
        "descargar_titulo": "Descargar o ficheiro para achegalo na conversa coa IA",
        "mas_informacion_titulo": {"instrucciones": "Ir á páxina de instrucións para crear con IA, co texto completo",
                                   "evaluacion": "Ir á páxina da avaliación VCER, co texto completo"},
        "rubrica": "Rúbrica VCER: 2, cúmprese; 1, en parte; 0, non se cumpre",
        "punto": "Recomendación",
        "acercar": "Ver a tamaño de lectura",
        "alejar": "Axustar á pantalla",
        "niveles": {"O mínimo.": "minimo", "O recomendado.": "recomendado", "En todos os casos.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Contidos baixo licenza <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.gl">CC BY-SA 4.0</a>.',
        "pie_2": f'<a href="creditos.html">Créditos e licenzas</a>. <a href="creditos.html#versions">Versión {VERSION}</a>. <a href="https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues">Suxestións e correccións</a>.',
    },
    "eu": {
        "nombre": "Vibe coding arduratsua",
        "guia": "Vibe coding bidez sortutako material hezitzaileak argitaratzeko gida",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Joan edukira",
        "nav": "Gidaren atalak",
        "nav_capitulos": "Aurreko eta hurrengo kapitulua",
        "nav_cortos": {"guia.html": "Gida", "para-la-ia.html": "IArekin sortu", "vcer.html": "VCER ebaluazioa", "referencias.html": "Erreferentziak", "creditos.html": "Kredituak"},
        "imprimir": "Orri hau inprimatu",
        "imprimir_desc": "Orri honetan ikusten dena bakarrik",
        "imprimir_menu": "Inprimatu edo deskargatu",
        "pdf": "Gida osoa PDFan deskargatu",
        "pdf_desc": "Orri guztiak dokumentu bakarrean",
        "tema": "Modu argia edo iluna",
        "idioma": "Hizkuntza",
        "citar": "Nola aipatu",
        "cita": f'De Haro, J. J. (2026). <i>Vibe coding arduratsua: vibe coding bidez sortutako material hezitzaileak argitaratzeko gida</i> ({VERSION} bertsioa). Vibe Coding Educativo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a>',
        "cita_nota": f'Gida bertsioa finkatu gabe aipatzeko: <a href="https://doi.org/{DOI_CONCEPTO}">https://doi.org/{DOI_CONCEPTO}</a>, beti azkenera eramaten duena.',
        "version_fecha": "{version} bertsioa, {fecha}",
        "autor": "Juan José de Haro",
        "contenido": "Edukia",
        "capitulo": "{n}. kapitulua",
        "pie_pdf": "Vibe coding arduratsua · Juan José de Haro · CC BY-SA 4.0 · {fecha}",
        "fecha": lambda d: f"{d.year}ko {MESES['eu'][d.month - 1]} {d.day}a",
        "infografia_titulo": "Laburpen grafikoa",
        "fases": {1: ("Ikasleak", "babestu"), 3: ("Materiala", "eraiki"),
                  6: ("Lana", "dokumentatu"), 9: ("Materiala", "partekatu")},
        "infografia_alt": "Hamar gomendioak dituen infografia, zerrendan agertzen diren berberak, lau fasetan multzokatuta: ikasleak babestu, materiala eraiki, lana dokumentatu eta materiala partekatu.",
        "ampliar": "Infografia handitu",
        "descargar": "Irudia deskargatu",
        "ver_animacion": "Animazioa ikusi",
        "volver_a_ver": "Berriro ikusi",
        "animacion_titulo": "Gida animazio batean",
        "anterior": "Aurrekoa",
        "siguiente": "Hurrengoa",
        "niveles_ayuda": "Zer esan nahi dute «Gutxienekoa» eta «Gomendatua»",
        "leer_capitulo": "Informazio gehiago",
        "que_hacer": "Zer egin behar den",
        "volver_guia": "Gidara itzuli",
        "cerrar": "Itxi",
        "copiar": "Testua kopiatu",
        "copiado": "Testua kopiatuta",
        "descargar_archivo": "Fitxategia deskargatu",
        "ver_archivo": {"instrucciones": "Sortzeko jarraibideak ikusi", "evaluacion": "Ebaluatzeko jarraibideak ikusi"},
        "ventana_ia": {
            "instrucciones": ("Material bat sortzeko jarraibideak",
                              "Hastean, erantsi fitxategia IArekiko elkarrizketan, edo itsatsi testua hasieran, sortu nahi den materialaren deskribapenarekin batera."),
            "evaluacion": ("Materiala ebaluatzeko jarraibideak",
                           "Amaitzean, erantsi fitxategia elkarrizketa berean, edo itsatsi testua, eta eskatu «ebaluatu materiala jarraibideen arabera»."),
        },
        "mas_informacion": "Informazio gehiago",
        "copiar_titulo": "Testua kopiatu IArekiko elkarrizketan itsasteko",
        "descargar_titulo": "Fitxategia deskargatu IArekiko elkarrizketan eransteko",
        "mas_informacion_titulo": {"instrucciones": "IArekin sortzeko jarraibideen orrira joan, testu osoarekin",
                                   "evaluacion": "VCER ebaluazioaren orrira joan, testu osoarekin"},
        "rubrica": "VCER errubrika: 2, betetzen da; 1, zati batean; 0, ez da betetzen",
        "punto": "Gomendioa",
        "acercar": "Irakurtzeko tamainan ikusi",
        "alejar": "Pantailara doitu",
        "siglas": ["IAren", "IA"],
        "niveles": {"Gutxienekoa.": "minimo", "Gomendatua.": "recomendado", "Kasu guztietan.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Edukiak <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.eu">CC BY-SA 4.0</a> lizentziarekin.',
        "pie_2": f'<a href="creditos.html">Kredituak eta lizentziak</a>. <a href="creditos.html#bertsioak">{VERSION} bertsioa</a>. <a href="https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues">Iradokizunak eta zuzenketak</a>.',
    },
    "en": {
        "nombre": "Responsible vibe coding",
        "guia": "A guide to publishing educational materials created with vibe coding",
        "comunidad": "Vibe Coding Educativo",
        "saltar": "Skip to content",
        "nav": "Sections of the guide",
        "nav_capitulos": "Previous and next chapter",
        "nav_cortos": {"guia.html": "Guide", "para-la-ia.html": "Creating with AI", "vcer.html": "VCER evaluation", "referencias.html": "References", "creditos.html": "Credits"},
        "imprimir": "Print this page",
        "imprimir_desc": "Only what is shown on this page",
        "imprimir_menu": "Print or download",
        "pdf": "Download the full guide as PDF",
        "pdf_desc": "All the pages in a single document",
        "tema": "Light or dark mode",
        "idioma": "Language",
        "citar": "How to cite",
        "cita": f'De Haro, J. J. (2026). <i>Responsible vibe coding: a guide to publishing educational materials created with vibe coding</i> (version {VERSION}). Vibe Coding Educativo. <a href="https://doi.org/{DOI}">https://doi.org/{DOI}</a>',
        "cita_nota": f'To cite the guide without specifying a particular version: <a href="https://doi.org/{DOI_CONCEPTO}">https://doi.org/{DOI_CONCEPTO}</a>, which always leads to the latest one.',
        "version_fecha": "Version {version}, {fecha}",
        "autor": "Juan José de Haro",
        "contenido": "Contents",
        "capitulo": "Chapter {n}",
        "pie_pdf": "Responsible vibe coding · Juan José de Haro · CC BY-SA 4.0 · {fecha}",
        "fecha": lambda d: f"{d.day} {MESES['en'][d.month - 1]} {d.year}",
        "infografia_titulo": "Visual summary",
        "fases": {1: ("Protect", "students"), 3: ("Build", "the material"),
                  6: ("Document", "the work"), 9: ("Share", "the material")},
        "infografia_alt": "Infographic with the ten recommendations, the same ones that appear in the list, grouped into four phases: protect students, build the material, document the work and share the material.",
        "ampliar": "Enlarge the infographic",
        "descargar": "Download the image",
        "ver_animacion": "Watch the animation",
        "volver_a_ver": "Watch again",
        "animacion_titulo": "The guide in an animation",
        "anterior": "Previous",
        "siguiente": "Next",
        "niveles_ayuda": "What «Minimum» and «Recommended» mean",
        "leer_capitulo": "More information",
        "que_hacer": "What needs to be done",
        "volver_guia": "Back to the guide",
        "cerrar": "Close",
        "copiar": "Copy the text",
        "copiado": "Text copied",
        "descargar_archivo": "Download the file",
        "ver_archivo": {"instrucciones": "View the instructions for creating", "evaluacion": "View the instructions for evaluating"},
        "ventana_ia": {
            "instrucciones": ("Instructions for creating a material",
                              "When starting, attach the file to the conversation with the AI, or paste the text at the beginning, together with the description of the material you want to create."),
            "evaluacion": ("Instructions for evaluating the material",
                           "When finished, attach the file to the same conversation, or paste the text, and ask it to «evaluate the material according to the instructions»."),
        },
        "mas_informacion": "More information",
        "copiar_titulo": "Copy the text to paste it into the conversation with the AI",
        "descargar_titulo": "Download the file to attach it to the conversation with the AI",
        "mas_informacion_titulo": {"instrucciones": "Go to the page of instructions for creating with AI, with the full text",
                                   "evaluacion": "Go to the page of the VCER evaluation, with the full text"},
        "rubrica": "VCER rubric: 2, met; 1, partly met; 0, not met",
        "punto": "Recommendation",
        "acercar": "View at reading size",
        "alejar": "Fit to screen",
        "siglas": ["AI"],
        "niveles": {"Minimum.": "minimo", "Recommended.": "recomendado", "In all cases.": "todos"},
        "pie_1": '© 2026 <a href="https://bilateria.org">Juan José de Haro</a>. Content under <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC BY-SA 4.0</a>.',
        "pie_2": f'<a href="creditos.html">Credits and licences</a>. <a href="creditos.html#versions">Version {VERSION}</a>. <a href="https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues">Suggestions and corrections</a>.',
    },
}
# La página de la evaluación VCER (ADR 21) muestra arriba el resultado que trae el enlace de la mención
# (?r=…&p=…&f=…&v=…&t=…&u=…). recursos/guia.js compone la frase con estas piezas: «recurso» lleva {t}
# (título) y {v} (versión); «frase», {recurso}, {u} (la dirección, entre paréntesis) y {fecha}, que se
# forma con «fecha» y el mes de «meses», ya con la preposición o el caso que pide cada idioma.
VCER = {
    "es": {"cab": "Evaluación VCER del recurso",
           "recurso": {"t": "El recurso «{t}»", "tv": "La versión {v} del recurso «{t}»",
                       "": "El recurso del que procede este enlace", "v": "La versión {v} del recurso del que procede este enlace"},
           "frase": "{recurso}{u} se evaluó con la rúbrica VCER{fecha}. Este es el resultado que declara su autoría:",
           "fecha": " en {mes} de {año}", "meses": MESES["es"], "pct": "{p} %",
           "nota": "Se trata de una autoevaluación orientativa, que no ha comprobado nadie más, y el recurso puede haber cambiado desde entonces.",
           "salidas": ("Leer la guía", "Crear con IA")},
    "ca": {"cab": "Avaluació VCER del recurs",
           "recurso": {"t": "El recurs «{t}»", "tv": "La versió {v} del recurs «{t}»",
                       "": "El recurs d'on prové aquest enllaç", "v": "La versió {v} del recurs d'on prové aquest enllaç"},
           "frase": "{recurso}{u} es va avaluar amb la rúbrica VCER{fecha}. Aquest és el resultat que en declara l'autoria:",
           "fecha": " {mes} de {año}", "meses": ["al gener", "al febrer", "al març", "a l'abril", "al maig", "al juny", "al juliol",
                                                 "a l'agost", "al setembre", "a l'octubre", "al novembre", "al desembre"], "pct": "{p} %",
           "nota": "Es tracta d'una autoavaluació orientativa, que ningú més no ha comprovat, i el recurs pot haver canviat des d'aleshores.",
           "salidas": ("Llegir la guia", "Crear amb IA")},
    "gl": {"cab": "Avaliación VCER do recurso",
           "recurso": {"t": "O recurso «{t}»", "tv": "A versión {v} do recurso «{t}»",
                       "": "O recurso do que procede esta ligazón", "v": "A versión {v} do recurso do que procede esta ligazón"},
           "frase": "{recurso}{u} avaliouse coa rúbrica VCER{fecha}. Este é o resultado que declara a súa autoría:",
           "fecha": " en {mes} de {año}", "meses": MESES["gl"], "pct": "{p} %",
           "nota": "Trátase dunha autoavaliación orientativa, que ninguén máis comprobou, e o recurso pode ter cambiado desde entón.",
           "salidas": ("Ler a guía", "Crear con IA")},
    "eu": {"cab": "Baliabidearen VCER ebaluazioa",
           "recurso": {"t": "«{t}» baliabidea", "tv": "«{t}» baliabidearen {v} bertsioa",
                       "": "Esteka honen jatorriko baliabidea", "v": "Esteka honen jatorriko baliabidearen {v} bertsioa"},
           "frase": "{recurso}{u} VCER errubrikarekin ebaluatu zen{fecha}. Hau da egileek adierazten duten emaitza:",
           "fecha": " {año}ko {mes}", "meses": ["urtarrilean", "otsailean", "martxoan", "apirilean", "maiatzean", "ekainean", "uztailean",
                                                "abuztuan", "irailean", "urrian", "azaroan", "abenduan"], "pct": "% {p}",
           "nota": "Autoebaluazio orientagarria da, beste inork egiaztatu ez duena, eta baliteke baliabidea ordutik aldatu izana.",
           "salidas": ("Gida irakurri", "IArekin sortu")},
    "en": {"cab": "VCER evaluation of the resource",
           "recurso": {"t": "The resource «{t}»", "tv": "Version {v} of the resource «{t}»",
                       "": "The resource this link comes from", "v": "Version {v} of the resource this link comes from"},
           "frase": "{recurso}{u} was evaluated with the VCER rubric{fecha}. This is the result stated by its authors:",
           "fecha": " in {mes} {año}", "meses": MESES["en"], "pct": "{p} %",
           "nota": "This is an indicative self-assessment that nobody else has checked, and the resource may have changed since then.",
           "salidas": ("Read the guide", "Creating with AI")},
}
# Los valores de r en el enlace, en el orden de las filas de la tabla de resultados de 06-evaluacion-vcer.md.
# Son los mismos en todos los idiomas, porque el enlace no depende del idioma del recurso.
RESULTADOS_VCER = ["recomendable", "mejorable", "no-recomendable"]
# El apartado «Para evaluar un recurso ya hecho» estuvo en para-la-ia.html hasta la versión 2.0, y hay
# enlaces a él publicados fuera de la guía. guia.js los lleva a su sitio nuevo, en vcer.html (ADR 21).
ANCLA_EVALUAR_ANTIGUA = {"es": "para-evaluar-un-recurso-ya-hecho", "ca": "per-avaluar-un-recurs-ja-fet",
                         "gl": "para-avaliar-un-recurso-xa-feito", "eu": "egindako-baliabide-bat-ebaluatzeko",
                         "en": "to-evaluate-an-existing-resource"}

# El vídeo de la animación que abre la portada (ADR 17) y su cartel, relativos a la carpeta del idioma.
VIDEO = "../animacion/vibe-responsable-zoom.{idioma}.mp4"
CARTEL_VIDEO = "../animacion/vibe-responsable-zoom.{idioma}.jpg"


def video(idioma):
    """El vídeo de la portada y su cartel en el idioma de la página o, si no lo hay, en castellano (ADR 20)."""
    for i in (idioma, "es"):
        if (RAIZ / "es" / VIDEO.format(idioma=i)).resolve().exists():
            return VIDEO.format(idioma=i), CARTEL_VIDEO.format(idioma=i), i
    return None

PAGINAS = [("index.html", "00-presentacion.md"), ("guia.html", "01-guia.md"),
           ("herramientas.html", "02-herramientas.md"), ("para-la-ia.html", "04-para-la-ia.md"),
           ("vcer.html", "06-evaluacion-vcer.md"), ("referencias.html", "05-referencias.md")]


def version(ruta):
    """Marca que cambia con el contenido del archivo. Va en su dirección (?v=…) para que el
    navegador no siga usando una copia antigua de los estilos o del script tras actualizar."""
    return hashlib.sha256((RAIZ / ruta).read_bytes()).hexdigest()[:10]


def pandoc(md):
    r = subprocess.run(["pandoc", "-f", "markdown-auto_identifiers+link_attributes", "-t", "html5", "--wrap=none"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def sin_notas(md):
    """Quita las notas de trabajo (<!-- … -->) del Markdown. Los marcadores de una sola
    palabra, como <!-- rubrica -->, se conservan porque el generador los sustituye."""
    return re.sub(r"<!--(?!\s*[\w-]+\s*-->).*?-->\n?", "", md, flags=re.S)


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


def anclas_de(idioma, fuente):
    """Las anclas de los apartados (##) de una página, en su orden, para enlazarlos en cualquier idioma."""
    md = (RAIZ / "contenido" / idioma / fuente).read_text(encoding="utf-8")
    return [ancla(c) for c in re.findall(r"^## (.+)$", md, flags=re.M)]


def titulo_de(md):
    return re.match(r"#\s+(.*)", md).group(1).strip()


def marco(idioma, archivo, titulo, cuerpo, clase, propio=None):
    """Cabecera, navegación y pie comunes a todas las páginas.

    «archivo» es la entrada del menú que se marca; «propio», el archivo de la página cuando no
    coincide con ella (un capítulo se marca como la guía), para enlazarla en los otros idiomas."""
    T = UI[idioma]
    propio = propio or archivo
    destino_idioma = "" if propio == "index.html" else propio
    alternativas = "\n".join(f'<link rel="alternate" hreflang="{i}" href="{URL_SITIO}{i}/{destino_idioma}">' for i in IDIOMAS)
    idiomas = "".join(f'<a role="menuitem" href="../{i}/{destino_idioma}" hreflang="{i}" lang="{i}"'
                      + (' aria-current="true"' if i == idioma else "") + f'>{html.escape(NOMBRES_IDIOMAS[i])}</a>'
                      for i in IDIOMAS)
    # El menú lleva también los créditos, donde está la forma de citar la guía
    entradas = PAGINAS + [("creditos.html", "03-creditos.md")]
    titulos = {a: titulo_de((RAIZ / "contenido" / idioma / m).read_text(encoding="utf-8")) for a, m in entradas}
    nav = []
    for a, _ in entradas:
        rotulo = T["nav_cortos"].get(a, titulos[a])
        destino = "./" if a == "index.html" else a
        actual = ' aria-current="page"' if a == archivo else ""
        nav.append(f'<li><a href="{destino}"{actual}>{html.escape(rotulo)}</a></li>')
    pag = f"""<!DOCTYPE html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} | {html.escape(T["nombre"])}</title>
<meta name="description" content="{html.escape(T["nombre"])}: {html.escape(T["guia"][0].lower() + T["guia"][1:])}. {html.escape(titulo)}.">
<meta name="author" content="Juan José de Haro">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
<meta property="og:title" content="{html.escape(titulos["guia.html"])}">
<meta property="og:description" content="{html.escape(T["guia"])}">
<meta property="og:image" content="{URL_SITIO}infografia/lista-iconos.{idioma}.png">
<meta property="og:type" content="article">
{alternativas}
<link rel="icon" href="../recursos/logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="../recursos/logo/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="../recursos/logo/apple-touch-icon.png">
<link rel="preload" href="../recursos/fuentes/atkinson-hyperlegible-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../recursos/estilos.css?v={version("recursos/estilos.css")}">
<script>(function(){{try{{var t=localStorage.getItem("{CLAVE_TEMA}");if(t!=="light"&&t!=="dark"){{t=matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";}}document.documentElement.dataset.theme=t;}}catch(e){{}}}})();</script>
<script src="../recursos/guia.js?v={version("recursos/guia.js")}" defer></script>
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">{html.escape(T["saltar"])}</a>
<header class="pizarra">
<div class="ancho pizarra-int">
<div class="sitio"><a class="sitio-guia" href="./"><img class="marca" src="../recursos/logo/logo.svg" alt="" width="30" height="30"><span>{html.escape(T["nombre"])}</span></a>
<span class="sitio-desc">{html.escape(T["guia"])}</span>
</div>
<nav aria-label="{html.escape(T["nav"])}"><ul>{"".join(nav)}</ul></nav>
<div class="utiles">
<div class="desplegable">
<button type="button" class="idiomas" title="{html.escape(T["idioma"])}" aria-label="{html.escape(T["idioma"])}" aria-haspopup="menu" aria-expanded="false">{icono("languages")}</button>
<div class="menu menu-idiomas" role="menu" hidden>{idiomas}</div>
</div>
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


def ventanas_ia(idioma):
    """Una ventana por archivo para la IA, que abren los enlaces de «Cómo empezar»: una instrucción
    breve, copiar, descargar y el enlace a la página completa. El texto del archivo va oculto, solo
    para copiarlo; quien quiera leerlo va a la página. Sin JavaScript, el enlace lleva a la página."""
    T = UI[idioma]
    ventanas = []
    # El archivo para crear está en para-la-ia.html; el de evaluar, en vcer.html, en «Cómo evaluar un recurso»
    destinos = {"instrucciones": "para-la-ia.html#" + anclas_de(idioma, "04-para-la-ia.md")[1],
                "evaluacion": "vcer.html#" + anclas_de(idioma, "06-evaluacion-vcer.md")[3]}
    for clave, destino in destinos.items():
        titulo, texto = T["ventana_ia"][clave]
        ventanas.append(f"""<dialog class="ventana-ia" id="ventana-{clave}" aria-labelledby="ventana-{clave}-titulo">
<div class="ventana-cab"><h2 id="ventana-{clave}-titulo">{html.escape(titulo)}</h2>
<button type="button" class="ventana-cerrar" aria-label="{html.escape(T["cerrar"])}" title="{html.escape(T["cerrar"])}">{icono("x")}</button></div>
<p>{html.escape(texto)}</p>
<div class="copiable ventana-botones">
<button type="button" class="copiar" data-hecho="{html.escape(T["copiado"])}" title="{html.escape(T["copiar_titulo"])}">{icono("copy")}<span>{html.escape(T["copiar"])}</span></button>
<a class="boton" href="{ARCHIVOS_IA[clave][1]}" download title="{html.escape(T["descargar_titulo"])}">{icono("download")}{html.escape(T["descargar_archivo"])}</a>
<pre hidden>{html.escape(archivo_ia(idioma, clave))}</pre>
</div>
<p class="ventana-mas"><a href="{destino}" title="{html.escape(T["mas_informacion_titulo"][clave])}">{html.escape(T["mas_informacion"])}{icono("arrow-right")}</a></p>
</dialog>""")
    return "\n".join(ventanas)


def ventana_animacion(idioma):
    """La animación en vídeo, en una ventana (ADR 17). El vídeo se descarga solo al abrirla, empieza
    a sonar con la misma pulsación y se detiene al cerrarla. Al terminar muestra «Volver a ver», porque
    el botón del reproductor apenas se distingue sobre el fotograma final. Sin JavaScript, el botón
    abre el vídeo."""
    T = UI[idioma]
    return f"""<dialog class="ventana-ia ventana-animacion" id="ventana-animacion" aria-labelledby="ventana-animacion-titulo">
<div class="ventana-cab"><h2 id="ventana-animacion-titulo">{html.escape(T["animacion_titulo"])}</h2>
<button type="button" class="ventana-cerrar" aria-label="{html.escape(T["cerrar"])}" title="{html.escape(T["cerrar"])}">{icono("x")}</button></div>
<div class="video-marco"><video data-src="{video(idioma)[0]}" poster="{video(idioma)[1]}" lang="{video(idioma)[2]}" controls playsinline preload="none"></video>
<button type="button" class="volver-a-ver" hidden>{icono("rotate-ccw")}{html.escape(T["volver_a_ver"])}</button></div>
</dialog>"""


def pagina_presentacion(idioma):
    """Portada: el texto en dos columnas y, al lado, el resumen gráfico."""
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
    hay_animacion = video(idioma) is not None
    if hay_animacion:
        tarjeta += (f'<a class="ver-animacion abrir-ventana" data-ventana="ventana-animacion" href="{video(idioma)[0]}">'
                    f'{icono("play")}{html.escape(T["ver_animacion"])}</a>')
    # Las notas del pie de la portada, que vienen del Markdown, como «Cómo se ha elaborado».
    # «Cómo citar» está de momento en créditos (<!-- cita --> en 03-creditos.md); volverá aquí.
    notas = '<div class="notas">' + "".join(bloque(i, "nota") for i in range(3, len(apartados))) + "</div>"
    # El botón que lleva a la guía sale de «Cómo se utiliza» y va bajo la imagen.
    cab, h = apartados[2]
    boton = re.search(r'<p><a [^>]*class="continuar"[^>]*>.*?</a></p>', h)
    apartados[2] = (cab, h.replace(boton.group(0), "").strip())
    boton = boton.group(0).replace("<p>", '<p class="ir-guia">', 1)
    # Todo el texto va seguido, para que en pantalla ancha fluya en dos columnas sin huecos
    # (un apartado puede empezar en una y seguir en la otra); la imagen, aparte, a la derecha.
    cuerpo = f"""<h1>{html.escape(titulo)}</h1>
<div class="entrada" {medidas}>
<div class="textos">
{bloque(0, "columna")}
{bloque(1, "columna")}
{bloque(2, "utiliza")}
{notas}
</div>
<aside class="paso-guia">{tarjeta}</aside>
{boton}
</div>
{visor(idioma)}
{ventanas_ia(idioma)}
{ventana_animacion(idioma) if hay_animacion else ""}"""
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
                 else f'<a class="ayuda-niveles" href="herramientas.html#{anclas_de(idioma, "02-herramientas.md")[2]}">{html.escape(T["niveles_ayuda"])}</a>')
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

    # Las filas se agrupan por fases: cada una, un elemento con su rótulo y su propia lista numerada
    inicios = sorted(T["fases"]) + [total + 1]
    fases = []
    for k, (a, b) in enumerate(zip(inicios, inicios[1:]), start=1):
        verbo, complemento = T["fases"][a]
        fases.append(f'<li class="fase" aria-labelledby="fase-{k}">'
                     f'<div class="fase-cab"><span class="fase-rotulo" id="fase-{k}"><span>{html.escape(verbo)}</span> '
                     f'<span>{html.escape(complemento)}</span></span></div>'
                     f'<ol class="fase-puntos" start="{a}">{"".join(filas[a - 1:b - 1])}</ol></li>')
    cuerpo = f"""<h1>{html.escape(titulo)}</h1>
<div class="tablero">
<section class="hoja" aria-label="{html.escape(titulo)}">
<ul class="diez">{"".join(fases)}</ul>
</section>
<div class="panel"></div>
</div>"""
    return marco(idioma, "guia.html", titulo, cuerpo, "pagina-lista")


def archivo_ia(idioma, clave):
    return (RAIZ / "contenido" / idioma / ARCHIVOS_IA[clave][0]).read_text(encoding="utf-8")


def tabla_rubrica(idioma):
    """La rúbrica del archivo de evaluación, en una tabla: una fila por punto y una columna por
    puntuación. Sale del propio archivo, para que la tabla y lo que lee la IA no se separen."""
    T = UI[idioma]
    caps = capitulos(idioma)
    texto = archivo_ia(idioma, "evaluacion")
    bloque = texto[texto.index("\n1. ") + 1:texto.index("\n## ", texto.index("\n1. "))]
    filas = []
    for punto in re.split(r"\n\s*\n", bloque.strip()):
        cab = re.match(r"(\d+)\.\s+([^\n]+)", punto)
        niveles = {n: " ".join(t.split()) for n, t in re.findall(r"^\s+([012]):\s+(.*?)(?=^\s+[012]:|^\s{3}\S|\Z)", punto, flags=re.S | re.M)}
        nombre = cab.group(2).strip()
        nota = re.search(r"\((.*?)\)", nombre)
        nombre = re.sub(r"\s*\(.*?\)", "", nombre).capitalize()
        for sigla in T.get("siglas", ["IA"]):   # las siglas vuelven a mayúsculas
            nombre = re.sub(rf"\b{sigla}\b", sigla, nombre, flags=re.I)
        n = int(cab.group(1))
        nombre = f'<a href="{caps[n][0]}">{html.escape(nombre)}</a>' if n in caps else html.escape(nombre)
        celda = f'<th scope="row"><span class="rub-n">{n}</span> {nombre}' + (f' <small>({html.escape(nota.group(1))})</small>' if nota else "") + "</th>"
        filas.append("<tr>" + celda + "".join(f'<td data-nota="{n}">{html.escape(niveles.get(n, ""))}</td>' for n in "210") + "</tr>")
    cabecera = "".join(f'<th scope="col">{n}</th>' for n in "210")
    return (f'<div class="rubrica"><table><caption>{html.escape(T["rubrica"])}</caption><thead><tr><th scope="col">{html.escape(T["punto"])}</th>{cabecera}</tr></thead>'
            f'<tbody>{"".join(filas)}</tbody></table></div>')


def resultado_vcer(idioma):
    """El recuadro que muestra el resultado traído por el enlace de la mención. Va oculto: guia.js lo
    rellena y lo muestra solo si el enlace trae un resultado válido. Sus textos viajan en un JSON."""
    V = dict(VCER[idioma])
    V.pop("salidas")
    datos = json.dumps(V, ensure_ascii=False).replace("</", "<\\/")
    return (f'<section class="resultado-vcer" aria-labelledby="h-resultado-vcer" hidden>'
            f'<h2 id="h-resultado-vcer">{html.escape(VCER[idioma]["cab"])}</h2>'
            f'<p class="rv-frase"></p>'
            f'<p class="rv-resultado"><strong class="rv-nombre"></strong><span class="rv-pct"></span></p>'
            f'<div class="rv-barra" aria-hidden="true"><span class="rv-relleno"></span><span class="rv-umbral"></span></div>'
            f'<p class="rv-significado"></p>'
            f'<p class="rv-nota"></p>'
            f'<script type="application/json" class="rv-textos">{datos}</script></section>')


def pagina_texto(idioma, archivo, fuente):
    T = UI[idioma]
    md = sin_notas((RAIZ / "contenido" / idioma / fuente).read_text(encoding="utf-8"))
    titulo = titulo_de(md)
    apartados = re.split(r"^## ", md.split("\n", 1)[1], flags=re.M)[1:]
    secciones = []
    for a in apartados:
        cab, resto = a.split("\n", 1)
        cab = cab.strip()
        resto = resto.replace("<!-- rubrica -->", "ARCHIVO-IA-RUBRICA").replace("<!-- cita -->", "CITA-DE-LA-GUIA")
        for clave in ARCHIVOS_IA:
            resto = resto.replace(f"<!-- {clave} -->", f"ARCHIVO-IA-{clave}\n\n~~~~\n" + archivo_ia(idioma, clave) + "~~~~")
        h = pandoc(resto.strip())
        if archivo == "herramientas.html":
            h = h.replace("<ul>", '<ul class="familias">', 1)
        botones = '<div class="copiable"><p class="copiable-cab solo-js">'
        copiar = f'<button type="button" class="copiar discreto" data-hecho="{html.escape(T["copiado"])}">{html.escape(T["copiar"])}</button></p>'
        # Un archivo para la IA lleva además su enlace de descarga, y su texto va plegado para no
        # ocupar la página; cualquier otro bloque lleva solo el botón de copiar
        if archivo == "vcer.html" and "<table>" in h:
            # Cada fila de la tabla de resultados, con su valor de r, para resaltar la que trae el enlace
            filas = iter(RESULTADOS_VCER)
            cuerpo_tabla = h[h.index("<tbody>"):h.index("</tbody>")]
            h = h.replace(cuerpo_tabla, re.sub(r"<tr(?: class=\"\w+\")?>", lambda m: f'<tr data-resultado="{next(filas)}">', cuerpo_tabla))
            h = h.replace("<table>", '<table class="resultados-vcer">', 1)
        h = h.replace("<p>ARCHIVO-IA-RUBRICA</p>", tabla_rubrica(idioma))
        h = h.replace("<p>CITA-DE-LA-GUIA</p>", f'<p>{T["cita"]}</p>\n<p>{T["cita_nota"]}</p>')   # la misma que la portada del PDF
        h = re.sub(r"<p>ARCHIVO-IA-(\w+)</p>\s*<pre[^>]*>(.*?)</pre>",
                   lambda m: botones + f'<a class="descarga" href="{ARCHIVOS_IA[m.group(1)][1]}" download>'
                             f'{icono("download")}{html.escape(T["descargar_archivo"])}</a>' + copiar +
                             f'<details class="archivo-ia"><summary>{html.escape(T["ver_archivo"][m.group(1)])}</summary>'
                             f'<pre>{m.group(2)}</pre></details></div>', h, flags=re.S)
        h = re.sub(r"(?<!</summary>)<pre[^>]*>(.*?)</pre>",
                   lambda m: botones + copiar + f"<pre>{m.group(1)}</pre></div>", h, flags=re.S)
        cuerpo_apartado = f'<div class="texto">{h}</div>'
        secciones.append(f'<section class="apartado" id="{ancla(cab)}" aria-labelledby="h-{ancla(cab)}">'
                         f'<h2 id="h-{ancla(cab)}">{html.escape(cab)}</h2>{cuerpo_apartado}</section>')
    cuerpo = f'<h1>{html.escape(titulo)}</h1>\n' + "\n".join(secciones)
    clase = "pagina-texto pagina-referencias" if archivo == "referencias.html" else "pagina-texto"
    if archivo == "para-la-ia.html":
        mudado = {ANCLA_EVALUAR_ANTIGUA[idioma]: "vcer.html#" + anclas_de(idioma, "06-evaluacion-vcer.md")[3]}
        cuerpo += f"<div hidden data-mudado='{html.escape(json.dumps(mudado), quote=False)}'></div>"
    if archivo == "vcer.html":
        # Arriba, el resultado que trae el enlace, si lo trae; al final, las salidas al resto de la guía
        leer, crear = VCER[idioma]["salidas"]
        salidas = (f'<p class="salidas-vcer"><a class="continuar" href="guia.html">{html.escape(leer)}</a> '
                   f'<a class="continuar" href="para-la-ia.html">{html.escape(crear)}</a></p>')
        cuerpo = cuerpo.replace("</h1>\n", "</h1>\n" + resultado_vcer(idioma) + "\n", 1) + salidas
        clase += " pagina-vcer"
    return marco(idioma, archivo, titulo, cuerpo, clase)


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
              + f'<nav class="entre-capitulos" aria-label="{html.escape(T["nav_capitulos"])}">{ant}'
                f'<a href="guia.html">{html.escape(T["volver_guia"])}</a>{sig}</nav>')
    return marco(idioma, "guia.html", titulo, cuerpo, "pagina-texto pagina-capitulo", propio=archivo)


# El PDF se justifica con el guionado de Chromium (hyphens: auto), que solo pone el guion
# donde corta la línea y deja limpio el texto para buscar y copiar. Chromium no trae
# diccionario para estos idiomas; en ellos los guiones opcionales los pone Pyphen, con los
# diccionarios de LibreOffice. Comprobado en septiembre de 2026 con es, ca, gl, eu, en, fr,
# it y pt: solo falta el catalán. Al añadir un idioma, comprobar si Chromium lo parte.
SIN_GUIONADO_CHROMIUM = {"ca"}
GUIONADO = {"en": "en_US"}   # diccionario de Pyphen para cada idioma, si no se llama igual


def guionar(h, idioma):
    """Inserta guiones opcionales (&shy;) en las palabras del texto para justificarlo en el PDF.

    No toca etiquetas, código ni direcciones. En catalán no parte por la ele geminada
    («col·laboració»), porque la norma cambia la grafía al partir y un guion opcional no puede."""
    if idioma not in SIN_GUIONADO_CHROMIUM:
        return h
    import pyphen
    dic = pyphen.Pyphen(lang=GUIONADO.get(idioma, idioma), left=2, right=3)
    def palabra(m):
        w = m.group()
        pos = [p for p in dic.positions(w) if w[p - 1] != "·"]
        for p in reversed(pos):
            w = w[:p] + "\u00ad" + w[p:]
        return w
    partes, dentro = [], 0
    for trozo in re.split(r"(<[^>]+>)", h):
        if trozo.startswith("<"):
            etiqueta = re.match(r"</?(\w+)", trozo)
            if etiqueta and etiqueta.group(1) in ("pre", "code", "script", "style"):
                dentro += -1 if trozo.startswith("</") else 1
        elif not dentro:
            # Las direcciones y los nombres de archivo (con «/», «@» o un punto entre letras) no se parten
            trozo = re.sub(r"\S+", lambda t: t.group() if re.search(r"[/@]|\w\.\w", t.group()) else
                           re.sub(r"[^\W\d_](?:[^\W\d_]|·)*[^\W\d_]", lambda m: palabra(m) if len(m.group()) >= 6 else m.group(), t.group()),
                           trozo)
        partes.append(trozo)
    return "".join(partes)


def pagina_completa(idioma, paginas):
    """Todas las páginas seguidas, con portada e índice, para imprimirlas a PDF (generar-pdf.js).

    Orden de lectura: presentación, guía, los capítulos que la desarrollan, herramientas,
    instrucciones para crear con IA, evaluación VCER, referencias y créditos. Los enlaces entre páginas pasan a ser anclas."""
    T = UI[idioma]
    d = FECHA_VERSION
    fecha = T["version_fecha"].format(version=VERSION, fecha=T["fecha"](d))
    caps = capitulos(idioma)
    titulos = {a: titulo_de((RAIZ / "contenido" / idioma / m).read_text(encoding="utf-8")) for a, m in PAGINAS}
    titulos["creditos.html"] = titulo_de((RAIZ / "contenido" / idioma / "03-creditos.md").read_text(encoding="utf-8"))
    titulos["referencias.html"] = titulo_de((RAIZ / "contenido" / idioma / "05-referencias.md").read_text(encoding="utf-8"))
    orden = [("index.html", titulos["index.html"]), ("guia.html", titulos["guia.html"])]
    orden += [(a, f"{T['capitulo'].format(n=n)}. {t}") for n, (a, t, _) in sorted(caps.items())]
    orden += [(a, titulos[a]) for a in ("herramientas.html", "para-la-ia.html", "vcer.html", "referencias.html", "creditos.html")]
    partes, indice = [], []
    for archivo, titulo in orden:
        clave = archivo[:-5]
        cuerpo = re.search(r'<main id="contenido" class="ancho">(.*)</main>', paginas[archivo], flags=re.S).group(1)
        cuerpo = re.sub(r'href="[a-z0-9-]+\.html#', 'href="#', cuerpo)
        cuerpo = re.sub(r'href="([a-z0-9-]+)\.html"', r'href="#pagina-\1"', cuerpo)
        cuerpo = cuerpo.replace('href="./"', 'href="#pagina-index"')
        cuerpo = cuerpo.replace('<details class="archivo-ia">', '<details class="archivo-ia" open>')   # en el PDF, desplegados
        # Las tablas cortas van enteras en una página; las largas, como la rúbrica, se reparten.
        cuerpo = re.sub(r"<table>(.*?</table>)", lambda m: ('<table class="entera">' if m.group(1).count("<tr") <= 6 else "<table>") + m.group(1), cuerpo, flags=re.S)
        partes.append(f'<section class="pdf-pagina" id="pagina-{clave}">{guionar(cuerpo, idioma)}</section>')
        indice.append(f'<li><a href="#pagina-{clave}">{html.escape(titulo)}</a></li>')
    return f"""<!DOCTYPE html>
<html lang="{idioma}" data-theme="light">
<head>
<meta charset="utf-8">
<title>{html.escape(T["nombre"])}</title>
<link rel="stylesheet" href="../recursos/estilos.css?v={version("recursos/estilos.css")}">
<style>
/* Solo para la impresión a PDF de la guía completa */
.pdf {{ background: #fff; color: #000; }}
.pdf .ancho {{ max-width: none; padding: 0; }}
.pdf-portada {{ break-after: page; min-height: 240mm; display: flex; flex-direction: column; }}
.pdf-portada .marca {{ width: 3.2rem; height: 3.2rem; margin-bottom: 1.2rem; }}
.pdf-portada .pdf-comunidad {{ margin: 0; font-weight: 700; color: var(--verde); }}
.pdf-portada h1 {{ font-size: 2.4rem; margin: 0.4rem 0 0.6rem; }}
.pdf-portada .pdf-sub {{ font-size: 1.15rem; margin: 0 0 1.6rem; color: #333; }}
.pdf-portada .pdf-autor {{ font-size: 1.15rem; font-weight: 700; margin: 0 0 0.4rem; }}
.pdf-portada .pdf-fecha {{ margin: 0 0 3rem; color: #333; }}
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
.pdf .familias {{ margin: 0; }}
.pdf .familias li {{ padding: 0.3rem 0 0.3rem; }}
.pdf .familias strong:first-child {{ margin-bottom: 0; }}
.pdf .apartado {{ display: block; padding: 0.8rem 0 0.2rem; }}
.pdf .apartado h2 {{ margin-bottom: 0.4rem; }}
.pdf .entrada {{ display: flex; flex-direction: column; gap: 1rem; }} /* la rejilla de la web no se reparte bien entre páginas */
.pdf .tarjeta {{ border: 0; box-shadow: none; padding: 0; margin: 1rem 0; break-before: page; }}
.pdf .tarjeta .miniatura {{ width: 10cm !important; height: auto !important; margin: 0 auto; border: 1px solid #bbb; }}
/* Las diez recomendaciones: sin la fila plegable de la web ni el recuadro de la lista,
   que se partía entre páginas; cada recomendación, entera en una página. */
.pdf .hoja {{ border: 0; border-radius: 0; box-shadow: none; overflow: visible; }}
.pdf .punto > .fila {{ display: none; }}
.pdf .punto {{ break-inside: avoid; padding: 1rem 0 0.2rem; }}
.pdf .punto + .punto {{ border-top: 1px solid #bbb; }}
.pdf .punto > .detalle {{ border-top: 0; }}
.pdf .detalle-caja {{ padding: 0; }}
/* El número del capítulo, separado del título como en la web */
.pdf h1:has(> .cifra-cap) {{ display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.7rem; align-items: center; }}
/* Ningún título solo al pie de página, ni recuadros o filas partidos, ni líneas sueltas */
.pdf h1, .pdf h2, .pdf h3, .pdf h4 {{ break-after: avoid; }}
.pdf p:has(+ ol), .pdf p:has(+ ul) {{ break-after: avoid; }} /* la frase que presenta una lista va con ella */
.pdf .que-hacer, .pdf .nivel, .pdf li, .pdf tr, .pdf .nota {{ break-inside: avoid; }}
/* Portada: las definiciones enteras, y los tres pasos en fila y juntos, como en pantalla */
.pdf .definicion, .pdf .utiliza {{ break-inside: avoid; }}
.pdf .utiliza ul {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
.pdf .textos > .utiliza {{ order: 0; }} /* tras el texto, en su página; la infografía va en la siguiente */
/* Dos líneas como mínimo a cada lado del salto. Con tres, un párrafo de cuatro o cinco
   líneas no puede cumplir las dos reglas a la vez, y Chromium deja una línea sola. */
.pdf p {{ orphans: 2; widows: 2; }}
/* Texto justificado con partición de palabras (véase SIN_GUIONADO_CHROMIUM); las tablas,
   de columnas estrechas, siguen alineadas a la izquierda. */
.pdf-pagina p, .pdf-pagina li {{ text-align: justify; hyphens: auto; }}
.pdf td p, .pdf th p, .pdf td, .pdf th, .pdf .utiliza li {{ text-align: left; }}
.pdf table.entera {{ break-inside: avoid; }}
.pdf .copiable pre {{ orphans: 4; widows: 4; -webkit-box-decoration-break: clone; box-decoration-break: clone; }}
.pdf .descarga, .pdf #como-citar {{ display: none; }} /* la cita ya va en la portada */
.pdf a {{ color: inherit; text-decoration: none; }}
.pdf .pdf-indice a, .pdf .texto a[href^="http"], .pdf .explicacion a[href^="http"] {{ color: var(--verde); }}
</style>
</head>
<body class="pdf" data-pie="{html.escape(T["pie_pdf"].format(fecha=fecha))}">
<section class="pdf-portada">
<img class="marca" src="../recursos/logo/logo.svg" alt="" width="54" height="54">
<p class="pdf-comunidad">{html.escape(T["comunidad"])}</p>
<h1>{html.escape(T["nombre"])}</h1>
<p class="pdf-sub">{html.escape(T["guia"])}</p>
<p class="pdf-autor">{html.escape(T["autor"])}</p>
<p class="pdf-fecha">{html.escape(fecha)}</p>
<div class="pdf-cita"><h2>{html.escape(T["citar"])}</h2><p>{T["cita"]}</p><p>{T["cita_nota"]}</p>
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
<title>{html.escape(UI["es"]["nombre"])}</title>
<link rel="icon" href="recursos/logo/favicon.svg" type="image/svg+xml">
<meta http-equiv="refresh" content="0; url=es/">
<link rel="canonical" href="{URL_SITIO}es/">
<script>
var d=[{disponibles}],n=(navigator.languages||[navigator.language||"es"]).map(function(x){{return x.slice(0,2);}});
var e=n.filter(function(x){{return d.indexOf(x)>-1;}})[0]||"es";location.replace(e+"/");
</script>
</head>
<body><p><a href="es/">{html.escape(UI["es"]["nombre"])}</a></p></body>
</html>
"""


def entrada_vcer():
    """vcer/index.html, la dirección del enlace de la mención (ADR 21). No lleva idioma, porque el
    recurso evaluado puede estar en cualquiera: envía a la página del idioma del navegador, o a la
    castellana, con los datos del enlace intactos."""
    disponibles = ",".join(f'"{i}"' for i in IDIOMAS)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(UI["es"]["nombre"])}</title>
<link rel="icon" href="../recursos/logo/favicon.svg" type="image/svg+xml">
<script>
var d=[{disponibles}],n=(navigator.languages||[navigator.language||"es"]).map(function(x){{return x.slice(0,2);}});
var e=n.filter(function(x){{return d.indexOf(x)>-1;}})[0]||"es";location.replace("../"+e+"/vcer.html"+location.search);
</script>
<meta http-equiv="refresh" content="0; url=../es/vcer.html">
<link rel="canonical" href="{URL_SITIO}es/vcer.html">
</head>
<body><p><a href="../es/vcer.html">{html.escape(UI["es"]["nombre"])}</a></p></body>
</html>
"""


def comprobar_referencias(idioma):
    """Cada enlace externo del texto debe estar en 05-referencias.md, y al revés.

    Quedan fuera los créditos, que hablan de la propia guía. Devuelve dos listas: las
    direcciones citadas que faltan en las referencias y las referencias que ya no se citan."""
    carpeta = RAIZ / "contenido" / idioma
    patron = r'\]\((https?://[^)\s]+)\)'
    citados = {}
    for md in sorted(carpeta.glob("*.md")) + sorted((carpeta / "capitulos").glob("*.md")):
        if md.name in ("03-creditos.md", "05-referencias.md"):
            continue
        for url in re.findall(patron, md.read_text(encoding="utf-8")):
            citados.setdefault(url, md.name)
    patron_url = r"https?://[^\s)>\]]+"
    texto_referencias = (carpeta / "05-referencias.md").read_text(encoding="utf-8")
    referencias = set(re.findall(patron_url, texto_referencias))
    # Cada entrada es una línea de la lista; puede dar varias direcciones de la misma obra
    # (el DOI y la edición web), y basta con que el texto cite una de ellas.
    entradas = [urls for urls in (re.findall(patron_url, l) for l in texto_referencias.splitlines() if l.startswith("- ")) if urls]
    # Una dirección cuenta como citada si la referencia es la misma página sin sus parámetros
    # (…/miae/?nivel=4), la portada de esa web citada en un idioma (…/miae/es/ → …/miae/)
    # o la portada de la obra a la que pertenece la página (…/html/apartado.html →
    # …/index.html), porque la referencia recoge la obra y el enlace del texto, el apartado;
    # una referencia con parámetros propios no vale para otra.
    portadas = {r for r in referencias if r.endswith("/index.html")}
    def variantes(url):
        base = url.split("?")[0]
        v = {url, base}
        idioma_final = re.match(r"(.*/)(es|ca|gl|eu|en)/$", base)
        if idioma_final:
            v.add(idioma_final.group(1))
        v.update(p for p in portadas if base.startswith(p[:-len("index.html")]))
        return v
    faltan = [f"{url} ({md})" for url, md in citados.items() if not (variantes(url) & referencias)]
    citadas = set().union(*(variantes(u) for u in citados)) if citados else set()
    sobran = [urls[0] for urls in entradas
              if not set(urls) & citadas and not any(u.startswith(URL_SITIO.rstrip("/")) for u in urls)]
    return faltan, sobran


def comprobar_enlaces_internos(idioma):
    """Revisa que cada enlace interno de las páginas generadas lleve a un archivo y a un ancla que existen."""
    base, rotos = RAIZ / idioma, []
    ids = {}   # anclas de cada página enlazada, también fuera de la carpeta del idioma (la animación)
    def anclas(pagina):
        if pagina not in ids:
            ids[pagina] = set(re.findall(r'id="([^"]+)"', pagina.read_text(encoding="utf-8")))
        return ids[pagina]
    for p in sorted(base.glob("*.html")):
        for href in re.findall(r'href="([^"]+)"', p.read_text(encoding="utf-8")):
            if re.match(r"(https?:|mailto:)", href):
                continue
            ruta, _, fragmento = href.partition("#")
            ruta = ruta.split("?")[0]   # la marca de versión (?v=…) no forma parte del archivo
            destino = p if not ruta else (base / ruta / "index.html" if ruta.endswith("/") or ruta == "./" else base / ruta)
            if not destino.resolve().exists():
                rotos.append(f"{p.name}: {href} (no existe)")
            elif fragmento and destino.suffix == ".html" and fragmento not in anclas(destino.resolve()):
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
        for fuente_ia, publicado in ARCHIVOS_IA.values():
            (destino / publicado).write_text((RAIZ / "contenido" / idioma / fuente_ia).read_text(encoding="utf-8"), encoding="utf-8")
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
    # Las comprobaciones, cuando ya están todos los idiomas, porque cada página enlaza las de los demás
    for idioma in IDIOMAS:
        rotos = comprobar_enlaces_internos(idioma)
        if rotos:
            print("ENLACES INTERNOS ROTOS:")
            for r in rotos:
                print("  ", r)
            raise SystemExit(1)
        faltan, sobran = comprobar_referencias(idioma)
        if faltan or sobran:
            print("REFERENCIAS (05-referencias.md):")
            for r in faltan:
                print("   falta la referencia de", r)
            for r in sobran:
                print("   ya no se cita en el texto:", r)
            raise SystemExit(1)
    (RAIZ / "index.html").write_text(portada(), encoding="utf-8")
    (RAIZ / "vcer").mkdir(exist_ok=True)
    (RAIZ / "vcer" / "index.html").write_text(entrada_vcer(), encoding="utf-8")
    (RAIZ / ".nojekyll").write_text("", encoding="utf-8")
