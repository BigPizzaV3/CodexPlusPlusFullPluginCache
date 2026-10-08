# Uitvoercontract: onderzoeksscope

## Doel

Leg vast wat onderzocht moet worden en welke bronnen en bewijssoorten nodig zijn.

## Primaire modus

`onderzoeken`

## Verplichte resultaatvelden

- `main_question`
- `user_task`
- `scope_included`
- `scope_excluded`
- `primary_entity`
- `contextual_qualifiers`
- `research_questions`
- `candidate_claims`
- `available_sources`
- `missing_sources`
- `stop_criteria`
- `acceptance_criteria`

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
  deliverable_type: onderzoeksscope
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    main_question: null
    user_task: null
    scope_included: null
    scope_excluded: null
    primary_entity: null
    contextual_qualifiers: null
    research_questions: null
    candidate_claims: null
    available_sources: null
    missing_sources: null
    stop_criteria: null
    acceptance_criteria: null
  next_action: null
```
