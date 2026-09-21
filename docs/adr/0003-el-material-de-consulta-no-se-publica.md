# 3. El material de consulta se descarga entero y se queda fuera del repositorio

Fecha: 2026-09-21 · Estado: aceptado · Sustituye al [ADR 2](0002-lo-normativo-se-consulta-no-se-copia.md)

## Contexto

El [ADR 2](0002-lo-normativo-se-consulta-no-se-copia.md) resolvía el problema de
la licencia dejando fuera del repositorio los documentos que no permiten
redistribuirse y copiando solo los abiertos. Al trabajar así aparecen dos
inconvenientes: cada consulta a un documento depende de una sesión autenticada
de Gemini Notebook, y el criterio de qué se copia y qué no obliga a comprobar la
licencia de cada fuente antes de poder leerla con comodidad.

La distinción que importa no es entre documentos abiertos y cerrados, sino entre
el material con el que se trabaja y el material que se publica. Ninguno de estos
documentos forma parte de la guía: se leen para redactarla y se citan por su
enlace oficial.

## Decisión

Todo el material de consulta se descarga a `fuentes/consulta/`, con una cabecera
que recoge título, autoría, licencia y procedencia. Esa carpeta está en
`.gitignore`: no se versiona, no se publica y no se redistribuye. En la guía,
cada documento se cita por su enlace oficial, y por artículo cuando es una
norma.

En el repositorio siguen los documentos que sostienen directamente la guía y
permiten redistribuirse, según el [ADR 1](0001-las-fuentes-se-guardan-en-el-repositorio.md):
los artículos y ponencias del CEDEC y de seLIA, la guía del INTEF y los
artículos propios del blog. El índice `fuentes/README.md` sigue listando el
material de consulta con su enlace oficial, aunque los archivos no estén.

## Alternativas descartadas

- **Copiar al repositorio solo los abiertos** (lo que decía el ADR 2): deja la
  lectura de lo demás atada a la sesión del cuaderno y mezcla en la misma
  carpeta material con dos regímenes distintos.
- **Subirlo todo al repositorio**: publicaría material con licencia no comercial
  o sin permiso de reutilización, y añadiría varios megas de textos legales que
  además cambian.
- **No descargar nada y consultar siempre el cuaderno**: cada consulta necesita
  conexión y sesión autenticada, y no permite buscar sobre el texto con las
  herramientas del propio repositorio.

## Cómo se consulta cada cosa

El material de consulta son veintitrés documentos: los quince del cuaderno de
Gemini Notebook y otros ocho de alcance mundial, añadidos después tras una
búsqueda en internet, que están solo en la copia local. Los del cuaderno suman
cerca de medio millón de palabras: no caben en la ventana de contexto de un
agente, y leerlos enteros no es una opción. El reparto
es este:

- **Pregunta que cruza varias fuentes** («¿qué base legitima este tratamiento y
  qué obligaciones tiene el centro?»): se pregunta al cuaderno, que responde con
  las citas de los documentos que la sostienen. Solo alcanza a sus quince
  documentos, no a los ocho añadidos después.
- **Pasaje concreto ya localizado**: se busca en la copia de `fuentes/consulta/`
  con las herramientas del repositorio y se lee solo ese fragmento.
- **Cita que va a la guía**: se comprueba contra la versión oficial en línea,
  porque los textos consolidados cambian.

## Consecuencias

El material de consulta no viaja con el repositorio: quien lo clone no lo tiene
y ha de descargarlo de nuevo desde los enlaces oficiales del índice o desde el
cuaderno. A cambio, se trabaja sobre el texto completo de todos los documentos sin
publicar nada que no deba publicarse. Como los textos legales consolidados
cambian, la copia local sirve para leer y localizar, pero la cita se comprueba
siempre contra la versión oficial en línea.
