# True/false: misconception checks and fallback

Use `kind: "true_or_false"` and `question_format: "TRUE_OR_FALSE"`. This is the fallback when a fact cannot naturally support another interactive format, or a matching/ordering exercise would have fewer than three entries. Never substitute a plain front/back card.

Write one precise, objectively testable statement. Provide exactly two answers, “True” and “False”, with exactly one correct and one incorrect. Supply `prompt.front`. The back is optional; omit it by default and do not add text that gives away whether the statement is true.

Avoid ambiguous qualifiers, double negatives, disputed interpretations, and false statements made obvious by absurd details. Across a deck, avoid an obvious pattern of all statements being true or all being false; do not invent false claims merely to meet a ratio. Keep answer labels unchanged.

## Payload example

```json
{
  "kind": "true_or_false",
  "question": {
    "question_format": "TRUE_OR_FALSE",
    "prompt": {
      "front": "Telemachus is Odysseus's father."
    },
    "answers": [
      {
        "type": "incorrect",
        "value": "True"
      },
      {
        "type": "correct",
        "value": "False"
      }
    ]
  }
}
```
