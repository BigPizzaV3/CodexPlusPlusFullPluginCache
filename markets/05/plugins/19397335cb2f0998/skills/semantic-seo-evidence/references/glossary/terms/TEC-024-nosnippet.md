---
term_id: TEC-024
preferred_name_nl: nosnippet
english_name: nosnippet
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Snippet- en AI-gebruikbeheer
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-024
- SRC-107
related_term_ids:
- AIS-013
- AIS-017
- TEC-023
status: active
---

# nosnippet

**Engelse term of afkorting:** nosnippet  
**Term-ID:** `TEC-024`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Snippet- en AI-gebruikbeheer  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

nosnippet is een robotsinstructie waarmee Google wordt gevraagd geen tekstsnippet of videovoorbeeld voor een URL te tonen en de inhoud niet als directe invoer voor AI Overviews en AI Mode te gebruiken.

## Afbakening

Met max-snippet kan de tekstlengte worden begrensd en data-nosnippet kan bepaalde HTML-secties uitsluiten van snippets. Deze controles zijn platformspecifiek.

## Wat is bevestigd?

- Google documenteert nosnippet, max-snippet en data-nosnippet voor zoekweergaven en generatieve functies.

- De crawler moet de instructie kunnen lezen.

## Wat is niet bevestigd?

- Dat nosnippet de URL volledig uit de index verwijdert.

- Dat data-nosnippet alle andere toepassingen of externe kopieën controleert.

## Praktische toepassing

1. Bepaal per contenttype welke preview en AI-input wenselijk is.

2. Test effect op gewone snippets en generatieve zichtbaarheid.

3. Gebruik geen snippetbeperking zonder de impact op doorklik en begrip af te wegen.

## Voorbeeld

Een betaalde of gevoelige passage kan met data-nosnippet worden uitgesloten terwijl de rest van de pagina als snippet beschikbaar blijft.

## Veelgemaakte misvatting

nosnippet is geen privacy- of auteursrechtbeveiliging en vervangt geen toegangscontrole.

## Zie ook

- noindex

- data-nosnippet

- AI Crawler Policy

- Source Eligibility

- Robots Meta Tag

## Verwante begrippen

- `AIS-013`: Source Eligibility
- `AIS-017`: AI Crawler Policy
- `TEC-023`: noindex
- data-nosnippet *(verwant concept buiten deze begrippenlijst)*
- Robots Meta Tag *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-024, SRC-107

**Update-trigger:** Platformwijziging of aangepast deelbeleid.
