---
name: what-did-we-decide
description: What did we decide? Use when the user asks what was decided, agreed or promised on a project and why, or wants the evidence behind a decision.
---

# What did we decide?

## 1. Search wide, then narrow

1. `delegent_get_context_for_task` with the question and the workstream if known. Decisions from the Overview and meeting captures rank high.
2. `delegent_get_status` for the Overview's decisions log.
3. `delegent_search_past_chats` if the user says it came up in an earlier Delegent chat.
4. `delegent_find_emails` for the email where it was confirmed.

## 2. Verify

Open each candidate with `delegent_get_source`. Prefer raw meeting transcripts and emails over summaries. Check dates: a later source can reverse an earlier decision.

## 3. Answer

- **The decision**, in one sentence, with date and who made it.
- **Evidence**: 1–3 sources, each with a short exact quote.
- **Changes since**: anything that superseded or questioned it.
- **Gaps**: what is not recorded, e.g. "no written confirmation from the client".

If sources conflict, say so and show both. Never fill a gap with a plausible guess.

## 4. Offer to record it

If the decision was not logged, offer `delegent_propose_overview_update` (section decisions) or `delegent_capture_work` (kind decision), citing the sources.
