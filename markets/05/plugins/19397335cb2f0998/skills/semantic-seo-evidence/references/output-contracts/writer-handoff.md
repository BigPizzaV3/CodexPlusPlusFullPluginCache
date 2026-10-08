# Uitvoercontract: writer-handoff

## Doel

Draag semantisch goedgekeurde inhoud veilig over aan een schrijversskill.

## Primaire modus

`verbeteren`

## Verplichte resultaatvelden

- `contract_name`
- `status`
- `target`
- `audience`
- `user_task`
- `entity_scope`
- `content_scope`
- `structure`
- `claims`
- `factual_locks`
- `locked_elements`
- `writer_freedom`
- `style_skill`
- `evidence`
- `warnings`
- `blockers`
- `return_conditions`

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
  deliverable_type: writer-handoff
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    contract_name: null
    status: null
    target: null
    audience: null
    user_task: null
    entity_scope: null
    content_scope: null
    structure: null
    claims: null
    factual_locks: null
    locked_elements: null
    writer_freedom: null
    style_skill: null
    evidence: null
    warnings: null
    blockers: null
    return_conditions: null
  next_action: null
```
