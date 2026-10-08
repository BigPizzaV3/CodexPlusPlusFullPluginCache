---
term_id: TERM-012A
preferred_name_nl: Representative Query
english_name: Representative Query
cluster_id: 2
cluster_name: Zoekintentie en queryverwerking
type_context: Queryverwerking / clustering
evidence_labels:
- D
- E
last_checked: '2026-07-25'
source_ids:
- SRC-020
- SRC-021
- SRC-036
related_term_ids:
- TERM-005A
- TERM-012B
- TERM-012C
status: active
---

# Representative Query

**Engelse term of afkorting:** Representative Query  
**Term-ID:** `TERM-012A`  
**Hoofdcategorie:** 2 Zoekintentie en queryverwerking  
**Type en context:** Queryverwerking / clustering  
**Bewijsbasis:** D en E  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een Representative Query is een zoekopdracht of synthetische formulering die wordt gekozen om een cluster van verwante queries functioneel te vertegenwoordigen. De representant kan bijvoorbeeld een medoid, populaire query, goed presterende query of door het systeem samengestelde query zijn. Hij hoeft niet de breedste of meest algemene query te zijn.

## Hoe een representant kan worden gekozen

| Methode | Uitleg | Gevolg |
| --- | --- | --- |
| Medoid of clustercentrum | De query ligt volgens de gekozen afstand centraal tussen andere clusterleden. | Hoeft niet de grootste zoekvraag of meest natuurlijke titel te zijn. |
| Populariteit | De query heeft veel zoekvolume of sterke groei binnen het cluster. | Populair is niet automatisch het duidelijkst of inhoudelijk volledigst. |
| Prestatie | De query wordt gekozen op basis van meetbare resultaten in het beschreven systeem. | De prestatiemaatstaf kan systeem- en periodegebonden zijn. |
| Synthetisch | Een nieuwe formulering vat het cluster samen zonder letterlijk als zoekopdracht voor te komen. | Bruikbaar als label, maar geen bewezen echte gebruikersquery. |
| Redactioneel | Een onderzoeker kiest de duidelijkste omschrijving van de gedeelde taak. | Vraagt menselijke beoordeling en documentatie. |

Het Google-patent over queryclustering beschrijft meerdere mogelijkheden voor de keuze van een representative query, waaronder populariteit, prestaties, een clustercentrum en een synthetische query. Daarmee is de oude regel dat een representative query altijd breder is aantoonbaar te beperkt. [SRC-020]

## Voorbeeld

| Clusterleden | Mogelijke representative query | Waarom |
| --- | --- | --- |
| scootmobiel in auto; opvouwbare scootmobiel kofferbak; lichtgewicht scootmobiel meenemen | Opvouwbare scootmobiel voor in de auto | Synthetische, natuurlijke formulering die de gedeelde gebruikerstaak samenvat. |
| scootmobiel 25 km; snelle scootmobiel 25 km/u; 25 km scootmobiel | Scootmobiel 25 km/u | Korte centrale term, maar aanvullende context blijft nodig voor regelgeving en modelkeuze. |

## Wat is bevestigd?

- Representative queries kunnen binnen queryclustering worden gebruikt om redundantie te beperken en clusters te presenteren. [SRC-020]

- De representant kan op verschillende selectiecriteria berusten. [SRC-020]

- Queryclusters kunnen verschillende intenties of aspecten van een oorspronkelijke query samenvatten. [SRC-021]

## Wat is niet bevestigd?

- Dat een representative query per definitie breder, korter of algemener is dan alle clusterleden.

- Dat de gekozen representant automatisch de beste paginatitel, hoofdzoekterm of URL is.

- Dat Google publiek één representative query voor ieder SEO-onderwerp beschikbaar stelt.

- Dat iedere SEO-tool dezelfde representant kiest of dezelfde clustering gebruikt.

## Praktische toepassing

1. Gebruik een representative query als intern clusterlabel of onderzoeksanker.

2. Leg vast hoe de representant is gekozen, bijvoorbeeld redactioneel, via SERP-overlap, embeddings of populariteit.

3. Controleer of de formulering de gedeelde gebruikerstaak correct weergeeft zonder belangrijke context te verliezen.

4. Gebruik niet automatisch één pagina voor alle clusterleden. Beoordeel zelfstandige taken en bewijsvormen.

5. Herzie de representant wanneer het cluster, taalgebruik of productaanbod duidelijk verandert.

## Veelgemaakte misvatting

“De representative query is altijd de breedste head term.” Een representant is de gekozen vertegenwoordiger van een cluster. Die keuze kan centraal, populair, synthetisch of redactioneel zijn en zegt op zichzelf niets over zoekwoordlengte.

## Zie ook

Query Cluster, Represented Query, Canonical Query, Medoid, Cluster Center, Parent Topic en Seed Query.

## Verwante begrippen

- `TERM-005A`: Query Cluster
- `TERM-012B`: Represented Query
- `TERM-012C`: Canonical Query
- Cluster Center *(verwant concept buiten deze begrippenlijst)*
- Medoid *(verwant concept buiten deze begrippenlijst)*
- Parent Topic *(verwant concept buiten deze begrippenlijst)*
- Seed Query *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-020, SRC-021, SRC-036
