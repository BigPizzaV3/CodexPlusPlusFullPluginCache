# Version 1 tools and permissions

Historical direct production clients accepted eleven tools. Actual-client checks
for this updated 0.1.1 candidate, including installed-plugin and model-host checks,
remain pending. The server's live `tools/list` schemas
are authoritative for the connected host. Account
identity comes from the grant; tools never accept a customer ID to select an
account. Every stateful request requires a caller-generated `request_id`.

| Tool | Purpose | Required permission |
| --- | --- | --- |
| `get_account_context` | Read connection limits, readiness, saved preferences, supported sites/countries and published templates. | Basic connection |
| `get_candidate_context` | Read permitted candidate facts and uncertainty; master-resume text is explicit. | `profile:read`; additional `resume:read` for `include_resume_text` |
| `search_jobs` | Start an owned search and return search/operation handles. | `jobs:search`, `jobs:read` |
| `list_search_results` | Page brief results within the specified owned search. | `jobs:read` |
| `get_job` | Read a stable owned job and its description quality. | `jobs:read` |
| `load_more_jobs` | Extend the exact search when the provider supports it. | `jobs:search`, `jobs:read` |
| `prepare_application` | Prepare one job, owned application or custom job; reuse existing packages. | `documents:generate` |
| `get_operation` | Read progress, action requirements and retry timing. | Permissions appropriate to the operation |
| `get_application_package` | Read readiness, delivered text/manifests and expiring PDF links. | `applications:read`, `documents:read` |
| `list_applications` | Read tracker summaries and document readiness. | `applications:read` |
| `record_application_outcome` | Persist an authorized external-outcome report and tracker update. | Optional `applications:write` |

Default consent does not include master-resume text or application-write access.
Normal customer generation entitlements apply. Replaying/reusing accepted work
and refreshing package links do not create another generation charge. Return
structured errors and server-directed retry hints; do not retry changed input
under an accepted request key.

Search results remain attached to their original search. Default result pages
contain ten brief jobs, maximum 25. Full job descriptions and resume text are
explicit reads. One active initial search per account and seven-day search
snapshot retention are version 1 limits; use current server readiness and retry guidance.

Clients present one numbered shortlist with the same numbers in summary and
detail views, retaining each displayed number's original `search_id`/`job_id`
mapping after subsequent searches. Numbered text with Markdown job links is the
default presentation; rich cards are optional. Ordinary search does not require
candidate-context or resume access. Ground personalized fit claims in conversation
facts confirmed for the connected candidate or explicitly attribute retrieved
candidate facts; keep other profiles separate.
Unknown skills, visa and work authorization must not silently become exclusion
criteria.

`list_search_results` and `get_job` expose `result_position`, the stable 1-based
position within the saved search. It is separate from the client's displayed
shortlist number when selecting a subset or changing display order.
`relevance_score` is null or an object with `value` (0–100), `scale: 100`,
`kind: "automated_relevance_hint"` and `candidate_fit_verified: false`. It is a
historical automated ranking hint, not a probability, confirmation of skills or
eligibility, or proof that a resume was used. The legacy `ats_score`, `ats_label`,
`ats_basis` and `ats_scoring_version` fields are null in MCP results; `ats_reasons`
is empty.

Operations use `queued`, `running`, `needs_input`, `succeeded`, `partial`, and
`failed`. A succeeded worker is not proof of package readiness. A complete
package needs two valid delivered PDFs. Missing artifacts, empty paths and
generation-error markers are not usable files. If one PDF is available, report
a partial package. Links are short-lived and bound to the owned grant, artifact
and revision; disconnect/scope removal invalidates existing links.

The runtime exposes each of these eleven operations with bounded schemas and
explicit `readOnlyHint`, `destructiveHint` and `openWorldHint` booleans. Public
metadata and results describe behavior without hidden instructions or promotion.
This bundle does not implement tools, an employer browser, submission, a
scheduler, email sending, document editing, or automatic purchases.
