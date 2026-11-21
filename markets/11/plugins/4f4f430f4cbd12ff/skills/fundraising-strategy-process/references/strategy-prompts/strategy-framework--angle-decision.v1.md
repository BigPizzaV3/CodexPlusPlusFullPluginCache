Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Case and strategic-angle decision

Help the user choose a defensible case and lead funding angle at
`case_funding_architecture`. Use the approved objective and organization frame,
reviewed benchmark diagnosis when applicable, project evidence, organizational
contribution, current use-of-funds version, readiness, capacity, and accepted
decisions.

First synthesize the case spine without smoothing over gaps:

- the need and intended outcome;
- what research and comparable projects support, including limitations;
- why this organization has a credible and distinctive role;
- what work, costs, implementation conditions, partners, and measures are
  required; and
- what is known, user-stated, inferred, recommended, or still missing.

Develop no more than three meaningfully different angles. Do not create
cosmetic variants. For each angle state:

- the core case and audience or payer type;
- organization/operator, program/pilot, or deliberate sequence logic;
- evidence supporting the angle and evidence that cannot travel to this case;
- what the organization would lead, adopt, adapt, add, measure, and test;
- workstream and source-type implications;
- readiness, access, capacity, and delivery constraints;
- material risks and decision criteria; and
- consequences for peers, opportunities, materials, and timing.

Recommend one lead angle or explicit sequence and explain why it best serves
the approved objective. Preserve credible alternatives and set-asides with
their reasons. Do not predict funder reactions or present a working program,
partner, budget, or outcome as approved reality.

If the current use of funds is missing, follow its required evidence policy and
ask for the smallest budget/scope judgment needed. If peer diagnosis, project
evidence, or organization readiness is too weak to support the choice, name the
gap and loop back only to the affected stage. Present the recommendation before
asking the user to accept, edit, sequence, or set it aside.

Return the typed decision proposal and only authorized section patches. The
stage gate remains open until the human decision and required use-of-funds
evidence are durably recorded. Return `no_change` when the accepted angle still
fits and no material evidence, scope, or decision has changed.
