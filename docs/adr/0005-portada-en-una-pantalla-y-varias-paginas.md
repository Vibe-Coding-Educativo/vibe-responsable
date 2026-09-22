# 5. La presentación y la guía caben en una pantalla, y el contenido se reparte en varias páginas

Fecha: 2026-09-21 · Estado: aceptado · Revisado el mismo día para que describa la web tal como quedó

## Contexto

La primera versión de la web ponía en una sola página la presentación, las
familias de herramientas y las diez recomendaciones desplegadas: más de ocho
mil píxeles de alto. Un segundo intento, con dos columnas y las recomendaciones
en acordeones, seguía siendo una página larga con parches. El autor la rechazó:
la lista debe verse sin ese desplazamiento, la infografía y la lista de diez
tienen que estar a la vista al entrar, y la ampliación de la imagen no puede
abrirse de golpe ni a un tamaño que no cabe en la pantalla.

## Decisión

El contenido se reparte en páginas, en el orden en que se lee, que es también el
de los archivos de `contenido/<idioma>/` y el del menú:

1. **Presentación** (`00-presentacion.md`, portada): qué es el vibe coding
   educativo, por qué existe la guía, cómo se utiliza y cómo se ha elaborado. El
   texto va en dos columnas y, al lado, la infografía en una columna propia, con
   un enlace para descargarla debajo. Su alto es el que deja la pantalla, y de
   él sale la anchura de su columna, así que en un monitor grande se lee sin
   ampliarla y en un portátil queda como miniatura. En pantallas de 700 píxeles
   de alto o menos, el texto no cabe en dos columnas, y «Cómo se utiliza», con
   el enlace que lleva a la guía, pasa bajo la infografía; en las demás va bajo
   el texto.
2. **Guía** (`01-guia.md`, `guia.html`): las diez recomendaciones.
3. **Herramientas y niveles** (`02-herramientas.md`).
4. **Instrucciones para la IA** (`04-para-la-ia.md`): los textos para copiar.

Fuera del menú quedan **Créditos y licencias** (`03-creditos.md`), enlazada
desde el pie, y los diez capítulos, que regula el
[ADR 7](0007-capitulos-en-paginas-propias-con-una-sola-fuente.md). El pie ocupa
una línea, con la autoría, las dos licencias y el enlace a los créditos.

La presentación y la guía caben en una pantalla, también en un portátil de
1366 × 650 píxeles útiles; en pantallas bajas se compactan solas. Las demás
páginas son texto explicativo y pueden extenderse hacia abajo.

La página de la guía es una lista con su explicación. A la izquierda están las
diez recomendaciones como una sola hoja pautada. A la derecha, un panel muestra
la recomendación elegida en dos columnas (el porqué y los dos niveles), con el
enlace a su capítulo y botones para pasar a la anterior o a la siguiente. En
escritorio el panel muestra siempre una recomendación, la primera al cargar. En
el móvil empiezan todas plegadas y la explicación se despliega bajo su fila. Sin
JavaScript, todo el contenido queda visible, una recomendación tras otra. La
página no tiene casillas ni recuento. Lo único que la web guarda en el navegador
es el tema claro u oscuro, y solo cuando se elige uno distinto al del
dispositivo con el botón de la cabecera; junto a él hay otro para imprimir la
página, que en papel sale sin navegación y con el aviso de borrador mientras lo
sea.

La infografía está solo en la presentación. La propia imagen es el único
control para ampliarla: abre un visor que la ajusta siempre a la pantalla, con
una entrada y una salida suaves, un botón para verla a tamaño de lectura y otro
para descargarla; bajo la imagen hay además un enlace de descarga, para quien no
quiera abrir el visor. Sus medidas salen del SVG original, no de un número
escrito a mano. El movimiento responde solo a acciones de la persona y se anula si el
dispositivo pide reducirlo.

El aspecto sale del aula: cabecera en verde pizarra, papel neutro y dos tintas,
verde para «Lo mínimo» y azul para «Lo recomendado». La tipografía es Atkinson
Hyperlegible, diseñada por el Braille Institute para la legibilidad, alojada en
el propio repositorio con su licencia OFL. La infografía usa la misma paleta y
la misma tipografía. El logotipo son unos corchetes de código con una marca de
verificación dentro, sobre el verde pizarra: toma los corchetes del logotipo de
la comunidad Vibe Coding Educativo y el amarillo de su fondo, para que se
reconozca como parte de ella, y sus trazos son los de dos iconos de Lucide. Las
páginas de texto llevan los títulos de apartado al margen. El cuerpo va en dos
columnas cuando el apartado tiene tres párrafos o más, salvo en los capítulos,
que van siempre a una columna. Los enlaces a otras webs
se abren en una pestaña nueva, sin texto de aviso añadido.

## Alternativas descartadas

- **Una sola página con acordeones y dos columnas**: reducía el alto a menos de
  la mitad, pero seguía siendo una página larga y el autor la rechazó.
- **La lista como portada**: fue la primera forma de esta decisión. El autor la
  encontró incoherente, porque antes de las recomendaciones hay que decir qué es
  el vibe coding educativo y por qué existe la guía.
- **Una hoja de revisión con casillas**: la página de la guía llevaba una
  casilla «Se cumple» por recomendación, un recuento y botones para copiar el
  resultado y borrar las marcas, guardadas en el navegador. El autor la vio
  publicada y mandó quitarlo: la página queda como lista y explicación, sin
  controles añadidos.
- **La infografía repetida en el panel de la guía**, y un botón «Ampliar» junto
  a la miniatura: eran redundantes con la presentación y con la propia
  miniatura.
- **Los créditos de iconos y tipografía en el pie**: lo recargaban; van a su
  página.
- **Pestañas dentro de una página**: ocultan contenido sin que se note, y no dan
  una dirección propia a cada parte.
- **Paleta crema con acento tostado y tarjetas redondeadas**: era la del primer
  diseño y es el aspecto por defecto de una página generada; no decía nada del
  tema.
- **Tipografía del sistema**: no depende de archivos, pero no aporta identidad y
  cambia de un dispositivo a otro. La elegida pesa 53 KB en total.

## Consecuencias

La página de la guía depende de JavaScript para el panel, aunque se degrada bien
sin él. La tipografía añade tres archivos y una licencia que acreditar. Un
cambio de texto en la presentación o en la guía puede hacer que dejen de caber
en una pantalla, así que hay que volver a medirlo después de cada cambio. Al
probar se encontraron dos fallos que solo aparecían en un navegador: en Safari,
una columna `auto` con una imagen dentro daba al panel 4.500 píxeles de alto, y
en el móvil el rótulo del aviso de borrador se salía de la pantalla. Cualquier
cambio en estas dos páginas debe volver a comprobarse en Chromium, Firefox y
WebKit, y en la pantalla de un portátil pequeño.
