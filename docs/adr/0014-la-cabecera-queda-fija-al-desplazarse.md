# 14. La cabecera queda fija al desplazarse

Fecha: 2026-09-24 · Estado: aceptado

## Contexto

Los capítulos y la página de instrucciones son largos: el capítulo 2 ocupa unas
seis pantallas en escritorio y trece en el móvil. Al bajar desaparecían el menú,
el botón de tema y el de imprimir. La cabecera mide 84 px en escritorio (un 10 %
de una pantalla de 800 px), 78 px en tableta y 139 px en el móvil (un 16 %),
porque ahí ocupa tres filas.

## Decisión

La cabecera queda fija arriba al desplazarse (`position: sticky`). En pantallas
de hasta 40rem se oculta al bajar y reaparece en cuanto se sube, o cuando el
foco llega a uno de sus controles con el teclado; no se oculta con el menú de
imprimir abierto. `guia.js` guarda su altura en `--alto-cabecera`, y todos los
elementos con `id` dejan ese margen al llegar desde un enlace interno, para que
el destino no quede debajo. En papel y en el PDF la cabecera no es fija.

## Alternativas descartadas

- **Dejarla como estaba**: obliga a volver arriba para cambiar de sección en las
  páginas largas.
- **Fija también en el móvil**: ocupa una sexta parte de la pantalla todo el
  tiempo.
- **Una cabecera reducida al bajar**: supone rehacer su maquetación para un
  segundo estado, cuando ocultarla y mostrarla es el patrón que ya se conoce en
  el móvil.

## Consecuencias

El menú está siempre a mano. Sin JavaScript la cabecera es fija también en el
móvil y los enlaces internos reservan un margen fijo de 6rem.
