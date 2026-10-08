# Uitvoercontract: topical-map

## Doel

Leg broncontext, gebruikersmissie, domeingrenzen, entiteiten, taakclusters, contextlagen, contentrollen, bewijs en prioriteiten vast.

## Primaire modus

`ontwerpen`

## Verplichte resultaatvelden

- `source_context`
- `central_user_mission`
- `knowledge_domain`
- `entities`
- `task_clusters`
- `contextual_layers`
- `content_roles`
- `priorities`
- `exclusions`
- `open_questions`
- `version`

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
  deliverable_type: topical-map
  status: provisional
  source_scope: {}
  assumptions: []
  warnings: []
  blockers: []
  result:
    source_context: null
    central_user_mission: null
    knowledge_domain: null
    entities: null
    task_clusters: null
    contextual_layers: null
    content_roles: null
    priorities: null
    exclusions: null
    open_questions: null
    version: null
  next_action: null
```
