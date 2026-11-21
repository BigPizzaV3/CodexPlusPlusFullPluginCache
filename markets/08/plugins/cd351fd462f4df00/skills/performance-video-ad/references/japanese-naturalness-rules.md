# Japanese naturalness gate

Run this gate after Hook and Body copy drafting and before storyboard or Animatic work.

## Separate copy surfaces

Treat UI labels and spoken copy as different writing tasks.

- UI labels may use compact nouns such as `原因仮説`, `最初の検証`, and `優先理由`.
- Subtitles and narration should use conversational phrases such as `いま何を疑っているか`, `まず何を確かめるか`, and `なぜそれからやるのか`.
- Do not repeat the same sentence as both a UI label and narration. Let the screen show structure while the voice explains the change.

## Human review questions

- Could a colleague say this sentence without sounding like they are reading a specification?
- Can it be read in one breath at the planned pace?
- Does it avoid three or more consecutive noun labels?
- Does it say who changes what, instead of ending only with `整理する`, `見直す`, or `支援する`?
- Is the visible action concrete enough to prove the sentence?
- Does reading it aloud reveal a stumble, repeated meaning, or translation-like ending?

## Forbidden or warning-prone spoken expressions

Reject these in Hook copy, subtitles, narration, and CTA copy unless a canonical source explicitly requires them and the user approves an exception:

- `成果線`
- `営業後工程`
- `初期見立てを相談する`
- `説明できる状態へ`
- `原因候補を見直す`
- `〜を実現`
- `〜を支援`
- `〜が可能となります`

The same compact domain noun may remain in a small UI label when it is natural there. For example, `原因仮説` is acceptable on a document field but should become `いま何を疑っているか` in spoken copy.

## Machine and human boundary

Run:

```bash
node scripts/validate-japanese-naturalness.mjs <hook-packages.json> <body-contract.json> [more...]
```

The script rejects known unnatural phrases and excessive line length, and warns about noun chains, abstract endings, and duplication. Human review still owns voice, nuance, and whether a line sounds natural when spoken.
