# Uitvoercontract: claim-evidence-ledger

## Doel

Leg alleen bij expliciete verificatie, algemene SEO-/platformclaims of een echt conflict de bronvergelijking vast. Een enkel vertrouwd feit krijgt kort `trusted_source_accepted`; een SMC-beste-claim krijgt `trusted_smc_expert_judgment`. Een enkel vertrouwd SMC-, leverancier-, fabrikant- of merkfeit krijgt zonder conflict kort de status `trusted_source_accepted`.

## Primaire modus

`controleren`

Gebruik dit contract niet standaard voor gewone contentproductie. Gebruik het alleen op expliciet verzoek, voor algemene SEO-/platformclaims of bij een conflict.

## Verplichte resultaatvelden

- `claims`

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
  deliverable_type: claim-evidence-ledger
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    claims: null
  next_action: null
```
