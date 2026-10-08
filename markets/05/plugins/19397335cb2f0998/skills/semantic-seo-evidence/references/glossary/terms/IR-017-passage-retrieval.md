---
term_id: IR-017
preferred_name_nl: Passage Retrieval
english_name: Passage Retrieval
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / RAG
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-017
- SRC-018
- SRC-072
related_term_ids:
- AIS-010
- AIS-011
- IR-018
- TERM-017B
- TERM-017C
status: active
---

# Passage Retrieval

**Engelse term of afkorting:** Passage Retrieval  
**Term-ID:** `IR-017`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / RAG  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Passage Retrieval haalt specifieke tekstpassages op die relevant zijn voor een vraag, in plaats van alleen volledige documenten als één geheel te behandelen.

## Afbakening

Passages kunnen vooraf worden gesegmenteerd of dynamisch worden geselecteerd. De grenzen beïnvloeden hoeveel context, bewijs en ruis wordt meegenomen.

## Wat is bevestigd?

- Onderzoek naar open-domain question answering gebruikt passage retrieval om gerichte bewijsstukken te vinden.

- Passages kunnen lexicaal, dense of hybride worden opgehaald.

## Wat is niet bevestigd?

- Dat iedere H2-sectie automatisch de passagegrens van een zoek- of AI-systeem vormt.

- Dat kortere passages altijd beter zijn.

## Praktische toepassing

1. Maak belangrijke secties zelfstandig begrijpelijk zonder onnatuurlijke fragmentatie.

2. Houd bron, voorwaarden en entiteit dicht bij de claim.

3. Test of segmentatie voldoende context behoudt voor correcte interpretatie.

## Voorbeeld

Een pagina over actieradius kan afzonderlijke passages bevatten over temperatuur, bestuurdersgewicht en snelheid, zodat een gerichte vraag de juiste uitleg kan ophalen.

## Veelgemaakte misvatting

Passage Retrieval is geen opdracht om tekst in vaste blokjes van een bepaald woordenaantal te hakken.

## Zie ook

- Chunking

- Passage Ranking

- RAG

- Grounding

- Context Window

## Verwante begrippen

- `AIS-010`: Retrieval-Augmented Generation
- `AIS-011`: Grounding
- `IR-018`: Passage Ranking
- `TERM-017B`: Context Window
- `TERM-017C`: Chunking

## Bronnen en actualiteit

**Kernbronnen:** SRC-017, SRC-018, SRC-072

**Update-trigger:** Wijziging in segmentatie, retrievalmodel of platformdocumentatie.
