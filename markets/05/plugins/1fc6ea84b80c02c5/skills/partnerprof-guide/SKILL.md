---
name: partnerprof-guide
description: Guide users through PartnerProf task admissibility checks, task preparation, and explicitly confirmed execution within declared constraints and bounds.
---

Use this skill when a user asks whether PartnerProf fits a bounded task, wants to understand its input or result contract, wants to prepare a task, or explicitly confirms execution of a task that was just prepared and reviewed.

## Workflow

1. For every new PartnerProf request, you MUST call `partnerprof_knowledge_map` before deciding that the request fits or does not fit, before asking task-specific questions, and before constructing or validating any input. This is a mandatory bootstrap gate, not an optional source lookup. If the tool is unavailable, stop the PartnerProf workflow and say that suitability cannot yet be assessed; do not infer the map from memory. After reading it, explain whether the requested workflow fits PartnerProf and state that all conclusions apply only to the user's declared state, constraints, geometry, tolerances, and computation bounds.
2. Before constructing or preparing a task, call `partnerprof_task_manifest`. Use that returned contract as the authority for required fields, optional fields, and validation rules.
3. If the user wants to prepare a task, collect only the missing choices named by the authoritative task contract, build a complete proposed task, and show it to the user for review. Do not call `partnerprof_prepare_task` until the user has seen the complete proposal and the required inputs are available.
   For a large public Cirq RCS source specifically, use `partnerprof_prepare_rcs_source` only after showing the direct source URL and independently obtained SHA3-512. This source URL is input evidence, not service routing. Report both source and canonical circuit hashes returned by PartnerProf.
4. After preparation, report the prepared task reference, the summary returned by the tool, and its expiration or lifetime when provided. Do not run the task in the same step.
5. Call `partnerprof_run_prepared_task` only after the user gives an explicit confirmation to execute the exact prepared task. Pass the unchanged prepared task reference and confirmation value required by the tool. Never silently alter inputs, substitute a task, or rerun after an unresolved result.
6. After execution, call `partnerprof_result_interpretation_contract` when result interpretation is needed. Report the actual event, witness or unresolved status, declared bounds, and integrity evidence returned by the service. Explain any limitations in plain language.

## Boundaries

- Treat the declared computation slice as the full scope of the result. An unresolved result does not prove global impossibility outside the declared bounds.
- Do not claim scientific truth, global optimality, physical proof, legal conclusions, or safety certification.
- Do not request, accept, or forward API keys, passwords, MFA codes, private matrices, private tenant data, or login credentials.
- MCP and API endpoint URLs are installation and navigation metadata managed by the plugin. They are never requester input. Do not ask the user for an endpoint, API URL, host, callback URL, webhook URL, or Challenge Base URL.
- The one exception in name only is `source_url` for `partnerprof_prepare_rcs_source`: it identifies the public circuit file being certified, never the PartnerProf service. It must match the current allow-list and must be paired with an independently known SHA3-512.
- Fields such as `endpoint` or `next.endpoint` returned by a tool tell the plugin which registered route follows. Never copy them into `task_manifest` and never present them as a missing user choice.
- Do not use this skill for uploads, private matrix retrieval, third-party transactions, or unrelated writing and productivity requests.
- If required inputs are missing or ambiguous, ask for the missing choice before preparing or running anything.
- Never claim that a request cannot be represented by PartnerProf until the current `partnerprof_knowledge_map` has been read in that conversation.
- Keep preparation and execution separate. A request to explain, draft, or review a task is not permission to execute it.

## Response requirements

Use the tool responses as the source of truth. Keep the user-facing explanation concise but include the selected bounds, relevant constraints, status, and the practical limit of the result. When a tool is unavailable or returns an error, describe the error without inventing a computation result and suggest the next safe step.
