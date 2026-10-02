# Instruccions per avaluar un recurs educatiu obert (avaluació VCER)

Aquestes instruccions procedeixen de la guia «Vibe coding responsable», per
publicar materials educatius creats amb vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/ca/).
Serveixen per avaluar un recurs ja fet, propi o d'una altra persona, s'hagi
creat o no seguint la guia.

## Com avaluar

- Treballa sobre el codi del recurs que et dono. Si no el tens, demana-me'l
  abans de començar.
- No el corregeixis: només avalua'l.
- Puntua cadascun dels deu punts amb 2, 1 o 0 segons la rúbrica VCER (vibe
  coding educatiu responsable), i justifica cada puntuació amb una frase
  sobre el que has vist al recurs.
- Si un punt no es pot comprovar amb el que t'he donat, deixa'l sense
  puntuar i digues què caldria per comprovar-lo.
- Abans de puntuar, fes un inventari complet, no una mostra: cada funció que
  demana o guarda dades de persones i com s'exporten o es copien; cada
  imatge, so, vídeo, icona i tipografia del projecte, i d'on surt (mira les
  imatges: un logotip redibuixat continua sent aliè); i tot el que es carrega
  de fora, i quan (en obrir, en prémer alguna cosa o en una finestra nova).
- Si el recurs està publicat, avalua aquella versió o comprova que coincideix
  amb el codi que t'han donat. Anota quina versió has avaluat: l'etiqueta de
  versió i el commit si és en un repositori, o l'adreça i la data de
  l'avaluació si no ho és.
- Per al punt 5, si pots executar codi, obre el recurs en un navegador i
  passa-li una eina automàtica d'accessibilitat, com axe-core, també amb
  contingut carregat i no només a la pantalla inicial. No comptis el que
  s'incrusta d'altres llocs. L'eina no comprova l'ús amb el teclat:
  recorre'l amb el tabulador. A la justificació del punt, digues què has
  provat i com; si només has pogut llegir el codi, indica-ho.

## Rúbrica VCER

1. CONTINGUT (eliminatori)
   2: No es detecten errors en el que ensenya: les dades, les definicions
      i les respostes que es donen per correctes.
   1: Hi ha alguna imprecisió menor en el que ensenya.
   0: Hi ha errors evidents en conceptes, dades o respostes.
   Aquesta puntuació només reflecteix els errors que has detectat: enumera'ls
   un per un i assenyala el que convé que comprovi una persona. Les errates i
   els errors de format de les referències no resten aquí: assenyala'ls a
   part.

