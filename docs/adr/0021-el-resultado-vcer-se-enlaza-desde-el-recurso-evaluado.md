# 21. El resultado VCER se enlaza desde el recurso evaluado a una página que lo explica

Fecha: 2026-10-02 · Estado: aceptado

## Contexto

La evaluación VCER (ADR 10) termina en un informe con un resultado y un
porcentaje, pero ese informe se quedaba en la conversación con la IA. Juanjo
pidió que la persona que evalúa su propio recurso pudiera indicar en él que ha
pasado la evaluación, con el porcentaje o sin él, y enlazar a una página nueva
de la guía que explique el resultado a las personas que no conocen la evaluación y sirva
de entrada al resto de la guía. Pidió expresamente que no fuera una ventana
emergente como la del enlace `?nivel=` del MIAE, sino algo más natural e igual
de informativo.

El resultado lo declara la persona que publica el recurso y nadie lo comprueba: el
enlace puede escribirse a mano y la misma web puede puntuar distinto con otro
modelo. Además, el recurso cambia después de evaluarse.

## Decisión

- **Página nueva, `vcer.html`** («La evaluación VCER», en el menú tras las
  instrucciones para la IA), generada de `contenido/<idioma>/06-evaluacion-vcer.md`:
  qué es la evaluación, los diez puntos con el capítulo de su recomendación,
  cómo se calcula el resultado, con la tabla de los tres resultados, y los
  límites de la evaluación. Termina con dos salidas: evaluar un recurso y leer
  la guía. La tabla de resultados pasa de «Instrucciones para la IA» a esta
  página, que es su único sitio; aquella remite aquí.
- **El resultado viaja en el enlace**, sin servidor ni registro:
  `vcer/?r=…&p=…&f=…&v=…&t=…&u=…`. `r` es el resultado (`recomendable`,
  `mejorable` o `no-recomendable`, igual en todos los idiomas) y es
  obligatorio; `p`, el porcentaje, opcional, porque un porcentaje sin su
  resultado engaña (un 85 % con un 0 en contenido es «No recomendable»); `f`,
  el año y el mes; `v`, la versión evaluada, si el recurso la tiene; `t`, el
  título, y `u`, la dirección, si está publicado en la web. La versión se
  añadió a petición de Juanjo: la mención sigue en el pie cuando sale una
  versión nueva sin evaluar, y con las dos cifras a la vista el lector sabe a
  qué atenerse.
- **`vcer/index.html` no lleva idioma**, porque el recurso evaluado puede estar
  en cualquiera: envía a la página del idioma del navegador con los datos
  intactos, como hace el MIAE con `?nivel=`.
- **Si el enlace trae un resultado válido, la página abre con un recuadro**, sin
  ventana: la frase con el recurso, la versión, la dirección y la fecha; el
  resultado con su porcentaje y una barra que marca el 70 %; su significado,
  tomado de la tabla, cuya fila queda resaltada; y el aviso de que es una
  autoevaluación orientativa que no ha comprobado nadie más. Los datos se
  escriben como texto; los que no son válidos se omiten, y sin un `r` válido la
  página se ve sin recuadro. La dirección del recurso se muestra sin enlace,
  para que la guía no sirva de trampolín a un sitio cualquiera con el rótulo
  «Recomendable».
- **El archivo de evaluación pide a la IA ofrecer la mención** («Evaluación VCER
  de la versión 1.2: Recomendable (85 %), octubre de 2026», en el idioma del
  material) y, si el proyecto tiene carpeta propia, guardar el informe en
  `evaluacion-vcer.md`, pero solo si el recurso es de la persona y la IA puede
  modificar sus archivos. Si el recurso es ajeno o la IA no puede tocarlo, no
  lo menciona. Lo pidió así Juanjo: lo que no puede hacerse en un caso no se
  propone.

## Alternativas descartadas

- **Ventana emergente al llegar, como en el MIAE.** Juanjo la descartó: interrumpe
  la lectura al llegar y no le acaba de gustar.
- **Solo el porcentaje.** Sin el resultado no se interpreta bien, por los puntos
  eliminatorios.
- **Una insignia gráfica.** Se deja para más adelante si se pide: el texto con
  enlace basta, dura y queda natural en un pie.
- **La dirección del recurso como enlace.** Daría a la web de la guía la forma de
  un aval hacia cualquier sitio.
- **Comprobar la versión consultando la web del recurso.** Obligaría a la guía a
  conectarse a otros sitios, y ninguna de sus páginas lo hace.

## Consecuencias

- Cada recurso evaluado que muestre la mención lleva a la guía, y la página
  explica la evaluación a las personas que no la conocen.
- La página nueva y el apartado del archivo de evaluación se mantienen en los
  cinco idiomas. Los valores de `r` no se traducen: cambiarlos rompería los
  enlaces ya publicados, así que no se cambian.
- Los textos del recuadro están en `VCER`, en `construir.py`; el significado de
  cada resultado sale de la tabla de la página, y los nombres de los puntos, de
  la rúbrica del archivo de evaluación, sin copias.

## Evidencia

- `URLSearchParams` decodifica los parámetros codificados como en cualquier
  dirección web, incluidos los espacios escritos como `%20` o `+`.
- `location.replace("../" + idioma + "/vcer.html" + location.search)` conserva
  los datos al pasar de `vcer/` a la página del idioma.

## Riesgos y limitaciones

- Cualquiera puede escribir un enlace con el resultado que quiera. La página lo
  presenta como lo que declara la autoría del recurso, y el aviso lo dice.
- Si una IA escribe mal el enlace (un `r` traducido, por ejemplo), la página se
  ve sin recuadro. Por eso el archivo de evaluación dice que `r` va siempre en
  la misma forma.

## Validación

2026-10-02, con un servidor local:

- La dirección `vcer/?…` abre la página del idioma del navegador con el
  recuadro, en Chromium, Firefox y WebKit, en escritorio, móvil y tableta, con
  tema claro y oscuro, sin errores ni desbordamiento (`probar-web`).
- Frases de los cinco idiomas con y sin título, versión, dirección, fecha y
  porcentaje; sin parámetros y con un `r` desconocido, sin recuadro; con un
  porcentaje de 150, un mes 13, una dirección `javascript:` y un título con
  etiquetas HTML, esos datos se omiten o se muestran como texto.
- axe-core (WCAG 2 A y AA y buenas prácticas) sin fallos en `vcer.html`, con y
  sin resultado, y en `para-la-ia.html`, en Chromium y Firefox, en claro y
  oscuro.
