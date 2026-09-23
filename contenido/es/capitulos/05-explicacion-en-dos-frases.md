# Entender qué hace el material

## La comprensión del código

Un recurso educativo es abierto cuando otra persona puede descargarlo, comprenderlo, modificarlo y mejorarlo. El artículo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centro Nacional de Desarrollo Curricular en Sistemas no Propietarios (CEDEC) dedica a los recursos educativos abiertos (REA), advierte de que un recurso con cientos de líneas de código que nadie entiende, ni siquiera la persona que las insertó, ha dejado de ser abierto en lo esencial, aunque su licencia diga lo contrario. La ponencia [«Crear REA con eXeLearning en tiempos de IA»](https://descargas.intef.es/cedec/formacion/SL_REA_IA_julio26/html/la-ia-y-el-codigo.html) lo expresa así: «Tenemos el código fuente. Pero no la comprensión».

El problema es práctico, ya que un material que funciona hoy puede dejar de hacerlo tras una actualización del navegador, y si nadie entiende cómo está hecho, tampoco podrá corregirse. El mismo artículo propone una regla sencilla: si no se puede explicar en dos frases qué hace el código, el recurso todavía no está listo para publicarse.

## La explicación en dos frases

Cumplir esta recomendación no exige saber programar, ya que es suficiente con poder decir con palabras corrientes tres cosas del material: qué hace, qué guarda y si se comunica con algún servicio externo. Una explicación de este tipo sería la siguiente: «El simulador calcula la aceleración de un cuerpo en un plano inclinado a partir del ángulo y del material elegidos, y dibuja las fuerzas. No guarda ningún dato ni se conecta con ningún servicio».

La forma de obtenerla es pedírsela a la propia IA, en lenguaje llano, y comprobar después que coincide con lo que se observa al usar el material. Si la inteligencia artificial (IA) afirma que no se guarda nada y el material recuerda las respuestas del día anterior, la explicación no es correcta y hay que aclararlo antes de publicar. El apartado de revisión del [archivo de instrucciones para la IA](para-la-ia.html) incluye esta petición en su punto 5.

## Cuatro comprobaciones sin saber programar

El artículo del CEDEC propone cuatro preguntas para detectar un código problemático sin necesidad de entenderlo línea a línea:

- **Si se puede leer.** Un código legítimo tiene palabras reconocibles, espacios y líneas de longitud razonable. Una línea de cientos de caracteres sin espacios, con letras y números mezclados, indica que el código está ofuscado.
- **Si hace referencia a direcciones externas.** Conviene buscar las direcciones web que aparecen en el código e investigar las que no se reconozcan.
- **Si pide permisos.** El acceso a la cámara, al micrófono, a la ubicación o al portapapeles solo es aceptable cuando el material lo justifica con una finalidad pedagógica clara.
- **Si su autor puede explicarlo.** Es la regla de las dos frases.

Las cuatro pueden encargarse a la IA, que puede localizar en el código las direcciones y los permisos. El mismo artículo resume estos criterios en un semáforo que clasifica el código en seguro, de riesgo moderado y peligroso.

## El código legible y comentado

El código generado por IA sin comentarios funciona como una caja negra. Cuando incluye comentarios en lenguaje natural, otras personas pueden comprenderlo, modificarlo y mantenerlo con mayor facilidad. Conviene pedirlo desde el principio, con los comentarios en el idioma del material y con nombres de variables comprensibles. Un ejemplo es el [simulador del plano inclinado con rozamiento](https://onio72.github.io/iesmajuelo/bach/fq1/planoincroz/), de Antonio González García, cuyo código está en un único archivo, dividido en secciones rotuladas y comentado en español.

El código comprimido en líneas interminables es motivo suficiente para no publicar, con la excepción de las bibliotecas conocidas, que suelen distribuirse así. Cuando el material es un proyecto con varios archivos, conviene añadir un documento que explique cómo está organizado y para qué sirve cada uno. Así lo hace Pablo G. Guízar en el [repositorio de su Quiz del Sistema Solar](https://github.com/PabloGGuizar/quiz), que describe la arquitectura del programa, el recorrido de los datos y la función de cada archivo.
