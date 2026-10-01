# Instruccions per crear un material educatiu obert

Aquestes instruccions procedeixen de la guia «Vibe coding responsable», per
publicar materials educatius creats amb vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/ca/).
Segueix-les en tota la feina, juntament amb el que et demani sobre el
material que vull crear. El material es publicarà en obert, perquè altres
persones el puguin utilitzar i adaptar.

## Abans de començar

Si no t'ho he dit, pregunta'm:
- L'autoria que hi ha de figurar (un nom o un nom d'usuari).
- On es publicarà: el web d'un xatbot, una plataforma per crear aplicacions,
  o un repositori o un lloc propi.

## Com s'ha de construir

- Llicència: CC BY-SA 4.0 per als continguts i AGPL v3 per al codi, excepte
  si t'indico unes altres.
- Si treballem al web d'un xatbot, fes el material com una pàgina HTML que
  funcioni per si sola en obrir-la al navegador, i no com un component que
  només funciona dins del xatbot.
- Pots utilitzar biblioteques, tipografies i altres recursos externs quan
  estalviïn feina o millorin el resultat. Carrega'ls d'un servei conegut i
  estable, i anota'ls a la nota de decisions, amb la seva llicència. Si alguna
  part del material deixaria de funcionar en obrir-lo descarregat en un
  ordinador sense internet, digues-m'ho amb paraules senzilles, per exemple:
  «si l'obres sense internet, les fórmules no es veuran».
- Dades personals: no demanis el nom ni cap dada que identifiqui una persona,
  excepte si l'eina ho necessita per a la seva funció, com un quadern de
  notes. En aquest cas guarda-ho només al dispositiu i ofereix l'opció
  d'exportar o imprimir sense els noms. Si el programa recull respostes de
  l'alumnat, mostra el resultat en acabar o permet descarregar-lo per
  lliurar-lo, i identifica cada persona amb un codi en lloc del seu nom. No
  enviïs res a cap servidor ni afegeixis analítica o comptadors de visites.
- Accessible, seguint les Pautes d'Accessibilitat per al Contingut Web
  (WCAG): utilitzable només amb el teclat, amb un ordre de tabulació lògic,
  etiquetes als controls, textos alternatius a les imatges, contrast
  suficient, sense dependre del color per entendre res i llegible a la
  pantalla d'un mòbil.
- Codi llegible i comentat en la llengua del material, sense comprimir, amb
  noms de variables comprensibles.
- Al peu del material: el títol, l'autoria, la llicència amb el seu enllaç i
  una declaració breu d'ús d'IA, amb l'eina, el mes i l'any, i el que jo hagi
  comprovat (pregunta-m'ho abans de publicar).
- Si incorpores imatges, sons o fragments de codi d'altres persones, utilitza
  només material la llicència del qual en permeti la reutilització, i indica'n
  l'autoria, la procedència i la llicència dins del mateix material.
- Si el programa ha de guardar dades de l'alumnat en els sistemes del centre,
  no escriguis claus ni contrasenyes al codi que arriba al navegador, fes que
  només el docent o el centre puguin llegir el que s'ha recollit i indica'm
  què ha de revisar una persona amb coneixements tècnics abans de posar-lo en
  ús.
- Després de cada canvi, torna a comprovar el que ja funcionava: executa les
  proves si n'hi ha o, si no ho pots fer, digues-me quines comprovacions he
  de repetir.

## Si es publica en un repositori o en un lloc propi

- Afegeix un fitxer LICENSE amb la llicència del codi i un altre amb la dels
  continguts, i indica la llicència al principi de cada fitxer de codi amb
  una línia SPDX-License-Identifier.
- Afegeix un document que expliqui com està organitzat el projecte i per a
  què serveix cada fitxer.
- Porta un registre de decisions (ADR) dins del projecte, amb un fitxer per
  decisió que reculli el context, les alternatives descartades i les
  conseqüències. Anota-hi cada decisió que prenguem, sense esperar que t'ho
  demani. En les decisions tècniques, anota també en què et bases
  (documentació oficial, una versió concreta del codi o una prova que es
  pugui repetir), els riscos coneguts i com ho has comprovat. No inventis
  fonts ni proves: el que no hagis pogut comprovar, marca-ho com a hipòtesi
  pendent de validació.
- Revisa l'accessibilitat amb una eina automàtica i corregeix el que detecti.
- Quan publiquem una versió, marca-la amb una etiqueta de versió (v1.0,
  v1.1…) i no moguis ni reutilitzis després una etiqueta ja publicada.

## Quan acabis el material

- Descriu breument què fa el material, què guarda i si es comunica amb algun
  servei extern.
- Prepara una llista breu de comprovacions amb els recorreguts principals i
  els casos extrems, per repetir-la després de cada canvi. Si el projecte ho
  permet, converteix-la en proves automàtiques.
- Escriu una nota breu amb les decisions importants que has pres i el motiu
  de cadascuna, o resumeix-les del registre de decisions si n'hi ha.
- Indica què he de comprovar jo, començant per la correcció dels continguts.
