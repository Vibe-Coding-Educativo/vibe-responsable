# No depende de servicios que pueden desaparecer

## Las dependencias de un material

Un material depende de un servicio externo cuando necesita algo que no está dentro de él para funcionar. Las formas más corrientes son el contenido incrustado desde otra web, las bibliotecas de programación y las tipografías que se cargan desde servidores ajenos, y las conexiones con servicios en línea. También es una dependencia la plataforma donde se ha creado el material, cuando este solo existe dentro de ella.

Estas dependencias no se ven al usar el material. Se descubren al leer el código o al pedir a la inteligencia artificial (IA) que las enumere, que es lo que hace el punto 6 del texto de revisión de las [instrucciones para la IA](para-la-ia.html).

## Los cambios en los servicios externos

Un servicio externo puede cambiar sus condiciones, pasar a ser de pago o cerrar, y el material que dependía de él deja de funcionar sin que su autor haya tocado nada. El artículo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centro Nacional de Desarrollo Curricular en Sistemas no Propietarios (CEDEC) dedica a los recursos educativos abiertos (REA), lo ilustra con el caso de un recurso que incrusta un mapa interactivo de una plataforma externa. Si la plataforma retira las presentaciones gratuitas, el recurso muestra un recuadro en blanco, y el docente no puede recuperar el contenido porque no tiene el archivo original. El artículo recomienda reservar el contenido incrustado para los vídeos y casos similares.

El riesgo no es solo que el servicio desaparezca. En 2024, el dominio polyfill.io, desde el que más de cien mil sitios web cargaban una biblioteca muy utilizada, cambió de propietario y empezó a servir código malicioso sin que las páginas afectadas hubieran modificado nada, según documentó la empresa de seguridad [Sansec](https://sansec.io/research/polyfill-supply-chain-attack). El mismo artículo del CEDEC advierte de otro riesgo propio del código generado por IA, que son las bibliotecas inventadas o suplantadas por otras de nombre casi idéntico.

## El enlace de una plataforma

Cuando el material se ha creado en la web de un chatbot o en una plataforma para crear aplicaciones, el enlace compartido dura lo que la empresa decida. Un cambio en el servicio, en sus condiciones o en la cuenta del docente puede dejar ese enlace sin efecto, y con él todas las páginas que lo hayan incrustado.

Lo mínimo es guardar en el propio ordenador una copia del código del material y actualizarla cuando cambie. Con esa copia el material puede recuperarse, publicarse en otro sitio o seguir trabajándose con otra herramienta.

## Materiales que lo incluyen todo

Lo recomendado es que el proyecto contenga todo lo que necesita para funcionar: las bibliotecas, las tipografías, las imágenes y los datos. Un material así puede copiarse a una memoria, subirse a la plataforma del centro o abrirse sin conexión, y no deja de funcionar por un cambio ajeno. Conviene pedirlo a la IA desde el principio.

La comprobación es sencilla y no requiere conocimientos técnicos, ya que consiste en abrir el material, desconectar el dispositivo de la red y volver a cargarlo. Un ejemplo es [Tantrix](https://felipsarroca.github.io/jocs/Tantrix/), un juego de Felip Sarroca que puede instalarse como aplicación y funciona sin conexión después de la primera visita. Esta guía sigue el mismo criterio: no utiliza bibliotecas ni servicios externos, y la tipografía está alojada en su propio repositorio.
