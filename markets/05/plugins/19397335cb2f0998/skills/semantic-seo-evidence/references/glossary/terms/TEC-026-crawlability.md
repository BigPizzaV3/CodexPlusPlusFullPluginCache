---
term_id: TEC-026
preferred_name_nl: Crawlability
english_name: Crawlability / Crawlbaarheid
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Crawling
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-068
- SRC-105
- SRC-110
related_term_ids:
- AIS-017
- TEC-022
- TEC-025
- TEC-027
- TEC-028
status: active
---

# Crawlability

**Engelse term of afkorting:** Crawlability / Crawlbaarheid  
**Term-ID:** `TEC-026`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Crawling  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Crawlability is de mate waarin een crawler een URL kan ontdekken, opvragen en de relevante response kan bereiken.

## Afbakening

Crawlbaarheid wordt beïnvloed door links, robotsregels, statuscodes, netwerktoegang, authenticatie, URL-structuur en crawlerbeleid.

## Wat is bevestigd?

- Google documenteert crawling als afzonderlijke fase vóór verwerking en indexering.

- Crawlbare links en sitemaps kunnen ontdekking ondersteunen.

## Wat is niet bevestigd?

- Dat crawlbaarheid automatisch indexering of ranking betekent.

- Dat iedere technisch bereikbare URL door iedere crawler wordt bezocht.

## Praktische toepassing

1. Gebruik crawlbare interne links en correcte statuscodes.

2. Controleer robots.txt, authenticatie en serverfouten.

3. Beheer verschillende crawlers per doel en prioriteit.

## Voorbeeld

Een productpagina met status 200 en interne links kan crawlbaar zijn, maar door noindex alsnog niet indexeerbaar.

## Veelgemaakte misvatting

Crawlability is niet hetzelfde als toegankelijkheid voor menselijke gebruikers of indexability.

## Zie ook

- Indexability

- Rendering

- robots.txt

- XML Sitemap

- AI Crawler Policy

## Verwante begrippen

- `AIS-017`: AI Crawler Policy
- `TEC-022`: robots.txt
- `TEC-025`: XML Sitemap
- `TEC-027`: Indexability
- `TEC-028`: Rendering

## Bronnen en actualiteit

**Kernbronnen:** SRC-068, SRC-105, SRC-110

**Update-trigger:** Nieuwe sitearchitectuur, serverwijziging of crawlproblemen.
