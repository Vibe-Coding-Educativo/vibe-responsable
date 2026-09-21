---
titulo: OpenWorksheets: una alternativa libre para crear fichas interactivas
autor: Juan José de Haro
blog: educacion.bilateria.org
fecha: 2026-06-21
url: https://educacion.bilateria.org/openworksheets-una-alternativa-libre-para-crear-fichas-interactivas
descargado: 2026-09-21
licencia: CC BY-SA 4.0
---

**[OpenWorksheets](https://openworksheets.github.io/)** (OWS) es una aplicación web libre para crear fichas interactivas y autocorregibles a partir de un PDF, una imagen o una hoja en blanco.

<figure class="wp-block-image size-large">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1-1024x621.png" class="wp-image-3775" loading="lazy" decoding="async" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1-1024x621.png 1024w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1-300x182.png 300w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1-768x466.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1-676x410.png 676w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-1.png 1106w" sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024" height="621" />
<figcaption>Pantalla inicial de OpenWorksheets</figcaption>
</figure>

El profesorado prepara su ficha, coloca encima los campos de respuesta y define las soluciones. Después, el alumnado la resuelve desde el navegador y el docente puede revisar las entregas, ver la puntuación y exportar los resultados.

OWS tiene como bandera la libertad, privacidad, portabilidad y reutilización sin depender de una plataforma cerrada. No necesita cuentas de usuario ni servidores externos, ya que todo funciona en el navegador del profesorado y en el del alumnado. La comunicación entre ambos se realiza mediante archivos de entrega cifrados, que tienen extensión .owsub (OpenWorksheets submissions) o a través de una URL (también cifrada) que se envía directamente al docente.

<figure class="wp-block-image size-large wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec3e78dd6">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2-1024x572.png" class="wp-image-3776" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2-1024x572.png 1024w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2-300x167.png 300w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2-768x429.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2-676x377.png 676w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-2.png 1331w" sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024" height="572" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
<figcaption>Pantalla inicial del editor con las diferentes formas de crear una ficha.</figcaption>
</figure>

Las formas que tenemos para crear una ficha (proyecto) son:

- Añadir PDF o imagen, esta es la forma habitual. Podemos abrir un PDF o una imagen para dibujar encima los campos autocorregibles de forma que podemos aprovechar documentos ya existentes.
- Abrir una ficha ya creada con extensión .owpkg (OpenWorksheets package). Podremos continuar trabajando en un proyecto guardado anteriormente.
- Comenzar con una hoja en blanco sobre la cual podremos crear nuestra ficha.
- Crear con IA (prompt) permite producir una ficha a partir de una página en blanco con los parámetros que definamos (nivel, tema, tipos de campos deseados, etc.). Se utilizan los tipos de campo que pueden generarse automáticamente; quedan fuera los que dependen directamente de recortes o zonas del PDF. OWS generará un prompt que podremos pegar en nuestra IA de cabecera. No hay que instalar nada.
- Crear o convertir fichas con IA (MCP). Es el camino más potente y el único que puede partir de un documento propio: instalando el servidor MCP de OpenWorksheets, la IA abre nuestro PDF o nuestra imagen, coloca los campos encima, cada uno en su sitio, y nos enseña el resultado antes de guardarlo. También puede inventar la ficha entera desde cero sobre hojas en blanco. El archivo no se sube a ningún servicio, lo abre nuestro propio ordenador, aunque la IA sí ve el contenido de las páginas para poder trabajar. Requiere instalar un programa una sola vez, y se explica en [un artículo aparte](https://educacion.bilateria.org/convertir-una-imagen-o-pdf-en-una-ficha-interactiva-hablando-con-la-ia).

<figure class="wp-block-image size-large wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec3e7b02a">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-1024x473.png" class="wp-image-3777" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-1024x473.png 1024w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-300x139.png 300w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-768x355.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-1536x710.png 1536w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3-676x312.png 676w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-3.png 1906w" sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024" height="473" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
<figcaption>Un proyecto abierto (ficha). En la parte izquierda accedemos a los botones para crear campos, las miniaturas y a la derecha la lista de todos los campos y sus propiedades cuando se selecciona uno.</figcaption>
</figure>

Además, las fichas pueden **guardarse** como archivo propio (.owpkg), exportarse como página web autónoma y **compartirse** mediante enlace (previa subida a la nube obteniendo un enlace público), como web incrustada en otra o integrarse en Moodle y otros LMS mediante SCORM 1.2.

La aplicación admite muchos tipos de respuesta: texto corto, respuesta numérica, fórmulas matemáticas o químicas, verdadero/falso, opción única o múltiple, desplegables, huecos, tablas editables, emparejamientos, ordenar elementos, arrastrar a zonas, unir con flechas, respuesta larga y grabación de voz. También permite insertar imágenes, audio, vídeo, contenido HTML, paquetes de eXeLearning, IMS CP y SCORM.

Como profesor de matemáticas y ciencias, soy especialmente sensible a la posibilidad de crear fórmulas. Cualquier texto de la ficha puede incluir fórmulas LaTeX. Además, el editor de fórmulas de elaboración propia, [EdiCuaTeX](https://edicuatex.github.io/), se integra de forma natural para permitir la edición visual sin conocimientos de LaTeX, tanto en la parte del profesorado como en la del alumnado. No obstante, soy consciente de que una gran parte del profesorado no usará nunca fórmulas en sus fichas, por ese motivo se pueden desactivar en la configuración de la ficha.

OpenWorksheets también incorpora opciones de seguridad y privacidad: cifrado de la ficha, cifrado de entregas, verificación de integridad, restricciones de acceso, tiempo límite y supervisión ligera durante la realización. Un semáforo de seguridad indica su nivel en la barra superior.

## Flujo de trabajo 

El flujo de trabajo más habitual es compartir la ficha mediante un enlace o código QR:

1.  El profesor crea la actividad en el editor a partir de un PDF, una imagen, IA o una hoja en blanco.
2.  Añade los campos de respuesta y configura las soluciones, la puntuación y las opciones de corrección.
3.  Exporta la ficha como paquete `.owpkg`.
4.  Sube ese paquete a Google Drive o a otro alojamiento público.
5.  En Google Drive, activa la opción **Cualquier persona con el enlace** y copia la URL pública del archivo.
6.  Pega esa URL en OpenWorksheets para generar el enlace final del alumnado.
7.  Comparte ese enlace con los estudiantes.
8.  El alumnado abre la ficha en el navegador, la completa y entrega sus respuestas mediante archivo o enlace de entrega.
9.  El docente abre las entregas en OpenWorksheets, comprueba su integridad, revisa las respuestas, ajusta las correcciones manuales si las hay y exporta los resultados a CSV.

Además de este flujo principal, OpenWorksheets permite otras formas de uso:

- Exportar la ficha como página web autónoma, para publicarla a través de una página web.
- Integrarla en Moodle u otro LMS mediante SCORM 1.2.
- Exportarla como IMS Content Package.
- Embeberla en otra página mediante un `iframe`.

<figure class="aligncenter size-full">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-6.png" class="wp-image-3780" loading="lazy" decoding="async" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-6.png 546w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-6-229x300.png 229w" sizes="auto, (max-width: 546px) 100vw, 546px" width="546" height="714" />
<figcaption>Cuadro de diálogo para compartir una ficha. Antes se tiene que subir la ficha a un servicio público de almacenamiento como Google Drive.</figcaption>
</figure>

<figure class="aligncenter size-large wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec3e7e652">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7-1024x771.png" class="wp-image-3781" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7-1024x771.png 1024w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7-300x226.png 300w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7-768x578.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7-676x509.png 676w, https://educacion.bilateria.org/wp-content/uploads/2026/06/imagen-7.png 1119w" sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024" height="771" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
<figcaption>Una ficha tal como la ve el alumnado. En la esquina inferior derecha tiene la opción de finalizarla.</figcaption>
</figure>

OpenWorksheets permite crear, compartir y corregir fichas interactivas con un enfoque abierto, portable y respetuoso con la privacidad. La intención es que el profesorado pueda conservar el control sobre sus materiales y utilizarlos en distintos contextos, sin depender de una plataforma cerrada.

Puedes ver una descripción de las posibilidades más completa en la página de las [características](https://openworksheets.github.io/caracteristicas.html) del programa.

<figure class="wp-block-gallery has-nested-images columns-default is-cropped wp-block-gallery-1 is-layout-flex wp-block-gallery-is-layout-flex" data-wp-context="" data-wp-interactive="core/gallery">
<figure class="wp-block-image size-large wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec3e8057e">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2-1024x768.png" class="wp-image-3795" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" data-id="3795" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2-1024x768.png 1024w, https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2-300x225.png 300w, https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2-768x576.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2-676x507.png 676w, https://educacion.bilateria.org/wp-content/uploads/2026/06/ows2.png 1448w" sizes="auto, (max-width: 1024px) 100vw, 1024px" width="1024" height="768" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
</figure>
</figure>

**Nota**: Este artículo tiene nivel 4 en el [marco MIAE](https://educacion.bilateria.org/marco-para-la-integracion-de-la-ia-generativa-en-las-tareas-educativas-v-2-revisada).

- [](https://twitter.com/share?url=https%3A%2F%2Feducacion.bilateria.org%2Fopenworksheets-una-alternativa-libre-para-crear-fichas-interactivas&text=OpenWorksheets%3A%20una%20alternativa%20libre%20para%20crear%20fichas%20interactivas "Compartir en X")
- [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Feducacion.bilateria.org%2Fopenworksheets-una-alternativa-libre-para-crear-fichas-interactivas "Compartir en LinkedIn")
- [](https://telegram.me/share/url?url=https%3A%2F%2Feducacion.bilateria.org%2Fopenworksheets-una-alternativa-libre-para-crear-fichas-interactivas&text=OpenWorksheets%3A%20una%20alternativa%20libre%20para%20crear%20fichas%20interactivas "Compartir en Telegram")
- [](https://api.whatsapp.com/send?text=https%3A%2F%2Feducacion.bilateria.org%2Fopenworksheets-una-alternativa-libre-para-crear-fichas-interactivas%20OpenWorksheets%3A%20una%20alternativa%20libre%20para%20crear%20fichas%20interactivas "Compartir en Whatsapp")
