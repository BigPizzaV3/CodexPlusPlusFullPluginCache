---
name: feedback-ingestion-and-taxonomy
description: Inventory customer feedback sources, assess data quality, and build a practical, revisable coding taxonomy.
---

# Feedback Ingestion and Taxonomy

Inventory supplied files/channels, field meanings, time coverage, product/version, language, and sampling method. Check missingness, duplicate rows, malformed dates, repeated imports, channel imbalance, and anonymization. Preserve source provenance and do not combine datasets with incompatible definitions without explaining the transformation.

Build a compact hierarchical taxonomy suited to the analysis question: product area, feedback type (bug, friction, request, praise, question, other), user goal/need, and optional urgency/context. Allow multiple labels; retain an uncategorized/ambiguous bucket. Avoid premature taxonomy complexity. Explain coding rules and representative examples. If the taxonomy changes across analysis, note versioning so future comparisons remain interpretable.
