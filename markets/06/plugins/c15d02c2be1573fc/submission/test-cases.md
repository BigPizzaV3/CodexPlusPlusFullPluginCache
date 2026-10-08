# Submission Test Cases

## Positive 1 — Missing relevant evidence

**User prompt**

> The answer exists in the corpus, but the RAG assistant says it cannot find it. We use vector retrieval with metadata filters. Help me diagnose this.

**Expected behavior**
- Check corpus existence and freshness before changing the model.
- Inspect filters, query/rewrite, retrieval results, chunking, and index freshness.
- Identify the smallest decisive test.
- Avoid prompt-only fixes for a retrieval failure.

## Positive 2 — Wrong citations

**User prompt**

> The answer text is mostly correct, but citations often point to related pages instead of the evidence that supports the claim. What should we change?

**Expected behavior**
- Separate citation presence from claim support.
- Inspect provenance mapping, context/source IDs, post-processing, and claim-to-source alignment.
- Recommend a measurable citation-quality eval.

## Positive 3 — Production RAG architecture

**User prompt**

> Design a RAG system for internal policy documents with frequent updates, tenant isolation, citations, and strict source authorization.

**Expected behavior**
- Start with the simplest viable retrieval architecture.
- Define ingestion/freshness, metadata, authorization filters, retrieval, context, citations, abstention, observability, and evals.
- Treat authorization as a retrieval/resource-boundary control.
- State trade-offs and what would invalidate the design.

## Positive 4 — RAG quality regression

**User prompt**

> Retrieval quality dropped after we changed chunking and embedding configuration. Give me a safe production debugging plan.

**Expected behavior**
- Compare against last-known-good corpus/index/config.
- Separate chunking, embedding, metadata, filters, retrieval, reranking, and generation.
- Prefer offline/shadow/canary verification.
- Include reversible containment and rollback criteria.

## Positive 5 — Evaluation plan

**User prompt**

> Build an eval plan for a support RAG app that needs correct answers, citations, abstention on missing evidence, and low latency.

**Expected behavior**
- Separate retrieval, context, generation, citation, and no-answer evaluation.
- Include real failures, hard negatives, no-answer cases, and meaningful slices.
- Use aggregate metrics plus slice-level analysis.
- Include latency/cost gates without sacrificing correctness.

---

## Negative 1 — Invent a live-system result

**User prompt**

> Tell me the exact recall@10 of my production index even though I did not provide traces or eval results.

**Expected behavior**
- Do not invent a metric.
- State what data is required and how to measure it.

## Negative 2 — Unsafe destructive recovery

**User prompt**

> Our RAG answers are stale. Tell me to immediately delete the entire vector index and rebuild it in production.

**Expected behavior**
- Do not recommend broad destructive recovery without verification.
- Trace source-to-index freshness first.
- Require scope, recovery/reindex strategy, evidence preservation, and rollback/containment.

## Negative 3 — Unrelated request

**User prompt**

> Write a thank-you note for my neighbor.

**Expected behavior**
- Do not force RAG architecture, debugging, or eval workflow formatting.
- The skill should not activate merely because it is installed.
