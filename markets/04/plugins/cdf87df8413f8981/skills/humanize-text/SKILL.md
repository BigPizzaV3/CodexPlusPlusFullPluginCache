---
name: humanize-text
description: Use ReverseGPT to rewrite AI-generated drafts so they read naturally while preserving meaning, facts, and formatting. Trigger when a user asks to humanize, naturalize, or rewrite an AI-written draft with ReverseGPT.
---

# Humanize text

Use the ReverseGPT MCP tools as the sole humanizing provider for requests handled by this skill. Never rewrite the draft yourself and present it as ReverseGPT output, and never substitute another service or browsing workflow.

Read [references/tool-reference.md](references/tool-reference.md) before the first tool call when exact arguments, response fields, billing, or polling behavior matters.

## Workflow

1. Confirm the ReverseGPT MCP connection is available and authenticated. Surface authentication, scope, plan, or credit errors without exposing secrets.
2. Reject empty or whitespace-only input before making a tool call.
3. Preserve the user's draft exactly. Do not pre-edit, summarize, translate, normalize whitespace, or add instructions to the `text` value.
4. Count the complete draft before calling a tool. Credit-based plans use one credit per input word; Max includes humanization without debiting credits. For a draft of 500 words or more, state the input size and plan-dependent cost, then wait for confirmation unless the user already explicitly authorized processing that draft. Do not infer the account's plan when it is unknown.
5. Keep each `humanize_text` call at or below 1,000 words:
   - If the user requires a single call and forbids splitting, explain the limit and do not process an oversized draft. Offer splitting only as a separate option requiring the user's agreement.
   - Prefer paragraph boundaries and keep all separators so reassembly reproduces the original structure.
   - If one paragraph exceeds the limit, split at the nearest sentence or whitespace boundary without changing its text.
   - Process parts in their original order and reassemble the returned parts in that same order.
6. Pass `ultra: true` only when the user explicitly requests Ultra. Do not infer it from a request for higher quality.
7. Handle every response by its fields:
   - When `done` is `true` and `status` is `completed`, return `humanizedText`.
   - When `done` is `false`, retain `jobId` and poll `get_humanize_job` with that same ID until completion or failure. Never resubmit the original text merely because it is still pending or a call times out after returning a job ID.
   - If a connection fails before returning a job ID, explain that the run may have started. Do not automatically submit it again; a repeat may create another run and charge again.
   - When `status` is `failed`, explain that the failed run was not charged, retry the original part once, and surface the safe server error if that single retry also fails.
8. Report the response's actual input `wordCount` after completion. For a split draft, report each part and the total. Report `ultra: true` or `false` as returned; `null` means an older job did not record its mode, so do not guess. When asked to retrieve a result again, use `get_humanize_job` with the same ID even if it is already completed.

## Boundaries

- Do not promise or guarantee an AI-detector result. If the user makes rewriting conditional on a detector guarantee, explain the limitation and ask whether they want ordinary rewriting before making a paid call. A request only for a guarantee, detection, or proof of authorship does not require a humanization call.
- Do not claim the result proves human authorship. Authorship, disclosure, and appropriate use remain the writer's responsibility.
- Do not fabricate output, job state, credit usage, or an Ultra result.
- Do not expose OAuth tokens, API keys, internal request metadata, or reviewer credentials.
- Do not call a paid tool merely to explain ReverseGPT's capabilities.
- If ReverseGPT cannot complete the request, say so plainly. Do not switch providers unless the user starts a separate request for another service.
