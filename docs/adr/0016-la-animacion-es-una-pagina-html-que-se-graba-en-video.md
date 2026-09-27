# 16. La animación es una página HTML con sonido sintetizado, que se graba en vídeo

Fecha: 2026-09-27 · Estado: propuesto

## Contexto

El autor pidió una animación rigurosa sobre el contenido de la guía y, mientras
se hacía, que llevara música y sonido. Tiene que servir para la web y para
difundirse en redes, donde circula como vídeo y se ve sobre todo en el móvil.
Los títulos y los mínimos de las recomendaciones han cambiado varias veces, y
la guía se traducirá a otros idiomas.

## Decisión

La animación es una página HTML, `animacion/animacion.es.html`, sin bibliotecas,
con la paleta, la tipografía y los iconos de Lucide de la web y la infografía.
Es cuadrada (1080 × 1080), para que se lea en el móvil y encaje en las redes, y
dura 2 min 15 s en diez escenas: portada, qué es el vibe coding educativo, por
qué esta guía, la definición de VCER, una escena por fase con sus
recomendaciones y «Lo mínimo» de cada una, cómo empezar y cierre.

- **Los textos salen de `contenido/es`**: las definiciones y la motivación,
  literales de la presentación; los títulos, de la lista; los mínimos,
  condensados de la lista sin añadir nada que no diga.
- **Todo se calcula a partir del tiempo**: `render(t)` coloca cada escena y
  cada elemento según el segundo `t`. La reproducción en el navegador y el
  vídeo son el mismo cálculo.
- **La música y los efectos se sintetizan con Web Audio** en la propia página:
  acordes I–vi–IV–V en do mayor a 96 pulsaciones, con un sonido para cada
  aparición marcada con `data-son`. No hay archivos de sonido ajenos que
  acreditar ni licencias que comprobar. Las escenas duran múltiplos de medio
  compás para que los cambios caigan a tiempo.
- **El sonido solo empieza al pulsar «Reproducir con sonido»** y tiene botón
  para silenciarlo. La página ofrece además el texto completo de la animación,
  plegado, para quien no pueda o no quiera verla.
- **La portada la ofrece en una ventana**: bajo la infografía, un botón «Ver
  la animación» abre una ventana del mayor tamaño que cabe con la página en
  modo incrustado (`?incrustar`), que muestra solo el escenario y sus
  controles, con el tema claro u oscuro de la web (`&tema=`), en un tamaño que
  deja margen alrededor (como mucho 40 rem de lado). Arranca sola (`&auto`),
  sin una segunda pulsación: los navegadores solo dejan sonar tras una acción
  de la persona, así que la portada crea el contexto de sonido al pulsar el
  botón y la animación lo toma prestado; si aun así no puede sonar, avanza en
  silencio con el reloj del sistema. El marco se carga al abrir la ventana y se
  vacía al cerrarla, y el contexto de sonido se cierra, para que no siga
  sonando; Escape la cierra también con el foco dentro. En su página propia, la
  animación espera parada mostrando la portada ya compuesta, con el botón
  «Reproducir con sonido». Debajo, un enlace lleva al texto de la
  animación en su página. Sin JavaScript, el botón lleva a esa página. Así la
  portada sigue cabiendo en una pantalla con la infografía a la vista (ADR 5).
- **El vídeo se genera con `node animacion/grabar.js`**: pinta cada fotograma
  con Playwright, obtiene la banda sonora con `OfflineAudioContext` y los une
  con ffmpeg en `animacion/vibe-responsable.es.mp4` (H.264 y AAC, 30 fps,
  unos 6,6 MB, sonoridad de −16 LUFS).
- **El MP4 no se guarda en el repositorio**: se regenera cuando cambia la
  página y se publica aparte (como archivo de una versión publicada o en las
  redes), para que cada cambio no añada varios megas al historial.

## Alternativas descartadas

- **Un vídeo hecho con un editor o generado por IA**: sería una pieza cerrada;
  cada cambio de texto o de idioma obligaría a rehacerlo, y el texto no se
  podría corregir ni leer con un lector de pantalla.
- **Formato 16:9**: en un móvil vertical el texto quedaría ilegible.
- **La animación en la portada, en lugar de la infografía o debajo de todo**:
  en la columna de la infografía queda pequeña y la deja fuera de la vista;
  debajo, la portada deja de caber en una pantalla. El autor propuso abrirla
  con un botón en una ventana, como los archivos para la IA.
- **Música de un banco con licencia libre**: obliga a acreditarla y a
  comprobar su licencia, y no se sincroniza con las apariciones. La sintetizada
  pesa unas líneas de código.
- **Animaciones CSS con transiciones**: no permiten pintar un instante exacto,
  de modo que el vídeo no coincidiría con lo que se ve en la web.

## Consecuencias

Cambiar un texto es editar la página y volver a ejecutar `grabar.js` (unos
cinco minutos). Si cambian los títulos o los mínimos de la guía, hay que
trasladarlos a mano a la animación, igual que a la infografía. En un móvil el
texto del escenario queda pequeño (el escenario se reduce a la anchura de la
pantalla); el vídeo a pantalla completa o el texto plegado lo resuelven. El
comprobador de enlaces internos de `construir.py` lee ahora las anclas de la
página de destino aunque esté fuera de la carpeta del idioma.

## Evidencia

- Web Audio y `OfflineAudioContext`: especificación del W3C, «Web Audio API»
  (https://www.w3.org/TR/webaudio/).
- Iconos: Lucide, `lucide-static` 1.48.0 (licencia ISC; los derivados de
  Feather, MIT), los mismos de `infografia/iconos/` más `user`, `file-text`,
  `scan-eye`, `x`, `check` y los de los controles.

## Riesgos y limitaciones

- Los navegadores sintetizan el sonido en tiempo real: en un equipo muy lento
  podría entrecortarse. El vídeo no tiene este problema.
- La música es sencilla y se repite cada cuatro compases.
- Los mínimos condensados pueden perder matices respecto a la lista; la
  revisión del autor es la que los da por buenos.

## Validación

- Capturas de cada escena revisadas una a una; sin solapamientos entre las
  tarjetas y la tira de las diez recomendaciones.
- `probar-web` en Chromium, Firefox y WebKit, en escritorio, tableta y móvil,
  con tema claro y oscuro: 18 combinaciones sin errores de JavaScript, sin
  recursos que fallen y sin desbordamiento.
- Ventana de la portada en Chromium y Firefox, a 1366 × 768, 1920 × 1080 (tema
  oscuro) y 390 × 844: cabe sin barras de desplazamiento y el marco se vacía
  al cerrar. En Chromium, Firefox y WebKit la animación arranca sola al abrir
  la ventana, con el contexto de sonido en marcha, y al cerrarla el contexto
  queda cerrado.
- axe-core en Chromium y Firefox, con la animación parada, en marcha y con el
  texto desplegado: ninguna infracción. Recorrido con el tabulador en orden
  lógico por todos los controles.
- Vídeo comprobado con ffprobe (1080 × 1080, 30 fps, 135 s, audio AAC) y con el
  filtro `ebur128` de ffmpeg: −16,3 LUFS integrados y pico verdadero de
  −3,3 dBFS. Espectrograma revisado: soplos en los cambios de escena,
  percusión suave en las fases y acorde final.
