# Transaction interface

The bundled `scripts/aidm_campaign.py` accepts a JSON domain delta.

## Allowed top-level keys

- `status_patch`
- `ledger_append`
- `project_updates`
- `timeline_append`
- `recap_append`
- `source_references`

Unknown keys are rejected.

## Example

```json
{
  "status_patch": {
    "location": "Upper Lens Chamber",
    "resources": {
      "actions": 2,
      "credits": 35
    }
  },
  "ledger_append": [
    {
      "account": "credits",
      "amount": -5,
      "unit": "credit",
      "memo": "Replacement lens mount",
      "provenance": "EXACT"
    }
  ],
  "project_updates": [
    {
      "progress_id": "progress:align-observatory",
      "status": "ACTIVE",
      "state": {
        "stages": ["survey", "align", "verify"],
        "current_stage": "align",
        "completed_stages": ["survey"]
      }
    }
  ],
  "timeline_append": [
    {
      "summary": "The survey identified the warped lens mount.",
      "provenance": "GENERATED_CANON"
    }
  ],
  "recap_append": "The survey is complete; alignment remains.",
  "source_references": [
    "player-declaration",
    "project:progress:align-observatory"
  ]
}
```

The player declaration is recorded separately and exactly. Never place invented
player action, dialogue, intent, tactics, power use, emotion, belief, conclusion,
priority, allocation, or acceptance fields in the delta.

## Atomicity and recovery

The database transaction verifies the expected prior head and previous
transaction hash, applies domain deltas, inserts the transaction, advances the
state head, rebuilds projections, verifies head equality, and commits or rolls
back as one unit.

The external manifest is atomically replaced afterward. A recovery marker lets
`repair-manifest` or an idempotent replay finish synchronization after an
interrupted manifest write.
