# L'avaluació VCER

## Què és l'avaluació VCER

VCER són les sigles de «vibe coding educatiu responsable». És l'avaluació que proposa la guia «Vibe coding responsable» per comprovar si un recurs educatiu compleix l'essencial de la guia abans de publicar-lo o d'utilitzar-lo. Serveix per a qualsevol recurs ja fet, propi o aliè, tant si s'ha creat seguint la guia com si no.

L'avaluació la fa una IA a partir d'un [fitxer d'instruccions](#com-avaluar-un-recurs) que es descarrega de la guia. La IA revisa el codi del recurs, puntua cada punt de la rúbrica amb 2, 1 o 0, justifica cada puntuació i proposa les tres millores que més pujarien el resultat.

## Com es calcula el resultat

El percentatge és la suma de les puntuacions dividida pel màxim possible dels punts que la IA ha pogut comprovar. El contingut i les dades personals són eliminatoris. Amb el percentatge i aquests dos punts s'obté un d'aquests tres resultats:

| Resultat | Quan es dona | Què significa |
| --- | --- | --- |
| **Recomanable** | 70 % o més, amb el contingut i les dades personals puntuats i sense un 0 en cap d'ells ni en l'accessibilitat | El recurs compleix l'essencial de la guia i es pot utilitzar o publicar. Les millores proposades el completen. |
| **Millorable** | Menys del 70 %, o quan no s'ha pogut comprovar el contingut o les dades personals, o l'accessibilitat té un 0 | El recurs té errors que convé corregir abans de publicar-lo o de recomanar-lo, encara que cap no el descarta. L'informe indica quins són i què falta per comprovar. |
| **No recomanable** | Un 0 en el contingut o en les dades personals, sigui quin sigui el percentatge | El recurs té errors evidents en el que ensenya o envia dades de l'alumnat a serveis aliens al centre. No convé utilitzar-lo amb l'alumnat ni publicar-lo fins a corregir-lo. |

## Límits de l'avaluació

La IA només detecta els errors que veu, sobretot en el contingut, i el resultat pot variar segons el model utilitzat. Per això la puntuació és orientativa i no substitueix la revisió d'una persona. A més, el resultat correspon a la versió del recurs que es va avaluar, en la data de l'avaluació.

## Com avaluar un recurs

El fitxer d'avaluació, que apareix a continuació, es dona a la IA juntament amb el recurs que es vol avaluar, i se li demana «avalua aquest recurs segons les instruccions». La manera de donar-l'hi depèn d'on sigui el recurs:

- **Si s'ha creat al web d'un xatbot o en una plataforma per crear aplicacions**, s'adjunta el fitxer, o se n'enganxa el text, a la mateixa conversa, quan el material està acabat.
- **Si és en una carpeta de l'ordinador o en un repositori**, es dona el fitxer a un agent de programació o a un editor de codi amb IA obert en aquesta carpeta. És la manera més completa, perquè la IA pot llegir tots els fitxers del projecte i, si pot executar codi, provar el recurs al navegador.
- **Si només es té el web publicat**, propi o aliè, s'obre una conversa amb la IA i s'hi adjunten el fitxer d'avaluació i el codi de la pàgina, desat des del navegador. Si el web està format per diversos fitxers, la IA només veurà els que se li donin, de manera que convé obtenir el codi complet, per exemple del seu repositori, i avaluar-lo com en el cas anterior.

<!-- evaluacion -->

La IA puntua cada recomanació amb la rúbrica VCER, dona un percentatge final i proposa les tres millores que més pujarien la puntuació. Si després se li demana corregir-lo, primer proposa els canvis i espera que s'aprovin; abans convé desar-ne una còpia. Si el recurs és propi, la IA ofereix a més desar l'informe al projecte i afegir al peu del material una menció amb el resultat, enllaçada a aquesta pàgina.

## La rúbrica VCER

Cada punt de la rúbrica comprova una de les recomanacions de la guia, que es desenvolupa en el seu capítol. Aquesta és la rúbrica que utilitza el fitxer d'avaluació:

<!-- rubrica -->
