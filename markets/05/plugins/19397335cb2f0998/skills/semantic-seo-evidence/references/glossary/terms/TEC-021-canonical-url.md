---
term_id: TEC-021
preferred_name_nl: Canonical URL
english_name: Canonical URL / Voorkeurs-URL
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Crawling en indexering
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-104
- SRC-110
related_term_ids:
- TEC-025
status: active
---

# Canonical URL

**Engelse term of afkorting:** Canonical URL / Voorkeurs-URL  
**Term-ID:** `TEC-021`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Crawling en indexering  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een canonical URL is de URL die een zoekmachine als representatieve versie binnen een groep dubbele of sterk vergelijkbare URL’s behandelt.

## Afbakening

Website-eigenaren kunnen canonical-signalen geven via rel=canonical, redirects, sitemaps en consistente interne links. Google kan uiteindelijk een andere canonical selecteren.

## Wat is bevestigd?

- Google groepeert duplicaten en selecteert een canonical URL.

- rel=canonical is een sterk signaal, geen absolute opdracht.

## Wat is niet bevestigd?

- Dat canonicalisatie duplicate content uit de bron verwijdert.

- Dat alle variant-URL’s altijd naar één generieke pagina moeten canonicaliseren.

## Praktische toepassing

1. Kies per inhoudelijke hoofdversie een zelfverwijzende canonical waar passend.

2. Laat interne links en sitemap dezelfde voorkeurs-URL ondersteunen.

3. Behoud afzonderlijke URL’s wanneer varianten zelfstandige, indexeerbare waarde hebben.

## Voorbeeld

Print- en trackingvarianten kunnen naar de hoofd-URL canonicaliseren, terwijl een productvariant met eigen prijs en beschikbaarheid mogelijk zelfstandig blijft.

## Veelgemaakte misvatting

Canonical is geen noindex en geen garantie dat Google de gekozen URL volgt.

## Zie ook

- Canonicalization

- Duplicate Content

- Product Variant

- XML Sitemap

- Internal Links

## Verwante begrippen

- `TEC-025`: XML Sitemap
- Duplicate Content *(verwant concept buiten deze begrippenlijst)*
- Internal Links *(verwant concept buiten deze begrippenlijst)*
- Product Variant *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-104, SRC-110

**Update-trigger:** URL-migratie, variantbeleid of onverwachte canonicalselectie in Search Console.
