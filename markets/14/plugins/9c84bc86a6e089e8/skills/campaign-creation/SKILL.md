---
name: campaign-creation
description: Build a draft outbound campaign in Alta end to end — audience, pitch, workflow, rep, launch. Use whenever the user wants to create, draft, set up, or modify an Alta campaign, and follow it before calling any campaign tool. Requires the Alta MCP server.
---

# Campaign creation (draft) skill

## Role

You orchestrate Alta's outbound **draft** campaign creation using the chat tools below. The flow has exactly **three pauses** — between pauses, you batch persist + next-build calls in a single assistant turn so the user gets to the next decision point immediately. You only have the user's messages — if required details are missing, infer reasonable defaults only where the user is silent, prefer conservative choices over blocking forever, and when the user contradicts themselves, favor the latest intent.

## Follow-ups (ask before each pause, not between batched calls)

Ask **short, concrete follow-up questions** only for inputs needed by the **next** pause-anchor tool — never for tools inside a batch, and never for inputs you can infer.

- Before **Pause 1**: if the user wants search/ICP targeting and you need filters, geography, or ICP detail, ask before `search_prospects`.
- **Inside the Pause 1 batch — DO NOT ask.** Infer `campaignName` (from the audience description) and `pitchBrief` (a one-or-two-sentence framing from the audience + conversation). The backend enriches `build_campaign_pitch` from the account's Compass (company URL, product copy, value props) and the campaign name, so a short brief is enough. Asking the user "what's your campaign name?" or "what's your pitch?" between Pause 1 and Pause 2 is wrong — the user reacts to the generated pitch in Pause 2 instead.
- **Inside the Pause 2 batch — DO NOT ask.** Infer `channels` (default to both `email` and `linkedin` unless the user explicitly named a single channel) and `instructions` (synthesize from the approved pitch's tone, top value prop, and CTA, plus the audience). Asking the user "what channels?" or "what tone?" between Pause 2 and Pause 3 is wrong — they react to the generated workflow in Pause 3. The persist (`update_campaign({ workflow })`) is also part of this batch — fire it immediately after `preview_campaign_workflow` in the same turn.
- Before closing **Pause 3**'s batch: if the user did not name a rep and did not say skip, ask who should send (or confirm skip) before `match_campaign_rep`.

When you still need information, **ask first**, then call tools — do not guess launch-critical choices without user confirmation unless you can infer them from context (audience, prior messages, or backend enrichment).

### How to ask

Ask in plain chat — short, concrete questions, one or two sentences. When the answer is one of a small set of discrete choices (e.g. confirming a pitch, picking a tone, selecting channels), phrase the options inline so the user can reply with a word or two (e.g. "Use this pitch, try a different tone, or switch the angle?"). The exact options for each pause are specified in the Pause sections below. This is about **how** you ask when asking is permitted; it does **not** override the "DO NOT ask" rules inside the Pause 1 / Pause 2 batches.

## Canonical pipeline — three pauses, batch in between

Stop only at these three pauses. Everything else flows in the same turn.

### Pause 1 — Audience

After `search_prospects` returns, ask the user in chat: "Start a campaign with this audience, refine the search, or try a different audience?". If they want to refine or switch audiences, ask a short follow-up for the new filters and call `search_prospects` again. If they want to start, run all three in a single turn — **infer the campaign name and pitch brief yourself; do not ask the user**:

1. `create_draft_campaign` — pick a `campaignName` from the audience description (e.g. "VPs of Sales — SaaS outreach"). Pass `prospectsCount` (the `total` from the prior `search_prospects` call) and a short `description` you write yourself summarizing why this audience is a strong fit — **1–2 sentences, max 250 characters**. Use the returned `campaignId` for the next two calls. The tool result includes `campaignUrl` — render it as a clickable markdown link (`[Open campaign in Alta](<url>)`) prominently in your reply; do not invent or reformat the URL.
2. `update_campaign` — `{ campaignId, targetAudience: { prospectSourceType: "datasets_people", searchCriteria: <the searchCriteria search_prospects returned> } }`. To run the campaign over an existing audience instead of a live search — one the user named, or one you just filled with `create_audience` + `update_audience` — pass `{ campaignId, targetAudience: { prospectSourceType: "list", audienceListId: <the audience id> } }` instead. Pick one shape, never both.
3. `build_campaign_pitch` — `{ campaignId, pitchBrief }`. Pass a one-or-two-sentence `pitchBrief` you wrote yourself from the audience + conversation. **Unless the user explicitly gave pitch direction** (e.g. "focus on X", "mention cost savings", "highlight our compliance angle") — in which case use their words verbatim in the brief. The backend enriches the pitch from the account's Compass (company URL, product copy, case studies, value props) — a brief framing is enough. Do not ask the user for pitch details; they react in Pause 2.

### Pause 2 — Pitch

After `build_campaign_pitch` returns, ask the user in chat: "Use this pitch, try a different tone, or change the angle?". If they want a different tone or angle, call `build_campaign_pitch` again with an updated `pitchBrief` reflecting their direction — do not persist the rejected version. If they approve, run all three in a single turn — **infer channels and instructions yourself; do not ask the user**:

1. `update_campaign` — `{ campaignId, pitch: <pitch payload from build_campaign_pitch> }`.
2. `preview_campaign_workflow` — `{ campaignId, instructions, channels }` — assembles the agentic workflow (and, where supported, streams a live preview). **It does NOT persist the workflow.** **Unless the user explicitly gave workflow direction** (e.g. specific tone, sequences to avoid, channel preferences) — in which case use their words verbatim. Default `channels` to both `email` and `linkedin` unless the user explicitly named one. Synthesize `instructions` from the approved pitch's tone, top value prop, and CTA + the audience description.
3. `update_campaign` — `{ campaignId, workflow: <the workflow object verbatim from the preview_campaign_workflow tool result> }`. **Pass the workflow exactly as returned — copy `agenticSettings.context` character-for-character; do not reformulate, summarize, or "clean up" the prose.** This persist must happen in the same turn as `preview_campaign_workflow`, before stopping for the user.

Then stop and wait for the user to react in Pause 3.

### Pause 3 — Workflow

After the Pause 2 batch completes (`preview_campaign_workflow` + immediate persist), ask the user in chat: "Launch this workflow, change the channels, or change the instructions?". If they want to change channels or instructions, run another Pause 2-style batch — call `preview_campaign_workflow` with the new args, then `update_campaign({ workflow })` immediately with the new workflow, then pause again. If they want to launch, run these in a single turn (no extra `update_campaign` for the workflow — already persisted in Pause 2 batch):

1. If the user named a rep: `match_campaign_rep`, then `update_campaign` with `{ campaignId, repIds }`. Skip otherwise.
2. `open_draft_campaign_in_alta` — `{ campaignId }`.

The flow at a glance: **audience pause → pitch pause → workflow pause → launch**. When the user explicitly skips a step (e.g. no search audience, no rep), drop that bullet from the relevant batch but keep the rest of the order.

## Audience from a CRM list

When the user wants the campaign to run on a list from their CRM (HubSpot, Pipedrive, Zoho, Dynamics, Attio…), build an audience from it instead of a search at Pause 1:

1. `list_crm_lists` with no source — the connected CRMs that have lists, each with a `people` source and a `companies` source. If none is connected, tell the user to connect their CRM in Alta. If several are, ask which one unless the user named it.
2. `list_crm_lists` with the source — the people source for a list of contacts or leads, the companies source for a list of companies — and `search` set to the list name the user gave. If more than one list matches, ask which one.
3. `create_audience` — name it after the list; `entityType: "person"` for a people list, `"company"` for a companies list.
4. `update_audience` — `{ audienceListId, crmList: { sourceType, entityType, externalListId, mapping: null, method, syncBatchSize }, filters: null, companyAudienceListId: null, amount: null }`. `method: "manual"` (the default) copies the list's records now. Use `"dynamic"` only for a people source whose `supportsDailySync` is true, when the user wants people who join the list later to keep coming in — it syncs daily. Leave `mapping` null; only when the import rejects the mapping, or the user wants a specific CRM field to fill an Alta field, call `get_crm_fields` and pass its adjusted `suggestedMapping`.
5. Companies list only — the campaign needs people, not companies: `create_audience` a people audience, then `update_audience` — `{ audienceListId: <the people audience>, companyAudienceListId: <the companies audience>, filters: <the roles to reach, optional>, peoplePerCompany, amount }`. If the user didn't say whom to reach at each company, ask before importing.
6. `update_campaign` — `{ campaignId, targetAudience: { prospectSourceType: "list", audienceListId: <the people audience> } }`, on a draft campaign. To show the user who is in it first, use `list_audience_people`.

To pause, resume or resize a daily sync later: `get_audience` shows each source's `sync` (null for a one-time import); then `update_audience` — `{ audienceListId, sourceSync: { audienceListSourceId, status: "paused" | "active" | null, batchSize: <or null> } }`. Pausing stops new records from coming in.

## Run mode, sending schedule and settings

Works outside the three-pause flow too, including on a new draft. When `get_campaign` returns `settings: null` (and `runMode: null`), the first `update_campaign` with `runMode` or `settings` creates the settings from the campaign builder's defaults in `copilot` mode, with your changes applied — tell the user it runs in copilot unless they asked for autoPilot. If it returns `schedule: null`, don't send `schedule` — point the user to the campaign builder to set the sending schedule up.

- **Read** them with `get_campaign` — the result has `runMode` (`copilot` or `autoPilot`) and `schedule`. Describe the schedule in plain words (e.g. "Mon–Fri, 9:00–17:00 Europe/London"), not raw minutes or bit strings.
- **Change** them with `update_campaign({ campaignId, runMode })` and/or `update_campaign({ campaignId, schedule })`. Send only the schedule fields that change — the rest keep their current values.
- **Settings page fields** (reply assistant, daily prospects quota, deduplication, unsubscribe and tracking, enrichment, message quality) come back from `get_campaign` under `settings`. Change them with `update_campaign({ campaignId, settings })`, sending only the fields that change. To attach a reply assistant set `settings.replyAgentId`, and `settings.replyAgentAutomatic` to choose between sending its replies automatically and saving them as drafts; `replyAgentId: null` detaches it.
- Switching to `autoPilot` means future messages go out without review — say so when the user asks for it.
- A schedule change applies to messages scheduled from now on; don't promise that messages already queued will move.

## Rules

- **Three pauses, no more, no less.** Stop only after `search_prospects`, `build_campaign_pitch`, and `preview_campaign_workflow`. Within a batch, fire persist + next-build calls together in the same assistant turn — do not narrate "I'm now persisting…" between them.
- **Reuse `campaignId`** from `create_draft_campaign` for every later tool call.
- **`update_campaign` persists pitch, audience, reps, and workflow.** `preview_campaign_workflow` only assembles the workflow — it never writes to the campaign. The Pause 2 batch must end with `update_campaign({ workflow })` immediately after `preview_campaign_workflow`, in the same turn. `build_campaign_pitch` and `match_campaign_rep` assemble data only — they never write to the campaign on their own.
- **Agentic workflows only.** `update_campaign({ workflow })` only accepts the agentic workflow returned by `preview_campaign_workflow` — never build or send workflow steps yourself. If the campaign already has a step-based workflow (touch points), do not replace it; tell the user to edit those steps in the campaign builder.
- **Search source vs audience source.** `datasets_people` keeps searching as the campaign runs, so it fits an open-ended audience; `list` runs over exactly the people in that audience and nothing else, so it fits a list the user reviewed. An audience can only be set while the campaign is still a draft, and it must already hold people — import into it before pointing the campaign at it.
- **Order matters.** Never auto-chain across a UI render: `search_prospects` → `build_campaign_pitch` (without the audience pause) is wrong. `preview_campaign_workflow` → `open_draft_campaign_in_alta` (without the workflow pause) is wrong.
- **`open_draft_campaign_in_alta` is the closer.** Only call it inside the Pause 3 batch, after pitch and workflow are persisted (and rep when the user named one). Never call it earlier.
- **Drive every transition through chat.** After each pause-anchor tool, ask the user in plain chat with the inline options listed for that pause and **wait for their explicit confirmation** before running the next batch. Don't restate the tool's output — assume the user has already seen what the tool returned; keep replies to one or two sentences.
- **Re-run the build tool to change anything.** If the user wants different pitch angles, tone, or different channels, call `build_campaign_pitch` (without persisting the rejected pitch) or `preview_campaign_workflow` (re-assembles the workflow only) with updated arguments — and follow each workflow re-run with `update_campaign({ workflow })` in the same turn to persist the new version.
- **Execute what the user asked in this turn** even if the full campaign isn't complete yet, and never block a requested step because later steps are missing.
