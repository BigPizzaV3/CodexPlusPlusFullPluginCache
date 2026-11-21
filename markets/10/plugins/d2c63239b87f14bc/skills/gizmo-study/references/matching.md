# Matching: associations

Use `kind: "match_pairs"` and `question_format: "MATCH_PAIRS"` for clear associations such as characters and roles, structures and functions, or words and meanings. **At least three distinct pairs are required by the MCP schema**, giving at least three choices on each side. If fewer are available, use another interactive question, with true/false as the fallback; do not invent associations to reach the minimum.

Supply `prompt.front`; `prompt.back` is optional and should be omitted by default. The `answers` field is an array of `[left, right]` pairs; each side is an answer object with `type: "correct"` and `value`. Do not use bare strings or invent a `pairs` field. Every item must have one unambiguous matching partner; avoid duplicate labels or interchangeable counterparts. Do not give away the matching associations in visible supporting context. Preserve the real associations rather than changing them for visual balance.

## Payload example

```json
{
  "kind": "match_pairs",
  "question": {
    "question_format": "MATCH_PAIRS",
    "prompt": {
      "front": "Match each character to their relationship with Odysseus."
    },
    "answers": [
      [
        {
          "type": "correct",
          "value": "Penelope"
        },
        {
          "type": "correct",
          "value": "Wife"
        }
      ],
      [
        {
          "type": "correct",
          "value": "Telemachus"
        },
        {
          "type": "correct",
          "value": "Son"
        }
      ],
      [
        {
          "type": "correct",
          "value": "Laertes"
        },
        {
          "type": "correct",
          "value": "Father"
        }
      ]
    ]
  }
}
```
