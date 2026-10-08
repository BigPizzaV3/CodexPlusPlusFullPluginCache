# ChatGPT / Codex Adapter

`SKILL.md` remains the canonical source.

## Skill-aware environments

If the OpenAI runtime supports Agent Skills or a compatible skills directory, install the entire `socratic-tutor` folder as one skill and preserve the directory name.

For Codex-style local environments that recognize the cross-runtime Agent Skills location, a common installation layout is:

```text
~/.agents/skills/socratic-tutor/SKILL.md
```

Copy the entire directory, not only `SKILL.md`, so the behavioral tests remain available.

## Chat interfaces without local skill installation

Use the body of `../SKILL.md` as a developer/system-level instruction or as the highest-priority reusable instruction mechanism offered by the interface.

Do not translate the skill into XML. The Markdown core already contains the behavioral contract.
