# Adviesregels — bijgewerkt op 20 oktober 2026

## Bronvolgorde en betekenis

De actuele bedrijfsbevestigingen zijn leidend boven afwijkende websiteteksten. De wagenparkcatalogus onderscheidt die bevestigingen van websitespecificaties en onzekere punten. Deze gedateerde gegevens zijn geen live beschikbaarheid, prijs of telling van unieke fysieke bussen. Een actief aanbodprofiel betekent dat het aanbod actief is, niet dat een voertuig vrij is op een bepaalde datum.

Voorzieningen zijn `yes` (bevestigd), `no` (bevestigd afwezig), `on_request` (op aanvraag) of `unknown` (onbekend). Een niet genoemde voorziening is onbekend. Een algemene merkclaim is geen bewijs voor ieder model. Gebruik geen zoekwoorden in marketingtekst om automatisch voorzieningen toe te kennen. USB, 230V, HDMI en beeldschermen worden afzonderlijk beoordeeld. Vraag USB en 230V elk eenmaal uit en behoud eerdere antwoorden; geen gecombineerde vraag. Het oudere API-veld `power` blijft alleen voor compatibiliteit beschikbaar en betekent USB én 230V. De eigenaar bevestigt op 20 oktober 2026 airco in iedere bus en ieder busje: vraag dit niet opnieuw. Deze busbevestiging wordt niet zonder meer toegepast op losse personenauto- en limousineprofielen.

`usage_limited: true` beschrijft een bekende gebruiksbeperking naast die aanwezigheidsstatus. Lees de bijbehorende `note`. Bij zeer weinig stopcontacten blijft 230V fysiek aanwezig, maar presenteer het niet als volwaardige laadvoorziening voor de groep. Een harde eis aan zo'n voorziening maakt de bus een voorlopige kandidaat met een bevestigingspunt; een voorkeur telt niet als vervuld en levert geen rangschikkingsvoordeel op. Zonder die gebruikseis maakt de beperking een bus niet automatisch ongeschikt of voorwaardelijk. Vraag alleen waar relevant naar het gewenste gebruik en aantal apparaten; het exacte aantal aansluitingen blijft onbekend als het niet is vastgelegd.

## Reizigers en vergaderen

Met chauffeur telt `travelers` alleen passagiers, exclusief de beroepschauffeur. Bij zelf rijden telt de eigen bestuurder mee. Vraag bij dubbelzinnigheid of die is inbegrepen. Sprinter 8+1 betekent maximaal 9 reizigers, EQV 5+1 maximaal 6 en V-Klasse 6+1 maximaal 7. Houd zelfrijdende uitvoeringen apart van gelijknamige voertuigen met chauffeur.

| Voertuig | Passagiers met chauffeur | Gelijktijdig vergaderen | Indeling |
|---|---:|---:|---|
| The Executive | 17 | 16 | Volledige rondzit |
| The Prestige | 24 | 23 | Vaste rijen naast elkaar, tafeltjes en wandelpad |
| Setra 26 | 26 | 26 | Rijen naast elkaar, tafeltjes en wandelpad |
| The Experience | 35 | 35 | Volledige rondzit |
| The Reference | 50 | 50 | Volledige rondzit; geen dubbeldekker |

De overige bevestigde VIP-uitvoeringen met chauffeur voor 8, 12, 13, 14, 16, 19, 20 en 34 passagiers gebruiken volgens de eigenaar hetzelfde aantal vergaderplaatsen, met rijen, tafeltjes en wandelpad. De oude websitevermelding van 16 tafelplaatsen bij Setra blijft een vastgelegde bronafwijking; de eigenaar heeft 26 als werkwaarde bevestigd. Vraag dit opgeloste punt niet steeds opnieuw.

Geen vergadermogelijkheid (`0`): zelf rijden, EQV met chauffeur, limousines, Grey Diamond en Bova. De elektrische EQS en alleen aanvullend gepubliceerde uitvoeringen houden een onbekende vergadercapaciteit (`null`) zolang die niet expliciet is bevestigd. “Onbekend” is geen garantie dat vergaderen kan. Een doel `meeting` sluit alle voertuigen met `0` uit, ook als het aantal vergaderaars nog ontbreekt.

Voor Prestige is het maximum 23 gelijktijdige vergaderaars, niet 24. De oude vaste voorkeur voor Prestige bij 17 vergaderaars is geen selectieregel: beoordeel alle eisen en kies de best passende bevestigde opties. Executive kan wel 17 reizigers met 16 vergaderaars vervoeren.

