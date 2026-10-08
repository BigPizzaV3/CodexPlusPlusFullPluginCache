# Uitvoercontract: onderzoeksresultaat

## Doel

Rapporteer onderzoeksbevindingen, bronstatus, beperkingen en resterende vragen.

## Primaire modus

`onderzoeken`

## Verplichte resultaatvelden

- `main_question`
- `findings`
- `source_scope`
- `evidence_status`
- `unresolved_questions`
- `conflicts`
- `update_triggers`
- `readiness`

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
  deliverable_type: onderzoeksresultaat
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    main_question: null
    findings: null
    source_scope: null
    evidence_status: null
    unresolved_questions: null
    conflicts: null
    update_triggers: null
    readiness: null
  next_action: null
```
