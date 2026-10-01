# Oferir el codi perquè altres persones l'adaptin

## L'obertura a la pràctica

La llicència lliure dona el permís per reutilitzar un material, però **el permís resulta insuficient si el material no es pot obtenir en una forma que permeti treballar-hi**. La [Recomanació sobre els Recursos Educatius Oberts (REO)](https://www.unesco.org/es/legal-affairs/recommendation-open-educational-resources-oer) de l'Organització de les Nacions Unides per a l'Educació, la Ciència i la Cultura (UNESCO) no parla només d'accés, sinó de reutilització, reconversió, adaptació i redistribució. El programari lliure ho planteja de manera semblant amb les seves [quatre llibertats](https://www.gnu.org/philosophy/free-sw.ca.html), entre les quals hi ha la d'estudiar com funciona el programa i canviar-lo, i la de distribuir còpies de les versions modificades, per a les quals l'accés al codi és una condició necessària. La [Declaració sobre el coneixement lliure](https://wikieducator.org/Declaration_on_libre_knowledge) estén la mateixa idea a qualsevol recurs de coneixement: és lliure quan qualsevol el pot utilitzar per a qualsevol finalitat, aprendre'n, copiar-lo, adaptar-lo i compartir el resultat en benefici de la comunitat.

L'article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/), del Centre Nacional de Desenvolupament Curricular en Sistemes no Propietaris (CEDEC), ho concreta en un principi de simplicitat adaptable, segons el qual convé preferir el que és funcional i senzill al que és complex i tancat, i el criteri de qualitat d'un recurs és que es pugui reutilitzar.

## L'obtenció del material

El mínim és que el material ofereixi el seu codi per copiar-lo o descarregar-lo. Al web d'un xatbot i a les plataformes per crear aplicacions normalment es pot veure el codi, però les altres persones només reben un enllaç, de manera que convé afegir al mateix material la manera d'obtenir-lo, o publicar-lo a part. Juntament amb el codi convé oferir la nota de decisions de la recomanació 7, que permet a una altra persona continuar-lo sense haver d'endevinar per què està fet així.

El recomanat és publicar el projecte en un repositori obert, amb una explicació de com fer-lo servir i com modificar-lo. Un repositori permet, a més, que altres persones proposin millores i que l'autor les incorpori.

En un repositori el codi continua canviant després de publicar-se, de manera que l'enllaç al projecte porta sempre a la versió més recent. Per recuperar més endavant la versió exacta que es va publicar, es va fer servir a classe o es va avaluar, **convé marcar cada versió publicada amb una etiqueta de versió**, o *tag* en la terminologia de Git, com v1.0 o v1.1. La crea la IA en publicar, i n'hi ha prou d'indicar-l'hi una vegada a les seves instruccions. Una etiqueta ja publicada no es mou ni es reutilitza, perquè deixaria d'assenyalar el que es va publicar. Al seu costat es pot anotar l'identificador del *commit*, el codi que Git assigna a cada estat desat del projecte, que serveix de referència exacta encara que l'etiqueta es canviés per error.

## Un material fàcil d'adaptar

**Un material és més reutilitzable quan el contingut està separat del funcionament**. Un qüestionari les preguntes del qual són en una llista al principi del codi, o en un fitxer a part, es pot adaptar a una altra matèria canviant aquesta llista, sense tocar la resta. Convé demanar-ho a la intel·ligència artificial (IA) des del principi, juntament amb el codi comentat de la recomanació 3 i l'absència de dependències de la recomanació 4, que són les altres dues condicions que faciliten l'adaptació.

També ajuda indicar a la documentació quines parts estan pensades per canviar-se, com els textos, els colors o la llengua. Una persona que vulgui traduir el material, o ajustar-lo a un altre nivell educatiu, troba així per on començar.
