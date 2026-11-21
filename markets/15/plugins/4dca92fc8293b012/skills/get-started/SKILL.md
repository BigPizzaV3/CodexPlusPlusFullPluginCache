---
name: get-started
description: Help a user get started with Script.it by inspecting their connected workspace and building, saving, and testing their first automation. Use when the user runs plugin setup, asks to get started with Script.it, or asks to turn the task in this conversation into their first Script.it workflow.
---

# Get started with Script.it

Move from the user's goal to a verified first result, with a saved workflow or
agent when that is what the user requested.
Follow explicit user instructions over these defaults. If the user requests
only an explanation, inspection, or a draft, respect that scope.

## Open the workspace

1. Call Script.it's `start_session` before giving generic setup advice. If this
   conversation already has a usable Script.it session and its complete context,
   reuse it. Read all returned context, including runtime instructions, skills,
   workspaces, and connected integrations. Recover any truncated context through
   documented means before relying on missing details.
2. Use the returned `session_id` for `run_command` and `read_output`. Follow the
   live runtime reference for commands and workspace paths. Read relevant skills
   using the documented commands before building. Keep execution in Script.it.
3. If authentication is required, use the supported connection flow and resume
   after it succeeds. Never ask for passwords or tokens in the conversation. If
   the tools are unavailable, explain the connection needed; do not claim a
   session opened or substitute a local execution for a Script.it run.

## Choose the first task

- If the conversation already contains a concrete supported task, continue
  it immediately. Reuse supplied inputs, destinations, preferences, and the
  requested execution mode. Accept concrete jobs such as scraping a portal,
  sourcing leads, processing invoices, or building a knowledge agent, alongside
  "keep doing this" and "when this happens, do that". Do not require recurrence.
- If no task is given, ask one short question with three concrete choices
  grounded in the available capabilities. Include at least one option that
  needs no additional app connection, such as collecting a public page into a
  CSV. Use concrete tasks from the use-case guide below; include schedules,
  event rules, or interactive agents when relevant to the user.
  Tailor other options to connected apps. Let the user choose or describe
  their own task before creating a workflow.
- Ask only for information that blocks progress, such as the source URL, a
  destination that cannot be inferred, or an ambiguous workspace. Use a returned
  default workspace when appropriate. Do not ask users to repeat known details.
- If a needed integration is missing, use the documented connection process.
  Complete independent work while waiting when useful, and identify the step
  that remains blocked. Never describe an unconnected app as available.

## Build and verify

Once the user has chosen a task, follow [Automate a task](../build-automation/SKILL.md)
using the existing session and recovered task. It covers all twelve product
use cases, one-off execution, saved workflows, interactive agents, schedules,
and event triggers. Do not repeat discovery or ask the user to restate known inputs.

Starting setup alone does not authorize messages, external writes, or recurring
runs. Complete actions already requested by the user, including an explicitly
requested schedule or event trigger, when the necessary information is available.

## Show the result

Lead with what was completed and a small preview of its actual output. Link to
the output, saved workflow, or agent using a URL returned by Script.it or a URL
format explicitly documented in the live context. If only a session URL is
available, label it as the session and identify any saved resource separately.

State whether recurring execution is active, configured but inactive, or not
configured when relevant. Finish with one useful next action, such as changing
an input or completing an event connection. If the user already requested that action and
provided what is needed, complete it instead of offering to do it later.
