# Daily pursuit radar templates

Read this file when configuring the skill, defining a customer rubric, creating a schedule, or formatting the final digest.

## Customer configuration

```yaml
saved_searches:
  selection: all # or exact IDs/names
reporting:
  minimum_score: 70
  maximum_finalists: 10
  maximum_matches_per_search: 200
  changes_only: true
rubric:
  hard_disqualifiers:
    - Outside approved market or geography
    - Required contract vehicle is unavailable
    - Insufficient response time
  criteria:
    - name: Capability fit
      weight: 30
      full_credit: Scope directly matches our products or services
    - name: Buyer fit
      weight: 20
      full_credit: Buyer is in an approved target segment
    - name: Contract access
      weight: 20
      full_credit: We hold or can use the required vehicle
    - name: Competitive position
      weight: 15
      full_credit: We have a customer, partner, or incumbent advantage
    - name: Timing
      weight: 10
      full_credit: There is sufficient capture and proposal time
    - name: Strategic value
      weight: 5
      full_credit: Opportunity supports a named growth priority
```

Treat this as a template, not a Govly default. Use the customer's actual criteria and scoring anchors.

## Scheduled prompt

```text
Every weekday at 7:30 AM local time, use the Govly Daily Pursuit Radar skill.

Review the opportunity saved searches configured in this chat. Apply the
attached scoring rubric. Report only new or materially changed opportunities
that score at or above the configured threshold. Include the score breakdown,
supporting Govly evidence, unknowns, deadline, and recommended next action.

If nothing qualifies, say so briefly. Do not modify Govly records, saved
searches, inbox items, follows, or workspaces.
```

## Digest format

```md
# Pursuit radar — YYYY-MM-DD

Status: Complete | Partial coverage | First run | Setup needed
Coverage: X saved searches; Y matches; Z unique opportunities; N finalists

| Status | Score | Confidence | Opportunity | Buyer | Deadline | Matched searches | Why it ranks |
|---|---:|---|---|---|---|---|---|

## Finalists

### Opportunity title — score/100, confidence
- Evidence:
- Score breakdown:
- Risks and unknowns:
- Recommended next action:

## Not reported
- Disqualified: X
- Below threshold: Y
- Unchanged and suppressed: Z
```
