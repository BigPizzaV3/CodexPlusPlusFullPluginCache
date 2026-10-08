---
term_id: TERM-011E
preferred_name_nl: Candidate Generation
english_name: Candidate Generation
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / meerfasige zoekarchitectuur
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-039
- SRC-040
- SRC-041
related_term_ids:
- IR-017
- TEC-026
- TEC-027
- TERM-011B
- TERM-011C
- TERM-011D
- TERM-011F
status: active
---

# Candidate Generation

**Engelse term of afkorting:** Candidate Generation  
**Term-ID:** `TERM-011E`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / meerfasige zoekarchitectuur  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Candidate Generation is de vroege retrievalfase waarin uit een grote collectie efficiënt een beperkte groep mogelijke resultaten wordt geselecteerd. Het hoofddoel is doorgaans voldoende relevante kandidaten met hoge recall beschikbaar te maken voor latere scoring of reranking. Een kandidaat is nog geen definitief hoog gerangschikt resultaat.

## Plaats in een meerfasig systeem

| Fase | Hoofddoel | Typische afweging |
| --- | --- | --- |
| Crawlen en beschikbaar maken | Informatie technisch bereikbaar en verwerkbaar maken. | Dekking, actualiteit, beleid en kosten. |
| Candidate generation | Een brede maar beheersbare kandidatenlijst ophalen. | Recall en snelheid. |
| Eerste ranking of scoring | Kandidaten voorlopig ordenen. | Efficiëntie en relevantieschatting. |
| Reranking | Een kleinere set met rijkere modellen nauwkeuriger ordenen. | Kwaliteit versus rekentijd. |
| Selectie voor antwoord of SERP | Bronnen, passages of resultaten tonen of gebruiken. | Relevantie, kwaliteit, diversiteit, beleid en presentatie. |

Google Research beschrijft multi-stage cascaded retrievalarchitecturen waarin efficiënte retrievalmodellen worden gevolgd door effectievere rerankmodellen. Hybride onderzoek beschrijft eveneens een eerste retrievalstap die lexicale en semantische kandidaten combineert voordat reranking plaatsvindt. [SRC-041] [SRC-039]

## Waarom deze fase belangrijk is

Een later model kan alleen documenten of passages beoordelen die in de kandidatenlijst terecht zijn gekomen. Wanneer een technisch toegankelijke en inhoudelijk relevante bron in de eerste fase niet wordt opgehaald, kan een latere reranker die bron meestal niet alsnog selecteren.

## Praktische toepassing

1. Zorg dat belangrijke pagina’s crawlbaar, indexeerbaar, intern bereikbaar en technisch stabiel zijn.

2. Gebruik duidelijke titels, koppen, ankerteksten, productnamen, identifiers en zichtbare kerninformatie.

3. Beantwoord natuurlijke varianten van de gebruikerstaak zonder voor iedere formulering een aparte dunne pagina te maken.

4. Voorkom tegenstrijdige canonical-, noindex-, robots- of renderinginstellingen die beschikbaarheid beperken.

5. Maak belangrijke passages niet afhankelijk van interacties of scripts die crawlers of gebruikers niet betrouwbaar kunnen uitvoeren.

## Wat is niet bevestigd?

- Dat er één openbare kandidatenpool bestaat die voor alle Google- en AI-resultaten hetzelfde is.

- Dat website-eigenaren de exacte candidate-generationdrempels of gebruikte retrievers kunnen uitlezen.

- Dat opname in een kandidatenlijst automatisch een ranking, citatie of aanbeveling betekent.

- Dat één technische optimalisatie inhoudelijke relevantie en bronkwaliteit kan vervangen.

## Veelgemaakte misvatting

“Mijn pagina staat niet in het AI-antwoord, dus de inhoud is afgekeurd.” De pagina kan buiten de kandidatenlijst zijn gebleven, lager zijn gererankt, niet voor de uiteindelijke passage zijn geselecteerd of om presentatie- en beleidsredenen niet zichtbaar zijn geworden.

## Zie ook

Retrieval Eligibility, Crawlability, Indexability, Sparse Retrieval, Dense Retrieval, Hybrid Retrieval, Reranking en Passage Retrieval.

## Verwante begrippen

- `IR-017`: Passage Retrieval
- `TEC-026`: Crawlability
- `TEC-027`: Indexability
- `TERM-011B`: Sparse Retrieval
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval
- `TERM-011F`: Reranking
- Retrieval Eligibility *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-039, SRC-040, SRC-041
