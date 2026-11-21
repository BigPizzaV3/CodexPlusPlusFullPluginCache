---
name: "plant-performance-review"
description: "Daily PR triage for one accessible Plant and one Plant-local day. Read-only. Compares the day with the 7 days before it and makes no root-cause claims."
---

# Plant performance review

Use only the tools this server lists. Read-only.

## Procedure

1. Find the Plant: search_plants if the user names one, else list_accessible_plants. Use only a returned Plant ID. If exactly one result name is the same as the user's Plant name (any letter case), use it. If the user gives only the end of a Plant code, for example P043 or PR043, and not a full code such as NORTH-P043: search with the digits only, for example 043. If codes with different prefixes contain those digits, show all of them and ask. No match: stop and say so. Several matches: ask the user. If a tool returns the FORBIDDEN error, stop and say so; do not try another Plant ID.
2. Times: a clock time with no zone is Plant time. If the user names a zone, change the time to Plant time and state the two times. SG is UTC+8. VN is UTC+7.
3. Call get_plant_daily_performance: start D minus 7 days, end D, plain dates, and the Plant timezone unless the user gives one. Timezone required: stop and ask. Baseline: the 7 days before D. Day: row D.
4. No row for D or PR on D null: say 'no reported value'. Never show 0. Coverage partial: name the null fields.
5. Compare PR on D with the baseline range, ignoring nulls. Below: say so, with units. Otherwise: not low against 7 days; stop.
6. Report irradiation and availability for D as returned. They are observations, not causes.
7. Find the device: list_devices, with nameQuery when the user names a device. nameQuery matches the name and the label; letter case, spaces, and separators are ignored. Use only a returned device ID. Exactly one match: use it. No match: call list_devices again without nameQuery and use the devices with a similar name or label as candidates. No match or more than one: show the name, label, and type of each candidate and ask the user before you read data. Do not select a device only because its name is similar. In the answer, state the device name and label.
8. Optional devices: get_string_daily_analytics (view for_date, date D). A weak string is a hypothesis. get_plant_dashboard is latest status only, never status on D.
9. Report Plant, D, timezone, values with units, 7-day range, coverage, warnings, and ranked next checks. Causes are hypotheses only. A tool not in tools/list is not checked: do not call it.

## Limits

NOT CHECKED in every answer: work orders, DataHub, status as of D, device fault history. Not read by this procedure; read only if the user asks: alarm history (list_alarms), sub-day window (query_plant_5min).
