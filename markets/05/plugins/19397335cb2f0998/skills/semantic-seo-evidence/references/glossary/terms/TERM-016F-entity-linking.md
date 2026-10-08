---
term_id: TERM-016F
preferred_name_nl: Entity Linking
english_name: Entity Linking
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Entiteitsverwerking, kennisbanken en identifiers
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-051
- SRC-052
related_term_ids:
- TERM-003A
- TERM-016E
- TERM-016G
- TERM-016H
status: active
---

# Entity Linking

**Engelse term of afkorting:** Entity Linking  
**Term-ID:** `TERM-016F`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Entiteitsverwerking, kennisbanken en identifiers  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Entity linking is het koppelen van een tekstvermelding aan een specifieke entiteit of identifier in een kennisbron, wanneer een passende entiteit beschikbaar en voldoende aannemelijk is.

## Uitgebreide uitleg

Entity linking bouwt voort op mentiondetectie. Een systeem zoekt kandidaatentiteiten, vergelijkt de mention en context met die kandidaten en kiest vervolgens een koppeling of besluit dat geen geschikte entiteit beschikbaar is.

De kennisbron bepaalt welke entiteiten en identifiers kunnen worden gekozen. Dezelfde tekst kan in verschillende knowledge bases anders worden gekoppeld of helemaal niet voorkomen.

Modellen gebruiken vaak lokale context, documentcontext, kandidaatpopulariteit, embeddings en relaties met andere mentions. Entity disambiguation vormt daardoor vaak een belangrijk onderdeel van linking.

Een correcte koppeling helpt informatie over dezelfde entiteit samen te brengen. Een foute koppeling kan juist kenmerken van verschillende personen, producten of organisaties vermengen.

## Technische onderdelen

| Fase | Functie | Risico |
| --- | --- | --- |
| Mentiondetectie | vinden welke tekst een entiteit kan noemen | mention gemist of grens fout |
| Kandidaatgeneratie | mogelijke knowledge-base-entiteiten verzamelen | juiste kandidaat ontbreekt |
| Disambiguatie en scoring | context met kandidaten vergelijken | populaire maar verkeerde entiteit gekozen |
| Link of NIL-besluit | identifier toewijzen of geen koppeling maken | onterecht koppelen of onterecht NIL |

## Voorbeeld

De naam “Pride” kan verwijzen naar een algemeen begrip, een evenement, een organisatie of een product. In een tekst met “Nipponia”, “driewielscooter”, “650 watt” en een product-ID wordt de bedoelde productentiteit duidelijker. De uiteindelijke koppeling blijft afhankelijk van de kennisbron en het model.

## Wat is bevestigd?

- Entity linking combineert mentiondetectie, kandidaatentiteiten en disambiguatie.

- Contextuele representaties en entity embeddings kunnen bij de keuze tussen kandidaten worden gebruikt.

- Een systeem kan een NIL- of niet-gelinkte uitkomst nodig hebben wanneer geen geschikte entiteit beschikbaar is.

## Wat is niet bevestigd?

- Een uitgever kan niet garanderen dat Google, ChatGPT of een ander platform dezelfde identifier kiest.

- Het toevoegen van sameAs of structured data dwingt geen entity link af.

- Een interne product-ID is niet automatisch een wereldwijd herkende knowledge-graph-ID.

## Praktische toepassing

- Gebruik stabiele interne identifiers en consistente officiële namen voor merken, modellen en varianten.

- Koppel productpagina’s, structured data, feeds en video’s aan dezelfde feitenbasis.

- Noem bij dubbelzinnige modellen vroeg merk, producttype en onderscheidende kenmerken.

- Controleer of opvolgers, uitvoeringen en accuconfiguraties niet onder één onduidelijke naam worden samengevoegd.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Entity linking is hetzelfde als een interne link naar een andere webpagina. Het gaat om een semantische koppeling van een mention aan een entiteitsidentifier, niet om hyperlinkarchitectuur. |
| --- |

## Zie ook

TERM-016E Named Entity Recognition, TERM-016G Entity Disambiguation, TERM-016H Coreference Resolution, TERM-003A RDF-triple.

## Verwante begrippen

- `TERM-003A`: RDF-triple
- `TERM-016E`: Named Entity Recognition
- `TERM-016G`: Entity Disambiguation
- `TERM-016H`: Coreference Resolution

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-051, SRC-052
