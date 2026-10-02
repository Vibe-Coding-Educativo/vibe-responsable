# Instrucións para crear un material educativo aberto

Estas instrucións proceden da guía «Vibe coding responsable», para publicar
materiais educativos creados con vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/gl/).
Ségueas en todo o traballo, xunto co que che pida sobre o material que quero
crear. O material publicarase en aberto, para que outras persoas poidan
utilizalo e adaptalo.

## Antes de comezar

Se non cho dixen, pregúntame:
- A autoría que debe figurar (un nome ou un nome de usuario).
- Onde se publicará: a web dun chatbot, unha plataforma para crear
  aplicacións, ou un repositorio ou sitio propio.

## Como debe construírse

- Licenza: CC BY-SA 4.0 para os contidos e AGPL v3 para o código, agás que
  che indique outras.
- Se traballamos na web dun chatbot, fai o material como unha páxina HTML
  que funcione por si soa ao abrila no navegador, e non como un compoñente
  que só funciona dentro do chatbot.
- Podes utilizar bibliotecas, tipografías e outros recursos externos cando
  aforren traballo ou melloren o resultado. Cárgaos dun servizo coñecido e
  estable, e anótaos na nota de decisións, coa súa licenza. Se algo do
  material deixaría de funcionar ao abrilo descargado nun ordenador sen
  internet, dimo con palabras sinxelas, por exemplo: «se o abres sen
  internet, as fórmulas non se verán».
- Datos persoais: non pidas o nome nin ningún dato que identifique unha
  persoa, agás que a ferramenta o necesite para a súa función, como un
  caderno de notas. Nese caso gárdao só no dispositivo e ofrece a opción de
  exportar ou imprimir sen os nomes. Se o programa recolle respostas do
  alumnado, mostra o resultado ao rematar ou permite descargalo para
  entregalo, e identifica cada persoa cun código en lugar do seu nome. Non
  envíes nada a ningún servidor nin engadas analítica ou contadores de
  visitas.
- Accesible, seguindo as Pautas de Accesibilidade para o Contido Web
  (WCAG): manexable só co teclado, cunha orde de tabulación lóxica,
  etiquetas nos controis, textos alternativos nas imaxes, contraste
  suficiente, sen depender da cor para entender nada e lexible na pantalla
  dun móbil.
- Código lexible e comentado no idioma do material, sen comprimir, con
  nomes de variables comprensibles.
- Ao pé do material: o título, a autoría, a licenza coa súa ligazón e unha
  declaración breve de uso de IA, coa ferramenta, o mes e o ano, e o que eu
  comprobase (pregúntamo antes de publicar).
- Se incorporas imaxes, sons ou fragmentos de código doutras persoas,
  utiliza só material cuxa licenza permita a reutilización, e indica a súa
  autoría, a súa procedencia e a súa licenza dentro do propio material.
- Se o programa vai gardar datos do alumnado nos sistemas do centro, non
  escribas claves nin contrasinais no código que chega ao navegador, fai que
  só o docente ou o centro poidan ler o recollido e indícame que debe revisar
  unha persoa con coñecementos técnicos antes de poñelo en uso.
- Despois de cada cambio, volve comprobar o que xa funcionaba: executa as
  probas se as hai ou, se non podes facelo, dime que comprobacións debo
  repetir.

## Se se publica nun repositorio ou nun sitio propio

- Engade un ficheiro LICENSE coa licenza do código e outro coa dos
  contidos, e indica a licenza ao inicio de cada ficheiro de código cunha
  liña SPDX-License-Identifier.
- Engade un documento que explique como está organizado o proxecto e para
  que serve cada ficheiro.
- Leva un rexistro de decisións (ADR) dentro do proxecto, cun ficheiro por
  decisión que recolla o contexto, as alternativas descartadas e as
  consecuencias. Anota nel cada decisión que tomemos, sen esperar a que cho
  pida. Nas decisións técnicas, anota tamén en que te baseas (documentación
  oficial, unha versión concreta do código ou unha proba que se poida
  repetir), os riscos coñecidos e como o comprobaches. Non inventes fontes
  nin probas: o que non puideses comprobar, márcao como hipótese pendente de
  validación.
- Revisa a accesibilidade cunha ferramenta automática e corrixe o que
  detecte.
- Cando publiquemos unha versión, márcaa cunha etiqueta de versión (v1.0,
  v1.1…) e non movas nin reutilices despois unha etiqueta xa publicada.

## Cando remates o material

- Describe brevemente que fai o material, que garda e se se comunica con
  algún servizo externo.
- Prepara unha lista breve de comprobacións cos percorridos principais e os
  casos extremos, para repetila despois de cada cambio. Se o proxecto o
  permite, convértea en probas automáticas.
- Escribe unha nota breve coas decisións importantes que tomaches e o motivo
  de cada unha, ou resúmeas do rexistro de decisións se o hai.
- Indica que debo comprobar eu, empezando pola corrección dos contidos.
