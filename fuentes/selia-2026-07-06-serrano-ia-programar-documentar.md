---
titulo: Inteligencia artificial: programar, documentar y no acabar en un berenjenal
autor: Ernesto Serrano (eXeLearning)
evento: I Jornada sobre Software Libre e Inteligencia Artificial Abierta (seLIA), URJC Fuenlabrada
fecha: 2026-07-06
url: https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html
descargado: 2026-09-21
licencia: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
nota: transcripción del material publicado (eXeLearning); las imágenes incrustadas se han omitido
---

---

[Página ][ **2**[/]**10**]

# La IA hoy... y el berenjenal 

# Qué facilita de verdad 

Sin hype: hoy la IA ayuda de verdad en tareas concretas.

- **Generar código**: borradores, funciones repetitivas, *boilerplate*.
- **Detectar errores**: explicar trazas, sugerir causas.
- **Pruebas**: tests para código sin cobertura.
- **Documentación**: a partir del código real.

Pero **propone, no decide**. Y va tan rápido que es fácil **perder el rastro**.

# Notas del ponente 

Lista breve y reconocible; no te detengas. El objetivo es llegar rápido al giro: todo esto es genial... hasta que pierdes el porqué. Ejemplo cercano: un PR asistido por IA que funciona y pasa los tests, y a las tres semanas nadie recuerda por qué se eligió ese enfoque.

---

[Página ][ **3**[/]**10**]

# El berenjenal 

# Velocidad sin rastro = caos 

En unas semanas, el proyecto que iba rapidísimo se convierte en un berenjenal:

- El **código** está; el **\"por qué\"** no.
- Nadie recuerda qué alternativas se descartaron ni con qué evidencia.
- Y en **software libre**, encima: *¿de dónde viene ese código? ¿la licencia y la procedencia están limpias?*

> Programar rápido es fácil. **No acabar en un berenjenal** es el trabajo de verdad.

# Notas del ponente 

Este es el gancho de la charla --- dale gracia. El berenjenal no es culpa de la IA, es de **proceso**: la IA solo hace que el caos llegue antes. La pregunta que abre la siguiente sección: ¿y si capturamos la **decisión**, no solo el resultado?

---

[Página ][ **4**[/]**10**]

# ADRs: la IA apoya la decisión 

# Un ADR captura el porqué 

Un **ADR** (Architecture Decision Record) documenta **una decisión**: no el código, el **porqué**.

Cada uno es un `DEC-NNNN` con secciones fijas: *Contexto · Problema ·* *Opciones · Evidencia · Decisión* *· Consecuencias · Riesgos · Validación*.

En **mod_exelearning** (plugin de Moodle, **GPLv3**): **60 ADRs** --- 53 aceptadas, 4 propuestas, 3 superseded. En el código, cada función **cita su decisión**: `// (DEC-0008)`.

# El frontmatter deja rastro 

``` yaml
id: DEC-0043
titulo: "Detección de GeoGebra calificable"
estado: Aceptada        # Propuesta | Aceptada | Rechazada | Superseded
fecha: 2026-06-22
agentes: [erseco, codex]
herramienta_ia:
  interfaz: codex
  modelo: gpt-5
fuentes: [REPO-071, EXP-014]
```

