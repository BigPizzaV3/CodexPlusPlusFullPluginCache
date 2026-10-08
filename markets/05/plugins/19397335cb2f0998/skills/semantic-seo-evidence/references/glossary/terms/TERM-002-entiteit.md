---
term_id: TERM-002
preferred_name_nl: Entiteit
english_name: Entity
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: NLP / Semantic Web / knowledge representation
evidence_labels:
- A
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-001
- SRC-061
- SRC-064
- SRC-065
related_term_ids:
- TERM-002A
- TERM-002B
- TERM-002E
- TERM-003B
- TERM-016F
- TERM-016G
status: active
---

# Entiteit

**Engelse term of afkorting:** Entity  
**Term-ID:** `TERM-002`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** NLP / Semantic Web / knowledge representation  
**Bewijsbasis:** A, B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een entiteit is iets waarnaar binnen een gekozen domein of systeem afzonderlijk kan worden verwezen. Dat kan bijvoorbeeld een persoon, organisatie, plaats, product, gebeurtenis, document, object of concept zijn. De entiteit zelf moet worden onderscheiden van haar naam, tekstvermelding, type en identifier.

## Vier informatielagen die niet door elkaar mogen lopen

| Laag | Betekenis | Voorbeeld |
| --- | --- | --- |
| Entiteit | Het bedoelde ding of concept | De specifieke For Motion On Four in een bepaalde uitvoering. |
| Vermelding | De tekstspan die naar de entiteit verwijst | “On Four”, “dit model” of “de vierwieler”. |
| Type | De categorie binnen een schema of model | Scootmobiel, voertuig of product. |
| Identifier | Een stabiele verwijzing binnen een namespace | Interne model-ID, productcode, URL of knowledge-base-ID. |

Dezelfde entiteit kan meerdere namen, schrijfwijzen en vermeldingen hebben. Andersom kan één naam naar verschillende entiteiten verwijzen. “Apple” kan bijvoorbeeld een organisatie, merk of voedingsmiddel aanduiden. Het vaststellen van de bedoelde identiteit vereist context en soms entity disambiguation.

## Entiteit is domein- en modelafhankelijk

Wat als entiteit wordt gemodelleerd hangt af van het doel. In een productregister kan een afzonderlijke accuconfiguratie een eigen entiteit of variant zijn. In een eenvoudig artikel kan diezelfde configuratie alleen als eigenschap worden beschreven. Een correcte keuze voorkomt dat modellen, uitvoeringen en waarden onbedoeld worden samengevoegd.

## Wat is bevestigd?

- RDF maakt uitspraken over resources die met identifiers kunnen worden aangeduid. [SRC-001]

- Google’s Knowledge Graph-documentatie beschrijft real-world entities als knooppunten met verschillende typen. [SRC-065]

- Google Cloud Entity Analysis maakt onderscheid tussen een representatieve entiteitsnaam, type, mentions, metadata en salience. [SRC-061]

- NLP-onderzoek onderscheidt mentiondetectie, entity linking en disambiguation als afzonderlijke taken. Deze zijn in batch 3 apart beschreven.

## Wat is niet bevestigd?

- Dat ieder zelfstandig naamwoord automatisch een afzonderlijke entiteit is.

- Dat een entiteit overal één universele identifier of één universeel type heeft.

- Dat het vaak herhalen van entiteitsnamen automatisch zoekmachinebegrip of rankings verbetert.

- Dat een door een API herkende entiteit zonder controle feitelijk juist of volledig gedisambigueerd is.

- Dat alle zoekmachines dezelfde interne entiteitenverzameling gebruiken.

## Praktische toepassing

1. Geef belangrijke producten, organisaties, personen en locaties een stabiele interne ID.

2. Leg officiële naam, alternatieve naam, variant, type en hoofd-URL afzonderlijk vast.

3. Bepaal bij dubbelzinnige namen welke context nodig is om de juiste entiteit te herkennen.

4. Koppel eigenschappen uitsluitend aan de juiste variant of tijdsperiode.

5. Gebruik natuurlijke vermeldingen in tekst; vermijd geforceerde naamherhaling.

## Veelgemaakte misvatting

“On Four” in een zin is automatisch de entiteit. Strikt genomen is het een vermelding die naar een bedoelde entiteit kan verwijzen.

## Zie ook

Entiteitsvermelding, Entiteitstype, Entiteitsidentifier, Entity Linking, Entity Disambiguation, Knowledge Graph en EAV.

## Verwante begrippen

- `TERM-002A`: Entiteitsvermelding
- `TERM-002B`: Entiteitstype
- `TERM-002E`: Kennisgraaf
- `TERM-003B`: Entity-Attribute-Value (EAV)
- `TERM-016F`: Entity Linking
- `TERM-016G`: Entity Disambiguation
- EAV *(verwant concept buiten deze begrippenlijst)*
- Entiteitsidentifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-001, SRC-061, SRC-064, SRC-065
