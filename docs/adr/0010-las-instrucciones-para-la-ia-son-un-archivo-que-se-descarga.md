# 10. Las instrucciones para la IA son archivos que se descargan, uno para crear y otro para evaluar

Fecha: 2026-09-23 · Estado: aceptado

## Contexto

La página «Instrucciones para la IA» ofrecía primero tres textos para copiar (al
empezar, al terminar y las condiciones para un repositorio) y después dos. El
texto de empezar mezclaba lo que pide la guía, que es igual en todos los
materiales, con la descripción del material concreto, que cambia cada vez. Había
que editar un bloque largo en cada uso, con el riesgo de borrar algo, y lo dicho
al empezar se diluye en las conversaciones largas o no llega a las sesiones
siguientes.

## Decisión

Lo que pide la guía está en un solo archivo, `contenido/<idioma>/instrucciones-ia.md`,
que `construir.py` publica como `instrucciones-vibe-responsable.md` y muestra
entero en `para-la-ia.html`, en el lugar de la marca `<!-- instrucciones -->`,
con dos botones: descargar y copiar. El archivo:

- contiene solo lo que pide la guía; el material se describe aparte;
- pide a la IA que pregunte la autoría y el lugar de publicación si no los
  conoce, de modo que se usa sin editarlo;
- lleva la licencia fija (CC BY-SA 4.0 y AGPL v3), salvo que se indiquen otras;
- incluye las condiciones para un repositorio o sitio propio, que la IA aplica
  según el lugar de publicación;
- permite cargar bibliotecas, tipografías y otros recursos externos cuando
  ahorran trabajo, porque rehacerlos desde cero o alojarlo todo en el material no
  es realista. La IA los anota en la nota de decisiones, que sirve a quien
  arregle o adapte el material más adelante, y al docente solo le dice, con
  palabras sencillas, qué dejaría de funcionar al abrirlo descargado sin
  internet. El capítulo 4 sigue el mismo criterio;
- no lleva lista de revisión: al terminar, el material se revisa con el
  archivo de evaluación, adjunto en la misma conversación, y después se pide
  corregirlo (24-09-2026). Antes llevaba su propia lista de diez puntos, que
  repetía la rúbrica con otras palabras y obligaba a llevar cada cambio a las
  dos;
- pide a la IA una lista de comprobaciones del propio material, con sus
  recorridos principales y sus casos extremos, para repetirla después de cada
  cambio, y que la convierta en pruebas automáticas si el proyecto lo permite
  (25-09-2026). La lista comprueba que el material sigue funcionando tras un
  cambio, así que no sustituye la evaluación con la rúbrica ni repite sus diez
  puntos;
- en un repositorio, pide marcar cada versión publicada con una etiqueta de
  versión, sin moverla ni reutilizarla, y anotar en el registro de decisiones
  la evidencia, los riesgos y la validación de las decisiones técnicas
  (25-09-2026).
Evaluar un recurso ya hecho tiene su propio archivo, `contenido/<idioma>/evaluacion-ia.md`,
publicado como `evaluacion-vibe-responsable.md` y mostrado en la misma página (marca
`<!-- evaluacion -->`). Sirve para recursos propios o ajenos, hechos o no con la
guía, y no corrige nada:

- una rúbrica de 2, 1 o 0 para cada uno de los diez puntos, con un nivel
  descrito para cada valor y una frase que justifique la nota; lo que no puede
  comprobarse queda sin puntuar;
- un porcentaje sobre los puntos puntuados, con «No recomendable» si el punto 1
  (contenido) o el 2 (datos personales) tienen 0, «Mejorable» por debajo del
  70 % y «Recomendable» desde el 70 %, solo si esos dos puntos se han podido
  puntuar (23-09-2026: un recurso con errores evidentes o sin comprobar la
  privacidad no puede recomendarse por buena que sea la media), y siempre que
  el punto 5 (accesibilidad) no tenga 0, porque un recurso que no puede usarse
  con el teclado sacaba un 90 % con el resto perfecto; con 0 en el 7 queda en
  «Mejorable», sin hacerlo eliminatorio, que dejaría como «No recomendable» un
  recurso usable con fallos de contraste, color y pantalla estrecha (23-09-2026);
  y las tres mejoras que más subirían la nota;
- el punto 1 se puntúa con los errores que la IA detecta por su cuenta, que
  bastan para ver un recurso sin revisar, aunque no certifican el contenido;
- el punto 5 se comprueba, si la IA puede ejecutar código, con una herramienta
  automática de accesibilidad en el navegador, también con contenido cargado,
  sin contar lo incrustado de otros sitios y recorriendo aparte el teclado; la
  IA dice qué ha probado y cómo. Está en el propio archivo porque quien evalúa
  solo lee ese archivo: al evaluar el Escritorio Digital (24-09-2026) la IA se
  limitó a leer el código y no vio el contraste de 1,96:1 de todas las
  ventanas ni los fallos que solo aparecían con datos cargados. No es requisito
  de la nota, que depende del material y no de la herramienta, para no
  castigar a quien evalúa desde un chat sin ejecutar código;
