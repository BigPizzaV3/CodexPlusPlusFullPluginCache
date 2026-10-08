# AI-DM Engine / Campaign Contract v1.1 — Recovered Deployment Copy

Status: production-target architecture for plugin work  
Version: 1.1

## Ownership

The Engine is reusable immutable software.

The Campaign owns mutable state, current canon, books, Story So Far, Runtime
Primer, current resume and checkpoints.

The Plugin/Skill is an adapter. It must not contain mutable campaign state.

## Required Campaign package

```text
CAMPAIGN_PACKAGE/
├── CAMPAIGN_MANIFEST.json
├── campaign.sqlite
├── AI_DM_RUNTIME_PRIMER.md
├── STORY_SO_FAR.md
├── books/
├── checkpoints/
└── migrations/
```

`CAMPAIGN_MANIFEST.json` is the only current-authority locator.

Never infer current authority from filenames such as CURRENT, MASTER, FINAL,
COMPLETE, newest-modified or semantic similarity.

## Manifest/current-head invariant

The manifest, current database `state_head`, latest committed transaction and
all current projections must agree on:

- current state head;
- current transaction hash.

A turn is not committed if any one remains on the prior head.

## Transaction chain

Every campaign begins with one committed `GENESIS` transaction.

Every later substantive turn records:

- transaction_id;
- stable unique turn_id;
- exact player declaration;
- prior state head;
- resulting state head;
- previous transaction hash;
- transaction hash;
- phase before/after;
- campaign time before/after;
- domain delta;
- validation receipt;
- source/retrieval references;
- committed status.

### Idempotency

`turn_id` is unique.

Reprocessing the same committed `turn_id` with the same declaration:

- does not spend resources twice;
- does not advance time twice;
- does not create a new state head;
- returns the existing transaction.

The same `turn_id` with different declaration text is an error.

## Atomic commit

One atomic database transaction must:

1. verify expected prior head;
2. verify previous transaction hash;
3. validate proposed deltas;
4. mutate affected campaign-domain rows;
5. insert transaction;
6. update state head;
7. rebuild affected projections;
8. verify every current projection uses the resulting head;
9. commit.

Failure rolls the entire operation back.

The external manifest is then atomically rewritten to the same head/hash.

## Genesis

Genesis is transaction zero:

- turn_id: `GENESIS`;
- prior head: `GENESIS_ZERO`;
- previous transaction hash: 64 zeroes;
- resulting head: Genesis state head;
- delta: full accepted Genesis-current-state establishment.

## Provenance

Material current values distinguish:

- EXACT
- DERIVED
- GENERATED_CANON
- NORMALIZED
- BOUNDED
- FUTURE_UNKNOWN
- SEALED
- NOT_TRACKED

## First Establishment

When no prior value exists and fair live simulation genuinely requires it, the
DM may generate the fact logically before resolving any dependent outcome.

First Establishment cannot legitimize:

- impossible NPC knowledge;
- arithmetic errors;
- retrospective historical precision;
- interface leakage;
- post-hoc hidden counters chosen to defeat the player.

## Player sovereignty

Only the player chooses the player character's voluntary:

- actions;
- dialogue;
- tactics;
- power use;
- beliefs;
- conclusions;
- emotions;
- priorities;
- allocations;
- acceptance/rejection of relationships and bargains.

## Sealed state

Sealed Campaign data may be used internally for fair adjudication.

It must not leak through visible narration, commands, Story So Far or ordinary
retrieval.

## Checkpoints

Checkpoints are recovery artifacts, not competing current authorities.

Creating a checkpoint does not advance gameplay state head or transaction hash.

## Plugin classification

The plugin result must be classified honestly as one of:

1. FULL PASS — Skill + executable/storage path can durably operate Contract 1.1.
2. READ/ADJUDICATE PASS, WRITE LIMITATION — runtime works but persistence needs
   explicit file handoff or another storage layer.
3. SKILL-ONLY PASS — instructions/references work but executable Campaign
   operations do not.
4. FAIL — authored Skill cannot actually install/invoke.
