---
term_id: TERM-002C
preferred_name_nl: Entiteitsidentifier
english_name: Entity Identifier
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Data- en kennisbeheer
evidence_labels:
- A
- B
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-044
- SRC-061
- SRC-065
related_term_ids:
- TEC-013
- TEC-014
- TEC-021
- TERM-002
- TERM-003A
- TERM-016F
status: active
---

# Entiteitsidentifier

**Engelse term of afkorting:** Entity Identifier  
**Term-ID:** `TERM-002C`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Data- en kennisbeheer  
**Bewijsbasis:** A en B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een entiteitsidentifier is een stabiele, binnen een afgesproken namespace unieke verwijzing naar een entiteit. Een identifier helpt verschillende namen, vermeldingen, pagina’s en gegevensrecords aan dezelfde bedoelde entiteit te koppelen.

## Naam, URL en identifier zijn niet automatisch hetzelfde

Een naam is leesbaar maar kan veranderen of dubbelzinnig zijn. Een URL kan een identifierfunctie hebben, maar kan ook alleen een tijdelijke locatie zijn. Een interne product-ID, GTIN, Knowledge Graph MID, URI of andere sleutel kan een entiteit stabieler aanduiden, mits het bereik en de eigenaar van de identifier duidelijk zijn.

| Identifiervorm | Sterk punt | Risico of grens |
| --- | --- | --- |
| Interne ID | Volledig beheerbaar binnen de organisatie | Niet vanzelf bruikbaar buiten het eigen systeem. |
| URI of @id | Kan als web- of graphidentifier worden gebruikt | Stabiliteit en canonical beleid moeten worden bewaakt. |
| Productcode of GTIN | Herkenbaar in handel en productdata | Alleen bruikbaar wanneer officieel en variantcorrect. |
| Knowledge-base-ID | Koppelt aan een externe kennisbron | Externe dekking, beleid en beschikbaarheid zijn niet beheersbaar. |

## Wat is bevestigd?

- RDF gebruikt IRIs om resources te identificeren. [SRC-001]

- SKOS-concepten kunnen met URI’s ondubbelzinnig worden geïdentificeerd. [SRC-044]

- Google Knowledge Graph API kan entiteiten via ID’s en typen teruggeven. [SRC-065]

- Google Cloud Entity Analysis kan bij bekende entiteiten metadata zoals een Knowledge Graph MID leveren. [SRC-061]

## Wat is niet bevestigd?

- Dat één identifier overal universeel geldig of herkend is.

- Dat iedere URL automatisch een stabiele entiteitsidentifier vormt.

- Dat het toevoegen van @id of sameAs een zoekmachine dwingt een entiteitskoppeling te accepteren.

- Dat twee gelijknamige productrecords zonder variantcontrole mogen worden samengevoegd.

## Praktische toepassing

1. Ken ieder merk, model, variant, accessoire en organisatieobject een stabiele interne ID toe.

2. Bewaar alternatieve namen en externe identifiers als eigenschappen van dezelfde record.

3. Verandert een URL, behoud dan de entiteits-ID en leg de migratie vast.

4. Controleer altijd of een productidentifier bij de juiste variant, uitvoering en markt hoort.

## Veelgemaakte misvatting

De zichtbare productnaam is voldoende als unieke identifier. Namen kunnen dubbel zijn, wijzigen of op meerdere varianten slaan.

## Zie ook

Entiteit, Entity Linking, RDF-triple, @id, sameAs, Product Variant en Canonical URL.

## Verwante begrippen

- `TEC-013`: @id
- `TEC-014`: sameAs
- `TEC-021`: Canonical URL
- `TERM-002`: Entiteit
- `TERM-003A`: RDF-triple
- `TERM-016F`: Entity Linking
- Product Variant *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-044, SRC-061, SRC-065
