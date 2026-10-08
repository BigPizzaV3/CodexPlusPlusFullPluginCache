---
name: detect-ai-writing-patterns
description: Diagnose text that feels artificial, generic, over-polished, repetitive, templated, corporate, or characteristically AI-written without claiming authorship detection. Use when a user asks whether a text sounds like AI, why writing feels unnatural, which passages are generic, where voice is missing, what an AI detector might react to, or wants a line-level style audit before rewriting; support German, English, marketing, business, academic, social, email, script, and personal writing.
---

# Detect AI Writing Patterns

Analyze the writing, not the identity of its author. Do not claim to determine whether a human or AI wrote the text.

## Workflow

1. Establish language, audience, purpose, medium, desired voice, and whether a reference sample exists.
2. Preserve the difference between an intentional formal style and accidental generic language.
3. Read `references/pattern-rubric.md` and inspect the complete text before marking individual passages.
4. Identify only supported patterns. Quote the shortest useful excerpt and explain its effect in context.
5. Distinguish:
   - `strong issue`: clearly harms naturalness, specificity, rhythm, or credibility;
   - `possible issue`: context-dependent or repeated too often;
   - `not an issue`: legitimate wording that merely resembles a common pattern.
6. Look for clusters rather than treating one phrase as proof. Consider repetition, sentence rhythm, abstraction, voice, predictability, and information density together.
7. Do not rewrite unless requested. When requested, hand off to `$humanize-writing` or provide targeted alternatives.

## Output

Return:

1. **Overall impression** — naturalness, voice, specificity, rhythm, and fit for purpose.
2. **Pattern map** — excerpt, pattern, severity, why it matters, and repair direction.
3. **What already sounds human** — elements worth preserving.
4. **Highest-impact changes** — no more than the useful number.
5. **Limitations** — state that style analysis cannot establish authorship or guarantee detector results.

Avoid a mechanical checklist dump when only a few issues are material.

