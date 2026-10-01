# Gardar o rastro de como se fixo

## O motivo de cada decisión

Coa intelixencia artificial (IA) prográmase moi de présa, e **ás poucas semanas ninguén lembra por que se tomou cada decisión**. Ernesto Serrano, do equipo de eXeLearning, descríbeo no seu relatorio [«Inteligencia artificial: programar, documentar y no acabar en un berenjenal»](https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html): o código está, pero o porqué non, e ninguén lembra que alternativas se descartaron nin con que argumentos. A IA non causa esa desorde, aínda que fai que chegue antes.

Conservar o rastro serve para tres cousas. Permite retomar o traballo despois dun tempo sen ter que reconstruílo, permite explicarllo a outra persoa que queira continualo, e evita desfacer de boa fe unha decisión que tiña un motivo. Nun material educativo aberto ten unha cuarta utilidade, xa que lles mostra ás persoas que o reutilizan como se fixo, que é o que completa a declaración da recomendación 8.

## O rexistro de decisións

A forma habitual de conservalo no desenvolvemento de software é o rexistro de decisións de arquitectura, ou ADR, polas siglas do seu nome en inglés, *Architecture Decision Record*. Cada decisión importante anótase nun documento breve que recolle catro cousas:

- **O contexto.** A situación que obriga a decidir.
- **A decisión.** O que se fai, co detalle suficiente para aplicalo.
- **As alternativas descartadas.** Cada unha co motivo polo que non se escolleu, que é a parte que evita repetir o debate máis adiante.
- **As consecuencias.** O que mellora e o que empeora.

Unha decisión que deixa de valer non se borra, senón que se marca como substituída pola nova, de modo que o rastro se conserva. No proxecto que presenta o relatorio, cada rexistro anota ademais con que ferramenta de IA e con que modelo se tomou a decisión, o que permite cambiar de ferramenta sen perder a historia.

Nese mesmo proxecto, cada rexistro recolle tamén a evidencia na que se apoia a decisión, os riscos coñecidos e a forma en que se validou. O relatorio resúmeo na regra «sen fonte non hai afirmación»: cada dato remite á documentación oficial, a unha versión concreta do código ou a unha proba que calquera pode repetir. Esta precaución é especialmente útil coa IA, xa que pode redactar unha xustificación convincente dunha decisión que parte dunha premisa falsa. A evidencia anotada permítelle á persoa comprobala sen refacer o traballo. O que non se puido verificar anótase como hipótese pendente de validación, de forma que ninguén o tome despois por un feito comprobado.

## O traballo da IA e o da persoa

**O rexistro non supón unha tarefa engadida para o docente**, xa que o escribe a IA a partir do que se decide na conversa, e a persoa comproba que o anotado corresponde ao decidido. O relatorio resúmeo en que a IA propón e a persoa dispón.

O rexistro tampouco se reconstrúe ao final, xa que un material adoita saír de moitas sesións de traballo repartidas en días distintos, e recompoñer despois esas conversas resulta inviable. **O rexistro escríbese no momento en que se decide**, e por iso resiste o paso das sesións. Aos axentes de programación indícaselles unha vez no seu ficheiro de instrucións, e mantéñeno en todas. Convén pedilo polo seu nome, por exemplo «leva un rexistro de decisións con ADR», xa que a IA coñece o formato e aplícao sen máis explicacións. Na web dun chatbot, o mínimo é pedir ao rematar cada sesión que a IA anote as decisións dese día nun documento que se vai gardando.

## Un exemplo da comunidade

A guía interactiva [«Elige tu IA»](https://explikarlos.github.io/elige-ia/), publicada como expliCarlos, leva no seu repositorio un [rexistro de decisións](https://github.com/explikarlos/elige-ia/blob/main/docs/decisions/ADR-001-static-pages.md). O primeiro explica por que a aplicación é estática e non ten servidor. Entre as alternativas descartadas figura unha base de datos, que permitiría sincronizar as respostas, pero que se descartou porque aumentaba os riscos de privacidade, o custo e o mantemento. Calquera persoa que retome ese proxecto sabe así que a ausencia de servidor responde a unha decisión meditada.

Esta guía leva tamén o seu propio [rexistro](https://github.com/Vibe-Coding-Educativo/vibe-responsable/tree/main/docs/adr), que recolle as decisións sobre as súas fontes, a súa web e os seus exemplos.
