---
term_id: TEC-012
preferred_name_nl: JSON-LD
english_name: JSON for Linking Data / JSON-LD
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: W3C-standaard / serialisatie
evidence_labels:
- A
last_checked: '2026-07-25'
source_ids:
- SRC-096
- SRC-097
related_term_ids:
- TEC-010
- TEC-011
- TEC-013
- TEC-014
- TERM-003A
status: active
---

# JSON-LD

**Engelse term of afkorting:** JSON for Linking Data / JSON-LD  
**Term-ID:** `TEC-012`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** W3C-standaard / serialisatie  
**Bewijsbasis:** A  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

JSON-LD is een W3C-standaard om linked data en semantische relaties in JSON-vorm uit te drukken.

## Afbakening

Met een context, typen, properties en identifiers kan gewone JSON aan een gedeeld datamodel worden gekoppeld. Google raadt JSON-LD voor veel structured-data-implementaties aan, maar de inhoud blijft bepalend.

## Wat is bevestigd?

- JSON-LD 1.1 is een W3C Recommendation.

- JSON-LD kan entiteiten met @id verbinden en vocabulairetermen via @context interpreteren.

## Wat is niet bevestigd?

- Dat JSON-LD door iedere zoekmachine hetzelfde wordt verwerkt.

- Dat technisch geldige JSON-LD onjuiste of onzichtbare claims acceptabel maakt.

## Praktische toepassing

1. Gebruik één consistente bron voor zichtbare gegevens en JSON-LD.

2. Geef entiteiten stabiele @id-waarden wanneer dit inhoudelijk nuttig is.

3. Valideer syntax en ondersteunde properties per platform.

## Voorbeeld

Een Organization-object kan een vaste @id krijgen en vanuit LocalBusiness- of Product-markering worden hergebruikt.

## Veelgemaakte misvatting

JSON-LD is een serialisatievorm, geen op zichzelf staand inhoudelijk kwaliteitsbewijs.

## Zie ook

- Structured Data

- Schema.org

- @id

- sameAs

- RDF-triple

## Verwante begrippen

- `TEC-010`: Structured Data
- `TEC-011`: Schema.org
- `TEC-013`: @id
- `TEC-014`: sameAs
- `TERM-003A`: RDF-triple

## Bronnen en actualiteit

**Kernbronnen:** SRC-096, SRC-097

**Update-trigger:** Nieuwe JSON-LD-standaard of gewijzigde platformondersteuning.
