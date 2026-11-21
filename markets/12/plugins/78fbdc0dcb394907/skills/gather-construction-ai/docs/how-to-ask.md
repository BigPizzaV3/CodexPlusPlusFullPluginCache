# How to Ask

Three roles, three prompts each, cheapest-first. See [model-and-cost.md](model-and-cost.md)
for why these are cheap and how to make your own runs cheaper.

## Site QS

1. *"Duplicate allocations on Elm Street for last week"* — scoped dates, one skill
   (`data-quality`), no agent.
2. *"Pull the cached progress report for Elm Street, this period"* — hits `getCachedReport`
   directly instead of rebuilding it from raw shift records.
3. *"Red team this compensation event before I send it"* — this one is worth the cost: it runs
   the top model on purpose (see the model table below).

## Commercial manager

1. *"CVR for the project, this month vs last"* — a bounded date range, one skill.
2. *"Time-bar sweep, last 14 days"* — narrow window, not "check everything since the contract
   started".
3. *"Final account position — agreed vs unagreed, cached figures only"* — reuses this period's
   cached reports rather than re-fetching every shift record behind them.

## Planner

1. *"Compare Revision 4 against Revision 3 — what moved?"* — a diff between two already-imported
   programmes, no agent needed.
2. *"Is our Accepted Programme compliant?"* — single skill (Programme Advisor), scoped to the
   current revision.
3. *"What if the steel delivery slips three weeks?"* — a what-if on the imported programme; ask
   for one scenario at a time rather than "model every possible delay".

## What makes a run expensive

- An unscoped date range ("since the project started" instead of "last two weeks").
- Asking for an agent when one skill would answer it — an agent chains several skills and
  costs accordingly.
- Re-deriving a report the platform already caches, instead of asking for the cached one.
- Asking for every contract branch's guidance "just in case" instead of naming the contract
  form up front.
- Running Red Team or a full Bid Advisor review on a draft that's still changing — save it for
  the version you're about to send.

## Which model to pick

- A single skill runs on whatever model you're already using — there's no reason to switch up
  for it.
- An agent runs on the model set in its own frontmatter — you don't choose per call.
- Reserve the top model for adversarial or entitlement judgement: Red Team and the
  time-and-claims advisor. Everything else is tuned to run well on a mid-tier model.
