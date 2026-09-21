# No recoge datos personales, o los datos no salen del dispositivo

## Los datos personales en un material educativo

Un dato personal es cualquier información que permite identificar a una persona. En un material educativo lo son el nombre, el correo electrónico, las notas, la voz o la imagen del alumnado, y también las respuestas de una actividad cuando se guardan asociadas a un nombre. Un cuestionario que pide el nombre y lo envía a un servidor junto con las respuestas está tratando datos personales.

La mayor parte del alumnado es menor de edad, y las normas de protección de datos son más exigentes en ese caso. En la Unión Europea, el [Reglamento General de Protección de Datos](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679) fija en 16 años la edad para consentir el tratamiento de los propios datos en los servicios en línea, y permite a cada país rebajarla hasta los 13. En España, la [Ley Orgánica 3/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673) la establece en 14 años. Por debajo de esa edad, el consentimiento corresponde a las familias.

## La decisión sobre los datos del alumnado

Publicar un material que recoge datos del alumnado no es una decisión que pueda tomar cada docente por su cuenta. En España, la [guía para centros educativos](https://www.aepd.es/documento/guia-centros-educativos.pdf) de la Agencia Española de Protección de Datos indica que las administraciones y los centros deben disponer de instrucciones para el uso de las tecnologías por el profesorado, que deberá utilizar las que la administración o el centro hayan dispuesto. La misma guía señala que, de lo que un profesor publica al margen de su función docente en el centro, el responsable es el propio profesor.

La consecuencia es que un material creado por iniciativa propia, que guarde datos del alumnado en un servicio ajeno al centro, convierte a su autor en responsable de ese tratamiento. Otros países tienen normas distintas, pero la precaución es la misma: antes de recoger datos del alumnado hay que contar con el centro.

## Materiales que no necesitan datos

La forma más sencilla de cumplir es que el material no recoja datos. El Reglamento europeo establece el principio de minimización, según el cual los datos deben limitarse a lo necesario para su finalidad, y obliga a aplicar la protección de datos desde el diseño. La [guía de UNICEF sobre la IA y la infancia](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children), de alcance mundial y publicada en inglés, recomienda lo mismo: reducir al mínimo la recogida de datos y adoptar un enfoque de privacidad desde el diseño.

En un material creado con vibe coding, esto se traduce en unas pocas decisiones que pueden pedirse a la IA desde el principio:

- **Sin identificación.** El material no pide el nombre. Si hace falta distinguir a varias personas, basta con un alias que no las identifique.
- **Todo en el navegador.** Las respuestas y el progreso se guardan en el propio dispositivo y no se envían a ningún servidor.
- **Sin cuentas de usuario.** El material se utiliza sin registrarse en ningún servicio.
- **Sin analítica.** El material no incluye contadores de visitas ni herramientas de seguimiento.

Un material construido así puede publicarse sin tratar ningún dato personal, de modo que las obligaciones anteriores no llegan a plantearse.

## Los envíos de datos a otros servidores

Otro riesgo está en el código que envía información sin que su autor lo sepa. El artículo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), del CEDEC, describe un caso ilustrativo: un cuestionario de matemáticas que, al completarse, enviaba las respuestas a un dominio externo. El docente pensaba que era un contador de uso, y en realidad ese dominio recopilaba datos de menores sin el consentimiento que exige el Reglamento. El mismo artículo advierte de los materiales que piden permiso para usar la cámara, el micrófono o la ubicación sin una finalidad pedagógica clara.

Las plataformas para crear aplicaciones merecen una atención especial, ya que añaden con facilidad cuentas de usuario y bases de datos, y entonces los datos se guardan en los servidores de una empresa. Lo mismo ocurre cuando el material se abre dentro de la web de un chatbot: el alumnado entra en el servicio de un tercero, que puede exigir registro o una edad mínima.

Para comprobar un material no hace falta leer el código, ya que es suficiente con pedir a la IA que enumere todas las direcciones externas que aparecen en él y que explique para qué sirve cada una, como hace el texto de revisión de las [instrucciones para la IA](../para-la-ia.html). Una dirección que no se reconozca es motivo suficiente para no publicar hasta aclararla.
