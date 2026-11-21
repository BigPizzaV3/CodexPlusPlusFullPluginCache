# Evidence, scoring and prioritization contract

The score summarizes observed website quality within a declared sample. It is not a Google ranking factor, a legal/accessibility certification, a security certification, a forecast of conversion uplift, or a claim about the entire site. Never invent traffic, revenue, search demand, analytics, lab results or field Core Web Vitals.

## Files and commands

Use Python 3.10+; no packages, credentials or network access are needed for the local calculator. Run from this skill's directory (replace paths as needed):

```sh
python scripts/score_audit.py --init https://example.com --output audit-input.json
python scripts/score_audit.py audit-input.json --output audit-scored.json --markdown audit-report.md
```

`--init` creates a blank evidence-input template containing all 40 untested checks. It does not inspect the URL. Replace its initial timestamps, scope and limitations with the actual audit window and observed scope after inspection. The second command validates the evidence input, computes scores, and optionally writes a Markdown report. It exits 2 on invalid input; fix the evidence file and retry. Input/output/report paths must differ. The calculator does not upload files or change the website. It may overwrite an existing requested output file; keep per-client audit files in separate folders.

`audit.schema.json` is the **input** schema (JSON Schema 2020-12), not the enriched output schema. The script additionally validates ID uniqueness, cross-references, category/check agreement, dependency cycles, absolute HTTP(S) URLs without credentials, timestamp offsets and chronology. Unknown fields are rejected. Do not use the scored JSON as the next input; revise the original evidence input.

If Python is unavailable, apply the identical arithmetic below and retain the complete check register. Do not silently change weights or treat unknowns as passes.

## Immutable baseline

Catalog version `1.0.0` contains 40 checks, five per category. Check weights sum to 100 within each category; category weights sum to 100:

| Category ID | Weight |
|---|---:|
| technical_seo | 20 |
| on_page_seo | 15 |
| performance | 15 |
| accessibility | 15 |
| ux_mobile | 10 |
| conversion | 10 |
| security | 10 |
| content | 5 |

The script verifies the canonical JSON hash of `checks.json`. Reordering object keys or changing whitespace is harmless; modifying checks/weights makes validation fail. Preserve this baseline between client audits. A deliberate methodology change requires a new catalog version and corresponding script/schema update; scores across different baselines are not directly comparable. This protects comparability against accidental editing, not deliberate tampering with the calculator itself.

Every check appears in output. Omitted input checks become `not_tested`; choosing only favorable checks cannot erase the missing checks from coverage. Unknown or repeated IDs are rejected. Findings are a remediation explanation and never apply an additional penalty to a scored check.

## Evidence and statuses

Evidence entries require `id`, source `url`, collection `method`, timezone-aware `captured_at`, and a concrete `observation`. If an uploaded report/excerpt does not identify its source URL, set `url` to `null` and provide a nonempty `source_label` identifying the actual supplied source and missing provenance; never fabricate a URL. `source_label` is optional when a valid URL is known. Optional `limitation` and `artifact` can identify collection caveats and a saved screenshot/report reference. Keep evidence concise, reproducible and tied to the actual sampled URL when known. Redact credentials, tokens and visitor data. A URL alone is not a substantive observation. Evidence/finding IDs use 1–100 letters, digits, dots, underscores or hyphens, beginning with a letter or digit.

Checks require `id`, `status`, and `evidence_ids`. Include `notes` for tested devices, relevant page coverage, mixed results and missing portions:

- `pass`: all material applicable criteria in the check are supported by adequate evidence; credit 1.
- `partial`: complete required inspection shows observed material mixed results across applicable criteria or sampled pages, explicitly described; credit 0.5. Incomplete testing or missing required evidence is `not_tested`, not partial. Do not assign arbitrary percentages or use partial merely to soften a failure.
- `fail`: adequate evidence establishes a material failure of the check's criteria; credit 0.
- `not_tested`: unable to assess, tool access missing, evidence absent, or inspection not performed. No credit denominator contribution; reduces evidence coverage. Include the reason. An inaccessible page, unavailable analytics, absent field data or missing authorization is usually untested, not N/A.
- `na`: inspection establishes that the entire check is inapplicable to the declared site/scope. Requires both evidence and nonempty `na_reason`; excluded from the applicable denominator. Justify against the catalog's applicability note. An inapplicable subtest does not automatically exempt the whole compound check.

`pass`, `partial`, `fail`, and `na` require at least one valid evidence reference. The calculator checks structural evidence presence, not whether prose proves a claim; the auditing agent must verify evidential adequacy. All evidence and finding IDs must be unique. A no-evidence audit has no numeric category scores or overall score.

For CWV, separate field data from lab diagnostics. Record field source, URL/origin scope, device, reporting window, percentile, metric availability and provider assessment. Missing field data is not a failure. A provider may report a passed assessment using available metrics while INP is unavailable; retain that exact provider result and explicitly report the limited coverage, while this fixed three-metric composite check remains `not_tested`. Use `partial` only when complete required evidence demonstrates mixed good/non-good results. Do not claim measured INP, complete three-metric field coverage, or real-user CWV from a Lighthouse score. The calculator does not interpret metric values or replace tool/provider results.

## Arithmetic

For each category, let:

- `P` = possible fixed check weight (100).
- `N` = weight of justified N/A checks.
- `A = P − N` = applicable check weight.
- `M` = weight of checks with pass, partial or fail status.
- `E` = sum of each assessed check's weight × credit.

Category score = `100 × E / M`, or `null` when `M = 0`. Category evidence coverage = `100 × M / A`, or `null` when `A = 0`. All-N/A is unassessed, not a perfect score. The output also shows raw full-catalog measured share `100 × M / P` and N/A share `100 × N / P` so exclusions remain visible.

