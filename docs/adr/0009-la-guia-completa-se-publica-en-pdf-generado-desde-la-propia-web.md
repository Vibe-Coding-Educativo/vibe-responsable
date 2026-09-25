# 9. La guía completa se publica en PDF, generado desde la propia web

Fecha: 2026-09-22 · Estado: aceptado

## Contexto

El autor quiere poder imprimir la guía entera y que cualquiera pueda hacerlo
desde la web, sin ir página por página. Además, cuando la guía deje de ser
borrador se depositará en Zenodo para obtener un DOI, y Zenodo necesita un
fichero cerrado, no una web. La guía tiene quince páginas (presentación, lista,
diez capítulos, herramientas, instrucciones para la IA y créditos) que salen del
Markdown de `contenido/` mediante `construir.py` ([ADR 4](0004-web-estatica-generada-desde-markdown.md)),
y el texto cambia con la revisión, así que un PDF montado a mano quedaría viejo
enseguida.

## Decisión

`python3 construir.py --pdf` genera, además de la web, la guía completa en
`es/vibe-responsable-es.pdf`, que se publica junto a las páginas. El nombre lleva
el idioma porque, una vez descargado, es lo único que lo indica.

El PDF sale de las mismas páginas que la web: `construir.py` junta el contenido
de todas en una sola página intermedia (`es/completo.html`, que no se publica y
está en `.gitignore`), con una portada, un índice enlazado y las páginas en el
orden de lectura: presentación, lista, los diez capítulos, herramientas,
instrucciones, referencias y créditos. Los enlaces entre páginas pasan a ser anclas dentro
del documento. La portada lleva el título, el autor, la fecha, el aviso de
borrador mientras lo sea, la licencia y el apartado «Cómo citar», con la misma
cita que la página de créditos de la web; cuando exista el DOI, se añadirá en
los dos sitios desde el mismo texto de `construir.py`. Cada página del PDF lleva
al pie el título de la guía, el autor, la licencia y el número de página.

La impresión la hace `generar-pdf.js` con el Chromium de Playwright, instalado
de forma global para todos los proyectos, sin añadir dependencias al
repositorio. El script sirve el repositorio por HTTP en un puerto libre mientras
imprime, porque con `file://` el navegador no carga la tipografía. Usa la misma
hoja de estilos que la web y sus reglas de impresión, que ocultan toda la
navegación y muestran el aviso de borrador.

Encima de ellas, el documento intermedio lleva reglas de composición propias,
porque lo que en pantalla se pliega o se reparte en rejillas no funciona en
papel. Sin JavaScript, la lista de recomendaciones mostraría a la vez cada fila
plegada y su detalle, así que en el PDF solo sale el detalle, sin el recuadro de
la lista, y cada recomendación va entera en una página. Las rejillas de la
presentación y de los apartados pasan a bloques, que Chromium reparte mejor
entre páginas. Ningún título queda solo al pie, los recuadros y las tablas
cortas (hasta seis filas) no se parten, y los párrafos y bloques de código no
dejan líneas sueltas. En los párrafos se piden dos líneas como mínimo a cada lado
del salto: con tres, un párrafo de cuatro o cinco líneas no puede cumplir las dos
reglas a la vez, y Chromium las relaja dejando una línea sola. En la
presentación, los tres pasos para empezar van en fila, sin partirse, justo después
del texto, y la infografía ocupa la página siguiente. Cada capítulo empieza en página nueva. Tras cambiar el
contenido o estas reglas, hay que repasar el PDF página por página, porque un
cambio de pocas líneas puede dejar una página casi vacía.

El texto corrido del PDF va justificado y con partición de palabras; las tablas,
de columnas estrechas, siguen alineadas a la izquierda. Parte las palabras el
propio Chromium (`hyphens: auto`, según el idioma de la página), que solo pone el
guion donde corta la línea y deja limpio el texto para buscar y copiar. Se
comprobó en septiembre de 2026 con los idiomas previstos para la traducción
(castellano, catalán, gallego, euskera, inglés, francés, italiano y portugués):
Chromium los parte todos menos el catalán. En los idiomas sin diccionario
(`SIN_GUIONADO_CHROMIUM` en `construir.py`), `guionar()` inserta guiones
opcionales con Pyphen, que usa los diccionarios de guionado de LibreOffice; en
ellos, esos guiones quedan también en el texto del PDF. No se parten las
direcciones, los nombres de archivo ni el código, y en catalán tampoco la ele
geminada, porque la norma cambia la grafía al partirla («col-/laboració») y un
guion opcional no puede hacerlo. Al añadir un idioma hay que comprobar si
Chromium lo parte. La web no se justifica: se lee en pantallas estrechas y en
navegadores con diccionarios distintos.

En la web, el botón de la impresora de la cabecera despliega dos opciones, cada
una con una línea que dice lo que hace: imprimir la página que se está viendo o
descargar la guía completa en PDF.

## Alternativas descartadas

- **Unir los PDF de cada página**: da portadas y pies inconsistentes, sin índice
  ni numeración seguida, y no resuelve los enlaces entre páginas.
- **Generar el PDF desde el Markdown con pandoc y LaTeX**: exigiría mantener
  una segunda maquetación y una instalación de LaTeX; el PDF dejaría de parecerse
  a la web.
- **Un enlace suelto al PDF en el pie o en la portada**: la portada no admite
  más contenido sin dejar de caber en una pantalla ([ADR 5](0005-portada-en-una-pantalla-y-varias-paginas.md)),
  y el pie es de una línea. Va con la acción de imprimir, que es de la misma
  familia.
- **Publicar la página intermedia como «versión para imprimir»**: repetiría
  todo el contenido en otra dirección.

## Consecuencias

Cada cambio de contenido exige regenerar el PDF con `--pdf` antes de publicar;
si se olvida, el PDF queda desfasado respecto a la web. Generarlo necesita
`node` y Playwright, que no hacen falta para la web. El PDF pesa unos 430 KB y
tiene unas cuarenta páginas; entra en el repositorio como binario y cambia con
cada regeneración. La fecha de la portada es la del día en que se genera.
