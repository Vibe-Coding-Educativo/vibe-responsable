---
titulo: Crear REA con eXeLearning en tiempos de IA
subtitulo: Del contenido generado a la transparencia del código; retos para mantener la «A» de Abierto
autor: CEDEC (INTEF)
evento: I Jornada sobre Software Libre e Inteligencia Artificial Abierta (seLIA), URJC Fuenlabrada
fecha: 2026-07-06
url: https://descargas.intef.es/cedec/formacion/SL_REA_IA_julio26/index.html
descargado: 2026-09-21
licencia: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
nota: transcripción del material publicado (eXeLearning); las imágenes incrustadas se han omitido
---


---

# Punto de partida 

# Cuando crear es más fácil que comprender 

Imagina que alguien os regala una **impresora mágica**. En segundos produce libros de texto, actividades, explicaciones, imágenes. Todo parece perfecto. Todo parece real. Pero hay algo que esa máquina no te dice: no sabe si todo lo que imprime es verdad. No recuerda de dónde sacó las ideas. Y el mecanismo interno\... nadie lo entiende del todo.

---

# Tres desafíos clave 

# Replanteando la naturaleza de los REA en tiempos de IA 

A medida que la comunidad educativa empieza a usar esa imprenta, aparecen tres grietas. **No son catástrofes**. Son señales de alerta que debemos leer antes de que se conviertan en problemas reales. Las veremos una a una. Pero antes, conviene tenerlas juntas en la cabeza: **la grieta de la verdad, la grieta de la autoría, y la grieta del código.**

---

# Fiabilidad del contenido 

# ¿Lo que diga la IA? 

Los textos suenan bien. Las referencias parecen reales. Las explicaciones resultan convincentes. Pero a veces mienten. Con elegancia, con confianza, sin señales de alarma. En el aula, un error que nadie detecta no es un error: es un aprendizaje equivocado. Y lo más peligroso no es el error obvio, sino el error plausible: la fecha que casi es correcta, la cita que casi existió, el dato que casi coincide. Por eso **la revisión humana no es opcional**. La IA puede acelerar la producción, pero **la responsabilidad pedagógica no se delega**. Nunca.

---

# Dudas en la autoría y la licencia 

# Un horizonte de incertidumbre 

Las licencias Creative Commons que tan bien conocemos están pensadas para un mundo donde alguien crea algo y decide cómo compartirlo. Pero ¿qué ocurre cuando nadie sabe exactamente qué se ha creado ni cómo? ¿Quién es el autor de un texto generado por IA? ¿La persona que escribió el prompt? ¿La empresa que entrenó el modelo? ¿Los millones de obras que alimentaron ese entrenamiento sin saberlo? La pregunta que antes era «¿qué licencia tiene este recurso?» se convierte en «¿cómo se ha creado y qué herramientas han participado?». **La «A» de Abierto empieza a tambalearse.**

# Situación actual 

- En la práctica jurídica actual (España, UE y la mayoría de ordenamientos), **la autoría requiere una persona física**. La IA por lo tanto no puede ostentar derechos de propiedad intelectual.
- Una organización o una administración puede ostentar el derecho de autoría (cedido) especialmente en obras colectivas coordinadas por la misma.
- Es importante conocer el grado de intervención humana en la creación de materiales, si se usa la IA como herramienta auxiliar y los prompts con intención creativa clara el autor sería humano, si la IA crea de forma autónoma no debería haber autor reconocible.
- Si hay autoría humana se podrían aplicar licencias del tipo CC (recomendadas CC-BY y CC-BY-SA en los REA) pero hoy por hoy usar estas licencias no tiene plenas garantías jurídicas a contenido generado por IA si no conoces la cadena de derechos. Hay litigios abiertos (Getty Images vs. Stability AI, autores vs. OpenAI, etc.) que determinarán si el entrenamiento con obras protegidas constituye infracción y qué consecuencias tiene para los outputs.
- Las posturas frente a lo anterior son:

  -------------------------------------- ------------------------------------------------------- -------------------------------------------------
  **Postura**                            **Descripción**                                         **Riesgo**
  Ignorar el problema                    Licenciar CC BY sin más                                 Alto, especialmente para instituciones públicas
  Declarar la incertidumbre              Indicar el uso de IA y remitir a los T&C del servicio   Moderado, al menos hay transparencia
  Evitar CC BY en contenido IA puro      Solo licenciar CC la aportación humana demostrable      Conservador pero más sólido
  Usar solo herramientas con garantías   Usar modelos con datos licenciados                      Reduce el riesgo pero no lo elimina
  -------------------------------------- ------------------------------------------------------- -------------------------------------------------

Mas información:

