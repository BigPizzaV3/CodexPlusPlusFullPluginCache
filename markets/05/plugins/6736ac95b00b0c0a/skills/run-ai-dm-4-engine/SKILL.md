---
name: run-ai-dm-4-engine
description: Run, validate, inspect, transact, checkpoint, or export campaign-agnostic AI-DM 4 text campaigns bound through a Contract-1.1 CAMPAIGN_MANIFEST.json. Use for AI-DM gameplay and slash commands when the user supplies or explicitly selects a Campaign directory or ZIP, and for synthetic campaign/package validation. Never use chat memory as campaign storage or infer authority from filenames.
---

# AI-DM 4 Engine

Treat the Engine as immutable reusable software, the Campaign package as mutable
canon/state, and this Skill as the adapter between them.

## Mandatory boot sequence

1. Resolve the Campaign package the user explicitly supplied or selected.
2. Read `CAMPAIGN_MANIFEST.json` before any other Campaign artifact.
3. Run:

   ```bash
   python3 scripts/aidm_campaign.py validate --campaign <path>
   ```

4. Stop before gameplay or current-state claims when validation fails.
5. Read the Campaign-owned `AI_DM_RUNTIME_PRIMER.md`, then
   `STORY_SO_FAR.md`, then only relevant current records/books.
6. Never select authority by `CURRENT`, `MASTER`, `FINAL`, recency, file size,
   or semantic similarity.

If the surface cannot execute the bundled script or cannot return a changed
Campaign/checkpoint file, state the write limitation before adjudicating. Do
not claim a turn committed when only chat context changed.

Read [ENGINE_CAMPAIGN_CONTRACT_v1.1.md](references/ENGINE_CAMPAIGN_CONTRACT_v1.1.md)
for authority and transaction invariants. Read
[CAMPAIGN_BINDING.md](references/CAMPAIGN_BINDING.md) for directory/ZIP handling.

## Commands

Run visible commands through one manifest-selected projection head:

```bash
python3 scripts/aidm_campaign.py command \
  --campaign <path> --name /status
```

Supported commands are `/status`, `/ledger`, `/projects`, `/timeline`, `/recap`,
and `/save`. For `/save`, provide `--output <checkpoint.zip>`.

Commands do not advance gameplay. Never reveal data marked `SEALED`.

## Substantive turns

Preserve the user's declaration byte-for-byte. Never invent the player
character's voluntary action, dialogue, tactics, power use, beliefs,
conclusions, emotions, priorities, allocations, or acceptance of a bargain.

Before committing:

1. identify phase and Campaign time;
2. retrieve only relevant current authority;
3. adjudicate fair consequences;
4. draft a domain delta;
5. audit arithmetic, chronology, NPC knowledge, correction scope, provenance,
   sealed leakage, and player sovereignty;
6. use one stable unique `turn_id`.

Commit with:

```bash
python3 scripts/aidm_campaign.py turn \
  --campaign <path> \
  --turn-id <stable-id> \
  --declaration '<exact declaration>' \
  --delta-file <delta.json>
```

For a ZIP Campaign, also pass `--output <changed-campaign.zip>`. A directory
Campaign is updated in place and may additionally be exported with `--output`.

Same `turn_id` plus the same exact declaration is an idempotent replay. The
same `turn_id` with different text must be rejected.

The delta grammar and examples are in
[TRANSACTION_INTERFACE.md](references/TRANSACTION_INTERFACE.md).

## Checkpoints and persistence

Commit internal Campaign state after each substantive turn. Create an external
checkpoint on `/save`, explicit request, major boundary, migration, or major
milestone:

```bash
python3 scripts/aidm_campaign.py checkpoint \
  --campaign <path> --output <checkpoint.zip>
```

A checkpoint must not advance the gameplay state head or transaction hash.
Return the changed Campaign/checkpoint file to the user. Chat memory is never a
save mechanism.

## Provenance and progress

Use only these material provenance classes:

- `EXACT`
- `DERIVED`
- `GENERATED_CANON`
- `NORMALIZED`
- `BOUNDED`
- `FUTURE_UNKNOWN`
- `SEALED`
- `NOT_TRACKED`

Use the typed Progress Models in
[PROGRESS_MODEL_1.0.md](references/PROGRESS_MODEL_1.0.md). Do not flatten every
unfinished fact into one generic X/Y clock.

## First Establishment and corrections

Generate a previously undefined world fact only when fair live simulation
requires it and the in-world method can establish it. Never use First
Establishment to excuse impossible knowledge, arithmetic errors, retroactive
precision, hidden-interface leakage, or post-hoc counters.

Keep corrections narrow unless the user explicitly generalizes them. Record
what changed, why, what remains preserved, and the affected projections.

## Refusal boundary

Do not resume gameplay without a valid bound Campaign and explicit gameplay
authorization. Do not embed Campaign state in this Skill. Do not mutate a
production Campaign during engine development; use synthetic fixtures or an
explicit disposable copy.
