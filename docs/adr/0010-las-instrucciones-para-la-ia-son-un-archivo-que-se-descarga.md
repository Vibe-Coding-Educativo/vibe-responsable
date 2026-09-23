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
  internet. El capítulo 6 sigue el mismo criterio;
- incluye la lista de revisión, que se activa con «revisa el material según las
  instrucciones».
Evaluar un recurso ya hecho tiene su propio archivo, `contenido/<idioma>/evaluacion-ia.md`,
publicado como `evaluacion-vibe-responsable.md` y mostrado en la misma página (marca
`<!-- evaluacion -->`). Sirve para recursos propios o ajenos, hechos o no con la
guía, y no corrige nada:

- una rúbrica de 2, 1 o 0 para cada uno de los diez puntos, con un nivel
  descrito para cada valor y una frase que justifique la nota; lo que no puede
  comprobarse queda sin puntuar;
- un porcentaje sobre los puntos puntuados, con «No recomendable» si el punto 2
  (datos personales) tiene 0, «Mejorable» por debajo del 70 % y «Recomendable»
  desde el 70 %, y las tres mejoras que más subirían la nota;
- el punto 1 se puntúa con los errores que la IA detecta por su cuenta, que
  bastan para ver un recurso sin revisar, aunque no certifican el contenido;
- si después se pide corregir, la IA propone los cambios antes de hacerlos y,
  si no hay nota de decisiones, describe el recurso tal como está.

La página muestra además la rúbrica en una tabla (marca `<!-- rubrica -->`), que
`construir.py` genera a partir del propio `evaluacion-ia.md`, para que la tabla y
lo que lee la IA no puedan separarse. Por eso la rúbrica mantiene su formato:
`N. TÍTULO`, y debajo `2:`, `1:` y `0:` con su descripción, redactada en forma
impersonal para que sirva igual a la IA y a quien lee la tabla.

La página explica cómo usarlo en cada familia de herramientas: adjunto al primer
mensaje en un chatbot, como archivo de instrucciones del proyecto en un agente o
editor, y en las instrucciones permanentes del proyecto en las plataformas.

## Alternativas descartadas

- **Dos textos para copiar (empezar y revisar)**: seguía mezclando la guía con la
  descripción del material y obligaba a editar el texto en cada uso.
- **Un archivo solo para empezar y la revisión como texto aparte**: dos piezas
  donde basta una; la revisión se pide con una frase.
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

- Los capítulos remiten al «archivo de instrucciones para la IA» y a su
  apartado de revisión, por número de punto. Si cambia la numeración de la
  lista de revisión, hay que revisar esas remisiones.
- Al traducir la guía, cada idioma necesita su `instrucciones-ia.md` y su
  `evaluacion-ia.md`.
- Los dos archivos repiten los diez puntos: un cambio en uno debe llevarse al
  otro.
