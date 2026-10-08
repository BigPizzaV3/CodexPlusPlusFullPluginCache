# Generic LLM Adapter

Use this adapter when the target LLM has no native skill mechanism but accepts a system prompt, developer prompt, custom instruction, persona, or equivalent high-priority context.

## Procedure

1. Open `../SKILL.md`.
2. If the target interface accepts Markdown with YAML frontmatter, pass the file as-is.
3. Otherwise remove only the YAML frontmatter between the first two `---` markers.
4. Place the remaining `SKILL.md` body in the highest-priority instruction field available.
5. Put the learner's request in the ordinary user-message field.

The adapter deliberately does not duplicate the skill text. `SKILL.md` is the canonical source.

## Minimal wrapper when a wrapper is required

```text
Follow the Socratic Tutor instructions supplied below unless they conflict with higher-priority host instructions or the user's explicit request for a direct answer.

[INSERT THE BODY OF SKILL.md HERE]
```

Do not add vendor-specific tool syntax unless the target runtime requires it.
