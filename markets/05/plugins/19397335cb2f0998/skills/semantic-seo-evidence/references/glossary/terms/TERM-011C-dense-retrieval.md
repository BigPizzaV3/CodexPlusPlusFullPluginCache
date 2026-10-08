---
term_id: TERM-011C
preferred_name_nl: Dense Retrieval
english_name: Dense Retrieval
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / embeddings / semantische retrieval
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-015
- SRC-016
- SRC-017
- SRC-019
- SRC-030
related_term_ids:
- IR-016
- IR-017
- TERM-011B
- TERM-011D
- TERM-016C
status: active
---

# Dense Retrieval

**Engelse term of afkorting:** Dense Retrieval  
**Term-ID:** `TERM-011C`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / embeddings / semantische retrieval  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Dense Retrieval haalt informatie op door queries en documenten of passages als dichte vectorrepresentaties, embeddings, weer te geven. Een model leert deze vectoren zo dat relevante query-itemparen volgens een gekozen gelijkenis- of afstandsmaat dicht bij elkaar kunnen liggen, ook wanneer zij weinig exacte woorden delen.

## Hoe het werkt

Dense Passage Retrieval gebruikt bijvoorbeeld afzonderlijke encoders voor queries en passages. Het systeem leert relevante paren in een vectorruimte te plaatsen en kan daarna passages ophalen op basis van vectorsimilariteit. [SRC-017]

Veelgebruikte vergelijkingen zijn cosine similarity, dot product en Euclidische afstand. Deze maten gedragen zich niet identiek wanneer vectorlengtes niet zijn genormaliseerd. Cosine en dot product zijn gelijkenismaten, terwijl Euclidische afstand kleiner wordt naarmate vectoren dichter bij elkaar liggen. [SRC-019]

| Sterk in | Voorbeeld |
| --- | --- |
| Parafrasen | “Hoe ver kan ik rijden?” kan dicht liggen bij “praktische actieradius”. |
| Contextuele betekenis | Het model kan “Pride” in een scootmobielcontext anders representeren dan het algemene woord trots. |
| Passage retrieval | Een specifieke alinea kan worden gevonden zonder dat de hele pagina dezelfde bewoording gebruikt. |
| Meertalige of variabele formuleringen | Afhankelijk van model en training kunnen betekenisverwante formuleringen worden verbonden. |

| Beperking | Waarom belangrijk |
| --- | --- |
| Zeldzame codes en exacte cijfers | Een vector kan een modelnummer, foutcode of eenheid onvoldoende precies onderscheiden. |
| Model- en domeinafhankelijkheid | Een embedding die elders goed werkt, hoeft in een specialistisch productdomein niet dezelfde relaties te leren. |
| Minder transparante score | Het is moeilijker uit te leggen welke tekstkenmerken precies tot een vectorpositie leidden. |
| Semantisch dichtbij is niet automatisch juist | Een inhoudelijk vergelijkbare passage kan verouderd, onbetrouwbaar of voor de verkeerde variant zijn. |

## Word2Vec en GloVe, juiste plaats

Word2Vec en GloVe zijn invloedrijke methoden om woordrepresentaties te leren. Zij zijn geen complete retrievalsystemen en niet automatisch de embeddings die moderne zoekmachines gebruiken. Contextuele modellen kunnen dezelfde term afhankelijk van de zin anders representeren. [SRC-015] [SRC-016]

## Praktische toepassing voor content

1. Beantwoord dezelfde gebruikerstaak in natuurlijke taal en gebruik relevante omschrijvingen, in plaats van alleen exacte trefwoorden te herhalen.

2. Maak passages semantisch compleet. Benoem entiteit, eigenschap, waarde, context en uitzondering waar die nodig zijn.

3. Gebruik ondubbelzinnige modelnamen en identifiers naast natuurlijke beschrijvingen, zodat dense en sparse signalen elkaar kunnen aanvullen.

4. Zorg dat belangrijke informatie niet uitsluitend uit impliciete verwijzingen zoals “deze” of “hij” bestaat wanneer de passage zelfstandig moet kunnen worden opgehaald.

5. Behandel embeddingscores uit externe tools als analysematen, niet als directe Google-scores.

## Wat is niet bevestigd?

- Dat alle zoek- en AI-platforms hetzelfde embeddingmodel, dezelfde vectorruimte of dezelfde afstandsmaat gebruiken.

- Dat een hoge cosine similarity voldoende is voor ranking, citatie, aanbeveling of feitelijke juistheid.

- Dat Word2Vec of GloVe de huidige algemene retrievalmethode van Google is.

- Dat een schrijver een tekst op één ideale vectorscore kan optimaliseren.

## Veelgemaakte misvatting

“Dense retrieval begrijpt de tekst zoals een mens.” Een model leert statistische representaties die nuttig kunnen zijn voor betekenisvolle matching. Dat garandeert geen menselijk begrip, feitelijke controle of juiste toepassing.

## Zie ook

Embedding, Vector Search, Cosine Similarity, Dot Product, Euclidische afstand, Passage Retrieval, Sparse Retrieval en Hybrid Retrieval.

## Verwante begrippen

- `IR-016`: Vector Search
- `IR-017`: Passage Retrieval
- `TERM-011B`: Sparse Retrieval
- `TERM-011D`: Hybrid Retrieval
- `TERM-016C`: Embedding
- Cosine Similarity *(verwant concept buiten deze begrippenlijst)*
- Dot Product *(verwant concept buiten deze begrippenlijst)*
- Euclidische afstand *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-015, SRC-016, SRC-017, SRC-019, SRC-030
