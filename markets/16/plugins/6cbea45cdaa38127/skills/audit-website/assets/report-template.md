# AuditIn72: your website review — {{business_or_domain}}

Audit date: {{date_and_timezone}} · Target: {{requested_url}} · Observed final URL: {{final_url}}

## What works and what to improve first

{{Summarize the strongest observed issues, likely business implications, and demonstrated strengths. State material access/measurement gaps. Do not promise ranking, traffic, legal compliance, security, or conversion outcomes.}}

{{Explain the most useful next actions in plain language before the detailed scorecard. Show up to three leading issues only when the evidence supports them. Address the owner as "you" and "your website".}}

## Scope and confidence

- Objective, audience, market, primary conversion, and explicit assumptions: {{context}}
- Scope: {{mode}}, {{sample_count}} sampled pages; {{template_selection_reason}}
- Sources and dates: {{tools_used_and_measurement_periods}}
- Device/viewport coverage: {{actual_devices_or_not_tested}}
- Limits: {{blocked_pages_missing_exports_unperformed_checks}}

| Sampled URL | Page type | Selection reason | Inspection performed |
| --- | --- | --- | --- |
| {{url}} | {{type}} | {{reason}} | {{method}} |

## Scorecard

Copy the calculator's eight category results, category weights, weighted coverage, N/A exclusions, overall result, and provisional label exactly. Scores follow this plugin's rubric; coverage indicates how much applicable check weight was actually assessed. These are distinct from Lighthouse scores and external certifications.

| Category | Weight | Quality / 100 | Coverage | Status / limitations |
| --- | ---: | ---: | ---: | --- |
| Technical SEO | 20% | {{score_or_untested}} | {{coverage}} | {{status}} |
| On-page SEO | 15% | {{score_or_untested}} | {{coverage}} | {{status}} |
| Performance / CWV | 15% | {{score_or_untested}} | {{coverage}} | {{status}} |
| Accessibility | 15% | {{score_or_untested}} | {{coverage}} | {{status}} |
| UX / mobile | 10% | {{score_or_untested}} | {{coverage}} | {{status}} |
| Conversion / CRO | 10% | {{score_or_untested}} | {{coverage}} | {{status}} |
| Security / hygiene | 10% | {{score_or_untested}} | {{coverage}} | {{status}} |
| Content quality | 5% | {{score_or_untested}} | {{coverage}} | {{status}} |

Overall: {{computed_score_or_not_available}}, {{coverage}}, {{provisional_reason}}.

For performance, show the source's field metrics, page/origin scope, device, percentile/period, and provider assessment separately from dated lab measurements. If measurements are absent, say so.

## Prioritized findings

| ID | Finding | Kind | Severity | Priority | Impact / reach | Confidence | Effort | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{F001}} | {{title}} | {{observed_or_hypothesis_or_needs_verification}} | {{severity}} | {{priority}} | {{impact_and_sample_scope}} | {{confidence}} | {{estimate_and_assumptions}} | {{role}} |

For each finding:

**{{ID}} — {{title}}**

- Observation and affected sampled URLs: {{precise_fact_or_hypothesis}}
- Evidence: {{evidence_ids_and_clickable_source_urls_capture_date_tool_context}}
- Why it matters: {{supported_business_or_user_effect_with_limits}}
- Remedy: {{specific_steps_and_configuration_context}}
- Dependencies and suggested owner: {{dependency_ids_and_role}}
- Acceptance test: {{reproducible_steps_and_expected_result}}

## Quick wins

List only calculator-eligible quick wins with evidence, a meaningful effect, no unmet dependency, and an estimated effort of four hours or less. If there are none, say so. Keep critical incidents in immediate triage even if they also take little time. Do not fill a quota with cosmetic suggestions.

## Repair or rebuild?

{{Use the owner decision guide. State targeted improvements, consider a broader redesign after scope verification, or more evidence needed. Name the supporting finding IDs. Explain feasible repairs and uncertainties. A low or incomplete score alone does not justify replacing the site.}}

## Your improvement plan

| Window | Finding IDs / action | Suggested owner | Dependencies | Effort assumption | Done when |
| --- | --- | --- | --- | --- | --- |
| Immediate triage | {{confirmed_critical_or_high_risk_items_if_any}} | {{role}} | {{dependencies}} | {{estimate}} | {{acceptance}} |
| Next 2 weeks | {{high_value_fixes_and_required_measurement}} | {{role}} | {{dependencies}} | {{estimate}} | {{acceptance}} |
| Next 30 days | {{template_or_structural_fixes}} | {{role}} | {{dependencies}} | {{estimate}} | {{acceptance}} |
| Later / experiments | {{larger_work_or_CRO_hypotheses}} | {{role}} | {{instrumentation}} | {{estimate}} | {{decision_rule}} |

Adapt windows to the client's capacity and dependencies. Omit empty rows rather than inventing work. Explain when a prerequisite changes the suggested order. Owner roles are recommendations, not assignments to real people.

## Verification backlog

{{List untested check IDs and why, needed sources/access, and the next concrete validation action. Keep hypotheses and evidence gaps distinct from proven defects.}}

## Evidence appendix and method

{{Complete evidence ledger, cited standards, catalog version, score formula/version, justified N/A checks, raw measurements/settings, and known limitations.}}

## Retest

{{Agree on a comparable sample and method. For re-audits, list each prior finding as resolved/persistent/regressed/new/unverified with fresh evidence. Explain coverage changes before comparing scores.}}

## Brief for whoever makes the changes

{{Provide a short, useful handoff of the site URL, goal, verified findings, recommended repair/redesign scope, dependencies, and acceptance criteria. No registration or contact details are needed to receive it. Nothing is automatically sent to SiteIn72.}}

---

This audit was provided by [SiteIn72](https://sitein72.com/).

{{Keep the attribution once at the end. Do not append a sales offer, paid-service referral, quote invitation, pricing, or purchase link.}}
