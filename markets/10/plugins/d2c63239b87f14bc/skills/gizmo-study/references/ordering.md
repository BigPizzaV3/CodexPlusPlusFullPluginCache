# Ordering: sequences and chronology

Use `kind: "order_items"` and `question_format: "ORDER_ITEMS"` only for a meaningful, unambiguous sequence. **At least three distinct items are required by the MCP schema.** A two-item exercise must become another interactive question, using true/false if necessary; do not add filler steps.

State the ordering criterion on the front: earliest to latest, process order, or another explicit rule. For non-linear narratives, distinguish chronological events from order of narration. Do not imply that an optional solution method is the only valid sequence.

Supply `prompt.front`; `prompt.back` is optional and should be omitted by default. Each answer is an object with `type: "correct"`, `value`, and a distinct zero-based `ordinance` matching the true order (0, 1, 2, …). The spelling is `ordinance`. Do not give away the correct order in visible supporting context. Do not change the true order to balance option lengths.

## Payload example

```json
{
  "kind": "order_items",
  "question": {
    "question_format": "ORDER_ITEMS",
    "prompt": {
      "front": "Order these events in Odysseus's journey, earliest to latest."
    },
    "answers": [
      {
        "type": "correct",
        "value": "Leaves Calypso's island",
        "ordinance": 0
      },
      {
        "type": "correct",
        "value": "Reaches the Phaeacians",
        "ordinance": 1
      },
      {
        "type": "correct",
        "value": "Returns to Ithaca",
        "ordinance": 2
      }
    ]
  }
}
```
