# Uitvoercontract: query-network

## Doel

Verbind queries, intenties, taken, entiteiten, contexten, bewijsbehoeften en contentbeslissingen.

## Primaire modus

`ontwerpen`

## Verplichte resultaatvelden

- `source_context`
- `central_user_task`
- `primary_entity`
- `scope_boundary`
- `nodes`
- `relations`
- `content_decisions`
- `exclusions`
- `hypotheses`

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
  deliverable_type: query-network
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    source_context: null
    central_user_task: null
    primary_entity: null
    scope_boundary: null
    nodes: null
    relations: null
    content_decisions: null
    exclusions: null
    hypotheses: null
  next_action: null
```
