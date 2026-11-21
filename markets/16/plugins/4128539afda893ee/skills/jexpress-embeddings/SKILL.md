---
name: jexpress-embeddings
description: Explore J-Express original embedding vectors when asked for nearest neighbors, semantic search, PCA/UMAP, concept directions or placement of new text.
---

# jexpress-embeddings

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
Use goal `embedding` for exploration or `semantic-search` for text retrieval.

- Confirm objects in rows, dimensions in columns, original source observations and embedding model/revision, pooling, normalization and preprocessing. A 384-column matrix alone is not MiniLM compatibility. Reject projected coordinates masquerading as original embeddings.
- Call `find_embedding_neighbors` with an existing `queryId` and `limit:10`. It uses all original dimensions and cosine similarity. The query must be complete and nonzero; incomplete/zero candidates are excluded and counted. This tool does not generate a text embedding.
- Use PCA to inspect major variance; it centers but does not L2-normalize vectors. PCA/K-means Euclidean geometry and cosine retrieval differ unless normalization conditions justify equivalence. Do not silently z-score embedding dimensions.
- Use `run_scientific_analysis` with `operation:"umap"`, `"concepts"` or `"projection-quality"`. Each returns a job ID; poll `get_analysis_job`, then read saved results through `get_analysis_summary` and `query_analysis_result`. Concepts require explicit disjoint `groupAIds`/`groupBIds` with at least two examples each. Projection quality requires `sourceAnalysisId` of a current fingerprinted PCA/UMAP on the same objects; old or stale results are rejected. `show_view` remains image capture, not computation.
- Use `search_embedding_text` for compatible local MiniLM search. Its job saves ranked IDs/similarities and a query digest, not the query text. Retain the request text separately for exact reproduction. Use `add_text_embedding` to create a child containing one newly encoded sentence; source unlock and `confirm:true` are required. Both check the pinned model/revision and reference cosine ≥0.97. Missing model assets require explicit `allowModelDownload:true`; no paid inference API or query text is sent to model hosting. The shared encoder uses mean pooling, L2 normalization and a 256-token limit, matching the model card. Do not download models without the user's authorization.
- Compare projected neighborhoods to original-vector neighbors at multiple k and seeds. Neighborhood preservation samples 128 reference objects above 1,000 objects; report that as an estimate. The UMAP worker caps at 5,000 complete vectors; a UI workflow can impose a smaller limit. 2D distance and density are not original-space semantic distance/density.
- Define concept directions with representative positive/negative examples, independent holdouts, sensitivity and confounder checks; never treat an appealing axis label as validation.
- For new text, use the compatible local model path with matching revision, pooling and preprocessing. Do not invent embedding vectors or substitute another model. Browser inference may download model assets; do not add a paid remote service or send data remotely without authorization.

## Validation and evidence
Use the MiniLM text-embedding demo for real 384D model provenance, or the synthetic embedding demo for a small fixture. Compare returned neighbors to source observations and exact cosine calculations; check exclusions and ambiguous examples. Automated tests exercise the bundled fixture and full-vector neighbor path; the new encoder guards are smoke-tested without a model download; actual browser model loading/text insertion and semantic interpretation remain manual.

## References
- Reimers & Gurevych (2019), Sentence-BERT, https://aclanthology.org/D19-1410/
- McInnes, Healy & Melville (2018/2020), UMAP, https://arxiv.org/abs/1802.03426
- Venna & Kaski (2001), Neighborhood preservation in nonlinear projection methods, https://research.aalto.fi/en/publications/neighborhood-preservation-in-nonlinear-projection-methods-an-expe/


Call `list_scientific_capabilities` for the current supported versus blocked methods.

## Load a demo without replacing the workspace
Call `list_demo_datasets`, then authorized `import_demo_dataset({demo:"text-embeddings",confirm:true})`. Poll the job for fresh dataset IDs. Existing datasets, analyses, selections and the active view are preserved; never use the old replace-workspace demo UI for an autonomous MCP test.
