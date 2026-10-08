# Report and export requirements

Read this reference after completing the analysis and before delivering results.

## Written report

Use this order:

1. Executive summary: two to four sentences with the headline story.
2. Recommended actions: three to six ranked actions, consolidated by root cause.
3. Staffing mix findings.
4. Budget variance findings.
5. Allocation findings.
6. AI leverage opportunities, only when task codes, activity codes, or line-item descriptions identify actual work categories. Otherwise state that AI leverage was not assessed from the available detail.
7. Data notes and limitations when needed.

Every detailed finding should identify the item, severity, observed evidence, likely driver, and a concrete recommendation. If nothing material is supported in a section, state that briefly.

For each ranked action provide:

- what to do
- why it matters, tied to supported dollars or risk when available
- timeframe, such as immediately, before the matter closes, at renewal, or as an ongoing practice change

When evidence is incomplete, “confirm X before acting” is a valid action.

## Workbook payload

Create a JSON payload with this shape:

```json
{
  "title": "Q3 E-Billing Review",
  "summary": {
    "headline": "Headline finding",
    "audience": "internal review",
    "key_numbers": [
      {"label": "Total billed", "value": "$286,450"}
    ]
  },
  "action_plan": [
    {
      "priority": 1,
      "action": "Specific action",
      "why_it_matters": "Supported impact",
      "timeframe": "Immediately"
    }
  ],
  "findings": [
    {
      "category": "Staffing Mix",
      "item": "Firm and matter",
      "severity": "high",
      "driver": "Plain-language likely driver",
      "recommendation": "Specific next step"
    }
  ],
  "ai_assessment_status": "assessed",
  "ai_assessment_note": "Task codes and line descriptions were available.",
  "ai_leverage": [
    {
      "work_type": "Document review on Matter X",
      "opportunity_level": "high",
      "rationale": "Why first-pass AI assistance fits",
      "caveat": "Attorney QC and applicable confidentiality/AI-use controls are required."
    }
  ],
  "normalized_data": [
    {"entity": "Firm", "matter_id": "M-1005"}
  ]
}
```

Allowed finding severities and AI opportunity levels are `high`, `medium`, and `low`. Priorities should be numeric so the workbook can sort them.

Set `ai_assessment_status` to `assessed` when task codes, activity codes, or narrative work descriptions were reviewed, even if `ai_leverage` is empty. Set it to `not_assessed` when that task-level evidence is unavailable, leave `ai_leverage` empty, and explain why in `ai_assessment_note`. Older payloads without a status are treated conservatively as `not_assessed`.

## Generate the files

Write the payload to a temporary JSON file, choose a user-visible output basename, and run from the skill directory:

```bash
python3 scripts/build_workbook.py <payload.json> <output-basename>
```

This creates:

- `<output-basename>.xlsx` with Summary, Action Plan, Findings, AI Leverage, and Normalized Data tabs
- `<output-basename>_findings.csv` with the flat findings table

The workbook helper requires `openpyxl`. Keep the normalized-data tab focused on rows needed for follow-up when the source is very large, but do not hide exclusions.

Deliver both files with the written report and mention that the workbook supports sorting, filtering, and sharing.
