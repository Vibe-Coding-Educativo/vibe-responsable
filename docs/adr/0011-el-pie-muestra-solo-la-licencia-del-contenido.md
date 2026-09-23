# 11. El pie muestra solo la licencia del contenido

Fecha: 2026-09-23 · Estado: aceptado

## Contexto

El pie de todas las páginas, y la página de licencia del PDF, indicaban dos
licencias: AGPL v3 para el código y CC BY-SA 4.0 para los contenidos. Pero esta
web no es un programa. Es la presentación de un texto, y su código
(`construir.py`, `recursos/`, `infografia/generar.py`) solo sirve para mostrarlo.
Quien lee la guía necesita saber cómo puede reutilizar el texto y la infografía.
La licencia del código solo le importa a quien vaya al repositorio.

## Decisión

El pie y el PDF indican solo la licencia del contenido, CC BY-SA 4.0. La AGPL v3
del código se indica en el archivo `LICENSE`, en el apartado «Licencias» del
`README.md` y en la página «Créditos y licencias», a la que el pie enlaza.

Esto se refiere a la licencia de esta web. Las instrucciones para la IA siguen
recomendando la AGPL v3 para el código de los materiales que otras personas
creen, porque esos materiales sí son programas.

## Alternativas descartadas

- **Mantener las dos licencias en el pie.** Da a una pieza secundaria el mismo
  peso que al contenido, que es lo que importa al lector.
- **Quitar la AGPL también de los créditos.** Ahí se explica cómo reutilizar
  todo lo que forma la web, y el código también forma parte.

## Consecuencias

El pie es más corto y se centra en lo que importa al lector. Quien quiera
reutilizar el código encuentra su licencia en los créditos y en el repositorio.
