# Antes de publicar: diez recomendaciones

Esta guía nace de dos motivos, uno ético y otro legal. El motivo ético es que quien crea un material con ayuda de la inteligencia artificial se beneficia del conocimiento que otras personas han compartido antes, desde el software libre hasta los recursos educativos abiertos. Publicar un material que nadie más puede reutilizar, que deja fuera a parte del alumnado o que oculta cómo se ha hecho es una actitud poco solidaria con esa comunidad. Lo habitual es que ocurra por desconocimiento y no por mala intención.

El motivo legal es que publicar un material convierte a su autor en responsable de lo que ese material hace, y algunas decisiones que parecen técnicas tienen consecuencias jurídicas. Recoger datos del alumnado sin que el centro lo haya autorizado puede vulnerar la normativa de protección de datos, que es especialmente estricta cuando se trata de menores. Incorporar imágenes, textos o piezas de software sin respetar su licencia vulnera los derechos de sus autores. En ambos casos la responsabilidad recae en la persona que publica, y no en la IA que generó el material.

La lista que sigue reúne las diez recomendaciones de la guía, de forma que también sirve para revisar un material que ya está hecho. Cada una enlaza con el capítulo donde se explica con más detalle. Las que tienen consecuencias legales son, sobre todo, la 2, la 3 y la 8, mientras que las demás responden al compromiso con el alumnado y con la comunidad docente. Las tres primeras son las esenciales, por lo que conviene empezar por ellas.

