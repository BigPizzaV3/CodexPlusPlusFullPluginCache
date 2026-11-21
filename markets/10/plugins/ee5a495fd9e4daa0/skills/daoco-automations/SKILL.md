---
name: daoco-automations
description: Set up, change, pause, or delete automations, recurring work Daoco runs in the brand on a schedule or when something happens there, while the app is closed, such as a weekly performance review or a post idea every morning, and read what the runs produced. Use when the person wants something done every day or week, once at a later time, or whenever an event happens.
---

# Set up automations in Daoco

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for brand selection and tool boundaries.

An automation is a request Daoco runs on a schedule or on an event. Each run starts a new brand thread owned by the person, as `start_work` does, and keeps going while the app is closed. Every run uses workspace tokens, and its drafts and approvals follow the brand's approval settings. Say both before creating one.

## Check what already runs

Call `list_automations` first. `automations` are this app's own; `otherAutomations` are everything else in the brand (assistants' tasks, other apps' automations, ones people made in Daoco, brief inboxes), each with its trigger and, where listed, its workflow. Do not set up work another automation already does; offer to change the existing one instead, or point the person to it in Daoco when it is not this app's.

## Create one

Create an automation only when the person asked for recurring, later, or event-driven work. `create_automation` takes a short `name`, the `instructions` each run sends, and exactly one trigger:

- `intervalMinutes`, 30 or more, counted from now (1440 is daily).
- `cron`, five fields, read in `timezone` (`0 9 * * 1` is Mondays at 9:00).
- `runAt`, an ISO 8601 time for one run later.
- `event`, with `platform` where it applies, to run when something happens in the brand.

Ask for the person's time zone when the schedule depends on a local time, and pass an IANA name; the default is UTC. Use a `clientRequestId` so a retry does not create a second one.

Where the server lists `workflow`, an automation can run one of the brand's workflows on every run: pass its id from `list_automations` `workflows`, and the `instructions` say what it is about. Elsewhere, write the instructions as the full request in plain words.

Write `instructions` as one complete request in the person's words; each run reads only them, the automation's latest runs, and the brand's scheduled and recent posts. Keep the person's scope: an automation that drafts does not publish unless they asked, and publishing still follows the approval settings. Do not run it more often than the request needs.

If the reply is `already_running`, another automation in the brand already does this work (`existing` says whose and when); nothing was created. Tell the person instead of retrying with different words. A reply with `alreadyExisted` returned this app's identical automation.

Confirm what was created: the name, the trigger in words, the first run (`nextRunAt`), and that it can be paused or deleted from the app or in Daoco.

## Manage them

`update_automation` changes the name, instructions, trigger, time zone, workflow where offered, or `status`: `paused` stops runs, `active` resumes from now. `delete_automation` ends one; a run already working finishes, and past threads stay. Change or delete only the automation the person named. An app has at most 25. Daoco may pause one itself (`pausedBecause`), for example when the app is turned off; report the reason. A run still working when the next is due skips that one.

## Read the results

Each run is an ordinary thread, listed in `list_automations` with its `threadId`. Read it with `get_work_status`, `read_work`, and `get_output`, and check `list_work` with `view: "needs_you"` for approvals runs raised.
