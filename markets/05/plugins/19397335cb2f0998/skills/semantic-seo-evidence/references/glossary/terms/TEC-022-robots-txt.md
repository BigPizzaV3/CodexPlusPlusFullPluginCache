---
term_id: TEC-022
preferred_name_nl: robots.txt
english_name: Robots Exclusion Protocol / robots.txt
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Crawlerbeheer
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-105
- SRC-110
related_term_ids:
- AIS-017
- AIS-018
- AIS-019
- TEC-023
- TEC-026
status: active
---

# robots.txt

**Engelse term of afkorting:** Robots Exclusion Protocol / robots.txt  
**Term-ID:** `TEC-022`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Crawlerbeheer  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

robots.txt is een bestand op hostniveau waarmee ondersteunde crawlers instructies krijgen over welke URL-paden zij wel of niet mogen opvragen.

## Afbakening

Het bestand beheert crawlen, niet rechtstreeks indexering. Een geblokkeerde URL kan onder omstandigheden als URL zonder inhoud in resultaten bekend blijven.

## Wat is bevestigd?

- Google documenteert robots.txt als crawlcontrole.

- Regels zijn crawler- en padgebonden en worden per host gelezen.

## Wat is niet bevestigd?

- Dat Disallow gelijkstaat aan noindex.

- Dat robots.txt vertrouwelijke informatie beveiligt.

## Praktische toepassing

1. Blokkeer alleen URL’s waarvan crawling werkelijk onnodig of ongewenst is.

2. Gebruik noindex voor indexeringsuitsluiting wanneer de crawler de regel kan lezen.

3. Controleer afzonderlijke AI- en trainingscrawlers op hun officiële user-agent.

## Voorbeeld

Een filterruimte kan voor bepaalde crawlers worden geblokkeerd om onnodige crawlvarianten te beperken, maar privédata moet achter toegangscontrole staan.

## Veelgemaakte misvatting

robots.txt is geen beveiligingsmaatregel en geen algemene toestemming voor contentgebruik.

## Zie ook

- Crawlability

- noindex

- AI Crawler Policy

- OAI-SearchBot

- GPTBot

## Verwante begrippen

- `AIS-017`: AI Crawler Policy
- `AIS-018`: OAI-SearchBot
- `AIS-019`: GPTBot
- `TEC-023`: noindex
- `TEC-026`: Crawlability

## Bronnen en actualiteit

**Kernbronnen:** SRC-105, SRC-110

**Update-trigger:** Nieuw crawlerbeleid, sitearchitectuur of platformuser-agent.
