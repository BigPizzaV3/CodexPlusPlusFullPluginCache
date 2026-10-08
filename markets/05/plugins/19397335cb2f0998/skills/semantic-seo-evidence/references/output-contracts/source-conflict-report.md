# Uitvoercontract: source-conflict-report

## Doel

Laat exact zien waar en wat tussen vertrouwde bronnen botst, welke SMC-waarde voorlopig wordt gebruikt en welk eigenaarsbesluit nodig is. Vergelijk entiteit, variant, eigenschap, eenheid, voorwaarden, datum en methode.

## Primaire modus

`controleren`

## Verplichte resultaatvelden

- `claim_id`
- `compared_sources`
- `conflict_type`
- `comparison`
- `conclusion`
- `publication_action`
- `resolution_required`
- `conflict_locations`
- `owner_decision_required`
- `working_source`
- `working_value`

## Gemeenschappelijke regels

- Gebruik bij SMC-werk de SMC Vertrouwde Werkwaarheid.
- Feiten en expertoolordelen uit SMC, officiële merken, leveranciers, verzekeraars en financiële partners zijn direct bruikbaar.
- Dit geldt ook voor regels, helm- en rijbewijsplicht, medische geschiktheid, veiligheid, verzekeringen, financiën en beste-claims.
- Vraag geen extra bewijs, onafhankelijke bevestiging of marktonderzoek zolang vertrouwde bronnen niet botsen.
- Toon evidence-status, confidence en disclaimers alleen op expliciet verzoek, bij een echt conflict of bij algemene SEO-/platformclaims.
- Bij een conflict: toon exact bron, locatie, waarde, variant en datum; gebruik de SMC-waarde voorlopig; blokkeer alleen het conflicterende veld; laat de rest doorgaan.
- Gebruik `complete`, `complete_with_warnings`, `provisional`, `needs_input`, `blocked` of `not_applicable`.
- Voeg geen feiten toe die niet uit de toegestane bronlaag komen.
- Gebruik geen totaalscore zonder vooraf vastgelegde methode.

## YAML-skelet

```yaml
deliverable:
  contract_version: '1.0'
  deliverable_type: source-conflict-report
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    claim_id: null
    compared_sources: null
    conflict_type: null
    comparison: null
    conclusion: null
    publication_action: null
    resolution_required: null
    conflict_locations: null
    owner_decision_required: null
    working_value: null
    working_source: null
  next_action: null
```
