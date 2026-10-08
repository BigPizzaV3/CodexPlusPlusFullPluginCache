---
term_id: TEC-013
preferred_name_nl: '@id'
english_name: JSON-LD @id / Entiteitsidentifier
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: JSON-LD / entity identity
evidence_labels:
- A
last_checked: '2026-07-25'
source_ids:
- SRC-096
- SRC-097
- SRC-098
related_term_ids:
- GOV-017
- TEC-012
- TEC-015
- TEC-016
status: active
---

# @id

**Engelse term of afkorting:** JSON-LD @id / Entiteitsidentifier  
**Term-ID:** `TEC-013`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** JSON-LD / entity identity  
**Bewijsbasis:** A  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

@id is in JSON-LD de sleutel waarmee een node of entiteit een IRI of andere identifier krijgt, zodat verwijzingen naar dezelfde entiteit expliciet kunnen worden verbonden.

## Afbakening

Een @id is bij voorkeur stabiel, uniek binnen de bedoelde context en bruikbaar over meerdere pagina’s. Het is geen zichtbaar HTML-id-attribuut en niet hetzelfde als een database-primary-key.

## Wat is bevestigd?

- JSON-LD gebruikt @id om nodes te identificeren en relaties te vormen.

- Google’s Organization-documentatie gebruikt identifiers en URL’s om organisatie-informatie samenhangend te beschrijven.

## Wat is niet bevestigd?

- Dat een @id automatisch een Google Knowledge Graph-entiteit creëert.

- Dat iedere willekeurige fragment-URL duurzaam en ondubbelzinnig is.

## Praktische toepassing

1. Kies een stabiele, beheerde URL of IRI per belangrijke entiteit.

2. Hergebruik exact dezelfde @id voor dezelfde entiteit.

3. Wijzig identifiers niet zonder migratie- en verwijzingsplan.

## Voorbeeld

De organisatie kan `https://example.nl/#organization` als @id gebruiken en vestigingen via afzonderlijke identifiers modelleren.

## Veelgemaakte misvatting

@id is geen rankingtruc. Het helpt alleen wanneer het datamodel inhoudelijk consistent is.

## Zie ook

- Entiteitsidentifier

- JSON-LD

- Organization

- LocalBusiness

- Single Source of Truth

## Verwante begrippen

- `GOV-017`: Single Source of Truth
- `TEC-012`: JSON-LD
- `TEC-015`: Organization
- `TEC-016`: LocalBusiness
- Entiteitsidentifier *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-096, SRC-097, SRC-098

**Update-trigger:** Domeinmigratie, entiteitssplitsing of wijziging van identifierbeleid.
