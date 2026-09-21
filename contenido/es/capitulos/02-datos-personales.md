# No envía datos personales a servicios ajenos al centro

Lo que hay que hacer depende del tipo de material. La tabla resume los cuatro casos que se explican en este capítulo, y cada uno enlaza con su apartado.

| Si el material… | Entonces… |
| --- | --- |
| está pensado para el alumnado o para publicarse en abierto | [no necesita datos](#materiales-que-no-necesitan-datos), y no debe pedirlos |
| es una herramienta del docente con su alumnado identificado | [los datos se quedan en su dispositivo](#herramientas-que-necesitan-identificar-al-alumnado), conforme a las normas del centro |
| recoge las respuestas del alumnado | [los resultados llegan al docente sin pasar por servicios ajenos al centro](#programas-que-recogen-las-respuestas-del-alumnado) |
| lo pone el centro a disposición del profesorado | [los datos van a los sistemas del centro](#programas-que-el-centro-pone-a-disposicion-del-profesorado), y la decisión es del centro |

## Los datos personales en un material educativo

Un dato personal es cualquier información que permite identificar a una persona. En un material educativo lo son el nombre, el correo electrónico, las notas, la voz o la imagen del alumnado, y también las respuestas de una actividad cuando se guardan asociadas a un nombre. Un cuestionario que pide el nombre y lo envía a un servidor junto con las respuestas está tratando datos personales.

La mayor parte del alumnado es menor de edad, y las normas de protección de datos son más exigentes en ese caso. En la Unión Europea, el [Reglamento General de Protección de Datos](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679) fija en 16 años la edad para consentir el tratamiento de los propios datos en los servicios en línea, y permite a cada país rebajarla hasta los 13. En España, la [Ley Orgánica 3/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673) la establece en 14 años. Por debajo de esa edad, el consentimiento corresponde a las familias.

Aunque el alumnado pueda dar su consentimiento a partir de esa edad, las buenas prácticas aconsejan que las familias reciban una información precisa sobre lo que hacen sus hijos y sobre las herramientas que utilizan. Conviene que esa información indique qué materiales se emplean, si recogen algún dato y con qué finalidad, de forma que la familia conozca el material antes de que se utilice en el aula.

## La decisión sobre los datos del alumnado

Publicar un material que envía datos del alumnado a un servidor no es una decisión que pueda tomar cada docente por su cuenta. En España, la [guía para centros educativos](https://www.aepd.es/documento/guia-centros-educativos.pdf) de la Agencia Española de Protección de Datos indica que las administraciones y los centros deben disponer de instrucciones para el uso de las tecnologías por el profesorado, que deberá utilizar las que la administración o el centro hayan dispuesto. La misma guía señala que, de lo que un profesor publica al margen de su función docente en el centro, el responsable es el propio profesor.

La consecuencia es que un material creado por iniciativa propia, que guarde datos del alumnado en un servicio ajeno al centro, convierte a su autor en responsable de ese tratamiento. Otros países tienen normas distintas, pero la precaución es la misma: antes de recoger datos del alumnado hay que contar con el centro.

## Materiales que no necesitan datos

La forma más sencilla de cumplir es que el material no recoja datos. El Reglamento europeo establece el principio de minimización, según el cual los datos deben limitarse a lo necesario para su finalidad, y obliga a aplicar la protección de datos desde el diseño. La [guía sobre la inteligencia artificial (IA) y la infancia](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children) del Fondo de las Naciones Unidas para la Infancia (UNICEF), de alcance mundial, recomienda lo mismo: reducir al mínimo la recogida de datos y adoptar un enfoque de privacidad desde el diseño.

En un material creado con vibe coding, esto se traduce en unas pocas decisiones que pueden pedirse a la IA desde el principio:

- **Sin identificación.** El material no pide el nombre. Si hace falta distinguir a varias personas, basta con un alias que no las identifique.
- **Todo en el navegador.** Las respuestas y el progreso se guardan en el propio dispositivo y no se envían a ningún servidor.
- **Sin cuentas de usuario.** El material se utiliza sin registrarse en ningún servicio.
- **Sin analítica.** El material no incluye contadores de visitas ni herramientas de seguimiento.

Un material construido así puede publicarse sin tratar ningún dato personal, de modo que las obligaciones anteriores no llegan a plantearse.

## Herramientas que necesitan identificar al alumnado

Algunos materiales necesitan identificar al alumnado para cumplir su función, como un cuaderno de calificaciones, un plano de clase o un generador de grupos. Estas herramientas pueden crearse y publicarse, ya que el seguimiento del alumnado forma parte de la función educativa. La condición es que los datos permanezcan bajo el control del docente y de su centro.

La guía de la Agencia Española de Protección de Datos admite que el profesorado utilice aplicaciones en sus dispositivos personales, siempre que respeten la política de privacidad definida por el centro o por la administración educativa. Considera de especial importancia que ese uso no implique una transmisión de los datos del alumnado al prestador del servicio, para que los utilice con sus propios fines o los almacene de forma permanente.

En una herramienta creada con vibe coding, esta condición se cumple cuando los datos se guardan únicamente en el dispositivo del docente, ya sea en el navegador o en un archivo que se descarga y se vuelve a cargar. La aplicación publicada no contiene ningún dato, porque cada docente introduce los suyos y no salen de su equipo, de modo que el autor de la herramienta no trata datos de nadie. Conviene, además, que la herramienta permita compartir o imprimir la información sin los nombres, y que cada docente la utilice conforme a las normas de su centro, igual que haría con un cuaderno en papel o con una hoja de cálculo.

Un ejemplo es el [Cuaderno del Profesorado](https://github.com/imanlost/CuadernoProfesorado-v1.0), de Imanol Lostalé, un cuaderno docente completo que funciona sin servidor: la base de datos se guarda en el navegador o en un archivo del disco del docente, con sus copias de seguridad.

## Programas que recogen las respuestas del alumnado

Otro caso es el programa que un docente crea para comprobar los conocimientos de su alumnado, detectar errores de concepto o seguir su progreso. La iniciativa es individual, pero los datos los genera el alumnado en sus propios dispositivos y tienen que llegar al docente. Evaluar forma parte de la función educativa, de modo que el programa es legítimo, y lo que hay que cuidar es el camino que siguen los resultados. Hay varias formas de resolverlo sin enviar datos a servicios ajenos al centro, que pueden combinarse:

- **El resultado se entrega por los medios del centro.** El programa muestra el resultado al terminar, o lo guarda en un archivo, y el alumnado lo entrega por la plataforma del centro, como cualquier otra tarea. Así lo hace [OpenWorksheets](https://openworksheets.github.io/), una aplicación libre de fichas interactivas sin servidor ni cuentas, en la que el alumnado descarga un archivo de entrega al terminar.
- **El alumnado se identifica con un código.** El programa no pide el nombre, sino un código que solo el docente sabe a qué persona corresponde. El Reglamento europeo llama a esta técnica seudonimización, y exige que esa correspondencia se guarde por separado. En la [Plantilla correctora digital (PCD)](https://jjdeharo.github.io/pcd/), para exámenes tipo test, el único campo de identificación admite un código en lugar del nombre.
- **Los resultados se recogen en una hoja de cálculo del centro.** Cuando hace falta una recogida automática, cada docente despliega su propia copia del programa en la cuenta que el centro le proporciona, y no en una cuenta personal, de modo que los resultados llegan a una hoja de cálculo que solo él controla. El autor del programa publica una plantilla y no recibe ningún dato. Conviene que el centro lo conozca. Un ejemplo es el [Quiz del Sistema Solar](https://pablogguizar.github.io/quiz/), de Pablo G. Guízar, pensado para que cada docente lo despliegue con su propia hoja de cálculo, que mantiene las respuestas correctas fuera del navegador. El mismo autor explica cómo hacerlo con garantías en su [guía de seguridad para aplicaciones con Google Sheets](https://pablogguizar.github.io/apps-with-google-sheets/).
- **La entrega viaja cifrada.** El programa cifra el resultado con una clave del docente, de forma que el alumnado puede cifrar pero no descifrar, y solo el docente lo lee con su contraseña. Aunque el archivo se envíe por un canal poco seguro, su contenido resulta ilegible. [OpenWorksheets](https://openworksheets.github.io/) ofrece este cifrado como opción, y avisa además si un archivo de entrega ha sido manipulado.
- **La nota la gestiona la plataforma del centro.** El programa se exporta en un formato estándar y se sube a la plataforma que el centro ya utiliza, que es la que registra los resultados. Uno de esos formatos es SCORM, siglas en inglés de *Sharable Content Object Reference Model* (modelo de referencia para objetos de contenido compartibles). Es lo que hace el [Generador SCORM de Certificado de Finalización](https://github.com/PabloGGuizar/generador-scorm-de-certificado-de-finalizacion), de Pablo G. Guízar, que obtiene el nombre del estudiante de la propia plataforma y registra en ella que el curso se ha completado.
- **Las respuestas viajan directamente entre los dispositivos.** En las actividades en directo, como un concurso en el aula, los dispositivos del alumnado pueden conectarse con el del docente sin que las respuestas se guarden en ningún servidor. Para establecer la conexión suele intervenir un servicio intermediario, que ve identificadores técnicos pero no el contenido. Así funciona el [Buzzer WebRTC](https://pablogguizar.github.io/buzzer-webrtc/), de Pablo G. Guízar, un pulsador para actividades de respuesta rápida. WebRTC, siglas en inglés de *Web Real-Time Communication* (comunicación web en tiempo real), es la tecnología de los navegadores que permite esa conexión directa.

Estos programas son deterministas, es decir, aplican siempre las mismas reglas a las respuestas, y el análisis se hace en el propio dispositivo. La situación cambia si el programa envía las respuestas a un servicio de IA para que las valore. En ese caso los datos llegan a un tercero y, además, el [Reglamento europeo de IA](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/spa) clasifica como de alto riesgo los sistemas de IA destinados a evaluar los resultados del aprendizaje, lo que conlleva obligaciones importantes para su proveedor y para el centro que lo utiliza.

## Programas que el centro pone a disposición del profesorado

Un centro o una administración educativa puede decidir que un programa gestione datos del alumnado en sus propios sistemas, por ejemplo unas hojas de cálculo compartidas con las calificaciones. En ese caso los datos salen del navegador, y es legítimo, porque la decisión la toma el responsable de esos datos. La guía de la Agencia Española de Protección de Datos indica que los centros deben conocer las aplicaciones que vayan a utilizar, su política de privacidad y sus condiciones de uso antes de utilizarlas. Cuando interviene un proveedor externo, actúa como encargado del tratamiento y solo puede tratar los datos conforme a las instrucciones del centro.

Un programa creado con vibe coding puede cumplir esta función con tres cautelas. La primera es que los datos se guarden en la plataforma que el centro ya utiliza, sin añadir servicios nuevos. La segunda es que la decisión pase por el equipo directivo y por el delegado de protección de datos, y no por un docente a título individual. La tercera es la seguridad: el código de estos programas lo ha escrito la IA y lo habitual es que nadie lo haya revisado, de modo que un programa que maneja datos reales merece la revisión de una persona con conocimientos técnicos antes de ponerse en uso.

Cuando el programa se publica como plantilla para que otros centros lo utilicen, conviene acompañarlo de un aviso que indique a quién corresponde la responsabilidad sobre los datos. Un modelo es el de [IAGuar](https://elprofedelabata.es/iaguar/), una aplicación de gestión de guardias, cuyo autor indica que no tiene acceso a los datos de las copias desplegadas por terceros y que el responsable del tratamiento es el centro que pone en marcha su propia copia.

## Los envíos de datos a otros servidores

Otro riesgo está en el código que envía información sin que su autor lo sepa. El artículo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centro Nacional de Desarrollo Curricular en Sistemas no Propietarios (CEDEC) dedica a los recursos educativos abiertos (REA), describe un caso ilustrativo: un cuestionario de matemáticas que, al completarse, enviaba las respuestas a un dominio externo. El docente pensaba que era un contador de uso, y en realidad ese dominio recopilaba datos de menores sin el consentimiento que exige el Reglamento. El mismo artículo advierte de los materiales que piden permiso para usar la cámara, el micrófono o la ubicación sin una finalidad pedagógica clara.

Las plataformas para crear aplicaciones merecen una atención especial, ya que añaden con facilidad cuentas de usuario y bases de datos, y entonces los datos se guardan en los servidores de una empresa. Lo mismo ocurre cuando el material se abre dentro de la web de un chatbot: el alumnado entra en el servicio de un tercero, que puede exigir registro o una edad mínima.

Para comprobar un material no hace falta leer el código, ya que es suficiente con pedir a la IA que enumere todas las direcciones externas que aparecen en él y que explique para qué sirve cada una, como hace el texto de revisión de las [instrucciones para la IA](para-la-ia.html). Una dirección que no se reconozca es motivo suficiente para no publicar hasta aclararla.
