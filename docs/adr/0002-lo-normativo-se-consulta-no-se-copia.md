# 2. El material normativo se consulta en el cuaderno, no se copia al repositorio

Fecha: 2026-09-21 · Estado: sustituido por el [ADR 3](0003-el-material-de-consulta-no-se-publica.md)

## Contexto

La parte legal de la guía (protección de datos del alumnado, propiedad
intelectual, Reglamento de IA) se apoya en un cuaderno de Gemini Notebook con
quince documentos: reglamentos y leyes consolidadas, guías de la AEPD y
publicaciones de la UNESCO y de la Comisión Europea. El [ADR 1](0001-las-fuentes-se-guardan-en-el-repositorio.md)
estableció que las fuentes se guardan en el repositorio, pero aquí chocan dos
cosas: parte de ese material no permite la redistribución (las guías de la AEPD
no llevan licencia de reutilización expresa y las de la UNESCO y la de
anonimización son CC BY-NC-SA, incompatibles con una guía CC BY-SA), y los
textos legales consolidados cambian, de modo que una copia envejece mal.

## Decisión

De ese cuaderno se copian al repositorio solo los documentos con licencia que
lo permita y que sostengan el contenido de la guía: el marco AILit (CC BY 4.0),
la guía de la UNESCO para responsables de políticas (CC BY-SA 3.0 IGO) y las
orientaciones de la Generalitat de Catalunya (CC BY 4.0).

El resto se consulta en el cuaderno cuando hace falta, con la herramienta
`notebooklm`, que permite leer el texto íntegro de cualquier documento y
preguntar sobre el conjunto. En la guía se cita siempre por el enlace oficial,
y por artículo cuando se trata de una norma. El índice `fuentes/README.md`
recoge esos documentos con su enlace y el motivo por el que no se copian.

## Alternativas descartadas

- **Copiarlo todo igualmente**: publicaría en un repositorio público material
  con licencia no comercial o sin permiso de reutilización.
- **Copiar los textos legales**: un texto consolidado cambia; una copia fechada
  induciría a citar una redacción derogada.
- **No usar el cuaderno y buscar cada cosa en su web**: se pierde la consulta
  conjunta sobre los quince documentos, que es justamente lo que resuelve las
  preguntas que cruzan varias normas.

## Consecuencias

Las afirmaciones legales de la guía dependen de una consulta al cuaderno, que
exige la sesión de Gemini Notebook autenticada. A cambio, se cita siempre la
versión vigente y no se redistribuye nada sin permiso. Si el cuaderno dejara de
estar disponible, habría que recuperar los documentos desde los enlaces
oficiales del índice.
