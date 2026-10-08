---
term_id: TERM-023
preferred_name_nl: Contextual Domain
english_name: Contextual Domain
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Frameworkterm / context- en betekenisanalyse
evidence_labels:
- D
- F
last_checked: '2026-07-25'
source_ids:
- SRC-007
- SRC-009
- SRC-052
- SRC-082
- SRC-084
- SRC-085
related_term_ids:
- TERM-016G
- TERM-021B
- TERM-022
- TERM-024
- TERM-024A
status: active
---

# Contextual Domain

**Engelse term of afkorting:** Contextual Domain  
**Term-ID:** `TERM-023`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Frameworkterm / context- en betekenisanalyse  
**Bewijsbasis:** D en F  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een Contextual Domain is binnen het onderzochte framework het interpretatiekader waarin een term, query of informatiebehoefte betekenis krijgt. Het combineert het relevante kennisgebied met de concrete gebruikssituatie, taak en andere context die nodig is om een passende interpretatie te kiezen.

## Relatie met context en disambiguatie

Context kan worden opgevat als informatie die de situatie van relevante entiteiten karakteriseert. [SRC-084]

Word Sense Disambiguation gaat over het computationeel bepalen welke betekenis van een woord binnen de gegeven context bedoeld is. [SRC-085]

Taakcontext kan helpen queries te verfijnen of ondubbelzinnig te maken en resultaten op taakrelevantie te beoordelen. [SRC-082]

Contextual Domain is zelf geen algemeen erkende vaste NLP-laag. Het is een frameworkterm die deze verwante ideeën vertaalt naar contentplanning. [SRC-007; SRC-009]

## Verschil met een kennisdomein

Een kennisdomein is het relatief stabiele vakgebied met eigen entiteiten, terminologie en bewijsstandaarden.

Een Contextual Domain is de betekenis- en gebruikssituatie waarin een woord of vraag op dat moment wordt geïnterpreteerd.

Hetzelfde woord kan binnen verschillende contextual domains naar andere entiteiten of taken verwijzen.

## Voorbeeld van dubbelzinnigheid

Apple kan in een technologisch kader verwijzen naar Apple Inc. en producten zoals iPhone of MacBook.

In een voedingskader kan hetzelfde woord verwijzen naar fruit, voedingswaarde of teelt.

De omliggende woorden, gebruikerstaak, taal, bron en verdere sessiecontext helpen de bedoelde betekenis bepalen. Dit betekent niet dat iedere zoekmachine daarvoor een object met de officiële naam Contextual Domain aanmaakt.

## Wat is niet bevestigd?

- Dat Google een afzonderlijke Contextual Domain-score publiceert of gebruikt volgens de exacte frameworkdefinitie.

- Dat dwell time, bouncepercentage of klikgedrag een eenvoudige directe maat voor het juiste contextual domain zijn.

- Dat één toon, woordenschat of structuur voor alle gebruikers binnen hetzelfde domein optimaal is.

## Praktische toepassing

1. Noteer mogelijke betekenissen en entiteiten wanneer een term dubbelzinnig is.

2. Bepaal de taak, doelgroep, locatie, tijd en andere kwalificaties die het antwoord werkelijk veranderen.

3. Gebruik voldoende expliciete context om verkeerde interpretatie te voorkomen.

4. Beoordeel gebruikersreacties als taak- en UX-uitkomst, niet als eenvoudige rankingformule.

5. Kies alleen een aparte pagina wanneer de interpretatie een zelfstandige taak, dataset of bewijsbasis oplevert.

## Praktijkvoorbeeld

| Term | Contextual Domain | Bedoelde betekenis |
| --- | --- | --- |
| Pride | Scootmobielmodellen | Een specifiek model of productnaam. |
| Pride | Maatschappelijke evenementen | Een evenement of beweging. |
| Bereik | Scootmobielgebruik | Afstand onder bepaalde accu- en gebruiksomstandigheden. |
| Bereik | Communicatie of media | Aantal bereikte personen. |

## Veelgemaakte misvatting

Contextual Domain is een officiële Google-categorie die rechtstreeks uit bouncepercentage of dwell time wordt berekend. Het is een contextueel planningsmodel, geen gepubliceerde score.

## Zie ook

- Kennisdomein

- Contextual Layer

- Contextuele kwalificatie

- Word Sense Disambiguation

- Entity Disambiguation

- Gebruikerstaak

## Verwante begrippen

- `TERM-016G`: Entity Disambiguation
- `TERM-021B`: Gebruikerstaak
- `TERM-022`: Kennisdomein
- `TERM-024`: Contextual Layer
- `TERM-024A`: Contextuele kwalificatie
- Word Sense Disambiguation *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-007, SRC-009, SRC-052, SRC-082, SRC-084, SRC-085
