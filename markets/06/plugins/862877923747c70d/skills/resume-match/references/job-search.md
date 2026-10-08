# Current job comparison

## Search and verify

Derive plausible titles and adjacent roles from demonstrated work. Record user constraints as Hard / Preferred / Unknown. Ask for geography only when its absence would make the search mostly irrelevant. Do not assume the candidate is the account owner. Distinguish radius from commute distance/time. Remote jobs may restrict country, state, timezone, travel, or authorization.

Use available live search, then inspect full posting details. Prefer employer careers pages and employer-linked ATS sources. Reputable aggregators can supply discovery or clearly labeled secondary evidence. No specific jobs API is required or assumed. If live retrieval is unavailable, return no verified current openings and finish other requested work.

Search a pool larger than N when practical. Deduplicate employer plus requisition ID; otherwise compare role, location, and description. Record discovered and canonical application URLs, source type, stated posting date, and actual check timestamp with timezone. A refreshed/indexed date is not proof of a new vacancy.

Inspect the detail page and application route for closure, expiration, missing requisitions, or generic talent-pool redirects. An Apply button alone is insufficient. Never submit forms. Describe supported availability as currently advertised and checked at the recorded time, not guaranteed vacant. Conflicting closure evidence or uninspectable essential details exclude primary recommendations.

If only a secondary source is accessible, disclose that. Include it in the primary list only when full requirements and current advertisement are directly inspectable without conflicting evidence; never imply employer confirmation. Otherwise treat as an unverified lead outside N.

## Admission and comparison

Assess every opening with the same matching rubric. Keep availability, mandatory qualifications, user constraints, functional fit, and comparison separate.

Primary recommendations need all of:

1. Inspectable central requirements and supported current advertisement.
2. No known or likely blocker, regardless of how poor the baseline is.
3. All material mandatory requirements and hard user constraints established; unresolved conditions create conditional leads outside N.
4. A supported Better or Roughly equal comparison.

A salary range entirely below a hard floor fails. An unstated range or one straddling the floor is conditional unless a qualifying level is confirmed. Separate base pay from bonus/OTE, currency, and annual/hourly pay; don't convert without the necessary hours assumptions.

Use Better / Roughly equal / Worse / Indeterminate:

- Better: stronger central evidence or removal of a blocker with no offsetting material disadvantage. Explain why any tradeoff is acceptable under stated user preferences. Do not silently accept a substantial pay, scope, or location compromise for the user.
- Roughly equal: comparable evidence for central work, eligibility, scope, and constraints, with no supported material disadvantage. Don't force a winner.
- Worse: a material disadvantage not offset under stated priorities.
- Indeterminate: insufficient evidence or unresolved material tradeoffs to justify the comparison.

Never compare independently tuned scores or undefined uncertainty intervals. Easier is not automatically better: senior candidates seeking senior work should not be steered to junior roles just because minimums are met.

If the baseline is unassessable, return independently assessed matches without claiming equality/improvement. A closed original posting can remain an explicitly historical baseline if full text is supplied.

## Results and stopping

Return at most N primary openings, default 3, including zero when warranted. Keep conditional and unverified leads visibly separate and outside the count. State concise reasons for scarcity.

For each primary opening show title, employer, location/arrangement, direct link, status source and check time, stated pay and posting date or not stated, fit, eligibility, baseline comparison, strongest evidence, and important gaps. Include the original in a compact comparison table. Never future-date checks.

Stop after N supported results or after a focused pool and one reasonable expansion of relevant titles/sources cease producing suitable results. Describe actual search bounds, not an exhaustive market claim. For large N, work in useful batches and report the count achieved.

In explicitly synthetic testing, label fixture availability and all job outputs fictional. Mock data tests filtering and comparison, never real freshness.
