# 13. Las vías para enviar sugerencias se reúnen en un panel del aviso de borrador

Fecha: 2026-09-24 · Estado: aceptado

## Contexto

La guía está en revisión y se quiere recoger la experiencia del profesorado que
crea aplicaciones: lo que falta, lo que sobra y lo que no se ajusta a cómo se
trabaja de verdad. Se presentó en el grupo de Telegram Vibe Coding Educativo, con
un tema abierto para comentarla, y en LinkedIn, X y Bluesky, invitando a comentar
allí. Esos anuncios se pierden con el tiempo y no alcanzan a las personas que
llegan a la web por otro camino, así que la web debe reunir todas las vías.

## Decisión

La etiqueta «Borrador» de la cabecera es un botón que despliega un panel breve:
explica que la guía está en revisión y enumera las vías para enviar sugerencias,
cada una con su enlace:

- las incidencias del repositorio en GitHub
  (<https://github.com/Vibe-Coding-Educativo/vibe-responsable/issues>). Se enlaza
  la lista y no el formulario de una incidencia nueva, para que se vea antes lo
  que ya se ha propuesto;
- el tema del grupo de Telegram abierto para comentar la guía;
- los comentarios de la publicación de presentación en LinkedIn, X y Bluesky.

El enlace «Sugerencias y correcciones» del pie de todas las páginas abre el mismo
panel sin mover la página. Sin JavaScript, la etiqueta es solo un aviso y el
enlace del pie lleva a las incidencias de GitHub. El panel se cierra al pulsar
fuera o con Escape, y no se imprime. El PDF no lleva ninguna de las vías, porque
su pie solo identifica la guía y su licencia.

## Alternativas descartadas

- **Una ventana al entrar.** Estorba justo a quien llega desde uno de esos
  anuncios y ya sabe dónde comentar, y para no repetirse en cada visita tendría
  que guardar en el navegador que ya se ha visto.
- **Enlazar solo las incidencias de GitHub**, como se hizo al principio. Exige
  una cuenta de GitHub y deja fuera las conversaciones que ya están ocurriendo en
  el grupo y en las redes.
- **Un formulario o un correo.** Añade un servicio externo o expone una dirección,
  y las aportaciones no quedan a la vista de los demás.

## Consecuencias

El panel depende del aviso de borrador: cuando la guía deje de serlo, hay que
decidir si las vías se mantienen en otro sitio o se quedan solo en el pie. Las
sugerencias llegan dispersas por cinco sitios y hay que recogerlas de todos. Los
enlaces a las publicaciones de las redes llevan a un anuncio concreto; si se
publica otro, hay que cambiarlos. Los textos y enlaces están en `UI` de
`construir.py` (`participar`).

Las propuestas que se incorporan se agradecen en «Créditos y licencias», con
enlace a su incidencia o al grupo donde se hicieron, y diciendo qué cambió en la
guía. Las primeras, de Ernesto Serrano (incidencias) y David Cordones (grupo de
Telegram), se incorporaron el 25-09-2026.
