---
term_id: TERM-017B
preferred_name_nl: Context Window
english_name: Context Window
cluster_id: 4
cluster_name: NLP en taalmodellen
type_context: Taalmodellen, invoerlimieten en long-contextverwerking
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-055
- SRC-062
- SRC-063
related_term_ids:
- AIS-010
- AIS-011
- TERM-016B
- TERM-017A
- TERM-017C
status: active
---

# Context Window

**Engelse term of afkorting:** Context Window  
**Term-ID:** `TERM-017B`  
**Hoofdcategorie:** 4 NLP en taalmodellen  
**Type en context:** Taalmodellen, invoerlimieten en long-contextverwerking  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Een context window is de maximale hoeveelheid invoer en gesprekshistorie, en afhankelijk van de interface mogelijk ook gereserveerde uitvoer, die een model tijdens één verwerking kan meenemen. De limiet wordt meestal in tokens uitgedrukt.

## Uitgebreide uitleg

Het context window bepaalt hoeveel informatie tegelijk beschikbaar kan worden gesteld. De precieze telling verschilt per model en productinterface. Systeeminstructies, hulpmiddeluitvoer, bijlagen, gesprekshistorie en verwachte uitvoer kunnen allemaal een deel van het budget gebruiken.

Contextcapaciteit is niet hetzelfde als effectief gebruik. Onderzoek laat zien dat modellen informatie in het midden van een lange context soms minder betrouwbaar benutten dan informatie aan het begin of einde.

Een context window is ook niet hetzelfde als trainingskennis, een externe zoekindex of blijvend geheugen. Informatie kan tijdens één verzoek beschikbaar zijn zonder later behouden te blijven. Omgekeerd kan een model patronen uit training bevatten die niet in de huidige context staan.

RAG, samenvatting, filtering en hiërarchische verwerking kunnen worden gebruikt om relevante informatie te selecteren. Geen van deze methoden is voor iedere dataset en taak universeel het beste.

## Belangrijke afbakening

| Begrip | Functie | Belangrijke grens |
| --- | --- | --- |
| Context window | hoeveel context tegelijk kan worden aangeboden | capaciteit garandeert geen correcte benutting |
| Trainingskennis | patronen geleerd tijdens training | kan verouderd, onvolledig of niet herleidbaar zijn |
| Retrievalindex | externe collectie waaruit informatie kan worden opgehaald | alleen opgehaalde informatie komt in de actieve context |
| Gespreksgeheugen | door een product bewaarde of samengevatte informatie | productafhankelijk en niet gelijk aan modelcontext |

## Voorbeeld

Een handleiding kan technisch volledig in een groot context window passen. Het model hoeft daardoor nog niet iedere specificatie even goed te vinden, vooral niet wanneer de relevante waarde midden in veel vergelijkbare informatie staat. Duidelijke structuur, retrieval en bronverwijzing blijven belangrijk.

## Wat is bevestigd?

- Generatieve modellen hebben een begrensde hoeveelheid informatie die per verwerking beschikbaar is.

- Een groter context window maakt langere invoer mogelijk.

- Peer-reviewed onderzoek toont dat positie en contextstructuur de effectieve benutting kunnen beïnvloeden.

## Wat is niet bevestigd?

- Een groot context window betekent niet dat alle invoer foutloos wordt onthouden of gebruikt.

- Een volledig document in de context garandeert geen correct antwoord of citaat.

- Er bestaat geen ideale SEO-paginalengte die rechtstreeks uit een modelcontextlimiet volgt.

## Praktische toepassing

- Plaats belangrijke feiten in de relevante sectie en koppel ze aan duidelijke entiteiten, voorwaarden en broninformatie.

- Vertrouw bij grote kennisbanken niet alleen op maximale context, maar evalueer ook retrieval en documentstructuur.

- Vermeld modelversie en contextinstellingen bij technische experimenten.

- Gebruik geen vaste woord- of tokenlimiet als algemene contentregel.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Als een tekst binnen het context window past, kan het model alles erin even goed gebruiken. Capaciteit en effectieve informatiebenutting zijn verschillende eigenschappen. |
| --- |

## Zie ook

TERM-017A Sliding Window, TERM-017C Chunking, TERM-016B Token en tokenisatie, RAG en Grounding.

## Verwante begrippen

- `AIS-010`: Retrieval-Augmented Generation
- `AIS-011`: Grounding
- `TERM-016B`: Token en tokenisatie
- `TERM-017A`: Sliding Window
- `TERM-017C`: Chunking

## Bronnen en actualiteit

**Kernbronnen:** SRC-055, SRC-062, SRC-063
