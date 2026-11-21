---
name: icanpreneur
description: 'Foundation for every task that uses the Icanpreneur tools: workspaces (called ideas), Canvas, customer segments, research, interviews, contacts, Buyer Personas, positioning, landing pages, sales decks, notes, exports and team access. Load it before the first Icanpreneur tool call in a conversation and before any billable or destructive call. Covers vocabulary, IDs, credits, waiting for generated work, retries, evidence rules and deletion.'
---

# Icanpreneur: how to use the tools

Icanpreneur helps founders, product teams, consultants and startup programs decide from customer evidence. Ground what you say in what is saved in the workspace, and be clear how strong that evidence is.

Load a workflow skill as well when the task matches:

| The user wants to                                                                           | Also load                                                                |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| A Buyer Persona's reaction to an offer, price, pitch or idea                                | [icanpreneur-persona-feedback](../icanpreneur-persona-feedback/SKILL.md) |
| Set up a workspace, segments, research or interviews; read findings                         | [icanpreneur-build-research](../icanpreneur-build-research/SKILL.md)     |
| Positioning, a landing page, a sales deck or a preview                                      | [icanpreneur-gtm-assets](../icanpreneur-gtm-assets/SKILL.md)             |
| Decide what to test or change; judge whether evidence supports something; update the Canvas | [icanpreneur-decide](../icanpreneur-decide/SKILL.md)                     |
| Review several startups together; prepare mentoring                                         | [icanpreneur-cohort-review](../icanpreneur-cohort-review/SKILL.md)       |

Notes, exports, team access and questions about saved work need only this skill. Use the user's words (workspace, Canvas, research, persona) and name a tool only when it helps. Some website terms map to the tools: IVA is Icanpreneur's assistant, "Validate customer problems" is `ProblemDiscoveryAndValidation` research, "Analyze won/lost deals" is `WinLoss`, "Understand buyer decisions" is `BuyerPersona`, "Talk with your persona" is `ask_buyer_persona`. Some website features have no tool: see [references/not-available.md](references/not-available.md).

## The rules that matter most

1. **Real versus simulated.** Synthetic interviews, synthetic contacts and persona answers are simulations. They give hypotheses, not validation, demand or traction. Always say how many sources are real, imported and synthetic.
2. **Show the source.** Every conclusion names its evidence: the insight or interview, whether it is real, imported or synthetic, and a count when the tool returns one. Leave missing quotes and counts missing. Quote only returned text, in the interview's language. Mark your interpretation as yours.
3. **Do what was asked.** Complete the workflow the user authorized and say which steps use credits. Ask only when a consequential choice is missing, when you would add scope they did not request, or when they asked to review first.
4. **Never guess.** Take IDs from results in this conversation. Do not invent names, quotes, numbers or proof. If a tool you need is unavailable, say so and do not claim the work was done.
5. **Credits.** Before the first billable call, check `get_ai_credit_balance`. At zero or below, do not start; explain that a positive AI-credit balance is required. Work already admitted can finish below zero. The billable tools are in [references/billing-and-async.md](references/billing-and-async.md); easy to miss are `validate_canvas_item`, `create_canvas_customer_segment`, `create_canvas_item` with omitted or empty `relatedItemIds`, and interview imports. Do not state a charge no tool returned. If a call is blocked or fails, report it. Do not write the persona's answer, script, positioning or page yourself in its place.
6. **Generated work.** Scripts, documents and previews use `ready`/`error`; analyses and personas use `status`. `create_idea` creates the initial Canvas during the call; after success, read `get_canvas` immediately. There is no separate Canvas readiness field. Poll asynchronous work a few times with brief delays, then report pending work and its IDs. Never call a generator again to check or promise to watch.
7. **Unknown outcomes.** No mutation is guaranteed safe to retry. After a timeout or dropped connection, read what was saved before trying again.
8. **Delete only within the user's authorized scope** (read the destructive-actions reference first). Explain the affected resource and known consequences. A specific delete request supplies authorization; ask only if scope or consequences need clarification. Do not delete to fix something an update can fix. Do not promise removal or recovery of external previews or presentations. Details: [references/destructive-actions.md](references/destructive-actions.md).
9. **Keep workspaces separate.** Never use one client's findings in another's work.

## Working with the tools

- Use `get_profile` with `{}` to identify the connected Icanpreneur user. Its stable `id` is the platform user ID; `name` and `email` are display metadata. It reads only the authenticated account and cannot select another user or update the profile.
- Find the workspace with `list_ideas`. `ideaId` is the idea's `uniqueId`. Archived workspaces need `includeArchived`. Ask if several match. Read before you write; reads are free.
- Use the workspace language (`get_idea`) unless asked otherwise. Check `list_supported_languages` for another.
- Paged lists default to 20 items. Page with `take` and `skip` to `totalCount` before counting or concluding something is missing. Research insights, quality, members, invitations, languages and credit costs are unpaged; send only their supported fields.
- A customer segment is a Canvas `CustomerSegments` item. A Buyer Persona is created only by `BuyerPersona` research. A positioning document's `id` is the `positioningDocumentId`. Full table: [references/ids-and-fields.md](references/ids-and-fields.md).
- Updates leave omitted fields unchanged, but `sections`, `text`, `relatedItemIds` and `customerSegmentIds` replace the whole value. Read, change, send the full result.
- An interview's `stage` is separate from analysis `status` (`NotStarted`, `Pending`, `Complete`, `Error`). `updatedOn` is a modification timestamp, not a completion time. Research reads select the latest attempt, which can be partial or absent. Persona `Complete` alone is insufficient: an empty persona can be Complete. Positioning generation requires Complete and a nonempty description. Details: [references/billing-and-async.md](references/billing-and-async.md).
- `create_contact` records real people only. Never use it for simulated or "modeled on" people.
- `upload_file` needs the real bytes in `contentBase64`; never rebuild them from a summary. Transcripts cannot be passed as text.
- Research evidence, quotes and supporting counts come from `list_research_insights`, which returns all categories. There is no separate per-insight read tool.

## Reporting

Lead with the answer and name the workspace, research or persona you used. Add one line on the evidence behind findings. Say what you changed, what is still processing and what you did not do. Save to the workspace only what was asked; offer once to save conclusions as a note ([references/team-and-notes.md](references/team-and-notes.md)).

**Read before acting:** [references/evidence.md](references/evidence.md) before reporting any evidence counts; [references/billing-and-async.md](references/billing-and-async.md) before a billable or generating call you are unsure about; [references/destructive-actions.md](references/destructive-actions.md) before any delete; [references/definitions.md](references/definitions.md) before creating or judging Canvas items; [references/multiple-workspaces.md](references/multiple-workspaces.md) for more than one workspace; [references/team-and-notes.md](references/team-and-notes.md) for notes, exports and invitations.
