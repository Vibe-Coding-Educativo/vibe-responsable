# 17. La portada abre en vídeo una segunda animación, un zoom infinito

Fecha: 2026-09-27 · Estado: propuesto

## Contexto

Tras la primera animación (ADR 16), el autor pidió otra con un estilo que
impresionara a quien la viera, que siguiera siendo rigurosa, que tuviera chispa y
que no pareciera una presentación, y dejó el estilo en manos del agente. Después
pidió que la portada la mostrara como vídeo en lugar de la primera, sin el
enlace al texto de la animación.

## Decisión

- **Estilo: un zoom infinito con tipografía cinética**, en un solo plano sin
  cortes (`animacion/zoom.es.html`). Hay cinco niveles, cada uno dentro de un
  objeto del anterior: la conversación con la IA, y dentro de su cursor la
  fase 1; dentro de la pantalla de una tableta, la fase 2; dentro de una tecla,
  la fase 3; dentro del símbolo de Creative Commons, la fase 4. Al final una
  copia del material se divide en 2, 4, 8… hasta 256, y la cámara sale de vuelta
  por todos los niveles hasta la conversación, donde aparece el cierre. Cada
  nivel tiene un color de la paleta de la guía; los números de las
  recomendaciones son grandes y huecos; las palabras entran al ritmo de la
  música; hay un temblor de cámara en cada golpe, grano de película y viñeta.
  La chispa está en los gestos visuales (el sello «Verdadero» tapado por
  «Error», los datos que rebotan en el escudo, la plataforma que revienta), no
  en el texto, que sigue siendo impersonal.
- **Los textos salen de la guía**, como en la primera animación; los ejemplos
  (la pregunta del cuestionario, las decisiones del registro, el código) son
  ilustrativos.
- **Mecánica**: la cámara es un número z (parte entera, nivel; decimal, avance
  hacia el siguiente). Cada nivel se escala alrededor del punto fijo de su
  portal, cuyo lugar y tamaño se miden en el propio documento, de modo que la
  inmersión es continua. Los elementos se animan con fotogramas clave en
  `data-k`. Todo sale del tiempo, igual que en la primera (ADR 16).
- **Música**: electrónica a 120 pulsaciones en la menor, sintetizada, con un
  crescendo antes de cada inmersión, un impacto al llegar, un «rebobinado» en
  la vuelta atrás y un limitador final.
- **La portada la muestra como vídeo**: el botón «Ver la animación» abre una
  ventana con `animacion/vibe-responsable-zoom.es.mp4` (122 s, 1080 × 1080,
  6,6 MB) y su cartel. El vídeo se descarga solo al abrir la ventana, arranca
  con la misma pulsación y se detiene al cerrarla. Sin JavaScript, el botón
  abre el vídeo. Sustituye a la primera animación incrustada (ADR 16), cuya
  página sigue disponible pero ya no se enlaza, y desaparece el enlace al texto
  de la animación. Este vídeo sí se guarda en el repositorio, porque la web lo
  sirve; los demás siguen fuera (`.gitignore`).

## Alternativas descartadas

- **Incrustar la página del zoom, como la primera**: pinta en directo cientos
  de elementos escalados y, en equipos modestos, podría ir a saltos; el vídeo
  se reproduce igual en todas partes.
- **Guardar el vídeo en una publicación de GitHub en lugar del repositorio**:
  se serviría desde otro dominio y como descarga; no se ha comprobado si se
  reproduce bien dentro de la página (hipótesis sin validar), y servirlo con la
  propia web es lo más sencillo.
- **Menos compresión** (14 MB): el grano cambia en cada fotograma y dispara el
  peso; con más compresión el texto sigue nítido y el grano se suaviza.

## Consecuencias

La portada pesa lo mismo al entrar: el vídeo solo se descarga al pedirlo. Cada
cambio en la animación exige volver a grabarla (unos 30 minutos) y recomprimir
el vídeo, y cada versión añade unos 6,6 MB al historial del repositorio. Sin
voz, el vídeo no necesita subtítulos; su texto está en la página de la
animación, que ya no se enlaza desde la portada.

## Evidencia

- Recompresión: `ffmpeg -i <grabación> -i <sonido.wav> -c:v libx264 -preset
  slow -crf 31 -af alimiter=limit=0.79 -c:a aac -b:a 128k -movflags +faststart`.
  Con CRF 28 pesaba 8,2 MB; con CRF 22, 14 MB.

## Riesgos y limitaciones

- Los navegadores de Playwright para Firefox y WebKit en Linux no traen H.264,
  así que la reproducción del vídeo solo se ha probado en Chromium; Firefox y
  Safari de escritorio y móvil sí lo reproducen con los códecs del sistema
  (hipótesis pendiente de validar en los equipos del autor).
- La grabación tarda unos 30 minutos por la cantidad de elementos de cada
  fotograma.

## Validación

- Capturas de cada parte revisadas: sin solapes entre recomendaciones, las
  cuatro inmersiones continuas y la vuelta atrás por todos los niveles.
- Sonido: −15,8 LUFS integrados y pico por debajo de 0 dB en la página; en el
  vídeo, limitado a −2 dB.
