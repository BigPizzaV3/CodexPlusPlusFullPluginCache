# Plugin Runtime Rule

The participant's current working directory is their project folder, not this plugin
bundle. The local state file `.devpost-hackathon-state.json` lives in the
participant's project root.

This plugin runs entirely from skill instructions — there are no scripts to execute and
no Node dependency. You read the plugin's own content/config files (relative to the skill
you are running, exactly like the other entries under **Required References**), compose
the response yourself, and write state by editing the JSON file directly.

## Primary Interface

Chat is the primary participant interface. Compose responses text-first so they render in
any Codex host (terminal or desktop). The rich progress visual is the `devpost` MCP
server's stepper widget on hosts that can render it; your composed text must always stand
on its own without it. Do not tell the participant to open a localhost page, and do not
generate or embed images — the stepper widget is the only progress visual.

Every command should:

1. Read the required references and local state (`.devpost-hackathon-state.json`).
2. Make its workflow-specific state or document updates (see **Writing State**).
3. Render the journey stepper by calling the `show_hackathon_stepper` MCP tool (the
   bundled `devpost` server — `mcp__devpost__show_hackathon_stepper`) with the
   `active_step` for this stage — once per response, before the text. See **Journey
   Stepper**.
4. Compose the participant-facing text yourself (see **Composing the Response**).
5. End with the next-step callout when another command should run, as the final line —
   natural language leads, the exact command follows:

```text
Say "next" when you're ready — or type `$command-name`.
```

The spoken option is how people actually advance mid-conversation; the command is the
durable, discoverable re-entry point (it works in a fresh chat, and it's what the help
page and map teach). Always show both.

**When the journey is complete, there is no "next."** After a verified submission,
`next_command` is `hackathon-map` — a recovery command, not a next step — so do not emit
the "Say next" phrasing (there is nothing to advance to). Close with an anytime-offer
instead, as the final line:

```text
That's everything — type `$hackathon-map` anytime to see where things stand.
```

**The callout is an affordance, not a toll gate.** When the participant answers a branch
prompt in natural language — "move on", "next", "yes", "let's do it", or describing the
choice — treat it as the offered command and proceed on that turn. Never ask them to
re-type a command you just offered. Exceptions, which stay strict: the "yes, submit"
confirmation in `$submit-project`, and the registration and rules agreements — those
require the unambiguous confirmations their skills specify.

**Next-command discipline.** Update state first, then emit the callout from the state's
`next_command` — the two must never disagree. Never re-issue the command that just ran
unless a re-run is genuinely the recommendation (another `$prepare-submission` pass is the
legitimate case). At the Resources fork, use the two-path callout from the resources
skill, not a single next command.

## Devpost MCP Server

The `devpost` server (`https://devpost.com/mcp`) is the source of truth for official
event data. In ChatGPT the app connection provides it automatically; other hosts add it
once per `SETUP.md`. Follow these rules everywhere so a turn never becomes a
troubleshooting session:

- **Preload the tools on hosts that defer them.** Some hosts expose MCP tools lazily — only
  the server name is visible until the tool schemas are loaded. If the `devpost` tools are not
  in your tool list when a skill needs them, load/list the `devpost` server's tools once, then
  proceed. This is loading, not probing — it does not count as verifying or setting up the
  server, and it never involves the participant.
- **Call only what you need, when you need it.** Each skill lists the `devpost` tools its page
  can draw on; call just the ones required to render the current response, at the point you
  need them. Do not call every tool to pre-fetch data, and do not call a tool whose result you
  will not use. (Preloading tool *schemas* per the previous rule is fine — this rule is about
  actual tool calls.)
- **Do not verify, probe, or set up the server.** Assume the tools are available and call them
  directly. Never call a tool just to check it exists, and never tell the participant to
  register, add, re-authenticate, or restart the server during a normal turn. One-time
  install/setup lives in `SETUP.md`, not in participant responses.
- **Every `devpost` call requires sign-in — there is no public tier.** The **auth gate** is
  the skill's *first required call*: if it fails on auth, follow **On auth failure** below.
  Do not add a separate `whoami` probe before a catalog or form call — the required call
  itself is the gate. `whoami` is called as an explicit pre-gate only where a skill's own
  instructions say so (`$prepare-submission`, `$submit-project` — long flows that end in a
  Devpost write). One personalization exception: `$build-onboard` calls `whoami` once to
  greet the participant by name — never as an auth probe; if it fails or returns nothing,
  the onboarding proceeds namelessly and nothing is blocked or reported.
- **On availability failure, degrade in one line — do not self-correct.** If a `devpost` call
  errors or returns nothing for reasons other than authentication, treat it as "official data
  unavailable," not "something is misconfigured."
  Fall back immediately to the skill's named fallback file (official Devpost links live in
  `config/hackathon.json`) and note once, in a short clause, that the event details are
  provisional. Do not retry in a loop, diagnose the error, or re-explain the fallback on
  later turns.
