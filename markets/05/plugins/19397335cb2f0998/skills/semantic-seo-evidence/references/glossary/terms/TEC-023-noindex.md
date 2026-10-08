---
term_id: TEC-023
preferred_name_nl: noindex
english_name: noindex
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Indexeringsbeheer
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-106
- SRC-107
- SRC-112
related_term_ids:
- AIS-017
- TEC-021
- TEC-022
- TEC-027
status: active
---

# noindex

**Engelse term of afkorting:** noindex  
**Term-ID:** `TEC-023`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Indexeringsbeheer  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

noindex is een indexeringsinstructie in een robots-meta-element of X-Robots-Tag waarmee ondersteunende zoekmachines wordt gevraagd een URL of resource niet in resultaten op te nemen.

## Afbakening

De crawler moet de instructie kunnen lezen. Een URL die tegelijk via robots.txt is geblokkeerd kan de noindex-regel mogelijk niet laten verwerken.

## Wat is bevestigd?

- Google verwijdert een gecrawlde URL met geldige noindex uit Search.

- OpenAI adviseert noindex wanneer ook een link en titel niet in ChatGPT Search gewenst zijn.

## Wat is niet bevestigd?

- Dat noindex in robots.txt door Google wordt ondersteund.

- Dat noindex de content beveiligt of iedere externe kopie verwijdert.

## Praktische toepassing

1. Gebruik meta robots voor HTML en X-Robots-Tag voor andere bestanden.

2. Laat crawling toe totdat de regel is verwerkt.

3. Controleer gevolgen voor interne links, structured data en AI-searchdoelen.

## Voorbeeld

Een interne zoekresultatenpagina kan noindex krijgen wanneer zij geen zelfstandige zoekwaarde heeft.

## Veelgemaakte misvatting

noindex is niet hetzelfde als Disallow. De ene regelt indexering, de andere crawling.

## Zie ook

- robots.txt

- Indexability

- X-Robots-Tag

- Canonical URL

- AI Crawler Policy

## Verwante begrippen

- `AIS-017`: AI Crawler Policy
- `TEC-021`: Canonical URL
- `TEC-022`: robots.txt
- `TEC-027`: Indexability
- X-Robots-Tag *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-106, SRC-107, SRC-112

**Update-trigger:** Wijziging in publicatiebeleid, platformondersteuning of indexeringsstatus.
