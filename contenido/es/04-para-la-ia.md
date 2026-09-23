# Instrucciones para la IA

## Para qué sirven estos textos

Las diez recomendaciones de la guía pueden darse directamente a la inteligencia artificial (IA), de modo que el trabajo de cumplirlas no recaiga sobre la persona. El primer texto se entrega al empezar, para que el material se genere ya conforme a la guía. El segundo se entrega al terminar, para revisar lo que se ha obtenido.

Ambos textos sirven en cualquier herramienta, desde la web de un chatbot hasta un agente de programación. Basta con indicar en el primero dónde se publicará el material, y la IA aplica las condiciones que corresponden cuando se trata de un repositorio o de un sitio propio. Conviene tener presente que la revisión de la IA no sustituye a la de la persona, ya que el modelo también se equivoca al revisar su propio trabajo.

## Al empezar un material

```
Vas a crear un material educativo que después se publicará en abierto, para que
otras personas puedan utilizarlo y adaptarlo.

EL MATERIAL
- Qué tiene que hacer: [describir aquí lo que se necesita]
- A quién va dirigido: [materia, curso o edad del alumnado]
- Autoría que debe figurar: [nombre o nombre de usuario]
- Licencia: CC BY-SA 4.0
- Dónde se publicará: [la web del chatbot, una plataforma, o un repositorio o
  sitio propio]

CÓMO DEBE CONSTRUIRSE
- Salvo que se publique en un repositorio o en un sitio propio, un único
  archivo HTML, con los estilos y el código dentro, sin bibliotecas,
  tipografías ni servicios externos, de forma que funcione sin conexión y pueda
  incrustarse en otra página.
- Datos personales: no pidas el nombre ni ningún dato que identifique a una
  persona, salvo que la herramienta lo necesite para su función, como un
  cuaderno de notas. En ese caso guárdalo solo en el dispositivo y ofrece la
  opción de exportar o imprimir sin los nombres. Si el programa recoge
  respuestas del alumnado, muestra el resultado al terminar o permite
  descargarlo para entregarlo, e identifica a cada persona con un código en
  lugar de su nombre. No envíes nada a ningún servidor ni añadas analítica o
  contadores de visitas.
- Accesible: manejable solo con el teclado, con un orden de tabulación lógico,
  etiquetas en los controles, textos alternativos en las imágenes, contraste
  suficiente, sin depender del color para entender nada y legible en la pantalla
  de un móvil.
- Código legible y comentado en español, sin comprimir, con nombres de variables
  comprensibles.
- Al pie del material: el título, la autoría, la licencia con su enlace y una
  línea que indique que se ha creado con inteligencia artificial.
- Si incorporas imágenes, sonidos o fragmentos de código de otras personas,
  utiliza solo material cuya licencia permita la reutilización, e indica su
  autoría, su procedencia y su licencia dentro del propio material.
- Si el programa va a guardar datos del alumnado en los sistemas del centro,
  indícame qué debe revisar una persona con conocimientos técnicos antes de
  ponerlo en uso.

SI SE PUBLICA EN UN REPOSITORIO O EN UN SITIO PROPIO
- El proyecto puede tener varios archivos, pero debe contener todo lo que
  necesita para funcionar, sin depender de servicios externos.
- Añade un archivo de licencia, con una licencia de software libre para el
  código y una Creative Commons libre para los contenidos.
- Añade un documento que explique cómo está organizado el proyecto y para qué
  sirve cada archivo.
- Lleva un registro de decisiones (ADR) dentro del proyecto, con un archivo por
  decisión que recoja el contexto, las alternativas descartadas y las
  consecuencias. Anota en él cada decisión que tomemos, sin esperar a que te lo
  pida.
- Revisa la accesibilidad con una herramienta automática y corrige lo que
  detecte.

CUANDO TERMINES
- Explica en dos frases qué hace el material, qué guarda y si se comunica con
  algún servicio externo.
- Escribe una nota breve con las decisiones importantes que has tomado y el
  motivo de cada una, o resúmelas del registro de decisiones si lo hay.
- Indica qué debo comprobar yo, empezando por la corrección de los contenidos.
```

## Al terminar, para revisar

```
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
   lugar visible y, si es un proyecto con varios archivos, que incluye el
   archivo de licencia.
4. USO DE IA. Comprueba que el material indica que se ha creado con IA y qué ha
   comprobado la persona que lo publica.
5. EXPLICACIÓN. Resume en dos frases qué hace el material, qué guarda y si se
   comunica con algún servicio externo.
6. DEPENDENCIAS. Enumera lo que el material necesita para funcionar y no está
   dentro del archivo, e indica si dejaría de funcionar sin conexión.
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
```
