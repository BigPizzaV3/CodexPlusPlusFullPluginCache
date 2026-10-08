# B2B Messaging Workshop

A self-guided B2B messaging workshop that produces your Product Marketing Source of Truth.

The plugin guides a founder or product marketer through the [Eldur Studio](https://eldur.studio) framework one section at a time. The canonical framework numbers these phases 0–3; the UI also labels their ordinal position so the fourth and final phase is unmistakable:

1. Company snapshot
2. Product marketing strategy
3. Positioning
4. Pressure test

At every step it shows only the relevant guidance or prompt from the Notion template, asks focused questions, and checks the answer for specificity and evidence. Saying `example` reveals one clearly fictional ExampleCo Legal answer without advancing the workshop or changing the user's work.

When the user asks for `help`, the workshop explains the decision, offers grounded answer shapes, and recommends a useful direction without inventing company facts. It also collects quote provenance and anonymization preferences together, supports a single consolidated persona for simple self-serve purchases, and turns missing proof into a concrete validation plan.

## What v1 includes

- A free, skills-only plugin with no hosted server, account, database, or telemetry.
- Natural answers plus optional text commands: `example`, `help`, `skip`, `back`, and `pause`.
- Copyable checkpoints that preserve progress, approved answers, hypotheses, and gaps.
- Evidence and provenance rules that keep invented claims out of the result.
- Phase 2 synthesis from approved inputs and a six-part pressure test.
- A clean Markdown source of truth with approved answers and no template instructions or guidance callouts.
- Optional creation of the same clean document as a separate Notion page when Notion is connected and the user confirms the write.

The workshop describes these as text replies and does not make them look like clickable buttons. Phase-level guidance appears once; each question uses its own Notion guidance or field prompt. The plugin never changes the canonical Notion template.

## Starter prompts

- `Start my B2B messaging workshop.`
- `Resume my messaging workshop from this checkpoint: ...`
- `Pressure-test my existing B2B messaging framework.`

## Repository structure

- `.codex-plugin/plugin.json` — plugin identity and starter prompts.
- `skills/run-b2b-messaging-workshop/` — the guided workshop skill.
- `skills/run-b2b-messaging-workshop/references/` — canonical template, question bank, synthesis rules, fictional examples, and evidence rules.
- `tests/publication-evals.md` — eleven positive, three negative, and behavioral publication checks.
- `tests/fixtures/` — reproducible research, checkpoint, and pressure-test fixtures.

## Validate locally

Run the OpenAI plugin and skill validators from their installed creator skills, then exercise the publication prompts in fresh conversations. The full expected behavior is documented in `tests/publication-evals.md`.

Public submission also requires verified publisher identity, a logo, website, support contact, privacy-policy and terms URLs, availability regions, and release notes. Those distribution details are intentionally not fabricated in this repository.

The canonical template and its guidance are owned by [Eldur Studio LLC](https://eldur.studio). Copyright [Eldur Studio LLC](https://eldur.studio) 2026.
