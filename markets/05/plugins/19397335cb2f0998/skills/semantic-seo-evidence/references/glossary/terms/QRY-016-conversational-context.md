---
term_id: QRY-016
preferred_name_nl: Conversational Context
english_name: Conversational Context / Gesprekscontext
cluster_id: 2
cluster_name: Zoekintentie en queryverwerking
type_context: Conversational search / NLP
evidence_labels:
- D
- B
last_checked: '2026-07-25'
source_ids:
- SRC-084
- SRC-113
- SRC-121
related_term_ids:
- QRY-013
- QRY-017
- TERM-016H
- TERM-017B
- TERM-021B
status: active
---

# Conversational Context

**Engelse term of afkorting:** Conversational Context / Gesprekscontext  
**Term-ID:** `QRY-016`  
**Hoofdcategorie:** 2 Zoekintentie en queryverwerking  
**Type en context:** Conversational search / NLP  
**Bewijsbasis:** D en B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Conversational Context is informatie uit eerdere beurten, rollen en gedeelde verwijzingen die nodig is om de huidige vraag in een gesprek correct te begrijpen.

## Afbakening

Een korte vervolgvraag kan zonder eerdere context onvolledig zijn. Gesprekscontext kan entiteiten, keuzes, beperkingen en doelen uit eerdere beurten meenemen.

## Wat is bevestigd?

- Conversational-searchonderzoek toont dat eerdere beurten nodig kunnen zijn om actuele vragen te herschrijven of op te lossen.

- Zoekassistenten kunnen vervolgvragen in de context van een gesprek beantwoorden.

## Wat is niet bevestigd?

- Dat alle eerdere informatie altijd relevant blijft.

- Dat ieder platform dezelfde hoeveelheid of soort gespreksgeschiedenis gebruikt.

## Praktische toepassing

1. Maak zelfstandige kernfeiten duidelijk genoeg om ook buiten één gesprek te begrijpen.

2. Leg verwijzingen als “die”, “de tweede” en “dat model” zorgvuldig vast.

3. Test belangrijke vragen zowel zelfstandig als in een logische vervolgreeks.

## Voorbeeld

Na “vergelijk de On Four met de City Cruiser” kan “welke heeft de kleinste draaicirkel?” alleen correct worden geïnterpreteerd met de eerdere modelcontext.

## Veelgemaakte misvatting

Conversational Context is niet hetzelfde als onbeperkt alle oude beurten meenemen. Onjuiste of verouderde context kan het antwoord verslechteren.

## Zie ook

- Session Context

- Coreference Resolution

- Query Rewriting

- Context Window

- Gebruikerstaak

## Verwante begrippen

- `QRY-013`: Query Rewriting
- `QRY-017`: Session Context
- `TERM-016H`: Coreference Resolution
- `TERM-017B`: Context Window
- `TERM-021B`: Gebruikerstaak

## Bronnen en actualiteit

**Kernbronnen:** SRC-084, SRC-113, SRC-121

**Update-trigger:** Nieuwe conversational-searchonderzoeken of platformwijzigingen.
