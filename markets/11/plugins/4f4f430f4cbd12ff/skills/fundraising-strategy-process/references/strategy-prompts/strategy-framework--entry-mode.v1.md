Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Entry-mode interpretation

Classify the user's job into exactly one primary framework entry mode:

- `full_fundraising_strategy`: an end-to-end position, case, routes,
  priorities, roadmap, and management rhythm;
- `landscape_or_benchmark`: a fair comparison or mapped landscape supporting a
  defined decision;
- `prospect_relationship_expansion`: current, lapsed, covered, and genuinely
  new opportunities and paths in;
- `program_project_case`: a fundable program, initiative, or project grounded
  in analogs, evidence, budget, outcomes, and payer precedent;
- `live_opportunity_proposal`: work backward from a real opportunity's current
  criteria, limits, deadline, and application requirements; or
- `execution_or_refresh`: turn an existing strategy into owned goals, account
  plans, materials, cadence, stewardship, and learning.

Choose the mode from the decision and useful output the user needs, not from
which data happens to be available. If the request spans modes, select the
dominant decision as primary and record the other work as a dependency or
downstream seed; do not invent a hybrid ID.

Normalize the brief into: focal entity; organization/program/initiative/project
scope; intended decision; audience; useful output; definition of success; use
of funds; population and geography; time horizon or deadline; constraints;
exclusions; and known sharing boundaries. Preserve the user's language where
it carries judgment. Do not silently turn an aspiration into a commitment or a
provisional budget into an approved amount.

Use the selected mode's canonical natural start stage and default maturity.
For every upstream dependency, classify the available durable receipt as
usable, missing, stale, conflicting, or invalidated. A later-stage entry may
skip replaying completed work, but it may not hide a current-position, peer,
project-evidence, case, qualification, or access dependency that could change
the requested decision.

Ask a focused question only when ambiguity in entity, scope, decision,
audience, or success definition would change the entry mode, start stage, or
first useful output. Otherwise choose the best-supported interpretation,
label the uncertainty, and propose confirmation. Return the typed entry brief,
dependency checklist, required human decisions, and smallest useful next
artifact requested by the caller schema.
