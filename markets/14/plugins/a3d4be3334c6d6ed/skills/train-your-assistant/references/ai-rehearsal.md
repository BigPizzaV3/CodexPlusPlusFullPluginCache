# Test answers without customer actions

<!-- ChatGPT Codex — CODEX-V2-007. Working V2 source. -->

The rehearsal uses the workspace's configured AI model with approved public
knowledge and fictional customer questions. It does not invoke the live agent
pipeline, current agent instructions, conversation memory or business tools.
No messages, calls, payments, contacts, bookings or automations can be executed.
Never present this rehearsal as end-to-end production or delivery verification.

1. Identify the business and read the approved draft revision. Resume saved tests
   with list_ai_rehearsals/get_ai_rehearsal before creating duplicates.
2. Prepare one to five fictional questions with prepare_ai_rehearsal. Cover price,
   unit/tax uncertainty, inclusions, package distinctions, missing facts or human
   handover. Use no real customer identifiers, secrets or payment details. Do not
   copy private floors into question text. Optional mustMention/mustNotMention
   criteria are checked locally and never sent to the model.
3. Select fewer offerings if the approved public context exceeds 20 KB. Do not
   silently truncate facts or prices. Preparation makes no provider calls.
4. Show the exact questions, source revision and usage notice. These use normal
   configured-provider AI usage/billing. Only after the owner approves, call
   run_ai_rehearsal with confirm true and the previewId. Source/draft/PDF approval
   is not permission to purchase test calls.
5. Run one question per call and continue an already approved plan only while
   queued. Stop on blocked/partial/uncertain outcomes. A queued approved plan can
   resume within its 24-hour lifetime; a never-started approval expires after
   30 minutes. To renew a pending receipt, re-prepare using the returned requestId,
   questions and offeringKeys while the source revision is still current.
6. Unknown interrupted calls are not automatically repeated: a request may have
   reached the provider even if no result was saved. Explain uncertainty and retain
   the saved record. A new attempt needs a fresh reviewed plan.
7. Show actual answers and flags. Local substring checks do not establish correct
   reasoning or factual accuracy. Only after the owner assesses an exact answer,
   call review_ai_rehearsal with its answerHash and pass/fail verdict. Never supply
   the owner's verdict yourself. Live-agent/delivery verification remains false.
8. Fix knowledge through the separate draft preview/approval/application flow and
   prepare a fresh rehearsal of the approved revision. Old results are marked stale
   when approved facts change. Do not silently treat them as tests of the new facts.

There are at most ten new plans and thirty attempt reservations per UTC day,
five questions per plan and twenty saved plans. Reservations survive deletion
of history and include blocked/uncertain attempts; they are not a claim that each
attempt was billed. Normal platform usage/spend gates apply as well. Two tests may
execute per API process and only one active lease per workspace is allowed.

Webhook/custom providers are refused because an arbitrary webhook could trigger
outside actions. A model-proposed function/tool call is recorded as blocked and
is never executed. Provider credentials and raw error details are not returned.
Resolve configuration blockers before preparing another plan; do not loop on them.

If these tools are unavailable, retain the original ChatGPT content rehearsal and
state that it did not run the configured Endelir model. Live channel/device testing,
current agent instructions, tools and production pipeline still need separate checks.
