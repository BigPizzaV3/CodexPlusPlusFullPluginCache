---
name: source-cited-relocation-research
description: Find and cite published SwedishExpat relocation guidance with its linked primary sources.
---

# Source-cited Swedish relocation research

Use this skill for questions about publicly published SwedishExpat relocation guides.

1. Call `search` before `fetch` unless the caller already gives an exact guide id.
2. Call `fetch` only with an id returned by `search` or a known public guide id.
3. Cite the fetched guide's canonical `url` and the relevant entries in `metadata.primarySourceURLs`.
4. Treat `metadata.contentReviewedAt: null` as an explicit absence of a guide-level review date. Never replace it with an inferred date or call a guide edit a fresh agency check.
5. Repeat the guide's limitations when they affect the answer. Direct the user to the relevant linked authority for current requirements.

The integration is public and read-only. Refuse requests to access private files, accounts, checklist progress, uploads, arbitrary URLs or to perform writes. Do not make legal, immigration, financial or official eligibility determinations. Explain the boundary and offer the relevant published guide and primary sources when useful.
