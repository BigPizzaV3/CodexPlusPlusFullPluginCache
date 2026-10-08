---
term_id: ENT-011
preferred_name_nl: Predicaat
english_name: Predicate
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: RDF / kennisrepresentatie
evidence_labels:
- A
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-031
related_term_ids:
- ENT-012
- TEC-011
- TEC-012
- TERM-002F
- TERM-003A
status: active
---

# Predicaat

**Engelse term of afkorting:** Predicate  
**Term-ID:** `ENT-011`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** RDF / kennisrepresentatie  
**Bewijsbasis:** A  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een predicaat is het middelste onderdeel van een RDF-triple en geeft aan welke eigenschap of relatie tussen het subject en het object wordt uitgedrukt.

## Afbakening

In RDF wordt het predicaat geïdentificeerd met een IRI. Het hoeft taalkundig geen werkwoord te zijn. Het kan bijvoorbeeld verwijzen naar een eigenschap als heeftMotorvermogen, isVariantVan of wordtVerkochtDoor.

## Wat is bevestigd?

- Een RDF-triple bestaat uit subject, predicaat en object.

- Het predicaat bepaalt de betekenis van de verbinding en wordt in RDF door een IRI benoemd.

## Wat is niet bevestigd?

- Dat ieder grammaticaal werkwoord automatisch een bruikbaar RDF-predicaat is.

- Dat zoekmachines iedere zin rechtstreeks in exact één RDF-predicaat omzetten.

## Praktische toepassing

1. Gebruik een ondubbelzinnige relatie die past bij het datamodel.

2. Maak onderscheid tussen eigenschappen, typen en relaties.

3. Hergebruik waar mogelijk bestaande vocabulairetermen in plaats van willekeurige nieuwe relaties.

## Voorbeeld

In de triple “On Four, heeft motorvermogen, 1000 watt” is “heeft motorvermogen” het predicaat.

## Veelgemaakte misvatting

Een predicaat is niet simpelweg het tweede woord van een zin. Het is de formele relatie binnen de triple.

## Zie ook

- RDF-triple

- Property

- Ontologie

- Schema.org

- JSON-LD

## Verwante begrippen

- `ENT-012`: Property
- `TEC-011`: Schema.org
- `TEC-012`: JSON-LD
- `TERM-002F`: Ontologie
- `TERM-003A`: RDF-triple

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-031

**Update-trigger:** Nieuwe of gewijzigde RDF-specificaties en vocabulairekeuzes.
