# Routing policy

## Source-of-truth matrix

| Intent | Primary system | Examples | Do not use as substitute |
|---|---|---|---|
| Durable knowledge | Notion | decisions, research, procedures, project context | TickTick description, Calendar notes |
| Personal action | TickTick | call, buy, submit, investigate, follow up | Calendar unless it consumes a time slot |
| Fixed time commitment | Google Calendar | meeting, doctor, flight, appointment | TickTick as the only record |
| Conditional / recurring monitoring | ChatGPT Automations | notify when price drops, daily briefing, watch for reply | polling manually in TickTick |
| Shared team work | Linear | bug, feature, engineering task, project issue | personal TickTick task as team source of truth |
| Email operation | Gmail | search/read/reply/send/archive | Notion as mailbox |
| Files/docs | Google Drive | locate/create/edit/share Docs/Sheets/Slides/files | Notion unless intentionally converting to knowledge |
| Contact resolution | Google Contacts | attendee/recipient identity | guessing an email address |

## Ambiguity rules

### Task vs event
Use Calendar only when the thing itself happens at a specific time or reserves time. A due date alone does not make an action an event.

- "Submit tax form by Friday" -> task.
- "Tax adviser call Friday 14:30" -> event.
- "Prepare questions for tax adviser before Friday" -> task, optionally linked conceptually to the event.

### Task vs Linear
Use Linear when other people or a team should treat the item as a shared tracked work object. Use TickTick when it is the user's private next action.

- "Fix checkout callback timeout" in a team engineering context -> Linear.
- "Ask Misha about the callback timeout tomorrow" -> TickTick.

### Knowledge vs file
Use Notion when the value is the structured knowledge itself. Use Drive when the value is a file/document artifact, especially when format, sharing, or collaboration matters.

### Automation vs task reminder
Use TickTick for a known action at a known date/time. Use Automation when execution depends on a future external condition or when the user wants repeated future delivery/checking.

## Retrieval order examples

- "When is my dentist?" -> Calendar.
- "What did we decide about provider X?" -> Notion, then relevant Drive/Linear only if needed.
- "Did I already make a task for MOT?" -> TickTick.
- "What happened with the price watch?" -> Automations/task state as appropriate.
- "Find the email where they confirmed it" -> Gmail.

## Persistence policy

Prefer compact, high-signal records.

### Good task titles
- "Book MOT inspection"
- "Send school bus confirmation"
- "Ask provider for termination fee"

Avoid:
- "Do stuff"
- full conversational sentences
- dumping research into a task title

### Good knowledge pages
Start with a short summary, then structured context. Preserve source links/citations when available. Separate facts from hypotheses.
