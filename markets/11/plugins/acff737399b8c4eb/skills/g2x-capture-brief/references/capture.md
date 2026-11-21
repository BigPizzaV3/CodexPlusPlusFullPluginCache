# Bid/No-Bid and capture

Keep three outcomes separate: extracting what the solicitation requires, assessing the company's fit, and tracking how a response satisfies each requirement. Do not label one as another.

By default, do the analysis in the user's own agent from the documents you read in full. Use G2X-hosted analysis only when the user chooses it. Prefer an existing completed run. Reading must not quietly become paid processing: check what a tool does before starting it. The capture tools below start paid work on G2X. Results are scoped to the user's account and its proposal workspaces.

For a hosted run, keep the run and workspace IDs and the selected document IDs. Poll the same run instead of starting another. A timeout alone does not prove failure. Never mark a requirement compliant because it was extracted. The bid decision stays with the user.

### `g2x_prepare_opportunity_documents`

Open or create the user's G2X workspace for an opportunity and prepare its source documents for analysis, then list them. This is a deliberate action: it may start reading documents that are not on file yet and the workspace's requirements extraction.

- Inputs: `opportunity_id` (required).
- Output: the workspace's document rows. A new workspace is named as new; a reused workspace starts nothing new. To list what is on file without starting anything, use the document listing in [Opportunities and documents](opportunities.md) instead.
- Plan: Starter and up. Write. On the research endpoint: no.
- Example: `{"opportunity_id": "<id from a search result>"}`

### `g2x_shred_opportunity`

Start a G2X requirements extraction over the opportunity's full document set: solicitation, attachments and amendments. Choose documents deliberately; include instructions and amendments as well as the statement of work.

- Inputs: `opportunity_id` (required); `selected_attachment_ids` (source attachment identifiers to read, up to 200; omit to read the default source set; giving them replaces the workspace's saved selection).
- Output: a run identifier. A run already in flight is joined, not duplicated. The completed run holds typed, cited requirements with family, kind and source location. Read it back with the run tool below.
- Plan: Starter and up. Write. On the research endpoint: no.
- Example: `{"opportunity_id": "<opportunity id>"}`

### `g2x_qualify_opportunity`

Start G2X's quick Bid/No-Bid analysis of an opportunity against a company profile.

- Inputs: exactly one of `opportunity_id` or `workspace_id` (required); `profile_id` (company profile to qualify against; omit for the account's default profile; giving one replaces the workspace's selected profile); `name` (optional run name shown in G2X).
- Output: a run identifier. A profile missing fields answers `blocked` instead of running; report what is missing. The completed analysis holds a go, go-with-risks or no-go recommendation, overall and dimension scores, blockers, risks, advantages, gaps, possible partners and what could change the answer.
- Plan: Starter and up. Write. On the research endpoint: no.
- Example: `{"opportunity_id": "<opportunity id>"}`

### `g2x_get_analysis_run`

Report a capture run's status and, once it completes, its results. It never starts a run. Poll it at a sensible interval with a bounded wait, and resume the same run after a slow response.

- Inputs: exactly one of `run_id` (an extraction or qualification run id) or `opportunity_id` (lists earlier runs on that opportunity, newest first, without starting one).
- Output: run status, and on completion the extracted requirements, compliance totals, or the Bid/No-Bid verdict with dimensions, blockers, risks and evidence. With `opportunity_id`, the list of earlier runs. If there is no earlier analysis, it says so; starting one is a separate, explicit step.
- Plan: all plans. Read only. Checking a run does not spend a capture slot. On the research endpoint: no.
- Example: `{"run_id": "<run id from the start call>"}`

### `g2x_compliance_matrix`

Read a stored compliance matrix from a completed qualification or supported compliance run. Requirements extraction produces cited requirements, not a compliance matrix; read extraction results with `g2x_get_analysis_run` and never send an extraction run ID to this reader. The matrix reader never creates a matrix or starts analysis. Use the exact supported run or workspace ID a previous call returned, and preserve a genuine no-matrix result.

- Inputs: `run_id` (a compliance or qualification run id), or `workspace_id` (reads its latest matrix). Give at least one.
- Output: one row per extracted requirement with its status (met, partial, missing), the evidence it needs, citations to the source documents and which proposal sections cover it. Extracted rows are not evidence that the company complies.
- Plan: all plans. Read only. On the research endpoint: no.
- Example: `{"run_id": "<completed qualification or compliance run id>"}`

A useful requirements output keeps each requirement, whether it is mandatory or desirable where the source says, its citation and any open interpretation. When you build a brief or matrix in the agent, keep source document and version IDs with it. Updating a pipeline stage or CRM record after analysis is a separate requested action.
