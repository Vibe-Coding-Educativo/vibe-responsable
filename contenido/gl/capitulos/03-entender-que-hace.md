# Entender que fai o material

## A comprensión do código

Un recurso educativo é aberto cando outra persoa pode descargalo, comprendelo, modificalo e melloralo. O artigo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que o Centro Nacional de Desenvolvemento Curricular en Sistemas non Propietarios (CEDEC) dedica aos recursos educativos abertos (REA), advirte de que un recurso con centos de liñas de código que ninguén entende, nin sequera a persoa que as inseriu, deixou de ser aberto no esencial, aínda que a súa licenza diga o contrario. No seu relatorio [«Crear REA con eXeLearning en tiempos de IA»](https://descargas.intef.es/cedec/formacion/SL_REA_IA_julio26/html/la-ia-y-el-codigo.html), Martín Núñez Calleja exprésao así: «Temos o código fonte. Pero non a comprensión».

O problema é práctico, xa que un material que funciona hoxe pode deixar de facelo tras unha actualización do navegador, e se ninguén entende como está feito, tampouco se poderá corrixir. O mesmo artigo propón unha regra sinxela: **se non se pode explicar en dúas frases que fai o código, o recurso aínda non está listo para publicarse**.

## Unha breve descrición do material

Cumprir esta recomendación non esixe saber programar, xa que abonda con poder dicir con palabras correntes tres cousas do material: **que fai, que garda e se se comunica con algún servizo externo**. Unha explicación deste tipo sería a seguinte: «O simulador calcula a aceleración dun corpo nun plano inclinado a partir do ángulo e do material escollidos, e debuxa as forzas. Non garda ningún dato nin se conecta con ningún servizo».

A forma de obtela é pedirlla á propia IA, en linguaxe sinxela, e comprobar despois que coincide co que se observa ao usar o material. Se a intelixencia artificial (IA) afirma que non se garda nada e o material lembra as respostas do día anterior, a explicación non é correcta e hai que aclaralo antes de publicar. A [avaliación VCER](para-la-ia.html#para-avaliar-un-recurso-xa-feito) inclúe esta petición no seu punto 3.

## Catro comprobacións sen saber programar

O artigo do CEDEC propón catro preguntas para detectar un código problemático sen necesidade de entendelo liña por liña:

- **Se se pode ler.** Un código lexítimo ten palabras recoñecibles, espazos e liñas de lonxitude razoable. Unha liña de centos de caracteres sen espazos, con letras e números mesturados, indica que o código está ofuscado.
- **Se fai referencia a enderezos externos.** Convén buscar os enderezos web que aparecen no código e investigar os que non se recoñezan.
- **Se pide permisos.** O acceso á cámara, ao micrófono, á localización ou ao portapapeis só é aceptable cando o material o xustifica cunha finalidade pedagóxica clara.
- **Se o seu autor pode explicalo.** É a regra das dúas frases.

As catro poden encargarse á IA, que pode localizar no código os enderezos e os permisos. O mesmo artigo resume estes criterios nun semáforo que clasifica o código en seguro, de risco moderado e perigoso.

## O código lexible e comentado

O código xerado por IA sen comentarios funciona como unha caixa negra. Cando inclúe comentarios en linguaxe natural, outras persoas poden comprendelo, modificalo e mantelo con maior facilidade. Convén pedilo desde o principio, cos comentarios no idioma do material e con nomes de variables comprensibles. Un exemplo é o [simulador do plano inclinado con rozamento](https://onio72.github.io/iesmajuelo/bach/fq1/planoincroz/), de Antonio González García, cuxo código está nun único ficheiro, dividido en seccións rotuladas e comentado en castelán.

**O código comprimido en liñas interminables é motivo suficiente para non publicar**, coa excepción das bibliotecas coñecidas, que adoitan distribuírse así. Cando o material é un proxecto con varios ficheiros, convén engadir un documento que explique como está organizado e para que serve cada un. Así o fai Pablo G. Guízar no [repositorio do seu Quiz del Sistema Solar](https://github.com/PabloGGuizar/quiz), que describe a arquitectura do programa, o percorrido dos datos e a función de cada ficheiro.
