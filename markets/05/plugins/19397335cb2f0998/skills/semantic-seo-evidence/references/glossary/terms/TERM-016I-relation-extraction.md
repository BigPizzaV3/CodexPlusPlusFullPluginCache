---
term_id: TERM-016I
preferred_name_nl: Relation Extraction
english_name: Relation Extraction
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Informatie-extractie, kennisgrafen en claimmodellering
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-054
related_term_ids:
- TERM-003A
- TERM-003B
- TERM-016E
- TERM-020A
status: active
---

# Relation Extraction

**Engelse term of afkorting:** Relation Extraction  
**Term-ID:** `TERM-016I`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Informatie-extractie, kennisgrafen en claimmodellering  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Relation extraction is het automatisch herkennen en typeren van relaties tussen mentions, entiteiten, gebeurtenissen of waarden in tekst.

## Uitgebreide uitleg

Relation extraction probeert van ongestructureerde taal een gestructureerde relatie te maken. Een relatie kan bijvoorbeeld “heeft motorvermogen”, “is onderdeel van”, “is opvolger van”, “is geschikt voor” of “wordt beïnvloed door” zijn.

Sommige systemen werken binnen één zin. Andere combineren informatie uit meerdere zinnen of een volledig document. De beschikbare relatietypen hangen af van taak, schema en trainingsdata.

Een geëxtraheerde relatie is een modeluitkomst, geen bewijs dat de bewering waar is. Negatie, onzekerheid, voorwaarden, tijd en bron kunnen de betekenis veranderen. “Heeft geen 1000-wattmotor” mag niet als positieve relatie worden opgeslagen.

Voor betrouwbare content hoort relation extraction daarom te worden gekoppeld aan provenance, variantinformatie en menselijke verificatie.

## Voorbeeld

Mogelijke omzetting van tekst naar gestructureerde claims:

| Tekst | Mogelijke relatie | Extra controle nodig |
| --- | --- | --- |
| De On Four heeft een motor van 1000 watt. | On Four - heeft motorvermogen - 1000 W | uitvoering, bron en nominaal of piekvermogen |
| De rollatordrager is geschikt voor model X. | rollatordrager - is geschikt voor - model X | versie, montagevoorwaarden en maximaal gewicht |
| Koude kan het praktische bereik verlagen. | lage temperatuur - kan beïnvloeden - praktisch bereik | richting, grootte, omstandigheden en bron |
| Model B is niet de opvolger van model A. | negatie van opvolgerrelatie | negatie moet expliciet worden behouden |

| Notitie: Een triple of EAV-record wordt pas betrouwbaar wanneer bron, datum, context, methode en zekerheid worden toegevoegd. |
| --- |

## Wat is bevestigd?

- Relation extraction is een gevestigde informatie-extractietaak met getypeerde relaties.

- Relaties kunnen onder andere causaal, deel-geheel, instrumenteel of entiteit-eigenschapgericht zijn.

- Taalcontext, richting en argumentrollen zijn belangrijk voor een correcte relatie.

## Wat is niet bevestigd?

- Een automatisch geëxtraheerde triple is niet automatisch een waar feit.

- Zoekmachines slaan iedere zin aantoonbaar op als dezelfde relationset.

- Meer expliciete relaties in tekst garanderen geen ranking of knowledge-graphopname.

## Praktische toepassing

- Schrijf belangrijke claims met een duidelijke entiteit, relatie, waarde, eenheid en voorwaarde.

- Bewaar negatie, modaliteit en onzekerheid, bijvoorbeeld kan, moet, maximaal en onder deze omstandigheden.

- Koppel geëxtraheerde claims aan een bewijsrecord en broncontrole.

- Gebruik automatische extractie om inconsistenties te vinden, niet om zonder review productspecificaties te publiceren.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Wanneer een zin grammaticaal een subject, werkwoord en object heeft, is de relatie automatisch volledig en feitelijk juist. Extractie moet ook richting, context, negatie, tijd, bron en variant verwerken. |
| --- |

## Zie ook

TERM-003A RDF-triple, TERM-003B EAV, Provenance, TERM-016E Named Entity Recognition.

## Verwante begrippen

- `TERM-003A`: RDF-triple
- `TERM-003B`: Entity-Attribute-Value (EAV)
- `TERM-016E`: Named Entity Recognition
- `TERM-020A`: Provenance

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-054
