# 1. Las fuentes consultadas se guardan en el repositorio

Fecha: 2026-09-21 · Estado: aceptado

## Contexto

La guía se apoya en artículos y ponencias publicados en la web, propios y
ajenos. Las páginas cambian, se reorganizan o desaparecen, y la guía se
consultará durante años: una cita que remita solo a una URL puede quedarse sin
respaldo. Además, al redactar hace falta releer el material entero, no un
resumen hecho de memoria.

## Decisión

Cada documento que sostiene directamente la guía se guarda en `fuentes/`,
transcrito a Markdown, con una cabecera que recoge título, autoría, fecha de
publicación, URL, fecha de descarga y licencia. La guía del INTEF es la
excepción: se guarda el PDF original, con su texto extraído al lado para poder
buscar en él. Los artículos propios del blog van en `fuentes/blog/`. Las
imágenes que aportan información, en `fuentes/imagenes/`. El índice
`fuentes/README.md` lista todo con su autoría y su licencia.

El material que solo se consulta para trabajar (normas, guías de organismos,
artículos de contexto) no se guarda aquí: lo regula el
[ADR 3](0003-el-material-de-consulta-no-se-publica.md).

Solo se guarda material con licencia que permita la copia y la redistribución
(CC BY, CC BY-SA o equivalente). Si una fuente necesaria no la tuviera, se
anotaría en el índice con su URL, sin copiarla.

## Alternativas descartadas

- **Dejar las fuentes fuera del repositorio, en local o con `.gitignore`**: el
  material desaparecería al cambiar de equipo y nadie podría comprobar de dónde
  sale cada afirmación de la guía.
- **Guardar solo los enlaces**: no protege contra el enlace roto ni contra el
  cambio silencioso del contenido citado.
- **Guardar el HTML original completo**: pesa mucho, arrastra código y hojas de
  estilo ajenas, y dificulta leer y citar el texto.

## Consecuencias

El repositorio crece con material de terceros, que queda publicado en un
repositorio público: por eso cada archivo lleva su autoría y su licencia dentro,
y el índice las repite. Obliga a comprobar la licencia antes de descargar nada.
A cambio, la guía puede citar con exactitud y cualquiera puede verificar las
fuentes aunque las páginas originales cambien.
