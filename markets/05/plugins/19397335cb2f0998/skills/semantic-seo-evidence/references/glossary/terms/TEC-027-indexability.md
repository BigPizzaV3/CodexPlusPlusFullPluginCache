---
term_id: TEC-027
preferred_name_nl: Indexability
english_name: Indexability / Indexeerbaarheid
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Indexering
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-104
- SRC-106
- SRC-110
related_term_ids:
- AIS-013
- TEC-021
- TEC-023
- TEC-026
- TEC-028
status: active
---

# Indexability

**Engelse term of afkorting:** Indexability / Indexeerbaarheid  
**Term-ID:** `TEC-027`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Indexering  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Indexability is de technische en beleidsmatige mogelijkheid dat een zoekmachine een URL en inhoud in zijn index opneemt.

## Afbakening

Een crawlbare pagina kan door noindex, canonicalisatie, duplicatie, foutstatus of andere verwerking niet als zelfstandige indexversie worden opgenomen.

## Wat is bevestigd?

- Google behandelt crawling, verwerking, canonicalisatie en indexering als afzonderlijke onderwerpen.

- noindex en canonical-signalen kunnen de indexstatus beïnvloeden.

## Wat is niet bevestigd?

- Dat indexeerbaar gelijkstaat aan daadwerkelijk geïndexeerd.

- Dat een geïndexeerde URL voor relevante queries automatisch zichtbaar wordt.

## Praktische toepassing

1. Controleer statuscode, robotsmeta, canonical en inhoud.

2. Gebruik URL Inspection en indexeringsrapporten voor diagnose.

3. Houd alleen URL’s indexeerbaar die zelfstandige waarde en duidelijke ownership hebben.

## Voorbeeld

Een pagina kan crawlbaar en technisch indexeerbaar zijn, maar als duplicaat worden samengevoegd met een andere canonical.

## Veelgemaakte misvatting

Indexability is een voorwaarde, geen kwaliteits- of rankinggarantie.

## Zie ook

- Crawlability

- Canonical URL

- noindex

- Rendering

- Source Eligibility

## Verwante begrippen

- `AIS-013`: Source Eligibility
- `TEC-021`: Canonical URL
- `TEC-023`: noindex
- `TEC-026`: Crawlability
- `TEC-028`: Rendering

## Bronnen en actualiteit

**Kernbronnen:** SRC-104, SRC-106, SRC-110

**Update-trigger:** Indexeringsprobleem, templatewijziging of canonicalconflict.
