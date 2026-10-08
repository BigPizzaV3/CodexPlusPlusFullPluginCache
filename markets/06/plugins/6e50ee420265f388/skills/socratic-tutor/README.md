# Socratic Tutor Skill

A provider-agnostic Socratic tutoring skill designed to work across instruction-following LLMs.

## What "portable" means

The behavioral core is ordinary Markdown and does not rely on a specific vendor API, XML prompt syntax, tools, or function calls. A runtime that supports the Agent Skills convention can install the directory directly. A runtime without skill loading can still use the same `SKILL.md` body as a system/developer instruction.

Native installation cannot be literally identical across every LLM product because products expose different extension mechanisms. The adapters in `adapters/` explain how to reuse the same core without forking its behavior.

## Files

- `SKILL.md` — canonical behavior and metadata.
- `TESTS.md` — behavioral conformance scenarios.
- `tests/validate_package.py` — structural validator.
- `adapters/generic-system-prompt.md` — fallback for any LLM accepting high-priority instructions.
- `adapters/chatgpt-codex.md` — guidance for OpenAI-style skill/instruction runtimes.
- `adapters/claude.md` — guidance for Claude-style skill/instruction runtimes.
- `adapters/gemini.md` — guidance for Gemini-style skill/instruction runtimes.

## Install in an Agent Skills-compatible runtime

Copy the whole `socratic-tutor` directory into the runtime's skills directory. Keep the directory name exactly `socratic-tutor`, matching the `name` field in `SKILL.md`.

Then invoke or allow the runtime to discover the skill when the user's intent is learning, reasoning practice, guided problem solving, or conceptual understanding.

## Use in a generic LLM

Open `SKILL.md`, remove the YAML frontmatter if the target interface does not accept it, and place the remaining Markdown in the highest-priority instruction field available to you.

Do not paste both the canonical skill and a rewritten copy. Duplicated instructions drift over time.

## Design goals

- one canonical behavioral source;
- no vendor-specific commands in the core;
- direct-answer escape hatch when the learner asks for it;
- progressive scaffolding rather than indiscriminate questioning;
- factual questions answered directly;
- explicit misconception handling;
- testable behavioral invariants.

## Validation

Run:

```bash
python tests/validate_package.py
```

Then use the scenarios in `TESTS.md` against each target model/runtime. Structural validation cannot guarantee behavioral compliance, so both layers matter.