- Juan José de Haro. Inteligencia Artificial en Educación. *[¿A quién pertenece el contenido generado por la IA?.](https://descargas.intef.es/cedec/proyectoedia/guias/contenidos/inteligencia_artificial/html/a-quien-pertenece.html "Enlace a web. Abre en ventana nueva")*
- Creative Commons. CCSignal. *[CC-Signals](https://creativecommons.org/cc-signals/ "Enlace a web. Abre en ventana nueva")* (Es una iniciativa de Creative Commons que propone un \"contrato social\" mediante un sistema de señales legibles por máquinas. Permite a los creadores expresar sus preferencias sobre si sus contenidos pueden ser usados para el entrenamiento de modelos de IA, fomentando la ética y la transparencia).
- Comisión Europea. Código de buenas prácticas definitivo sobre marcado y etiquetado de contenidos generados por IA. [Code of Practice on marking and labelling of AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content "Enlace a web. Abre en ventana nueva") (Marcado obligatorio (AI Act): Según el Reglamento de IA de la UE, a partir de agosto de 2026, los proveedores y usuarios deben marcar el contenido sintético (audio, imagen, vídeo o texto) mediante metadatos o etiquetas legibles por máquina para informar que el contenido ha sido generado o manipulado artificialmente

---

# La IA y el código 

# Nuestro programador de cabecera 

Esta es la más técnica de las tres grietas, pero quizá la más profunda. Cuando la IA escribe un juego educativo, una simulación, un componente interactivo\... funciona. Eso es lo impresionante. Pero a menudo nadie de la comunidad sabría explicar cómo ni modificarlo si algo falla. **Tenemos el código fuente. Pero no la comprensión**. Y sin comprensión, la apertura es solo un espejismo. El principio del software libre decía: **cualquier persona debe poder estudiar, modificar y mejorar el programa**. Ese principio se rompe cuando el código es tan opaco que nadie puede tocarlo.

---

# Del producto al proceso 

# Lo importante del cómo frente al qué 

Del mismo modo que dice la leyenda que una \"molesta impresora\" no podía ser arreglada por desconocimiento del código fuente y que eso fue una de las causas del nacimiento del proyecto GNU de Stallman\...

Si el software libre dijo «muéstrame el código», los **REA de la era de la IA deberían decir «muéstrame cómo lo has construido».**

---

# Marco de \"Transparencia IA\" 

# La transparencia ampliará la A de abierto de los REA 

Cuando comparto un REA, puedo también compartir: qué herramientas usé, qué revisé manualmente, qué generé de forma automática, qué dependencias tiene el código, qué prompts guiaron la creación. Esta documentación no es un requisito técnico. Es **un gesto de respeto hacia la comunidad que va a usar ese recurso**. Es decir: «te doy no solo lo que he creado, sino el conocimiento para que puedas continuarlo». Eso es lo que llamamos **Transparencia IA**.

---

# El papel de eXeLearning 

# Un escenario privilegiado 

eXeLearning no es víctima de este dilema. Es el escenario privilegiado para resolverlo. Formato abierto, comunidad real, independencia de plataformas propietarias, exportación a estándares\... Todas **estas características hacen de eXeLearning el lugar natural donde puede arraigar esta nueva cultura de la transparencia**.

Las oportunidades son concretas: metadatos de transparencia IA en los recursos, sistemas de trazabilidad, documentación técnica en los iDevices, comunidades de práctica para revisar código generado. No hablamos de ciencia ficción. Hablamos de decisiones que podemos tomar hoy

---

# Epílogo 

# A modo de reflexión

---

# Créditos y descarga 

# Descargar el archivo fuente 

  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Título        [Crear REA con eXeLearning en tiempos de IA]
  Descripción   [Ponencia en I Jornada sobre Software Libre e Inteligencia Artificial Abierta celebrada en la URJC en Fuenlabrada el 6 de julio de 2026. ]
  Autoría       [Cedec]
  Licencia      [[Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]
  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Información general sobre este recurso educativo 

Este contenido fue creado con [eXeLearning](https://exelearning.net/), el editor libre y de fuente abierta diseñado para crear recursos educativos.

[Descargar el archivo .elpx](#){download="Crear REA con eXeLearning en tiempos de IA.elpx" onclick="try{var p=window.parent;if(p&&p!==window&&p.eXeLearning&&p.eXeLearning.app){p.postMessage(,'*');return false;}}catch(e)if(typeof downloadElpx==='function')downloadElpx();return false;" style="background-color:#107275;color:#ffffff;"}

# Transparencia IA 

¿Qué ha hecho la IA en esta charla?

- Una vez desarrollada las ideas de los desafíos, la transparencia y el papel de eXeLearning (con lápiz, papel y borrador) **la IA generó la narrativa de la impresora mágica, las grietas y la nueva frontera**. Los texto han sido revisados por humanos y modificados para acomodarlos a la charla.
- La [banda sonora](https://open.spotify.com/playlist/0kxcF96PBhiTMBTbl9IFpb?si=zz8kMyirQeOhy-eig635Nw&pi=6VlD5tviT3e2B&nd=1&dlsi=3a03110ee78045b0 "Enlace a Spotify. Abre en ventana nueva") de la charla
- La **imagen que se incorpora a continuación** que resume dicha narrativa:

<figure class="exe-figure position-center" style="width: 800px;">
<img src="../content/resources/ChatGPT%20Image%203%20jul%202026,%2011_34_37.png" title="Narrativa de la charla" width="800" height="1200" alt="Narrativa de la charla" />
<figcaption><span class="author">Imagen obtenida por ChatGPT </span>. <span class="title"><em>Narrativa de la charla</em></span> <span class="license"><span class="sep">(</span><a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en" class="license" target="_blank" rel="noopener">CC0</a><span class="sep">)</span></span></figcaption>
</figure>
