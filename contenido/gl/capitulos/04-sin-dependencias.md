# Non depender de servizos que poden desaparecer

## As dependencias dun material

Un material depende dun servizo externo cando necesita algo que non está dentro del para funcionar. As formas máis correntes son o contido incrustado doutra web, as bibliotecas de programación e as tipografías que se cargan desde servidores alleos, e as conexións con servizos en liña. Tamén é unha dependencia a plataforma onde se creou o material, cando este só existe dentro dela.

Estas dependencias non se ven ao usar o material. Descóbrense ao ler o código ou ao pedirlle á intelixencia artificial (IA) que as enumere, que é o que pide o punto 4 da [avaliación VCER](para-la-ia.html#para-avaliar-un-recurso-xa-feito).

## Os cambios nos servizos externos

Un servizo externo pode cambiar as súas condicións, pasar a ser de pagamento ou pechar, e o material que dependía del **deixa de funcionar sen que o seu autor tocase nada**. O artigo [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que o Centro Nacional de Desenvolvemento Curricular en Sistemas non Propietarios (CEDEC) dedica aos recursos educativos abertos (REA), ilústrao co caso dun recurso que incrusta un mapa interactivo dunha plataforma externa. Se a plataforma retira as presentacións gratuítas, o recurso mostra un recadro en branco, e o docente non pode recuperar o contido porque non ten o ficheiro orixinal. O artigo recomenda reservar o contido incrustado para os vídeos e casos semellantes.

O risco non é só que o servizo desapareza. En 2024, o dominio polyfill.io, desde o que máis de cen mil sitios web cargaban unha biblioteca moi utilizada, cambiou de propietario e comezou a servir código malicioso sen que as páxinas afectadas modificasen nada, segundo documentou a empresa de seguridade [Sansec](https://sansec.io/research/polyfill-supply-chain-attack). O mesmo artigo do CEDEC advirte doutro risco propio do código xerado por IA, que son as bibliotecas inventadas ou suplantadas por outras de nome case idéntico.

## A ligazón dunha plataforma

Cando o material se creou na web dun chatbot ou nunha plataforma para crear aplicacións, a ligazón compartida dura o que a empresa decida. Un cambio no servizo, nas súas condicións ou na conta do docente pode deixar esa ligazón sen efecto, e con ela todas as páxinas que a incrustasen.

**O mínimo é gardar no propio ordenador unha copia do código do material** e actualizala cando cambie. Con esa copia o material pode recuperarse, publicarse noutro sitio ou seguir traballándose con outra ferramenta. Para que sirva, o material ten que ser unha páxina que se abra por si soa no navegador. Os chatbots máis utilizados, como ChatGPT, Gemini ou Claude, xeran a miúdo a aplicación como un compoñente de React, unha biblioteca de programación moi estendida, que só funciona dentro da súa propia web. Por iso o [ficheiro de instrucións para a IA](para-la-ia.html) pídelles unha páxina HTML.

## O que se carga de fóra

Programar desde cero o que xa resolve unha biblioteca coñecida non é realista, e tampouco o é aloxar dentro do material todo o que utiliza. As bibliotecas que mostran fórmulas, gráficos ou mapas, e as tipografías, poden cargarse de fóra, sempre que procedan dun servizo coñecido e quede constancia delas. Un servizo coñecido tampouco garante que vaia manterse igual, e por iso convén comprobar que deixa de funcionar ao abrir o material sen conexión.

O recomendado é pedirlle á IA que cargue estes recursos de servizos coñecidos e que os anote na nota de decisións da recomendación 7, coa súa licenza. Esa lista non está pensada para o docente, senón para arranxar ou adaptar o material máis adiante, unha tarefa que moitas veces volverá facer unha IA. O que non se pode recuperar doutro sitio, como as imaxes, os textos e os datos propios, convén que estea dentro do material, ou polo menos gardado nunha copia, e non só incrustado desde outra plataforma.

Ao docente interésalle sobre todo unha consecuencia práctica: **se o material seguirá funcionando ao abrilo descargado nun ordenador sen internet**, por exemplo nunha aula sen conexión. A comprobación non require coñecementos técnicos, xa que consiste en abrir o material, desconectar o dispositivo da rede e volver cargalo. Un exemplo é [Tantrix](https://felipsarroca.github.io/jocs/Tantrix/), un xogo de Felip Sarroca que pode instalarse como aplicación e funciona sen conexión despois da primeira visita. A avaliación VCER pídelle á IA que o explique con palabras sinxelas, do tipo «se o abres sen internet, as fórmulas non se verán».
