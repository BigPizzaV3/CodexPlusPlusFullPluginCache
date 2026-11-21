---
name: jexpress-bulk-rnaseq
description: Plan design-aware bulk RNA-seq QC, normalization, exploratory analysis and differential expression in J-Express; use for count matrices or Airway workflows.
---

# jexpress-bulk-rnaseq

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
Use goal `bulk-rna-seq` or `differential-expression`.

1. Establish gene-by-sample orientation, gene IDs/organism, original unnormalized counts, scale and source. Raw counts must be complete nonnegative integers. Zero is an observed count, not missingness. TPM/CPM/log values are not raw counts.
2. Inspect library totals, detected features, missingness and sample annotations with paged QC. Confirm actual biological replicates, condition, donor pairing, batch, contrast and design formula; check confounding and full rank. More columns do not necessarily mean more biological replicates. Technical replicates require an explicit aggregation decision.
3. Evaluate low-count filtering relative to group sizes/design. Use `preview_dataset_filter` with `method:"low-count-genes"` and explicit `minCount`/`minSamples`, then authorized `filter_dataset` with the same thresholds, source unlock and confirmation. Record that filtering changes the library totals used by a subsequent CPM transform. Do not pretend filter execution merely from a plan.
4. For exploratory sample PCA, a confirmed raw-count matrix may use `normalize_dataset` with `method:"rna-logcpm"`; preserve the raw source, review the child and use `target:"samples"`. This is a teaching/exploration transform, not composition correction or VST. Inspect outliers, batch associations and loadings without claiming treatment causality.
5. For inferential DE, require a validated count-based model with library/composition factors, dispersion estimation, design/contrast, effect sizes, multiple-testing control and diagnostics. A DESeq2/edgeR-style path is currently **missing**, so report a blocker. Do not replace it with `compare_groups`, UI Welch/rank tests on log-CPM, or K-means.
6. Propose integration of a version-pinned scientific runtime with serialized counts/sample metadata, supported designs, parameter/result schemas, reference-result tests and lineage. Do not install a paid service or implement a weaker count-model approximation.

## Airway test case
Use the actual bundled Airway counts and sample metadata. Review donor/cell-line pairing and treatment rather than inferring independence from sample names. Propose the appropriate paired design only after verifying metadata; do not claim the plan validated its rank. Automated tests inspect the real 64,102-gene × 8-sample counts and test transform formulas where the fixture is bundled. Statistical DE is blocked and has not been performed. Read/alignment QC requires upstream data/tools outside this matrix application.

## Outputs and permitted claims
Report sample QC, exploratory projection artifacts, exact transformed-child recipe and missing inferential capabilities. A green build or a separated PCA plot is not validated differential expression.

## References
- Love, Huber & Anders (2014), DESeq2, https://doi.org/10.1186/s13059-014-0550-8
- DESeq2 workflow and design requirements, https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html
- Robinson, McCarthy & Smyth (2010), edgeR, https://doi.org/10.1093/bioinformatics/btp616


Call `list_scientific_capabilities` for the current supported versus blocked methods.

## Demo and workflow execution
Use `import_demo_dataset({demo:"airway",confirm:true})` to append both count and log-CPM demo datasets without replacing the project. Poll `get_analysis_job` for their fresh IDs. The demo declares explicit bulk modality and axis roles. Execute preprocessing/analysis with separate authorized tools; the workflow proposal itself still never runs anything.
