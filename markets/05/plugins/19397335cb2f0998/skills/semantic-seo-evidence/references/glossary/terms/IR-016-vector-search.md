---
term_id: IR-016
preferred_name_nl: Vector Search
english_name: Vector Search / Vectorzoeken
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Dense retrieval
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-017
- SRC-019
- SRC-049
related_term_ids:
- IR-015
- TERM-011C
- TERM-011D
- TERM-011F
- TERM-013
status: active
---

# Vector Search

**Engelse term of afkorting:** Vector Search / Vectorzoeken  
**Term-ID:** `IR-016`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Dense retrieval  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Vector Search zoekt naar informatieobjecten waarvan de vectorrepresentatie volgens een gekozen afstands- of gelijkenismaat dicht bij de queryvector ligt.

## Afbakening

Voor grote collecties worden vaak approximate-nearest-neighbour-methoden gebruikt. De kwaliteit hangt af van embeddingmodel, index, afstandsmaat, filters en evaluatie.

## Wat is bevestigd?

- Vector search ondersteunt semantische retrieval zonder uitsluitend exacte woordoverlap.

- Afstand of similarity wordt berekend binnen een specifieke representatieruimte.

## Wat is niet bevestigd?

- Dat de dichtstbijzijnde vector altijd het beste of feitelijk juiste antwoord is.

- Dat één drempelwaarde voor alle onderwerpen, talen en taken werkt.

## Praktische toepassing

1. Combineer vectorzoeken met metadatafilters en waar nodig lexicale signalen.

2. Evalueer precision, recall en fouten op echte gebruikerstaak.

3. Herbouw de index wanneer embeddings of brondata veranderen.

## Voorbeeld

Een vraag over “weinig kracht in de handen” kan passages vinden over duimgas, voetgas en aangepaste bediening, ook zonder exacte woordoverlap.

## Veelgemaakte misvatting

Vector Search is geen bewijs van begrip of waarheid. Het is een methode om vergelijkbare representaties op te halen.

## Zie ook

- Dense Retrieval

- Contextual Embedding

- Semantic Distance

- Hybrid Retrieval

- Reranking

## Verwante begrippen

- `IR-015`: Contextual Embedding
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval
- `TERM-011F`: Reranking
- `TERM-013`: Semantische afstand

## Bronnen en actualiteit

**Kernbronnen:** SRC-017, SRC-019, SRC-049

**Update-trigger:** Nieuw embeddingmodel, nieuwe indexmethode of gewijzigde retrievaldoelen.
