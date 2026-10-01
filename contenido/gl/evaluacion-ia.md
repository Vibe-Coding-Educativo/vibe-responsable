# Instrucións para avaliar un recurso educativo aberto (avaliación VCER)

Estas instrucións proceden da guía «Vibe coding responsable», para publicar
materiais educativos creados con vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/gl/).
Serven para avaliar un recurso xa feito, propio ou doutra persoa, creado ou
non seguindo a guía.

## Como avaliar

- Traballa sobre o código do recurso que che dou. Se non o tes, pídemo antes
  de comezar.
- Non o corrixas: só avalíao.
- Puntúa cada un dos dez puntos con 2, 1 ou 0 segundo a rúbrica VCER (vibe
  coding educativo responsable), e xustifica cada puntuación cunha frase
  sobre o que viches no recurso.
- Se un punto non se pode comprobar co que che dei, déixao sen puntuar e di
  que faría falta para comprobalo.
- Antes de puntuar, fai inventario completo, non unha mostra: cada función
  que pide ou garda datos de persoas e como se exportan ou copian; cada
  imaxe, son, vídeo, icona e tipografía do proxecto, e de onde sae (mira as
  imaxes: un logotipo redebuxado segue sendo alleo); e todo o que se carga de
  fóra, e cando (ao abrir, ao premer algo ou nunha xanela nova).
- Se o recurso está publicado, avalía esa versión ou comproba que coincide
  co código que che deron. Anota que versión avaliaches: a etiqueta de
  versión e o commit se está nun repositorio, ou o enderezo e a data da
  avaliación se non o está.
- Para o punto 5, se podes executar código, abre o recurso nun navegador e
  pásalle unha ferramenta automática de accesibilidade, como axe-core, tamén
  con contido cargado e non só na pantalla inicial. Non contes o que se
  incrusta doutros sitios. A ferramenta non comproba o manexo co teclado:
  percórreo co tabulador. Na xustificación do punto, di que probaches e
  como; se só puideches ler o código, indícao.

## Rúbrica VCER

1. CONTIDO (eliminatorio)
   2: Non se detectan erros no que ensina: os datos, as definicións e as
      respostas que se dan por correctas.
   1: Hai algunha imprecisión menor no que ensina.
   0: Hai erros evidentes en conceptos, datos ou respostas.
   Esta puntuación só reflicte os erros que detectaches: enuméraos un por
   un e sinala o que convén que comprobe unha persoa. As gralladas e os
   fallos de formato das referencias non restan aquí: sinálaos á parte.

2. DATOS PERSOAIS (eliminatorio)
   2: Non pide datos que identifiquen a ninguén, ou gárdaos só no
      dispositivo e permite exportar sen nomes; ou envíaos unicamente a un
      servizo do centro, sen claves visibles no código e de forma que só o
      docente ou o centro poidan lelos. Non leva analítica.
   1: Non envía datos do alumnado a servizos alleos, pero garda nomes sen
      opción de exportar sen eles, ou o envío ao servizo do centro non está
      ben protexido (claves no código, un enderezo que permite ler o
      recollido).
   0: Envía datos do alumnado a un servidor alleo ao centro, ou leva
      analítica ou seguimento.
   Se o recurso manexa datos reais do alumnado, indica que convén a
   revisión dunha persoa con coñecementos técnicos antes de usalo.
   O que se carga ou se incrusta doutros servidores (vídeos, audios,
   tipografías, bibliotecas) valórase no punto 4, non aquí.

3. ENTENDER QUE FAI
   2: Pode describirse brevemente que fai, que garda e con que se comunica,
      e o que declara o material coincide co código.
   1: Enténdese o seu funcionamento, pero hai partes de propósito pouco
      claro ou non explica que garda.
   0: Hai funcións ou comunicacións cuxo propósito non se pode explicar, ou
      o que declara non coincide co código.

4. DEPENDENCIAS
   2: O que carga ou incrusta de fóra procede de servizos coñecidos e está
      anotado, e os textos, as imaxes e os datos propios están dentro do
      material.
   1: Carga ou incrusta recursos externos sen anotalos, ou parte do contido
      propio (un vídeo, un audio, un mapa) só está noutra plataforma.
   0: O contido principal depende dun servizo externo, ou carga código de
      enderezos descoñecidos.

