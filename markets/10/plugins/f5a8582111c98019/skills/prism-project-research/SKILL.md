---
name: prism-project-research
description: Use when a user wants to find, synthesize, or organize source-backed knowledge in their authorized Prism Projects. Do not use for unrelated public-web research or actions Prism does not expose.
---

# Prism Project research

Use Prism as the user's authorized knowledge layer. Keep saved evidence, your interpretation, and any proposed change distinct.

## Workflow

1. Start with `get_prism_workspace_context`. Use `profile: "essentials"` when the Project is already known; use `profile: "full"` only when recent objects or richer routing context are needed.
2. If the target Project or object is ambiguous, use `resolve_prism_object` or `get_prism_task_context`. Ask the user only when the returned candidates do not establish a safe choice.
3. Call each operation directly using its advertised schema: `search_library` for search, `get_library_file_text` for source text, `patch_article_blocks` for draft revisions, and `create_project_monitor` for monitor creation. Each operation is exposed upfront with its own permissions and annotations.
4. Retrieve the smallest useful evidence set. Preserve source identifiers, titles, locations, dates, and links returned by Prism. If retrieval is unexpectedly empty, inspect `get_project_status` before concluding that no evidence exists.
5. For a user-requested private synthesis run, call `get_project_agent_availability` before `ask_project_agent`. Poll `get_project_agent_run` only at the returned cadence. Project Agent runs use existing authorized evidence and do not browse or edit Project content.
6. Lead with the answer. Then identify the strongest supporting evidence, separate inference from sourced facts, and state important gaps or conflicts.

## Durable changes

- Model runs and scenario comparisons save results. Use `run_research_model` and `compare_model_scenarios` with `library:write` and their preview/commit protocol. `propose_model_refresh` only returns candidates for review.
- YouTube transcript preview requires an existing Project folder. Omit `createFolderPath` or set it to false; use a write tool to create a folder.
- Make a durable Prism change only when the user asks for it and the current connection exposes the required write scope.
- Follow preview-and-commit instructions returned by the selected action. Reuse an idempotency key only for a retry of the same intent.
- Use `create_artifact` for a user-requested private table, chart, document, spreadsheet, or presentation. Do not imply that creating an artifact publishes it.
- Never bypass optimistic version checks, Project restrictions, confirmation requirements, or a missing host capability.

## Boundaries

- A skill does not grant access. Operate only on Projects and scopes authorized by the current Prism connection.
- Do not expose credentials, connection tokens, private identifiers, or inaccessible Project data.
- Do not publish, send email, submit an external form, place a trade, connect a brokerage, or permanently delete data unless an exact Prism tool exposes that action and the user explicitly requests it. Prism's submitted plugin does not expose brokerage execution or outbound email.
- Treat research deltas and writing revisions as proposals for human review. Do not describe a proposed change as already applied.
- If the host cannot call an authorized tool, follow the capability recovery guidance rather than inventing a substitute action.

## Successful result

Return a concise, source-backed answer or the identifiers and links for the private Prism objects created. Name unresolved access, indexing, or evidence gaps without guessing.
