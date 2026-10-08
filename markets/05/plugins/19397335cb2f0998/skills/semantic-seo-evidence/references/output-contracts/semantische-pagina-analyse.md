# Uitvoercontract: semantische-pagina-analyse

## Doel

Ontleed een pagina of document op doel, taak, entiteiten, intenties, structuur, claims, bewijs en coverage.

## Primaire modus

`analyseren`

## Verplichte resultaatvelden

- `target`
- `material_scope`
- `page_purpose`
- `user_task`
- `source_context`
- `entities`
- `intents`
- `contextual_qualifiers`
- `structure`
- `claims`
- `topical_coverage`
- `content_roles`
- `observations`
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
  deliverable_type: semantische-pagina-analyse
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    target: null
    material_scope: null
    page_purpose: null
    user_task: null
    source_context: null
    entities: null
    intents: null
    contextual_qualifiers: null
    structure: null
    claims: null
    topical_coverage: null
    content_roles: null
    observations: null
    limitations: null
  next_action: null
```
