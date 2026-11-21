---
name: phrase
description: Work with a user's Phrase account (TMS translation projects and jobs, Strings localization keys and translations, quality checks) through the Phrase MCP tools. Use when the user asks about translation job status, creating or updating jobs, localization keys, translations, or translation quality in Phrase.
---

# Phrase

Use the Phrase MCP tools to read and change data in the user's own Phrase account. Phrase has three main areas:

- **TMS** (translation management): projects, jobs, analyses, assignments.
- **Strings** (software localization): projects, keys, locales, translations, glossaries.
- **Quality**: automated translation quality checks, including placeholder and variable mismatches.

## How to work

1. Identify the product area first (TMS or Strings). They use different projects and tools; don't apply TMS settings to a Strings project or the reverse.
2. For lookups, call the read tools and answer from the returned data. Say plainly when a result is empty or when a list is paginated and you only saw the first page.
3. For "my jobs" questions in TMS, start with the jobs assigned to the signed-in user. If none are assigned and the user is an admin or project manager (the role in whoAmI), say so, then list the jobs in their projects and filter those. A job is overdue when its due date has passed and its status is not DELIVERED, COMPLETED, CANCELLED, DECLINED or REJECTED.
4. Before any write (create, update, delete, bulk change), tell the user exactly what will change and in which project, then wait for a clear yes. For bulk changes, show the count and a sample first.
5. Before pushing strings or translations, check what already exists so reviewed translations are not overwritten without the user knowing. Before creating a job, check whether one already exists for the same file and target language; if it does, or if a value is already what the user asked for, say so instead of repeating the change.
6. Report what was actually changed after each write, using the tool's response.

## Boundaries

- Only act on the signed-in user's account and only on what they asked for.
- If a tool returns an error, show the error message and what you tried; don't retry a write with different parameters without asking.
- If the user asks for something Phrase's tools can't do, say so instead of approximating it.
