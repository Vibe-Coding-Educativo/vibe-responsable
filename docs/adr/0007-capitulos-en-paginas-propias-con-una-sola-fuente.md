# 7. Cada capítulo tiene su página, y lo que hay que hacer sale de una sola fuente

Fecha: 2026-09-21 · Estado: aceptado

## Contexto

La guía tiene una lista de diez recomendaciones, que cabe en una pantalla, y un
capítulo que desarrolla cada una. Los capítulos explican el porqué y son largos:
el de los datos personales pasa de dos mil palabras. El autor advirtió de que
quien los lee puede acabar sin saber qué tiene que hacer, porque esa respuesta
(«Lo mínimo» y «Lo recomendado») estaba solo en la página de la lista. También
encontró un enlace interno roto: los capítulos enlazaban `../creditos.html` como
si estuvieran en una subcarpeta, y eran diez enlaces en ocho capítulos.

## Decisión

Cada capítulo es un archivo de `contenido/<idioma>/capitulos/` y se publica en
su propia página, `capitulo-N.html`, al mismo nivel que las demás. No aparecen
en el menú: se llega a cada uno desde su recomendación en la guía, y entre ellos
con «Anterior» y «Siguiente». Un capítulo puede extenderse hacia abajo cuanto
haga falta; la regla de caber en una pantalla vale para la presentación y para
la guía, no para los textos explicativos.

Cada capítulo empieza con un recuadro, «Qué hay que hacer», que repite «Lo
mínimo» y «Lo recomendado» de su recomendación. El recuadro no tiene texto
propio: el generador lo toma de `01-guia.md`, de modo que esas indicaciones
tienen una sola fuente y un cambio llega a la vez a la guía y al capítulo. El
capítulo puede llevar, antes de su primer apartado, un texto previo; el de los
datos personales lo usa para una tabla de casos que enlaza con cada apartado.

El generador comprueba en cada ejecución todos los enlaces internos de las
páginas, archivo y ancla, y se detiene si alguno no existe.

## Alternativas descartadas

- **Repetir las indicaciones a mano en cada capítulo**: habría dos versiones del
  mismo texto, que acabarían por contradecirse.
- **El recuadro al final del capítulo**: sirve de cierre, pero no orienta durante
  la lectura, que es donde el lector se pierde.
- **Un «en la práctica» al final de cada apartado**: añade texto a capítulos que
  ya dicen muchas cosas.
- **Repartir un capítulo largo en varias páginas**: se llegó a montar y se
  deshizo, porque el autor se refería a varias pantallas, no a varias páginas.
- **Los capítulos en una subcarpeta**: habría hecho correctos los enlaces `../`,
  pero complica las rutas de los estilos y del menú sin ninguna ventaja.

## Consecuencias

Cambiar lo que hay que hacer en una recomendación se hace solo en `01-guia.md`.
Los títulos de los apartados de un capítulo son también sus anclas, así que
cambiar un título puede romper un enlace, y la comprobación del generador lo
avisa. Los enlaces a otras webs no se comprueban al generar y hay que
repasarlos en cada revisión de la guía.
