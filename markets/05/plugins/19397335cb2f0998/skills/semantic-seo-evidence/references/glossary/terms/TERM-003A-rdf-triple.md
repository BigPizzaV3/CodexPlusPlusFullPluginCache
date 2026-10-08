---
term_id: TERM-003A
preferred_name_nl: RDF-triple
english_name: RDF Triple
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Semantic Web en graafdatamodellering
evidence_labels:
- A
- E
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-002
- SRC-031
related_term_ids:
- TEC-010
- TERM-002
- TERM-002E
- TERM-002F
- TERM-003B
- TERM-016F
status: active
---

# RDF-triple

**Engelse term of afkorting:** RDF Triple  
**Term-ID:** `TERM-003A`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Semantic Web en graafdatamodellering  
**Bewijsbasis:** A en E  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een RDF-triple is een formele uitspraak in het Resource Description Framework. De uitspraak bestaat uit een subject, een predicaat en een object. Het subject geeft aan waar de uitspraak over gaat, het predicaat benoemt de eigenschap of relatie en het object geeft de waarde of de andere resource aan waarop de uitspraak betrekking heeft.

## Uitgebreide uitleg

RDF is een W3C-datamodel voor het representeren en verbinden van informatie op het web. Een verzameling RDF-triples vormt een RDF-graaf. In zo’n graaf zijn entiteiten, waarden en relaties als knooppunten en verbindingen te modelleren.

In een formele RDF-triple is het predicaat een unieke identifier, meestal een IRI. Het object kan een andere geïdentificeerde resource zijn, maar ook een letterlijke waarde zoals tekst, een getal of een datum. In een begrijpelijke contentbriefing mag dezelfde structuur eenvoudiger worden weergegeven, zolang duidelijk blijft welk onderwerp, welke eigenschap en welke waarde of relatie worden bedoeld.

NLP-systemen kunnen relaties uit tekst halen die later als triples worden vastgelegd. Daaruit volgt niet dat een triple zelf een algemene NLP-syntaxis is. De technische thuisbasis van het begrip ligt bij RDF, het Semantic Web, kennisgrafen en andere graafmodellen.

## Volledig voorbeeld

| Onderdeel | Inhoud |
| --- | --- |
| Subject | Tom Hanks |
| Predicaat | speelde in |
| Object | Forrest Gump |
| Volledige triple | (Tom Hanks, speelde in, Forrest Gump) |

| Niet-voorbeeld<br>“Tom Hanks speelde” is geen volledige triple. Het object ontbreekt. De zin kan wel het begin van een relationele uitspraak zijn. |
| --- |

## Wat is bevestigd?

- De stabiele W3C Recommendation RDF 1.1 definieert een RDF-graaf als een verzameling subject-predicaat-object-triples. [SRC-031]

- RDF 1.2 bouwt hierop voort. Op 24 juli 2026 was RDF 1.2 nog een Candidate Recommendation en geen definitieve W3C Recommendation. [SRC-001]

- Google LLC heeft een techniek gepatenteerd voor het indexeren en doorzoeken van graafgestructureerde kennisbanken die triples aanleveren. [SRC-002]

## Wat is niet bevestigd?

- Dat Google iedere gewone webpagina volledig naar RDF-triples omzet en op die manier opslaat.

- Dat iedere zin of iedere zoekopdracht automatisch een geldige RDF-triple is.

- Dat het opnemen van meer entiteiten of relationele zinnen op zichzelf een hogere ranking veroorzaakt.

- Dat een patent de precieze actuele inzet, dekking of weging van een techniek in Google Search bewijst.

## Praktische toepassing

1. Gebruik de triple als controlemodel voor belangrijke feiten. Bepaal steeds duidelijk het onderwerp, de eigenschap of relatie en de waarde of andere entiteit.

2. Gebruik stabiele identifiers voor producten, personen, organisaties en varianten wanneer informatie in meerdere systemen wordt hergebruikt.

3. Voeg bij getallen ook eenheid, context, bron, datum en voorwaarden toe. Een kale triple is niet automatisch voldoende bewijs.

4. Gebruik RDF, JSON-LD of andere structured-data-oplossingen alleen wanneer de gegevens overeenkomen met de zichtbare inhoud en het werkelijke paginatype.

5. Schrijf gewone tekst natuurlijk. Dwing niet iedere zin in een mechanische subject-predicaat-objectvorm.

## Veelgemaakte misvatting

| Misvatting<br>“Google gebruikt triples, dus iedere alinea moet uit expliciete triples bestaan.” De technische relevantie van triples rechtvaardigt een helder feiten- en relatiemodel, maar geen onnatuurlijke schrijfstijl of rankinggarantie. |
| --- |

## Zie ook

EAV, entiteit, entity linking, knowledge graph, ontologie, structured data, provenance en datakwaliteit.

## Verwante begrippen

- `TEC-010`: Structured Data
- `TERM-002`: Entiteit
- `TERM-002E`: Kennisgraaf
- `TERM-002F`: Ontologie
- `TERM-003B`: Entity-Attribute-Value (EAV)
- `TERM-016F`: Entity Linking
- EAV *(verwant concept buiten deze begrippenlijst)*
- provenance en datakwaliteit *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-002, SRC-031