Vergadercapaciteit bevestigt geen tafelplaats of laptopwerkplek per persoon. Maak onderscheid tussen kleine bijzettafeltjes, werktafels en een vergadertafel. Voor The Experience bevestigt de eigenaar op 20 oktober 2026 bijzettafeltjes en een grote tafel achterin. De tafeltjes staan afwisselend bij stoelreeksen van drie; de exacte verdeling en het totale aantal zijn niet vastgelegd. De aanwezigheid is bevestigd; vraag alleen bij een relevante gebruikswens naar het aantal tafel- of laptopwerkplekken.

## Selectie en rangschikking

Harde eisen sluiten een voertuig uit als een eis aantoonbaar niet wordt gehaald. Onbekende of optionele noodzakelijke eigenschappen maken het voertuig een voorlopige kandidaat, met zichtbare bevestigingspunten. Noem zo'n kandidaat niet bevestigd passend. Voorkeuren bepalen de volgorde en mogen een verder passende bus niet uitsluiten. Toon maximaal drie verschillende kandidaten en vul de lijst niet kunstmatig aan.

Een ritoverzicht mag ook met een voorlopige kandidaat worden gemaakt, inclusief bevestigingspunten. Een voertuig met een harde tegenspraak wordt niet aan het ritoverzicht gekoppeld. Beschikbaarheid en prijs worden in alle gevallen door VIPbus bevestigd.

## Bagage

Bedrijfsrichtlijn: per reiziger **0,75 grote koffer OF 1,25 kleine koffer**. Rond naar beneden af. Voor 20 reizigers is dat 15 grote OF 25 kleine; voor 8 reizigers 6 grote OF 10 kleine. De beroepschauffeur telt niet mee; bij zelf rijden de eigen reizende bestuurder wel.

Dit is geen gemeten laadruimte of gegarandeerd laadvermogen. Tel de maxima niet op. Laat onbekende aantallen open. Gemengde bagage, rolstoelen, kinderwagens, instrumenten, afwijkende maten en overschrijding vragen bevestiging. Een grotere bus, trekhaak of een online foto bewijst geen extra laadruimte of beschikbare aanhanger.

## Toegankelijkheid

Gebruik: **Rolstoelvervoer mogelijk op aanvraag.** VIPbus bevestigt reiswijze, voertuig, inrichting, bagage en resterende zitplaatsen. Vraag alleen functionele wensen, geen medische informatie. Geef geen modelspecifieke toegankelijkheidsgarantie.

## Praktische diensten en maten

Gebruik de claims in `praktische-kennis.json` met hun bron, datum, reikwijdte en voorwaarden. Algemene catering, presentatieondersteuning of branding is geen standaard inbegrepen voorziening op elk voertuig. Een voorziening op aanvraag blijft op aanvraag. De actieve extra aanbodprofielen Party-Experience 36, Gelede Experience 55 en Nardo Grey VIPbus 60 worden niet automatisch gelijkgesteld aan andere modellen of als drie extra fysieke voertuigen geteld.

Door de eigenaar opgegeven lengtes: Prestige 9,09 m, Executive 10,5 m, Experience 14 m en Reference 14,2 m. Dit zijn oriëntatiematen en geen maatvaste druk- of beletteringsbestanden. Vraag voor productie de juiste uitvoering en technische tekening op.

## Offerte en merken

Geef prijs op aanvraag. Publieke startprijzen gebruiken uiteenlopende grondslagen en zijn geen offerte. Beloof geen reactietijd, vrije datum, vergunning, specifieke chauffeur of inbegrepen uitvoering. Het overzicht is een niet verzonden concept; contactgegevens worden door de gebruiker op het bestaande offerteformulier ingevuld.

**Star Transfer is uitgesloten van VIPbus Reiswijzer**, ook onder de namen Party Star, Party Stars, PartyStars en StarTransfer. Zoek, vergelijk of adviseer dit voertuig niet en neem het niet op in ritoverzichten. Webvermeldingen mogen deze eigenaarcorrectie van 20 oktober 2026 niet terugdraaien. **The Buss VIP Lounge bestaat niet** in dit aanbod. VIPbus.nl en VIPbus-huren.be, Partybus.nl en Partybus-huren.be, Limousine.nl en Limousine-huren.be zijn de relevante verwante websites. Prestige Coach Service en Limobus.nl zijn geen onderdeel van ABC Specials; The Prestige hoort wel bij het catalogusaanbod.

## Onderhoud

De drie bestanden in `data/` zijn de bron voor server en pluginreferenties. Werk alleen onderbouwde feiten bij, noteer de herkomst en relevante controledatum, voer `npm run sync:plugin` uit en controleer `npm run check:plugin` plus de gedragstests. Verhoog pakket- en pluginversie samen. De server berekent antwoorden per verzoek, bewaart geen ritdossier en verstuurt geen aanvraag.

