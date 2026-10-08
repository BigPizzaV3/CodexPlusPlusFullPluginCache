# Credit usage

## One pricing and billing authority

The Orbit API owns operation pricing, the credit ledger, and billing decisions
for the connected Orbit account or organization. ChatGPT is an adapter, not a
separate billing system. A ChatGPT subscription does not imply unlimited Orbit
usage.

- Read the [public pricing catalog](https://api.orbitsearch.com/v2/developer/pricing)
  for current operation rates and units. This is a public, read-only lookup;
  never ask for an API key or bypass app tools with authenticated REST calls.
- Use the [billing dashboard](https://developer.orbitsearch.com/dashboard/billing)
  for account-specific balances, purchases, and plan details.
- For the connected account's usage, call `get_credit_usage` and report the
  returned available/reserved credits, usage, request count, and period. Preserve
  the response's scope: connection-level usage is not necessarily the entire
  organization's usage. Do not infer missing totals.
- Do not copy fixed prices into this skill, invent dollar conversions, or assume
  signup credits, monthly resets, bonuses, or a particular remaining balance.
  State an allowance only when the current account or plan evidence confirms it.
- If the catalog cannot be read or an operation is missing, say its current
  price could not be verified. Do not substitute remembered or pending PR prices.

## What consumes credits

Use the deployed catalog and returned billing metadata as the authority. The
centralized billing model distinguishes these operations:

| Operation | How to explain usage |
| --- | --- |
| Cached search | Charged in blocks of unique cached profiles returned, rounded up using the catalog's block unit. An empty cached result set has no cached-result charge. Candidate Discovery results are excluded from that count. |
| Candidate Discovery | Charged for unique profiles returned. Generation within the same operation replaces the discovery tier rather than stacking discovery and generation fees. |
| Profile generation | Partial and full generation use their respective catalog rates. Full generation includes intermediate partial work. A later explicit upgrade is a new operation. A profile already at the requested depth does not incur a new generation fee unless regeneration is requested. |
| Explicit profile read | `get_profile` uses the profile-read rate, including for an already-generated profile. It retrieves existing data without generating, refreshing, or repairing it; request enrichment separately when needed. Search can embed identity fields, contact fields, and generated sections such as bio, jobs, and education; the complete profile includes image galleries and source links where available. |
| Watchers | Completed runs and updates use their respective catalog rates. Recurring activity can consume credits after the initial request; insufficient credits can pause a watcher. |

Do not infer that unlisted management actions are free. Generation depth,
profile reads, and discovery are different operations, not interchangeable
names for the same charge. Polling an existing operation does not repeatedly
charge already-settled results, but newly completed work can still settle.

For an estimate, use current rates and units with the requested scope. Label
unknown result counts as estimates, not a guaranteed total. Avoid opening every
search result automatically: read the profiles needed for the user's requested
answer, reusing sufficient profiles already read in the conversation. Do not
omit the full read needed to support substantive claims just to conceal its cost.
Confirm unclear bulk scope or recurring watcher activity before starting it;
do not add repetitive confirmation prompts to ordinary requested lookups.

## Insufficient credits and topping up

Treat HTTP 402 or `developer_api_credits_insufficient`, including an equivalent
error returned by an app tool, as a billing failure:

1. Stop additional paid work. Preserve any usable partial results and explain
   which requested work did not complete. Never represent the error as no
   matching people or claim the unfinished task succeeded.
2. Show `requiredCredits` and `remainingCredits` only if returned by the service.
   Otherwise explain that more credits are needed without guessing an amount.
3. Link to the [Orbit billing dashboard](https://developer.orbitsearch.com/dashboard/billing).
   Ask the user to use the same Orbit account connected to ChatGPT and, where
   applicable, the same organization. An organization billing administrator may
   need to help. Do not promise that signing into ChatGPT also signs them into
   the Orbit website, or claim a purchase happened before confirmation.
4. Do not automatically buy credits, switch billing accounts, loop retries,
   or silently replace the unfinished research with web search or memory.
5. After the user confirms credits are available, resume only the necessary
   unfinished work. For a paused watcher, inspect its state before offering to
   resume it; topping up alone is not proof it has restarted.

Example: "Orbit needs more credits to finish this search. You can add credits
in [Orbit billing](https://developer.orbitsearch.com/dashboard/billing) using
the Orbit account connected here. Then we can continue."

## Retries, holds, and partial work

Preserve existing resource IDs and any supported request/idempotency key when
retrying the same request with unchanged inputs. Use only fields exposed by
the app tool; do not invent an idempotency parameter. Check the existing search
or enrichment status after an ambiguous timeout instead of launching duplicate
paid work. A genuinely new operation is not a retry of an earlier one.

Async work may return partial results and per-result failures. Report these
accurately. Temporary reservations or holds are not settled consumption, and
releasing unused credits is not a purchase. Rely on API-reported balances and
settlement rather than computing a second ledger from tool calls. Distinguish
rate limits (HTTP 429) from insufficient credits (HTTP 402); do not recommend
topping up merely because a request was rate-limited.
