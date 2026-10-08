# Uitvoercontract: onderhoudsrapport

## Doel

Leg update-trigger, impact, besluiten, changelog, versie en releasegereedheid vast.

## Primaire modus

`onderhouden`

## Verplichte resultaatvelden

- `trigger`
- `affected_records`
- `comparison`
- `decisions`
- `affected_outputs`
- `affected_pages`
- `change_log_ids`
- `version_decision`
- `tests`
- `release_readiness`

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
  deliverable_type: onderhoudsrapport
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    trigger: null
    affected_records: null
    comparison: null
    decisions: null
    affected_outputs: null
    affected_pages: null
    change_log_ids: null
    version_decision: null
    tests: null
    release_readiness: null
  next_action: null
```
