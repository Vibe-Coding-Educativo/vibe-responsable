# Revisar el contingut sense delegar-lo a la IA

## Com s'equivoca la intel·ligència artificial

Els textos que genera la intel·ligència artificial (IA) sonen bé, les explicacions resulten convincents i les referències semblen reals. Tanmateix, de vegades són falsos. El risc no és en l'error evident, que qualsevol detecta, sinó en l'error versemblant: la data que gairebé és correcta, la cita que gairebé va existir, la dada que gairebé coincideix. Martín Núñez Calleja, del Centre Nacional de Desenvolupament Curricular en Sistemes no Propietaris (CEDEC), ho resumeix amb claredat a la seva ponència [«Crear REA con eXeLearning en tiempos de IA»](https://descargas.intef.es/cedec/formacion/SL_REA_IA_julio26/html/fiabilidad-del-contenido.html), dedicada als recursos educatius oberts (REO): **«A l'aula, un error que ningú no detecta no és un error: és un aprenentatge equivocat»**.

En un material interactiu el problema es multiplica, perquè l'error no es llegeix una vegada, sinó que es repeteix amb cada alumne que el fa servir. Un simulador amb una fórmula mal aplicada, un qüestionari que dona per bona una resposta incorrecta o una explicació que inverteix una relació de causa i efecte ensenyen aquest error tantes vegades com s'obri el material.

## Què es revisa en el material

Convé revisar el material complet abans de publicar-lo, i no només la part que s'ha demanat expressament. La comprovació abasta quatre aspectes:

- **Els continguts.** Els conceptes, les dades, les dates, les unitats i les fórmules que apareixen a les explicacions.
- **Les activitats.** Els enunciats, les opcions de resposta i, sobretot, quines es donen per correctes. Un distractor mal plantejat pot ser tan perjudicial com una resposta equivocada.
- **La retroacció.** El que el material respon quan l'alumnat s'equivoca, que només es veu si es proven respostes incorrectes.
- **El comportament en els casos extrems.** Què passa en deixar una resposta en blanc, en escriure un nombre negatiu, en introduir un valor enorme o en prémer dues vegades seguides.

La manera de fer-ho és recórrer el material com ho faria l'alumnat, també amb respostes equivocades, i no limitar-se a mirar la pantalla inicial. Molts errors només apareixen en arribar al final de l'activitat o en repetir-la.

## La revisió després de cada canvi

Amb la IA és fàcil modificar un material ja revisat, i aquesta facilitat té un risc. Un canvi que sembla petit, com afegir una pregunta o canviar el disseny, pot espatllar una altra part que ja funcionava, encara que aparentment no tingui relació amb el que s'ha demanat. Aquests errors es coneixen com a regressions, i la revisió inicial no els detecta, ja que es va fer sobre la versió anterior.

Per detectar-los, **la revisió es converteix en una llista de comprovacions que es repeteix després de cada canvi important**. La llista recull els recorreguts principals i els casos extrems que ja s'han comprovat, i la pot redactar la mateixa IA a partir del que s'ha provat. En un qüestionari, per exemple, podria ser la següent:

- El qüestionari es completa de principi a fi.
- Una resposta incorrecta mostra la retroacció prevista.
- Una resposta en blanc no produeix errors.
- En reiniciar, l'activitat torna a l'estat inicial.
- Funciona només amb el teclat.

Quan el projecte ho permet, la IA pot convertir aquestes comprovacions en proves automàtiques i executar-les després de cada canvi. Els agents de programació ho fan sense ajuda. Aquestes proves només confirmen que el material continua funcionant com abans, i la correcció del que ensenya continua depenent de la revisió descrita més amunt. La IA es pot encarregar de repetir les comprovacions, tot i que decidir quins comportaments s'han de conservar correspon a la persona que coneix el material.

## La responsabilitat pedagògica

La IA accelera la producció, però **la responsabilitat pedagògica continua sent de la persona que publica el material**. Així ho recull també la [«Guía sobre el uso de la inteligencia artificial en el ámbito educativo»](https://code.intef.es/wp-content/uploads/2026/09/ACTUALIZACI%C3%93N-GU%C3%8DA-DE-LA-IA-DEF-1-SEPT-2026-Publicable-v5.pdf) de l'Institut Nacional de Tecnologies Educatives i de Formació del Professorat (INTEF), en la seva versió 2.0 de setembre de 2026, que entre els seus principis ètics situa la supervisió humana i la responsabilitat: el professorat ha de mantenir el control sobre l'ús de la IA, i les decisions educatives no poden dependre de sistemes automatitzats.

Això té una conseqüència pràctica per a la resta de la guia. La IA es pot encarregar de gairebé totes les recomanacions, des de la llicència fins a l'accessibilitat, però no d'aquesta. Pot assenyalar què convé comprovar, i fins i tot advertir del que no està segura, però no pot certificar que el que ensenya el material sigui correcte. Per això, a l'[avaluació VCER](vcer.html), la IA puntua només els errors que detecta i assenyala el que ha de revisar la persona.

## La revisió després de publicar

La revisió no acaba en publicar. Les persones que fan servir el material troben errors que el seu autor no ha vist, perquè el proven amb un altre alumnat, en altres dispositius i amb altres preguntes. Per això convé donar-lo a conèixer en una comunitat docent i atendre els comentaris de les persones que el proven. Al grup de Telegram [Vibe Coding Educativo](https://t.me/vceduca), la secció «¡Comparte tu App!» està pensada per presentar els programes publicats, i els comentaris que reben serveixen per corregir-los i millorar-los.

## El valor didàctic del material

Que les dades siguin exactes és el mínim, no l'objectiu. Un material pot no contenir cap error i continuar sent pobre des del punt de vista didàctic. L'article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/) assenyala tres aspectes que cap codi no substitueix.

El primer és la claredat de l'objectiu d'aprenentatge, de manera que l'alumnat sàpiga en tot moment què s'espera que aprengui i per què. El segon és la retroacció formativa, que no consisteix només a indicar si una resposta és correcta, sinó a explicar-ne el motiu, oferir una pista i convidar a intentar-ho de nou. El tercer és la coherència metodològica, és a dir, que cada activitat respongui a una decisió didàctica i no al que la IA va proposar per defecte.

La pregunta que convé fer-se en revisar no és si el material ha quedat vistós, sinó si ajuda a aprendre millor. Aquesta valoració correspon a la persona que coneix la matèria i a l'alumnat, i és la seva aportació al vibe coding educatiu.
