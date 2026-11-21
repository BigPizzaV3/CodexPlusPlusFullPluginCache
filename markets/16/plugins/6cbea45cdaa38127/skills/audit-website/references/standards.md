# Website audit standards and evidence boundaries

Verified against the primary sources linked below on **2026-10-03**. This is a versioned baseline for reusable client audits, not a promise that documentation, thresholds, search features, or browser behavior will stay unchanged. Recheck the relevant official source when starting an audit, especially when the source version or a reported tool behavior differs. Record the verification date and tool versions in the report. If live verification is unavailable, disclose that this baseline was used.

## Performance and Core Web Vitals

The current Core Web Vitals are LCP, INP, and CLS. Evaluate field metrics at the 75th percentile and keep mobile and desktop separate. Use these threshold boundaries exactly:

| Metric | Good | Needs improvement | Poor |
|---|---:|---:|---:|
| LCP | <= 2,500 ms | > 2,500 and <= 4,000 ms | > 4,000 ms |
| INP | <= 200 ms | > 200 and <= 500 ms | > 500 ms |
| CLS | <= 0.10 | > 0.10 and <= 0.25 | > 0.25 |

Source: [Google web.dev — Web Vitals](https://web.dev/articles/vitals), [threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds).

PageSpeed Insights field data uses a trailing 28-day CrUX collection period. Record whether each result describes the tested URL or an origin fallback; origin data cannot establish the experience of an individual page. Insufficient samples mean unavailable evidence, not a pass or failure. PSI documents a provider-specific exception: when INP has insufficient data, good LCP and CLS can still yield a passing assessment. Reproduce that provider result, disclose missing INP, and do not describe all three metrics as verified. If either LCP or CLS is unavailable, PSI cannot assess the aggregation. Record the exact collection period returned rather than inventing dates. [Google — About PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about).

Lab diagnostics and field measurements answer different questions. A Lighthouse performance score is neither a field CWV pass nor a ranking score. TBT helps investigate blocking work but is not INP. Page-load CLS may miss shifts later in a visit. Preserve metric units, test timestamp, tool/version, viewport or device strategy, throttling and location when available. Separate repeated lab runs from historical field data; never average mobile, desktop, lab, and field into a metric. Differences warrant investigation rather than selecting whichever number looks better. [Google web.dev — Lab and field data differences](https://web.dev/articles/lab-and-field-data-differences).

## Technical SEO and on-page SEO

Use successful public retrieval, status/redirect evidence, crawl directives, internal linking, metadata, and rendered content to assess discoverability. Crawlability, indexability, actual indexing, ranking, and traffic are distinct. A public page audit alone does not establish Google-selected canonicals, Search Console status, penalties, search demand, backlinks, or ranking changes. Request relevant client exports when needed; mark the limitation otherwise.

Avoid universal rules that prescribe keyword density, word count, exactly one heading, or a fixed heading count. Duplicate URLs do not automatically produce a duplicate-content penalty. Evaluate useful titles, descriptions, semantic structure and content against page purpose; label display-length guidance as a heuristic. No audit score or implementation promises inclusion in Google's index or first-place rankings. [Google — SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).

Robots.txt controls crawling and is not a reliable way to prevent indexing; an externally linked blocked URL can appear in results. An absent robots.txt is not inherently an SEO defect. A crawler must be allowed to fetch the response to read its `noindex` directive. Inspect both robots meta tags and `X-Robots-Tag` headers when available, interpreting directives for the relevant user agent. Do not recommend removing intended exclusions from account, internal-search, staging, or other intentionally excluded pages. [Google — Robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro), [robots metadata specification](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag).

Treat declared canonical URLs as signals and check consistency with redirects, internal links, and sitemaps. Do not equate a declaration with Google's selected canonical, and do not recommend consolidating pages with materially different user intent merely because their layout is similar. [Google — Canonicalization methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

Evaluate structured data only when a supported type fits the visible content. Separate syntactic validity, required properties, content-policy eligibility, and actual search appearance. Valid markup never guarantees a rich result, and not every page needs every schema type. Recheck the current feature-specific documentation before recommending a type. [Google — Structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

## Accessibility

Use **WCAG 2.2 Level AA as an audit target** unless the client specifies another target. Cite criterion numbers for supported findings. Useful checks include text alternatives (1.1.1), contrast (1.4.3), reflow (1.4.10), keyboard use (2.1.1), focus visibility (2.4.7), focus not obscured (2.4.11), target size (2.5.8), labels/instructions (3.3.2), and name/role/value (4.1.2). Reflow includes a 320 CSS-pixel width test for ordinary vertically scrolling content, with exceptions for necessary two-dimensional layouts. The AA target-size criterion is 24 by 24 CSS pixels with specified exceptions, not a universal 44-pixel requirement. Check exceptions before declaring failures. Conformance concerns full pages and complete processes; a sampled URL is not proof of sitewide conformance. [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/).

Automated tools cannot complete every accessibility check. Record manual keyboard, zoom/reflow, focus, dialog and assistive-technology checks separately. A tool's 100 score is not an accessibility certification. Mark unperformed manual checks as untested. [W3C WAI — Evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/).

Include representative users with disabilities where practical, and state the scope and limitations of user research. A small study does not establish universal usability or statistical significance; combine user evaluation with standards evaluation. [W3C WAI — Involving users](https://www.w3.org/WAI/test-evaluate/involving-users/).

## UX/mobile and conversion/CRO

The following are this plugin's evidence policies, not external scoring standards:

- Inspect representative mobile and desktop layouts and specific tasks, including navigation, product/service comprehension, contact or purchase paths, form errors, and interruptions. Name the tested viewport and state. Do not generalize one screenshot to every device.
- A broken link or obscured required control is an observed defect when reproduced. A proposed headline, CTA position, shorter form, trust cue, or information layout is normally a hypothesis until tested with relevant users or controlled experiments.
- Do not invent analytics, conversion rates, abandonment rates, traffic, revenue, or percentage uplift. Separate qualitative confidence from business impact; quantify impact only with client data and stated assumptions.
- For each CRO hypothesis, specify audience, current friction, proposed change, success metric, guardrail metric, and validation method. A/B testing needs appropriate allocation, sample planning, duration, and analysis; a before/after change alone cannot isolate causation.
- Prefer clarity, accurate claims, transparent costs, and informed choice. Do not recommend deceptive urgency, hidden fees, consent interference, or other manipulative patterns.

## Security and basic technical hygiene

Public-page auditing is a passive hygiene review. Observe HTTPS behavior, visible mixed-content problems, relevant response headers, publicly presented errors, and cookie attributes when the tools expose them. The plugin's policy excludes port scans, credential attacks, payload injection, vulnerability exploitation, secret discovery, and form submission as part of an ordinary URL audit. Never claim penetration-test coverage or certify a site as secure from this review.

Header recommendations require context. CSP `frame-ancestors` can provide framing protection, so missing `X-Frame-Options` alone does not prove a vulnerability. Do not recommend obsolete `X-XSS-Protection` or `Expect-CT` as mandatory safeguards. Missing CSP is a hardening observation, not proof that XSS is exploitable. Consider staged CSP rollout and application compatibility. HSTS options, particularly subdomain scope and preload, need deployment review rather than copy-and-paste enforcement. [OWASP — HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).

Assess cookies by purpose. `Secure` limits sending to HTTPS; `HttpOnly` is appropriate when JavaScript access is unnecessary, especially for session identifiers. `SameSite` settings must account for the application's legitimate flows. Do not label every cookie without `HttpOnly` as a session vulnerability. Redact cookie values and tokens from evidence; preserve names and attributes only when necessary. [MDN — Secure cookie configuration](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Cookies).

## Content quality

Assess whether pages satisfy their intended audience's needs with clear, original, reliable, sufficiently complete information. Consider authorship or expertise where appropriate, evidence for claims, accuracy, freshness, and whether the next step is understandable. Do not infer authorship, plagiarism, or AI generation from style alone. Avoid invented E-E-A-T scores presented as Google's measurement, fabricated credentials, keyword stuffing, and arbitrary word-count minimums. [Google — Helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

## Reporting contract

These are this plugin's reporting conventions:

1. Every finding identifies the affected URL/template, observed fact, evidence source and time, test method, scope, impact, confidence, severity, remediation, and a verifiable acceptance criterion.
2. Distinguish **observed**, **measured**, **inferred**, and **not tested** evidence. A recommendation may be valuable without pretending its effect was measured.
3. Keep source-tool scores separate from the plugin's advisory score. State the advisory formula and denominator, disclose coverage, exclude genuinely inapplicable checks, and never treat unknown checks as passes.
4. Group repeated template defects to avoid inflating finding counts. Severity reflects user or business harm; priority also incorporates reach, confidence, effort, dependencies, and client goals.
5. Quick wins require both plausible value and limited effort. The plan includes an owner role, estimate range, dependency, validation method, and suggested sequence. Treat effort and timing as estimates, not commitments.
6. Preserve a client-specific baseline and use comparable methods for a re-audit. Retain outstanding limitations until new evidence resolves them.
