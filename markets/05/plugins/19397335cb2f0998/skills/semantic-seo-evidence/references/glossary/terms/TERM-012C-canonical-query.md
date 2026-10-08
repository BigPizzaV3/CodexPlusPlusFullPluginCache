---
term_id: TERM-012C
preferred_name_nl: Canonical Query
english_name: Canonical Query
cluster_id: 2
cluster_name: Zoekintentie en queryverwerking
type_context: Queryverwerking / normalisatie / frameworkgebruik
evidence_labels:
- E
- F
last_checked: '2026-07-25'
source_ids:
- SRC-008
- SRC-020
- SRC-045
related_term_ids:
- ENT-010
- QRY-013
- QRY-014
- TEC-021
- TERM-012A
status: active
---

# Canonical Query

**Engelse term of afkorting:** Canonical Query  
**Term-ID:** `TERM-012C`  
**Hoofdcategorie:** 2 Zoekintentie en queryverwerking  
**Type en context:** Queryverwerking / normalisatie / frameworkgebruik  
**Bewijsbasis:** E en F  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Canonical Query is een contextafhankelijke term voor een gestandaardiseerde, genormaliseerde of voorkeursvorm van één of meer queryvarianten. De exacte betekenis verschilt per systeem. Een canonical query is niet automatisch hetzelfde als een representative query en er bestaat geen openbaar universeel Google-register met één canonical query per onderwerp.

## Mogelijke betekenissen

| Gebruik | Wat wordt gecanonicaliseerd? | Voorbeeld |
| --- | --- | --- |
| Spelling en afkorting | Varianten worden naar een standaardvorm gebracht. | “scoot mobiel” en “scootmobiel”; “km per uur” en “km/u” in een intern systeem. |
| Entiteit of locatie | Verschillende schrijfwijzen worden aan dezelfde entiteit of plaats gekoppeld. | Merk- en modelnaam met een stabiele identifier. |
| Natuurlijke vraag | Een korte of onvolledige query wordt omgezet in een welgevormde vraag. | “on four bereik” wordt intern bijvoorbeeld “Wat is het bereik van de For Motion On Four?”. |
| Frameworkvoorkeur | Een centrale formulering wordt gekozen voor onderzoek en contentplanning. | Voorkeursvraag die de gebruikerstaak duidelijk omschrijft. |

Een actief Google-patent beschrijft het canonicaliseren van zoekqueries naar welgevormde natuurlijke-taalvragen. Dit bewijst een beschreven Google-techniek binnen de reikwijdte van het patent, niet dat ieder Google-product of iedere query op dezelfde manier wordt verwerkt. [SRC-045]

## Verschil met Representative Query

| Begrip | Hoofdfunctie | Kan synthetisch zijn? |
| --- | --- | --- |
| Canonical Query | Varianten normaliseren of één voorkeursvorm bepalen. | Ja, afhankelijk van systeem of framework. |
| Representative Query | Een cluster van mogelijk verschillende queries vertegenwoordigen. | Ja, een patent beschrijft ook synthetische representanten. |
| Seed Query | Startpunt voor uitbreiding, onderzoek of clustering. | Meestal een gekozen bestaande of redactionele startquery. |

## Wat is bevestigd?

- Querycanonicalisatie en normalisatie zijn echte queryverwerkingstechnieken met verschillende toepassingen. [SRC-045]

- Een Google-patent beschrijft canonicalisatie naar natuurlijke-taalvragen. [SRC-045]

- Koray gebruikt Canonical Query binnen een bredere Semantic Search-uitleg. [SRC-008]

## Wat is niet bevestigd?

- Dat Canonical Query overal exact dezelfde technische betekenis heeft.

- Dat Google voor ieder onderwerp één openbare canonical query aanwijst.

- Dat de canonical query automatisch de beste paginatitel of hoofdterm is.

- Dat iedere queryvariant na canonicalisatie exact dezelfde zoekresultaten moet krijgen.

## Praktische toepassing

1. Gebruik een canonical query intern om spelling, modelnamen en taakformuleringen consistent te beheren.

2. Bewaar daarnaast de echte queryvarianten en context. Normalisatie mag waardevolle verschillen niet verbergen.

3. Koppel product- en merkvarianten aan stabiele identifiers in plaats van alleen aan een tekstuele voorkeursquery.

4. Noem in audits altijd welke betekenis van canonical query wordt gebruikt.

## Veelgemaakte misvatting

“Canonical Query werkt zoals een canonical URL en Google kiest één officiële query.” De overeenkomst zit alleen in het idee van een voorkeurs- of genormaliseerde vorm. Queryverwerking en URL-canonicalisatie zijn verschillende technische problemen.

## Zie ook

Query Normalization, Query Rewriting, Query Expansion, Representative Query, Entity Resolution, Canonical URL en Stable Identifier.

## Verwante begrippen

- `ENT-010`: Entity Resolution
- `QRY-013`: Query Rewriting
- `QRY-014`: Query Expansion
- `TEC-021`: Canonical URL
- `TERM-012A`: Representative Query
- Query Normalization *(verwant concept buiten deze begrippenlijst)*
- Stable Identifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-008, SRC-020, SRC-045
