# Reporting and remediation standard

Read this reference for technical audits with multiple issues, combined reports, site batches, or a request for a prioritized action plan. Avoid long tables for a one-error focused check.

## Compact report structure

**Scope and coverage**
- Target: the supplied source or the exact requested and final URL. Note whether the scan used static HTML, user-supplied markup, or a sitemap sample.
- Performed: the exact MCP tool names and options that ran, plus notable limits (e.g., links disabled, 2-page sample).
- Coverage: report actual discovered/selected/audited/partial/failed counts and `next_page_offset` when applicable; do not infer unreported quantities.
- Status: pass / needs-attention / partial / failed, grounded in tool output. An unavailable validation service is **not** a pass.

**Findings by priority**

| Priority | Finding | Evidence | Proposed action | Verify by |
| --- | --- | --- | --- | --- |
| High / Medium / Low / Verify | Precise validator issue | URL + issue message + status or line only when returned | Smallest practical fix to source/canonical/metadata/markup | Focused re-run or manual check |

Use only rows supported by returned evidence. Avoid listing every duplicate of a site-wide finding; consolidate repeated issues and state how many affected pages were actually observed.

**Boundaries and next action**
- Separate conclusive validation failures from potential SEO improvements and checks excluded by the server.
- State remaining unknowns, including JavaScript content, linked stylesheet contents, authentication, user interactions, Search Console data, actual rankings, and indexing status.
- Recommend a bounded next check; never suggest unlimited automatic rescanning.

## Prioritization rubric

- **High:** confirmed issues that materially block access, break critical markup/links for the intended page, or represent systemic errors on multiple actually-audited pages. Do not label a risk high solely from speculation.
- **Medium:** confirmed technical or metadata deficiencies that degrade discoverability or experience but lack evidence of critical breakage.
- **Low:** hygiene, optional metadata, noncritical formatting, or informational warnings.
- **Verify:** inconclusive link responses, 403/429, intermittent errors, redirects without final-destination confirmation, sampled findings with unclear applicability, or external service failures. Use this instead of pretending certainty.

Severity returned by a validator is **not** automatically business priority. Keep severity and recommended priority distinguishable when useful. Ranking impact, traffic impact and fix effort are **not measurable** from these tools alone.

## Example phrasing

- Good: "The sitemap-based sample audited 2 of 2 selected pages. That is not a complete domain audit; remaining pages are untested."
- Good: "The URL returned HTTP 302 during link checking. The validator did not follow the redirect; verify whether the final destination is intended."
- Good: "The JSON-LD block parses successfully as JSON. Schema.org validity and rich-result eligibility were not evaluated."
- Good: "The CSS parser reported an error. This hosted tool checks syntax locally and does not perform full CSS standards conformance testing."
- Bad: "Your whole site is SEO optimized" based on a 2-page sample.
- Bad: "All accessibility checks passed" when the tool merely checked accessibility signals.
- Bad: "Your rich results are valid" based only on JSON parsing.
- Bad: "Your links are broken" merely because the server received 403 or 429.

## Response discipline

Write for the user's goal, not the plugin's marketing. Prioritize concrete changes with short evidence-linked rationales. Do not claim to have fixed, deployed, exported, continuously monitored, or revisited any resource unless a corresponding permitted tool call succeeded.
