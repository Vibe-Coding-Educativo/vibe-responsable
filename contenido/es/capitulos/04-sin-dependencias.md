# No depender de servicios que pueden desaparecer

## Las dependencias de un material

Un material depende de un servicio externo cuando necesita algo que no está dentro de él para funcionar. Las formas más corrientes son el contenido incrustado desde otra web, las bibliotecas de programación y las tipografías que se cargan desde servidores ajenos, y las conexiones con servicios en línea. También es una dependencia la plataforma donde se ha creado el material, cuando este solo existe dentro de ella.

Estas dependencias no se ven al usar el material. Se descubren al leer el código o al pedir a la inteligencia artificial (IA) que las enumere, que es lo que pide el punto 4 de la [evaluación VCER](para-la-ia.html#para-evaluar-un-recurso-ya-hecho).

## Los cambios en los servicios externos

Un servicio externo puede cambiar sus condiciones, pasar a ser de pago o cerrar, y el material que dependía de él **deja de funcionar sin que su autor haya tocado nada**. El artículo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centro Nacional de Desarrollo Curricular en Sistemas no Propietarios (CEDEC) dedica a los recursos educativos abiertos (REA), lo ilustra con el caso de un recurso que incrusta un mapa interactivo de una plataforma externa. Si la plataforma retira las presentaciones gratuitas, el recurso muestra un recuadro en blanco, y el docente no puede recuperar el contenido porque no tiene el archivo original. El artículo recomienda reservar el contenido incrustado para los vídeos y casos similares.

El riesgo no es solo que el servicio desaparezca. En 2024, el dominio polyfill.io, desde el que más de cien mil sitios web cargaban una biblioteca muy utilizada, cambió de propietario y empezó a servir código malicioso sin que las páginas afectadas hubieran modificado nada, según documentó la empresa de seguridad [Sansec](https://sansec.io/research/polyfill-supply-chain-attack). El mismo artículo del CEDEC advierte de otro riesgo propio del código generado por IA, que son las bibliotecas inventadas o suplantadas por otras de nombre casi idéntico.

## El enlace de una plataforma

Cuando el material se ha creado en la web de un chatbot o en una plataforma para crear aplicaciones, el enlace compartido dura lo que la empresa decida. Un cambio en el servicio, en sus condiciones o en la cuenta del docente puede dejar ese enlace sin efecto, y con él todas las páginas que lo hayan incrustado.

**Lo mínimo es guardar en el propio ordenador una copia del código del material** y actualizarla cuando cambie. Con esa copia el material puede recuperarse, publicarse en otro sitio o seguir trabajándose con otra herramienta. Para que sirva, el material tiene que ser una página que se abra por sí sola en el navegador. Los chatbots más utilizados, como ChatGPT, Gemini o Claude, generan a menudo la aplicación como un componente de React, una biblioteca de programación muy extendida, que solo funciona dentro de su propia web. Por eso el [archivo de instrucciones para la IA](para-la-ia.html) les pide una página HTML.

## Lo que se carga de fuera

Programar desde cero lo que ya resuelve una biblioteca conocida no es realista, y tampoco lo es alojar dentro del material todo lo que utiliza. Las bibliotecas que muestran fórmulas, gráficos o mapas, y las tipografías, pueden cargarse desde fuera, siempre que procedan de un servicio conocido y quede constancia de ellas. Un servicio conocido tampoco garantiza que vaya a mantenerse igual, y por eso conviene comprobar qué deja de funcionar al abrir el material sin conexión.

Lo recomendado es pedir a la IA que cargue estos recursos de servicios conocidos y que los anote en la nota de decisiones de la recomendación 7, con su licencia. Esa lista no está pensada para el docente, sino para quien tenga que arreglar o adaptar el material más adelante, que muchas veces será de nuevo una IA. Lo que no puede recuperarse de otro sitio, como las imágenes, los textos y los datos propios, conviene que esté dentro del material, o al menos guardado en una copia, y no solo incrustado desde otra plataforma.

Al docente le interesa sobre todo una consecuencia práctica: **si el material seguirá funcionando al abrirlo descargado en un ordenador sin internet**, por ejemplo en un aula sin conexión. La comprobación no requiere conocimientos técnicos, ya que consiste en abrir el material, desconectar el dispositivo de la red y volver a cargarlo. Un ejemplo es [Tantrix](https://felipsarroca.github.io/jocs/Tantrix/), un juego de Felip Sarroca que puede instalarse como aplicación y funciona sin conexión después de la primera visita. La evaluación VCER pide a la IA que lo explique con palabras sencillas, del tipo «si lo abres sin internet, las fórmulas no se verán».
