---
term_id: IR-012
preferred_name_nl: Inverted Index
english_name: Inverted Index / Omgekeerde index
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Lexicale retrieval
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-029
related_term_ids:
- IR-011
- IR-013
- IR-014
- TERM-011B
- TERM-016B
status: active
---

# Inverted Index

**Engelse term of afkorting:** Inverted Index / Omgekeerde index  
**Term-ID:** `IR-012`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Lexicale retrieval  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een inverted index koppelt termen of tokens aan de documenten en posities waarin zij voorkomen, zodat lexicale zoekopdrachten efficiënt kunnen worden uitgevoerd.

## Afbakening

In plaats van per document alle woorden te doorlopen, kan het systeem vanuit een term direct naar een postingslijst met documenten, frequenties en posities gaan.

## Wat is bevestigd?

- Omgekeerde indexen vormen een klassieke basis voor grootschalige tekstzoekmachines.

- De index kan frequentie, positie, veld en andere statistieken bewaren.

## Wat is niet bevestigd?

- Dat een inverted index alleen exacte volledige woorden kan ondersteunen.

- Dat het voorkomen van een term automatisch hoge relevantie betekent.

## Praktische toepassing

1. Gebruik stabiele tokenisatie en normalisatie.

2. Bewaar belangrijke velden en posities wanneer phrase matching of veldweging nodig is.

3. Combineer lexicale indexering zo nodig met semantische retrieval.

## Voorbeeld

De term “draaicirkel” verwijst in de omgekeerde index naar alle documenten en passages waarin deze term is opgenomen.

## Veelgemaakte misvatting

Een inverted index begrijpt niet vanzelf de volledige gebruikersintentie. Het is een toegangsstructuur, geen complete relevantiebeoordeling.

## Zie ook

- Index

- Lexical Retrieval

- Sparse Retrieval

- BM25

- Tokenisatie

## Verwante begrippen

- `IR-011`: Index
- `IR-013`: Lexical Retrieval
- `IR-014`: BM25
- `TERM-011B`: Sparse Retrieval
- `TERM-016B`: Token en tokenisatie

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-029

**Update-trigger:** Wijziging in tokenizer, normalisatie, veldschema of zoekarchitectuur.
