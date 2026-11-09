# 22. Un recuento de visitas que no distingue a quien lee no es seguimiento

Fecha: 2026-11-09 · Estado: aceptado

## Contexto

Hasta la versión 2.0, la guía prohibía cualquier contador de visitas. El capítulo 2 decía «Sin analítica. El material no incluye contadores de visitas ni herramientas de seguimiento», las instrucciones para crear con IA pedían no añadir «analítica o contadores de visitas» y el punto 2 de la rúbrica VCER, que es eliminatorio, daba un 0 a todo recurso que llevara «analítica o seguimiento».

Una web educativa puede necesitar saber qué páginas se leen sin saber nada de quién las lee. La regla anterior trataba igual un servicio de analítica de terceros, que sigue a las personas entre sitios, y un recuento sumado por página hecho por quien publica. La Agencia Española de Protección de Datos (AEPD) distingue los dos casos: su guía *Uso de cookies para herramientas de medición de audiencia* (enero de 2024) exime del consentimiento la medición de audiencia página por página hecha solo para quien publica (apartado II), con unas garantías mínimas (apartado III.A).

## Decisión

La guía admite, como mucho, un recuento de visitas por página que cumpla todo esto:

- lo hace quien publica en su propio servidor, no un servicio de terceros;
- se suma por página;
- no guarda nada que distinga a quien lee, ni su IP ni la página de la que llega;
- la web lo explica.

Cualquier otra analítica o seguimiento sigue dando un 0 en el punto 2 de la rúbrica. Se cambian, en los cinco idiomas, el punto 2 de la rúbrica (niveles 2 y 0), el apartado del capítulo 2, que pasa a llamarse «Sin seguimiento» y enlaza la guía de la AEPD remitiendo a sus apartados II y III.A, y las instrucciones para crear con IA, que solo añaden un contador si la persona lo pide y con esas condiciones. La guía de la AEPD se añade a las referencias, con su título en castellano en todas las versiones.

Juanjo eligió esta opción el 09-11-2026 frente a quitar el contador del Diario de IA Educativa o dejar que su evaluación VCER bajara a «no recomendable», y aprobó la redacción el mismo día.

## Alternativas descartadas

- **Mantener la prohibición total.** Excluye un recuento que no recoge datos de nadie y que la AEPD exime de consentimiento; obligaría a quitar contadores inocuos en lugar de distinguirlos de los que siguen a las personas.
- **Admitir cualquier analítica sin cookies.** Hay servicios sin cookies que identifican a las personas por otras vías (huella del navegador, IP); la condición útil es que no se guarde nada que distinga a quien lee.
- **Remitir solo a la AEPD sin dar las condiciones.** La guía se dirige a docentes de cualquier país, y las condiciones tienen que poder comprobarse sin conocer la normativa española.

## Consecuencias

Es un cambio de lo que dice la guía, así que sube a la versión 3.0 (ADR 19), con su DOI. Las evaluaciones VCER hechas antes no cambian de resultado salvo en el caso que se admite ahora. Al evaluar un recurso con contador, la IA tiene que comprobar en el código qué se envía y qué se guarda en el navegador.

## Evidencia

- AEPD, *Uso de cookies para herramientas de medición de audiencia*, versión de enero de 2024, <https://www.aepd.es/guias/guia-cookies-analiticas-externas.pdf>, apartados II y III.A (p. 4): informar a quien visita, vida útil limitada de lo que se guarda (13 meses como ejemplo) sin renovarse sola en nuevas visitas, y datos conservados como máximo 25 meses. Descargado y leído el 09-11-2026.
- Caso que motivó el cambio: el contador del Diario de IA Educativa (ADR 33 de su repositorio), que suma visitas por página y por hora en el servidor de quien publica, sin cookies, IP, navegador ni procedencia.

## Riesgos

La rúbrica no menciona la caducidad de lo que se guarda en el navegador. Si un recuento guarda algo allí, la garantía del apartado III.A de la AEPD pide que caduque; el capítulo 2 remite a ese apartado.
