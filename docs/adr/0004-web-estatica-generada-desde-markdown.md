# 4. La web se publica como HTML estático, generado a partir de textos escritos en Markdown, sin dependencias en el navegador

Fecha: 2026-09-21 · Estado: aceptado

## Contexto

La guía se publica como web, porque se lee mejor que un documento y permite
enlazar cada recomendación. Pide a quien publica materiales que no dependan de
servicios que pueden desaparecer, que no recojan datos, que sean accesibles y
que su código pueda entenderse. La web de la guía tiene que cumplir lo mismo,
o perdería su argumento. El texto lo edita también el autor directamente, así
que debe estar en un formato que se pueda retocar sin tocar HTML. Y la guía se
traducirá al inglés, al catalán, al gallego y al euskera.

## Decisión

La web que se publica y que recibe el navegador es HTML. El Markdown es solo
el formato en que se escriben los textos, en `contenido/<idioma>/`, y no llega
a quien lee la guía. El script `construir.py` convierte esos textos en HTML con
pandoc y los monta en una plantilla: las páginas de cada idioma en `/<idioma>/`
y una portada en la raíz que envía al idioma del navegador si existe. El HTML
generado se guarda en el repositorio y lo sirve GitHub Pages tal cual
(`.nojekyll`).

En el navegador solo hay HTML, una hoja de estilos, un script de unas ciento
cincuenta líneas y la tipografía, todo servido desde el propio repositorio: sin
bibliotecas, sin recursos cargados de otros servidores, sin analítica. El aspecto claro u oscuro sigue la preferencia del dispositivo. Sin
JavaScript la página se lee entera; la infografía se abre como enlace en lugar de
ampliarse. Los enlaces a otras
webs se abren en una pestaña nueva, para no sacar al lector de la guía.

La forma de evitar el desplazamiento largo que se describía aquí (dos columnas y
acordeones en una sola página) quedó sustituida por el [ADR 5](0005-portada-en-una-pantalla-y-varias-paginas.md).

Los textos de la interfaz están en un diccionario por idioma dentro de
`construir.py`, y los de la infografía en otro dentro de
`infografia/generar.py`, de modo que añadir un idioma es añadir su bloque y su
carpeta de contenido.

## Alternativas descartadas

- **eXeLearning**: es la herramienta habitual del autor, pero la guía se quiere
  como web ligera enlazable punto a punto, y el Markdown permite que autor y
  agente editen el mismo archivo sin conflictos.
- **Un generador de sitios (Jekyll, Hugo, MkDocs)**: añade una dependencia y un
  tema ajeno para una web de pocas páginas; el script propio cabe en un archivo
  y cualquiera puede leerlo.
- **Convertir el Markdown en el navegador con una biblioteca**: haría depender
  la lectura de JavaScript y de código de terceros, contra lo que la guía
  recomienda.
- **Escribir el HTML a mano**: obligaría al autor a editar HTML y duplicaría el
  texto entre idiomas y formatos.

## Consecuencias

Después de cambiar el contenido hay que ejecutar `python3 construir.py` y
subir también el HTML generado; si se olvida, la web queda desfasada respecto
al Markdown. Quien quiera regenerarla necesita pandoc. A cambio, la web es
ligera (el 21-09-2026, las quince páginas de un idioma con los estilos y el
script sumaban 189 KB, más 53 KB de tipografía), no depende de nadie y cumple las
recomendaciones que ella misma da.
