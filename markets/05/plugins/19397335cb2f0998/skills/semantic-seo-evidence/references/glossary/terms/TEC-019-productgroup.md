---
term_id: TEC-019
preferred_name_nl: ProductGroup
english_name: ProductGroup
cluster_id: 7
cluster_name: Technische semantiek en zoektoegang
type_context: Schema.org-type / productvarianten
evidence_labels:
- A
- B
last_checked: '2026-07-25'
source_ids:
- SRC-095
- SRC-101
related_term_ids:
- ENT-010
- QLT-021
- TEC-013
- TEC-018
status: active
---

# ProductGroup

**Engelse term of afkorting:** ProductGroup  
**Term-ID:** `TEC-019`  
**Hoofdcategorie:** 7 Technische semantiek en zoektoegang  
**Type en context:** Schema.org-type / productvarianten  
**Bewijsbasis:** A en B  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

ProductGroup is een Schema.org-type voor een groep producten die varianten van hetzelfde basismodel vormen.

## Afbakening

Eigenschappen zoals variesBy, hasVariant en productGroupID kunnen aangeven waarop varianten verschillen en welke Product-objecten bij de groep horen.

## Wat is bevestigd?

- Google ondersteunt ProductGroup voor het groeperen van productvarianten.

- Varianten kunnen op één pagina of meerdere URL’s worden aangeboden, met verschillende implementatievoorwaarden.

## Wat is niet bevestigd?

- Dat ieder vergelijkbaar model binnen één ProductGroup hoort.

- Dat kleuren, accupakketten en snelheidsuitvoeringen zonder afzonderlijke productidentiteit mogen worden samengevoegd.

## Praktische toepassing

1. Definieer welke kenmerken werkelijk variantbepalend zijn.

2. Geef iedere variant eigen identifiers en actuele waarden.

3. Voorkom dat specificaties van één variant op de hele groep worden toegepast.

## Voorbeeld

Een modelreeks kan varianten met verschillende accuconfiguraties bevatten, mits de relatie en eigen specificaties duidelijk zijn.

## Veelgemaakte misvatting

ProductGroup is geen categoriepagina voor alle scootmobielen van een merk.

## Zie ook

- Product

- Product Variant

- Entity Resolution

- @id

- Data Quality

## Verwante begrippen

- `ENT-010`: Entity Resolution
- `QLT-021`: Data Quality
- `TEC-013`: @id
- `TEC-018`: Product
- Product Variant *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-095, SRC-101

**Update-trigger:** Nieuwe variantstructuur, modelgeneratie of gewijzigde productidentifiers.
