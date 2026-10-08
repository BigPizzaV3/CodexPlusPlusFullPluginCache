---
term_id: TERM-016A
preferred_name_nl: Natural Language Processing
english_name: Natural Language Processing (NLP)
cluster_id: 4
cluster_name: NLP en taalmodellen
type_context: Computerlinguïstiek, machine learning en taaltechnologie
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-026
- SRC-046
- SRC-050
- SRC-058
- SRC-061
related_term_ids:
- TERM-016B
- TERM-016C
- TERM-016D
- TERM-016E
- TERM-016I
status: active
---

# Natural Language Processing

**Engelse term of afkorting:** Natural Language Processing (NLP)  
**Term-ID:** `TERM-016A`  
**Hoofdcategorie:** 4 NLP en taalmodellen  
**Type en context:** Computerlinguïstiek, machine learning en taaltechnologie  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Natural Language Processing is het vakgebied waarin computationele methoden worden ontwikkeld om natuurlijke taal en spraak te analyseren, representeren, classificeren, koppelen, transformeren en genereren.

## Uitgebreide uitleg

NLP combineert inzichten uit taalkunde, computerwetenschappen, statistiek en machine learning. Afhankelijk van de toepassing werkt een systeem met regels, statistische modellen, neurale netwerken, kennisbronnen of combinaties daarvan.

Het vakgebied omvat veel verschillende taken. Voorbeelden zijn tokenisatie, woordsoorttagging, parsing, tekstclassificatie, Named Entity Recognition, entity linking, coreference resolution, relation extraction, vertaling, retrieval, vraagbeantwoording, samenvatting en tekstgeneratie.

Moderne modellen kunnen complexe patronen in taal modelleren en op veel taken sterke resultaten leveren. Dat is niet hetzelfde als aantonen dat een systeem taal, feiten, intenties of gevolgen op dezelfde manier begrijpt als een mens. De precieze capaciteiten en fouten hangen af van model, data, taak en evaluatie.

Python, bibliotheken en frameworks zijn hulpmiddelen waarmee NLP-systemen kunnen worden gebouwd. Zij zijn geen onderdeel van de definitie van NLP en bepalen op zichzelf niet de kwaliteit van een analyse.

## Technische onderdelen

| Taakgroep | Voorbeelden | Uitkomst |
| --- | --- | --- |
| Voorverwerking | tokenisatie, normalisatie, zinssegmentatie | verwerkbare taaleenheden |
| Taalkundige analyse | woordsoorten, syntaxis, semantische rollen | structuur en functies in taal |
| Entiteitsverwerking | NER, entity linking, disambiguation, coreference | mentions, typen, identifiers en verwijzingen |
| Informatie-extractie | relation extraction, events, tijd | gestructureerde claims of relaties |
| Representatie en retrieval | embeddings, sparse en dense retrieval | vergelijkbare of relevante kandidaten |
| Generatie en transformatie | vertaling, samenvatting, vraagbeantwoording, tekstgeneratie | nieuwe of omgevormde taaluitvoer |

## Voorbeeld

Een systeem kan in de zin “De Nipponia Pride heeft een motor van 650 watt” eerst tokens maken, de productnaam als mention herkennen, het model mogelijk aan een productidentifier koppelen en de relatie motorvermogen = 650 watt extraheren. Iedere stap kan afzonderlijk fouten maken. De geëxtraheerde waarde moet daarom nog met een bron en variant worden gecontroleerd.

## Wat is bevestigd?

- NLP omvat meerdere analyse-, representatie-, extractie- en generatietaken.

- Transformers, embeddings en taakgerichte modellen zijn belangrijke moderne technieken, naast oudere statistische en regelgebaseerde methoden.

- Officiële taal-API’s kunnen bijvoorbeeld entiteitsnamen, typen, mentions en metadata teruggeven.

## Wat is niet bevestigd?

- NLP is geen enkel algoritme of één rankingfactor.

- Een modeluitvoer bewijst niet automatisch menselijk begrip of feitelijke juistheid.

- Er bestaat geen vaste NLP-schrijfstijl waarmee Google of een AI-platform content gegarandeerd beter behandelt.

## Praktische toepassing

- Gebruik NLP-begrippen om systemen en analyses te begrijpen, niet als lijst met verplichte woorden voor schrijvers.

- Zorg voor heldere entiteitsnamen, correcte eenheden, expliciete voorwaarden en logische verwijzingen. Dat helpt vooral de gebruiker en vermindert ambiguïteit.

- Laat belangrijke product- en wettelijke claims altijd uit een gecontroleerd feitenregister komen.

- Test automatische extractie of clustering steekproefsgewijs met menselijke beoordeling.

## Veelgemaakte misvatting

| Belangrijke begrenzing: NLP betekent dat een computer een tekst volledig begrijpt zodra hij woorden, entiteiten en zinsstructuur kan herkennen. Herkenning en representatie zijn nuttige stappen, maar garanderen geen volledige interpretatie, waarheid of goed oordeel. |
| --- |

## Zie ook

TERM-016B Token en tokenisatie, TERM-016C Embedding, TERM-016D Transformer, TERM-016E Named Entity Recognition, TERM-016I Relation Extraction.

## Verwante begrippen

- `TERM-016B`: Token en tokenisatie
- `TERM-016C`: Embedding
- `TERM-016D`: Transformer
- `TERM-016E`: Named Entity Recognition
- `TERM-016I`: Relation Extraction

## Bronnen en actualiteit

**Kernbronnen:** SRC-026, SRC-046, SRC-050, SRC-058, SRC-061
