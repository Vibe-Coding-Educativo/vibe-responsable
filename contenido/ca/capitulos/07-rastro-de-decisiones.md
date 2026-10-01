# Guardar el rastre de com es va fer

## El motiu de cada decisió

Amb la intel·ligència artificial (IA) es programa molt de pressa, i **al cap de poques setmanes ningú no recorda per què es va prendre cada decisió**. Ernesto Serrano, de l'equip d'eXeLearning, ho descriu a la seva ponència [«Inteligencia artificial: programar, documentar y no acabar en un berenjenal»](https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html): el codi hi és, però el perquè no, i ningú no recorda quines alternatives es van descartar ni amb quins arguments. La IA no causa aquest desordre, però fa que arribi abans.

Conservar el rastre serveix per a tres coses. Permet reprendre la feina al cap d'un temps sense haver de reconstruir-la, permet explicar-la a una altra persona que la vulgui continuar, i evita desfer de bona fe una decisió que tenia un motiu. En un material educatiu obert té una quarta utilitat, ja que mostra a les persones que el reutilitzen com es va fer, que és el que completa la declaració de la recomanació 8.

## El registre de decisions

La manera habitual de conservar-lo en el desenvolupament de programari és el registre de decisions d'arquitectura, o ADR, per les sigles del seu nom en anglès, *Architecture Decision Record*. Cada decisió important s'anota en un document breu que recull quatre coses:

- **El context.** La situació que obliga a decidir.
- **La decisió.** El que es fa, amb el detall suficient per aplicar-ho.
- **Les alternatives descartades.** Cadascuna amb el motiu pel qual no es va triar, que és la part que evita repetir el debat més endavant.
- **Les conseqüències.** El que millora i el que empitjora.

Una decisió que deixa de valer no s'esborra, sinó que es marca com a substituïda per la nova, de manera que el rastre es conserva. Al projecte que presenta la ponència, cada registre anota, a més, amb quina eina d'IA i amb quin model es va prendre la decisió, cosa que permet canviar d'eina sense perdre la història.

En aquest mateix projecte, cada registre recull també l'evidència en què es basa la decisió, els riscos coneguts i la manera com es va validar. La ponència ho resumeix en la regla «sense font no hi ha afirmació»: cada dada remet a la documentació oficial, a una versió concreta del codi o a una prova que qualsevol pot repetir. Aquesta precaució és especialment útil amb IA, ja que pot redactar una justificació convincent d'una decisió que parteix d'una premissa falsa. L'evidència anotada permet a la persona comprovar-la sense refer la feina. El que no s'ha pogut verificar s'anota com a hipòtesi pendent de validació, de manera que ningú no ho prengui després per un fet comprovat.

## La feina de la IA i la de la persona

**El registre no suposa una tasca afegida per al docent**, ja que l'escriu la IA a partir del que es decideix a la conversa, i la persona comprova que el que s'ha anotat correspon al que s'ha decidit. La ponència ho resumeix dient que la IA proposa i la persona disposa.

El registre tampoc no es reconstrueix al final, ja que un material sol sortir de moltes sessions de treball repartides en dies diferents, i recompondre després aquestes converses resulta inviable. **El registre s'escriu en el moment en què es decideix**, i per això resisteix el pas de les sessions. Als agents de programació se'ls indica una vegada al seu fitxer d'instruccions, i el mantenen en totes. Convé demanar-lo pel seu nom, per exemple «porta un registre de decisions amb ADR», ja que la IA coneix el format i l'aplica sense més explicacions. Al web d'un xatbot, el mínim és demanar en acabar cada sessió que la IA anoti les decisions d'aquell dia en un document que es va desant.

## Un exemple de la comunitat

La guia interactiva [«Elige tu IA»](https://explikarlos.github.io/elige-ia/), publicada com a expliCarlos, porta al seu repositori un [registre de decisions](https://github.com/explikarlos/elige-ia/blob/main/docs/decisions/ADR-001-static-pages.md). El primer explica per què l'aplicació és estàtica i no té servidor. Entre les alternatives descartades hi figura una base de dades, que hauria permès sincronitzar les respostes, però que es va descartar perquè augmentava els riscos de privacitat, el cost i el manteniment. Qualsevol persona que reprengui aquest projecte sap així que l'absència de servidor respon a una decisió meditada.

Aquesta guia porta també el seu propi [registre](https://github.com/Vibe-Coding-Educativo/vibe-responsable/tree/main/docs/adr), que recull les decisions sobre les seves fonts, el seu web i els seus exemples.
