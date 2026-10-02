# 19. Cada versión publicada lleva número, etiqueta y DOI

Fecha: 2026-10-01 · Estado: aceptado

## Contexto

La recomendación 10 de la guía pide marcar cada versión publicada con una
etiqueta, y Juanjo quiere ver la versión de sus programas en el pie y en los
créditos. Hasta el 01-10-2026 la guía era un borrador sin número: el
repositorio no tenía etiquetas y la web no decía qué versión se estaba leyendo.
Al cerrar el borrador (ADR 13) se decidió publicar la 1.0 y depositarla en
Zenodo para tener un DOI, como el MIAE.

## Decisión

- La versión se define en un solo sitio, `construir.py` (`VERSION`,
  `FECHA_VERSION`, `DOI`, `DOI_CONCEPTO`), y de ahí sale a todas las páginas y a
  los PDF.
- El pie de todas las páginas dice «Versión 1.0». Hasta la 2.0 enlazaba a las
  notas de esa versión en GitHub (`releases/tag/v1.0`); desde el 02-10-2026
  enlaza al apartado «Versiones» de los créditos, que explica el criterio de
  numeración y lo que cambia en cada versión, con su DOI. Juanjo lo pidió al
  pasar de la 1.1 a la 2.0 en el mismo día: «es posible que alguno se pregunte
  qué ha pasado». Es información para el visitante, no contenido de la guía, así
  que añadirla no cambia la versión ni los PDF depositados; cada versión nueva
  añade su entrada, con los cambios en viñetas, en los cinco idiomas.
- La portada del PDF y su pie llevan la versión y su fecha, no la fecha en que
  se generó el archivo.
- La cita lleva el número de versión y el DOI de esa versión; debajo, el DOI de
  concepto, que lleva siempre a la última.
- Cada versión tiene su etiqueta en el repositorio (`v1.0`), su versión
  publicada en GitHub con unas notas breves y su depósito en Zenodo con los PDF
  de todos los idiomas y los archivos para la IA.
- La versión cambia cuando cambia el texto de la guía, no con los ajustes de
  la web. Las correcciones de traducción, ortografía o expresión, que no
  cambian lo que dice la guía, suben el segundo número (1.1); un cambio de
  contenido, el primero (2.0). Juanjo fijó este criterio el 02-10-2026, al
  preparar la 1.1, frente a un esquema de tres números (1.0.1) que se le
  propuso: «me parece más claro».

El DOI de la 1.0 se reservó en Zenodo antes de generar los PDF, para que la
cita impresa ya lo lleve: versión `10.5281/zenodo.23081518`, concepto
`10.5281/zenodo.23081517`. La 1.1 (02-10-2026), que corrige las traducciones y la redacción, se
preparó igual: versión `10.5281/zenodo.23097280`, etiqueta `v1.1`. La 2.0 (02-10-2026), que añade la página de la
evaluación VCER y la mención del resultado en el recurso evaluado (ADR 21), es
un cambio de contenido: versión `10.5281/zenodo.23105801`, etiqueta `v2.0`.

## Alternativas descartadas

- **La fecha como versión.** Es lo que había; no sirve para citar ni para saber
  si dos copias son la misma.
- **Numerar también los ajustes de la web.** Multiplicaría los depósitos en
  Zenodo sin que cambie lo que se cita.
- **Pedir el DOI después de publicar la web.** Obligaría a regenerar los PDF y
  a subir otra versión a Zenodo solo para añadir el DOI.

## Consecuencias

Publicar una versión nueva exige cambiar `VERSION`, `FECHA_VERSION` y los DOI
en `construir.py` (pidiendo antes una versión nueva en Zenodo y reservando su
DOI), regenerar la web y los PDF, etiquetar el commit y depositar los archivos.
Una etiqueta publicada no se mueve ni se reutiliza.

## Evidencia

El borrador de Zenodo 23081518 se creó el 01-10-2026 con la skill
`deposito-zenodo`; su DOI se reservó con la API de InvenioRDM
(`POST /api/records/{id}/draft/pids/doi`). El DOI de concepto sigue la pauta
comprobada en el MIAE: el número del registro padre (22647407 frente a
22647408). Hasta que se publique el depósito, ninguno de los dos DOI resuelve.
