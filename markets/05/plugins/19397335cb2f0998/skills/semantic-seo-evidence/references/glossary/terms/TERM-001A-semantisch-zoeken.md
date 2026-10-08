---
term_id: TERM-001A
preferred_name_nl: Semantisch zoeken
english_name: Semantic Search
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Information Retrieval / zoektechnologie
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-022
- SRC-030
- SRC-064
- SRC-070
related_term_ids:
- QRY-013
- TERM-001
- TERM-002
- TERM-002E
- TERM-011B
- TERM-011C
- TERM-011D
status: active
---

# Semantisch zoeken

**Engelse term of afkorting:** Semantic Search  
**Term-ID:** `TERM-001A`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Information Retrieval / zoektechnologie  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Semantisch zoeken is een verzamelnaam voor zoekmethoden die naast letterlijke teken- en woordovereenkomst ook betekenis, context, intentie, concepten, entiteiten, relaties of eerdere interacties gebruiken om relevante informatie te vinden en te rangschikken.

## Geen enkele vaste techniek

Semantic Search is geen enkel algoritme. Een zoeksysteem kan verschillende methoden combineren, waaronder lexicale varianten, query rewriting, taxonomieën, knowledge graphs, embeddings, dense retrieval, neural matching en reranking. Exacte woordmatching blijft vaak belangrijk voor namen, codes, citaten, getallen en specialistische termen.

| Benadering | Wat zij toevoegt | Voorbeeld |
| --- | --- | --- |
| Lexicale verrijking | Varianten, spelling, woordvormen en synoniemen | “mobiliteitsscooter” kan helpen bij “scootmobiel”. |
| Context en intentie | Interpretatie van het gebruiksdoel | “Pride bereik” gaat bij een productcontext niet over emotie. |
| Entiteiten en relaties | Identificeert dingen en hun verbindingen | Een model hoort bij een merk en heeft een bepaalde accuconfiguratie. |
| Vectorrepresentaties | Vergelijkt betekenisrepresentaties van queries en passages | Een vraag kan bij een passage passen zonder dezelfde woorden. |
| Querygeschiedenis of sessiecontext | Gebruikt eerdere formuleringen of interacties | Een vervolgvraag kan verwijzen naar het eerder genoemde model. |

## Wat is bevestigd?

- In de vakliteratuur is semantic search een familie van technieken die verder gaat dan eenvoudige string- en trefwoordmatching. [SRC-070]

- Google documenteert BERT, neural matching en RankBrain als systemen die betekenis, intentie en conceptrelaties helpen interpreteren. [SRC-022] [SRC-030]

- Google introduceerde de Knowledge Graph als een manier om dingen en hun relaties te modelleren, niet alleen tekenreeksen. [SRC-064]

- Moderne zoekarchitecturen kunnen lexicale en semantische retrieval combineren; deze onderdelen zijn in batch 2 afzonderlijk gedefinieerd.

## Wat is niet bevestigd?

- Dat een zoekmachine menselijke betekenis volledig of foutloos begrijpt.

- Dat semantic search uitsluitend op knowledge graphs of uitsluitend op embeddings berust.

- Dat exacte woorden onbelangrijk zijn geworden.

- Dat “Google is een Semantic Search Engine” een complete officiële technische classificatie van alle Google Search-processen is.

- Dat alle zoek- en AI-platforms dezelfde queryinterpretatie, entiteitenbron of semantische ruimte gebruiken.

## Praktische toepassing

1. Formuleer de informatiebehoefte en mogelijke interpretaties van een query.

2. Benoem belangrijke namen, codes, eenheden en vaktermen exact waar dat nodig is.

3. Gebruik natuurlijke synoniemen en beschrijvingen zonder alle varianten geforceerd te herhalen.

4. Maak relaties en voorwaarden expliciet wanneer zij de betekenis veranderen.

5. Controleer of de content ook een parafrase of vervolgvraag kan beantwoorden zonder vaag te worden.

## Veelgemaakte misvatting

Semantisch zoeken heeft trefwoorden volledig vervangen. In de praktijk worden lexicale en semantische signalen vaak gecombineerd.

## Zie ook

Semantic SEO, Sparse Retrieval, Dense Retrieval, Hybrid Retrieval, Query Rewriting, Entiteit en Knowledge Graph.

## Verwante begrippen

- `QRY-013`: Query Rewriting
- `TERM-001`: Semantic SEO
- `TERM-002`: Entiteit
- `TERM-002E`: Kennisgraaf
- `TERM-011B`: Sparse Retrieval
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval

## Bronnen en actualiteit

**Kernbronnen:** SRC-022, SRC-030, SRC-064, SRC-070
