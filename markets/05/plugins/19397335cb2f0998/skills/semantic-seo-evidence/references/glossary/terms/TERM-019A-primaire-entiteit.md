---
term_id: TERM-019A
preferred_name_nl: Primaire entiteit
english_name: Primary Entity / Main Entity
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Contentplanning / structured data / kennisrepresentatie
evidence_labels:
- A
- B
last_checked: '2026-07-25'
source_ids:
- SRC-028
- SRC-079
- SRC-089
related_term_ids:
- TEC-010
- TEC-011
- TERM-002
- TERM-019
status: active
---

# Primaire entiteit

**Engelse term of afkorting:** Primary Entity / Main Entity  
**Term-ID:** `TERM-019A`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Contentplanning / structured data / kennisrepresentatie  
**Bewijsbasis:** A en B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

De primaire entiteit is het specifieke ding of concept dat een pagina, passage, dataset of ander informatieobject hoofdzakelijk beschrijft. Andere entiteiten ondersteunen, kwalificeren, vergelijken of contextualiseren deze hoofdentiteit.

## Afbakening

Een pagina kan meerdere belangrijke entiteiten bevatten, maar meestal is er één hoofdobject waarop de belangrijkste claims en eigenschappen betrekking hebben. Bij een vergelijking kunnen juist twee of meer gelijkwaardige primaire objecten bestaan.

Schema.org definieert mainEntity als de primaire entiteit die in een pagina of ander CreativeWork wordt beschreven. Dit is een vocabulaire-eigenschap, geen bewijs van een Google-rankingfactor. [SRC-079]

Google geeft aan dat structured data zichtbaar, relevant en representatief voor de hoofdinhoud moet zijn. Correcte markering garandeert geen rich result of ranking. [SRC-089]

## Praktische toepassing

1. Formuleer de primaire entiteit zo specifiek als nodig is voor betrouwbare feiten.

2. Koppel claims alleen aan die uitvoering waarvoor bron, datum en voorwaarden gelden.

3. Gebruik secundaire entiteiten om de hoofdentiteit uit te leggen, niet om de focus ongemerkt te verschuiven.

4. Gebruik mainEntity alleen wanneer het schema en het paginatype dit inhoudelijk rechtvaardigen en de zichtbare tekst dezelfde entiteit beschrijft.

## Wat is niet bevestigd?

- Dat iedere pagina precies één primaire entiteit moet hebben.

- Dat mainEntity verplicht is voor Google Search of AI Search.

- Dat het toevoegen van mainEntity automatisch entiteitsbegrip, citaties of rankings oplevert.

## Praktijkvoorbeeld

| Onderdeel | Primaire entiteit | Secundaire entiteit | Waarom |
| --- | --- | --- | --- |
| Productuitleg | Specifiek scootmobielmodel en uitvoering | Accu, stoel, accessoire | De claims gaan hoofdzakelijk over dat model. |
| Vergelijking | Twee geselecteerde modellen | Meetmethode, gebruiker, route | Beide modellen worden gelijkwaardig beoordeeld. |
| Wettelijk artikel | Een concrete verkeersregel | Voertuigcategorie, land, datum | De regel is het hoofdonderwerp, niet een product. |

## Veelgemaakte misvatting

Primaire entiteit en meest gebruikte zoekwoord zijn hetzelfde. Een entiteit is een refereerbaar object of concept; een zoekwoord is een formulering die iemand gebruikt.

## Zie ook

- Central Entity

- Entiteit

- Entiteitsidentifier

- Schema.org

- Structured data

## Verwante begrippen

- `TEC-010`: Structured Data
- `TEC-011`: Schema.org
- `TERM-002`: Entiteit
- `TERM-019`: Central Entity
- Entiteitsidentifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-028, SRC-079, SRC-089
