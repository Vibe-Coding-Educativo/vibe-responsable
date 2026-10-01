# Nola egin zen arrastoa gordetzea

## Erabaki bakoitzaren arrazoia

Adimen artifizialarekin (IA) oso azkar programatzen da, eta **aste gutxiren buruan inork ez du gogoratzen zergatik hartu zen erabaki bakoitza**. Ernesto Serranok, eXeLearning taldekoak, [«Inteligencia artificial: programar, documentar y no acabar en un berenjenal»](https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html) hitzaldian deskribatzen du: kodea hor dago, baina zergatia ez, eta inork ez du gogoratzen zer aukera baztertu ziren ezta zer argudiorekin ere. IAk ez du nahaste hori eragiten, baina lehenago iristea eragiten du.

Arrastoa gordetzeak hiru gauzatarako balio du. Denbora baten ondoren lana berriro hartzeko aukera ematen du, berreraiki beharrik gabe; jarraitu nahi duen beste pertsona bati azaltzeko aukera ematen du; eta arrazoi bat zuen erabaki bat fede onez desegitea saihesten du. Material hezitzaile ireki batean laugarren erabilgarritasun bat du, berrerabiltzen duten pertsonei nola egin zen erakusten baitie, eta hori da 8. gomendioko adierazpena osatzen duena.

## Erabakien erregistroa

Software-garapenean hori gordetzeko ohiko modua arkitektura-erabakien erregistroa da, edo ADR, ingelesezko izenaren siglengatik, *Architecture Decision Record*. Erabaki garrantzitsu bakoitza dokumentu labur batean jasotzen da, lau gauza biltzen dituena:

- **Testuingurua.** Erabakitzera behartzen duen egoera.
- **Erabakia.** Egiten dena, aplikatzeko adinako xehetasunarekin.
- **Baztertutako aukerak.** Bakoitza aukeratu ez zen arrazoiarekin; hori da geroago eztabaida errepikatzea saihesten duen zatia.
- **Ondorioak.** Zer hobetzen den eta zer okertzen den.

Balio izateari uzten dion erabaki bat ez da ezabatzen, berriak ordeztutako gisa markatzen da baizik, arrastoa gorde dadin. Hitzaldiak aurkezten duen proiektuan, erregistro bakoitzak, gainera, jasotzen du zein IA tresnarekin eta zein eredurekin hartu zen erabakia, eta horrek tresnaz aldatzeko aukera ematen du historia galdu gabe.

Proiektu berean, erregistro bakoitzak jasotzen ditu, halaber, erabakiaren oinarri den ebidentzia, arrisku ezagunak eta nola baliozkotu zen. Hitzaldiak «iturririk gabe, ez dago baieztapenik» arauan laburbiltzen du: datu bakoitzak dokumentazio ofizialera, kodearen bertsio zehatz batera edo edonork errepika dezakeen proba batera eramaten du. Zuhurtzia hori bereziki erabilgarria da IArekin, premisa faltsu batetik abiatzen den erabaki baten justifikazio sinesgarria idatz baitezake. Jasotako ebidentziari esker, pertsonak egiazta dezake lana berriro egin gabe. Egiaztatu ezin izan dena baliozkotzeko dagoen hipotesi gisa jasotzen da, inork gero egiaztatutako gertaeratzat har ez dezan.

## IAren lana eta pertsonarena

**Erregistroa ez da irakaslearentzako zeregin gehigarri bat**, IAk elkarrizketan erabakitzen denetik idazten baitu, eta pertsonak egiaztatzen du jasotakoa erabakitakoarekin bat datorrela. Hitzaldiak laburbiltzen du IAk proposatzen duela eta pertsonak erabakitzen duela.

Erregistroa ez da amaieran berreraikitzen ere, material bat egun desberdinetan banatutako lan-saio askotatik sortu ohi baita, eta elkarrizketa horiek gero berrosatzea ezinezkoa da. **Erregistroa erabakitzen den unean idazten da**, eta horregatik irauten du saioz saio. Programazio-agenteei behin adierazten zaie beren jarraibide-fitxategian, eta saio guztietan mantentzen dute. Komeni da bere izenez eskatzea, adibidez «eraman erabakien erregistro bat ADRekin», IAk formatua ezagutzen baitu eta azalpen gehiagorik gabe aplikatzen baitu. Txatbot baten weban, gutxienekoa da saio bakoitzaren amaieran IAri eskatzea egun horretako erabakiak gordetzen joaten den dokumentu batean jaso ditzala.

## Komunitateko adibide bat

expliCarlos izenez argitaratutako [«Elige tu IA»](https://explikarlos.github.io/elige-ia/) gida interaktiboak [erabakien erregistro](https://github.com/explikarlos/elige-ia/blob/main/docs/decisions/ADR-001-static-pages.md) bat du bere biltegian. Lehenak azaltzen du zergatik den aplikazioa estatikoa eta zergatik ez duen zerbitzaririk. Baztertutako aukeren artean datu-base bat dago, erantzunak sinkronizatzeko aukera emango zukeena, baina baztertu egin zen pribatutasun-arriskuak, kostua eta mantentze-lanak handitzen zituelako. Proiektu hori berriro hartzen duen edonork badaki, horrela, zerbitzaririk eza gogoeta egindako erabaki baten ondorioa dela.

Gida honek ere bere [erregistroa](https://github.com/Vibe-Coding-Educativo/vibe-responsable/tree/main/docs/adr) du, bere iturriei, bere webari eta bere adibideei buruzko erabakiak jasotzen dituena.
