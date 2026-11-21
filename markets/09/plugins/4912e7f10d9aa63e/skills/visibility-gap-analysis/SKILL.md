---
name: visibility-gap-analysis
description: Analyze Linkeddit search visibility measurements and recommendation gaps when a user asks why competitors appear, where visibility changed, or what evidence-backed improvements to prioritize.
---

# Visibility gap analysis

Resolve the user's domain with `answer_projects_list`; use returned project IDs. If several projects match, clarify the target before retrieving detailed records. Use the connected tools' current schemas; missing tools are an access limitation, not proof of a particular plan.

For current performance, use `answer_metrics_get`. For a change over time, use `answer_trends_get` with the requested period. Preserve each measurement segment (provider, model, tool version, locale), metric definitions, sample counts, and disclosures. Compare like segments and time windows. `usable=false` or missing observations mean unavailable measurement, not zero visibility. Do not average across segments or attribute a change to a cause without evidence.

For improvement opportunities, call `answer_gaps_list`, then `answer_gap_get` for the gaps most relevant to the user's buyers. Keep recorded observations, cited sources, hypotheses, and suggested actions distinct. A competitor mention alone does not establish a recommendation. Note evidence dates and gaps in coverage.

Return the material findings with source links or returned record IDs, why each matters, and a practical next action. Label your prioritization as analysis rather than a stored score. If the user wants content, draft it in the conversation from the retrieved evidence; don't imply it has been saved or published.

Reading results does not require a new audit. If the user requests a new audit, use the available estimate tool, explain its scope and credit estimate, and obtain agreement before starting it. No automatic project creation, recurring monitoring, or publishing follows from an analysis request.
