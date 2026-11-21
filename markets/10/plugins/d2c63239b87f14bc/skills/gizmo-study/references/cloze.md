# Cloze: retrieval in context

Use `kind: "cloze"` and `question_format: "CLOZE"`. Hide a meaningful term in a sentence with enough visible context to make its answer unambiguous. This is an interactive fill-in-the-blank question, not a plain front/back card.

Prefer this kind when the learner should retrieve an answer rather than recognise it among choices. It fits names and places in literature/history, terminology in science, vocabulary in a natural sentence, and meaningful parts of formulas. For example, turn “Who is the king of Ithaca?” into “The king of Ithaca who returns after the Trojan War is [Odysseus](#segment-king).” Keep enough context for one defensible answer, hide only the target concept, and avoid answer leaks elsewhere in the prompt. Do not blank arbitrary words or replace a whole explanation with a long hidden passage.

Encode each blank as `[hidden text](#segment-KEY)`. Every key must have a matching `segments.KEY` array with exactly one correct answer whose `value` equals the hidden text **and at least two plausible incorrect distractors**. Aim for three useful distractors when the material supports them; two is the required minimum. Use unique keys made of letters, digits, underscores, or hyphens. Omit `prompt.back` by default, or set it to null, except when it holds a target-language cloze sentence for translation practice. Gizmo displays this text while the learner is answering; it is not post-answer feedback. If a back is useful, hide any tested answer there with its segment marker; any remaining visible context must not disclose a blank, its synonym, or an explanation that effectively supplies the answer. The same rule applies to unhidden front text. Never use an unmarked sentence as a cloze question.

Read [answer quality](answer-quality.md) for every segment. Write distractors that fit the sentence grammatically, belong to the same category, have similar lengths, and are definitively wrong in context. Supply these alternatives explicitly; do not leave the correct answer alone or rely on enrichment to invent distractors. If useful alternatives cannot be written, choose another interactive approach. Do not include external links or URLs; only the required `#segment-KEY` markers may appear in the front or back. If a meaningful blank cannot be formed, use true/false instead.

For a blank asking for “severity”, a back beginning “Severity describes impact” reveals the answer. Omit it. Do not place the unhidden answer or solved sentence on the back. A hidden answer is allowed on either side: segment markers must correspond to the same `segments` entries wherever they appear.

## Payload example

```json
{
  "kind": "cloze",
  "question": {
    "question_format": "CLOZE",
    "prompt": {
      "front": "Odysseus is king of [Ithaca](#segment-home)."
    },
    "segments": {
      "home": [
        {
          "type": "correct",
          "value": "Ithaca"
        },
        { "type": "incorrect", "value": "Sparta" },
        { "type": "incorrect", "value": "Troy" },
        { "type": "incorrect", "value": "Pylos" }
      ]
    }
  }
}
```

## Language-practice layout

Apply this guidance to any language pair. For vocabulary pairs and translation practice, separate the source sentence and its translation. Follow the requested direction, including native-to-learning-language production practice. When direction is unspecified, use the supplied learning language on the front and the learner’s language on the back if those roles are clear from context; never assume either language is English or Spanish. Use only the source sentence on the front and the target-language cloze sentence on the back. For all language practice, omit instruction preambles such as “Complete the translation”, “Translate the following”, or “Fill in the blank”, including equivalents in other languages; the two sentences and hidden segment already express the task. Do not concatenate instructions and both sentences into one front. A back containing a hidden segment is an active part of the question, not an answer explanation. The default instruction to omit backs does not apply to this translation layout: `back` is required for these exercises.

For monolingual vocabulary or grammar practice, use a natural sentence with a hidden target directly; do not add an unnecessary translation or instruction preamble.

Before saving each translation card, inspect the fields: front = source sentence only, back = target sentence with at least one segment marker. The front must have no segment marker. Never use `"front": "source sentence\n\ntarget sentence with a blank"` with an omitted back; it is still one front. Split that payload into separate `front` and `back` fields. Preserve the segment key, correct answer, and distractors when splitting.

Keep sentences natural and appropriate to the learner’s level, use the supplied vocabulary, and hide the word being practised in the target-language translation. Distractors must be target-language alternatives that fit that blank grammatically and remain wrong for the source sentence. Do not add the unhidden translation anywhere else.

The following is one illustrative language pair; the layout applies equally to other languages and either translation direction.

```json
{
  "kind": "cloze",
  "question": {
    "question_format": "CLOZE",
    "prompt": {
      "front": "Voy a la escuela.",
      "back": "I go to [school](#segment-place)."
    },
    "segments": {
      "place": [
        { "type": "correct", "value": "school" },
        { "type": "incorrect", "value": "work" },
        { "type": "incorrect", "value": "church" }
      ]
    }
  }
}
```
