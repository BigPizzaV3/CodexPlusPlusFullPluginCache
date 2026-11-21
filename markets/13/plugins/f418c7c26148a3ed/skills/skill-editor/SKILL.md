---
name: skill-editor
description: View, edit, switch on or off, restore and draft the skills in Knowledge > Skills - the workspace's own skills and its copies of Kenso's default skills - so every agent that loads them follows the workspace's version.
---

# Skill editor

A skill is a set of instructions an agent follows for one job. The workspace's skills live in Knowledge > Skills in Kenso, as files at level `skill`. There are two kinds:

- **Kenso skills**: the workspace's copies of Kenso's built-in skills, which Kenso puts in the Skills folder when Kenso skills are on for the workspace. Kenso keeps an untouched copy up to date. An edited copy keeps the workspace's text, and the app shows a banner when Kenso has a newer version.
- **Workspace skills**: skills people wrote or Ken drafted from their work. Agents list them as `knowledge/<cmd>`.

A skill reaches agents when it is on, reviewed and has a command (`cmd`). In the Ken pane it is `/<cmd>`.

Knowledge has no tool in this app: you cannot list, read, change, switch on or off, restore or draft a skill here. You help the person write the change, by the rules below, and they make it in Knowledge at `https://app.ken.so/<workspace id>/demo/knowledge`.

## Rules

- **Admins edit shared skills.** A shared skill, every Kenso skill included, changes only through a workspace admin; a private skill belongs to the person who made it. When the file is locked for the person, write the change for them to send to a workspace admin.
- **A yes before each save.** Show the change as before and after, in the skill's own words, and hand it over after the person agrees.
- **Read, then write.** Work from the text as it is now: ask the person to paste it fresh before each change, because someone may have saved since.
- **Keep the approvals.** A skill must never let an agent send, launch, book, spend credits, or change a campaign's schedule or volume without a person's yes. Keep every approval step and "a person approves" line. When a requested edit would remove one, say so and leave that part out.
- **Keep what agents parse.** Leave the tool calls, operation names and the double-brace brand placeholders exactly as they are unless the person asks to change one; a wrong operation name breaks the skill.
- **Edit the main text only.** A Kenso skill's references stay Kenso's and cannot be edited. To change what a reference says, add the override to the main text ("For this workspace, ignore the subject-line rule in the copy reference: we write ...").
- **Kenso skills are switched off, never deleted.** Delete refuses them.
- **Triggers only on request.** A trigger makes the skill run on its own and can build a workflow that spends credits. Set or change `trigger` only when the person asks, and say what it will run.
- **Cite what clients want.** A rule about what a client wants carries its source: who said it, where and when.

## In this app, step by step

1. **Open it.** The person opens `https://app.ken.so/<workspace id>/demo/knowledge`, the Skills folder, and the skill; each file has its own page, `https://app.ken.so/<workspace id>/demo/knowledge/f/<file id>`. When Knowledge does not open, it is off for this workspace: say so in one sentence and stop. Kenso's current text of a Kenso skill is read-only at `https://app.ken.so/<workspace id>/demo/knowledge/ken/<name>`.
2. **Read it.** Ask them to paste the skill's text, and Kenso's current text when they want to see what the workspace changed. Summarize it: what it does, when it runs, its steps, and anything that looks out of date.
3. **Write the change.** Agree the steps, wording or rules to add, drop or rewrite, then write the new text of each heading that changes, before and after. Only the main text: references stay Kenso's, so an override goes in the main text.
4. **They save it.** On the file's page they edit the text in place (the editor takes markdown, and Markdown source shows the raw text). Each save is a new version in History. A command is lowercase words joined by hyphens, up to 40 characters; without one the skill stops reaching agents.
5. **On or off.** The file's Active switch. An off skill leaves agents' lists and the `/` menu. A Kenso skill that is off still loads Kenso's default text by its exact name, so pipelines that load it keep working.
6. **Undo.** History lists every version, newest first: restoring one writes it as a new version, so nothing is lost. Back to Kenso's current text of a Kenso skill: Reset to Ken's version in the file's toolbar.
7. **When Kenso updates a skill.** An edited copy shows a banner with See changes, Keep mine and Reset to new. To merge, ask for both texts, show what Kenso changed next to what the workspace changed, and on a yes give them the merged text to save; then they click Keep mine so the update stops showing as waiting.
8. **A new skill.** Write it as steps an agent follows: when to use it, what it needs, the steps, the rules, what it hands back. They add it in the Skills folder with New file, keep it private and off until one real request walked through it reads right, then switch it on, and share it (admins) when the team should use it.

## What this skill cannot do yet

- Edit a skill's references. They stay Kenso's.
- Delete a Kenso skill. Switch it off.
- Change a built-in skill for a workspace that has no Kenso skill copies.
- Read or save anything in Knowledge from this app: the person does it in Knowledge.

