---
term_id: TERM-016B
preferred_name_nl: Token en tokenisatie
english_name: Token and Tokenization
cluster_id: 4
cluster_name: NLP en taalmodellen
type_context: NLP-voorverwerking en modelinvoer
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-048
related_term_ids:
- TERM-016C
- TERM-017B
- TERM-017C
- TERM-018
status: active
---

# Token en tokenisatie

**Engelse term of afkorting:** Token and Tokenization  
**Term-ID:** `TERM-016B`  
**Hoofdcategorie:** 4 NLP en taalmodellen  
**Type en context:** NLP-voorverwerking en modelinvoer  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Een token is een verwerkingseenheid die door een tokenizer uit tekst of andere invoer wordt gemaakt. Tokenisatie is het proces waarmee de invoer in zulke eenheden wordt gesegmenteerd.

## Uitgebreide uitleg

Een token hoeft geen volledig woord te zijn. Afhankelijk van de tokenizer kan een token een woord, woorddeel, teken, interpunctieteken, getal, spatiepatroon of speciaal controlesymbool zijn.

Moderne taalmodellen gebruiken vaak subwordtokenisatie. Daardoor kunnen zeldzame woorden en nieuwe namen uit kleinere delen worden opgebouwd. De precieze segmentatie verschilt per tokenizer, vocabulaire, taal en modelversie.

Het aantal tokens is daarom niet gelijk aan het aantal woorden. Hoofdletters, accenten, samenstellingen, interpunctie, cijfers en spaties kunnen de tokenisatie beïnvloeden. Een Nederlandse samenstelling zoals “scootmobielaccu” kan door verschillende tokenizers anders worden opgesplitst.

Tokenisatie is een technische stap. De gebruiker ziet meestal woorden en zinnen, terwijl het model met token-ID’s en bijbehorende representaties werkt.

## Belangrijke afbakening

| Begrip | Wat het is | Wat het niet automatisch is |
| --- | --- | --- |
| Woord | Taalkundige of orthografische eenheid | Eén modeltoken |
| Token | Uitkomst van een specifieke tokenizer | Een universeel taalonderdeel |
| Subword | Deel van een woord dat als token kan dienen | Een morfeem met vaste taalkundige betekenis |
| Token-ID | Numerieke verwijzing naar een vocabulaire-item | De betekenis zelf |
| Tokenlimiet | Technische limiet of budget binnen een modelinterface | Een SEO-lengteadvies |

## Voorbeeld

De tekst “25 km/u” kan afhankelijk van de tokenizer worden verdeeld in één of meerdere tokens voor het getal, de spatie, de eenheid en de schuine streep. Een andere tokenizer kan dezelfde tekst anders segmenteren. Daarom kan een woordenteller niet betrouwbaar voorspellen hoeveel modeltokens een tekst heeft.

## Wat is bevestigd?

- Tokenizers kunnen woorden, subwoorden en andere tekeneenheden produceren.

- SentencePiece is een voorbeeld van een taalonafhankelijke subwordtokenizer die rechtstreeks op ruwe tekst kan worden getraind.

- Tokenaantallen en segmentatie zijn tokenizer- en modelafhankelijk.

## Wat is niet bevestigd?

- Er bestaat geen universele beste tokenverdeling voor SEO-content.

- Een vast aantal tokens per alinea of kop is geen bevestigde Google-regel.

- Een term vaker schrijven omdat hij mogelijk uit meerdere tokens bestaat levert geen bewezen voordeel op.

## Praktische toepassing

- Gebruik een tokenmeter alleen wanneer een concrete API, contextlimiet of kostencalculatie dat nodig maakt.

- Behoud correcte merknamen, modelnamen, eenheden en interpunctie. Verander taal niet om een vermeende tokenizer te manipuleren.

- Zorg in RAG- of extractiesystemen dat segmentatie geen getal van de bijbehorende eenheid of productnaam van de variant scheidt.

- Leg in een feitenregister waarden en eenheden ook gestructureerd vast, los van de lopende tekst.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Een token is gewoon een woord. In werkelijkheid kan één woord meerdere tokens opleveren en kunnen cijfers, interpunctie en speciale symbolen afzonderlijke tokens zijn. |
| --- |

## Zie ook

TERM-017B Context Window, TERM-017C Chunking, TERM-016C Embedding, TERM-018 Sequence Modeling.

## Verwante begrippen

- `TERM-016C`: Embedding
- `TERM-017B`: Context Window
- `TERM-017C`: Chunking
- `TERM-018`: Sequence Modeling

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-048
