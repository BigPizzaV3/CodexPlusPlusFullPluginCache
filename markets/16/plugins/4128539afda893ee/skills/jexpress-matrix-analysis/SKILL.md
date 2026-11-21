---
name: jexpress-matrix-analysis
description: Analyze general numeric or legacy expression matrices with J-Express when asked for PCA, CA, clustering, heatmaps, profiles or descriptive group comparisons.
---

# jexpress-matrix-analysis

**Status: preview.** This procedure is still being validated against the J-Express tools and has not been scientifically validated.

## Shared tool procedure
1. Call `list_datasets`; select an explicit dataset ID, never assume the active dataset.
2. Call `list_scientific_capabilities` and `read_dataset_details`. Check the registry version, actual method status and connected tool schemas. A code-audited MCP path is not evidence of successful execution.
3. Call `inspect_dataset_quality` with `offset:0, limit:20`; follow `samples.nextOffset` for sample/cell summaries. A scan over 5 million values is explicitly incomplete. Metadata presence does not prove valid experimental design.
4. Call `propose_analysis_workflow` with the goal below. Supply optional `objective` as scientific context; the assistant chooses the controlled goal. This is a read-only proposal, not an LLM or an executor.
5. Explain prerequisites, blockers, parameter choices and human review gates. Never execute a blocked step or silently reinterpret a UI-only operation as an MCP method.
6. After user-authorized analysis, call `run_analysis` separately, poll `get_analysis_job`, require `status:completed` and an `analysisId`, then use `get_analysis_summary` and bounded `query_analysis_result` pages (`limit` ≤100). Record failed jobs as failed. Prefer saved results over `query_pca`, which recomputes on current values.
7. For a derived dataset, resolve its actual returned ID, inspect its new scale and QC, and re-plan. Dependencies do not pipe PCA scores or transformed values automatically into another tool. Report source ID, derived/analysis IDs, versions, parameters, validation, rationale and limits.

Do not use proposal text as an unlock or execution command. Matrix writes remain locked by default. `normalize_dataset` creates a child and requires a separately explicit `unlock_dataset`, `confirm:true`, then `lock_dataset` after the operation. Preserve source values and check the child's recipe. Existing authorization still applies; do not unlock without user authorization.

## Decision procedure
Use goal `exploration`, `clustering` or `correspondence` as appropriate. Route original embeddings and RNA counts to their dedicated procedures first.

- Establish observations versus variables, units, feature/sample roles, missingness and preprocessing. Legacy defaults are unconfirmed roles, not measured facts. Use bounded matrix/metadata slices if classification is unclear.
- For PCA, select `target:"samples"` or `"features"` explicitly. The current method centers variables, does not standardize, imputes column means and uses approximate power iteration. Request 2–3 components initially (tool range 2–15; rank may yield fewer). Review variance, loadings and outliers; changing component signs does not change PCA geometry. Decide whether variable scaling is warranted by units/noise, not visual separation.
- For K-means, choose Euclidean geometry, meaningful scaling and a justified editable k. Run separate seeds and compare memberships/empty clusters before interpretation. Each call uses one initialization. To cluster actual PCA scores, run and save PCA, then use `create_pca_score_dataset` with its analysis ID, explicit source unlock and `confirm:true`. Poll the returned job, inspect the child and run K-means with `target:"samples"` on that child. Old PCA records without input fingerprints must be rerun; a changed source is rejected. Do not describe raw-matrix K-means as clustering on PCA scores.
- For hierarchical clustering, choose `linkage:"upgma"` with `distance:"euclidean"` as a starting point only after scale review. Compare Pearson distance for profile shape; review constant profiles and missing overlaps. Supported alternatives are `single`, `complete`, `wpgma`, and `pearson-absolute`. The implementation uses pairwise-complete distances and caps at 10,000 observations with quadratic storage.
- For conventional CA, require a scientifically meaningful abundance/contingency table, no missing/negative values and strictly positive margins. The legacy implementation shifts negative values; the planner blocks that input. Never call a global offset standard CA. Inspect applied shift and inertia. Review memory for large opposite axes.
- Open profiles and heatmaps manually in J-Express; `list_views`/`show_view` can capture an already rendered view, not execute a method. State color scaling and units.
- `compare_groups` requires two existing group IDs on the same axis; outputs are descriptive means/SD/differences. For continuous-expression inferential tests, the UI has Welch/Student, rank and permutation tests with BH adjustment, but these are not a count-based RNA-seq model and have no dedicated MCP path.

## Validate and interpret
Check finite scores, explained variance/inertia, assignment counts and ID alignment. Check outlier and preprocessing sensitivity. PCA/clustering agreement on the same matrix is not independent validation; groups are exploratory hypotheses. Reject silent mean imputation in a scientifically unsuitable setting.

## Examples and evidence
Ask for `propose_analysis_workflow({datasetId:"<id>",goal:"clustering"})`; review scale/axis checks and choose the observation target before running. Automated tests cover signed/zero-margin CA rejection, proposal purity and missing-data/scale checks; the legacy browser project still needs end-to-end user validation.

## References
- Jolliffe & Cadima (2016), Principal component analysis: a review, https://doi.org/10.1098/rsta.2015.0202
- MacQueen (1967), Some methods for classification and analysis of multivariate observations, https://digicoll.lib.berkeley.edu/record/113015


Call `list_scientific_capabilities` for the current supported versus blocked methods.
