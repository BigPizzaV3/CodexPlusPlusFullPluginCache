# FifthRow platform links and identifiers

LCM stands for Large Consulting Model, FifthRow's consulting-agent platform.

Use the canonical URL returned by the tool for the exact resource the user wants. Keep its configured environment and company origin. Never replace a detail link with the dashboard, strip a company subdomain, guess a hostname, or turn an API endpoint into a UI link. If no supported detail URL is available, explain that and present the tool result; do not invent a link.

| Resource | Platform path | Correct identifier and returned field |
| --- | --- | --- |
| Reusable App definition | `/apps/template/{template_slug}/detail` | The actual `slug` returned by `search_catalog`/`get_app`; use their `url`. The template UUID and revision ID are tool arguments, not this route's slug. |
| One App execution and result | `/apps/{app_execution_id}` | The execution UUID from `run_app`/`get_app_run`/history; use `result_url` or `execution.link`. Never use the template UUID here. |
| One standalone Flow execution | `/flows/{execution_id}` | Exact Flow invocation UUID and `execution_type="flow"`; use the returned result URL. |
| App Autopilot schedule | `/autopilots/apps/{autopilot_id}` | The recurring schedule UUID; use `autopilot_url` or the schedule item's `url`. |
| Flow or Skill Autopilot schedule | `/autopilots/flows/{autopilot_id}` | The platform library routes non-App schedules here. Use the schedule UUID, never its execution UUID. |
| Existing Answers conversation | `/answers/{conversation_id}` | A Pathfinder conversation UUID. LCM `answer_execution_id`, stored SearchAnswer IDs and App/Flow IDs cannot be substituted. LCM Answers currently returns no compatible conversation detail URL. |
| App report view | `/report/apps/{app_execution_id}` | One App execution, only when the requested report URL is returned or verified. Prefer the canonical execution result link by default. |

For a new App run, tools require `app_template_id`, the returned non-empty `app_template_revision_id` when available, and declared variables. For reading results, tools require `app_execution_id` or `execution_id` with the exact `execution_type`. An App revision is never a template slug or execution UUID. `source_app_execution_id` repeats saved inputs through `run_app`; it does not identify the reusable template.

Autopilot responses distinguish **schedule** (`autopilot_id`, `autopilot_url`) from **this invocation** (`execution_id`, `execution_type`, `result_url`). Link the schedule when discussing settings/frequency, and link this execution when discussing progress/findings. For Skill results, use the returned output reference; no standalone Skill execution page is established by this contract.

An App Builder `job_id` is a background job identifier, not a platform page ID. On completion inspect the returned template or `get_app` and link its actual template URL. Before completion show the status in text without fabricating a Builder page.

The MCP card's `ui://lcm/workbench/...` URI and relative host deep links such as `/runs/{id}` are internal card navigation. They are not FifthRow website URLs and must never be copied into platform links.

Include important status and exact links in the normal chat response even when the host hides cards inside a trace. For a background run, say what is running and that you are waiting for its result. Update the outcome when the host delivers completion. Link labels should say what opens: App workflow, App result or Autopilot schedule.
