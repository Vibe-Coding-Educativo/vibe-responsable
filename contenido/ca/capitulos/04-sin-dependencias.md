# No dependre de serveis que poden desaparèixer

## Les dependències d'un material

Un material depèn d'un servei extern quan necessita alguna cosa que no és dins seu per funcionar. Les formes més corrents són el contingut incrustat des d'un altre web, les biblioteques de programació i les tipografies que es carreguen des de servidors aliens, i les connexions amb serveis en línia. També és una dependència la plataforma on s'ha creat el material, quan aquest només existeix dins seu.

Aquestes dependències no es veuen en fer servir el material. Es descobreixen en llegir el codi o en demanar a la intel·ligència artificial (IA) que les enumeri, que és el que demana el punt 4 de l'[avaluació VCER](para-la-ia.html#per-avaluar-un-recurs-ja-fet).

## Els canvis en els serveis externs

Un servei extern pot canviar les seves condicions, passar a ser de pagament o tancar, i el material que en depenia **deixa de funcionar sense que el seu autor hagi tocat res**. L'article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centre Nacional de Desenvolupament Curricular en Sistemes no Propietaris (CEDEC) dedica als recursos educatius oberts (REO), ho il·lustra amb el cas d'un recurs que incrusta un mapa interactiu d'una plataforma externa. Si la plataforma retira les presentacions gratuïtes, el recurs mostra un requadre en blanc, i el docent no en pot recuperar el contingut perquè no té el fitxer original. L'article recomana reservar el contingut incrustat per als vídeos i casos similars.

El risc no és només que el servei desaparegui. El 2024, el domini polyfill.io, des del qual més de cent mil llocs web carregaven una biblioteca molt utilitzada, va canviar de propietari i va començar a servir codi maliciós sense que les pàgines afectades haguessin modificat res, segons va documentar l'empresa de seguretat [Sansec](https://sansec.io/research/polyfill-supply-chain-attack). El mateix article del CEDEC adverteix d'un altre risc propi del codi generat per IA, que són les biblioteques inventades o suplantades per unes altres de nom gairebé idèntic.

## L'enllaç d'una plataforma

Quan el material s'ha creat al web d'un xatbot o en una plataforma per crear aplicacions, l'enllaç compartit dura el que l'empresa decideixi. Un canvi en el servei, en les seves condicions o en el compte del docent pot deixar aquest enllaç sense efecte, i amb ell totes les pàgines que l'hagin incrustat.

**El mínim és guardar a l'ordinador propi una còpia del codi del material** i actualitzar-la quan canviï. Amb aquesta còpia el material es pot recuperar, publicar en un altre lloc o continuar treballant-lo amb una altra eina. Perquè serveixi, el material ha de ser una pàgina que s'obri per si sola al navegador. Els xatbots més utilitzats, com ChatGPT, Gemini o Claude, generen sovint l'aplicació com un component de React, una biblioteca de programació molt estesa, que només funciona dins del seu propi web. Per això el [fitxer d'instruccions per a la IA](para-la-ia.html) els demana una pàgina HTML.

## El que es carrega de fora

Programar des de zero el que ja resol una biblioteca coneguda no és realista, i tampoc no ho és allotjar dins del material tot el que utilitza. Les biblioteques que mostren fórmules, gràfics o mapes, i les tipografies, es poden carregar de fora, sempre que procedeixin d'un servei conegut i en quedi constància. Un servei conegut tampoc no garanteix que es mantindrà igual, i per això convé comprovar què deixa de funcionar en obrir el material sense connexió.

El recomanat és demanar a la IA que carregui aquests recursos de serveis coneguts i que els anoti a la nota de decisions de la recomanació 7, amb la seva llicència. Aquesta llista no està pensada per al docent, sinó per arreglar o adaptar el material més endavant, una tasca que moltes vegades tornarà a fer una IA. El que no es pot recuperar d'un altre lloc, com les imatges, els textos i les dades pròpies, convé que sigui dins del material, o almenys guardat en una còpia, i no només incrustat des d'una altra plataforma.

Al docent li interessa sobretot una conseqüència pràctica: **si el material continuarà funcionant en obrir-lo descarregat en un ordinador sense internet**, per exemple en una aula sense connexió. La comprovació no requereix coneixements tècnics, ja que consisteix a obrir el material, desconnectar el dispositiu de la xarxa i tornar-lo a carregar. Un exemple és [Tantrix](https://felipsarroca.github.io/jocs/Tantrix/), un joc de Felip Sarroca que es pot instal·lar com a aplicació i funciona sense connexió després de la primera visita. L'avaluació VCER demana a la IA que ho expliqui amb paraules senzilles, del tipus «si l'obres sense internet, les fórmules no es veuran».
