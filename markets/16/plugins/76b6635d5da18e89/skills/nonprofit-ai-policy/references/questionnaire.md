# Policy questionnaire

Use ordinary language in conversation. These IDs are for the answer file. Reuse clear answers already supplied. Group related missing questions into the five exchanges below; do not repeat answered questions.

All fields below are required. Set `version` to `1`. Use an array for `dataScope`, `workflows`, and `vendorRequirements`, with at least one choice in each. Every other field is a single ID. `dataScope: ["none"]` cannot coexist with any other category. Only sensitive handling, autonomy, and disclosure support `undecided`; ask about other missing required choices. Do not infer policies from organization type.

## 1 Your organization

### What kind of nonprofit is this?
Answer field: `orgType`.

- `human-services`: Human services
- `health-research`: Health, disease, and research
- `education`: Education and youth
- `federated`: United Way or federated campaign
- `faith`: Faith-based
- `arts-culture`: Arts and culture
- `foundation`: Community or private foundation
- `association`: Association or membership
- `environment-animal`: Environment and animal welfare
- `other`: Other

## 2 The data AI may use

### Which data categories may approved AI tools use? Choose one or more categories, not actual records.
Answer field: `dataScope`.

- `public`: Public information only. Websites, 990s, news, published reports.
- `contact`: Constituent contact and relationship records. Names, addresses, notes, interactions.
- `giving`: Giving history and capacity indicators. Gifts, pledges, wealth screening results.
- `finance`: Financial and accounting records. General ledger, batches, reconciliations.
- `program`: Program, client, or patient data. Service records and outcomes tied to people.
- `hr`: Employee and volunteer records. Personnel files, applications, evaluations.
- `none`: No personal data of any kind. AI works only on content that names no one.

### How should sensitive categories be handled?
Answer field: `sensitiveHandling`.

- `excluded`: Kept out of AI tools entirely. Health, minors, financial account numbers, and similar categories never enter an AI tool.
- `approved-only`: Allowed only inside approved platforms. Permitted where a written agreement covers confidentiality, use, and deletion.
- `undecided`: Not decided yet. The draft starts with the strict rule until the board decides.

## 3 The work AI may assist

### Which work may AI assist? Choose one or more.
Answer field: `workflows`.

- `prospect-research`: Prospect research and donor briefings
- `donor-comms`: Drafting donor communications and acknowledgements
- `gift-processing`: Gift entry, coding, and receipting
- `reconciliation`: Reconciliation between fundraising and finance
- `reporting`: Reporting and board materials
- `grants`: Grant research and drafting
- `marketing`: Marketing and campaign content
- `constituent-support`: Constituent and donor support responses
- `internal-ops`: Internal work: notes, summaries, scheduling

### How much may AI do after the workflow is approved?
Answer field: `autonomy`.

- `draft-only`: Draft and recommend only. A person reviews and sends, posts, or saves everything AI prepares.
- `approve-routine`: Routine actions after approval. Low-risk actions may run once a person approves the workflow. Anything outbound or financial waits for individual approval.
- `undecided`: Not decided yet. The draft starts at draft-only and asks the board to decide on routine automation.

## 4 Who approves

### Which role approves a new AI tool or use?
Answer field: `approver`.

- `executive`: The Executive Director or CEO
- `ai-lead`: A designated AI lead on staff
- `committee`: A cross-functional staff committee
- `board-committee`: A board committee (finance, audit, or governance)

### Who reviews staff-prepared AI communications?
Answer field: `staffReview`.

- `relationship-owner`: The staff member who owns the relationship
- `supervisor`: A supervisor or second reviewer
- `tiered`: The owner for routine messages; a supervisor for major gifts and grants

## 5 Disclosure vendors and review

### When should AI assistance be disclosed?
Answer field: `disclosure`.

- `always`: Whenever AI helped produce a communication
- `material`: When AI produced the substance, not just grammar or formatting
- `on-request`: On request, and in public-facing content
- `undecided`: Not decided yet

### What must the organization obtain or confirm from a vendor before approval? Choose one or more. These are proposed requirements, not vendor findings.
Answer field: `vendorRequirements`.

- `no-training`: Our data is not used to train the vendor’s models
- `soc2`: A current SOC 2 report or an equivalent independent audit
- `named-models`: Named model providers and where processing happens
- `approval-controls`: Human approval controls on the actions AI can take
- `audit-log`: A record of AI actions and who approved them
- `dpa`: A data processing agreement and a subprocessor list
- `off-switch`: The ability to turn AI features off
- `export`: Export and deletion of our data when we leave

### How often should the policy be reviewed?
Answer field: `reviewCadence`.

- `quarterly`: Quarterly
- `semiannual`: Twice a year
- `annual`: Annually
- `on-change`: Annually, and whenever a new tool or data category is proposed

## Optional legacy inputs

Do not ask for revenue or staff role; neither changes the policy clauses. To import an existing website answer file, `revenueBand` and `authorRole` are accepted as optional validated fields. Use `--schema` for their allowed IDs. Omit them for a new plugin intake.

## Answer file

See [sample-answers.json](sample-answers.json) for a fictional complete example. Use only the documented fields and user-supplied choices. The file contains no organization name, contact details, vendor account information, or personal records.

The label "Public information only" describes the public data category. If selected alongside other categories, the draft also permits those separately selected categories. Clarify a user who says "public only" and also supplies personal-data choices. Sensitive-data selection affects the proposed organization policy; it never authorizes supplying sensitive records to this plugin.
