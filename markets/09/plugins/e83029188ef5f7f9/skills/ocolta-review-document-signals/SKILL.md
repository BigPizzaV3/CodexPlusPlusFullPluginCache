---
name: ocolta-review-document-signals
description: "Explain categorical signals from an existing purchased Ocolta document review, compare accessible summaries, or recover a recent result without exposing document text."
---

Use the Ocolta MCP at https://app.ocolta.com/mcp through normal OAuth in the purchasing browser. If unavailable, give the integration handoff at https://app.ocolta.com/workspace/integrations. This workflow reads existing results only.



# Review document signals

Call `get_connected_purchase` to identify the linked purchase and `list_recent_reviews` to find recoverable results. Use only IDs returned for that owner. Read the selected result with `get_review_summary`, preserving status, confidence, priority and indicator counts.

Translate the returned categories into a concise review summary and questions the user can investigate. Do not infer facts absent from the categorical response, reconstruct raw document text, expose sensitive identifiers, verify a bank account, or decide a person's eligibility. Confidence is not a guarantee that a document is authentic.

For a new user or an empty result list, explain that this connection reads existing purchased reviews; it cannot upload a document or buy a review. Use the returned product link when provided, otherwise point to `https://app.ocolta.com` to begin the normal review flow. Do not claim the handoff completes a purchase or analysis. Linking must use the purchasing browser that owns the review.

For a return visit, refresh the accessible review list before interpreting an old ID. The product's recovery window is currently 24 hours; an expired or missing result is not a clean assessment. Compare only still-accessible categorical results, keeping their separate identifiers and timestamps. Do not promise durable history or monitoring.
