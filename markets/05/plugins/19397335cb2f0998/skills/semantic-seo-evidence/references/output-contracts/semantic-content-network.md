# Uitvoercontract: semantic-content-network

## Doel

Ontwerp contentassets, zelfstandige taken, relaties, canonical owners en overlapcontrole.

## Primaire modus

`ontwerpen`

## Verplichte resultaatvelden

- `central_user_mission`
- `assets`
- `relations`
- `overlap_controls`
- `fact_source`
- `maintenance_owner`

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
  deliverable_type: semantic-content-network
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    central_user_mission: null
    assets: null
    relations: null
    overlap_controls: null
    fact_source: null
    maintenance_owner: null
  next_action: null
```