2. DADES PERSONALS (eliminatori)
   2: No demana dades que identifiquin ningú, o les guarda només al
      dispositiu i permet exportar sense noms; o les envia únicament a un
      servei del centre, sense claus visibles al codi i de manera que només
      el docent o el centre les puguin llegir. No porta analítica.
   1: No envia dades de l'alumnat a serveis aliens, però guarda noms sense
      opció d'exportar sense ells, o l'enviament al servei del centre no
      està ben protegit (claus al codi, una adreça que permet llegir el que
      s'ha recollit).
   0: Envia dades de l'alumnat a un servidor aliè al centre, o porta
      analítica o seguiment.
   Si el recurs gestiona dades reals de l'alumnat, indica que convé la
   revisió d'una persona amb coneixements tècnics abans de fer-lo servir.
   El que es carrega o s'incrusta d'altres servidors (vídeos, àudios,
   tipografies, biblioteques) es valora al punt 4, no aquí.

3. ENTENDRE QUÈ FA
   2: Es pot descriure breument què fa, què guarda i amb què es comunica,
      i el que declara el material coincideix amb el codi.
   1: S'entén el seu funcionament, però hi ha parts de propòsit poc clar o
      no explica què guarda.
   0: Hi ha funcions o comunicacions el propòsit de les quals no es pot
      explicar, o el que declara no coincideix amb el codi.

4. DEPENDÈNCIES
   2: El que carrega o incrusta de fora procedeix de serveis coneguts i està
      anotat, i els textos, les imatges i les dades pròpies són dins del
      material.
   1: Carrega o incrusta recursos externs sense anotar-los, o una part del
      contingut propi (un vídeo, un àudio, un mapa) només és en una altra
      plataforma.
   0: El contingut principal depèn d'un servei extern, o carrega codi
      d'adreces desconegudes.

5. ACCESSIBILITAT
   2: Es fa servir sencer amb el teclat, els controls tenen etiqueta, les
      imatges text alternatiu, el contrast és suficient, no depèn del color
      i s'adapta a una pantalla estreta.
   1: Falla en un o dos d'aquests aspectes, sense impedir-ne l'ús.
   0: Falla en tres o més, o no es pot fer servir amb el teclat.

6. MATERIAL ALIÈ
   2: Cada element aliè indica autoria, procedència i llicència, i la
      llicència en permet la reutilització; o no hi ha material aliè.
   1: Hi ha material aliè amb llicència vàlida, però sense acreditar del
      tot.
   0: Hi ha material aliè sense llicència que en permeti la reutilització o
      sense cap atribució.

7. RASTRE
   2: Hi ha un registre o una nota amb les decisions importants i el seu
      motiu.
   1: Hi ha documentació que explica com està fet, però no per què.
   0: No hi ha res.

8. ÚS D'IA
   2: Indica que s'ha fet amb IA i què ha comprovat la persona.
   1: Indica que s'ha fet amb IA, sense dir què s'ha comprovat.
   0: No ho indica. Si consta que no es va fer servir IA, no es puntua.

9. LLICÈNCIA
   2: Autoria i llicència lliure visibles al material, amb enllaç. Si és un
      projecte de diversos fitxers, inclou el fitxer de llicència.
   1: Falta l'autoria o la llicència, la llicència no és lliure (NC o ND) o
      no enllaça al seu text.
   0: No indica ni autoria ni llicència.

10. REUTILITZACIÓ
   2: El codi es pot obtenir sencer, s'entén en llegir-lo, amb comentaris on
      calen, i hi ha indicacions per modificar-lo.
   1: Es pot obtenir, però és difícil d'entendre sense comentaris, està en
      part comprimit o no té indicacions.
   0: No es pot obtenir, o està ofuscat o comprimit.

## Resultat

- Calcula el percentatge: la suma de les puntuacions dividida pel màxim
  possible dels punts puntuats.
- Dona un resultat: «No recomanable» si el punt 1 o el 2 tenen 0, sigui quin
  sigui el percentatge; «Millorable» per sota del 70 %; «Recomanable» a partir
  del 70 %, sempre que els punts 1 i 2 s'hagin pogut puntuar i el punt 5 no
  tingui 0. Si algun dels punts 1 i 2 ha quedat sense puntuar, el resultat és
  «Millorable» i indica què falta per comprovar; si el punt 5 té 0, també és
  «Millorable» i indica què n'impedeix l'ús.
- Comença l'informe amb una línia com «Rúbrica VCER: Recomanable (85 %)»,
  seguida d'una altra amb la versió avaluada, i afegeix-hi a sota una frase
  amb el que significa aquest resultat:
  - Recomanable: compleix l'essencial de la guia i es pot utilitzar o
    publicar; les millores proposades el completen.
  - Millorable: té errors que convé corregir abans de publicar-lo o
    recomanar-lo, encara que cap no el descarta.
  - No recomanable: té errors evidents en el que ensenya o envia dades de
    l'alumnat a serveis aliens al centre; no convé utilitzar-lo ni
    publicar-lo fins a corregir-lo.
- A la justificació del punt 3, inclou aquesta descripció breu. A la del 4,
  enumera les adreces externes del codi i per a què serveix cadascuna, i
  digues amb paraules senzilles què deixaria de funcionar en obrir-lo
  descarregat en un ordinador sense internet. A la del 6, enumera el
  material aliè.
- Acaba amb les tres millores que més pujarien la puntuació.

## Si el recurs és meu

- Fes això només si el recurs és meu i pots modificar-ne els fitxers. Si no
  saps si és meu, pregunta-m'ho en acabar l'informe. Si és d'una altra
  persona o no en pots modificar els fitxers, no ho mencionis.
- Ofereix-me aquestes dues coses i fes només les que aprovi:
  - Si el projecte té una carpeta pròpia, com ara un repositori, desar
    l'informe complet en un fitxer anomenat evaluacion-vcer.md, que substitueix
    el d'una avaluació anterior.
  - Afegir al peu del material, en la seva llengua, una menció amb el
    resultat, com ara «Avaluació VCER de la versió 1.2: Recomanable (85 %),
    octubre de 2026», enllaçada a una adreça com aquesta:
    https://vibe-coding-educativo.github.io/vibe-responsable/vcer/?r=recomendable&p=85&f=2026-10&v=1.2&t=Fraccions%20equivalents&u=https%3A%2F%2Fejemplo.github.io%2Ffracciones%2F
- A l'enllaç, r és el resultat (recomendable, mejorable o no-recomendable,
  sempre en aquesta forma); p, el percentatge; f, l'any i el mes de
  l'avaluació; v, la versió avaluada; t, el títol del recurs, el mateix que
  figura al peu, i u, la seva adreça. Codifica t i u com es fa en una adreça
  web.
- Si el recurs no té número de versió, treu «de la versió 1.2» de la menció
  i v de l'enllaç. Si no està publicat al web, treu u de l'enllaç.
- El percentatge és opcional: ofereix-me la menció amb ell i sense. Sense
  percentatge, treu «(85 %)» de la menció i p de l'enllaç.
- Si ja hi ha una menció, actualitza-la amb el resultat nou.

## Si després et demano corregir-lo

- Abans de canviar res, digues-me què canviaries i espera que ho aprovi. No
  canviïs el contingut ni el funcionament, excepte si t'ho demano.
- Si no hi ha nota de decisions, escriu-ne una que descrigui com funciona el
  recurs ara, i indica que s'ha redactat després.
- Si falta la llicència o la indicació d'ús d'IA, prepara'm el text per
  afegir-lo.
