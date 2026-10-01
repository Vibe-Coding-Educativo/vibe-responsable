# 20. La guía se publica en cinco idiomas

Fecha: 2026-10-01 · Estado: aceptado

## Contexto

La guía se escribió en castellano, para docentes de cualquier país. Antes de
depositar la versión 1.0 en Zenodo, Juanjo pidió traducirla a los idiomas
habituales de sus trabajos: «antes lo teníamos que haber traducido»; y después,
«sí, los cinco idiomas y el vídeo en castellano». Ese mismo día, ya publicada la 1.0, pidió también el vídeo: «haz la animación en todos los idiomas»; y, sobre las traducciones, que «en algún lado hay que decir que las traducciones son automáticas y no han sido revisadas por un revisor profesional». El generador ya estaba
preparado para varios idiomas (`IDIOMAS`, una carpeta por idioma en
`contenido/` y un bloque por idioma en `UI`), pero algunas piezas tenían el
castellano escrito en el código.

## Decisión

- La guía se publica en castellano (original e idioma por omisión), catalán,
  gallego, euskera e inglés, cada uno en su carpeta (`es/`, `ca/`, `gl/`, `eu/`,
  `en/`) con su PDF. La raíz envía al idioma del navegador si está entre ellos.
- La cabecera lleva un botón de idioma (icono `languages` de Lucide), delante
  del de tema porque condiciona todo lo demás. Abre un menú con los cinco
  idiomas, cada uno con su nombre en su propia lengua, que lleva a la misma
  página en el otro idioma. Cada página declara sus equivalentes con
  `hreflang`.
- Las traducciones las hace la IA a partir del original en castellano, de forma
  automática y sin revisión de un traductor profesional; los créditos de cada
  idioma y la descripción del depósito de Zenodo lo dicen.
- Los títulos de las obras citadas se mantienen en su idioma original. Los
  enlaces apuntan a la versión en el idioma de la página cuando la fuente la
  tiene: las licencias Creative Commons en los cinco; la definición de obras
  culturales libres y Wikimedia Commons en catalán, gallego e inglés (Wikimedia
  también en euskera); la página de la FSF en catalán e inglés; la UNESCO, el
  W3C y la normativa europea en inglés. Si no hay versión, se mantiene la
  castellana.
- En inglés y en euskera se traduce también el nombre de la guía
  («Responsible vibe coding», «Vibe coding arduratsua»), y la cita usa el
  título traducido. En catalán y gallego el nombre coincide con el castellano.
- La sigla VCER se mantiene en todos los idiomas; en inglés y euskera se aclara
  que procede del castellano.
- El vídeo de la portada se graba en cada idioma. `animacion/traducir.py`
  genera `zoom.<idioma>.html` a partir de `zoom.es.html`, el único que se edita,
  con una tabla de sustituciones que avisa si un texto ya no está en el
  original; luego `grabar.js` graba cada página. Si falta el vídeo de un idioma,
  `video()` usa el castellano. Los cuatro vídeos traducidos se grabaron el 01-10-2026 y se comprimieron como el castellano (ADR 17): entre 6,4 y 6,5 MB, −16,1 LUFS y picos de −1,7 a −1,8 dBFS; el cartel de cada uno es su último fotograma.
- La infografía se genera en cada idioma con `infografia/generar.py`, y se
  convierte a PNG con `rsvg-convert` y la misma paleta reducida (64 colores).

Lo que estaba en castellano dentro del código pasa a salir del propio texto o
del bloque de cada idioma: las anclas de los apartados que se enlazan desde la
plantilla (`anclas_de`), el formato de las fechas (`fecha`), las siglas que la
rúbrica devuelve a mayúsculas (`siglas`) y las palabras átonas que la
infografía no deja a final de línea.

## Alternativas descartadas

- **Traducir solo al inglés.** Deja fuera a buena parte del profesorado de su
  comunidad, que trabaja en catalán, gallego o euskera.
- **Traducir con un servicio de traducción automática en la propia web.**
  Envía el texto a un tercero, no se puede revisar y no produce PDF ni archivos
  para la IA en cada idioma.
- **Una copia de la animación por idioma, editada a mano.** Cinco archivos de
  800 líneas que se separarían con el primer cambio; la tabla de traducciones
  obliga a cambiar el original y deja ver qué falta traducir.
- **Enlazar siempre las fuentes en castellano.** Contradice el criterio de
  enlazar en el idioma del texto cuando existe la versión.

## Consecuencias

Cada cambio de contenido debe hacerse en los cinco idiomas; `construir.py`
comprueba en todos los enlaces internos y que cada enlace del texto tenga su
referencia. Las traducciones no han tenido revisión humana completa: conviene
que hablantes de cada lengua las revisen, sobre todo la vasca. Las sugerencias
de cualquier idioma llegan por el mismo sitio (ADR 13).

## Evidencia

Comprobado el 01-10-2026 con el servidor local: las portadas de los cinco
idiomas en Chromium, Firefox y WebKit, en escritorio y móvil, sin errores ni
desbordamiento; el menú de idiomas en Chromium y Firefox; axe-core sin
infracciones en la portada, las instrucciones para la IA y el capítulo 2 de
cada idioma. Las versiones traducidas de las fuentes se comprobaron una a una
con peticiones HTTP; el W3C no tiene traducción al catalán, gallego ni euskera
de las páginas citadas.
