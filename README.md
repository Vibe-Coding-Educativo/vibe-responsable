# Guía para publicar materiales educativos creados con vibe coding

Guía ética y de responsabilidad, no técnica, para la comunidad educativa: licencias libres, protección de los datos del alumnado y del profesorado, código comprensible, transparencia sobre el uso de la IA y registro de las decisiones.

**Web de la guía:** <https://vibe-coding-educativo.github.io/vibe-responsable/>

Nace en el grupo de Telegram [Vibe Coding Educativo](https://t.me/vceduca) y se dirige a docentes de cualquier país. Contiene una presentación, la lista «Antes de publicar: diez recomendaciones» con su infografía, un capítulo que desarrolla cada recomendación, los textos para dar a la IA y una página sobre las herramientas. Está en revisión por su autor.

## Cómo está organizado el repositorio

| Carpeta o archivo | Contenido |
| --- | --- |
| `contenido/<idioma>/` | El texto de la guía en Markdown, un archivo por página, en el orden en que se leen: `00-presentacion.md`, `01-guia.md`, `02-herramientas.md`, `04-para-la-ia.md` y `03-creditos.md`, más un archivo por capítulo en `capitulos/`. Es lo único que hay que editar para cambiar el contenido. |
| `construir.py` | Genera la web a partir del Markdown. Necesita [pandoc](https://pandoc.org/). |
| `es/`, `index.html` | La web generada. No se editan a mano. |
| `recursos/` | Hoja de estilos, script y tipografía de la web, y el logotipo con su favicon en `recursos/logo/` (el original editable es `logo.svg`). |
| `infografia/` | La infografía, su original editable en SVG y el script que la genera. |
| `fuentes/` | Los documentos consultados, con su autoría y su licencia, y el índice de los que solo se consultan. |
| `docs/adr/` | Registro de las decisiones del proyecto, con su contexto y las alternativas descartadas. |

Para regenerar la web después de cambiar el contenido:

```bash
python3 construir.py
python3 infografia/generar.py     # solo si cambian los títulos de la lista
```

La web no usa bibliotecas ni servicios externos, y no recoge ni guarda ningún dato. La tipografía va dentro del propio repositorio.

## Cómo se ha hecho

La guía se elabora en el nivel 4 del [MIAE](https://educacion.bilateria.org/marco-para-la-integracion-de-la-ia-generativa-en-las-tareas-educativas-miae-v-2-1), la colaboración avanzada entre la persona y la IA. El texto y el código se han escrito en diálogo con Claude Code. El autor ha dirigido y corregido el contenido, ha contrastado las afirmaciones con sus fuentes y ha revisado el resultado. La web se ha probado en Chromium, Firefox y WebKit, en escritorio, tableta y móvil, con tema claro y oscuro. Las decisiones tomadas durante la elaboración están en [`docs/adr`](docs/adr/README.md).

## Licencias

- **Código** (`construir.py`, `recursos/`, `infografia/generar.py`): [GNU AGPL v3](LICENSE).
- **Contenidos** (textos de la guía e infografía): [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es).
- **Iconos**: [Lucide](https://lucide.dev/), licencia ISC.
- **Tipografía**: [Atkinson Hyperlegible](https://www.brailleinstitute.org/freefont/), del Braille Institute, [licencia OFL](recursos/fuentes/OFL.txt).
- **Fuentes de terceros** en `fuentes/`: cada documento conserva su autoría y su licencia, indicadas en su cabecera y en [`fuentes/README.md`](fuentes/README.md).

© 2026 [Juan José de Haro](https://bilateria.org)
