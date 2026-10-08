# Uitvoercontract: semantic-content-brief

## Doel

Maak een inhoudelijk veilig contract voor productie of schrijven.

## Primaire modus

`ontwerpen`

## Verplichte resultaatvelden

- `target`
- `user_task`
- `audience`
- `primary_entity`
- `secondary_entities`
- `contextual_qualifiers`
- `intents`
- `scope`
- `required_sections`
- `required_facts`
- `bounded_claims`
- `prohibited_claims`
- `unresolved_questions`
- `internal_link_needs`
- `media_needs`
- `cta_role`
- `writer_handoff_ready`

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
  deliverable_type: semantic-content-brief
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    target: null
    user_task: null
    audience: null
    primary_entity: null
    secondary_entities: null
    contextual_qualifiers: null
    intents: null
    scope: null
    required_sections: null
    required_facts: null
    bounded_claims: null
    prohibited_claims: null
    unresolved_questions: null
    internal_link_needs: null
    media_needs: null
    cta_role: null
    writer_handoff_ready: null
  next_action: null
```
