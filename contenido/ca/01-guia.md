# Abans de publicar: deu recomanacions

## 1\. Revisar el contingut sense delegar-lo a la IA

La intel·ligència artificial (IA) es pot equivocar amb tota naturalitat, i un error en una simulació o en un qüestionari acaba sent un aprenentatge equivocat. Abans de publicar cal fer servir el material com ho faria l'alumnat i comprovar els conceptes, les dades i les respostes que dona per bones. Aquesta revisió no es pot delegar, ja que la responsabilitat del que s'ensenya és de la persona que ho publica.

- **El mínim.** Recórrer el material de principi a fi, també amb respostes equivocades, i revisar cada resultat amb el criteri de la matèria. Després de cada canvi important, repetir el recorregut amb una llista de comprovacions que pot redactar la mateixa IA, ja que una modificació petita pot espatllar una cosa que ja funcionava.
- **El recomanat.** Demanar a la IA que converteixi aquesta llista en proves automàtiques i les executi després de cada canvi.

## 2\. No enviar dades personals a serveis aliens al centre

El nom, les notes, la veu o la imatge de l'alumnat són dades personals. A Espanya, l'Agència Espanyola de Protecció de Dades indica a la seva [guia per a centres educatius](https://www.aepd.es/documento/guia-centros-educativos.pdf) que el professorat ha d'utilitzar les eines que el centre o l'administració hagin disposat, i que el contingut que un docent publica pel seu compte, al marge del centre, és responsabilitat seva. Altres països tenen normes diferents, però la precaució és la mateixa. La manera més senzilla de complir és que el material no demani dades. Quan una eina necessita identificar l'alumnat, com un quadern de qualificacions, les dades s'han de quedar al dispositiu del docent o en els sistemes que el centre hagi decidit utilitzar. Cal tenir una cura especial amb les plataformes que afegeixen amb facilitat comptes d'usuari i bases de dades, ja que aleshores les dades es guarden en servidors aliens.

- **El mínim.** No demanar noms reals ni res que identifiqui una persona, excepte si l'eina ho necessita per a la seva funció, i en aquest cas guardar-ho només al dispositiu. Preguntar a la IA si l'aplicació envia informació a algun servidor. Si el material s'obre dins d'una plataforma, cal comprovar si exigeix registre o una edat mínima abans d'enviar l'enllaç a l'alumnat, ja que se l'està portant al servei d'un tercer.
- **El recomanat.** Publicar el material en un lloc que l'alumnat pugui obrir sense registrar-se, i comprovar que el codi no conté adreces web de serveis que no es reconeguin. Quan el programa hagi de gestionar dades de l'alumnat en els sistemes del centre, la decisió correspon al centre, i convé una revisió tècnica abans de posar-lo en ús.

## 3\. Entendre què fa el material

Si ningú no entén com funciona un material, no es podrà corregir quan falli, i a la pràctica deixa de ser obert. Per complir aquest punt no cal saber programar, ja que n'hi ha prou de poder descriure breument què fa l'aplicació, què guarda i si es comunica amb algun servei extern.

- **El mínim.** Demanar a la IA que expliqui en llenguatge planer què fa l'aplicació i si guarda o envia alguna cosa, i comprovar que l'explicació coincideix amb el que s'observa en fer-la servir. Demanar també que el codi propi del material estigui comentat i sigui llegible, ja que el codi comprimit en línies interminables és motiu suficient per no publicar. Les biblioteques conegudes que s'hi incloguin són l'excepció, perquè se solen distribuir així.
- **El recomanat.** Afegir un document que expliqui com està organitzat el projecte i per a què serveix cada fitxer.

## 4\. No dependre de serveis que poden desaparèixer

Un recurs que incrusta contingut d'un altre web, o que carrega peces des de servidors aliens, deixa de funcionar quan aquests serveis canvien o tanquen. El mateix passa amb la plataforma on s'ha creat el material, ja que l'enllaç compartit dura el que l'empresa decideixi.

- **El mínim.** Guardar a l'ordinador propi una còpia del codi del material, i actualitzar-la quan canviï.
- **El recomanat.** Demanar a la IA que carregui de serveis coneguts el que el material necessiti de fora i ho anoti a la nota de decisions, i guardar dins del projecte les imatges, els textos i les dades pròpies.

## 5\. Fer-lo accessible a qualsevol persona

Els materials generats amb IA tendeixen al que és vistós, i els efectes decoratius solen ser un obstacle per a una part de l'alumnat. Un material accessible es fa servir sense ratolí, s'entén sense dependre del color i es llegeix bé en una pantalla petita.

- **El mínim.** Demanar a la IA des del principi que segueixi les pautes d'accessibilitat, i provar el resultat només amb el teclat, amb el text ampliat i en un telèfon.
- **El recomanat.** Demanar a la IA que revisi l'accessibilitat amb una eina automàtica i corregeixi el que detecti. Els agents de programació ho poden fer sense ajuda, ja que instal·len l'eina, l'executen i apliquen les correccions.

## 6\. Citar l'autoria del que es pren d'altres persones

Les imatges, els textos, els sons i les peces de programari que s'incorporen tenen autoria i llicència, encara que els hi hagi posat la IA. L'atribució ha d'anar dins del mateix material, perquè l'acompanyi quan circuli fora del seu context.

- **El mínim.** Indicar l'autoria, la procedència i la llicència de cada element aliè, i substituir els que no en permetin la reutilització.
- **El recomanat.** Revisar, a més, les llicències de les biblioteques de programari incloses, ja que algunes condicionen la llicència del conjunt.

## 7\. Guardar el rastre de com es va fer

Amb la IA s'avança molt de pressa, i al cap de poques setmanes ningú no recorda per què es va prendre cada decisió. Conservar aquest rastre permet reprendre la feina, explicar-la a una altra persona i no desfer per error el que tenia un motiu.

- **El mínim.** Mantenir un document amb les decisions importants i el seu perquè. El redacta la mateixa IA quan se li demana en acabar cada sessió de treball, i només cal revisar-lo i guardar-lo.
- **El recomanat.** Demanar a la IA que porti dins del projecte un registre de decisions o ADR, sigles en anglès d'*Architecture Decision Record* (registre de decisions d'arquitectura). La IA l'escriu a partir del que es decideix a la conversa, amb el context, les alternatives descartades i les conseqüències de cada decisió i, en les tècniques, en què es basa i com es va comprovar. Només cal revisar que el que s'ha anotat correspon al que s'ha decidit.

