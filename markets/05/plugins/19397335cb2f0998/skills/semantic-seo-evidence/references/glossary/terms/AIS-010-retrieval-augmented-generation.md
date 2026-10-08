---
term_id: AIS-010
preferred_name_nl: Retrieval-Augmented Generation
english_name: Retrieval-Augmented Generation / RAG
cluster_id: 8
cluster_name: AI Search
type_context: AI / Information Retrieval
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-024
- SRC-117
related_term_ids:
- AIS-011
- AIS-012
- AIS-013
- AIS-014
- IR-017
status: active
---

# Retrieval-Augmented Generation

**Engelse term of afkorting:** Retrieval-Augmented Generation / RAG  
**Term-ID:** `AIS-010`  
**Hoofdcategorie:** 8 AI Search  
**Type en context:** AI / Information Retrieval  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Retrieval-Augmented Generation, RAG, is een architectuur waarbij een generatief model informatie uit externe bronnen ophaalt en die informatie gebruikt bij het samenstellen van een antwoord.

## Afbakening

RAG combineert retrieval met generatie. De broncollectie, query, passagekeuze, contexttoewijzing en generatie bepalen samen de kwaliteit. Een systeem kan tekst, data of andere modaliteiten ophalen.

## Wat is bevestigd?

- Het oorspronkelijke RAG-onderzoek combineert parametrische modelkennis met opgehaalde documenten voor kennisintensieve taken.

- Google beschrijft generatieve zoekfuncties met retrieval en grounding op basis van webbronnen.

## Wat is niet bevestigd?

- Dat ieder antwoord van een taalmodel RAG gebruikt.

- Dat opgehaalde bronnen automatisch correct worden gebruikt of geciteerd.

## Praktische toepassing

1. Beheer bronkwaliteit, actualiteit en toegangsrechten.

2. Evalueer retrieval en generatie afzonderlijk.

3. Koppel belangrijke claims aan ondersteunende passages en provenance.

## Voorbeeld

Een assistent kan producthandleidingen, eigen testdata en actuele regelgeving ophalen voordat hij een antwoord over een model samenstelt.

## Veelgemaakte misvatting

RAG voorkomt hallucinaties niet automatisch. Onjuiste retrieval of foutieve synthese kan nog steeds tot een misleidend antwoord leiden.

## Zie ook

- Grounding

- Passage Retrieval

- Answer Synthesis

- Citation

- Source Eligibility

## Verwante begrippen

- `AIS-011`: Grounding
- `AIS-012`: Answer Synthesis
- `AIS-013`: Source Eligibility
- `AIS-014`: Citation
- `IR-017`: Passage Retrieval

## Bronnen en actualiteit

**Kernbronnen:** SRC-024, SRC-117

**Update-trigger:** Nieuw retrievalmodel, gewijzigde broncollectie of platformdocumentatie.