For category weight `W`, global measured weight is `Σ(W × M / P)`; global applicable weight is `Σ(W × A / P)`. Overall evidence coverage = `100 × global measured / global applicable`, or `null` when there are no applicable checks. This is a weighted coverage calculation across the complete catalog, not an average over the selected checks.

Overall quality score = `Σ(W × category score / 100)`, retaining all original category weights. It is **null if any category has no assessed check**, including an entirely N/A category. Never reweight away an unassessed category to manufacture an overall score.

An overall result is **provisional** when any category coverage is below 60% or unassessed, overall coverage is below 80% or unassessed, or the overall score is null. A provisional numeric score may be shown only alongside its coverage and caveats. Otherwise the status is `assessed`; this still describes the sample, not a full-site certification. Category status is provisional below 60%, unassessed without a score, otherwise assessed. Compute thresholds and grades using unrounded numbers; round displayed values to two decimals. The provided catalog's weight increments make threshold-boundary coverage exact.

Grades: 90–100 Strong; 75–<90 Good; 60–<75 Needs improvement; 40–<60 Weak; 0–<40 Poor; null Unassessed. Scores are not comparable without scope, evidence coverage, N/A share, device mix and catalog version.

Example: a category has pass weight 30, partial weight 25, fail weight 15, untested weight 20 and justified N/A weight 10. `M=70`, `E=42.5`, `A=90`; score `60.71`, applicable coverage `77.78%`, raw measured share `70%`, N/A share `10%`. That one category does not establish an overall score.

## Findings and risk-first work order

Each finding requires `id`, `title`, one `category`, one or more matching `check_ids`, `severity`, `kind`, `impact`, `reach`, `effort_hours`, `confidence`, `evidence_ids`, `remediation`, `validation`, `owner_role`, and `dependencies` (an empty list when none). Finding/check/evidence/dependency references must resolve; dependency cycles and self-dependencies are rejected. Consolidate the same root cause into one finding with multiple matching check/evidence references; do not repeat it to inflate the count. The validator rejects duplicate IDs, but semantic deduplication remains an editorial responsibility. Cross-category root causes should use one primary category and describe secondary effects in the text; do not duplicate score penalties.

Kinds:

- `observed`: directly supported by evidence; at least one evidence reference required.
- `hypothesis`: a plausible explanation or opportunity that has not been established. State what evidence would test it.
- `needs_verification`: a signal needing confirmation before remediation. Missing data is not proof of a defect.

Severity describes the evidenced failure/risk, independently of business benefit or estimated implementation cost:

- **Critical:** confirmed severe interruption of core business access or material exposure needing immediate triage. Reserve this for explicit evidence; no speculative vulnerability claims.
- **High:** substantial harm to a primary journey, index eligibility, accessibility or relevant technical safety.
- **Medium:** meaningful impairment affecting a bounded journey, group or recurring quality issue.
- **Low:** limited/localized impairment or optimization with modest practical consequence.
- **Info:** context, monitoring or a nondefect observation.

For an unverified finding, severity expresses the **potential risk to verify**, not a confirmed defect; use restrained wording. Such findings always receive `action_type=verify_first` and cannot be quick wins.

Impact (1–5) estimates consequence to the stated client goal: 1 negligible, 2 modest/local, 3 meaningful, 4 major, 5 severe/core outcome. Reach (1–5) estimates the affected share of the **declared scope**: 1 isolated, 2 small subset, 3 several important pages/journeys, 4 most key journeys, 5 broadly sitewide when evidence supports that conclusion. These are ordinal judgments, not revenue/traffic projections; include uncertainty in evidence/notes. `effort_hours` is a positive estimate of active work, not a delivery promise. Confidence is high (direct reproducible evidence), medium (credible but limited evidence), or low (tentative/context missing).

Priority is a work-order calculation separate from the finding's descriptive severity. Risk tiers always override the arithmetic: P0 critical, P1 high, P2 medium, P3 low, P4 info. Within a tier, put observed issues before verification tasks, then sort descending by:

`benefit_effort_index = impact × reach × confidence_factor / max(effort_hours, 0.25)`

Confidence factors: high 1, medium 0.75, low 0.5. The 0.25-hour floor prevents tiny estimates from creating unbounded rankings. The index is a prioritization aid, not financial ROI. Exact ties use finding ID alphabetically for stable reproducibility. The output reports both the risk tier and the global numbered rank; a cheap cosmetic task cannot displace a severe confirmed risk.

Dependencies do not erase risk/urgency. Output retains the sorted risk queue plus `blocked_by` references; execute prerequisites before dependent work. A P0 item may require a P2 prerequisite to be handled first for that fix. The generated remediation plan groups immediate triage (P0–P1), next planned work (P2), and later optimization (P3–P4), with a separate verification-first list. Assign a human role, a concrete fix, and a measurable/reproducible validation step to every finding. Agree real calendar dates with the client instead of inventing them.

A **quick win** requires all of: observed evidence, impact at least 3/5, medium/high confidence, positive estimated effort at most 4 hours, severity other than info, and no outstanding recorded dependencies. An appealing but unverified idea is an experiment/verification task, not a quick win.

## Review before delivery

Check the original observations against every scored status, preserve all limitations, and review N/A rationales for denominator inflation. Verify the sampled URLs and audit window, field-versus-lab notes, complete 40-check register, severity wording, dependencies, quick-win eligibility and remediation owners/validation steps. Reassess affected checks after fixes using the same catalog and comparable scope; do not promise a score increase until retested.
