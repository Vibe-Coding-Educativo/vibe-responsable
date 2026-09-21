# 8. La infografía es un SVG generado con un script, con iconos de Lucide

Fecha: 2026-09-21 · Estado: aceptado

## Contexto

El autor pidió una sola infografía que permitiera ver de una vez las diez
recomendaciones. Para decidir con los resultados delante, encargó dos versiones:
una hecha por el agente, con iconos, y otra ilustrada, generada con Codex. Vistas
las dos, eligió la primera. La guía se traducirá a otros cuatro idiomas, y los
títulos de las recomendaciones han cambiado varias veces durante la redacción.

## Decisión

La infografía la genera `infografia/generar.py`, que escribe un SVG de
1080 × 1850 píxeles con los títulos de las diez recomendaciones, cada uno con un
icono de Lucide guardado en `infografia/iconos/`. Usa la paleta y la tipografía
de la web. Los textos están en un diccionario por idioma dentro del script, de
modo que una traducción o un cambio de título se resuelve regenerando la imagen.
Las diez recomendaciones van en una sola serie, sin separar unas pocas como
esenciales.

El SVG es el original editable y se conserva en el repositorio. Para la web se
exporta a PNG y se reduce su paleta, con lo que pesa unos 90 KB.

## Alternativas descartadas

- **La versión ilustrada generada por IA**: más vistosa, pero es una imagen
  cerrada. Cada cambio de título o cada idioma obligaría a generarla de nuevo,
  con un resultado distinto cada vez, y su texto no se puede corregir.
- **Diez ilustraciones, una por recomendación**: fue una mala lectura del
  encargo; el autor quería una sola imagen.
- **Tres recomendaciones destacadas como «lo esencial»**: el autor pidió
  quitar la división, porque las diez tienen el mismo rango.

## Consecuencias

Los títulos de la infografía están escritos en el script, aparte de
`01-guia.md`: al cambiar un título de la guía hay que cambiarlo también ahí y
regenerar la imagen. Regenerarla necesita `rsvg-convert` y Pillow. Los iconos
de Lucide obligan a acreditar su licencia ISC, lo que se hace en la página de
créditos.