No todas las personas trabajan con los mismos medios. Muchas crean sus materiales dentro de la **web de un chatbot**, donde la aplicación queda alojada en la propia plataforma, se comparte mediante un enlace y no siempre puede sacarse de ella. Otra posibilidad es utilizar **agentes de programación**, que son programas de IA que trabajan directamente con los archivos del ordenador, como [Codex CLI](https://developers.openai.com/codex/cli), [Antigravity](https://antigravity.google/) o [Claude Code](https://claude.com/product/claude-code), por citar algunos de los disponibles en 2026. En este caso el código queda en manos de quien lo crea y puede publicarse en un sitio propio o en un repositorio como [GitHub](https://github.com/), lo que da mucho más margen. Por este motivo, cada recomendación indica lo mínimo, que puede cumplirse en cualquier caso, y lo que conviene añadir cuando se dispone del código alojado en algún repositorio. En el artículo [«Consolas de IA: qué son y cómo se instalan»](https://educacion.bilateria.org/consolas-de-ia-en-2026-que-son-como-se-instalan-y-que-cuestan-ahora/) se explica cómo empezar a trabajar con estos agentes.

## 1\. El contenido es correcto y lo ha revisado una persona

La IA puede equivocarse con total naturalidad, y un error en una simulación o en un cuestionario acaba siendo un aprendizaje equivocado. Antes de publicar hay que usar el material como lo haría el alumnado y comprobar los conceptos, los datos y las respuestas que da por buenas. Esta revisión no se puede delegar, ya que la responsabilidad de lo que se enseña es de quien lo publica.

- **Lo mínimo.** Recorrer el material de principio a fin, también con respuestas equivocadas, y revisar cada resultado con el criterio de la materia.
- **Si se dispone del código.** Lo mismo. En este punto no hay diferencia entre una forma de trabajar y otra.

## 2\. No recoge datos personales, o los datos no salen del dispositivo

El nombre, las notas, la voz o la imagen del alumnado son datos personales. En la Unión Europea, decidir cómo se tratan corresponde al centro o a la administración educativa, y no a cada docente por su cuenta. Otros países tienen normas distintas, pero la precaución es la misma. La forma más sencilla de cumplir es que el material no pida datos, o que todo lo que se escriba en él se quede en el navegador de quien lo usa.

- **Lo mínimo.** No pedir nombres reales ni nada que identifique a una persona. Si el material se abre dentro de la plataforma de un chatbot, hay que comprobar si exige registro o una edad mínima antes de enviar el enlace al alumnado, ya que se le está llevando al servicio de un tercero.
- **Si se dispone del código.** Comprobar que no envía información a ningún servidor. Basta con buscar en el código las direcciones web que aparecen y preguntar por las que no se reconozcan.

## 3\. Lleva una licencia libre a la vista

Todo lo que se crea queda protegido por derechos de autor de forma automática, de modo que un material sin licencia no puede reutilizarse legalmente aunque esté publicado. Una licencia libre indica a las demás personas que pueden usarlo, adaptarlo y compartirlo, y con qué condiciones. El código y los contenidos necesitan licencias distintas, y lo generado por la IA plantea dudas de autoría que se tratan en su capítulo.

- **Lo mínimo.** Escribir la autoría y la licencia dentro del propio material, en un lugar visible, por ejemplo al pie.
- **Si se dispone del código.** Añadir el archivo de licencia al repositorio, con una licencia de software libre para el código y una Creative Commons para los contenidos.

## 4\. Explica qué ha hecho la IA y qué ha hecho la persona

Quien reutiliza un material necesita saber cómo se ha creado para decidir cuánto puede fiarse de él. Una declaración breve indica qué herramientas se han usado, qué partes se han generado de forma automática y qué se ha revisado a mano.

- **Lo mínimo.** Una o dos frases dentro del material, junto a la licencia.
- **Si se dispone del código.** Una sección en la documentación que incluya, además, las instrucciones principales que se dieron a la IA.

## 5\. Quien lo publica sabe explicar qué hace

Un material cuyo funcionamiento no entiende ni su autor deja de ser abierto en la práctica, ya que nadie podrá corregirlo cuando falle. No hace falta saber programar para cumplir este punto. Basta con poder resumir en dos frases qué hace la aplicación, qué guarda y si se comunica con algún servicio externo.

- **Lo mínimo.** Pedir a la IA que explique en lenguaje llano qué hace la aplicación y si guarda o envía algo, y comprobar que la explicación coincide con lo que se observa al usarla.
- **Si se dispone del código.** Pedir que el código esté comentado y sea legible. El código ilegible, comprimido en líneas interminables, es motivo suficiente para no publicar.

## 6\. No depende de servicios que pueden desaparecer

Un recurso que incrusta contenido de otra web, o que carga piezas desde servidores ajenos, deja de funcionar cuando esos servicios cambian o cierran. Lo mismo ocurre con la propia plataforma del chatbot, puesto que el enlace compartido dura lo que la empresa decida.

- **Lo mínimo.** Guardar una copia de la conversación con la que se creó el material y, si la plataforma lo permite, del archivo resultante.
- **Si se dispone del código.** Incluir dentro del material todo lo que necesita para funcionar, de forma que pueda usarse incluso sin conexión.

## 7\. Puede usarse con teclado, con lector de pantalla y en un móvil

Los materiales generados con IA tienden a lo vistoso, y los efectos decorativos suelen ser un obstáculo para parte del alumnado. Un material accesible se maneja sin ratón, se entiende sin depender del color y se lee bien en una pantalla pequeña.

- **Lo mínimo.** Pedir a la IA desde el principio que siga las pautas de accesibilidad, y probar el resultado solo con el teclado, con el texto ampliado y en un teléfono.
- **Si se dispone del código.** Pasar, además, una herramienta automática de revisión de accesibilidad y corregir lo que detecte.

## 8\. Acredita lo que toma de otras personas

Las imágenes, los textos, los sonidos y las piezas de software que se incorporan tienen autoría y licencia, aunque los haya colocado la IA. La atribución debe ir dentro del propio material, para que lo acompañe cuando circule fuera de su contexto.

- **Lo mínimo.** Indicar autoría, procedencia y licencia de cada elemento ajeno, y sustituir los que no permitan la reutilización.
- **Si se dispone del código.** Revisar, además, las licencias de las bibliotecas de software incluidas, ya que algunas condicionan la licencia del conjunto.

## 9\. Conserva el rastro de cómo se hizo

Con la IA se avanza muy deprisa, y a las pocas semanas nadie recuerda por qué se tomó cada decisión. Conservar ese rastro permite retomar el trabajo, explicarlo a otra persona y no deshacer por error lo que tenía un motivo.

- **Lo mínimo.** Guardar la conversación y una nota breve con las decisiones importantes y su porqué.
- **Si se dispone del código.** Llevar un registro de decisiones en el propio repositorio, una por archivo, con el contexto, las alternativas descartadas y las consecuencias.

## 10\. Otra persona puede descargarlo, modificarlo y mejorarlo

La licencia da el permiso, pero no basta si el material no puede obtenerse en una forma que permita trabajar con él. Un recurso educativo es abierto de verdad cuando otro docente puede adaptarlo a su aula sin pedir nada a nadie.

- **Lo mínimo.** Ofrecer el archivo para descargar si la plataforma lo permite. Si no lo permite, compartir las instrucciones con las que se creó, de forma que otra persona pueda rehacerlo.
- **Si se dispone del código.** Publicarlo en un repositorio abierto, con una explicación de cómo usarlo y cómo modificarlo.

Al final de la guía se incluye esta misma lista preparada para dársela a la IA, tanto al empezar un material, para que lo genere cumpliéndola, como al terminarlo, para que ayude a revisarlo.