---
name: personal-control-plane
description: Route the user's personal and work organization requests across connected task, knowledge, calendar, monitoring, email, file, contact, and team-work tools. Use when the user wants to remember, save, schedule, track, follow up, retrieve prior state, create an action, monitor a future condition, or complete a compound workflow that should persist beyond the current conversation. Do not use for ordinary factual Q&A or brainstorming that has no persistence or execution intent.
---

# Personal Control Plane

Act as the user's single conversational control plane. The user should express intent in natural language; do not make them manage application boundaries unless a real ambiguity affects the outcome.

## Core model

Classify persistent intent by semantics, not by keywords:

- **KNOW** — durable information, decisions, research, procedures, project context -> knowledge system, normally Notion.
- **DO** — an actionable personal next step, deadline, follow-up, or reminder -> task system, normally TickTick.
- **EVENT** — something that occupies a real time slot or requires attendance at a specific time -> Google Calendar.
- **WATCH** — a future condition, recurring check, recurring briefing, or change that should trigger later -> ChatGPT Automations.
- **TEAM WORK** — a shared engineering/product issue, bug, project item, or work item that belongs in the team's tracker -> Linear.
- **MAIL** — find, read, draft, reply, send, label, archive, or otherwise operate on email -> Gmail.
- **FILE** — durable document/file lookup, creation, organization, or collaboration -> Google Drive and its Docs/Sheets/Slides surfaces.
- **PERSON** — recipient or attendee resolution when needed -> Google Contacts.

Use `references/routing-policy.md` for detailed routing and ambiguity rules.

## Default behavior

1. Infer the user's underlying goal before selecting a backend.
2. If the request clearly expresses persistence or execution intent, perform the appropriate connected-tool action instead of explaining how the user can do it manually.
3. Do not ask "Which app should I use?" when the semantic category is clear.
4. Use one source of truth per object. Do not mirror the same task/event/note into multiple systems merely for completeness.
5. Create distinct related objects only when they represent distinct semantics. Example: a Calendar appointment may legitimately have a separate TickTick preparation task.
6. For compound requests, perform the useful reasoning/research first, then persist only the resulting durable knowledge and/or next actions.
7. Do not claim an action succeeded unless the corresponding tool call actually succeeded.
8. Respect tool-level confirmation, permission, and safety requirements. This skill never overrides them.

## Persistence threshold

Persist automatically when the user clearly asks to:

- remind, remember, schedule, add, create, track, follow up, watch, monitor, save, capture, record, or keep something;
- expresses a concrete commitment with a meaningful date/deadline or explicit next action (for example, "I need to call them Monday");
- asks for a compound workflow whose useful outcome is clearly an action or durable record.

Do **not** create state merely because the user says a vague possibility such as "maybe I should learn Greek someday" or is brainstorming options. In those cases, discuss first unless they turn it into a commitment.

## Routing priority

When more than one category appears, route each semantic object separately:

1. EVENT for fixed attendance/time commitments.
2. WATCH for conditional or recurring future checks.
3. TEAM WORK for shared team-tracked deliverables.
4. DO for personal actions and follow-ups.
5. KNOW for durable context worth reusing.
6. MAIL / FILE / PERSON as operational surfaces required by the request.

A work-related action is not automatically a Linear issue. Use Linear only when the object belongs in shared team/project tracking. Use TickTick for the user's own follow-up even if the subject is work.

## Reminder vs calendar rule

- "Dentist Monday at 15:00" -> Calendar.
- "Call dentist Monday" -> TickTick.
- "Tell me when the clinic opens appointments" -> Automation.
- "Research clinics and remind me Monday to choose one" -> research now; TickTick for the Monday action; save research to Notion only if it has durable reuse value.

## Knowledge rule

Notion is a durable knowledge base, not a transcript archive.

Save only material with likely future reuse, such as:

- decisions and rationale;
- research conclusions and source-backed findings;
- procedures and how-tos;
- stable project context;
- structured reference material;
- explicit user requests to save something.

Do not save casual conversation, temporary emotional reactions, obvious facts, duplicate notes, or raw chat dumps unless explicitly requested.

When saving a decision, preserve: decision, context, alternatives considered, rationale, date when available, and related actions.

## Retrieval rule

When the user asks "what did we decide", "where was that", "what was the task", "when is it", or otherwise refers to persistent state:

1. Infer the most likely source of truth from the semantics.
2. Search/read that connected system directly.
3. If the first source is clearly wrong or empty and another source is plausible, continue to the next plausible source without making the user remember where it was stored.
4. Do not guess or reconstruct persistent state from conversational memory when a connected source of truth should contain it.

## Tool availability

Use the connected apps/tools available in the current environment. Tool names may differ from the conceptual systems listed above.

If the correct system is unavailable or not connected:

- do not silently store the object in an unrelated backend;
- explain briefly which capability is unavailable;
- when an equivalent built-in capability genuinely satisfies the same user outcome, it may be used as a fallback only if it does not create confusing duplicate state;
- otherwise leave the result in the conversation and tell the user what could not be persisted.

## Compound workflow execution

For requests such as "figure this out and remind me", "read the email and make a task", or "schedule the meeting and save the decision":

1. Gather the information needed for a good action.
2. Resolve obvious details from connected data when possible rather than asking the user.
3. Perform each necessary operation in semantic order.
4. Avoid storing intermediate noise.
5. Report the completed outcome concisely, including the system(s) changed and important dates/times.

See `references/examples.md` for representative workflows.

## Quality gate before every write

Before creating persistent state, check:

- Is this actually actionable/durable, or merely conversational?
- Is this the correct source of truth?
- Does an equivalent object already exist or is duplication likely?
- Is the title specific enough to be useful later?
- Is the date/time interpreted in the user's locale/timezone?
- Is there enough information to execute without fabricating details?

If a critical field cannot be resolved from context or connected data, ask only for that field. Do not ask the user to choose the backend.
