---
term_id: TERM-013
preferred_name_nl: Semantische afstand
english_name: Semantic Distance
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Semantiek / vectoren / grafen / taxonomieën
evidence_labels:
- A
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-017
- SRC-019
- SRC-042
- SRC-043
- SRC-044
related_term_ids:
- IR-016
- TERM-002E
- TERM-002F
- TERM-002G
- TERM-014A
- TERM-014B
- TERM-016G
status: active
---

# Semantische afstand

**Engelse term of afkorting:** Semantic Distance  
**Term-ID:** `TERM-013`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Semantiek / vectoren / grafen / taxonomieën  
**Bewijsbasis:** A, B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Semantische afstand is een verzamelbegrip voor een numerieke of structurele maat die aangeeft hoe ver twee representaties, concepten of knooppunten volgens een gekozen model van elkaar liggen. De betekenis van de uitkomst hangt volledig af van het representatietype, de afstands- of gelijkenismaat en de context. Er bestaat geen universele semantische afstandsscore voor SEO.

## Belangrijkste typen

| Type | Representatie | Voorbeelden van maat | Belangrijkste nuance |
| --- | --- | --- | --- |
| Vectorafstand | Embeddings van woorden, passages, queries of documenten. | Euclidische afstand; cosine distance. Cosine similarity en dot product zijn gelijkenismaten. | Model, training, normalisatie en vectorlengte beïnvloeden de uitkomst. |
| Graafafstand | Knooppunten en relaties in een semantisch netwerk of knowledge graph. | Kortste pad, gewogen pad of gemiddelde minimale padlengte. | Relatietype, richting en gewicht kunnen belangrijker zijn dan alleen het aantal stappen. |
| Taxonomische of ontologische afstand | Concepten in een hiërarchie, thesaurus of ontologie. | Padlengte, diepte, laagste gemeenschappelijke voorouder of information content. | Een hiërarchische relatie is iets anders dan een algemene associatieve relatie. |
| Contextafhankelijke afstand | Dezelfde term in verschillende zinnen, domeinen of gebruikssituaties. | Afstand in contextuele embeddings of een domeinspecifiek model. | Geen afzonderlijke universele formule; het is een eigenschap van de gekozen representatie en context. |

## Vectorafstand en gelijkenis

Google’s technische ML-uitleg noemt Euclidische afstand, cosine similarity en dot product. Een kleinere Euclidische afstand betekent meer nabijheid. Bij cosine similarity en dot product duidt juist een hogere waarde doorgaans op meer gelijkenis. Daarom is de algemene zin “een kleinere score betekent altijd meer semantische samenhang” onjuist. [SRC-019]

## Graaf- en taxonomische afstand

Klassiek onderzoek naar semantic nets gebruikt padlengten om conceptuele afstand te modelleren, maar waarschuwt dat andere relatietypen dan hiërarchische relaties aanvullende behandeling vragen. [SRC-042]

Resnik liet zien dat puur randen tellen in een taxonomie beperkingen heeft en stelde een maat op basis van information content voor. SKOS onderscheidt bovendien hiërarchische relaties, broader en narrower, van associatieve related-relaties. Dat verschil is belangrijk: twee concepten kunnen sterk gerelateerd zijn zonder taxonomisch dicht bij elkaar te staan. [SRC-043] [SRC-044]

## Voorbeelden

| Paar | Welke relatie? | Waarom één afstandsgetal onvoldoende kan zijn |
| --- | --- | --- |
| scootmobiel en mobiliteitshulpmiddel | Taxonomisch: scootmobiel kan als specifieker type worden gemodelleerd. | De precieze positie hangt af van de gebruikte taxonomie. |
| scootmobiel en actieradius | Sterk inhoudelijk gerelateerd, maar geen synoniemen of eenvoudige is-a-relatie. | Associatieve relatedness is iets anders dan similarity of taxonomische nabijheid. |
| Pride en trots | Zelfde tekenreeks, mogelijk verschillende entiteiten of betekenissen. | Context en entity disambiguation bepalen de juiste representatie. |
| On Four en 1000 W | Entiteit-eigenschap-waarderelatie. | Een kennisgraafrelatie zegt meer dan alleen een woordvectorafstand. |

## Wat is bevestigd?

- Embeddingruimten kunnen met Euclidische afstand, cosine of dot product worden vergeleken, met verschillende interpretaties. [SRC-019]

- Padgebaseerde conceptafstand is een erkende methode in hiërarchische semantic nets. [SRC-042]

- Information-contentmaten kunnen taxonomische similarity anders modelleren dan enkel edge counting. [SRC-043]

- SKOS onderscheidt directe en indirecte hiërarchische relaties van associatieve related-relaties. [SRC-044]

## Wat is niet bevestigd?

- Dat PageRank onderdeel is van de algemene definitie of berekening van semantische afstand.

- Dat queryfrequentie, klikgedrag of zoekvolume standaardcomponenten zijn van vector- of graafafstand.

- Dat één kleinere afstand in iedere maat automatisch meer relevantie, kwaliteit of ranking betekent.

- Dat externe SEO-tools de interne semantische afstand van Google of AI-platforms exact kunnen meten.

- Dat een contentnetwerk moet worden ontworpen door alleen de kleinste afstand tussen termen na te streven.

## Praktische toepassing

1. Noem altijd het representatietype en de maat wanneer een afstand of similarityscore wordt gerapporteerd.

2. Gebruik vectorafstand voor clustering en retrievalonderzoek, maar controleer resultaten handmatig op entiteit, taak, context en feiten.

3. Gebruik graaf- en ontologierelaties om het soort verband vast te leggen, niet alleen het aantal stappen.

4. Maak onderscheid tussen similarity, relatedness, hiërarchie en feitelijke relaties.

5. Gebruik PageRank, populariteit of interactiedata alleen als afzonderlijke signalen wanneer een bron dat ondersteunt, niet als semantische afstand.

## Veelgemaakte misvatting

“Een kleine semantische afstand betekent dat twee termen op dezelfde pagina horen.” Afstand beschrijft een relatie binnen een gekozen model. De contentbeslissing hangt daarnaast af van gebruikerstaak, intentie, entiteit, bewijs, risico en gewenste informatievorm.

## Zie ook

Semantic Similarity, Semantic Relatedness, Vector Search, Knowledge Graph, Ontology, Taxonomy, Entity Disambiguation en Cosine Similarity.

## Verwante begrippen

- `IR-016`: Vector Search
- `TERM-002E`: Kennisgraaf
- `TERM-002F`: Ontologie
- `TERM-002G`: Taxonomie
- `TERM-014A`: Semantische gelijkenis
- `TERM-014B`: Semantische verwantschap
- `TERM-016G`: Entity Disambiguation
- Cosine Similarity *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-017, SRC-019, SRC-042, SRC-043, SRC-044
