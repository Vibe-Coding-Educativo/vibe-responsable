# Decisiones de arquitectura (ADR)

Cada archivo recoge una decisión que condiciona el trabajo futuro: por qué se
tomó, qué se descartó y qué consecuencias tiene. Sirven para que nadie las
deshaga después de buena fe, ni siquiera nosotros dentro de un año.

| Nº | Decisión | Estado |
|---|---|---|
| [1](0001-las-fuentes-se-guardan-en-el-repositorio.md) | Las fuentes consultadas se guardan en el repositorio | aceptado |
| [2](0002-lo-normativo-se-consulta-no-se-copia.md) | El material normativo se consulta en el cuaderno, no se copia | sustituido por el 3 |
| [3](0003-el-material-de-consulta-no-se-publica.md) | El material de consulta se descarga entero y se queda fuera del repositorio | aceptado |
| [4](0004-web-estatica-generada-desde-markdown.md) | La web se publica como HTML estático, generado a partir de textos escritos en Markdown, sin dependencias en el navegador | aceptado |
| [5](0005-portada-en-una-pantalla-y-varias-paginas.md) | La presentación y la guía caben en una pantalla, y el contenido se reparte en varias páginas | aceptado |
| [6](0006-los-ejemplos-salen-del-catalogo-de-la-comunidad.md) | Los ejemplos de los capítulos salen del catálogo de la comunidad | aceptado |
| [7](0007-capitulos-en-paginas-propias-con-una-sola-fuente.md) | Cada capítulo tiene su página, y lo que hay que hacer sale de una sola fuente | aceptado |
| [8](0008-infografia-generada-con-un-script.md) | La infografía es un SVG generado con un script, con iconos de Lucide | aceptado |
| [9](0009-la-guia-completa-se-publica-en-pdf-generado-desde-la-propia-web.md) | La guía completa se publica en PDF, generado desde la propia web | aceptado |

Para añadir una, se copia [la plantilla](0000-plantilla.md) con el número
siguiente y se anota aquí. Una decisión que deje de valer no se borra: se marca
como «sustituida por» la nueva, para que quede el rastro.
