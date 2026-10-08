---
term_id: ENT-010
preferred_name_nl: Entity Resolution
english_name: Entity Resolution
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Datamanagement / kennisrepresentatie
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-025
- SRC-052
- SRC-120
related_term_ids:
- QLT-021
- TERM-002
- TERM-016F
- TERM-016G
status: active
---

# Entity Resolution

**Engelse term of afkorting:** Entity Resolution  
**Term-ID:** `ENT-010`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Datamanagement / kennisrepresentatie  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Entity Resolution is het proces waarbij wordt bepaald welke records, namen, profielen of vermeldingen naar dezelfde echte entiteit verwijzen en welke juist afzonderlijk moeten blijven.

## Afbakening

Het begrip is breder dan Entity Linking. Entity Linking koppelt een tekstvermelding meestal aan een bekende entiteit in een externe kennisbank. Entity Resolution kan ook records binnen of tussen eigen databronnen samenvoegen, bijvoorbeeld twee schrijfwijzen van hetzelfde scootmobielmodel of twee klantrecords van dezelfde persoon.

## Wat is bevestigd?

- Wetenschappelijke literatuur behandelt Entity Resolution en record linkage als methoden voor het herkennen en samenvoegen van records die dezelfde werkelijke entiteit beschrijven.

- De uitkomst hangt af van identifiers, kenmerken, context, datakwaliteit en de gekozen beslisregels.

## Wat is niet bevestigd?

- Dat dezelfde naam automatisch dezelfde entiteit betekent.

- Dat Entity Resolution door alleen een merknaam vaker te herhalen betrouwbaar wordt uitgevoerd.

## Praktische toepassing

1. Leg stabiele identifiers, officiële namen, varianten en voorgangers vast.

2. Gebruik meerdere kenmerken om records te vergelijken, zoals merk, modelcode, bouwjaar en accuconfiguratie.

3. Bewaar twijfelgevallen als afzonderlijke records totdat voldoende bewijs beschikbaar is.

## Voorbeeld

De namen “On Four 32 km/u” en “For Motion On Four, 1000 W, lithium” kunnen naar dezelfde uitvoering verwijzen. Zonder modelcode, bouwjaar en accu-informatie mag dit niet automatisch worden aangenomen.

## Veelgemaakte misvatting

Entity Resolution is niet hetzelfde als alle vergelijkbaar klinkende namen samenvoegen. Een verkeerde samenvoeging verspreidt juist foutieve eigenschappen over meerdere entiteiten.

## Zie ook

- Entiteit

- Entity Linking

- Entity Disambiguation

- Entiteitsidentifier

- Datakwaliteit

## Verwante begrippen

- `QLT-021`: Data Quality
- `TERM-002`: Entiteit
- `TERM-016F`: Entity Linking
- `TERM-016G`: Entity Disambiguation
- Entiteitsidentifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-025, SRC-052, SRC-120

**Update-trigger:** Nieuwe identifierstandaarden, gewijzigde productnamen of conflicten tussen databronnen.
