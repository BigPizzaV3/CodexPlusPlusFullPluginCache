---
term_id: TERM-016D
preferred_name_nl: Transformer
english_name: Transformer
cluster_id: 4
cluster_name: NLP en taalmodellen
type_context: Neurale netwerkarchitectuur en sequence modeling
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-026
- SRC-046
- SRC-058
related_term_ids:
- TERM-016A
- TERM-016C
- TERM-017B
- TERM-018
status: active
---

# Transformer

**Engelse term of afkorting:** Transformer  
**Term-ID:** `TERM-016D`  
**Hoofdcategorie:** 4 NLP en taalmodellen  
**Type en context:** Neurale netwerkarchitectuur en sequence modeling  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Een transformer is een neurale netwerkarchitectuur die attentionmechanismen gebruikt om relaties tussen posities in een sequentie te modelleren, in combinatie met onder meer tokenrepresentaties, positionele informatie en feed-forwardlagen.

## Uitgebreide uitleg

De oorspronkelijke transformerarchitectuur bevatte een encoder en een decoder. Later zijn veel varianten ontstaan, waaronder encoder-onlymodellen, decoder-onlymodellen en encoder-decodermodellen.

Self-attention laat een model bij het maken van een representatie informatie uit andere posities in dezelfde sequentie wegen. Positie-informatie blijft nodig, omdat attention op zichzelf de volgorde niet vanzelf vastlegt.

BERT is een encodergeoriënteerde transformer die bidirectionele contextrepresentaties leert. Generatieve decodergeoriënteerde modellen worden vaak autoregressief getraind om volgende tokens te voorspellen. Beide behoren tot de transformerfamilie, maar hebben andere functies en trainingsdoelen.

Transformers kunnen worden gebruikt voor classificatie, extractie, retrieval, vertaling, generatie en andere taken. Niet ieder transformermodel is een groot taalmodel en niet ieder groot taalmodel werkt in iedere situatie hetzelfde.

## Belangrijke afbakening

| Architectuurvorm | Typische werking | Voorbeelden van taken |
| --- | --- | --- |
| Encoder-only | maakt contextuele representaties van invoer | classificatie, NER, extractie, embeddings |
| Decoder-only | genereert tokens op basis van voorafgaande context | tekstgeneratie, conversatie, codegeneratie |
| Encoder-decoder | codeert invoer en genereert een doelreeks | vertaling, samenvatting, transformatie |

## Voorbeeld

In de zin “De snelle scootmobiel heeft een uitneembare accu” kan een transformer representaties maken waarin het woord “accu” rekening houdt met de omliggende woorden. Hoe dat gebeurt en welke informatie wordt behouden, hangt af van model, training en taak.

## Wat is bevestigd?

- Transformers gebruiken attention als centraal onderdeel van de architectuur.

- Encoder-, decoder- en encoder-decodervarianten kunnen voor verschillende taal- en retrievaltaken worden gebruikt.

- BERT leert bidirectionele contextrepresentaties en is niet hetzelfde als een decoder-only generatief model.

## Wat is niet bevestigd?

- Attentiongewichten zijn niet automatisch een volledige verklaring van een modelbeslissing.

- Er bestaat geen directe transformer-schrijfregel voor SEO.

- Het gebruik van een transformer door een platform maakt iedere uitkomst niet automatisch feitelijk juist of stabiel.

## Praktische toepassing

- Gebruik de term om modelarchitecturen en verschillen tussen toepassingen correct te beschrijven.

- Vermijd de algemene uitspraak dat “AI” of “de transformer” een tekst op één vaste manier begrijpt.

- Controleer altijd de concrete taak, invoerlimiet, modelversie en evaluatiemethode.

- Voor contentschrijvers blijven duidelijke taal, bewijs en gebruikerstaak belangrijker dan het nabootsen van een architectuur.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Iedere transformer voorspelt alleen het volgende woord. Next-token prediction is kenmerkend voor veel generatieve decodertraining, maar transformers worden ook gebruikt voor embeddings, classificatie, extractie en andere taken. |
| --- |

## Zie ook

TERM-018 Sequence Modeling, TERM-016C Embedding, TERM-017B Context Window, TERM-016A NLP.

## Verwante begrippen

- `TERM-016A`: Natural Language Processing
- `TERM-016C`: Embedding
- `TERM-017B`: Context Window
- `TERM-018`: Sequence Modeling

## Bronnen en actualiteit

**Kernbronnen:** SRC-026, SRC-046, SRC-058
