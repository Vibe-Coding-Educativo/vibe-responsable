# 15. Las recomendaciones siguen el orden de la vida del material

Fecha: 2026-09-24 · Estado: aceptado

## Contexto

Las diez recomendaciones no seguían un criterio de orden explícito. Tras las dos
eliminatorias de la evaluación VCER, la licencia, la declaración de IA, el
código, las dependencias, la accesibilidad, la autoría ajena, el registro y la
reutilización se alternaban sin relación, y dos recomendaciones remitían a una
posterior (la declaración de IA y la reutilización, al registro del punto 9).
El autor señaló que la licencia (3) y la oferta del código (10) son dos partes
de lo mismo, compartir, y decidió mantenerlas separadas pero revisar el orden.

## Decisión

Las recomendaciones siguen la vida del material, en cuatro fases:

| Fase | Recomendaciones | Antes |
|---|---|---|
| Proteger al alumnado | 1. Revisar el contenido · 2. No enviar datos personales | 1, 2 |
| Construir el material | 3. Entender qué hace · 4. No depender de servicios · 5. Hacerlo accesible | 5, 6, 7 |
| Documentar el trabajo | 6. Citar la autoría ajena · 7. Guardar el rastro · 8. Declarar el uso de IA | 8, 9, 4 |
| Compartir el material | 9. Publicar con licencia libre · 10. Ofrecer el código | 3, 10 |

Toda remisión entre recomendaciones va hacia atrás: la declaración de IA (8) y
la oferta del código (10) remiten al registro (7), que ya se ha leído. Los
capítulos, la rúbrica VCER, la infografía y los iconos de la lista siguen la
misma numeración. Las cuatro fases se muestran igual en la infografía (ADR 8) y
en la lista de la guía: un rótulo vertical en el margen izquierdo, en dos líneas
(verbo y complemento), junto a una llave que abarca sus recomendaciones. En la
lista, el rótulo mide lo máximo que cabe en una fase de dos recomendaciones en
una pantalla de portátil (unos 10,5 píxeles), y la lista no crece en altura, de
modo que la página sigue cabiendo en una pantalla. Cada fase es un elemento de
lista con su nombre y su propia lista numerada, para que los lectores de
pantalla anuncien el grupo. En el papel el rótulo pasa a ser un título
horizontal sobre cada fase. Los nombres de las fases están en `UI` de
`construir.py` (`fases`) y en `infografia/generar.py`, y deben coincidir.

## Alternativas descartadas

- **Fusionar la licencia y la oferta del código en una sola recomendación**:
  dejaba nueve, obligaba a rehacer el título, la infografía y la rúbrica, y los
  anuncios ya publicados hablaban de diez. El autor prefirió mantener las dos.
- **Mantener el orden anterior**: no tenía un criterio que pudiera explicarse y
  obligaba a remitir hacia delante.
- **Ordenar por importancia**: las diez tienen el mismo rango (ADR 8); solo las
  dos primeras, eliminatorias en la evaluación, van delante por serlo.

## Consecuencias

Cambian las direcciones de los capítulos: `capitulo-3.html`, por ejemplo, pasa a
ser «Entender qué hace el material». Un enlace ya compartido a un capítulo
concreto lleva ahora a otro, aunque ninguno queda roto, y las evaluaciones VCER
hechas antes citan los puntos con la numeración antigua (correspondencia en la
tabla). El cambio se hizo mientras la guía era un borrador, antes del DOI.
