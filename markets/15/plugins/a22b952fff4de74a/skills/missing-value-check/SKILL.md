---
name: "missing-value-check"
description: "Explain a blank, zero, old, or missing value for one accessible Plant and one Plant-local day. Read-only. Compares the live and stored sources and makes no root-cause claims."
---

# Missing value check

Use only the tools this server lists. Read-only.

## Procedure

1. Find the Plant: search_plants if the user names one, else list_accessible_plants. Use only a returned Plant ID. If exactly one result name is the same as the user's Plant name (any letter case), use it. If the user gives only the end of a Plant code, for example P043 or PR043, and not a full code such as NORTH-P043: search with the digits only, for example 043. If codes with different prefixes contain those digits, show all of them and ask. No match: stop and say so. Several matches: ask the user. If a tool returns the FORBIDDEN error, stop and say so; do not try another Plant ID.
2. Times: a clock time with no zone is Plant time. If the user names a zone, change the time to Plant time and state the two times. SG is UTC+8. VN is UTC+7.
3. Name the value: the metric, its unit, and the Plant or the device. D is a Plant-local date. Use yesterday if no date is given. Read only D, from 00:00 to the next day 00:00 in Plant time. If the timezone is missing, ask for it. For a Plant value, do not find a device.
4. Find the device: list_devices, with nameQuery when the user names a device. nameQuery matches the name and the label; letter case, spaces, and separators are ignored. Use only a returned device ID. Exactly one match: use it. No match: call list_devices again without nameQuery and use the devices with a similar name or label as candidates. No match or more than one: show the name, label, and type of each candidate and ask the user before you read data. Do not select a device only because its name is similar. In the answer, state the device name and label.
5. Read the live source for D at 5m. For a Plant value, call get_plant_chart with the chart that shows the metric. For a device value, call query_device_telemetry with the resolved device ID and the metric key. Count the points with a value, the null points, and the zero points. A key with status no_points is not proof that the device has no data. If the reply gives a suggestion, call again with that key and state both keys. Otherwise, select a key from deviceKeys or say the key is not on the device. State the key you used. Null means no reported value, never 0 or the previous value.
6. Read the stored source for D. Call query_plant_5min with the Plant metric, from D 00:00 to the next day 00:00 with Plant offsets. Count the rows with a value, the null rows, and the zero rows. For a device value, these Plant rows are context only. Call get_plant_daily_performance with start D, end D, plain dates, and the Plant timezone. Report the row for D, or say there is no row.
7. Call get_plant_dashboard with view devices_detail. Report the device status and the last data time, if returned. Online is not proof of fresh data. This is the latest status, not the status on D.
8. Classify the gap from the counts. No source data: no values in the live or the stored source. Live present but stored missing: live values, no stored values. Stored present but live missing: stored values, no live values. True zero: both sources give 0 at the same times. If the counts do not fit one class, say so and give the counts.
9. For missing rows or null values, say 'no reported value'. Never show 0 for missing data. A value is 0 only when the source returns 0.
10. Report the Plant, D, timezone, metric and unit, device if any, the counts for each source (with a value, null, zero), the class, coverage, and warnings. Do not give a root cause. Give next checks as hypotheses only. State each limit below.

## Limits

NOT CHECKED in every answer: work orders, AVA Logger connection, data pipeline runs, status as of D. Not read by this procedure; read only if the user asks: alarm history (list_alarms).
