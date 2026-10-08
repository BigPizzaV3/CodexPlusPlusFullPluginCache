---
term_id: TERM-011F
preferred_name_nl: Reranking
english_name: Reranking
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / ranking / meerfasige systemen
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-017
- SRC-039
- SRC-040
- SRC-041
related_term_ids:
- AIS-012
- IR-018
- TERM-011D
- TERM-011E
status: active
---

# Reranking

**Engelse term of afkorting:** Reranking  
**Term-ID:** `TERM-011F`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / ranking / meerfasige systemen  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Reranking is het opnieuw ordenen van een eerder opgehaalde, beperkte kandidatenlijst met een nauwkeuriger of rijker model. Een reranker kan meer interactie tussen query en document analyseren dan een snelle eerste retriever, maar kan doorgaans alleen werken met de kandidaten die al zijn opgehaald.

## Verschil tussen retrieval en reranking

| Kenmerk | Eerste retrieval | Reranking |
| --- | --- | --- |
| Collectieomvang | Werkt over een zeer grote collectie. | Werkt over een veel kleinere kandidatenlijst. |
| Hoofddoel | Goede kandidaten niet missen. | Beste kandidaten nauwkeuriger ordenen. |
| Snelheid | Zeer belangrijk. | Meer rekentijd per kandidaat mogelijk. |
| Modelinteractie | Vaak eenvoudiger of vooraf geïndexeerd. | Kan query en passage gezamenlijk en gedetailleerd beoordelen. |
| Risico | Gemiste bron kan later niet worden hersteld. | Verkeerde score of bias kan goede kandidaten naar beneden plaatsen. |

Onderzoek naar cascaded searcharchitecturen beschrijft efficiënte retrieval gevolgd door effectievere learning-to-rank- of neurale rerankmodellen. Cross-encoders kunnen query en passage gezamenlijk verwerken, maar zijn duurder dan vooraf berekende embeddings. [SRC-041]

Recente hybride systemen combineren query rewriting, sparse en dense retrieval en cross-encoder reranking. Dit laat zien dat retrieval en reranking afzonderlijke functies zijn die samen kunnen worden geoptimaliseerd. [SRC-040]

## Mogelijke rerankingsignalen

- Fijnmazige query-passage-interactie.

- Taak- en intentieovereenkomst.

- Exacte entiteiten, eigenschappen, getallen en voorwaarden.

- Passagekwaliteit, volledigheid en zelfstandig begrip.

- Actualiteit, bronkenmerken, diversiteit of productspecifieke constraints, afhankelijk van het systeem.

## Praktische toepassing voor content

1. Zorg dat de belangrijkste passage niet alleen woorden deelt met de query, maar het concrete probleem volledig en nauwkeurig oplost.

2. Benoem beperkingen en voorwaarden dicht bij de bijbehorende claim, zodat een passage niet misleidend uit context kan worden gehaald.

3. Gebruik tabellen, lijsten of stappen alleen wanneer zij de taak werkelijk verduidelijken.

4. Maak de bronidentiteit, auteur, testmethode en datum zichtbaar wanneer die nodig zijn om kwaliteit te beoordelen.

5. Behandel een hoge gewone ranking niet als garantie op selectie in ieder AI-antwoord. Andere kandidaten, passages en modellen kunnen per vraag verschillen.

## Wat is niet bevestigd?

- Dat alle commerciële zoek- en AI-systemen één reranker of dezelfde features gebruiken.

- Dat een externe tool de werkelijke interne rerankingscore van Google of een AI-platform kan meten.

- Dat een lange of sterk geformatteerde passage automatisch beter wordt gererankt.

- Dat reranking een gemiste kandidaat uit de eerste retrievalfase kan herstellen.

## Veelgemaakte misvatting

“Reranking is gewoon de uiteindelijke Google-ranking.” Reranking is een algemene technische fase. Een commerciële zoekmachine kan meerdere retrieval-, ranking-, reranking-, kwaliteits- en presentatiestappen gebruiken. De precieze architectuur is platform- en productafhankelijk.

## Zie ook

Candidate Generation, Learning to Rank, Cross-Encoder, Passage Ranking, Hybrid Retrieval, Answer Synthesis en Source Selection.

## Verwante begrippen

- `AIS-012`: Answer Synthesis
- `IR-018`: Passage Ranking
- `TERM-011D`: Hybrid Retrieval
- `TERM-011E`: Candidate Generation
- Cross-Encoder *(verwant concept buiten deze begrippenlijst)*
- Learning to Rank *(verwant concept buiten deze begrippenlijst)*
- Source Selection *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-017, SRC-039, SRC-040, SRC-041
