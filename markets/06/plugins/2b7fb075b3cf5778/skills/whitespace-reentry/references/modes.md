# Reentry Modes

Read only the mode or artifact template needed for the current request.

## Resume

Recover:

- intended outcome and why it mattered;
- last known stopping point and reason work stopped;
- decisions, constraints, and approaches already ruled out;
- current state and material changes since the stopping point;
- one reversible next action and how completion will be verified.

Do not turn every open task into a new priority list. Keep only what changes the next move.

## Decision trace

Capture:

- the decision and when it was made;
- alternatives considered or rejected;
- evidence, constraints, and assumptions that supported it;
- dissent, uncertainty, or missing evidence;
- what has changed since then;
- verdict: `still holds`, `needs review`, or `superseded`, with evidence.

If no direct rationale exists, label the reconstruction as inferred.

## Handoff

Make the next actor operational quickly:

- outcome and definition of done;
- current working state;
- known-good paths, commands, artifacts, or contacts;
- decisions and constraints that must be preserved;
- blockers, risks, dependencies, and ownership;
- exact next action and expected receipt.

Do not hide uncertainty to make the handoff sound polished.

## Drift check

Treat the supplied plan, handoff, status note, or prior summary as a baseline, not truth. Compare it with current evidence and report:

- **Matches** — claims still supported;
- **Drifted** — claims contradicted or outdated;
- **Unresolved** — claims that cannot be checked;
- **Consequence** — what the drift changes about the next move.

Separate source, build, deployment, reachability, and visible runtime when they differ.

## Possibility compression

Reduce many demands into no more than three paths. Useful defaults are:

- **Continue** — preserve the current direction;
- **Simplify** — reduce scope or remove a dependency;
- **Change direction** — choose a different approach.

For each path, state the outcome, evidence, main tradeoff, reversibility, and first step. Recommend one when evidence supports it, but do not silently choose for the user.

## Reentry Capsule

Use this portable Markdown shape when the user asks to save or share the result:

```markdown
# Reentry Capsule: <title>

- Generated: <absolute date and time>
- Scope: <bounded project, task, or decision>
- Evidence window: <time range or sources checked>

## The thread
<intended outcome and why it matters>

## State now
<current observed and reported state; include important drift>

## Decisions and constraints
<what must be preserved, with rationale or uncertainty>

## Open loops
<only items that affect continuation>

## Next move
<one reversible action and its expected completion evidence>

## Evidence
- <source and freshness>

## Confidence
<confirmed, reported, inferred, stale, and unknown items>
```

Keep the capsule self-contained, but link to large evidence rather than copying it.
