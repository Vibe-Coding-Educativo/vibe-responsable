# Entendre què fa el material

## La comprensió del codi

Un recurs educatiu és obert quan una altra persona el pot descarregar, comprendre, modificar i millorar. L'article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), que el Centre Nacional de Desenvolupament Curricular en Sistemes no Propietaris (CEDEC) dedica als recursos educatius oberts (REO), adverteix que un recurs amb centenars de línies de codi que ningú no entén, ni tan sols la persona que les va inserir, ha deixat de ser obert en l'essencial, encara que la seva llicència digui el contrari. A la seva ponència [«Crear REA con eXeLearning en tiempos de IA»](https://descargas.intef.es/cedec/formacion/SL_REA_IA_julio26/html/la-ia-y-el-codigo.html), Martín Núñez Calleja ho expressa així: «Tenim el codi font. Però no la comprensió».

El problema és pràctic, ja que un material que funciona avui pot deixar de fer-ho després d'una actualització del navegador, i si ningú no entén com està fet, tampoc no es podrà corregir. El mateix article proposa una regla senzilla: **si no es pot explicar en dues frases què fa el codi, el recurs encara no està llest per publicar-se**.

## Una descripció breu del material

Complir aquesta recomanació no exigeix saber programar, ja que n'hi ha prou de poder dir amb paraules corrents tres coses del material: **què fa, què guarda i si es comunica amb algun servei extern**. Una explicació d'aquest tipus seria la següent: «El simulador calcula l'acceleració d'un cos en un pla inclinat a partir de l'angle i del material triats, i dibuixa les forces. No guarda cap dada ni es connecta amb cap servei».

La manera d'obtenir-la és demanar-la a la mateixa IA, en llenguatge planer, i comprovar després que coincideix amb el que s'observa en fer servir el material. Si la intel·ligència artificial (IA) afirma que no es guarda res i el material recorda les respostes del dia anterior, l'explicació no és correcta i cal aclarir-ho abans de publicar. L'[avaluació VCER](para-la-ia.html#per-avaluar-un-recurs-ja-fet) inclou aquesta petició al seu punt 3.

## Quatre comprovacions sense saber programar

L'article del CEDEC proposa quatre preguntes per detectar un codi problemàtic sense necessitat d'entendre'l línia per línia:

- **Si es pot llegir.** Un codi legítim té paraules reconeixibles, espais i línies de longitud raonable. Una línia de centenars de caràcters sense espais, amb lletres i nombres barrejats, indica que el codi està ofuscat.
- **Si fa referència a adreces externes.** Convé buscar les adreces web que apareixen al codi i investigar les que no es reconeguin.
- **Si demana permisos.** L'accés a la càmera, al micròfon, a la ubicació o al porta-retalls només és acceptable quan el material ho justifica amb una finalitat pedagògica clara.
- **Si el seu autor el pot explicar.** És la regla de les dues frases.

Totes quatre es poden encarregar a la IA, que pot localitzar al codi les adreces i els permisos. El mateix article resumeix aquests criteris en un semàfor que classifica el codi en segur, de risc moderat i perillós.

## El codi llegible i comentat

El codi generat per IA sense comentaris funciona com una caixa negra. Quan inclou comentaris en llenguatge natural, altres persones el poden comprendre, modificar i mantenir amb més facilitat. Convé demanar-ho des del principi, amb els comentaris en la llengua del material i amb noms de variables comprensibles. Un exemple és el [simulador del pla inclinat amb fregament](https://onio72.github.io/iesmajuelo/bach/fq1/planoincroz/), d'Antonio González García, el codi del qual és en un únic fitxer, dividit en seccions retolades i comentat en castellà.

**El codi comprimit en línies interminables és motiu suficient per no publicar**, amb l'excepció de les biblioteques conegudes, que se solen distribuir així. Quan el material és un projecte amb diversos fitxers, convé afegir un document que expliqui com està organitzat i per a què serveix cadascun. Així ho fa Pablo G. Guízar al [repositori del seu Quiz del Sistema Solar](https://github.com/PabloGGuizar/quiz), que descriu l'arquitectura del programa, el recorregut de les dades i la funció de cada fitxer.
