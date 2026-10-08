---
term_id: TERM-002F
preferred_name_nl: Ontologie
english_name: Ontology
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Semantic Web / knowledge representation
evidence_labels:
- A
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-066
related_term_ids:
- QLT-021
- TEC-011
- TERM-002E
- TERM-002G
- TERM-003A
- TERM-003B
status: active
---

# Ontologie

**Engelse term of afkorting:** Ontology  
**Term-ID:** `TERM-002F`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Semantic Web / knowledge representation  
**Bewijsbasis:** A  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een ontologie is een geformaliseerd model van begrippen binnen een domein, met definities van klassen, eigenschappen, relaties en soms logische beperkingen. Een ontologie maakt expliciet welke soorten dingen bestaan en hoe uitspraken daarover moeten worden geïnterpreteerd.

## Meer dan een woordenlijst

Een woordenlijst geeft termen en definities. Een taxonomie ordent begrippen meestal breder en smaller. Een ontologie kan daarnaast formeel vastleggen dat een scootmobiel een voertuig is, dat een model door een organisatie wordt geproduceerd, dat een bereikwaarde een eenheid heeft en dat bepaalde relaties alleen tussen specifieke typen mogen bestaan.

| Onderdeel | Voorbeeld | Functie |
| --- | --- | --- |
| Class | Scootmobielmodel | Definieert een soort entiteit. |
| Individual | On Four uitvoering X | Een concrete entiteit of instantie. |
| Object property | wordt geproduceerd door | Verbindt twee entiteiten. |
| Data property | heeft motorvermogen | Verbindt een entiteit met een waarde. |
| Restrictie | motorvermogen heeft een numerieke waarde en eenheid | Begrenst geldige uitspraken of inferenties. |

## Wat is bevestigd?

- W3C beschrijft ontologieën als geformaliseerde vocabularia die termen via hun relaties definiëren. [SRC-066]

- OWL 2 biedt klassen, eigenschappen, individuen en datawaarden met formeel gedefinieerde betekenis. [SRC-066]

- Een OWL-ontologie kan als RDF-graaf worden weergegeven, maar heeft rijkere semantische mogelijkheden dan een losse tripleverzameling. [SRC-066]

## Wat is niet bevestigd?

- Dat iedere begrippenlijst of categorieboom een formele ontologie is.

- Dat een website een OWL-ontologie moet publiceren om semantisch vindbaar te zijn.

- Dat meer formele complexiteit altijd betere data of content oplevert.

- Dat een ontologie zelf garandeert dat feitelijke waarden correct zijn.

## Praktische toepassing

1. Gebruik eerst een eenvoudige taxonomie en feitenstructuur wanneer formele logica niet nodig is.

2. Ontwerp een ontologie pas wanneer typen, relaties, validatie of hergebruik complex genoeg zijn.

3. Definieer termen, domein, bereik en beperkingen voordat data wordt gemigreerd.

4. Versiebeheer de ontologie en leg uit welke systemen en pagina’s ervan afhankelijk zijn.

## Veelgemaakte misvatting

Een ontologie is een grote lijst semantische zoekwoorden. Zij beschrijft juist formele begrippen, relaties en mogelijke beperkingen.

## Zie ook

Taxonomie, Knowledge Graph, RDF-triple, EAV, Schema.org en Data Quality.

## Verwante begrippen

- `QLT-021`: Data Quality
- `TEC-011`: Schema.org
- `TERM-002E`: Kennisgraaf
- `TERM-002G`: Taxonomie
- `TERM-003A`: RDF-triple
- `TERM-003B`: Entity-Attribute-Value (EAV)
- EAV *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-066
