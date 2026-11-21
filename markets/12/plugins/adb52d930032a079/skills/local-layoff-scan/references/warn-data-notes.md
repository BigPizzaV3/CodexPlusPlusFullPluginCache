# WARN data notes

What the DataCEVA US Layoff Notices data covers, what each field means, and how to cite it.

## What a WARN notice is

The federal Worker Adjustment and Retraining Notification (WARN) Act generally requires employers with 100 or
more employees to give 60 days' notice before a plant closing or mass layoff, including to the state. Several
states have their own versions with lower thresholds or longer notice periods. States publish the notices they
receive, each in its own format. DataCEVA collects those public lists, standardizes them and refreshes them
daily.

WARN notices cover larger layoffs only (generally 50 or more workers at one site). They are a floor, not a
count of all job losses. They describe employers, never individual employees.

## Coverage

- 46 states and Washington, D.C. are collected.
- Arkansas, Wyoming and New Hampshire don't publish notices. Ohio is temporarily unavailable.
- Some states are collected in part, or from a saved copy of their history only. `get_data_coverage` reports
  each state's status, history range (`first_filed` to `last_filed`) and `last_refreshed` time.
- History depth differs by state, and some states have gaps.

## Fields

| Field | Meaning |
|---|---|
| `filed_date` and `filed_date_type` | When the state received the notice, or the date on the notice (`received` / `notice`) |
| `layoff_start_date` | The planned first day of layoffs |
| `employees_affected` | Workers affected, as filed. Blank means the state didn't publish a number |
| `layoff_type` / `permanence` | Layoff, closure, relocation or other; permanent, temporary or unknown |
| `industry` | From the state's own industry field; reported by some states only |
| `is_revision` | An update or correction to an earlier notice; left out of totals so a layoff isn't counted twice |
| `source.notice_url` | Link to the notice itself, when the state publishes one |
| `source.state_warn_page` | The state agency's WARN page |
| `as_of` | When the data was last refreshed; give it in every answer |
| `caveats` | Limits that apply to this answer; pass the relevant ones on to the user |

## Dates

- Searches filter on the filed date. GA, NJ, PA and much of MI publish only a planned layoff date, so they are
  left out of filed-date results unless `include_scheduled_only` is set.
- Always say whether a date is a filed date or a planned layoff date.

## How to cite

For each notice, name the state agency and link to `notice_url`, or to `state_warn_page` when there is no notice
link. End each answer with the as-of date, for example "Source: state WARN notices via DataCEVA, as of
2026-10-13."