- **On auth failure, hard-stop — do not continue.** If any `devpost` call fails because
  the participant is not signed in to Devpost, stop the flow. Say in one line
  that nothing on Devpost will work until they sign in, then offer the sign-in
  recovery (below). Never continue the journey as if they were signed in, never substitute
  web search or invented data for the blocked call, and never mark stages complete on this
  turn.
- **Sign-in recovery (consent first).** Ask whether they want to sign in now — do not run
  anything without their yes. On yes, where a terminal is available (Codex), run:

  ```bash
  codex mcp login devpost
  ```

  This opens the Devpost sign-in page directly. The active session cannot see newly stored
  credentials, so after the login completes, tell the participant to fully restart Codex and
  rerun the original command — do not retry the failed call in the same session. In hosts without a
  terminal (ChatGPT), sign-in is handled by the app connection: tell them to reconnect the
  Devpost app and rerun the command.
- **Never answer Devpost questions from web search.** Hackathon facts — what's open, dates,
  rules, prizes, requirements, resources — come from the `devpost` MCP or are declared
  unavailable. Web search is never a fallback for official data, on any failure or none.
- **Never present unofficial data as official.** Rules put forward for acknowledgment,
  submission requirements checked against, and hackathon resources shown to the participant
  must come from live `devpost` MCP data fetched this session. If the live data is
  unavailable, say so and show nothing in its place — do not substitute fallback files, web
  search results, or memory for official content. Fallback references may shape structure and
  questions, clearly labeled provisional, but never a consent gate or a resource list.

## Composing the Response

Build the text response in-context — do not run a script:

1. Read the page's content file from the plugin's `content/` directory, referenced
   relative to the current skill (e.g. `content/steps/start.md`). Each skill names
   its page content file under **Required References**.
2. Strip maintainer-only HTML comments (`<!-- ... -->`) — they are notes for editors, not
   for the participant.
3. Interpolate event values: replace `{{event.name}}` and `[Hackathon name]` with the
   event name (prefer live data from the `devpost` MCP server; otherwise the hackathon
   recorded in `.devpost-hackathon-state.json`). If official dates/URLs are unavailable,
   say so rather than inventing them.
4. Output, in order: a one-line headline for the stage, the interpolated page content,
   and the next-step callout. Keep it concise and text-only; the stepper widget already
   shows progress, so do not also hand-write a progress dashboard or ASCII stepper.

If you cannot read the content file, fall back to a compact text response with: the
current stage, the important blocker or result, the next command, and any required yes/no
prompt.

## Writing State

State lives in `.devpost-hackathon-state.json` in the participant's project root.
Edit it directly (a small JSON file edit is fine). Keep these rules:

- Keep the file small — the shape `$start-hackathon` initializes is the canonical one:
  local progress, light personalization, and local document paths only. Do not persist Devpost-owned data
  (registration, official dates, submitted status) — read that live from the `devpost`
  MCP server each turn.
- Write only when state actually changes on this turn. Turns that just read, recap, or
  answer a question should not write state.
- Preserve existing fields you are not changing; never reset progress the participant has
  already made.

## Submission Status Blocks

Whether the project is submitted is high-stakes truth, so the commands that surface it
(`$prepare-submission`, `$submit-project`, `$hackathon-map`) present it as one of these
two blocks, verbatim — heading level exactly `###`, nothing larger, never reworded or
softened:

```markdown
### ⏳ Not submitted yet
Nothing has been sent to Devpost.
```

```markdown
### ✅ Submitted to Devpost
Verified live. Your public project page: <URL>
```

Interpolate `<URL>` with the real public project page. This is the single source for both
blocks — the skills cite this section rather than restating the text, and each skill's own
instructions say which block applies when and name any sanctioned variants.

## Journey Stepper

Call `show_hackathon_stepper` once per response, before composing the text, on any turn
that moves the participant into a new step of the sequence. Pass the `active_step` for the
current stage:

| Stage / command       | `active_step` |
| --------------------- | ------------- |
| `$start-hackathon`    | `register`    |
| `$review-hackathon-rules` | `review`   |
| `$resources`          | `resources`   |
| `$prepare-submission` | `prepare`     |
| `$submit-project`     | `submit`      |

For the optional guided build tool (the `$build-*` commands, which all sit inside the
Resources step), pass `active_step: resources` and also:

- `build_assistant: true`
- `build_step`: the current sub-step from `learning.current_step` — one of `scope`, `prd`,
  `spec`, `checklist`, `build`. For `$build-onboard` (the entry step), pass
  `build_assistant: true` and omit `build_step`.

If the guided build tool is not active, omit `build_assistant` and `build_step` — the
stepper then shows Resources without the sub-stepper.

Use the exact argument names and accepted values from the `show_hackathon_stepper` tool's
own input schema; if the live tool differs from the mapping above, follow the schema and
pass the value that identifies the current stage.
