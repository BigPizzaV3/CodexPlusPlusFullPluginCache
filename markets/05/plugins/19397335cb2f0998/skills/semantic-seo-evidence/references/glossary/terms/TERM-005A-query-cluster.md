---
term_id: TERM-005A
preferred_name_nl: Query Cluster
english_name: Query Cluster
cluster_id: 2
cluster_name: Zoekintentie en queryverwerking
type_context: Information Retrieval / queryanalyse / clustering
evidence_labels:
- D
- E
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-020
- SRC-021
- SRC-036
related_term_ids:
- QRY-010
- QRY-013
- QRY-014
- TERM-005
- TERM-012A
- TERM-012C
status: active
---

# Query Cluster

**Engelse term of afkorting:** Query Cluster  
**Term-ID:** `TERM-005A`  
**Hoofdcategorie:** 2 Zoekintentie en queryverwerking  
**Type en context:** Information Retrieval / queryanalyse / clustering  
**Bewijsbasis:** D en E  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een Query Cluster is een groep zoekopdrachten die volgens een gekozen methode voldoende overeenkomst of samenhang vertonen. De clustering kan berusten op woorden, zoekresultaten, gebruikersgedrag, intentie, entiteiten, embeddings of een combinatie daarvan. Een querycluster is een analytische groep en niet automatisch een voorschrift om één pagina te maken.

## Hoe clusters kunnen worden gevormd

| Signaal | Wat wordt vergeleken? | Belangrijkste beperking |
| --- | --- | --- |
| Lexicale overeenkomst | Gedeelde woorden, woordstammen, frases of termen. | Mist queries die dezelfde bedoeling anders formuleren. |
| Resultaatoverlap | Overeenkomst tussen opgehaalde URL’s of documenten. | Resultaten veranderen door tijd, plaats, personalisatie en systeemupdates. |
| Klik- en sessiesamenhang | Queries of verfijningen die in vergelijkbare zoekreizen voorkomen. | Deze data is meestal niet volledig beschikbaar voor contentmakers. |
| Intentie en taak | De onderliggende actie of informatiebehoefte. | Vraagt menselijke beoordeling en kan meerdere interpretaties bevatten. |
| Entiteiten en relaties | Genoemde of bedoelde producten, personen, eigenschappen en verbanden. | Goede entity disambiguation is noodzakelijk. |
| Embeddings | Afstand of gelijkenis tussen geleerde vectorrepresentaties. | De uitkomst hangt af van model, trainingsdata en gekozen maat. |
| Hybride clustering | Combinatie van meerdere signalen. | Weging en drempels blijven methode- en domeinafhankelijk. |

Het Google-patent over queryclustering beschrijft onder andere clustering op zoektermen, resultaats-URL’s en responsieve documenten. Google-onderzoek naar query refinements combineert documentklikken en sessiesamenhang om onderliggende intenties te clusteren. Deze voorbeelden laten zien dat er geen enkele universele clustermethode bestaat. [SRC-020] [SRC-021]

## Voorbeeld

| Clusterdoel | Mogelijke clusterleden | Redactioneel besluit |
| --- | --- | --- |
| Scootmobiel in de auto meenemen | opvouwbare scootmobiel auto; scootmobiel in kofferbak; lichtgewicht scootmobiel meenemen; welke scootmobiel past in auto | Eén sterke keuze- en meetpagina kan passend zijn wanneer de gebruikerstaak, meetmethode en vervolgstap gelijk zijn. |
| Scootmobielaccu opladen | hoe accu opladen; laadtijd scootmobiel; oplader blijft rood; lithiumaccu bewaren | Mogelijk meerdere secties of probleemartikelen, omdat handelingen, risico’s en bewijzen verschillen. |

## Wat is bevestigd?

- Queryclustering is een erkende techniek binnen Information Retrieval en queryanalyse. [SRC-020] [SRC-021]

- Een representative query kan binnen een cluster worden gekozen om de groep te benoemen of te presenteren. [SRC-020]

- Clusters kunnen verschillende aspecten van de informatie rond een oorspronkelijke query samenvatten. [SRC-021]

## Wat is niet bevestigd?

- Dat iedere SEO-tool dezelfde correcte clusters produceert.

- Dat twee queries met overlappende zoekresultaten altijd dezelfde gebruikerstaak hebben.

- Dat iedere querycluster exact één pagina hoort te worden.

- Dat clustergrenzen permanent zijn. Taal, producten, vraag en resultaten kunnen veranderen.

## Praktische toepassing

1. Documenteer de gebruikte clustermethode en drempel. Een cluster zonder methode is moeilijk te beoordelen of te herhalen.

2. Controleer clusters handmatig op intentie, taak, doelgroep, entiteit en noodzakelijke bewijsvorm.

3. Maak onderscheid tussen queryvarianten die hetzelfde antwoord zoeken en deelvragen die een eigen oplossing nodig hebben.

4. Gebruik een clusterlabel als navigatie- en onderzoeksnaam, niet automatisch als paginatitel.

5. Hercontroleer belangrijke clusters na productwijzigingen, nieuwe regelgeving, duidelijke SERP-verschuivingen of nieuwe gebruikersvragen.

## Veelgemaakte misvatting

“Queries staan in hetzelfde cluster, dus ze moeten op één pagina.” Clustering toont overeenkomst volgens een gekozen methode. De pagina- of sectiekeuze hangt daarnaast af van taak, risico, benodigde diepte, bewijs, contentvorm en gebruikersroute.

## Zie ook

Query Network, Representative Query, Canonical Query, Search Intent, Query Rewriting, Query Expansion en Content Consolidation.

## Verwante begrippen

- `QRY-010`: Zoekintentie
- `QRY-013`: Query Rewriting
- `QRY-014`: Query Expansion
- `TERM-005`: Query Network
- `TERM-012A`: Representative Query
- `TERM-012C`: Canonical Query
- Content Consolidation *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-020, SRC-021, SRC-036
