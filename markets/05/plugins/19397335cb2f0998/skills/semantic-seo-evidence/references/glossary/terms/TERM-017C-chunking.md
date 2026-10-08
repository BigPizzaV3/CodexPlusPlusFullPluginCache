---
term_id: TERM-017C
preferred_name_nl: Chunking
english_name: Chunking
cluster_id: 4
cluster_name: NLP en taalmodellen
type_context: Documentsegmentatie, retrieval en RAG
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-024
- SRC-056
- SRC-057
- SRC-063
related_term_ids:
- AIS-010
- AIS-011
- TERM-011C
- TERM-017A
- TERM-017B
status: active
---

# Chunking

**Engelse term of afkorting:** Chunking  
**Term-ID:** `TERM-017C`  
**Hoofdcategorie:** 4 NLP en taalmodellen  
**Type en context:** Documentsegmentatie, retrieval en RAG  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Chunking is het opdelen van een document, dataset of andere informatiebron in kleinere delen die afzonderlijk kunnen worden verwerkt, opgeslagen, opgehaald of aan een model worden aangeboden.

## Uitgebreide uitleg

Chunks kunnen op vaste tokenlengte worden gemaakt, maar ook op zins-, alinea-, koppen-, sectie-, semantisch of hiërarchisch niveau. De beste keuze hangt af van documenttype, vragen, retrievalmethode, model en evaluatiedoel.

Kleine chunks kunnen een precies antwoord isoleren, maar verliezen sneller omliggende voorwaarden en referenten. Grote chunks bewaren meer samenhang, maar kunnen ruis toevoegen en retrieval minder specifiek maken.

Overlap kan grensinformatie behouden, maar veroorzaakt duplicatie en kan meerdere bijna gelijke resultaten opleveren. Hiërarchische methoden proberen kleinere bewijsstukken aan grotere sectiecontext te koppelen.

Onderzoek laat zowel voordelen van hiërarchische chunking als mogelijkheden zonder klassieke vooraf gemaakte chunks zien. Dat bevestigt dat chunking een ontwerpkeuze is en geen universele vaste regel.

## Technische onderdelen

| Strategie | Voordeel | Risico | Geschikte evaluatievraag |
| --- | --- | --- | --- |
| Vaste tokenlengte | eenvoudig en voorspelbaar | breekt betekenisvolle eenheden | blijven claims en voorwaarden samen? |
| Zin of alinea | natuurlijke taalgrens | te klein of te groot per document | kan de passage zelfstandig worden begrepen? |
| Kop of sectie | behoudt documentstructuur | secties kunnen sterk verschillen in lengte | sluit de sectie op de gebruikerstaak aan? |
| Semantisch | grens op inhoudelijke verandering | model- en drempelafhankelijk | blijft het onderwerp coherent? |
| Hiërarchisch | klein bewijs plus grotere context | complexere index en retrieval | wordt bewijs met juiste bovencontext geleverd? |
| Chunking-free | vermijdt vooraf gefixeerde grenzen | andere reken- en modelvereisten | vindt het systeem precies en controleerbaar bewijs? |

## Voorbeeld

Een productspecificatie “praktisch bereik 82 km onder testcondities X” mag niet worden gescheiden van de voorwaarden, bron en productvariant. Een chunk die alleen “82 km” bevat is kort, maar inhoudelijk onveilig. Een goede segmentatie houdt de waarde en noodzakelijke context bij elkaar.

## Wat is bevestigd?

- Chunkkeuzes kunnen retrieval en RAG-prestaties beïnvloeden.

- Er bestaan meerdere strategieën, waaronder vaste, structurele, semantische en hiërarchische chunking.

- Onderzoek ondersteunt niet één universele optimale chunkgrootte voor alle documenten en taken.

## Wat is niet bevestigd?

- Google vereist niet dat webcontent in kunstmatig kleine AI-chunks wordt geschreven.

- Een vaste lengte, bijvoorbeeld een bepaald aantal woorden of tokens, garandeert geen citatie of ranking.

- Meer overlap is niet altijd beter en kan duplicatie of ruis vergroten.

## Praktische toepassing

- Gebruik duidelijke koppen, alinea’s, tabellen en zelfstandig begrijpelijke secties omdat dit gebruikers en technische verwerking helpt.

- Splits een tekst niet onnatuurlijk alleen voor een vermeende AI-voorkeur.

- Evalueer een eigen RAG-systeem met echte vragen, bronpassages en fouten per chunkstrategie.

- Zorg dat claims, waarden, eenheden, voorwaarden en bronverwijzingen niet van elkaar worden losgeknipt.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Iedere alinea moet een zelfstandige mini-pagina voor AI zijn. Goede secties moeten begrijpelijk zijn, maar content mag context opbouwen en hoeft niet volgens één kunstmatige chunklengte te worden geschreven. |
| --- |

## Zie ook

TERM-017A Sliding Window, TERM-017B Context Window, TERM-011C Dense Retrieval, RAG, Grounding.

## Verwante begrippen

- `AIS-010`: Retrieval-Augmented Generation
- `AIS-011`: Grounding
- `TERM-011C`: Dense Retrieval
- `TERM-017A`: Sliding Window
- `TERM-017B`: Context Window

## Bronnen en actualiteit

**Kernbronnen:** SRC-024, SRC-056, SRC-057, SRC-063
