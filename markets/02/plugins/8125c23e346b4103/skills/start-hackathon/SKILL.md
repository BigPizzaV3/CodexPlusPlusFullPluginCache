---
name: start-hackathon
description: Start the Devpost Hackathon workflow in the current project folder and register for the event. Use when the user wants to begin the guided experience, initialize the local state file, register on Devpost, or understand the end-to-end flow before working through the event in Codex.
---

# Start Hackathon

## Purpose

Own the first real setup: initialize or resume the local hackathon state, register the participant for the event, compose the Start chat response, and point them to the next command.

Chat is the primary participant interface. Keep responses text-first so they render in any Codex host; the bundled `devpost` MCP server supplies rich inline visuals on hosts that support them.

## Required Data Source

Official event data comes from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure). Every `devpost` tool call requires sign-in; the auth gate is this skill's first required `devpost` call. On a fresh start that is a selection call — `list_open_hackathons` or `get_hackathon_overview` (see **Preconditions**); when a hackathon is already selected, it is `get_registration_form` (see **Registration**). Do not add a separate `whoami` call.

For the Start page, draw on these only as needed: `devpost.get_hackathon_overview`, `devpost.get_key_dates`, `devpost.get_announcements`. For inline selection when no hackathon is chosen (see **Preconditions**): `devpost.list_open_hackathons`.

For registration (see **Registration**): `devpost.get_registration_form` and `devpost.register_for_hackathon`.

## Required References

Read before responding:

- `references/plugin-runtime.md`
- `references/config/hackathon.json`
- `references/content/steps/start.md` (the page content you will present)

## Workspace Assumption

Treat the current directory as the participant's real hackathon project folder.

If the folder already contains project files, continue. This plugin is meant to operate inside the real project, not in a separate notes workspace.

## Preconditions

Read `.devpost-hackathon-state.json` if it exists. `$find-hackathon` is discovery only and
writes nothing, so selection normally happens here. If no hackathon has been chosen yet
(`hackathon.selected` is absent or false), do not stop and do not bounce the participant to
another command — resolve the selection inline, then continue with this command's flow in
the same turn:

1. If the participant named a hackathon in their message (a Devpost slug, a clear event
   name, or a devpost.com URL), confirm it via `get_hackathon_overview` and select it
   (`source: "known"`).
2. Otherwise call `devpost.list_open_hackathons` once:
   - **Exactly one hackathon in the catalog:** select it automatically — do not present a
     list of one or ask them to choose. Say so in one line: "This app currently features
     [name], so I've set you up for it — the full catalog is always on Devpost" (link
     `links.browse_hackathons` from `references/config/hackathon.json`). Then move on
     (`source: "featured"`).
   - **More than one:** present the short numbered list (top 3-5); when they pick, confirm
     via `get_hackathon_overview`, then continue (`source: "search"`).
   - **Fetch fails or returns nothing:** ask them to paste a hackathon name, slug, or URL.
     Never invent or assume an event no tool returned.
3. **Slug:** the catalog entries carry no slug. Derive it from the event's standard
   `https://<subdomain>.devpost.com/` URL — the subdomain is the slug. This is a
   deliberate shortcut for the current one-event period; revisit the identity/listing
   design when multiple events are supported. Later steps (for example `$resources`) read
   `hackathon.slug`, so always record it.
4. Record the selection in the `hackathon` block of the state file initialized below —
   `slug`, `name`, `url`, `selected: true`, and the `source` noted above.

The single-entry auto-select is deliberately not a config flag — the server-curated catalog
is the switch. While the catalog lists only one event (Build Week at launch),
`$start-hackathon` alone gets participants into it with zero friction; when the catalog
opens up after the event, this same rule automatically starts presenting choices. Nothing
to un-ship. Every later step targets the selected event.

## State Initialization

This command initializes the full local state, once. If `.devpost-hackathon-state.json`
does not exist in the project root, create it by writing this initial payload (the
canonical state shape), with the `hackathon` block filled in from **Preconditions**:

```json
{
  "plugin": "devpost-hackathon",
  "version": 2,
  "hackathon": { "slug": "", "name": "", "url": "", "selected": true, "source": "" },
  "participant": { "name": "", "display_name": "" },
  "project": { "name": "", "summary": "", "ai_usage": "", "codex_usage": "" },
  "current_stage": "start-hackathon",
  "completed_stages": [],
  "rules_acknowledged": false,
  "learning": { "status": "not-started", "current_step": "", "completed_steps": [], "plan_file": "", "checklist_file": "" },
  "submission": { "draft_file": "devpost-submission.md", "status": "not-started" },
  "next_command": "start-hackathon"
}
```

The initial payload deliberately does not add `start-hackathon` to `completed_stages` —
this stage is marked complete only after the registration gate resolves (see **Marking
Start Complete**). Never mark a stage complete before its auth gate has passed.

