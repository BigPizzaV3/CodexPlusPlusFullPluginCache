# Phase workflow

Use the server's guidance as the authority for phase status. A tracker is orientation only.

## Frame

Capture the smallest decision basis that lets the team work:

- side: buying, selling or advising;
- subject and decision objective;
- market, category, horizon and scope that matter;
- success measures, constraints and material unknowns; and
- lead person when known.

State working assumptions that allow progress. Ask only for missing facts that materially change the decision. `start_sponsorship_situation` and Frame saves create drafts. Confirmation requires decision rights and the exact preview flow.

If Frame changes after confirmation, reload the situation. Dependent evaluation may become `attention` and require reconfirmation. Preserve the earlier version and explain which evidence or output basis is affected.

## Evaluate

Begin with the decision, not a catalogue of available analyses. Use the smallest combination that resolves it:

- governed sponsorship evidence for cohorts, relationships, categories and price context;
- transparent valuation for documented packages or explicit scenarios; and
- saved or newly researched public evidence for current facts and decisive gaps.

Keep these meanings separate:

- a confirmed relationship confirms the relationship, not its current availability;
- an asking price is a seller position, not a paid fee;
- an estimate is model output, not an observed transaction;
- a scenario is conditional on its stated inputs; and
- absence from the snapshot means unrecorded, not open or available.

Save evaluation findings with provenance and current basis versions only after the exact Frame is confirmed. The agent may still calculate, research or draft exploratory work before confirmation, but it remains in the conversation and cannot be saved as a governed evaluation or decision basis. Any jump to later work stays provisional while an earlier phase is unconfirmed.

## Prepare

Prepare the commercial move the user asked for: recommendation, shortlist, package, budget, proposal assessment or negotiation position. Tie each material claim to current evidence or label it as an assumption or agent judgment.

When numbers matter, keep cost evidence, modelled rights value and activation assumptions distinct. Save reversible preparation metadata with `change.action: output_reference`; a draft may have no external file reference, but it still needs its owner, audience, summary, current Frame basis, evidence basis and material unknowns. A draft file or card does not finalize the output or commercial decision.

## Review

Record the actual outcome without inventing performance. Separate agreed commercial facts, observed delivery or result facts, interpretation and unresolved follow-up. Propose reusable lessons only from the confirmed terminal Review.

Closing and reopening use an exact preview and authorized confirmation. If the outcome is not yet terminal, save `change.action: review_draft` with `outcome: pending`, the observed facts, uncertainty and next actions, then continue the situation.

## Phase states

- `done`: confirmed in the authoritative record.
- `active`: current phase.
- `attention`: previously confirmed but needs renewed review.
- `upcoming`: not confirmed and not current.

Render all four states using the supplied projection. Never derive them from array position, card text or conversation history.
