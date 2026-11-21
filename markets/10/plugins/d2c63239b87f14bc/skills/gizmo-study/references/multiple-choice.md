# Selection: multiple applicable answers

Use `kind: "select_multiple"` and `question_format: "SELECT_MULTIPLE"` only for a genuine set of applicable answers. Every question needs **at least four options, at least two correct options, and at least one incorrect option**. Never use it for a single correct answer or mark a false option correct to meet the minimum. For a single-answer fact or calculation, prefer cloze with distractors or a precise true/false statement; otherwise reframe the learning objective as a factual set.

Read [answer quality](answer-quality.md) before drafting options. Supply all correct options and plausible distractors rather than relying on enrichment. Let the facts determine how many options are correct; do not make the correct count predictable. If a useful, balanced set cannot meet the minimums, choose another interactive approach without filler.

Supply `prompt.front`; `prompt.back` is optional and should be omitted by default. Say “Select all that apply” in the task. Each answer contains `type` (correct or incorrect) and `value`. Keep option text concise and parallel; do not give away the correct options in visible supporting context. Do not include links or URLs in any field.

Compare word counts and approximate character lengths before saving. If a correct option stands out by length or detail, shorten it or rewrite the distractors naturally while retaining their wrong ideas. If balanced, clearly wrong distractors cannot be written, choose another interactive approach or use true/false.

## Payload example

```json
{
  "kind": "select_multiple",
  "question": {
    "question_format": "SELECT_MULTIPLE",
    "prompt": {
      "front": "Which characters help Odysseus return home? Select all that apply."
    },
    "answers": [
      {
        "type": "correct",
        "value": "Athena"
      },
      {
        "type": "incorrect",
        "value": "Polyphemus"
      },
      {
        "type": "correct",
        "value": "Nausicaa"
      },
      {
        "type": "incorrect",
        "value": "The suitors"
      }
    ]
  }
}
```
