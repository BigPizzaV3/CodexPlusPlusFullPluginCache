
# Evidence Ledger and Claim Graph

Every material conclusion must be represented in both the evidence ledger and the claim graph before a deep workflow can pass.

An evidence record identifies a source and a bounded locator. A claim record classifies the statement and links it to evidence, assumptions, calculations, counterevidence, definitions, model lines, and downstream conclusions. Edges must use an allowed relation: supports, contradicts, qualifies, derived_from, assumes, defines, or supersedes.

Rules:

1. A reported fact needs at least one direct evidence edge.
2. A management claim must not be relabeled as a reported fact merely because it appears in a filing or call.
3. An analyst calculation needs reproducible inputs, formula or script name, units, and output.
4. A judgment must identify the supporting claims, strongest counterclaim, and the observation that would falsify it.
5. A material claim with unresolved contradictory evidence cannot be marked verified; use disputed or unresolved.
6. Do not cite a source that merely mentions the topic. The bounded source passage must entail the claim at the stated precision.
7. One source copied by multiple publishers remains one evidence lineage, not independent corroboration.