## 8\. Declarar l'ús d'IA i el que s'ha comprovat

En un material creat amb vibe coding el codi és obra de la IA, i el més habitual és que ningú no l'hagi revisat línia per línia. Les persones que el reutilitzin ho han de saber per decidir fins a quin punt se'n poden refiar. Per això convé indicar amb quina eina s'ha creat i, sobretot, què ha comprovat la persona que el publica, com la correcció dels continguts, el funcionament o el tractament de les dades.

- **El mínim.** Una o dues frases dins del material, al costat de la llicència, amb l'eina utilitzada i el que s'ha comprovat.
- **El recomanat.** La mateixa declaració a la documentació del projecte, amb un enllaç al registre de decisions del punt 7, que és el que explica com s'ha fet el material.

## 9\. Publicar amb una llicència lliure a la vista

Les obres queden protegides per drets d'autor de manera automàtica, de manera que un material sense llicència no es pot reutilitzar amb seguretat encara que estigui publicat. Una llicència lliure indica a les altres persones que poden fer-lo servir, adaptar-lo i compartir-lo, i amb quines condicions. El codi i els continguts necessiten llicències diferents, i el que genera la IA planteja dubtes d'autoria que es tracten al seu capítol.

- **El mínim.** Escriure l'autoria i la llicència dins del mateix material, en un lloc visible, per exemple al peu.
- **El recomanat.** Afegir el fitxer de llicència al projecte, amb una llicència de programari lliure per al codi, com AGPL v3 o MIT, i una Creative Commons (CC) lliure, com CC BY-SA o CC BY, per als continguts.

## 10\. Oferir el codi perquè altres persones l'adaptin

La llicència dona el permís, però el material s'ha de poder obtenir, a més, en una forma que permeti treballar-hi. D'aquesta manera una altra persona el pot adaptar a la seva aula sense demanar res a ningú.

- **El mínim.** Oferir el codi per copiar-lo o descarregar-lo, acompanyat de la nota de decisions del punt 7, de manera que una altra persona el pugui continuar.
- **El recomanat.** Publicar-lo en un repositori obert, amb una explicació de com fer-lo servir i com modificar-lo, i demanar a la IA que marqui cada versió publicada amb una etiqueta de versió, que permet recuperar després el codi exacte d'aquella versió.
