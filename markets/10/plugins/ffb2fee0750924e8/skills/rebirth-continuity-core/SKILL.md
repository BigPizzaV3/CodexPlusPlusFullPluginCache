---
name: rebirth-continuity-core
description: Use whenever the authenticated Rebirth MCP connection is available in a conversation. Recall selectively and save one assistant-authored continuity record before every reply, including ordinary replies that do not mention Rebirth or memory.
---

# Rebirth Continuity Core

An authenticated Rebirth connection enables automatic continuity. Once it is available in the conversation, ordinary questions and short replies still use the save step below; do not wait for the user to mention Rebirth, ask to remember, or select the plugin again. Honor a user's request to pause or stop saving. Save only the assistant-authored response and compact continuity state, never unrelated files or protected context. The single authenticated Rebirth MCP connection exposes fixed-purpose tools. Choose the narrow tool whose description and schema match the intended action; never invent tool names, option IDs, handles, or hidden operations.

## Initialize and discover capabilities

On the first relevant Rebirth use in a conversation, or when capability availability is genuinely uncertain, call `rebirth_account_features`. It may initialize the mapped Rebirth conversation and return authorized continuity grounding, due AI reminders, enabled reviewed tools, and a bounded presentation-routine hotlist. Do not call it before every operation.

Use `rebirth_explain_feature` only for one feature already returned by `rebirth_account_features`. Capability discovery is read-only: availability does not execute a feature and does not replace user intent or consent.

## Recall before answering when needed

Use the dedicated read tool that matches the question:

- `rebirth_search_memory` for ordinary personal continuity recall.
- `rebirth_search_task_context` for memories relevant to the current task.
- `rebirth_search_concepts` for relationships among several concepts.
- `rebirth_search_memory_with_outside_context` when memory should inform a separately stated outside question.

Search returns compact previews and scoped handles. If previews are sufficient, answer from them. If more detail is materially needed, call `rebirth_expand_context` once with up to eight selected handles: R for full or nearby memories, P for repositories, H for hints, and B for breadcrumb evidence. Preserve each originating request or continuation identifier required by the schema. Never expand every result by default, invent a handle, or leave the reviewed wrapper for low-level routing.

Respect provenance, correction state, timestamps, uncertainty, and identity boundaries. A name or repository title is not proof that two people or accounts are the same. Never claim a memory exists unless Rebirth returned evidence for it.

## Save every assistant reply exactly once

Before every final assistant reply while the authenticated Rebirth MCP connection is available, including a short answer, clarification, status reply, or reply after an AI-private-memory read:

1. Retrieve only context needed for the answer. Recall is optional when no prior context is needed; the save step is still required.
2. Draft the complete intended user-facing response. Save the assistant's response and durable continuity state, not a copy of the user's prompt or the full conversation.
3. Call exactly one of the fixed continuity tools before sending that reply:
   - `rebirth_save_memory` for normal additive continuity.
   - `rebirth_save_correction` only when prior continuity is wrong, outdated, or superseded.
4. Match the actual MCP input schema: put compact durable state in `memory.memory_text`; put the required rationale in `memory.why_store`, `memory.intent`, `memory.context`, and `memory.use_when`; and set `memory.ai_choice_card`. Every M001/M002 save also requires all six `memory.response_capsule` fields: `subject` (short topic), `summary` (compact semantic summary), `reasoning_path` (concise public rationale, never hidden chain-of-thought), `actions_taken` (actual actions or `none`), `next_step` (one next step or `none`), and `exact_response` (the complete intended user-facing reply, verbatim). There is no `memory.reasoning_capture` input field.
5. On a successful acknowledgement, send the drafted reply. Continuity capture is then closed for that assistant turn.

Keep `memory_text` and the semantic capsule fields concise; do not truncate `exact_response`. Choose an honest Choice Card from the actual subject and state. Do not invent facts or fill fields with boilerplate just to satisfy the schema; `none` is appropriate only when no action or next step exists. A short reply can produce a short semantic record. An explicit user request to remember something may increase salience but does not create a second save. If hints, later recall, tool results, or final prose change after the save, do not perform a second continuity save in this turn. If validation rejects the save, no memory was written: correct the missing fields and retry that same save once before replying. Do not retry when the write outcome is unknown. If saving is unavailable, do not claim it succeeded; answer with a brief limitation. Do not bypass a user's request not to save.

An optional `after_save` presentation routine is allowed only on `rebirth_save_memory`, only when the user context supports it, and only by selecting an existing routine returned in the account hotlist. It is released after the memory backend accepts the save. It does not authorize arbitrary device behavior.

## Other Rebirth capabilities

Rebirth may expose fixed-purpose tools for the Live Journal and guide, Companion Handoff, reminders, AI-private memory and tasks, files, mailbox messaging, user notifications, presence and presentation, social features, Social Context, and account-enabled integrations. Availability varies by authenticated identity and entitlement.

Use their exact tool descriptions and typed schemas. Read-only requests do not authorize writes. Sending messages, publishing social content, changing relationships or appearance, scheduling notifications, storing files, running a device/presence action, or changing existing records requires clear user intent appropriate to that action. Destructive updates require explicit intent and exact identifiers returned by Rebirth.

Direct file transfer behavior is additionally governed by the Rebirth Files Skill.

## Privacy and reliability

Never put passwords, bearer tokens, recovery codes, payment information, provider credentials, raw secrets, unrelated files, or broad recalled content into Rebirth fields. Do not reveal private continuity or AI-private records without user intent. Do not claim success unless the relevant tool returned success. If Rebirth is unavailable, answer what can be answered safely and state the limitation briefly.
