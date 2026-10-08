---
name: selenium-route-search
description: Plan chemical syntheses via the B12 Selenium route-search API. Use when asked to find synthetic routes / retrosynthesis for a molecule, assess whether a target is makeable, or compare disconnection strategies. Submits a target (SMILES), polls the async job, and returns ranked route families with feasibility and commercial-availability data.
---

# Selenium Route Search

Plan retrosynthetic routes for a target molecule through B12's Selenium API.
The API is **asynchronous**: you submit a target, it runs for minutes to hours,
and you poll for results. Route families come back ranked, with per-reaction
feasibility bands and commercial-leaf data.

## Prerequisites

Either the hosted MCP server is registered (tools
`quote_synthesis_assessment`, `start_synthesis_assessment`,
`submit_synthesis_campaign`, `get_synthesis_assessment`, and the route-family
read tools), **or** call the REST API directly with `SELENIUM_API_URL` plus a
bearer key. Prefer the hosted MCP tools when present.

## Core workflow

1. **Quote once.** Call `quote_synthesis_assessment` with the SMILES, optional
   `instructions`, and tier. An explicit request to run or assess the target is
   authorization to proceed at the requested/default tier; do not ask for a
   second conversational confirmation. Ask only when intent is ambiguous, the
   quote exceeds a user-stated budget. If credits are insufficient, explain the
   limit and stop the paid operation. The host's
   billable tool approval remains the final approval boundary.
2. **Start once.** Call `start_synthesis_assessment` with the returned quote id,
   exact credit amount, and stable campaign/candidate references. Retrying the
   same quote returns the original assessment without another debit.
3. **For two to 100 candidates, batch once.** Call
   `submit_synthesis_campaign` instead of fanning out quotes and starts.
   Generate `request_reference` internally, reuse it unchanged for retries,
   and never ask the user to invent it. Set `max_total_credits` only when the
   user states a budget; the server validates, prices, and queues the batch.
4. **Own progress checks.** Follow the monitoring guidance below; do not make
   the user repeatedly ask for status. Recover batches with
   `list_synthesis_assessments(campaign_reference=..., include_summaries=false)`.
5. **Read progressively.** Start with the compact terminal assessment, list
   route families, then open only the selected family that needs full detail.
5. **Interpret the terminal state:**
   - `completed` — all requested families solved.
   - `partial` — some families solved (others incomplete or the job timed out);
     the solved families are still valid results. This is common and useful.
   - `failed` — no charge (auto-refunded). Report briefly and use the same safe
     retry handle if the original request still applies; do not ask the user to
     reconfirm an idempotent retry.
   - `cancelled` — stopped on request.

## Choosing a tier

Scout is deliberately narrower than the portfolio tiers. Basic, Standard, and
Exhaustive use the same chemistry stack with increasing breadth/depth.

- **scout** — one bounded fast-lane direction (10 credits): one research pass,
  one family, one target route, no research follow-up. Use for high-volume
  triage. It may return one developed route hypothesis but does not guarantee
  latency, literature evidence, or a solved route.
- **basic** — "is there a route?" One research pass, up to 3 families. Cheapest;
  use when a Scout direction is insufficient.
- **standard** — "what are my options?" Ranked strategic alternatives. The default.
- **exhaustive** — "have we covered the space?" For a high-value target you're
  about to commit real lab time to.

Escalate promising targets from scout → basic → standard/exhaustive when the
user zeroes in on the molecules they care about.

## Reading the output

Each result has `families[]`. A solved family has a `best_route` with:
- `molecules[]` — target, intermediates, starting materials (with
  `commercially_available` where known).
- `reactions[]` — each with a human-readable `label`, `reaction_smiles`, and an
  `assessment.band` (`likely_feasible` / `uncertain` / `high_risk`).
- `scores` — `judge_combined_score` (0–100, the primary ranking) and a route
  `feasibility_band`. Rank and present routes by the judge score, not by raw
  feasibility (feasibility is noisier).
- `stats` — `reaction_count`, `longest_linear_sequence`, `commercially_solved`.

Incomplete families are returned as stubs (name + strategy summary, no route) —
mention them as explored-but-unsolved so coverage is clear.

## Guardrails

- **Cost is real.** Every submit debits credits; `partial` still charges (compute
  was spent), `failed` does not. Quote before runs, but mention price/balance
  once rather than narrating every billing check.
