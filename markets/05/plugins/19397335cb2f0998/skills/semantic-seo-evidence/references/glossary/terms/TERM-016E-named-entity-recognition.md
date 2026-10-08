---
term_id: TERM-016E
preferred_name_nl: Named Entity Recognition
english_name: Named Entity Recognition (NER)
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Informatie-extractie en entiteitsverwerking
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-050
- SRC-061
related_term_ids:
- TERM-002
- TERM-016F
- TERM-016G
- TERM-016H
status: active
---

# Named Entity Recognition

**Engelse term of afkorting:** Named Entity Recognition (NER)  
**Term-ID:** `TERM-016E`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Informatie-extractie en entiteitsverwerking  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Named Entity Recognition is de taak waarbij een systeem tekstvermeldingen lokaliseert en aan een entiteitstype koppelt, bijvoorbeeld persoon, organisatie, locatie, product, datum of hoeveelheid.

## Uitgebreide uitleg

NER werkt op mentions, de concrete tekstfragmenten waarin mogelijk een entiteit wordt genoemd. Het systeem bepaalt meestal de grenzen van het fragment en een type. Het hoeft daarmee nog niet te weten welke unieke persoon, organisatie of productvariant wordt bedoeld.

Welke typen beschikbaar zijn hangt af van dataset, model en domein. Een algemeen model kan personen en locaties herkennen, terwijl een domeinmodel ook productmodellen, onderdelen, aandoeningen of technische eigenschappen kan labelen.

Fouten kunnen ontstaan in de grens van een mention, het gekozen type of het volledig missen van een mention. Merknamen die ook gewone woorden zijn, nieuwe productnamen en samengestelde Nederlandse termen kunnen extra lastig zijn.

Een Google Cloud-API geeft bijvoorbeeld entiteitsnamen, typen, mentions, metadata en salience terug. Dat is één productimplementatie en geen volledige beschrijving van Google Search.

## Belangrijke afbakening

| Stap | Vraag | Mogelijke uitkomst bij “Nipponia Pride” |
| --- | --- | --- |
| NER | Welk tekstdeel is een mention en welk type heeft het? | “Nipponia Pride” als product of organisatie/productcombinatie |
| Entity Linking | Aan welke bekende identifier kan de mention worden gekoppeld? | een product-ID in een knowledge base |
| Disambiguation | Welke kandidaat is hier bedoeld? | het scootmobielmodel en niet het algemene woord pride |
| Coreference | Welke andere woorden verwijzen naar dezelfde entiteit? | “dit model” of “de driewieler” |

## Voorbeeld

In “De For Motion On Four heeft een motor van 1000 watt” kan een NER- of domeinsysteem mentions vinden voor merk, model en hoeveelheid. Het systeem heeft daarmee nog niet bewezen dat de waarde correct is of bij de juiste uitvoering hoort.

## Wat is bevestigd?

- NER is een gevestigde sequence-labeling- of span-detectietaak.

- NER onderscheidt tekstvermeldingen en typen, maar is niet automatisch entity linking.

- Entiteitstypen en prestaties verschillen per model, taal en domein.

## Wat is niet bevestigd?

- Een correct geschreven productnaam wordt door ieder platform altijd als dezelfde entiteit herkend.

- Een hoge entiteitsdichtheid verbetert automatisch de ranking.

- NER valideert de waarheid van een productclaim.

## Praktische toepassing

- Gebruik officiële en consistente merknamen en modelnamen, vooral bij de eerste vermelding.

- Leg productvariant, eenheid en belangrijke identifier expliciet vast.

- Controleer geautomatiseerde entiteitsannotaties handmatig bij nieuwe, samengestelde of dubbelzinnige namen.

- Vermijd onnodige herhaling. Duidelijkheid is het doel, niet een vaste mentionfrequentie.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Zodra een systeem een naam als entiteit herkent, weet het ook exact welke entiteit wordt bedoeld. NER herkent doorgaans eerst een mention en type. Linking en disambiguation zijn aanvullende stappen. |
| --- |

## Zie ook

TERM-016F Entity Linking, TERM-016G Entity Disambiguation, TERM-016H Coreference Resolution, TERM-002 Entity.

## Verwante begrippen

- `TERM-002`: Entiteit
- `TERM-016F`: Entity Linking
- `TERM-016G`: Entity Disambiguation
- `TERM-016H`: Coreference Resolution

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-050, SRC-061
