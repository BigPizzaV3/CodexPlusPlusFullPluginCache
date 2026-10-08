---
name: lightweight-app-guide
description: Explain how to use the Lightweight workout app, including navigation, starting and logging workouts, routines, gyms and Passport, progress, privacy, settings, and its ChatGPT connection. Use when someone asks how a Lightweight feature works, where to find something, what Lightweight supports, or how to complete an in-app workflow.
---

# Lightweight App Guide

Use this skill for product guidance about Lightweight. Read the relevant section
of [references/app-guide.md](references/app-guide.md) before answering.

## Answering workflow

1. Identify the feature or outcome the person is asking about.
2. Answer in the person's language, using the current labels and navigation in
   the guide.
3. Prefer a short path followed by numbered steps. Mention an important privacy,
   platform, or review consequence only when it affects that workflow.
4. If the guide does not establish that a feature exists, say so instead of
   inventing a menu, entitlement, or release status. Direct unresolved account
   or technical problems to `https://getlightweight.com/support`.

## Data and tool boundary

- General app-help questions do not require a Lightweight connection and must
  not trigger account-data tools.
- Use the MCP connection only when the person asks about their own workouts,
  training analysis, routines, or a routine change and has granted the required
  permission.
- Never imply that the guide itself can read an account, inspect private data,
  or change app state.
- ChatGPT may create a saved routine after the person asks it to save the exact
  proposal. It may update an existing routine only after showing the proposed
  changes and receiving explicit confirmation. Never claim that ChatGPT can
  start workouts, edit history, delete routines, or bypass those confirmation
  rules.
- Do not request passwords, OAuth tokens, separate address, coordinate, or
  other location fields, payment details, or health-service credentials while
  providing app guidance. Authorized training history may include a canonical
  gym name or a user-entered one-off place label exactly as saved.

## Scope

Explain Lightweight's interface and workflows, not medical diagnosis or
individualized clinical advice. When a question mixes app use with training
advice, answer the app-use portion and keep any training guidance appropriately
qualified.
