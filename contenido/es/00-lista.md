# Antes de publicar: diez recomendaciones

Esta guía nace de dos motivos, uno ético y otro legal. El motivo ético es que todo material creado con ayuda de la inteligencia artificial se beneficia del conocimiento que otras personas han compartido antes, desde el software libre hasta los recursos educativos abiertos. Publicar un material que nadie más puede reutilizar, que deja fuera a parte del alumnado o que oculta cómo se ha hecho es una actitud poco solidaria con esa comunidad. Lo habitual es que ocurra por desconocimiento y no por mala intención.

El motivo legal es que publicar un material convierte a su autor en responsable de lo que ese material hace, y algunas decisiones que parecen técnicas tienen consecuencias jurídicas. Recoger datos del alumnado sin que el centro lo haya autorizado puede vulnerar la normativa de protección de datos, que es especialmente estricta cuando se trata de menores. Incorporar imágenes, textos o piezas de software sin respetar su licencia vulnera los derechos de sus autores. En ambos casos la responsabilidad recae en la persona que publica, y no en la IA que generó el material.

La lista que sigue reúne las diez recomendaciones de la guía, de forma que también sirve para revisar un material que ya está hecho. Cada una enlaza con el capítulo donde se explica con más detalle. Las que tienen consecuencias legales son, sobre todo, la 2, la 3 y la 8, mientras que las demás responden al compromiso con el alumnado y con la comunidad docente.

No todas las personas trabajan con los mismos medios, y las herramientas para crear programas con IA son muy variadas. A grandes rasgos pueden agruparse en cuatro familias, que se presentan a continuación con algunos ejemplos de las disponibles en 2026.

