# Instrucciones para la IA

## Para qué sirven estos textos

Las diez recomendaciones de la guía pueden darse directamente a la inteligencia artificial, de modo que el trabajo de cumplirlas no recaiga sobre la persona. El primer texto se entrega al empezar, para que el material se genere ya conforme a la guía. El segundo se entrega al terminar, para revisar lo que se ha obtenido.

Ambos textos sirven en cualquier herramienta, desde la web de un chatbot hasta un agente de programación. Conviene tener presente que la revisión de la IA no sustituye a la de la persona, ya que el modelo también se equivoca al revisar su propio trabajo.

## Al empezar un material

```
Vas a crear un material educativo que después se publicará en abierto, para que
otras personas puedan utilizarlo y adaptarlo.

EL MATERIAL
- Qué tiene que hacer: [describir aquí lo que se necesita]
- A quién va dirigido: [materia, curso o edad del alumnado]
- Autoría que debe figurar: [nombre o nombre de usuario]
- Licencia: CC BY-SA 4.0

CÓMO DEBE CONSTRUIRSE
- Un único archivo HTML, con los estilos y el código dentro, sin bibliotecas,
  tipografías ni servicios externos, de forma que funcione sin conexión y pueda
  incrustarse en otra página.
- Sin datos personales: no pidas el nombre ni ningún dato que identifique a una
  persona. Si hay que conservar algo, como las respuestas o el progreso, que se
  quede en el navegador y no se envíe a ningún servidor. Sin analítica ni
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

CUANDO TERMINES
- Explica en dos frases qué hace el material, qué guarda y si se comunica con
  algún servicio externo.
- Escribe una nota breve con las decisiones importantes que has tomado y el
  motivo de cada una.
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
   persona y si envía algo fuera del navegador. Enumera todas las direcciones
   externas que aparezcan en el código.
3. LICENCIA. Comprueba que el material indica su autoría y su licencia en un
   lugar visible.
4. USO DE IA. Comprueba que el material indica que se ha creado con IA y qué ha
   comprobado la persona que lo publica.
5. EXPLICACIÓN. Resume en dos frases qué hace el material, qué guarda y si se
   comunica con algún servicio externo.
6. DEPENDENCIAS. Enumera lo que el material necesita para funcionar y no está
   dentro del archivo, e indica si dejaría de funcionar sin conexión.
7. ACCESIBILIDAD. Comprueba el manejo con el teclado, el orden de tabulación,
   las etiquetas de los controles, los textos alternativos, el contraste y el
   comportamiento en una pantalla estrecha.
8. MATERIAL AJENO. Enumera las imágenes, los sonidos, los textos y los
   fragmentos de código de otras personas, y comprueba que cada uno indica su
   autoría, su procedencia y su licencia.
9. RASTRO. Comprueba si existe una nota con las decisiones tomadas y su motivo,
   y complétala si falta alguna.
10. REUTILIZACIÓN. Comprueba que el material puede descargarse y modificarse, y
    que el código es legible y está comentado.
```

## Si se trabaja con un repositorio

Quien publique el material en un repositorio o en un sitio propio puede añadir estas condiciones al primer texto, que corresponden a lo recomendado en cada punto de la guía.

```
- Añade al proyecto un archivo de licencia, con una licencia de software libre
  para el código y una Creative Commons libre para los contenidos.
- Añade un documento que explique cómo está organizado el proyecto y para qué
  sirve cada archivo.
- Lleva un registro de decisiones dentro del proyecto, con un archivo por
  decisión que recoja el contexto, las alternativas descartadas y las
  consecuencias. Anota en él cada decisión que tomemos, sin esperar a que te lo
  pida.
- Revisa la accesibilidad con una herramienta automática y corrige lo que
  detecte.
```
