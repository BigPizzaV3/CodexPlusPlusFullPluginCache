# Socratic Tutor Portable Skill — Design

## Goal

Convert the original XML-style Socratic tutor prompt into one canonical, provider-agnostic skill that preserves behavior across heterogeneous LLM runtimes.

## Architecture

The package uses `SKILL.md` as the only behavioral source of truth. Adapters contain loading instructions only, so provider-specific packaging cannot drift from the teaching method. Behavioral conformance scenarios complement structural validation because syntactically valid skills can still be ignored or weakly followed by a model.

## Portability boundary

Behavioral portability is achievable for instruction-following LLMs. Native installation portability is runtime-dependent because vendors expose different extension and prompt mechanisms. The generic adapter provides the fallback path.

## Core invariants

- one core question per guided turn;
- scaffold from demonstrated learner knowledge;
- reveal direct answers when explicitly requested;
- directly answer purely factual requests;
- use contradictions to surface misconceptions where appropriate;
- respect higher-priority host and safety instructions;
- avoid vendor-specific syntax in the canonical skill.
