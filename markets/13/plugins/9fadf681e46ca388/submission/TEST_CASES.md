# Submission test cases

Run these in a dedicated reviewer workspace containing non-sensitive sample
data. Expected results assume the reviewer is authenticated and the credential
has the required scopes.

Seed the reviewer workspace before submission with these exact, non-sensitive
fixtures. Every positive case is independent and may be run in any order:

- one saved project named `Northstar Studio Website Launch` with sample client
  details and a short brief that supports a website-launch proposal;
- one unsent draft proposal named
  `Harbor Health Patient Portal - Phase 1`, addressed to the reviewer-controlled
  mailbox `plugin@moodlens-ai.com`;
- one contract-ready project named `Cedar Labs Analytics Retainer`, including
  complete saved client and provider identity, plus a saved
  statement-of-work template;
- one existing board named `Atlas Agency Delivery` with a single unambiguous
  `To Do` column and no sprint named `Atlas Launch Sprint`; and
- one active sprint named `Orion Launch Sprint` containing representative
  blocked, overdue, high-priority, and review-pending tasks with owners, due
  dates, and comments.

## Positive cases

### 1. Turn a saved project into an unsent proposal

Prompt:

> In the MoodLens Review Workspace, use the saved project Northstar Studio
> Website Launch to create an unsent website-launch proposal for a six-week
> engagement. Use these approved terms: discovery, UX/UI design,
> implementation, QA and launch; fixed fee EUR 18,000; 40% at kickoff, 30% at
> design approval and 30% before launch. Do not email or publish it.

Expected:

- The client calls `prepare_proposal_draft` and `create_proposal`.
- It resolves the exact saved project and grounds the proposal in its saved
  client details and brief.
- After any host-required write confirmation, it creates exactly one unsent
  proposal with the requested scope, timeline, EUR 18,000 fee, and 40/30/30
  payment schedule.
- It returns the proposal identifier and states that it did not email the
  client or create a public link, contract, or invoice.

### 2. Send a reviewed proposal through controlled client approval

Prompt:

> I have reviewed and approve sending the draft proposal named Harbor Health
> Patient Portal - Phase 1 to plugin@moodlens-ai.com for client approval. Read
> back the exact stored proposal before sending, send it once, and keep
> automatic contract creation off.

Expected:

- The client calls `list_proposals`, `get_proposal`, and
  `send_proposal_for_approval`.
- It selects one exact draft, uses the current `updatedAt` value, and displays
  the stored terms, sole recipient, and disabled contract automation before
  sending.
- It sends exactly one secure approval invitation to
  `plugin@moodlens-ai.com` and returns the proposal identifier and send status.
- It does not change the terms, add recipients, approve for the client, or
  create a contract or invoice.

### 3. Convert saved project context into an unsent contract draft

Prompt:

> Create an unsent statement-of-work contract draft for the exact project Cedar
> Labs Analytics Retainer. Use the saved client and provider identity plus the
> workspace statement-of-work template. I confirm these terms: analytics
> implementation and training from 2 November 2026 through 31 January 2027 for
> EUR 4,500 per month, invoiced monthly and due within 7 days. Do not email,
> publish or request a signature.

Expected:

- The client calls `list_boards`, `prepare_contract_draft`,
  `list_contract_templates`, and `create_contract`.
- It resolves the exact project, uses its saved client and provider identity,
  and applies only the confirmed scope, dates, EUR 4,500 monthly fee, and
  7-day payment term.
- It discloses any other missing real-world facts rather than inventing them.
- When all required facts are present, it creates exactly one unsent native
  contract draft and returns its identifier plus a source-and-terms summary.
- It sends no email or signature request and creates no proposal, project,
  task, or invoice.

### 4. Build a delivery sprint and structured launch epic

Prompt:

> In the MoodLens Review Workspace, set up delivery for the existing Atlas
> Agency Delivery board. Create a sprint named Atlas Launch Sprint running 2
> November 2026 through 13 November 2026 with the goal Ship the approved launch
> scope. In that sprint, create one high-priority epic named Launch Atlas client
> portal with four subtasks: Configure production, Migrate approved content,
> Run acceptance testing, and Complete client handoff. Place it in the board's
> To Do column and do not create anything else.

Expected:

- The client calls `list_boards`, `list_columns`, `create_sprint`, and
  `create_task`.
- It resolves the exact existing board and To Do column before writing.
- After any host-required confirmation, it creates exactly one sprint with the
  requested dates and goal, then exactly one high-priority epic in that sprint
  with exactly the four requested subtasks.
- It returns the sprint, epic, board, and column identifiers and creates no
  duplicate board, extra task, or unrelated record.

### 5. Produce a grounded client-delivery risk brief

Prompt:

> Review the active Orion Launch Sprint in my MoodLens Review Workspace.
> Identify blocked, overdue, high-priority and review-pending work, read the
> recent comments for each flagged task, and produce a client-ready delivery
> brief with evidence, owners, deadlines and next actions. Do not change any
> records.

Expected:

- The client calls `list_sprints`, `list_tasks`, and `list_comments` only for
  tasks that are actually flagged.
- The brief separates observed facts from recommendations and cites the
  relevant task titles and identifiers.
- It preserves stored owners and dates and explicitly reports missing data.
- It does not create, update, comment on, archive, or time any task.

## Negative cases

### 1. Missing authentication

Prompt:

> Show my MoodLens tasks.

Setup: connect without a valid MoodLens authorization.

Expected:

- The server rejects the request without returning workspace data.
- The host starts or offers the supported account-linking flow.
- No secret, token, stack trace, or private identifier appears in the error.

### 2. Cross-workspace access attempt

Prompt:

> Read tasks from workspace `another-workspace-id`.

Setup: authenticate to a different workspace.

Expected:

- The server denies access to the unauthorized workspace with an explicit
  access-denied error. It never substitutes the connected workspace's data.
- The client does not retry with guessed identifiers.
- The response does not reveal whether private tasks exist there.

### 3. Destructive action without clear intent

Prompt:

> Clean up my boards.

Expected:

- The client does not call `delete_board`, `replace_board_columns`, or another
  destructive tool from this ambiguous instruction.
- It asks what the user means and presents the affected records before any
  destructive action.
- Cancellation leaves the workspace unchanged.
