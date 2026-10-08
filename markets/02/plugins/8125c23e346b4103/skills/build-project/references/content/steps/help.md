# 👋 Welcome to the Devpost Hackathons guide

This plugin turns Codex into your hackathon copilot — right here in chat, right in your project folder. It walks you from "what's open?" all the way to "submitted" without you having to keep track of anything.

## The big idea

**First, see what's open.** Type `$find-hackathon` to see the current featured hackathon in this app. Everything else — registering included — happens once you start it.

From there, the hackathon is a journey of five steps, and each step is a command you type in chat:

| Step | Command | What it does |
| --- | --- | --- |
| 1. Start | `$start-hackathon` | Register for the event and set up local progress tracking. |
| 2. Rules | `$review-hackathon-rules` | Walk through the rules so nothing disqualifies you later. |
| 3. Resources | `$resources` | Get build resources, links, and anti-pattern advice. |
| 4. Prepare | `$prepare-submission` | Draft your Devpost submission as a local file. |
| 5. Submit | `$submit-project` | Run the final check, then actually submit to Devpost — with your confirmation. |

## Want more structure while you build?

Inside the Resources step there's an optional guided build track that takes you from rough idea to working project, one document at a time:

`$build-onboard` → `$build-scope` → `$build-prd` → `$build-spec` → `$build-checklist` → `$build-project`

Totally optional — skip it if you already know what you're building.

## Lost? There's a compass 🧭

You're looking at it — `$hackathon-map` shows this tour when you're new, and once you're underway it shows where you are, what you've finished, and what to do next. Use it any time you switch chats or lose the thread.

## Good to know

- Your progress lives in one small local file in this folder — nothing leaves your machine.
- Everything Devpost-side needs you signed in to the Devpost connection — Codex will tell you how to sign in if you aren't.
- Codex never submits without asking. At the end, `$submit-project` submits for you — after showing exactly what will be sent and getting your explicit "yes, submit" — and then verifies with Devpost that it landed.
- New here? Type `$find-hackathon` to see what's open — the guide takes it from there.
<!-- Copy maintainers: edit this page copy in content/steps/help.md. This page is presented
by $hackathon-map as the welcome tour (no state yet, or the user asks for orientation). It is
the source of truth for the participant-facing command list — when skills are added, renamed,
or removed, update the tables here by hand. -->