- **Never retry with a new quote or campaign request reference** — reuse the
  durable handle so the server deduplicates the billable work.
- **Respect caps.** `outstanding_job_limit_exceeded` /
  `submission_rate_limit_exceeded` (429) mean wait or cancel a job, not retry
  immediately. The execution limit itself queues internally.
- **Bulk/agentic runs**: use one `submit_synthesis_campaign` call for up to 100
  targets. Keep its generated campaign reference and recover the set through
  the existing assessment-list tool; do not issue 100 independent starts.
- **Don't surface internal identifiers** to the end user — present molecule
  names, reaction labels, and feasibility bands, not opaque ids or raw scores.

## Existing account access and purchases

The plugin uses the connected organization's existing credits. It does not sell
credits or subscriptions. If credits or permissions are insufficient, explain
the limit without promoting an upgrade, asking the user to buy credits, or
linking to checkout or a page that initiates a purchase. Do not invoke web
checkout endpoints through the REST fallback. Users may still inspect existing
results with their granted permissions. Keep result links focused on the
requested assessment or planning job.

## Error handling

Public errors carry `detail.code` + `detail.request_id`. Actionable ones:
`insufficient_credits` (402, explain the available balance and stop the paid operation), `invalid_smiles` / `unsupported_molecule` /
`molecule_too_large` (422, fix the input), `route_search_not_found` (404).
Include `request_id` and the `job_id` in any support report.

See `reference.md` for the exact REST calls, and `agent_loop.py` for a runnable
submit→poll→read example.


## Standalone research and selected-strategy development

When the hosted server lists the planning tools, choose by intent:
- Competing synthesis strategies or focused literature research: use
  `quote_synthesis_research`. SR stops at a persisted research report; it does not
  launch RouteDev. Do not also start a full assessment.
- Develop the user's specific strategy: use `quote_route_development` with the
  exact target and `strategy.kind=user_strategy`, preserving their detailed proposal.
- Develop one SR strategy: pass `strategy.kind=saved_strategy`, its `strategy_id`,
  and the SR job's `receipt.result` artifact reference as `strategy.source`.
- Paper-based route: use the bundled `selenium-paper-to-route` skill. Read and
  describe the paper on the host; pass the detailed proposal and target to RouteDev.

Both quote tools are free. Start with `start_synthesis_planning` using the exact
quoted credits and honoring the user's budget and host approval. Reuse the same
quote for retries. Poll `get_synthesis_planning` at the returned interval; recover
jobs across chats with `list_synthesis_planning`. Inspect full report/route with
`get_synthesis_planning_artifact`; cancel with `cancel_synthesis_planning`.
Keep IDs internal. Research findings are hypotheses or cited precedent, not
validated routes. Report partial development and deviations honestly. If planning
tools are absent, explain that the server has not enabled them; never silently
substitute a paid full assessment.

## Monitoring and presenting results

After admission, briefly state that work is queued/running and provide
`session_url` as **Open in Selenium** when the server returns it. Use only a
server-returned link; never invent a UI hostname or substitute a job ID for a
session ID. If no link is returned, say that this server has not provided one.

Own monitoring of the existing job. While the turn is active, use the host's
wait/sleep tool and honor `next_check_at` or `retry_after_seconds` before the next
status call. Give updates on meaningful stage changes, not every poll.

If the user wants background updates (including a request to run and notify),
and the host supports scheduled follow-ups, create one using the host's native
scheduler. Follow that host's authorization rules. Store the existing job ID,
operation, appropriate status tool, and returned minimum polling interval in the
follow-up prompt. Use an interval no shorter than that minimum or the scheduler's
supported minimum. The follow-up only reads that job: no new quotes, starts,
cancellations, or paid retries. Stay quiet while unchanged. On completed, partial,
failed, or cancelled, notify once with a brief result and returned session link,
then disable the follow-up. A timer notification alone does not check job status.

Only claim background monitoring after the scheduler confirms creation. If the
host lacks scheduling, explain the limitation once and give the session link for
inspection; do not promise to wake up after ending the turn. Do not use shell
background processes or cron as a substitute for a supported host scheduler.

For final RouteDev results, lead with **Open in Selenium**, a short outcome, and
key uncertainties/deviations. Retrieve artifacts when needed to substantiate the
summary, but do not dump the route JSON or draw a graph unless requested. For SR,
summarize the research report; a session link does not imply a developed route.
