---
term_id: IR-015
preferred_name_nl: Contextual Embedding
english_name: Contextual Embedding / Contextuele embedding
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: NLP / dense retrieval
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-019
- SRC-049
- SRC-058
related_term_ids:
- IR-016
- TERM-011C
- TERM-014A
- TERM-016C
- TERM-017B
status: active
---

# Contextual Embedding

**Engelse term of afkorting:** Contextual Embedding / Contextuele embedding  
**Term-ID:** `IR-015`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** NLP / dense retrieval  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een contextual embedding is een vectorrepresentatie waarvan de waarde afhangt van de omliggende tekst en de specifieke gebruikscontext.

## Afbakening

Hetzelfde woord kan verschillende representaties krijgen in verschillende zinnen. Contextuele embeddings kunnen woorden, zinnen, passages of documenten representeren.

## Wat is bevestigd?

- Transformergebaseerde modellen kunnen contextafhankelijke representaties leren.

- Contextuele embeddings worden gebruikt voor onder meer semantische matching, classificatie en retrieval.

## Wat is niet bevestigd?

- Dat een embedding een objectieve of volledige menselijke betekenis vastlegt.

- Dat twee teksten met kleine vectorafstand automatisch dezelfde feiten of intentie bevatten.

## Praktische toepassing

1. Gebruik een model dat past bij taal, domein en taak.

2. Test representaties op echte queries en relevante passages.

3. Bewaar modelversie, segmentatie en indexdatum voor reproduceerbaarheid.

## Voorbeeld

Het woord “stoel” krijgt in een scootmobielcontext een andere representatie dan in een eetkamercontext.

## Veelgemaakte misvatting

Contextual embeddings vervangen geen feitencontrole. Een semantisch vergelijkbare passage kan alsnog onjuist of verouderd zijn.

## Zie ook

- Embedding

- Dense Retrieval

- Vector Search

- Semantic Similarity

- Context Window

## Verwante begrippen

- `IR-016`: Vector Search
- `TERM-011C`: Dense Retrieval
- `TERM-014A`: Semantische gelijkenis
- `TERM-016C`: Embedding
- `TERM-017B`: Context Window

## Bronnen en actualiteit

**Kernbronnen:** SRC-019, SRC-049, SRC-058

**Update-trigger:** Nieuw embeddingmodel, andere taal, gewijzigde chunking of indexherbouw.
