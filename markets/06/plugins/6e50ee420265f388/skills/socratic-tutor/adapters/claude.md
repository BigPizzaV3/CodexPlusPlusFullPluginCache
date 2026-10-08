# Claude Adapter

`SKILL.md` remains the canonical source.

## Claude environments with skill loading

Where the environment supports local skills, install the whole `socratic-tutor` directory in the runtime's supported skill location. Claude Code setups commonly use a per-user skills directory such as:

```text
~/.claude/skills/socratic-tutor/SKILL.md
```

If the environment also supports the cross-runtime Agent Skills alias, the same skill can be mirrored or linked there rather than rewritten.

## Claude chat or API-style use

If there is no skill loader, place the body of `../SKILL.md` in the system/high-priority instruction field. Pass the learner's messages separately.

Do not maintain a Claude-specific behavioral fork. Any behavior change belongs in `SKILL.md`.