- **La web de un chatbot.** Asistentes generales como [ChatGPT](https://chatgpt.com/), [Gemini](https://gemini.google.com/) o [Claude](https://claude.ai/), que crean la aplicación dentro de la propia conversación. El material queda alojado en la plataforma y se comparte mediante un enlace.
- **Plataformas para crear aplicaciones.** Servicios como [Lovable](https://lovable.dev/), [Bolt](https://bolt.new/), [Replit](https://replit.com/), [Google AI Studio](https://aistudio.google.com/) o [Canva](https://www.canva.com/), que generan, alojan y publican la aplicación desde el navegador. Algunas permiten enviar el proyecto a un repositorio externo.
- **Editores de código con IA.** Programas como [Visual Studio Code](https://code.visualstudio.com/) o [Cursor](https://cursor.com/), que se instalan en el ordenador e incorporan un asistente que escribe y modifica los archivos del proyecto.
- **Agentes de programación.** Programas como [Codex CLI](https://developers.openai.com/codex/cli), [Antigravity (agy)](https://antigravity.google/) o [Claude Code](https://claude.com/product/claude-code), que reciben las instrucciones en lenguaje natural y trabajan directamente con los archivos del ordenador.

A efectos de esta guía no importa tanto la herramienta como la forma de trabajar que permite. En las dos primeras familias se suele poder ver el código, e incluso modificarlo, pero el material es una pieza única que vive en los servidores de una empresa. No es posible acompañarlo de otros archivos, como la licencia o la documentación, ni llevar un control cómodo de los cambios, y es la empresa la que decide cuánto tiempo se mantiene. En las dos últimas el material es una carpeta de archivos en el propio ordenador, que puede publicarse en un sitio propio o en un repositorio como [GitHub](https://github.com/), donde cada cambio queda registrado. Por este motivo, cada recomendación se concreta en dos indicaciones. **Lo mínimo** es lo que puede cumplirse con cualquier herramienta, incluso cuando el material se ha creado y se comparte dentro de la web de un chatbot, y es suficiente para publicar de forma responsable. **Lo recomendado** es lo que conviene hacer además, y requiere que el material sea un proyecto con sus propios archivos, publicado en un repositorio o en un sitio propio. Algunas plataformas permiten enviar el proyecto a un repositorio externo, y en ese caso pueden seguirse también estas indicaciones. Cuando no hay diferencia entre una forma de trabajar y otra, se da una sola indicación. En el artículo [«Consolas de IA: qué son y cómo se instalan»](https://educacion.bilateria.org/consolas-de-ia-en-2026-que-son-como-se-instalan-y-que-cuestan-ahora/) se explica cómo empezar a trabajar con los agentes de programación.

## 1\. El contenido es correcto y lo ha revisado una persona

La IA puede equivocarse con total naturalidad, y un error en una simulación o en un cuestionario acaba siendo un aprendizaje equivocado. Antes de publicar hay que usar el material como lo haría el alumnado y comprobar los conceptos, los datos y las respuestas que da por buenas. Esta revisión no se puede delegar, ya que la responsabilidad de lo que se enseña es de la persona que lo publica.

- **En todos los casos.** Recorrer el material de principio a fin, también con respuestas equivocadas, y revisar cada resultado con el criterio de la materia.

## 2\. No recoge datos personales, o los datos no salen del dispositivo

El nombre, las notas, la voz o la imagen del alumnado son datos personales. En la Unión Europea, decidir cómo se tratan corresponde al centro o a la administración educativa, y no a cada docente por su cuenta. Otros países tienen normas distintas, pero la precaución es la misma. La forma más sencilla de cumplir es que el material no pida datos, o que todo lo que se escriba en él se quede en el navegador donde se usa. Hay que tener especial cuidado con las plataformas que añaden con facilidad cuentas de usuario y bases de datos, ya que entonces los datos se guardan en servidores ajenos.

- **Lo mínimo.** No pedir nombres reales ni nada que identifique a una persona, y preguntar a la IA si la aplicación envía información a algún servidor. Si el material se abre dentro de una plataforma, hay que comprobar si exige registro o una edad mínima antes de enviar el enlace al alumnado, ya que se le está llevando al servicio de un tercero.
- **Lo recomendado.** Publicar el material en un sitio que el alumnado pueda abrir sin registrarse, y comprobar que el código no contiene direcciones web de servicios que no se reconozcan.

## 3\. Lleva una licencia libre a la vista

Todo lo que se crea queda protegido por derechos de autor de forma automática, de modo que un material sin licencia no puede reutilizarse legalmente aunque esté publicado. Una licencia libre indica a las demás personas que pueden usarlo, adaptarlo y compartirlo, y con qué condiciones. El código y los contenidos necesitan licencias distintas, y lo generado por la IA plantea dudas de autoría que se tratan en su capítulo.

- **Lo mínimo.** Escribir la autoría y la licencia dentro del propio material, en un lugar visible, por ejemplo al pie.
- **Lo recomendado.** Añadir el archivo de licencia al proyecto, con una licencia de software libre para el código y una Creative Commons para los contenidos.

## 4\. Indica que se ha hecho con IA y qué ha comprobado la persona

En un material creado con vibe coding el código es obra de la IA, y lo habitual es que nadie lo haya revisado línea a línea. Las personas que lo reutilicen deben saberlo para decidir cuánto pueden fiarse de él. Por ello conviene indicar con qué herramienta se ha creado y, sobre todo, qué ha comprobado la persona que lo publica, como la corrección de los contenidos, el funcionamiento o el tratamiento de los datos.

- **Lo mínimo.** Una o dos frases dentro del material, junto a la licencia, con la herramienta utilizada y lo que se ha comprobado.
- **Lo recomendado.** La misma declaración en la documentación del proyecto, con un enlace al registro de decisiones del punto 9, que es el que explica cómo se hizo el material.

## 5\. Se puede explicar qué hace en dos frases

Un material cuyo funcionamiento no entiende ni su autor deja de ser abierto en la práctica, ya que nadie podrá corregirlo cuando falle. No hace falta saber programar para cumplir este punto. Basta con poder resumir en dos frases qué hace la aplicación, qué guarda y si se comunica con algún servicio externo.

- **Lo mínimo.** Pedir a la IA que explique en lenguaje llano qué hace la aplicación y si guarda o envía algo, y comprobar que la explicación coincide con lo que se observa al usarla. Pedir también que el código esté comentado y sea legible, ya que el código comprimido en líneas interminables es motivo suficiente para no publicar.
- **Lo recomendado.** Añadir un documento que explique cómo está organizado el proyecto y para qué sirve cada archivo.

## 6\. No depende de servicios que pueden desaparecer

Un recurso que incrusta contenido de otra web, o que carga piezas desde servidores ajenos, deja de funcionar cuando esos servicios cambian o cierran. Lo mismo ocurre con la propia plataforma del chatbot, puesto que el enlace compartido dura lo que la empresa decida.

- **Lo mínimo.** Guardar en el propio ordenador una copia de la conversación con la que se creó el material y otra del código resultante.
- **Lo recomendado.** Incluir dentro del proyecto todo lo que necesita para funcionar, de forma que pueda usarse incluso sin conexión.

## 7\. Puede usarse con teclado, con lector de pantalla y en un móvil

Los materiales generados con IA tienden a lo vistoso, y los efectos decorativos suelen ser un obstáculo para parte del alumnado. Un material accesible se maneja sin ratón, se entiende sin depender del color y se lee bien en una pantalla pequeña.

- **Lo mínimo.** Pedir a la IA desde el principio que siga las pautas de accesibilidad, y probar el resultado solo con el teclado, con el texto ampliado y en un teléfono.
- **Lo recomendado.** Pedir a la IA que revise la accesibilidad con una herramienta automática y corrija lo que detecte. Los agentes de programación pueden hacerlo sin ayuda, ya que instalan la herramienta, la ejecutan y aplican las correcciones.

## 8\. Acredita lo que toma de otras personas

Las imágenes, los textos, los sonidos y las piezas de software que se incorporan tienen autoría y licencia, aunque los haya colocado la IA. La atribución debe ir dentro del propio material, para que lo acompañe cuando circule fuera de su contexto.

- **Lo mínimo.** Indicar autoría, procedencia y licencia de cada elemento ajeno, y sustituir los que no permitan la reutilización.
- **Lo recomendado.** Revisar, además, las licencias de las bibliotecas de software incluidas, ya que algunas condicionan la licencia del conjunto.

## 9\. Conserva el rastro de cómo se hizo

Con la IA se avanza muy deprisa, y a las pocas semanas nadie recuerda por qué se tomó cada decisión. Conservar ese rastro permite retomar el trabajo, explicarlo a otra persona y no deshacer por error lo que tenía un motivo.

- **Lo mínimo.** Mantener un documento con las decisiones importantes y su porqué. Lo redacta la propia IA cuando se le pide al terminar cada sesión de trabajo, y solo queda revisarlo y guardarlo.
- **Lo recomendado.** Pedir a la IA que lleve un registro de decisiones dentro del proyecto. Es la IA la que lo escribe, a partir de lo que se decide en la conversación, con un archivo por decisión que recoge el contexto, las alternativas descartadas y las consecuencias. A los agentes de programación basta con indicárselo una vez en sus instrucciones, y después solo queda revisar que lo anotado corresponde a lo decidido. El control de versiones conserva, además, la historia de los cambios.

## 10\. Otra persona puede descargarlo, modificarlo y mejorarlo

La licencia da el permiso, pero no basta si el material no puede obtenerse en una forma que permita trabajar con él. Un recurso educativo es abierto de verdad cuando otro docente puede adaptarlo a su aula sin pedir nada a nadie.

- **Lo mínimo.** Ofrecer el código para copiarlo o descargarlo, acompañado de la nota de decisiones del punto 9, de forma que otra persona pueda continuarlo.
- **Lo recomendado.** Publicarlo en un repositorio abierto, con una explicación de cómo usarlo y cómo modificarlo.

Al final de la guía se incluye esta misma lista preparada para dársela a la IA, tanto al empezar un material, para que lo genere cumpliéndola, como al terminarlo, para que ayude a revisarlo.