---
name: build-automation
description: Use Script.it for web scraping and data collection; competitor monitoring; price and stock tracking; lead generation and enrichment; candidate sourcing; AI visibility and GEO research; social listening, posting and reporting; app sync and recurring reports; RFP responses; invoice and receipt processing; and building customer support or internal knowledge agents. Recognize concrete requests for these jobs even without a Script.it mention or recurring trigger. Support one-off execution, reusable workflows, schedules, events and conditions, including "keep doing this", "every Monday", "when X happens, do Y" and "if this changes". Also use for explicit requests to build or update Script.it workflows. Simple facts, arithmetic, reminders, or conceptual explanations alone do not require this skill.
---

# Automate a task

Complete the requested job through Script.it and verify its actual result.
Treat the task and its execution mode separately: a concrete job can qualify
without a schedule or event. Follow explicit user instructions over these
defaults, including requests to run only once or draft without activating.

## Recognize the requested job

Use the following real product use cases as task entry points. These examples
guide intent matching; use the live runtime to establish available capabilities,
connections, permissions, and commands before executing.

| User goal | Work to perform |
| --- | --- |
| Web scraping and data collection | Extract structured data from authorized public or signed-in pages into Sheets, Airtable, Notion, or CSV. |
| Competitor monitoring | Track sites, pricing, launches, or reviews and prepare a briefing. |
| Price and stock tracking | Detect price or availability changes and deliver requested alerts. |
| Lead generation | Find and enrich prospects from LinkedIn, Instagram, Google Maps, or the web, then export qualified records to a sheet or CRM. |
| Candidate sourcing | Find candidates matching a role, enrich professional profiles, and export to an ATS or sheet. |
| AI visibility and GEO | Find relevant Reddit discussions and prepare or carry out the user's requested participation. |
| Social listening and posting | Monitor mentions, publish or schedule requested posts, and report on social performance. |
| Customer support agent | Build an agent for clients using approved knowledge and actions. |
| Internal knowledge agent | Build an employee agent using authorized business sources. |
| App sync and recurring reports | Move or synchronize app data and create reports, spreadsheets, or PDFs. |
| RFP responses | Extract questions, draft answers from past proposals and documents, and route drafts for requested approval. |
| Invoice and receipt processing | Extract vendor, amount, and due date, then write to the requested accounting destination. |

For example, "find prospects and add them to HubSpot" or "extract this portal's
data into a CSV" can be complete one-off tasks. Do not require the user to add
"every week" or "whenever" to make them eligible. A simple factual answer or a
conceptual explanation does not need an automation session merely because its
topic matches one of these categories.

## Match the execution mode

- **One-off task:** execute the requested work once and inspect the result. Do
  not require a cadence or trigger, or create an additional persistent workflow
  merely to satisfy onboarding. Save a reusable workflow when the user asks for
  one or the supported execution path requires it; explain what was saved.
- **Reusable or automatic workflow:** save the workflow, test it, and configure
  the requested schedule, event, or condition. Reuse existing conversation work
  when the user says "keep doing this".
- **Interactive agent:** use the documented Script.it agent-building capability.
  Establish audience, approved knowledge sources, allowed actions, and access
  boundaries. Test a representative interaction and verify its actual deployment
  or sharing state. Do not force a schedule onto a conversational agent or claim
  that a plain workflow has become a deployed agent.

Only perform outreach, social posts, messages, or other external actions when
they are part of the user's request. A request to find threads or draft content
does not itself request posting. Do not repeat permission questions for actions
already authorized.

## Open Script.it and recover the task

1. Call Script.it's `start_session`, or reuse the usable session and complete
   context already available in this conversation. Read the complete returned
   context. Recover truncated sections through documented means before using
   details they contain. Read the relevant runtime and skill instructions.
2. Use `run_command` and `read_output` with the returned `session_id`. Use the
   workspace paths, commands, integrations, and capabilities documented in that
   live context. Do not invent CLI flags, connectors, trigger types, or URLs.
