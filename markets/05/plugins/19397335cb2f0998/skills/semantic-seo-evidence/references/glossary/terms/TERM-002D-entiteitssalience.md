---
term_id: TERM-002D
preferred_name_nl: Entiteitssalience
english_name: Entity Salience
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: NLP / documentanalyse
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-061
- SRC-071
related_term_ids:
- TERM-002
- TERM-002A
- TERM-008
- TERM-019
status: active
---

# Entiteitssalience

**Engelse term of afkorting:** Entity Salience  
**Term-ID:** `TERM-002D`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** NLP / documentanalyse  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Entiteitssalience is de geschatte prominentie, centraliteit of samenvattingswaardigheid van een entiteit binnen een document, passage, taak of model. Salience is model- en contextafhankelijk en is niet hetzelfde als frequentie, waarheid, expertise of een algemene Google-rankingfactor.

## Waar kan salience op berusten?

| Mogelijke aanwijzing | Waarom relevant | Belangrijke grens |
| --- | --- | --- |
| Rol in de hoofdboodschap | De entiteit is nodig om het document samen te vatten | Samenvattingen en genres kunnen anders wegen. |
| Positie en discoursrol | Introductie, onderwerp of terugkerend referentiepunt | Eerste vermelding alleen is niet beslissend. |
| Aantal en spreiding van mentions | De entiteit komt in meerdere relevante secties terug | Frequentie kan ook boilerplate of herhaling zijn. |
| Relaties met andere kernentiteiten | De entiteit verbindt belangrijke feiten en gebeurtenissen | Veel relaties betekenen niet automatisch belangrijkheid. |
| Modelscore | Een API geeft een numerieke salienceschatting | Score is alleen interpreteerbaar binnen dat model en document. |

## Wat is bevestigd?

- Google Cloud Entity Analysis documenteert een saliencescore voor de belangrijkheid of centraliteit van een entiteit in de gehele aangeleverde tekst. [SRC-061]

- GUMsley behandelt salience als een taakafhankelijk begrip en gebruikt menselijke samenvattingen als strikte operationele definitie. [SRC-071]

- Entiteitssalience is relevant voor onder meer samenvatting en Information Retrieval, maar modellen kunnen belangrijke entiteiten missen. [SRC-071]

## Wat is niet bevestigd?

- Dat Google Search één openbare Entity Salience Score voor webpagina’s gebruikt.

- Dat vaker noemen altijd een hogere of betere salience oplevert.

- Dat de meest opvallende entiteit automatisch de meest relevante entiteit voor iedere query is.

- Dat salience bewijst dat een claim waar, actueel of deskundig is.

## Praktische toepassing

1. Controleer of de primaire entiteit en hoofdtaak in titel, introductie en kernsecties herkenbaar blijven.

2. Verminder boilerplate of zijpaden die de hoofdboodschap onnodig vertroebelen.

3. Gebruik geen frequentiequota; beoordeel inhoudelijke rol, spreiding en duidelijkheid.

4. Leg bij automatische salienceanalyse het model, de tekstversie en de scorecontext vast.

## Veelgemaakte misvatting

De entiteit met de meeste vermeldingen is automatisch de centrale entiteit. Salience kan afhangen van rol, structuur, context en taak, niet alleen telling.

## Zie ook

Entiteit, Entiteitsvermelding, Central Entity, Macrosemantiek en Documentstructuur.

## Verwante begrippen

- `TERM-002`: Entiteit
- `TERM-002A`: Entiteitsvermelding
- `TERM-008`: Macrosemantiek
- `TERM-019`: Central Entity
- Documentstructuur *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-061, SRC-071
