---
name: mental-models
description: Search, read, compare, and connect entries in The Business Engineer complete mental-models library. Use for a model name or ID, ontology navigation, source reconciliation, practice-instrument lookup, or selecting models for a decision.
---

# The complete mental-models library

Use the bundled retrieval script instead of reading the entire catalog into context. The plugin root is two directories above this skill directory. The command guide is [Library commands](../../references/library-commands.md).

A focused lookup usually needs:

1. `search "mechanism or name" --limit 8` to locate candidates.
2. `get <exact-ID>` to read the full definition, application, question, provenance, and retained earlier context.
3. `links <exact-ID>` when relationships matter.

Search defaults to the 1,052-entry consolidated catalog. Use `--collection core`, `disciplines`, `instruments`, `concepts`, or `all` deliberately. Search scores rank text matches; they are not confidence scores or proof that a model fits the case. Read full records before interpreting or comparing them.

## Identity and completeness

Read [Identity and evidence](../../references/identity-and-evidence.md) when working with source numbers, older entries, counts, or framework status.

- `core:137` and `BE-00-137` identify core model 137.
- `concept:137` and `BE-M0137` identify a different entry in the earlier ontology.
- `instrument:J` and `BE-P-J` identify practice instrument J.
- The script rejects a bare numeric ID because its namespace is ambiguous.
- Fifty previous IDs redirect to canonical homes and retain the earlier seat-specific text. Report that context when it materially differs.

For a broad decision, use `routes` or `practice routing` to find the relevant path and counter-lens. Retrieve only the required definitions and instruments. An authored route is a guide for inquiry, not a validated decision procedure.

For a model answer, explain the mechanism, useful conditions, boundary or falsifier, and one concrete application if requested. Preserve source attribution and epistemic status. Do not invent missing calibrations or claim every entry has empirical validation.

Use visual-atlas when the user wants the interactive library itself, and business-analysis when they want a full strategic application.
