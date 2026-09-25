# Guardar el rastro de cómo se hizo

## El motivo de cada decisión

Con la inteligencia artificial (IA) se programa muy deprisa, y a las pocas semanas nadie recuerda por qué se tomó cada decisión. Ernesto Serrano, del equipo de eXeLearning, lo describe en su ponencia [«Inteligencia artificial: programar, documentar y no acabar en un berenjenal»](https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html): el código está, pero el porqué no, y nadie recuerda qué alternativas se descartaron ni con qué argumentos. La IA no causa ese desorden, aunque hace que llegue antes.

Conservar el rastro sirve para tres cosas. Permite retomar el trabajo después de un tiempo sin tener que reconstruirlo, permite explicarlo a otra persona que quiera continuarlo, y evita deshacer de buena fe una decisión que tenía un motivo. En un material educativo abierto tiene una cuarta utilidad, ya que muestra a las personas que lo reutilizan cómo se hizo, que es lo que completa la declaración de la recomendación 8.

## El registro de decisiones

La forma habitual de conservarlo en el desarrollo de software es el registro de decisiones de arquitectura, o ADR, por las siglas de su nombre en inglés, *Architecture Decision Record*. Cada decisión importante se anota en un documento breve que recoge cuatro cosas:

- **El contexto.** La situación que obliga a decidir.
- **La decisión.** Lo que se hace, con el detalle suficiente para aplicarlo.
- **Las alternativas descartadas.** Cada una con el motivo por el que no se eligió, que es la parte que evita repetir el debate más adelante.
- **Las consecuencias.** Lo que mejora y lo que empeora.

Una decisión que deja de valer no se borra, sino que se marca como sustituida por la nueva, de modo que el rastro se conserva. En el proyecto que presenta la ponencia, cada registro anota además con qué herramienta de IA y con qué modelo se tomó la decisión, lo que permite cambiar de herramienta sin perder la historia.

En ese mismo proyecto, cada registro recoge también la evidencia en la que se apoya la decisión, los riesgos conocidos y la forma en que se validó. La ponencia lo resume en la regla «sin fuente no hay afirmación»: cada dato remite a la documentación oficial, a una versión concreta del código o a una prueba que cualquiera puede repetir. Esta precaución es especialmente útil con IA, ya que puede redactar una justificación convincente de una decisión que parte de una premisa falsa. La evidencia anotada permite a la persona comprobarla sin rehacer el trabajo. Lo que no se ha podido verificar se anota como hipótesis pendiente de validación, de forma que nadie lo tome después por un hecho comprobado.

## El trabajo de la IA y el de la persona

El registro no supone una tarea añadida para el docente, ya que lo escribe la IA a partir de lo que se decide en la conversación, y la persona comprueba que lo anotado corresponde a lo decidido. La ponencia lo resume en que la IA propone y la persona dispone.

El registro tampoco se reconstruye al final, ya que un material suele salir de muchas sesiones de trabajo repartidas en días distintos, y recomponer después esas conversaciones resulta inviable. El registro se escribe en el momento en que se decide, y por eso resiste el paso de las sesiones. A los agentes de programación se les indica una vez en su archivo de instrucciones, y lo mantienen en todas. Conviene pedirlo por su nombre, por ejemplo «lleva un registro de decisiones con ADR», ya que la IA conoce el formato y lo aplica sin más explicaciones. En la web de un chatbot, lo mínimo es pedir al terminar cada sesión que la IA anote las decisiones de ese día en un documento que se va guardando.

## Un ejemplo de la comunidad

La guía interactiva [«Elige tu IA»](https://explikarlos.github.io/elige-ia/), publicada como expliCarlos, lleva en su repositorio un [registro de decisiones](https://github.com/explikarlos/elige-ia/blob/main/docs/decisions/ADR-001-static-pages.md). El primero explica por qué la aplicación es estática y no tiene servidor. Entre las alternativas descartadas figura una base de datos, que habría permitido sincronizar las respuestas, pero que se descartó porque aumentaba los riesgos de privacidad, el coste y el mantenimiento. Cualquier persona que retome ese proyecto sabe así que la ausencia de servidor responde a una decisión meditada.

Esta guía lleva también su propio [registro](https://github.com/Vibe-Coding-Educativo/vibe-responsable/tree/main/docs/adr), que recoge las decisiones sobre sus fuentes, su web y sus ejemplos.