- antes de puntuar, la IA hace inventario completo en vez de mirar una
  muestra: funciones que piden o guardan datos de personas y cómo se exportan,
  archivos de imagen, sonido, vídeo, iconos y tipografías con su origen, y lo
  que se carga de fuera y cuándo. En la misma evaluación (24-09-2026) la IA
  había dado por bueno el punto 2 sin ver que Asistencia exportaba siempre con
  nombres, el 8 mirando solo los dos sonidos acreditados (faltaban 22 fondos,
  46 iconos y un logotipo redibujado) y el 6 describiendo como incrustadas
  apps que se abren en ventana nueva;
- si el recurso está publicado, se evalúa esa versión o se comprueba que
  coincide con el código: tras subir cambios al repositorio, la web siguió con
  la versión anterior hasta desplegarla;
- el informe indica, debajo del resultado, qué versión se ha evaluado: la
  etiqueta y el commit si el recurso está en un repositorio, o la dirección y
  la fecha si no lo está, para que la evaluación pueda comprobarse aunque el
  recurso cambie (25-09-2026);
- si después se pide corregir, la IA propone los cambios antes de hacerlos y,
  si no hay nota de decisiones, describe el recurso tal como está.

La rúbrica se ajustó tras probarla con el MIAE (23-09-2026), que sacó un 65 % por
criterios que no medían lo que se buscaba: lo incrustado o cargado de otros
servidores cuenta solo en el punto 4 (antes restaba también en el 2); el punto 10
castiga el código difícil de entender sin comentarios, no el código corto y claro
que no los lleva; y el punto 1 se limita a lo que el recurso enseña, sin contar
las erratas de las referencias.

La página muestra además la rúbrica en una tabla a la vista, sin plegar, presentada como la rúbrica del archivo de evaluación (marca `<!-- rubrica -->`), que
`construir.py` genera a partir del propio `evaluacion-ia.md`, para que la tabla y
lo que lee la IA no puedan separarse. Por eso la rúbrica mantiene su formato:
`N. TÍTULO`, y debajo `2:`, `1:` y `0:` con su descripción, redactada en forma
impersonal para que sirva igual a la IA y a quien lee la tabla.

Desde la portada, los enlaces a los dos archivos de «Cómo empezar» abren una
ventana en lugar de llevar a esta página, que resulta abrumadora para quien
empieza (25-09-2026). La ventana lleva una instrucción breve (adjuntar el archivo o
pegar el texto), los botones de copiar y descargar, el enlace «Más información» a
la página y una X para cerrar; se cierra también con Escape o al pulsar fuera. No
muestra el texto del archivo, que va oculto solo para copiarlo: quien quiera
leerlo va a la página. Sin JavaScript, el enlace lleva a la página, como antes.

La página explica cómo usarlo en cada familia de herramientas: adjunto al primer
mensaje en un chatbot, como archivo de instrucciones del proyecto en un agente o
editor, y en las instrucciones permanentes del proyecto en las plataformas.

## Alternativas descartadas

- **Dos textos para copiar (empezar y revisar)**: seguía mezclando la guía con la
  descripción del material y obligaba a editar el texto en cada uso.
- **Un archivo solo para empezar y la revisión como texto aparte**: dos piezas
  donde basta una; la revisión se pide con una frase.
- **Mantener una lista de revisión propia en el archivo de crear**: dos listas
  de los mismos diez puntos acaban diciendo cosas distintas, y la persona que
  crea el material recibe una revisión con un criterio distinto del que usará
  quien lo evalúe. Lo que solo pedía esa lista (la breve descripción del material,
  las direcciones externas, lo que falla sin internet y el material ajeno) pasó
  al informe de la evaluación.
- **La rúbrica de evaluación dentro del archivo de crear**: unas setenta líneas
  que acompañarían todo el trabajo sin servir para nada mientras se crea.
- **Exigir un material sin recursos externos**: obliga a programar desde cero lo
  que ya resuelven bibliotecas conocidas, y la web de un chatbot las carga por su
  cuenta.
- **Una sola cifra sin rúbrica ni punto eliminatorio**: la nota variaría de una
  evaluación a otra, y un recurso que envía datos del alumnado podría sacar
  una puntuación alta gracias al resto de puntos.
- **Solo descarga, sin mostrar el contenido**: impide leerlo antes de usarlo y
  deja sin opción a quien trabaja en una plataforma que no admite adjuntos.

## Consecuencias

- Los capítulos remiten a la evaluación VCER por número de punto. Si cambia la
  numeración de la rúbrica, hay que revisar esas remisiones.
- Al traducir la guía, cada idioma necesita su `instrucciones-ia.md` y su
  `evaluacion-ia.md`.
- Revisar un material al terminarlo exige adjuntar un segundo archivo; en un
  agente de programación basta con dejar los dos en la carpeta del proyecto.
