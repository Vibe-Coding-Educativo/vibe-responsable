# Instruccions per a la IA

## Com s'utilitzen

Les recomanacions de la guia es poden donar directament a la intel·ligència artificial (IA), de manera que la feina de complir-les no recaigui sobre la persona. Per fer-ho hi ha dos fitxers, que es poden descarregar i utilitzar en qualsevol eina: un per crear un material i un altre per avaluar un recurs ja fet. Tots dos contenen només el que demana la guia; el que ha de fer el material es descriu a part, com sempre.

El fitxer per crear es lliura en començar:

- **Al web d'un xatbot**, s'adjunta al primer missatge, juntament amb la descripció del material que es vol crear i la indicació «segueix les instruccions del fitxer adjunt».
- **En un agent de programació o un editor de codi amb IA**, es desa a la carpeta del projecte com a fitxer d'instruccions, i la IA el té en compte en totes les sessions.
- **A les plataformes per crear aplicacions**, s'enganxa a les instruccions permanents del projecte, que moltes ofereixen a la configuració o com un fitxer del mateix projecte.

Si la IA no coneix l'autoria o el lloc on es publicarà el material, les mateixes instruccions li demanen que ho pregunti abans de començar. En acabar, s'adjunta a la mateixa conversa el [fitxer d'avaluació](#per-avaluar-un-recurs-ja-fet) que apareix més avall i es demana «avalua el material segons les instruccions». Després, si es demana «corregeix-lo», la IA proposa els canvis i espera que s'aprovin. Aquesta revisió no substitueix la de la persona, ja que el model també s'equivoca en revisar la seva pròpia feina.

## Per crear un material

Aquest és el fitxer que es lliura a la IA en començar a crear un material. Es pot descarregar per adjuntar-lo o per desar-lo a la carpeta del projecte, o copiar-ne el text per enganxar-lo al principi de la conversa.

<!-- instrucciones -->

## Per avaluar un recurs ja fet

El fitxer d'avaluació, que aplica l'avaluació VCER (vibe coding educatiu responsable), serveix per a qualsevol recurs ja publicat, propi o aliè, s'hagi creat o no amb la guia. Per avaluar un web:

1. Descarregar el fitxer d'avaluació que apareix a continuació i adjuntar-lo a la conversa amb la IA, o copiar-ne el text i enganxar-lo al principi.
2. Proporcionar el codi del recurs: adjuntar el fitxer HTML desat des del navegador, o enganxar el codi.
3. Demanar «avalua aquest recurs segons les instruccions».

<!-- evaluacion -->

La IA puntua cada recomanació amb la rúbrica VCER, dona un percentatge final i proposa les tres millores que més pujarien la puntuació. Si després se li demana corregir-lo, primer proposa els canvis i espera que s'aprovin; abans convé desar-ne una còpia. La puntuació orienta, però no substitueix la revisió de la persona, sobretot en la correcció del contingut, on la IA només detecta els errors que veu.

Aquesta és la rúbrica VCER, la que utilitza el fitxer d'avaluació anterior:

<!-- rubrica -->

El percentatge final és la suma de les puntuacions dividida pel màxim possible dels punts que la IA ha pogut comprovar. Amb aquest percentatge i amb els punts essencials s'obté un d'aquests tres resultats:

| Resultat | Quan es dona | Què significa |
| --- | --- | --- |
| **Recomanable** | 70 % o més, amb el contingut i les dades personals puntuats i sense un 0 en cap d'ells ni en l'accessibilitat | El recurs compleix l'essencial de la guia i es pot utilitzar o publicar. Les millores proposades el completen. |
| **Millorable** | Menys del 70 %, o quan no s'ha pogut comprovar el contingut o les dades personals, o l'accessibilitat té un 0 | El recurs té errors que convé corregir abans de publicar-lo o de recomanar-lo, encara que cap no el descarta. L'informe indica quins són i què falta per comprovar. |
| **No recomanable** | Un 0 en el contingut o en les dades personals, sigui quin sigui el percentatge | El recurs té errors evidents en el que ensenya o envia dades de l'alumnat a serveis aliens al centre. No convé utilitzar-lo amb l'alumnat ni publicar-lo fins a corregir-lo. |
