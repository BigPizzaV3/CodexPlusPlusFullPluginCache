---
term_id: TERM-002E
preferred_name_nl: Kennisgraaf
english_name: Knowledge Graph
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Knowledge representation / Semantic Web
evidence_labels:
- A
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-064
- SRC-065
- SRC-066
related_term_ids:
- TERM-002
- TERM-002F
- TERM-002G
- TERM-003A
- TERM-006
- TERM-020A
status: active
---

# Kennisgraaf

**Engelse term of afkorting:** Knowledge Graph  
**Term-ID:** `TERM-002E`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Knowledge representation / Semantic Web  
**Bewijsbasis:** A, B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een kennisgraaf is een graafgestructureerde kennisrepresentatie waarin entiteiten of andere knooppunten via getypeerde relaties en eigenschappen met elkaar zijn verbonden. Een kennisgraaf kan identifiers, typen, waarden, provenance en schema-informatie bevatten.

## Basiselementen

| Element | Functie | Voorbeeld |
| --- | --- | --- |
| Knooppunt | Stelt een entiteit, concept of soms een waarde voor | On Four, For Motion, Lithiumaccu. |
| Relatie of edge | Verbindt twee knooppunten met een betekenisvol predicaat | On Four wordt geproduceerd door For Motion. |
| Eigenschap | Beschrijft een kenmerk of waarde | Motorvermogen 1000 watt. |
| Type of class | Plaatst een entiteit in een categorie | On Four is een scootmobielmodel. |
| Identifier | Maakt een knooppunt stabiel aanspreekbaar | Interne URI of product-ID. |
| Provenance | Legt herkomst en verantwoordelijkheid vast | Fabrikantsdocument of eigen meetrapport. |

Een kennisgraaf kan met RDF-triples worden uitgedrukt, maar niet iedere kennisgraaf gebruikt exact RDF of OWL. Omgekeerd is een netwerk van webpagina’s niet automatisch een kennisgraaf. De termen beschrijven verschillende informatielagen.

## Wat is bevestigd?

- Google beschreef de Knowledge Graph als een model van dingen, feiten en onderlinge relaties. [SRC-064]

- Google’s openbare Knowledge Graph API beschrijft real-world entities als knooppunten en noemt diverse entiteitstypen. [SRC-065]

- RDF biedt een standaard om graafuitspraken als triples te representeren. [SRC-001]

- OWL kan formele klassen, eigenschappen en logische relaties aan een kennisrepresentatie toevoegen. [SRC-066]

## Wat is niet bevestigd?

- Dat iedere website met interne links een knowledge graph is.

- Dat iedere kennisgraaf volledig correct, actueel of conflictvrij is.

- Dat Google’s interne Knowledge Graph volledig via de openbare API kan worden gezien.

- Dat structured data een organisatie automatisch in een specifieke interne knowledge graph opneemt.

- Dat meer triples automatisch betere rankings opleveren.

## Praktische toepassing

1. Gebruik stabiele entiteits-ID’s en duidelijke typen.

2. Leg relaties met expliciete predicaten vast, niet alleen als vage “gerelateerd aan”-links.

3. Voeg bron, datum, voorwaarden en zekerheid aan belangrijke feiten toe.

4. Valideer productvarianten en tegenstrijdige waarden voordat records worden samengevoegd.

5. Gebruik een kennisgraaf als beheermodel wanneer hergebruik, consistentie en relaties werkelijk nodig zijn.

## Veelgemaakte misvatting

Een Semantic Content Network is hetzelfde als een knowledge graph. Een contentnetwerk organiseert publicaties en gebruikersroutes; een kennisgraaf representeert entiteiten en getypeerde kennisrelaties.

## Zie ook

RDF-triple, Entiteit, Entiteitsidentifier, Ontologie, Taxonomie, Provenance en Semantic Content Network.

## Verwante begrippen

- `TERM-002`: Entiteit
- `TERM-002F`: Ontologie
- `TERM-002G`: Taxonomie
- `TERM-003A`: RDF-triple
- `TERM-006`: Semantisch contentnetwerk
- `TERM-020A`: Provenance
- Entiteitsidentifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-064, SRC-065, SRC-066
