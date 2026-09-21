---
titulo: Creación de recursos educativos adaptativos mediante vibe coding
autor: Juan José de Haro
blog: educacion.bilateria.org
fecha: 2026-05-25
url: https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding
descargado: 2026-09-21
licencia: CC BY-SA 4.0
---

Este artículo ha sido ampliado y reemplazado por [Metodología para la creación de sistemas educativos adaptativos bayesianos](https://educacion.bilateria.org/metodologia-para-la-creacion-de-sistemas-educativos-adaptativos-bayesianos)

Los **recursos educativos adaptativos** permiten que una actividad cambie según las respuestas del alumno. En este artículo veremos **dos ejemplos** y **un protocolo** para crear este tipo de recursos con IA. Para el que lo desee hay también un anexo matemático con la metodología utilizada.

- [Introducción a los recursos adaptativos](https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding/#Introduccion_a_los_recursos_adaptativos)
- [Ejemplo 1: Test adaptativo para la evaluación diagnóstica](https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding/#Ejemplo_1_Test_adaptativo_para_la_evaluacion_diagnostica)
- [Ejemplo 2: Itinerario adaptativo](https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding/#Ejemplo_2_Itinerario_adaptativo)
- [Cómo crear aplicaciones educativas con vibe coding](https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding/#Como_crear_aplicaciones_educativas_con_vibe_coding)
- [Anexo: Metodología matemática utilizada](https://educacion.bilateria.org/la-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding/#Anexo_Metodologia_matematica_utilizada)

## Introducción a los recursos adaptativos
Los recursos educativos suelen ser **lineales**, por ejemplo, un test de evaluación es el mismo para todos. De la relación entre aciertos y errores obtendremos una calificación y, con suerte, un análisis de lo que cada alumno ha fallado y lo que le conviene mejorar.

Si esa misma evaluación la hacemos adaptativa, **el sistema se acomoda a las respuestas del alumno, aprende de sus fallos y aciertos y ambos se convierten en información**: El sistema debe usar las respuestas del alumno como evidencias para actualizar hipótesis sobre su estado de aprendizaje. Estas hipótesis pueden ser niveles de aprendizaje, de dificultad, errores conceptuales, etc. El sistema adaptativo no hace las mismas preguntas a todos, sino que las adapta según las respuestas realizadas hasta el momento por el alumnado.

El sistema adaptativo **aprende de las respuestas del alumno para proponerle preguntas adaptadas a su nivel, de refuerzo si detecta errores o de ampliación y continuación más avanzada si detecta que puede hacerlo**.

Esto puede hacerse con cualquier recurso, no estamos limitados a la evaluación. Por ejemplo, con un itinerario de aprendizaje, un juego educativo, un tutorial interactivo y cualquier recurso educativo digital en el que tenga sentido la adaptación a las diferentes tipologías y necesidades del alumnado.

## Ejemplo 1: Test adaptativo para la evaluación diagnóstica
Hemos hecho dos ejemplos. El primero es un [test de evaluación de cultura general](https://jjdeharo.github.io/bayes-test/). Fue el primero, hecho a modo de demo educativa, y permite evaluar nuestros conocimientos en tres niveles: **básico, medio y avanzado**. Cada vez que respondemos una pregunta, el sistema nos hace otra, de forma que la información que recibe de la respuesta es máxima para conocer nuestro nivel. De esta forma va adaptando las preguntas hasta que tiene información suficiente para decidir el nivel que tenemos en este tema. Para que esto sea significativo, las preguntas deben estar correctamente clasificadas en los 3 niveles. Las preguntas han sido generadas mediante IA, pero podríamos habérselas suministrado ya clasificadas cada una en su nivel.

<figure class="aligncenter size-full wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec353432c">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen.png" class="wp-image-3707" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen.png 812w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-272x300.png 272w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-768x848.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-676x747.png 676w" sizes="auto, (max-width: 812px) 100vw, 812px" width="812" height="897" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
</figure>

El programa no solo determina el nivel del usuario, proporcionando el porcentaje de la probabilidad de pertenencia a cada uno, sino que crea un informe con aquellos aspectos en los que se puede mejorar y los que ya se dominan. Estos aspectos son los diferentes temas motivo de las preguntas (ciencias, historia, etc.).

<figure class="aligncenter size-full wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec35361e0">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-1.png" class="wp-image-3708" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-1.png 812w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-1-280x300.png 280w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-1-768x822.png 768w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-1-676x723.png 676w" sizes="auto, (max-width: 812px) 100vw, 812px" width="812" height="869" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
</figure>

Es importante remarcar que 7/10 no debe entenderse como una nota, ya que las preguntas han sido hechas para diagnosticar el nivel de conocimientos y lo que realmente importa es el nivel alcanzado. De ahí que sea una **evaluación diagnóstica**, pero no calificadora. Podríamos tener notas superiores o inferiores, de forma un tanto aleatoria, según los niveles en los que hubiésemos respondido. Es decir, un alumno que solo es capaz de responder cuestiones de nivel básico podría sacar un 8/10 y otro capaz de responder preguntas con más dificultad un valor inferior, precisamente porque, al ser capaz de responder preguntas más complejas, se le han hecho más de este tipo. Estas preguntas han servido para hacer un diagnóstico, pero no determinan una nota. No se hace un número fijo de preguntas; cuando el sistema tiene la certeza de que el alumno pertenece a una categoría determinada, entonces para de hacerlas. En el anexo se explica con más detalle el método utilizado.

## Ejemplo 2: Itinerario adaptativo
El siguiente ejemplo es una aplicación, llamada [Despejar la incógnita x](https://jjdeharo.github.io/bayes-itinerario/), que permite practicar la técnica para despejar incógnitas en una ecuación de primer grado. El itinerario consta de tres etapas.

En primer lugar, muestra la técnica que se usará en cada etapa. Se le pueden pedir tantos ejemplos resueltos como se quiera.

<figure class="aligncenter size-full wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec353a055">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-3.png" class="wp-image-3710" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-3.png 646w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-3-234x300.png 234w" sizes="auto, (max-width: 646px) 100vw, 646px" width="646" height="828" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
</figure>

Cuando se decide practicar la etapa, el sistema examina las respuestas para determinar si se domina o no la técnica correspondiente. En este programa se ha limitado a un mínimo de 4 respuestas para el que las resuelva correctamente y un máximo de 10 para el que no.

En el caso de no superar una etapa, el programa dará la oportunidad de repetirla de nuevo o continuar con el resto del itinerario.

<figure class="wp-block-image size-full">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-5.png" class="wp-image-3712" loading="lazy" decoding="async" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-5.png 667w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-5-300x283.png 300w" sizes="auto, (max-width: 667px) 100vw, 667px" width="667" height="629" />
</figure>

Una vez terminadas las 3 etapas, el sistema da una indicación del progreso (iniciando, avanzando o dominando) y un informe de los puntos fuertes y débiles.

<figure class="aligncenter size-large wp-lightbox-container" data-wp-context="" data-wp-interactive="core/image" data-wp-key="6ab0ec353cf23">
<img src="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-4-626x1024.png" class="wp-image-3711" loading="lazy" decoding="async" data-wp-class--hide="state.isContentHidden" data-wp-class--show="state.isContentVisible" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on--pointerdown="actions.preloadImage" data-wp-on--pointerenter="actions.preloadImageWithDelay" data-wp-on--pointerleave="actions.cancelPreload" data-wp-on-window--resize="callbacks.setButtonStyles" srcset="https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-4-626x1024.png 626w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-4-183x300.png 183w, https://educacion.bilateria.org/wp-content/uploads/2026/05/imagen-4.png 661w" sizes="auto, (max-width: 626px) 100vw, 626px" width="626" height="1024" />
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDEyIDEyIj4KICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0yIDBhMiAyIDAgMCAwLTIgMnYyaDEuNVYyYS41LjUgMCAwIDEgLjUtLjVoMlYwSDJabTIgMTAuNUgyYS41LjUgMCAwIDEtLjUtLjVWOEgwdjJhMiAyIDAgMCAwIDIgMmgydi0xLjVaTTggMTJ2LTEuNWgyYS41LjUgMCAwIDAgLjUtLjVWOEgxMnYyYTIgMiAwIDAgMS0yIDJIOFptMi0xMmEyIDIgMCAwIDEgMiAydjJoLTEuNVYyYS41LjUgMCAwIDAtLjUtLjVIOFYwaDJaIiAvPgogICAgICAgICAgICA8L3N2Zz4=" />
</figure>

Debemos destacar que el número de ejercicios propuestos, las ayudas recibidas y el avance por las etapas vienen determinados por las respuestas del alumno. El itinerario mantiene una estructura progresiva, pero se adapta dentro de cada etapa y decide cuándo conviene **avanzar, reforzar o repetir**.

## Cómo crear aplicaciones educativas con *vibe coding*
Hemos preparado la web [Recursos educativos adaptativos bayesianos](https://jjdeharo.github.io/recursos-adaptativos/) desde donde podrás descargar el archivo llamado **Protocolo de recursos adaptativos bayesianos**, con instrucciones para la inteligencia artificial. Este archivo deberás proporcionárselo a la IA para que sepa qué debe hacer. Este mismo documento lo puedes consultar en formato web en la página anterior.

Casi con toda seguridad, la inteligencia artificial no hará bien el programa a la primera, por lo que deberás comprobar si lo que ha hecho se adapta a tus necesidades y, a través del diálogo con la IA, adaptar el recurso hasta que esté realmente preparado.

------------------------------------------------------------------------

<figure class="wp-block-audio">

<figcaption>Pódcast del artículo realizado por NotebookLM</figcaption>
</figure>

------------------------------------------------------------------------

## Anexo: Metodología matemática utilizada
Esta parte solo es para los interesados en conocer los entresijos matemáticos que forma la metodología adaptativa utilizada por el protocolo anterior.

### Inferencia bayesiana 

El teorema de Bayes permite actualizar la probabilidad de una hipótesis cuando obtenemos una nueva evidencia. Es decir, partimos de una idea inicial sobre el nivel (o la categoría que hayamos definido) del alumno y la vamos modificando a medida que responde preguntas.

En un recurso adaptativo, las hipótesis pueden ser, por ejemplo: el alumno tiene un nivel básico, medio o avanzado.

Al comenzar, el sistema todavía no sabe cuál de estas hipótesis es la más probable, así que se asigna la misma probabilidad a todos:

- \\(P(\\text) = 33.3%\\)
- \\(P(\\text) = 33.3%\\)
- \\(P(\\text) = 33.3%\\)\

Estas probabilidades iniciales se llaman **probabilidades previas**. Representan lo que el sistema cree antes de observar la respuesta del alumno.

Cuando el alumno contesta una pregunta, aparece una nueva evidencia, ya que ha acertado o ha fallado una pregunta de cierto nivel. Esa respuesta modifica las probabilidades anteriores. Si acierta una pregunta avanzada, aumentará la probabilidad de que pertenezca al nivel avanzado. Si falla varias preguntas básicas, aumentará la probabilidad de que necesite refuerzo en ese nivel.

En forma matemática, el teorema de Bayes se expresa así:

\\\[\
P(H \\mid E) = \\frac\
\\\]

- Donde \\(P(H \\mid E)\\) es la probabilidad de la hipótesis después de observar la evidencia. En nuestro caso, sería la probabilidad de que el alumno tenga un determinado nivel después de ver su respuesta.
- \\(P(H)\\) es la probabilidad previa de esa hipótesis, antes de la respuesta.
- \\(P(E \\mid H)\\) es la probabilidad, llamada **verosimilitud**, de observar una determinada respuesta del alumno si una hipótesis concreta fuera cierta. Por ejemplo, qué probabilidad habría de que un alumno de nivel avanzado acertara una pregunta avanzada.
- \\(P(E)\\) es la probabilidad de observar esa evidencia, **sin saber todavía cuál es el nivel real del alumno**. En nuestro ejemplo, sería la probabilidad global de que el alumno acierte una pregunta avanzada, antes de decidir si pertenece al nivel básico, medio o avanzado.

Aplicado a un test adaptativo, el razonamiento sería el siguiente:

> Si un alumno fuera de nivel avanzado, sería bastante probable que acertara esta pregunta difícil.\
> Si fuera de nivel básico, sería poco probable que la acertara.\
> Como la ha acertado, aumenta la probabilidad de que sea de nivel avanzado.

Y al contrario:

> Si un alumno falla una pregunta básica, esa respuesta es más compatible con la hipótesis de que necesita refuerzo. Por tanto, el sistema aumenta la probabilidad de que esté en un nivel inicial o de que tenga dificultades en ese contenido.

Lo importante es que el sistema no toma una única respuesta como definitiva. Cada respuesta modifica un poco el diagnóstico. Después de varias preguntas, las probabilidades se van separando: una hipótesis gana peso y otras lo pierden.

Por ejemplo, después de varias respuestas, el sistema podría obtener algo así de un alumno en particular:

- \\(P(\\text) = 12%\\)
- \\(P(\\text) = 31%\\)
- \\(P(\\text) = 57%\\)

Esto no significa que el alumno tenga una nota de 5,7 ni que haya acertado el 57 % de las preguntas. Significa que, según las respuestas observadas, el sistema considera que la hipótesis más probable es que el alumno se encuentre en el nivel avanzado.

Esta es la diferencia principal respecto a un test tradicional. En un test lineal, las respuestas se acumulan para obtener una puntuación. **En un test adaptativo bayesiano, las respuestas se utilizan como evidencias para actualizar un diagnóstico.**

El mismo principio puede aplicarse a otros tipos de recursos. En un itinerario de aprendizaje, la hipótesis no tiene por qué ser "nivel básico, medio o avanzado", sino que puede ser "domina la técnica", "está en proceso" o "necesita refuerzo". Cada ejercicio resuelto aporta una nueva evidencia y permite decidir si conviene avanzar, repetir, ofrecer una explicación adicional o proponer actividades de mayor dificultad.

**La inferencia bayesiana permite que el recurso educativo no siga un camino fijo, sino que tome decisiones a partir de la información que va obteniendo del alumno.**

### Verosimilitudes y modelo IRT 3PL 

Para que Bayes actualice las probabilidades, el sistema calcula las verosimilitudes. En las preguntas o actividades organizadas por niveles de dificultad, estas verosimilitudes se generan mediante el modelo **IRT 3PL** (*Item Response Theory, three-parameter logistic model*), es decir, el modelo logístico de tres parámetros de la teoría de respuesta al ítem.

La idea general es que la probabilidad de acertar una pregunta aumenta cuando el nivel hipotético del alumno supera la dificultad de la pregunta, y disminuye cuando la dificultad supera el nivel hipotético del alumno.

El modelo usado es:

\\\[\
P(\\text\\mid H_i,q)=\
c_q+(1-c_q)\\cdot\
\\frac{1+e\^}\
\\\]

Donde \\(\\theta_i\\) representa numéricamente la hipótesis o nivel \\(H_i\\), \\(b_q\\) representa la dificultad de la pregunta o actividad, \\(a\\) es el parámetro de discriminación y \\(c_q\\) es la probabilidad mínima de acierto por azar.

En el modelo IRT 3PL, estos tres parámetros tienen una función concreta: \\(b_q\\) sitúa la dificultad del ítem, \\(a\\) indica cuánto discrimina entre niveles próximos y \\(c_q\\) establece el suelo de probabilidad de acierto.

En preguntas de opción múltiple, este suelo se calcula a partir del número de opciones:

\\\[\
c_q=\\frac\
\\\]

Por ejemplo, en una pregunta de cuatro opciones:

\\\[\
c_q=\\frac=025\
\\\]

Esto significa que la probabilidad de acierto no se considera inferior al 25 %, porque incluso un alumno que responde al azar tiene esa probabilidad de acertar.

Si el alumno falla, se usa la probabilidad complementaria:

\\\[\
P(\\text\\mid H_i,q)=1-P(\\text\\mid H_i,q)\
\\\]

Estas probabilidades de acierto y fallo son las verosimilitudes que utiliza Bayes para actualizar el diagnóstico.

El modelo IRT 3PL no sustituye al teorema de Bayes. Su función es generar las verosimilitudes que Bayes necesita para hacer la actualización.

En recursos que no son tests, la misma lógica se aplica a preguntas, pasos, retos o actividades autocorregibles, siempre que se representen mediante una dificultad, una respuesta observable y una interpretación del resultado. La evidencia es un acierto, un fallo, un paso superado, una pista solicitada, un intento adicional o un error detectado, siempre que el recurso haya definido cómo se traduce esa actuación en una evidencia utilizable.

Cuando las hipótesis no son niveles ordenados, por ejemplo, distintos errores conceptuales, el modelo IRT 3PL no es el adecuado, porque presupone una escala común de nivel o dominio. En esos casos, las verosimilitudes se definen según la relación diagnóstica entre cada actividad y cada hipótesis. La actualización bayesiana sigue siendo la misma; lo que cambia es la forma de obtener las verosimilitudes.

### Entropía de Shannon 

La incertidumbre del sistema se mide mediante la **entropía de Shannon**:

\\\[\
H=-\\sum_i p_i\\log_2(p_i)\
\\\]

Donde \\(p_i\\) es la probabilidad actual de cada hipótesis.

Cuando las probabilidades están muy repartidas, la entropía es alta. Por ejemplo, si básico, medio y avanzado tienen probabilidades parecidas, el sistema todavía no tiene un diagnóstico claro.

Cuando una hipótesis concentra la mayor parte de la probabilidad, la entropía baja. En ese caso, el sistema tiene más seguridad sobre el estado del alumno.

La entropía se usa para tres cosas: medir la incertidumbre del diagnóstico, seleccionar actividades que aporten información y decidir si el proceso finaliza.

### Selección adaptativa y ganancia de información 

Después de actualizar las probabilidades, el sistema decide qué pregunta, explicación, pista, ejercicio o actividad presenta a continuación.

Esta selección no se basa simplemente en subir la dificultad tras un acierto y bajarla tras un fallo. El método utilizado es la **ganancia esperada de información**. Es decir, el sistema estima qué actividad reduce más la incertidumbre sobre el estado del alumno.

Como la incertidumbre se mide con la entropía de Shannon, la ganancia de información se calcula como una **reducción esperada de entropía**. De forma simplificada:

\\\[\
IG(q)=H(\\text)-H(\\text)\
\\\]

Para cada posible actividad, el sistema calcula qué ocurre si el alumno la supera y qué ocurre si no la supera. En cada caso estima cómo cambian las probabilidades de las hipótesis y qué entropía tiene la nueva distribución. Después compara la entropía actual con la entropía esperada tras esa actividad.

La actividad más adecuada es la que distingue mejor entre las hipótesis que todavía son plausibles. Por eso, la mejor pregunta no siempre es la que coincide exactamente con el nivel más probable. Si el sistema duda entre nivel medio y avanzado, una pregunta difícil resulta más informativa que una pregunta media. Si duda entre nivel básico y medio, selecciona una pregunta más sencilla o intermedia.

Cuando varias actividades tienen una ganancia de información muy parecida, el sistema introduce diversidad de contenidos. Así evita repetir siempre el mismo tipo de pregunta o el mismo concepto cuando hay varias opciones igualmente útiles.

### Criterio de parada y resultado final 

El proceso se detiene cuando el sistema alcanza una confianza suficiente, cuando la entropía baja por debajo de un umbral previsto, cuando se llega al número máximo de preguntas o pasos, o cuando las actividades disponibles ya no aportan información relevante.

El resultado final no se limita a una etiqueta ni a una puntuación. Se presenta como una interpretación pedagógica: qué parece dominar el alumno, qué dificultades muestra, qué conviene reforzar y con qué grado de seguridad se propone el diagnóstico.

Si la incertidumbre sigue siendo alta, el sistema lo indica claramente. En ese caso, el resultado se presenta como una estimación provisional basada en las evidencias disponibles, no como una conclusión definitiva.

Esta es la diferencia principal respecto a un recurso educativo lineal. En una secuencia fija, todos los alumnos recorren el mismo camino y sus respuestas solo sirven para avanzar, retroceder o recibir una puntuación. En un recurso adaptativo bayesiano, cada respuesta o actuación se utiliza como evidencia para actualizar un modelo del estado del alumno y decidir cuál debe ser el siguiente paso: una nueva pregunta, una explicación, una pista, una actividad de refuerzo, una propuesta de ampliación, un cambio de itinerario o una recomendación de recursos.

**Nota**: El texto del artículo tiene nivel 1 en el [Marco para la integración de la IA generativa](https://educacion.bilateria.org/marco-para-la-integracion-de-la-ia-generativa-en-las-tareas-educativas-v-2-revisada) y el anexo nivel 4.

Este artículo ha sido ampliado y reemplazado por [Metodología para la creación de sistemas educativos adaptativos bayesianos](https://educacion.bilateria.org/metodologia-para-la-creacion-de-sistemas-educativos-adaptativos-bayesianos)

- [](https://twitter.com/share?url=https%3A%2F%2Feducacion.bilateria.org%2Fla-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding&text=Creaci%C3%B3n%20de%20recursos%20educativos%20adaptativos%20mediante%20vibe%20coding "Compartir en X")
- [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Feducacion.bilateria.org%2Fla-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding "Compartir en LinkedIn")
- [](https://telegram.me/share/url?url=https%3A%2F%2Feducacion.bilateria.org%2Fla-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding&text=Creaci%C3%B3n%20de%20recursos%20educativos%20adaptativos%20mediante%20vibe%20coding "Compartir en Telegram")
- [](https://api.whatsapp.com/send?text=https%3A%2F%2Feducacion.bilateria.org%2Fla-creacion-de-recursos-educativos-adaptativos-mediante-vibe-coding%20Creaci%C3%B3n%20de%20recursos%20educativos%20adaptativos%20mediante%20vibe%20coding "Compartir en Whatsapp")
