# Instrucciones para crear un material educativo abierto

Estas instrucciones proceden de la guía «Vibe coding responsable», para
publicar materiales educativos creados con vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/).
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
  no escribas claves ni contraseñas en el código que llega al navegador, haz
  que solo el docente o el centro puedan leer lo recogido e indícame qué debe
  revisar una persona con conocimientos técnicos antes de ponerlo en uso.
- Después de cada cambio, vuelve a comprobar lo que ya funcionaba: ejecuta las
  pruebas si las hay o, si no puedes hacerlo, dime qué comprobaciones debo
  repetir.

## Si se publica en un repositorio o en un sitio propio

- Añade un archivo LICENSE con la licencia del código y otro con la de los
  contenidos, e indica la licencia al inicio de cada archivo de código con una
  línea SPDX-License-Identifier.
- Añade un documento que explique cómo está organizado el proyecto y para qué
  sirve cada archivo.
- Lleva un registro de decisiones (ADR) dentro del proyecto, con un archivo por
  decisión que recoja el contexto, las alternativas descartadas y las
  consecuencias. Anota en él cada decisión que tomemos, sin esperar a que te lo
  pida. En las decisiones técnicas, anota también en qué te basas
  (documentación oficial, una versión concreta del código o una prueba que
  pueda repetirse), los riesgos conocidos y cómo lo has comprobado. No inventes
  fuentes ni pruebas: lo que no hayas podido comprobar, márcalo como hipótesis
  pendiente de validación.
- Revisa la accesibilidad con una herramienta automática y corrige lo que
  detecte.

## Cuando termines el material

- Describe brevemente qué hace el material, qué guarda y si se comunica con
  algún servicio externo.
- Prepara una lista breve de comprobaciones con los recorridos principales y
  los casos extremos, para repetirla después de cada cambio. Si el proyecto lo
  permite, conviértela en pruebas automáticas.
- Escribe una nota breve con las decisiones importantes que has tomado y el
  motivo de cada una, o resúmelas del registro de decisiones si lo hay.
- Indica qué debo comprobar yo, empezando por la corrección de los contenidos.
