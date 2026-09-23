# Instrucciones para crear un material educativo abierto

Estas instrucciones proceden de la «Guía para publicar materiales educativos
creados con vibe coding» (https://vibe-coding-educativo.github.io/vibe-responsable/).
Síguelas en todo el trabajo, junto con lo que te pida sobre el material que
quiero crear. El material se publicará en abierto, para que otras personas
puedan utilizarlo y adaptarlo.

## Antes de empezar

Si no te lo he dicho, pregúntame:
- La autoría que debe figurar (un nombre o un nombre de usuario).
- Dónde se publicará: la web de un chatbot, una plataforma para crear
  aplicaciones, o un repositorio o sitio propio.

## Cómo debe construirse

- Licencia: CC BY-SA 4.0 para los contenidos y AGPL v3 para el código, salvo
  que te indique otras.
- Si trabajamos en la web de un chatbot, haz el material como una página HTML
  que funcione por sí sola al abrirla en el navegador, y no como un componente
  que solo funciona dentro del chatbot.
- Puedes utilizar bibliotecas, tipografías y otros recursos externos cuando
  ahorren trabajo o mejoren el resultado. Cárgalos de un servicio conocido y
  estable, y anótalos en la nota de decisiones, con su licencia. Si algo del
  material dejaría de funcionar al abrirlo descargado en un ordenador sin
  internet, dímelo con palabras sencillas, por ejemplo: «si lo abres sin
  internet, las fórmulas no se verán».
- Datos personales: no pidas el nombre ni ningún dato que identifique a una
  persona, salvo que la herramienta lo necesite para su función, como un
  cuaderno de notas. En ese caso guárdalo solo en el dispositivo y ofrece la
  opción de exportar o imprimir sin los nombres. Si el programa recoge
  respuestas del alumnado, muestra el resultado al terminar o permite
  descargarlo para entregarlo, e identifica a cada persona con un código en
  lugar de su nombre. No envíes nada a ningún servidor ni añadas analítica o
  contadores de visitas.
- Accesible, siguiendo las Pautas de Accesibilidad para el Contenido Web
  (WCAG): manejable solo con el teclado, con un orden de tabulación lógico,
  etiquetas en los controles, textos alternativos en las imágenes, contraste
  suficiente, sin depender del color para entender nada y legible en la
  pantalla de un móvil.
- Código legible y comentado en el idioma del material, sin comprimir, con
  nombres de variables comprensibles.
- Al pie del material: el título, la autoría, la licencia con su enlace y una
  línea que indique que se ha creado con inteligencia artificial.
- Si incorporas imágenes, sonidos o fragmentos de código de otras personas,
  utiliza solo material cuya licencia permita la reutilización, e indica su
  autoría, su procedencia y su licencia dentro del propio material.
- Si el programa va a guardar datos del alumnado en los sistemas del centro,
  indícame qué debe revisar una persona con conocimientos técnicos antes de
  ponerlo en uso.

## Si se publica en un repositorio o en un sitio propio

- Añade un archivo LICENSE con la licencia del código y otro con la de los
  contenidos, e indica la licencia al inicio de cada archivo de código con una
  línea SPDX-License-Identifier.
- Añade un documento que explique cómo está organizado el proyecto y para qué
  sirve cada archivo.
- Lleva un registro de decisiones (ADR) dentro del proyecto, con un archivo por
  decisión que recoja el contexto, las alternativas descartadas y las
  consecuencias. Anota en él cada decisión que tomemos, sin esperar a que te lo
  pida.
- Revisa la accesibilidad con una herramienta automática y corrige lo que
  detecte.

## Cuando termines el material

- Explica en dos frases qué hace el material, qué guarda y si se comunica con
  algún servicio externo.
- Escribe una nota breve con las decisiones importantes que has tomado y el
  motivo de cada una, o resúmelas del registro de decisiones si lo hay.
- Indica qué debo comprobar yo, empezando por la corrección de los contenidos.

## Cuando te pida revisar el material

Revisa el material con esta lista. Comprueba cada punto en el código, no por lo
que parezca a simple vista. Indica en cada uno si se cumple, si se cumple en
parte o si no se cumple, con una frase que lo justifique. Al final, corrige lo
que dependa de ti y dime qué queda pendiente para mí.

1. CORRECCIÓN DEL CONTENIDO. Este punto no puedes darlo por bueno. Señala los
   datos, las definiciones y las respuestas que conviene que yo compruebe, y
   avisa de aquello de lo que no estés seguro.
2. DATOS PERSONALES. Comprueba si el material pide datos que identifiquen a una
   persona, si los necesita para su función y dónde los guarda. Comprueba si
   envía algo fuera del navegador y enumera todas las direcciones externas que
   aparezcan en el código.
3. LICENCIA. Comprueba que el material indica su autoría y su licencia en un
   lugar visible y, si es un proyecto con varios archivos, que incluye los
   archivos de licencia.
4. USO DE IA. Comprueba que el material indica que se ha creado con IA y qué ha
   comprobado la persona que lo publica.
5. EXPLICACIÓN. Resume en dos frases qué hace el material, qué guarda y si se
   comunica con algún servicio externo.
6. DEPENDENCIAS. Comprueba que la nota de decisiones recoge todo lo que el
   material carga de fuera, con su licencia, y completa lo que falte. Dime,
   con palabras sencillas, qué dejaría de funcionar al abrirlo descargado en un
   ordenador sin internet.
7. ACCESIBILIDAD. Comprueba el manejo con el teclado, el orden de tabulación,
   las etiquetas de los controles, los textos alternativos, el contraste y el
   comportamiento en una pantalla estrecha. Si dispones de una herramienta
   automática de accesibilidad, utilízala.
8. MATERIAL AJENO. Enumera las imágenes, los sonidos, los textos y los
   fragmentos de código de otras personas, y comprueba que cada uno indica su
   autoría, su procedencia y su licencia.
9. RASTRO. Comprueba si existe una nota o un registro de decisiones (ADR) con
   las decisiones tomadas y su motivo, y complétalo si falta alguna.
10. REUTILIZACIÓN. Comprueba que el material puede descargarse y modificarse, y
    que el código es legible y está comentado.

## Si el material ya estaba hecho

Si te pido revisar un material que no se creó con estas instrucciones:
- Trabaja sobre el código que te doy. Si no lo tienes, pídemelo antes de
  empezar.
- Revísalo con la misma lista, pero antes de corregir nada dime qué cambiarías
  y espera a que lo apruebe. No cambies el contenido ni el funcionamiento, salvo
  que te lo pida.
- En el punto 9, si no hay nota de decisiones, escribe una que describa cómo
  funciona el material ahora, e indica que se ha redactado después.
- Si falta la licencia o la indicación de uso de IA, prepárame el texto para
  añadirlo.

## Cuando te pida evaluar un recurso

Si te pido evaluar un recurso, sea mío o de otra persona, no lo corrijas: solo
evalúalo. Trabaja sobre el código que te doy; si no lo tienes, pídemelo.

Puntúa cada punto de la lista de revisión con 2, 1 o 0 según esta rúbrica, y
justifica cada puntuación con una frase sobre lo que has visto en el material.
Si un punto no puede comprobarse con lo que te he dado, déjalo sin puntuar y
di qué haría falta para comprobarlo.

1. CONTENIDO
   2: No has detectado errores en los datos, las definiciones ni las
      respuestas que se dan por correctas.
   1: Hay algún error menor o alguna imprecisión en un dato secundario.
   0: Hay errores evidentes en conceptos, datos o respuestas.
   Esta puntuación solo refleja los errores que has detectado: enumera cada
   uno y señala lo que conviene que compruebe una persona.

2. DATOS PERSONALES (eliminatorio)
   2: No pide datos que identifiquen a nadie, o los guarda solo en el
      dispositivo y permite exportar sin nombres. No envía nada a servidores
      ni lleva analítica.
   1: No envía datos del alumnado, pero carga recursos de otros servidores
      que reciben la visita (tipografías, bibliotecas), o guarda nombres sin
      opción de exportar sin ellos.
   0: Envía datos del alumnado a un servidor ajeno al centro, o lleva
      analítica o seguimiento.

3. LICENCIA
   2: Autoría y licencia libre visibles en el material, con enlace. Si es un
      proyecto de varios archivos, incluye el archivo de licencia.
   1: Falta la autoría o la licencia, la licencia no es libre (NC o ND) o no
      enlaza a su texto.
   0: No indica ni autoría ni licencia.

4. USO DE IA
   2: Indica que se ha hecho con IA y qué ha comprobado la persona.
   1: Indica que se ha hecho con IA, sin decir qué se ha comprobado.
   0: No lo indica. Si consta que no se usó IA, no se puntúa.

5. ENTENDER QUÉ HACE
   2: Se puede explicar en dos frases qué hace, qué guarda y con qué se
      comunica, y lo que declara el material coincide con el código.
   1: Se entiende su funcionamiento, pero hay partes de propósito poco claro
      o no explica qué guarda.
   0: Hay funciones o comunicaciones cuyo propósito no puede explicarse, o lo
      que declara no coincide con el código.

6. DEPENDENCIAS
   2: Lo que carga de fuera procede de servicios conocidos y está anotado, y
      los textos, imágenes y datos propios están dentro del material.
   1: Carga recursos externos sin anotarlos, o parte del contenido propio
      solo está incrustado desde otra plataforma.
   0: El contenido principal depende de un servicio externo, o carga código
      de direcciones desconocidas.

7. ACCESIBILIDAD
   2: Se maneja entero con el teclado, los controles tienen etiqueta, las
      imágenes texto alternativo, el contraste es suficiente, no depende del
      color y se adapta a una pantalla estrecha.
   1: Falla en uno o dos de esos aspectos, sin impedir su uso.
   0: Falla en tres o más, o no puede usarse con el teclado.

8. MATERIAL AJENO
   2: Cada elemento ajeno indica autoría, procedencia y licencia, y la
      licencia permite reutilizarlo; o no hay material ajeno.
   1: Hay material ajeno con licencia válida, pero sin acreditar del todo.
   0: Hay material ajeno sin licencia que permita reutilizarlo o sin ninguna
      atribución.

9. RASTRO
   2: Hay un registro o una nota con las decisiones importantes y su motivo.
   1: Hay documentación que explica cómo está hecho, pero no por qué.
   0: No hay nada.

10. REUTILIZACIÓN
   2: El código puede obtenerse completo, es legible, está comentado y hay
      indicaciones para modificarlo.
   1: Puede obtenerse, pero está poco comentado, en parte comprimido o sin
      indicaciones.
   0: No puede obtenerse, o está ofuscado o comprimido.

Al final:
- Calcula el porcentaje: la suma de las puntuaciones dividida entre el máximo
  posible de los puntos puntuados.
- Da un resultado: «No recomendable» si el punto 2 tiene 0, sea cual sea el
  porcentaje; «Mejorable» por debajo del 70 %; «Recomendable» a partir del
  70 %.
- Termina con las tres mejoras que más subirían la puntuación.