- El ADR **declara quién decidió** (persona o agente) y **con qué IA y modelo**.
- **\"Sin fuente no hay afirmación\":** cada dato cita `repo + ruta + commit`, doc oficial o experimento reproducible.
- Ver el ADR completo en el repo: [DEC-0043 ↗](https://github.com/exelearning/mod_exelearning/blob/main/research/decisiones/adr/DEC-0043-deteccion-geogebra-auto-scorm.md)

# Notas del ponente 

Núcleo de la charla. Enseña, si puedes, un ADR real en `github.com/exelearning/mod_exelearning`. Elegí **DEC-0043** a propósito para el ejemplo del frontmatter porque lo hizo **codex + gpt-5** (no Claude): así ya planto la semilla del agnosticismo antes de llegar a esa sección.

---

[Página ][ **5**[/]**10**]

# Propone la IA, dispone el humano 

# Los papeles quedan claros 

El ADR reparte los papeles:

- La **IA redacta** las *Opciones* y la *Evidencia* (con fuentes).
- El **humano decide**: fija el `estado` (Propuesta → **Aceptada / Rechazada**).

Ejemplo real: **auditorías multi-agente**. En **[DEC-0016 ↗](https://github.com/exelearning/mod_exelearning/blob/main/research/decisiones/adr/DEC-0016-auditoria-seguridad-correccion.md)**, decenas de agentes revisan en 12 dimensiones → **21 hallazgos**; el humano **corrige 18 y difiere 3** con justificación.

> La IA **propone**; el humano **dispone**. Y siempre: **revisa el diff**.

# Notas del ponente 

El mensaje para seLIA: la IA no toma la decisión, la **prepara**. El `estado` (Propuesta/Aceptada/Rechazada) es del humano. Las auditorías multi-agente dan buen \'wow\', pero recalca: el valor no es el número de agentes, es que **queda por escrito quién decidió y por qué**.

---

[Página ][ **6**[/]**10**]

# research/: no solo ADRs 

# Un sistema de trazabilidad completo 

Los ADRs no van solos: viven en [`research/`](https://github.com/exelearning/mod_exelearning/tree/main/research), un sistema que hace **todo trazable**.

- **`decisiones/`** --- los ADRs (`DEC-NNNN`).
- **`fuentes/`** --- fuentes citables (repos de referencia, docs): `REPO-NNN` / `FTE-NNN`.
- **`experimentos/`** --- reproducibles (`EXP-NNN`): comando, commit, entorno, métricas.
- **`analisis/`, `tareas/`, `status.yaml`, diario** --- trabajo y estado, **append-only**.
- **`plantillas/`, `schemas/`, `tools/`** --- plantilla de ADR, validación e **índices auto-generados**.
- **[`AGENTS.md` ↗](https://github.com/exelearning/mod_exelearning/blob/main/research/AGENTS.md)** --- las reglas del juego para personas y IA.

> Cada ADR **cita** sus fuentes y experimentos por su id. Tiras del hilo y llegas a la evidencia.

# Notas del ponente 

Es la parte que convence a un público de software libre: no es *\"confía en mí\"*, es un **sistema auditable** y público. Si puedes, ábrelo en vivo: `github.com/exelearning/mod_exelearning/tree/main/research` y el `AGENTS.md`. Regla estrella a leer en voz alta: **\"sin fuente no hay afirmación\"**. No te enredes con cada carpeta; basta la idea: decisiones + fuentes + experimentos, todo enlazado y append-only.

---

[Página ][ **7**[/]**10**]

# ¿ADR o SDD (spec-kit / openspec)? 

# Qué vs por qué 

**No compiten: SDD dice el *qué*; el ADR, el *por qué*.**

- **SDD** (Spec Kit, OpenSpec): spec → genera plan, tareas y código. **Caduca** al implementarla.
- **ADR**: registra la decisión y su evidencia. **Append-only**, perdura.

**A favor del ADR:** agnóstico (markdown+git, **sin lock-in**), auditable, ideal en **código vivo**.\
**En contra:** más manual, no genera código; para una *feature* nueva de cero, SDD estructura mejor.

> No es *o uno o otro*: se **combinan** (OpenSpec trae `spec-driven-with-adr`).

# Notas del ponente 

Respuesta a la pregunta típica: *\"¿por qué esto y no spec-kit / openspec?\"*. Clave: **SDD = qué, ADR = por qué**; en un proyecto **vivo y libre** lo que se pierde es el porqué, y markdown+git **no ata a ningún motor**. Remate: no es *o uno o otro* --- se **combinan** (OpenSpec trae `spec-driven-with-adr`). Si aprietan: *\"spec para la feature, ADR para la coherencia entre features\"*. Puedes usarla de reserva y saltarla si vas justo de tiempo.

---

[Página ][ **8**[/]**10**]

# Agnóstica, transparente y libre 

# IA agnóstica: sin atarte a ninguna 

El frontmatter registra `interfaz` y `modelo`, así el proceso **no se ata a ninguna IA**:

- **[DEC-0043 ↗](https://github.com/exelearning/mod_exelearning/blob/main/research/decisiones/adr/DEC-0043-deteccion-geogebra-auto-scorm.md)** se decidió con **`codex` + `gpt-5`**.
- **[DEC-0044 ↗](https://github.com/exelearning/mod_exelearning/blob/main/research/decisiones/adr/DEC-0044-auditoria-bugs-criticos.md)** (auditoría de bugs) con **`claude-code` + `claude-fable-5`**.
- Otros, con `claude-opus`... **da igual el motor**.
- Y el mismo proceso vale con **modelos de pesos abiertos** (Llama, Mistral, Qwen, DeepSeek) e incluso de **licencia libre / OSI** (OLMo, IBM Granite), corriendo **en local** (Ollama).

> La **decisión** y su **evidencia** sobreviven a la IA que las escribió. Cambias de modelo (o de proveedor) sin perder el hilo: **cero lock-in**.

# Notas del ponente 

Mensaje diferencial para una jornada de IA **abierta**: no dependemos de un proveedor. Como la evidencia se cita (`repo+ruta+commit`), cualquier IA ---o persona--- reproduce la verificación. Si preguntan por modelos locales: encaja perfecto, el proceso es el mismo con Ollama / pesos abiertos.

---

[Página ][ **9**[/]**10**]

# Software libre = transparencia + contexto 

# El repo libre es lo que lo hace posible 

Que el repo sea **libre y público** (mod_exelearning, **GPLv3**) no es un detalle: es lo que hace todo esto posible.

- **Contexto**: cualquier IA (o persona) lee el repo y **retoma el hilo** --- issues, PRs, ADRs, evidencia.
- **Transparencia**: todo es **append-only** y citable; se puede auditar.
- **Coherencia libre**: *pesos abiertos ≠ software libre*; prefiere modelos **abiertos/locales**, no subas datos sensibles y **devuelve al procomún**.

# Notas del ponente 

Cierre conceptual: el software libre es el **sustrato** que da CONTEXTO a la IA y TRANSPARENCIA al proceso; un repo cerrado no puede ofrecer esto. Coletilla clásica de la jornada: *pesos abiertos no es lo mismo que libre* --- mira la licencia real. En un repo privado, este sistema pierde casi toda su gracia.

---

[Página ][ **10**[/]**10**]

# Cierre 

# Takeaways 

1.  La IA **programa y documenta**; **tú decides**.
2.  Documenta la **decisión** (ADRs), no solo el código.
3.  Registra **qué IA y modelo** → **agnóstico**, sin lock-in.
4.  **Repo libre = transparencia + contexto** para cualquier IA.
5.  **Sin fuente no hay afirmación**, y **revisa el diff**.

# Moraleja 

> La IA no te saca del berenjenal. **Un buen ADR, sí.**

Programar rápido está al alcance de cualquiera. **Documentar la decisión** ---de forma trazable, agnóstica y libre--- es lo que te deja dormir tranquilo. Y si el repo es libre, el berenjenal lo desenredamos entre todos.

# Enlaces y gracias 

Gracias. ¿Preguntas? (y pásate por el stand)

- mod_exelearning --- <https://github.com/exelearning/mod_exelearning>
- eXeLearning --- <https://exelearning.net>
- seLIA (jornada) --- <https://codeberg.org/seLIA>
- GitHub de Ernesto --- <https://github.com/erseco>
- Web personal --- <https://ernesto.es>
