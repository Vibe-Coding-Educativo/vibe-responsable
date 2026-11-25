# 23. La guía advierte de que la excepción educativa no cubre lo publicado en abierto

Fecha: 2026-11-25 · Estado: aceptado

## Contexto

El 05-03-2026 la Comisión Europea publicó *Toma de decisiones fundamentadas sobre contenidos educativos digitales: Directrices de la UE para docentes y educadores* (en español, `10.2766/1574949`; en inglés, `10.2766/6984929`), con licencia CC BY 4.0. Se cotejó entera con la guía para ver si había algo que adoptar.

Casi todo lo que dice sobre publicar contenidos ya estaba en la guía: la revisión del contenido, la accesibilidad, las licencias abiertas, la declaración del uso de IA. Quedaba un hueco: el capítulo 6 pedía sustituir lo que no permita la reutilización, pero no decía que la excepción a los derechos de autor para la enseñanza no sirve para un material publicado en abierto. Mucho profesorado cree que el fin educativo basta para incluir cualquier imagen o texto.

## Decisión

- El capítulo 6 tiene una sección nueva, «El uso educativo no permite publicarlo todo». Explica que la excepción solo cubre el uso bajo la responsabilidad del centro, en el aula o en plataformas seguras para su profesorado y su alumnado, que cada Estado la aplica de forma distinta y que un material publicado en abierto queda fuera de ella. Se apoya en las directrices de la Comisión, que lo exponen en su apartado 3, «Creación».
- El capítulo 4 cita esas directrices como respaldo europeo de lo que ya decía: priorizar los estándares abiertos y la posibilidad de exportar, para no depender de un único proveedor. Hasta ahora ese capítulo se apoyaba solo en el CEDEC, y la guía se dirige a docentes de cualquier país.
- Las directrices se añaden a las referencias y a `fuentes/`, con su texto extraído. Las páginas en catalán, gallego y euskera enlazan la versión española, porque no hay versión en esos idiomas (ADR 20); la inglesa, la versión inglesa.
- El cambio sube la guía a la versión 4.0, porque añade contenido (criterio del ADR 19).

Lo propuso el agente tras cotejar los dos documentos, y Juanjo lo aprobó el 25-11-2026.

## Alternativas descartadas

- **Citar el artículo 5 de la Directiva (UE) 2019/790 en lugar de las directrices.** Es la norma original, pero su texto no se pudo leer de forma automática en EUR-Lex, y la ley española que la aplica (artículo 32 de la Ley de Propiedad Intelectual) no coincide literalmente con ella. Las directrices lo resumen para el profesorado y dicen que cada Estado lo aplica de forma distinta, que es lo que necesita saber quien publica.
- **Adoptar su lectura del artículo 50 del Reglamento de IA.** Da a entender que todo contenido creado o modificado con IA debe etiquetarse por ley. El capítulo 8 es más exacto: obliga a quien publica solo en dos casos.
- **Adoptar sus recomendaciones sobre analítica del aprendizaje y paneles de seguimiento.** Chocan con el capítulo 2 y con el ADR 22.
- **Advertir de que no se introduzcan obras protegidas en la IA.** Las directrices lo afirman sin dar base legal.

## Consecuencias

La guía responde a una duda frecuente sin añadir ninguna recomendación ni cambiar la rúbrica VCER, que ya penaliza los elementos sin permiso de reutilización. Las cuatro traducciones de la sección nueva son automáticas, como el resto (ADR 20).

## Evidencia

Las directrices se leyeron enteras el 25-11-2026. Los DOI se comprobaron ese día: el español lleva a la versión española en op.europa.eu y el inglés, a la inglesa. La fecha de publicación (05-03-2026) es la que dan las noticias de la Comisión en digital-strategy.ec.europa.eu y education.ec.europa.eu.

## Validación

`construir.py --pdf` generó la web y los cinco PDF sin avisos. Los capítulos 4 y 6, los créditos y las referencias se probaron con `probar-web` en Chromium, Firefox y WebKit, en escritorio, tableta y móvil, sin errores ni desbordamiento.
