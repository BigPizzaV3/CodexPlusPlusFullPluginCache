# Human Prose Editor

A skills-only OpenAI plugin for editing, auditing, and drafting prose while suppressing common LLM writing habits without flattening the writer's voice.

## What is in the package

- `.codex-plugin/plugin.json`: plugin manifest
- `skills/human-prose/SKILL.md`: trigger and working instructions
- `skills/human-prose/references/ai-writing-patterns.md`: detailed pattern inventory
- `skills/human-prose/references/final-check.md`: final editing and fiction checks
- `skills/human-prose/references/SOURCES.md`: provenance and attribution
- `SUBMISSION.md`: listing copy and trigger tests for a public submission

This plugin contains no app, MCP server, external account connection, or code execution. It is instruction-only.

## Before publishing

Open `.codex-plugin/plugin.json` and replace both instances of `Local Author` with the publisher name you want shown. Add website, privacy, terms, logo, or repository fields only if you actually have them. Do not invent URLs just to fill optional fields.

## Testing

The skill should activate for requests that explicitly ask to de-AI, humanize, de-slop, remove AI-writing patterns, audit for AI-slop, repair dialogue or cadence, rebuild weak narrative architecture, or draft finished fiction using these rules. Substantial fiction should pass the structural and cadence quality gate before its first visible output.

It should stay out of ordinary translation, summarization, factual questions, and grammar-only proofreading unless the user also asks for anti-AI style treatment.

Use the positive and negative trigger cases in `SUBMISSION.md` when testing.
