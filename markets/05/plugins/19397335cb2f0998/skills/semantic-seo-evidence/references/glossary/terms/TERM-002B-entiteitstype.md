---
term_id: TERM-002B
preferred_name_nl: Entiteitstype
english_name: Entity Type
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: NLP / schema / knowledge representation
evidence_labels:
- A
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-061
- SRC-065
- SRC-066
related_term_ids:
- TEC-010
- TERM-002
- TERM-002E
- TERM-002F
- TERM-002G
status: active
---

# Entiteitstype

**Engelse term of afkorting:** Entity Type  
**Term-ID:** `TERM-002B`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** NLP / schema / knowledge representation  
**Bewijsbasis:** A, B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een entiteitstype is een categorie die binnen een bepaald schema, model of taak aan een entiteit of vermelding wordt toegekend, zoals Persoon, Organisatie, Plaats, Product of Gebeurtenis. Typen helpen ordenen en disambigueren, maar zijn niet universeel.

## Typen zijn afhankelijk van het model

Een persoon kan tegelijk mens, auteur, medewerker en expert zijn. Een scootmobiel kan tegelijk product, voertuig en mobiliteitshulpmiddel zijn. Welk type het meest bruikbaar is, hangt af van het doel en het gebruikte schema. NLP-benchmarks gebruiken vaak een beperkte typenset, terwijl ontologieën veel fijnmaziger klassen kunnen bevatten.

| Omgeving | Mogelijk type | Doel |
| --- | --- | --- |
| NER-model | PERSON, ORGANIZATION, LOCATION | Tekstspans herkennen en grof classificeren. |
| Productregister | Scootmobielmodel, accuvariant, accessoire | Eigenschappen en varianten correct beheren. |
| Schema.org | Product, ProductGroup, Organization | Gestructureerde webinformatie beschrijven. |
| Ontologie | Mobiliteitsvoertuig, elektrisch voertuig, hulpmiddel | Formele relaties, beperkingen en inferentie vastleggen. |

## Wat is bevestigd?

- Google Knowledge Graph Search API documenteert verschillende entiteitstypen, waaronder Person, Organization, Place en LocalBusiness. [SRC-065]

- Google Cloud Entity Analysis retourneert entiteitstypen naast mentions en salience. [SRC-061]

- OWL-ontologieën kunnen klassen en relaties formeel vastleggen. [SRC-066]

## Wat is niet bevestigd?

- Dat één entiteit precies één type heeft.

- Dat alle systemen dezelfde typenhierarchie gebruiken.

- Dat een type uit structured data automatisch de interne classificatie van een zoekmachine bepaalt.

- Dat een foutloos type zonder context kan worden afgeleid uit een korte naam.

## Praktische toepassing

1. Maak voor productdata een beheersbare, gedocumenteerde typenset.

2. Scheid model, variant, onderdeel, accessoire, dienst en organisatie.

3. Leg meerdere typen alleen vast wanneer hun betekenis en gebruik duidelijk zijn.

4. Controleer of typekeuzes in tekst, structured data, feeds en interne systemen op elkaar aansluiten.

## Veelgemaakte misvatting

Een type is alleen een label. In formele modellen kan een type ook bepalen welke eigenschappen en relaties logisch of toegestaan zijn.

## Zie ook

Entiteit, Ontologie, Taxonomie, Knowledge Graph en Structured Data.

## Verwante begrippen

- `TEC-010`: Structured Data
- `TERM-002`: Entiteit
- `TERM-002E`: Kennisgraaf
- `TERM-002F`: Ontologie
- `TERM-002G`: Taxonomie

## Bronnen en actualiteit

**Kernbronnen:** SRC-061, SRC-065, SRC-066
