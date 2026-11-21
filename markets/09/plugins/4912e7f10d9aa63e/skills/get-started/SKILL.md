---
name: get-started
description: Orient a new Linkeddit user. Use when someone first connects Linkeddit or asks what it can do, how to start, or where their data is.
---

# Getting started with Linkeddit

Linkeddit is demand and competitor intelligence. It measures where AI answer
engines recommend a competitor instead of the user, tracks competitor moves,
and provides keyword research. Every result comes from data
Linkeddit recorded, so cite what the tools return rather than filling gaps.

## First steps

1. Call `answer_projects_list` to see which domains the user already tracks.
   If there are none, offer to create one with `answer_project_create`, which
   needs the user's domain, brand name and the competitors they care about.
2. For a tracked project, call `answer_metrics_get` for the headline numbers
   and `answer_gaps_list` for the buying questions where an engine recommended
   someone else.
3. For competitors, call `list_competitor_monitors`, then
   `get_competitor_brief` for the one the user names.
4. For keyword ideas, call `keyword_autocomplete` with the user's seed query.

Saved-lead search, Reddit profiles and lead insights, lead pipeline execution
and results, raw Reddit JSON fetching, and DM drafts are currently disabled.
Do not attempt those workflows or infer an account permission problem from their absence.

## Before anything that spends credits or changes something

- Always call `answer_audit_estimate` and show the user the credit estimate
  before `answer_audit_start`. Start an audit only after the user agrees.
- Publishing, unpublishing, archiving and share links change what other
  people see. Confirm with the user before calling those tools.

## Access

A connected Linkeddit account with access to the requested tools is required.
If tools are unavailable, explain that access could not be established and ask
the user to check their connection and account permissions. Do not infer a
specific subscription or authentication failure from missing tools alone.