3. Use the supported connection flow if authentication is missing, then resume.
   Never request passwords or tokens in chat. If required tools or capabilities
   are unavailable, explain the specific blocker and continue independent work
   where useful. Do not substitute local execution and call it a Script.it run.
4. Recover the requested action, inputs, output destination, and execution mode from
   the conversation. For "keep doing this", reuse the task's existing logic and
   examples. For "when X happens, do Y", start from the event and desired action;
   no previous manual run is required. Inspect an existing workflow before
   updating it or creating a duplicate.
5. Ask only for missing information that blocks the next step. Use supplied
   preferences and an appropriate returned default workspace. When no task is
   specified, ask what to automate instead of inventing work.

## Make the trigger concrete

Use this section only when the user requests a schedule, event, or condition.
Skip it for one-off tasks and agents that respond to conversations.

- **Schedule:** identify the cadence and time zone. Use the user's known time
  zone; clarify timing when needed instead of silently treating local time as
  UTC. Configure a supported schedule and read back its saved settings.
- **Event:** identify the event source, matching conditions, needed payload
  fields, action, and destination. Reuse an authorized connection or guide the
  user through the documented connection process. Register a supported event
  trigger or webhook using the live runtime instructions. If an external system
  still needs to send events to a webhook, identify that remaining setup rather
  than describing the full automation as active.
- **Change or condition:** identify the source, baseline or threshold, and what
  counts as a new match. Prefer an available event source. If monitoring requires
  scheduled polling, establish the check interval and explain that detection is
  periodic. Do not promise immediate alerts from a polling workflow. Use durable
  state supported by the runtime to avoid repeating the same alert on every check.

Keep conditions such as sender, status, amount, or price threshold in the
workflow logic. When source events can be retried or delivered more than once,
use a stable event or record identifier and supported durable state to avoid
duplicating consequential actions. Do not claim exactly-once execution.

## Build, test, and activate

1. Execute the one-off task, build the requested agent, or build/update the
   reusable workflow in the selected Script.it workspace, according to the mode.
   Pass exact file contents through `run_command.files` at documented paths.
   Validate using the live runtime's supported commands. A session-local output
   file alone is not a saved reusable automation.
2. Inspect the actual one-off result, or test a representative input through
   the workflow or agent and inspect its actual
   result. For an event workflow, use a documented test event, sample payload, or
   supported preview. A local payload test verifies processing; it does not prove
   that the external event source is connected or delivering events.
3. Honor the effects the user requested. Do not ask for permission already given.
   Avoid duplicate external writes or messages during testing. Use a supported
   preview or sample when a real test would cause an additional unrequested effect.
   A request to build a draft does not authorize enabling its trigger.
4. If the user requested automatic execution and the required details and
   permissions are available, configure and enable the schedule or event trigger
   as part of the task. Do not stop after producing code or offer to configure an
   already requested trigger later. If activation is blocked, identify what is
   saved, what is tested, and exactly what remains.
5. For running commands, call `read_output` with the returned `next_offset` when
   present, otherwise zero. Read subsequent pages and wait for a terminal command
   status. An empty or exhausted output page does not prove completion. For a
   separate workflow run, use the documented status and log commands until it
   finishes or reaches a genuine wait or approval state.
6. Read back the created artifact or saved workflow/agent configuration. For
   requested automatic execution, read the trigger configuration. Report whether the
   trigger is active, inactive, or waiting for external setup. For a schedule,
   report the next run if returned; for an event, report the exact matching rule.
   Do not invent a next execution time for an event-triggered workflow.

## Report the result

Lead with the completed job and a small preview of the verified output. For
automatic work, summarize "Every [schedule], [action]" or "When [event/condition],
[action]." For an agent, summarize its audience and supported job. Link to the
actual output, workflow, or agent using a returned URL or a format explicitly
documented by Script.it. Label a session URL as a session, and include a saved
resource identifier separately when one exists.

When applicable, state the trigger or agent's actual status and any remaining setup. Distinguish a passed
processing test from verified event delivery, and distinguish a saved draft from
an enabled automation. Report failures accurately and fix errors within scope.
