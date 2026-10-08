---
term_id: TERM-011A
preferred_name_nl: Relevantie in Information Retrieval
english_name: Relevance in Information Retrieval
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / evaluatie / gebruikersbehoefte
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-013
- SRC-014
- SRC-015
- SRC-016
- SRC-017
- SRC-030
- SRC-037
- SRC-038
related_term_ids:
- QRY-010
- TERM-011B
- TERM-011C
- TERM-011D
- TERM-011F
- TERM-015
- TERM-021B
status: active
---

# Relevantie in Information Retrieval

**Engelse term of afkorting:** Relevance in Information Retrieval  
**Term-ID:** `TERM-011A`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / evaluatie / gebruikersbehoefte  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Relevantie in Information Retrieval is de relatie tussen een informatiebehoefte of query en een document, passage, product, antwoord of ander informatie-item, binnen een bepaalde taak en context. Een retrievalsysteem kan hiervoor scores berekenen, maar relevantie zelf is niet één universele score of één enkel algoritme.

## Relevantie is meerdimensionaal

Relevantie is een centraal maar complex begrip binnen Information Retrieval. Mizzaro beschrijft meerdere soorten relevantie en plaatst die in een raamwerk met onder meer de informatiebehoefte, het informatie-item, taak en context. Recente overzichtsliteratuur behandelt relevantie eveneens als multidimensionaal en dynamisch. [SRC-037]

| Dimensie | Praktische vraag | Voorbeeld |
| --- | --- | --- |
| Topicale relevantie | Gaat de informatie over het bedoelde onderwerp? | Een pagina over actieradius behandelt accu, ritafstand en omstandigheden. |
| Semantische relevantie | Past de betekenis bij de vraag, ook zonder dezelfde woorden? | “Hoe ver kom ik?” kan relevant zijn voor informatie over praktisch bereik. |
| Taakrelevantie | Helpt de informatie de gebruiker een handeling of beslissing uit te voeren? | Een keuzetabel helpt een model selecteren; een definitie alleen mogelijk niet. |
| Contextuele relevantie | Geldt de informatie voor deze persoon, plaats, tijd, variant en situatie? | Een bereikwaarde is alleen bruikbaar met accuconfiguratie en testvoorwaarden. |
| Actualiteitsrelevantie | Is de informatie actueel genoeg voor de vraag? | Regelgeving en prijsinformatie vragen een concrete controledatum. |
| Presentatierelevantie | Staat de informatie in een vorm die de taak ondersteunt? | Afmetingen zijn beter vergelijkbaar in een tabel dan in verspreide alinea’s. |

## Systeemscore versus relevantiebeoordeling

Een systeem gebruikt ranking- of retrievalscores om de verwachte relevantie te schatten. BM25, TF-IDF, sparse modellen, dense retrievers en rerankers berekenen of leren ieder andere signalen. Zij zijn daarom geen uitwisselbare namen voor dezelfde ene relevantiescore. [SRC-012] [SRC-013] [SRC-014] [SRC-017]

Onderzoekscollecties zoals TREC gebruiken menselijke relevantiebeoordelingen, vaak qrels genoemd, om retrievalsystemen te evalueren. De concrete beoordelingsregels verschillen per taak en collectie. Een qrel is een beoordelingslabel binnen die testopzet, geen universele waarheid voor iedere gebruiker. [SRC-038]

## Blind Librarian, juiste status

| Frameworkmetafoor<br>Blind Librarian kan als beeldspraak worden gebruikt voor een systeem dat informatie terugvindt en ordent zonder zelf een volledig antwoord te formuleren. De term is geen algemeen erkende historische fase van Information Retrieval. Moderne systemen kunnen bovendien lexicale retrieval, semantische retrieval, reranking en antwoordgeneratie combineren. |
| --- |

## Wat is bevestigd?

- Relevantie is een centraal en meerdimensionaal begrip binnen Information Retrieval. [SRC-012] [SRC-037]

- Menselijke relevantiebeoordelingen worden gebruikt om retrievalsystemen binnen vastgelegde testcollecties te evalueren. [SRC-038]

- BM25 en TF-IDF zijn termgebaseerde methoden, terwijl Word2Vec, GloVe en dense retrievers representaties leren voor andere doelen. [SRC-013] [SRC-014] [SRC-015] [SRC-016] [SRC-017]

- Google beschrijft neural matching als een systeem waarmee concepten in queries en pagina’s beter kunnen worden gerelateerd. [SRC-030]

## Wat is niet bevestigd?

- Dat er één openbare universele relevantiescore bestaat die alle zoekmachines en AI-systemen op dezelfde manier berekenen.

- Dat één methode zoals TF-IDF, BM25 of cosine similarity de volledige kwaliteit en bruikbaarheid van content bepaalt.

- Dat Blind Librarian een officiële technische fase in de ontwikkeling van Google of Information Retrieval is.

- Dat meer semantisch verwante woorden automatisch meer relevantie of een hogere ranking opleveren.

## Praktische toepassing

1. Formuleer de echte informatiebehoefte en gebruikerstaak voordat content wordt geschreven.

2. Controleer niet alleen of de pagina over het onderwerp gaat, maar ook of het antwoord bruikbaar is voor de specifieke variant, situatie en beslissing.

3. Zet belangrijke feiten in een geschikte vorm, zoals een tabel, demonstratie, berekening of stap-voor-staproute.

4. Maak expliciet welke voorwaarden, uitzonderingen en onzekerheden de toepasbaarheid beperken.

5. Gebruik rankings, klikken en AI-citaties als meetgegevens, maar controleer ook correctheid, taakafronding en bedrijfsresultaat.

## Veelgemaakte misvatting

“Relevantie is de score die BM25, TF-IDF of een embeddingmodel geeft.” Een score is een systeemschatting op basis van een specifieke representatie en methode. Werkelijke bruikbaarheid hangt ook af van taak, context, actualiteit, bewijs en presentatie.

## Zie ook

Sparse Retrieval, Dense Retrieval, Hybrid Retrieval, Reranking, Semantic Relevance, Search Intent, User Task en Needs Met.

## Verwante begrippen

- `QRY-010`: Zoekintentie
- `TERM-011B`: Sparse Retrieval
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval
- `TERM-011F`: Reranking
- `TERM-015`: Semantische relevantie
- `TERM-021B`: Gebruikerstaak
- Needs Met *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-013, SRC-014, SRC-015, SRC-016, SRC-017, SRC-030, SRC-037, SRC-038
