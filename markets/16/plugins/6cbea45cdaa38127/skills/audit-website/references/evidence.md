# Evidence collection and boundaries

## Tool selection

Use the host's available tools under their own instructions. This plugin makes no assumptions about a particular browser connector, shell, paid SEO service, or authenticated analytics account.

| Available source | What it can support | What it cannot establish alone |
| --- | --- | --- |
| Retrieved page text | Visible copy, links actually returned, observed subject matter | Raw HTTP headers, complete DOM, layout, mobile behavior, absence of elements omitted by extraction |
| Browser with DOM and screenshots | Rendered headings, labels, observed page state, stated viewport layout | Site-wide behavior or an unperformed interaction |
| Raw HTTP/HTML inspection | Actual status, redirect/response headers, source metadata | Rendered JavaScript behavior, field performance |
| Lighthouse/PageSpeed report | Its dated lab checks and any separately supplied field section | Universal user experience, full accessibility conformance, guaranteed conversion impact |
| Search Console/analytics export | The included property's dates, filters, measurements | Unexported pages, current state outside its date range, causality by itself |
| Client statement | Business context and a reported problem | Verification of technical implementation or resolution |

When a required source is missing, keep the affected check `not_tested`. A browser error or a bot challenge is evidence of audit access limitations; corroborate before classifying an outage. Record unexpected redirects and the reason for following them. Do not broaden the sample to unrelated external domains just because a page links there.

## Evidence ledger

Use IDs such as E001, E002. Each record has a URL when known, method, timezone-aware `captured_at`, concise `observation`, and optionally `limitation`. Describe exactly what was seen, with enough detail for a reviewer to repeat it. For an imported report use its source page/report URL and identify the actual measurement date, scope, device, and source in the observation; distinguish that from the time the export was reviewed. When a client-supplied excerpt or export has no known source URL, use `url: null` with a descriptive `source_label` and explain the provenance limitation. Never invent an affected path or use the site's homepage as if it were the known source of unlocated material. Ask for the source URL only when it is needed to validate the claim.

Useful forms:

- HTTP: requested URL, final URL, status/redirect chain, exact relevant header value and method.
- DOM: URL, relevant element/selector, short observed text/attribute, actual page state.
- Visual/manual: URL, viewport, interaction steps, screenshot reference if captured, outcome.
- Performance: page/origin, device, field/lab, metric, value/unit, period, percentile, provider assessment, test settings and missing data.
- Imported evidence: filename/report URL, provider, date range, filters, sampling limitation, client-supplied provenance.

Separate standards citations from observed site evidence. A link explaining ideal behavior does not prove that the client site violates it. Use the narrowest evidence that supports the claim; do not copy entire pages into the audit.

## Sampling and check outcomes

Apply the catalog's criterion to the recorded sample and declare it in scope. A `pass` means the criterion was affirmatively checked for that sample. If samples have mixed results, use `partial` and name the passing/failing examples. A missing prerequisite or an incomplete check is `not_tested`, even if some favorable observations exist. A `fail` requires evidence of the failing criterion.

N/A means the criterion truly does not apply, such as form validation on a site with no form anywhere in the audited scope. Cite the evidence and scope for that conclusion. Lack of access, missing analytics, missing CrUX coverage, limited time, or missing tooling are never N/A. Record scope-limited inapplicability as such and do not generalize it to the whole site.

Avoid guarantees from small samples. State "2 of 6 sampled pages" when that is all that was checked. Assess reach conservatively; a likely shared template may justify a broader-impact hypothesis, but does not prove every page is affected.

## Performance and accessibility

Where tools permit, compare at least one representative mobile viewport and desktop viewport and state the exact dimensions. Do not describe a page as mobile-tested when only its responsive HTML was read. For keyboard testing, use a real tab sequence and verify visible focus and operability; do not infer keyboard access from a clickable screenshot.

Use the current standards reference for field and lab distinctions. Insufficient real-user data is an evidence gap, not a poor CWV result. An automated accessibility score covers only its checks. Describe the sampled/manual coverage explicitly and never present a scan as WCAG certification.

## Passive security hygiene

Review benign delivered responses, redirects, loaded resources, and public page content. Match recommendations to context. Missing CSP, HSTS, or a version-disclosure header can merit a hygiene finding; it does not establish that a vulnerability is exploitable. Do not recommend HSTS preload or broad CSP changes without staging and compatibility checks. Never include exposed secrets verbatim in the client report; redact them and provide a safe location reference. A confirmed exposure needs immediate containment and credential rotation by the owner, not attempted use of the secret.

## CRO and remediation evidence

Describe conversion friction as observed usability behavior, or as a hypothesis where user/analytics evidence is missing. Never promise numerical uplift. An experiment proposal includes its hypothesis, primary conversion metric, guardrail metrics, audience/segment, instrumentation prerequisite, and a decision rule agreed with the client. Do not prescribe a statistical sample size without traffic, baseline rate, effect size and test design.

Write acceptance criteria a teammate can actually retest: the URL/template, changed behavior, tool or interaction, and expected observable result. Where relevant, include regression checks on other sampled templates/devices.
