# Credits, quotas & limits

Every billable Delpha call spends **credits** from a team balance. Both surfaces —
[REST](rest-api.md) and [MCP](mcp.md) — draw on the same balance.

## What a call costs

Each operation has its own price in credits, and the prices are live configuration that changes
without a code release — **never hardcode one**. Read the current table from the credential-free
`GET https://api.delpha.io/v1/pricing` (one row per operation) or from the console; ultimate parent
and legal ID are the most expensive operations. A batch of N records costs price × N.

The console is authoritative for what a call cost you. Check
**Settings → Usage** for what you have actually spent and **Settings → Billing** for the balance.

## How a charge is made

1. **Reserve at admission.** The submit call reserves the credits before any work starts. No balance
   → **`402`**, and nothing runs.
2. **Settle on completion.** The reservation is converted to a charge when the job finishes. A batch
   settles only the items that **succeeded** and refunds the rest.
3. **Release on failure.** A job that errors releases its reservation.

Consequences worth designing for:

- **`402` is not retryable.** Top up or wait for the window to roll; retrying the same call just
  fails again.
- **`get*Result` is free.** Polling a result never charges. Only submission does.
- **Retrying a submit costs again.** Submission is idempotent in the sense that it has no side
  effects and mints a fresh `job_id` — but each submission is a new job and a new charge. Retry on
  transport failures, not on a `400`.

## Free credits

Signing up at `https://app.delpha.ai` provisions a team with a free credit grant — enough to try
every capability before buying anything. Credits are consumed subscription first, then free, then
purchased.

## Per-key ceilings

An API key can carry its own credit ceiling over a `forever`, `day`, `week` or `month` window, set
when the key is created and editable afterwards. Exhausting it returns the **same `402`** as an
empty team balance, with a distinct error code. A key with no ceiling is unlimited within the team
balance.

Use this to bound a shared or embedded key — a runaway loop then stops at its own ceiling instead of
draining the team.

## Rate and size limits

- **Batch: 1–100 items per request** (`422` beyond). Chunk larger lists.
- **Keys expire.** TTL is 1–730 days, default 365. A present expired key is rejected with `403`;
  rotate it in the
  console rather than creating a second one.
- **A team can hold a bounded number of live keys**, and key creation is rate-limited. Revoke what
  you no longer use.

## Seeing where credits went

- **Settings → Usage** — spend over time.
- **Product → Resolutions** — one row per call, with the inputs and the outcome.
- **Developer → Logs** — the request-level view for debugging an integration.

## See also

- [rest-api.md](rest-api.md) · [mcp.md](mcp.md) · [security.md](security.md)
