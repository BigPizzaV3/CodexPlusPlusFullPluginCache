# Public Vitae tools

Retrieved: 2026-09-24T11:50:26.355571+00:00 from unauthenticated `tools/list` at `https://mcp.vitae.ai/mcp`.

This is a schema snapshot, not customer data. Live schemas and account permissions take precedence. Read [tools.json](tools.json) only when you need exact parameters. Descriptions can mention tools that are not exposed; check actual availability.

Read-only annotations do not describe every approval rule. Vitae enforces mutation permissions and approval requirements on the server. A pending approval is not a completed write.

| Tool | Read-only hint | Purpose |
| --- | --- | --- |
| `agent_status` | Yes | Check the configured Ask Vitae agent provider and model. |
| `ask_vitae` | No | Ask the Vitae recruiting agent to search candidates, jobs, clients, pipeline status, or draft workflows. Approval-gated actions are returned for review and are not executed directly by this tool. |
| `get_dashboard` | Yes | Get recruiting dashboard counters: pipeline stats, activity totals, key metrics. |
| `resolve_approval` | No | Approve or decline a pending Ask Vitae agent approval. Returns the resolved approval object. |
| `list_threads` | Yes | List recent Ask Vitae conversation threads for the authenticated user. |
| `list_archived_threads` | Yes | List archived Ask Vitae conversation threads for the authenticated user. |
| `create_thread` | No | Create a new non-destructive Ask Vitae conversation thread for the authenticated user. |
| `get_thread` | Yes | Get an agent conversation thread with its message history. |
| `pin_thread` | No | Pin or unpin an Ask Vitae thread. |
| `archive_thread` | No | Archive or restore an Ask Vitae thread. |
| `get_search_results` | Yes | Get paginated results for a completed candidate search. |
| `get_search_details` | Yes | Get full details for a candidate search: prompt, filters, metadata. |
| `get_search_history` | Yes | List past candidate searches with status and sort filters. |
| `list_signals` | Yes | List ranked Signals for the tenant. Supports status, tier, and pagination filters. |
| `list_signal_opportunities` | Yes | Deprecated: use list_signals. List ranked Signals for the tenant. Supports status, tier, and pagination filters. |
| `get_monitoring_profile` | Yes | Get the tenant's BD Signals monitoring profile: ICP context, triggers, discovery queries, source domains, and scan cadence. |
| `run_signal_scan` | No | Queue a BD Signals scan for the tenant. This is mutating and requires approval. |
| `update_signal_status` | No | Surface, dismiss, or promote a Signal. This is mutating and requires approval. |
| `create_job_draft` | No | Create a new job draft in Vitae. Returns the draft job object. The job stays in DRAFT status until published. |
| `update_job` | No | Patch fields on an existing Vitae job. |
| `delete_job` | No | Soft-delete a Vitae job. This archives the job; it can be restored later. |
| `list_jobs` | Yes | List jobs in Vitae with optional query filters. |
| `get_job` | Yes | Get a single job by ID. Optionally include applications or matches. |
| `create_client` | No | Create a new client in Vitae. |
| `update_client` | No | Patch fields on an existing Vitae client. |
| `churn_client` | No | Mark a Vitae client as churned. Sets stage to "churned". |
| `list_clients` | Yes | List clients in Vitae with optional query filters. |
| `get_client` | Yes | Get a single client by ID with full detail. |
| `client_portfolio` | Yes | Get client portfolio with stage/name filters. Richer view than list_clients. |
| `import_campaign_contacts` | No | Atomically create or reuse up to 500 Contacts by caller-stable external identity and attach them to an existing campaign. Requires explicit approval before any data changes. |
| `create_candidate` | No | Create a new candidate in Vitae. |
| `update_candidate` | No | Patch fields on an existing Vitae candidate. |
| `delete_candidate` | No | Delete a candidate from Vitae. Only the creator can delete. |
| `search_ats_candidates` | Yes | Search the candidates already saved in this account's Vitae ATS, by name, email, or skill. This is the DEFAULT candidate search: use it whenever the user asks about their own candidates, and FIRST whenever they name a candidate but you do not have their ID, then pass the returned id to get_candidate or get_candidate_resume. This searches existing records only; to source new people from outside the ATS use start_sourcing_search or search_sourcing_pool. |
| `get_candidate` | Yes | Get a single candidate by ID. |
| `get_candidate_resume` | Yes | Get resume URL/metadata for a candidate. |
| `search_skills` | Yes | Search skills by name (typeahead). Use when building candidate profiles. |
| `pipeline_summary` | Yes | Grouped active applications by pipeline stage. |
| `list_candidates_in_pipeline` | Yes | List candidates in a job pipeline across stages. |
| `list_applicants` | Yes | Deprecated. Use list_candidates_in_pipeline instead. List candidates in a job pipeline across stages. |
| `move_application` | No | Move a candidate application to a different pipeline stage on a job. |
| `move_applicant` | No | Deprecated. Use move_application instead. Move a candidate application to a different pipeline stage on a job. |
| `move_applications_bulk` | No | Move multiple candidate applications to a pipeline stage on a job in one call. Creates a pending approval; no applications move until the user approves. |
| `move_applicants_bulk` | No | Deprecated. Use move_applications_bulk instead. Move multiple candidate applications to a pipeline stage on a job in one call. Creates a pending approval; no applications move until the user approves. |
| `get_best_matches` | Yes | Get candidates matched to a job, ranked by their persisted match score (highest first; the same score the job's match reports show). Includes candidates who already applied, so the first row is the job's best-scored candidate overall. |
| `get_pipeline_board` | Yes | Get candidates in a pipeline stage across all jobs. |
| `count_applications` | Yes | Count applications across the WHOLE account (every job), grouped by pipeline stage, with optional stage, minimum match score, updated-since date, job, or client filters. Returns counts only, never candidate rows. Excludes archived applications. With a minimum score it counts only applications whose candidate has a match score at least that high (scored applications only). Use this for account-wide "how many applications" questions, e.g. "how many applications have a match score above 80%", "how many candidates are in Interview across all jobs". |
| `count_matches` | Yes | Count AI match scores across the WHOLE account (every job), optionally filtered by a score range, a job, or a client. Returns counts only, never candidate rows. Each match is one candidate scored against one job, so this includes AI-sourced candidates who have not applied; it counts scored candidates only (candidates never run through matching have no score). Also returns the total scored count so you can state the number honestly. Use for "how many match scores are above 80%" style questions; use count_applications when the question is specifically about applications. |
| `describe_query_schema` | Yes | List every entity and field you can query across the account, with the operators, group-by, and aggregate options for each. Call this FIRST when the user asks an analytical "how many / average / by X" question so you use real field names with query_records. No parameters. |
| `query_records` | Yes | Run an account-wide, org-scoped count or aggregate over an allow-listed entity (applications, candidates, jobs, clients, matches). Filter by field, group by a low-cardinality field, and aggregate (count by default; avg/min/max/sum on numeric fields like matches.score). Returns counts/aggregates only, never record rows. Call describe_query_schema first to see valid entities, fields, and operators. Prefer ONE query_records call with combined filters over several calls. |
| `save_view` | No | Save a query_records query (entity + filters + aggregate + groupBy) under a name so it can be re-run later as a reusable segment, e.g. "Interview candidates scored above 90". Creates a pending approval; nothing is saved until the user approves. Re-running a saved view always re-checks the current organization. |
| `list_saved_views` | Yes | List the saved query_records segments (name + entity + filters) the user has saved. No parameters. |
| `run_saved_view` | Yes | Re-run a saved query_records segment by name and return its current count/aggregate. Org-scoped every time it runs. |
| `list_candidate_pools` | Yes | List candidate pools/shortlists shared across the current organization. |
| `get_candidate_pool` | Yes | Get a candidate pool with its members. Supports filtering. |
| `create_candidate_pool` | No | Create a new saved candidate pool/shortlist after the user approves the pending action. |
| `update_candidate_pool` | No | Add/remove candidates from a pool, or rename it, after the user approves the pending action. |
| `delete_candidate_pool` | No | Delete a saved candidate pool after the user approves the pending action. |
| `get_interview_responses` | Yes | List all interview responses/notes for a job. |
| `get_interview_response` | Yes | Get interview notes/rating for a specific candidate on a job. |
| `submit_interview_response` | No | Submit recruiter interview notes and rating for a candidate on a job. |
| `export_report` | Yes | Export a Vitae report as CSV. Returns the download URL. Types: pipeline, jobs, sources, clients, activity, candidates. |
| `list_workflows` | Yes | List automation workflows in the tenant with their status and triggers. |
| `run_workflow` | No | Run an automation workflow by id once, queuing an execution. |
| `trigger_workflow` | No | Fire a workflow trigger by id (e.g. cand-created); runs every active workflow that starts with it. |
| `create_workflow_draft` | No | Create an approval-gated recruiting workflow draft. |
| `create_skill` | No | Add one or more skills to the organization skill library. |
| `create_question_set` | No | Create an interview question set/template. |
| `list_adaptive_dashboard_blocks` | Yes | List dashboard blocks the agent can compose into saved surfaces. |
| `save_adaptive_surface_config` | No | Save a user adaptive dashboard/report surface configuration. |
