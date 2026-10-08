# Uitvoercontract: begripuitleg

## Doel

Leg één of meer begrippen uit met definitie, afbakening, bewijsgrens, praktisch gebruik en misvatting.

## Primaire modus

`uitleggen`

## Verplichte resultaatvelden

- `term_id_or_terms`
- `short_definition`
- `scope_boundary`
- `confirmed`
- `not_confirmed`
- `practical_use`
- `common_misconception`
- `evidence_status`
- `limitations`

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
  deliverable_type: begripuitleg
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    term_id_or_terms: null
    short_definition: null
    scope_boundary: null
    confirmed: null
    not_confirmed: null
    practical_use: null
    common_misconception: null
    evidence_status: null
    limitations: null
  next_action: null
```
