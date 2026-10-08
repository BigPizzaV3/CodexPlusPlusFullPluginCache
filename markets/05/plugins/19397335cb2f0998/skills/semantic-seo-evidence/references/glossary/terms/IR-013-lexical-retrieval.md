---
term_id: IR-013
preferred_name_nl: Lexical Retrieval
english_name: Lexical Retrieval / Lexicale retrieval
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-013
- SRC-014
related_term_ids:
- IR-012
- IR-014
- TERM-011B
- TERM-011C
- TERM-011D
status: active
---

# Lexical Retrieval

**Engelse term of afkorting:** Lexical Retrieval / Lexicale retrieval  
**Term-ID:** `IR-013`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Lexical Retrieval haalt informatie op op basis van woorden, tokens, woordgroepen en statistische tekstovereenkomst tussen query en documenten.

## Afbakening

De methode kan exacte termen, normalisatie, phrase matching, veldweging, TF-IDF en BM25 gebruiken. Zij is bijzonder sterk voor namen, codes, getallen en specifieke terminologie.

## Wat is bevestigd?

- Lexicale retrieval is een gevestigde vorm van tekstzoektechnologie.

- Exacte termen en zeldzame identifiers kunnen sterke onderscheidende signalen leveren.

## Wat is niet bevestigd?

- Dat lexical retrieval geen synoniemen of taalvariatie kan ondersteunen.

- Dat semantische retrieval lexicale methoden volledig overbodig heeft gemaakt.

## Praktische toepassing

1. Gebruik correcte productnamen, codes, cijfers en eenheden in zichtbare tekst.

2. Voorkom onnodige spellingvarianten en inconsistente identifiers.

3. Combineer met dense retrieval wanneer parafrasen en bredere betekenis belangrijk zijn.

## Voorbeeld

Een zoekopdracht naar modelcode “FM-OF32” kan lexicaal zeer precies worden gematcht, ook wanneer een semantisch model de code niet goed kent.

## Veelgemaakte misvatting

Lexicale retrieval is niet hetzelfde als keyword stuffing. Relevantie hangt ook af van veld, frequentie, lengte en taak.

## Zie ook

- Sparse Retrieval

- Inverted Index

- BM25

- Dense Retrieval

- Hybrid Retrieval

## Verwante begrippen

- `IR-012`: Inverted Index
- `IR-014`: BM25
- `TERM-011B`: Sparse Retrieval
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-013, SRC-014

**Update-trigger:** Nieuwe retrievalimplementaties of wijzigingen in tokenizer en ranking.