5. ACCESIBILIDADE
   2: Manéxase enteiro co teclado, os controis teñen etiqueta, as imaxes
      texto alternativo, o contraste é suficiente, non depende da cor e
      adáptase a unha pantalla estreita.
   1: Falla nun ou dous deses aspectos, sen impedir o seu uso.
   0: Falla en tres ou máis, ou non se pode usar co teclado.

6. MATERIAL ALLEO
   2: Cada elemento alleo indica autoría, procedencia e licenza, e a
      licenza permite reutilizalo; ou non hai material alleo.
   1: Hai material alleo con licenza válida, pero sen acreditar de todo.
   0: Hai material alleo sen licenza que permita reutilizalo ou sen
      ningunha atribución.

7. RASTRO
   2: Hai un rexistro ou unha nota coas decisións importantes e o seu
      motivo.
   1: Hai documentación que explica como está feito, pero non por que.
   0: Non hai nada.

8. USO DE IA
   2: Indica que se fixo con IA e que comprobou a persoa.
   1: Indica que se fixo con IA, sen dicir que se comprobou.
   0: Non o indica. Se consta que non se usou IA, non se puntúa.

9. LICENZA
   2: Autoría e licenza libre visibles no material, con ligazón. Se é un
      proxecto de varios ficheiros, inclúe o ficheiro de licenza.
   1: Falta a autoría ou a licenza, a licenza non é libre (NC ou ND) ou non
      ligazona ao seu texto.
   0: Non indica nin autoría nin licenza.

10. REUTILIZACIÓN
   2: O código pode obterse completo, enténdese ao lelo, con comentarios
      onde fan falta, e hai indicacións para modificalo.
   1: Pode obterse, pero é difícil de entender sen comentarios, está en
      parte comprimido ou non ten indicacións.
   0: Non pode obterse, ou está ofuscado ou comprimido.

## Resultado

- Calcula a porcentaxe: a suma das puntuacións dividida entre o máximo
  posible dos puntos puntuados.
- Dá un resultado: «Non recomendable» se o punto 1 ou o 2 teñen 0, sexa cal
  sexa a porcentaxe; «Mellorable» por debaixo do 70 %; «Recomendable» a
  partir do 70 %, sempre que os puntos 1 e 2 se puidesen puntuar e o punto
  5 non teña 0. Se algún dos puntos 1 e 2 quedou sen puntuar, o resultado é
  «Mellorable» e indica que falta por comprobar; se o punto 5 ten 0, tamén é
  «Mellorable» e indica que impide usalo.
- Comeza o informe cunha liña como «Rúbrica VCER: Recomendable (85 %)»,
  seguida doutra coa versión avaliada, e engade debaixo unha frase co que
  significa ese resultado:
  - Recomendable: cumpre o esencial da guía e pode utilizarse ou
    publicarse; as melloras propostas complétano.
  - Mellorable: ten fallos que convén corrixir antes de publicalo ou
    recomendalo, aínda que ningún o descarta.
  - Non recomendable: ten erros evidentes no que ensina ou envía datos do
    alumnado a servizos alleos ao centro; non convén utilizalo nin
    publicalo ata corrixilo.
- Na xustificación do punto 3, inclúe esa breve descrición. Na do 4,
  enumera os enderezos externos do código e para que serve cada un, e di con
  palabras sinxelas que deixaría de funcionar ao abrilo descargado nun
  ordenador sen internet. Na do 6, enumera o material alleo.
- Remata coas tres melloras que máis subirían a puntuación.

## Se despois che pido corrixilo

- Antes de cambiar nada, dime que cambiarías e agarda a que o aprobe. Non
  cambies o contido nin o funcionamento, agás que cho pida.
- Se non hai nota de decisións, escribe unha que describa como funciona o
  recurso agora, e indica que se redactou despois.
- Se falta a licenza ou a indicación de uso de IA, prepárame o texto para
  engadilo.
