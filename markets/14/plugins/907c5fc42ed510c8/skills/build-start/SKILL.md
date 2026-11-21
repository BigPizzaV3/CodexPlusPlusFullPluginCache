---
name: build-start
description: "Use only for the host's Build_ onboarding, an explicit welcome request, or a submitted standalone Press Enter to begin (legacy Press Enter to start). Show the brief introduction without building anything. A substantive app request belongs in the main build skill."
---

# Build_ welcome

Read or retain `../build/SKILL.md` as instructions only. It carries the workflow
for the next relevant app reply, including untagged follow-ups. The welcome does
not prepare the engine, create project state or authorize an application build.

For an actually submitted starter or explicit welcome, follow
`../build/Automation/CT90.md` and call the existing `get_build_workflow` once with
phase `welcome`. Reuse a result already obtained in THIS turn; do not duplicate a
call through main-skill/onboarding delegation. A setup event, blank message or chip
selection alone makes no MCP call. If unavailable, give one brief factual notice
and continue with the welcome; do not retry, reconnect or call another tool.

Read `../build/Automation/WC23.md` and show its original short introduction
unchanged as an assistant reply. Append this sentence once:

To continue with Build_, type @, select Build_, and add your reply.

Use this same existing plugin from the @ menu. The cue does not pin a chip, mount
scripts or create an extra empty continuation turn. Do not insert, clear, focus or
send composer text. Do not execute scripts, inspect unrelated uploads, create
projects, build a sample app, change settings or request a new connection.

If the welcome already appeared in this conversation, do not repeat it. Continue
a substantive request through `../build/SKILL.md`, or ask what the user wants to
make if they have not said. Pure usage help reads `../build/Automation/HP12.md`
and appends the same single continuation sentence, with no guide call or build.

Preserve substantive text submitted alongside the selection; do not replace it
with onboarding or require a retyped request. A user may skip the welcome and ask
for an app directly. Relevant untagged replies still use the established workflow.
No onboarding completion, account change or report is required before a first build.
