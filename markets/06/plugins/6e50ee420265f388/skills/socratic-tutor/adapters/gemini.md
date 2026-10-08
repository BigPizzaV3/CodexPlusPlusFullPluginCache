# Gemini Adapter

`SKILL.md` remains the canonical source.

## Gemini environments with reusable skills/instructions

Install or register the whole `socratic-tutor` directory when the runtime supports Agent Skills or an equivalent reusable-instruction mechanism.

If the runtime expects only a prompt or instruction file, use the body of `../SKILL.md` as the canonical instruction content rather than converting it into a separate Gemini-specific prompt.

## Gemini chat or API-style use

Place the `SKILL.md` body in the highest-priority system/instruction field available, and keep the learner's request as the user turn.

Do not duplicate or paraphrase the behavior in this adapter. This file exists only to explain loading strategy.