If a state file already exists but is partial — for example a legacy file containing only a
`hackathon` block, written by an older version of `$find-hackathon` — merge the initial
payload into it: add every missing field, preserve every field that is present (including
`hackathon`), and never reset progress.

If the state file already exists and is complete, do not reinitialize and do not reset
progress — load it, preserve it, and continue.

Do not create sample project content, draft submission files, or example hackathon notes
during this step. Only initialize or reuse the state file.

## Registration

Step 1 is the registration surface. After state is initialized:

1. Call `devpost.get_registration_form` immediately — do not first ask whether the participant is already registered, and do not call `whoami`. This call requires sign-in (when a hackathon was already selected before this run, it is the skill's first required call and therefore the auth gate) and it reports both the participant's registration status and the form requirements.
   - **Auth failure:** hard-stop per **On auth failure** in `references/plugin-runtime.md` — one-line notice, the sign-in recovery, and stop. Do not walk the participant through registration questions they will be unable to submit.
   - **Already registered:** say so in one line and skip the rest of this section — continue to the Start response.
   - **Availability failure (not auth):** degrade in one line per `references/plugin-runtime.md` and offer the browser fallback (the official event landing page from live data or the hackathon URL already in local state).
2. Walk the participant through the required fields conversationally:
   - Open the walk-through plainly: "Reply to these registration questions and agree to the rules and terms." Tell them they can answer in ordinary language — free text is fine — and that questions marked with an asterisk (*) are required.
   - Present each custom question's text VERBATIM, IN ALL CAPS, exactly as the form returns it — never paraphrase, summarize, or truncate a question (a participant must see precisely what they are answering). Mark required questions with an asterisk (*). Before submitting, confirm every required question has an answer — stop and ask rather than submitting with gaps or invented answers.
3. Show a short plain summary of exactly what will be submitted on the registration form and require an explicit confirmation before proceeding. Alongside the rules/terms agreement, include the website-prevails disclaimer: this guide is a helper — if anything here ever disagrees with the Devpost website, the website prevails.
4. On confirmation, call `devpost.register_for_hackathon` with the collected answers, then report the result. If it fails on availability, degrade in one line and offer the browser fallback above.

Do not persist registration status in the state file — it is Devpost-owned and read live. Registration is a real write to Devpost: never call `register_for_hackathon` without the participant's explicit go-ahead on this turn.

## Marking Start Complete

Once the registration section resolves without an auth stop — already registered,
registration submitted, or the availability-failure browser fallback (offered or
declined) — update `.devpost-hackathon-state.json` before composing the Start response:
add `start-hackathon` to `completed_stages`, and set `current_stage` and `next_command`
to `review-hackathon-rules` (per **Next-command discipline** in `references/plugin-runtime.md`).

On an auth failure, make no completion update: leave `current_stage` and `next_command`
as `start-hackathon` so `$hackathon-map` routes the participant back here, keep the
recorded `hackathon` selection so a rerun resumes cleanly after sign-in, and hard-stop
per `references/plugin-runtime.md`.

## Personalization

Do not ask personalization questions here — no name question, no project-idea question.
The guided build tool's onboarding (`$build-onboard`) picks up the participant's name via
`devpost.whoami` and the project idea through its interview; submission prep gathers the
rest. If the participant volunteers a name or project idea unprompted, record it in
`.devpost-hackathon-state.json` (`participant.display_name`, `project.summary`, and
`project.name` only for a clear project name), preserving the rest of the file — but never
solicit it.

## Presentation Output

After creating or loading state, compose the response in-context per `references/plugin-runtime.md`
("Composing the Response"): read `references/content/steps/start.md`, strip maintainer `<!-- -->`
comments, interpolate the event name, and present it as the participant-facing response.
Render the journey stepper widget first (see PLUGIN_RUNTIME). Keep the response text-only;
the stepper widget is the progress visual.

## Chat Output

Keep chat output minimal. Do not hand-write a separate progress dashboard or landing
experience — the stepper widget shows progress.

In normal operation, respond with:

- a warm welcome that names the event and explains that Codex will guide the participant through the hackathon from this project folder
- one sentence explaining that Codex will keep the process in chat with text progress
- whether state was created or loaded
- the next command: `$review-hackathon-rules`
- an invitation to ask questions about how the flow works before continuing

## Handoff

End by telling the participant:

1. Their registration status (registered here via MCP, already registered, or the browser fallback if declined/unavailable).
2. Run `$review-hackathon-rules` next.

The stepper note is on the Start page itself (`content/steps/start.md`): a simple stepper visualization always shows what stage they're in, and `$hackathon-map` is there whenever it isn't enough information. Don't repeat that note in your own prose — the page carries it.
