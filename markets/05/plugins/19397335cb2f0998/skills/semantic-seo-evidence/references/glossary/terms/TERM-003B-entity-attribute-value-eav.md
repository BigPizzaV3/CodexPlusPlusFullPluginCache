---
term_id: TERM-003B
preferred_name_nl: Entity-Attribute-Value (EAV)
english_name: Entity-Attribute-Value Model (EAV)
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Datamodellering en feitenbeheer
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-003
- SRC-031
related_term_ids:
- QLT-021
- TEC-010
- TERM-002
- TERM-003A
- TERM-020A
status: active
---

# Entity-Attribute-Value (EAV)

**Engelse term of afkorting:** Entity-Attribute-Value Model (EAV)  
**Term-ID:** `TERM-003B`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Datamodellering en feitenbeheer  
**Bewijsbasis:** D, met praktische frameworktoepassing  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Entity-Attribute-Value, afgekort EAV, is een datamodel waarin een feit wordt vastgelegd als een combinatie van een entiteit, een eigenschap en een waarde. Het model is vooral bruikbaar wanneer verschillende entiteiten niet allemaal dezelfde eigenschappen hebben of wanneer eigenschappen regelmatig veranderen.

## Uitgebreide uitleg

Een klassieke tabel heeft meestal vaste kolommen. In een EAV-model kan iedere eigenschap als een aparte rij worden opgeslagen. Dat geeft flexibiliteit bij sterk wisselende of schaarse eigenschappen, maar maakt validatie, vergelijking, datatypen en complexe zoekopdrachten vaak moeilijker.

EAV en een RDF-triple bestaan allebei uit drie posities, maar zijn niet hetzelfde. RDF beschrijft formele relaties in een graaf met identifiers en semantische regels. EAV is een algemeen databasepatroon voor entiteiten, eigenschappen en waarden. Een EAV-record kan naar RDF worden vertaald, maar EAV is geen automatisch subtype van RDF.

Binnen Semantic SEO is EAV vooral nuttig als intern feitenmodel voor producten, diensten, personen en organisaties. Het is geen bevestigde Google-rankingscore of verplicht contentformaat.

## Eenvoudig EAV-voorbeeld

| Veld | Voorbeeld |
| --- | --- |
| Entiteit | Model X, uitvoering met accupakket L |
| Eigenschap | Maximaal opgegeven bereik |
| Waarde | 100 kilometer |

## Waarom EAV alleen niet genoeg is

Een waarde is pas betrouwbaar bruikbaar wanneer ook duidelijk is waar zij vandaan komt, voor welke variant zij geldt en onder welke omstandigheden zij is vastgesteld. Daarom gebruikt de Begrippenlijst 2026 een uitgebreid EAV+ bewijsrecord.

| EAV+ veld | Wat wordt vastgelegd? |
| --- | --- |
| Entity-ID en variant | Unieke identificatie van het juiste model, bouwjaar, uitvoering of accupakket. |
| Eigenschap en waarde | Het concrete kenmerk, getal, object of oordeel. |
| Eenheid | Bijvoorbeeld kilometer, watt, kilogram of centimeter. |
| Claimtype | Fabrikantsopgave, eigen meting, officiële regel, deskundige inschatting of persoonlijke ervaring. |
| Voorwaarden | Temperatuur, gewicht, snelheid, ondergrond, land, datum of andere grenzen. |
| Bron en methode | De primaire bron en de manier waarop de waarde is vastgesteld. |
| Zekerheid en controledatum | Hoe sterk het bewijs is en wanneer hercontrole nodig is. |

## Wat is bevestigd?

- EAV is een bestaand databasemodel voor gegevens met uiteenlopende en veranderlijke eigenschappen. [SRC-003]

- Het model kan flexibel zijn bij schaarse en heterogene gegevens. Dezelfde flexibiliteit brengt ook technische nadelen mee, onder meer bij validatie, typen, vergelijking en querycomplexiteit. [SRC-003]

## Wat is niet bevestigd?

- Dat EAV in iedere situatie de meest ruimte-efficiënte of beste databasevorm is.

- Dat Google gewone contentpagina’s als EAV-records rangschikt.

- Dat een EAV-rij zonder bron, eenheid, variant en voorwaarden voldoende bewijs is.

- Dat meer ingevulde attributen automatisch meer topical authority opleveren.

## Praktische toepassing

1. Gebruik EAV+ als centrale feitenbasis voor productspecificaties, vergelijkingen, keuzehulpen, video’s, feeds en structured data.

2. Scheid fabrikantwaarden, eigen metingen, praktijkinschattingen en ervaringen van klanten.

3. Leg varianten afzonderlijk vast, zodat eigenschappen van twee uitvoeringen niet worden samengevoegd.

4. Publiceer alleen waarden die voor de bedoelde variant, markt, datum en situatie gelden.

5. Gebruik het model om inconsistenties tussen pagina’s en kanalen te vinden, niet om tekst kunstmatig met attributen te vullen.

## Veelgemaakte misvatting

| Misvatting<br>“EAV is gewoon een tweede soort RDF-triple.” Beide modellen hebben drie onderdelen, maar hun formele regels, toepassing en technische betekenis verschillen. |
| --- |

## Zie ook

RDF-triple, entiteit, productvariant, provenance, data quality, structured data, stable identifier en claim confidence.

## Verwante begrippen

- `QLT-021`: Data Quality
- `TEC-010`: Structured Data
- `TERM-002`: Entiteit
- `TERM-003A`: RDF-triple
- `TERM-020A`: Provenance
- productvariant *(verwant concept buiten deze begrippenlijst)*
- stable identifier en claim confidence *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-003, SRC-031
