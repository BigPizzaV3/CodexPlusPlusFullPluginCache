# ReverseGPT MCP tool reference

Production endpoint: `https://www.reversegpt.ai/api/mcp`

Transport: Streamable HTTP, stateless. The plugin uses OAuth 2.1 with PKCE S256 and dynamic client registration. The authorization server is `https://www.reversegpt.ai`; product scopes are `humanize:read humanize:write`.

ReverseGPT also supports `rg_live_…` API keys through `Authorization: Bearer` or `x-api-key`, but API keys are not part of this plugin package and must never be committed or echoed.

## Tools

### `humanize_text`

Rewrite a draft so it reads as natural human writing while preserving meaning, facts, and formatting.

| Input | Required | Type | Notes |
| --- | --- | --- | --- |
| `text` | Yes | string | Pass the user's draft verbatim. Maximum 1,000 words per call. |
| `ultra` | No | boolean | Request the Max-plan second pass only when the user asks for Ultra. It may be silently downgraded on another plan. |

Credit-based plans use one credit per input word; Max includes the run without debiting credits. A failed run is not charged. The server waits up to about ten seconds for completion, then returns the result or a pending job ID. Repeating the same `humanize_text` call starts a separate run and can spend credits again. If a connection fails before a job ID arrives, do not automatically resubmit.

### `get_humanize_job`

Read the status and result of an existing run, including one that already completed.

| Input | Required | Type | Notes |
| --- | --- | --- | --- |
| `jobId` | Yes | string | Reuse the exact ID returned by `humanize_text`. |

Polling is free. Keep polling the same job when `done` is `false`; do not resubmit the draft.

## Shared response envelope

Both tools return the following fields:

| Field | Meaning |
| --- | --- |
| `jobId` | Stable identifier for this run. |
| `status` | `pending`, `completed`, or `failed`. |
| `done` | Whether the run reached a terminal state. |
| `wordCount` | Input word count reported for billing and completion reporting. |
| `ultra` | Whether Ultra was enabled for this run. `null` means an older job did not record its mode; do not guess. |
| `humanizedText` | Completed rewritten text when available. |
| `wordsProcessed` | Completed output word count, or `null` before completion. |
| `chunkCount` | Server-side chunk count for the run. |
| `nextStep` | Server guidance for the current state, when provided. |

Branch on `done`, then `status`. A pending result must be polled with `get_humanize_job`. A completed result should contain the text to present. A failed result is not charged and may be retried once under the skill workflow.

## Tool annotations

| Tool | `readOnlyHint` | `openWorldHint` | `destructiveHint` | `idempotentHint` |
| --- | ---: | ---: | ---: | ---: |
| `humanize_text` | false | false | false | false |
| `get_humanize_job` | true | false | false | true |

`humanize_text` is neither read-only nor idempotent because it creates a job, can debit credits on credit-based plans, and a retry can start another run. It operates only on supplied text and private ReverseGPT job state, does not change public internet state, and destroys nothing. `get_humanize_job` is a free, side-effect-free read of an existing run.
