---
term_id: TERM-016C
preferred_name_nl: Embedding
english_name: Embedding
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Neurale representaties, semantische zoektechniek en clustering
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-015
- SRC-016
- SRC-019
- SRC-046
- SRC-049
related_term_ids:
- TERM-011C
- TERM-013
- TERM-014A
- TERM-016D
status: active
---

# Embedding

**Engelse term of afkorting:** Embedding  
**Term-ID:** `TERM-016C`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Neurale representaties, semantische zoektechniek en clustering  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Een embedding is een aangeleerde numerieke vectorrepresentatie van bijvoorbeeld een token, woord, zin, passage, document, afbeelding of entiteit, gemaakt voor een bepaald model en trainingsdoel.

## Uitgebreide uitleg

Embeddings plaatsen informatie in een vectorruimte. Elementen die volgens het model bruikbare overeenkomsten hebben, kunnen in die ruimte dichter bij elkaar liggen. Welke relaties worden vastgelegd hangt af van trainingsdata, modelarchitectuur en doelstelling.

Oudere woordembeddings zoals Word2Vec en GloVe geven vaak één algemene vector per woordvorm. Contextuele modellen kunnen voor hetzelfde woord verschillende representaties maken afhankelijk van de zin. Een productnaam als “Pride” kan daardoor in een productcontext anders worden gerepresenteerd dan het Engelse woord voor trots.

Embeddings kunnen op meerdere niveaus worden gemaakt. Sentence-BERT is bijvoorbeeld ontworpen om zinnen efficiënt als vergelijkbare vectoren te representeren. Dense retrieval gebruikt query- en passage-embeddings om kandidaten op te halen.

Een vector is niet vanzelf uitlegbaar als een lijst menselijke eigenschappen. De dimensies hebben meestal geen eenvoudige vaste betekenis en de afstand tussen vectoren blijft afhankelijk van de gekozen maatstaf.

## Technische onderdelen

| Embeddingtype | Eenheid | Typische toepassing | Belangrijke beperking |
| --- | --- | --- | --- |
| Statische woordembedding | woordvorm | analogieën, eenvoudige semantische vergelijking | dezelfde vector in iedere context |
| Contextuele tokenembedding | token in een zin | taalanalyse, classificatie, extractie | afhankelijk van omliggende context |
| Zins- of passage-embedding | zin of passage | clustering, dense retrieval, duplicaatdetectie | informatie kan bij samenvoegen verloren gaan |
| Documentembedding | volledig document | globale clustering en aanbeveling | kan specifieke passage-informatie verbergen |
| Entiteits-embedding | entiteit of knowledge-base-item | linking, graph learning, aanbeveling | afhankelijk van gekozen kennisbron |

## Voorbeeld

De zoekvraag “scootmobiel voor lange afstanden” en een passage over een groot accupakket, een praktisch bereik en laadmogelijkheden kunnen in een passend model dicht bij elkaar komen, ook zonder dezelfde woorden. Een ander model of een andere taak kan echter een andere afstand geven.

## Wat is bevestigd?

- Embeddings worden gebruikt voor semantische vergelijking, clustering, classificatie en dense retrieval.

- Zins-embeddings kunnen met een maat zoals cosinusgelijkenis worden vergeleken.

- De betekenis van nabijheid hangt af van model, data, trainingsdoel en maatstaf.

## Wat is niet bevestigd?

- Een embedding is geen objectieve kaart van menselijke betekenis.

- Er bestaat geen openbare Google-embeddingwaarde die een contentspecialist rechtstreeks kan meten.

- Een hogere embeddinggelijkenis met een zoekvraag garandeert geen ranking of AI-citatie.

## Praktische toepassing

- Gebruik embeddings voor onderzoek, clustering, semantische zoekfuncties en kwaliteitscontrole, niet voor automatische publicatiebeslissingen zonder review.

- Combineer semantische zoeking met exacte filters voor modelcodes, prijzen, snelheden en eenheden.

- Evalueer retrieval met echte gebruikersvragen en relevante passages uit het eigen domein.

- Bewaar bron, modelversie en instellingen wanneer embeddingresultaten worden gebruikt in een audit of experiment.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Een embedding bevat alle betekenis en feiten van een tekst. Een embedding is een taakgerichte compressie of representatie en kan nuances, negatie, voorwaarden of specifieke waarden onvoldoende behouden. |
| --- |

## Zie ook

TERM-011C Dense Retrieval, TERM-014A Semantische gelijkenis, TERM-013 Semantische afstand, TERM-016D Transformer.

## Verwante begrippen

- `TERM-011C`: Dense Retrieval
- `TERM-013`: Semantische afstand
- `TERM-014A`: Semantische gelijkenis
- `TERM-016D`: Transformer

## Bronnen en actualiteit

**Kernbronnen:** SRC-015, SRC-016, SRC-019, SRC-046, SRC-049
