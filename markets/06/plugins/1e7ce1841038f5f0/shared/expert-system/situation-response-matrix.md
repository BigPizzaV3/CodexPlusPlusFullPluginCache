# Situation response matrix

| Situation | Required response |
|---|---|
| External factual claim or search result is material | Route verification through `$control-deep-research`; only evidence-gated claims may be stated as facts. |
| Reliable current evidence is absent or contradictory | Report `UNKNOWN`, `UNVERIFIED`, or `DISPUTED`; do not complete the answer from plausibility or user preference. |
| Controlled sources conflict | Class 1 stop; do not choose a winner without authority. |
| Specification passes but outcome is poor | `FAIL`; diagnose specification, representation, implementation, or acceptance defect. |
| Representation cannot reach the target | Stop detailed production and run representation review or proof. |
| Missing bounded visual microdetail | Class 2 only when the role and bounds are explicit. |
| Product, brand, governance, or architecture choice missing | `OWNER_DECISION_REQUIRED`. |
| Build fails | Route to defect diagnosis; preserve evidence. |
| Regression appears | Isolate, repair or rollback, then re-run affected gates. |
| New dependency or tool is required | Classify authority; do not introduce it silently. |
| Performance fix changes visible design | Trade-off review; Class 1 when approved outcome changes. |
| Responsive implementation fails | Use an approved fallback or stop for decision. |
| Metrics pass but perception fails | Overall `FAIL`. |
| Visual quality passes but accessibility fails | Overall `FAIL`. |
| Legacy element is stronger than replacement | Run salvage review before deletion or rebuild. |
| Better technical solution emerges | Classify decision and verify compatibility before adoption. |
| Unknown case | Determine authority class, evidence, reversibility, and reviewer before acting. |
