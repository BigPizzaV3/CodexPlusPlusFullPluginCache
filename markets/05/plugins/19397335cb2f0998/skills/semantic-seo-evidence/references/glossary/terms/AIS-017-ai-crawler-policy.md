---
term_id: AIS-017
preferred_name_nl: AI Crawler Policy
english_name: AI Crawler Policy / AI-crawlerbeleid
cluster_id: 8
cluster_name: AI Search
type_context: Technisch beleid / governance
evidence_labels:
- B
last_checked: '2026-07-25'
source_ids:
- SRC-105
- SRC-112
- SRC-115
- SRC-116
related_term_ids:
- AIS-013
- AIS-018
- AIS-019
- TEC-022
status: active
---

# AI Crawler Policy

**Engelse term of afkorting:** AI Crawler Policy / AI-crawlerbeleid  
**Term-ID:** `AIS-017`  
**Hoofdcategorie:** 8 AI Search  
**Type en context:** Technisch beleid / governance  
**Bewijsbasis:** B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een AI-crawlerbeleid legt per crawler en gebruiksdoel vast of en onder welke voorwaarden content mag worden opgehaald voor zoeken, gebruikersacties, indexering of modeltraining.

## Afbakening

Verschillende platforms gebruiken afzonderlijke user-agents. Zoektoegang, gebruikersgestuurde toegang en training mogen daarom niet als één keuze worden behandeld.

## Wat is bevestigd?

- OpenAI, Anthropic en Perplexity publiceren verschillende crawlernamen en functies.

- robots.txt kan ondersteunde crawlers per user-agent sturen.

## Wat is niet bevestigd?

- Dat één algemene regel voor ‘alle AI-bots’ altijd passend is.

- Dat robots.txt juridisch alle vormen van hergebruik of reeds verkregen kopieën controleert.

## Praktische toepassing

1. Inventariseer user-agent, doel, gewenste toegang en controlefrequentie.

2. Scheid search, user fetch en training.

3. Test regels en documenteer de bedrijfsbeslissing.

## Voorbeeld

Een organisatie kan OAI-SearchBot toestaan voor ChatGPT Search en GPTBot blokkeren voor mogelijke training.

## Veelgemaakte misvatting

AI-crawlerbeleid is geen eenmalige technische instelling. Namen, doelen en beleid kunnen wijzigen.

## Zie ook

- robots.txt

- OAI-SearchBot

- GPTBot

- Source Eligibility

- Content Governance

## Verwante begrippen

- `AIS-013`: Source Eligibility
- `AIS-018`: OAI-SearchBot
- `AIS-019`: GPTBot
- `TEC-022`: robots.txt
- Content Governance *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-105, SRC-112, SRC-115, SRC-116

**Update-trigger:** Nieuwe crawler, gewijzigde platformvoorwaarden of bedrijfsbeleid.
