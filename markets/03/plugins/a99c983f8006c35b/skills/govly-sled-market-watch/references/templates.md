# SLED market watch templates

Read this file when configuring the watch, creating a schedule, or formatting the final report.

## Customer configuration

```yaml
topics:
  - name: Emergency communications
    include:
      - emergency communications
      - public safety radio
      - interoperable communications
    exclude:
      - consumer wireless
places:
  names:
    - State of Colorado
  confirmed_place_ids: []
signals:
  content_types:
    - meeting
  lookback_days: 7
opportunities:
  status: open
  posted_or_modified_lookback_days: 14
reporting:
  maximum_results_per_topic: 100
  maximum_details_to_open: 10
  changes_only: true
```

Treat this as a template, not a Govly default. Confirm all place IDs and use the customer's actual topics and exclusions.

## Scheduled prompt

```text
Every weekday at 7:00 AM local time, use the Govly SLED Market Watch skill.

Search for recent SLED public meetings and other configured signals matching the
topic groups and confirmed places in this chat. Search open SLED opportunities
for the same topics and places. Report new or materially changed records, and
grade any possible connection using the skill's evidence labels.

If no relevant activity is found, say so and show the coverage window. Do not
modify Govly records, saved searches, inbox items, follows, or workspaces.
```

## Report format

```md
# SLED market watch — YYYY-MM-DD

Status: Complete | Partial coverage | First run | Setup needed
Coverage: X topics; Y confirmed places; DATE–DATE; N signals; M opportunities

## Early signals

| Status | Date | Meeting or signal | Agency/place | Topic | Why it matters | Source |
|---|---|---|---|---|---|---|

## Open opportunities

| Status | Deadline | Opportunity | Buyer/place | Topic | Why it matters |
|---|---|---|---|---|---|

## Potential connections

### Connection label — signal ↔ opportunity
- Supporting facts:
- Uncertainty:
- Monitoring action:

## Watch gaps
- Ambiguous or skipped places:
- Partial queries:
- Missing evidence:
```
