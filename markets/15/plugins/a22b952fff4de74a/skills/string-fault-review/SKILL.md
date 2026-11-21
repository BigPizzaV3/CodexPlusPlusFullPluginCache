---
name: "string-fault-review"
description: "Review weak strings for one accessible Plant and one Plant-local day. Read-only. Compare current and voltage with peers. Causes are hypotheses only."
---

# String fault review

Use only the tools this server lists. Read-only.

## Procedure

1. Find the Plant: search_plants if the user names one, else list_accessible_plants. Use only a returned Plant ID. If exactly one result name is the same as the user's Plant name (any letter case), use it. If the user gives only the end of a Plant code, for example P043 or PR043, and not a full code such as NORTH-P043: search with the digits only, for example 043. If codes with different prefixes contain those digits, show all of them and ask. No match: stop and say so. Several matches: ask the user. If a tool returns the FORBIDDEN error, stop and say so; do not try another Plant ID.
2. Times: a clock time with no zone is Plant time. If the user names a zone, change the time to Plant time and state the two times. SG is UTC+8. VN is UTC+7.
3. Find the device: list_devices, with nameQuery when the user names a device. nameQuery matches the name and the label; letter case, spaces, and separators are ignored. Use only a returned device ID. Exactly one match: use it. No match: call list_devices again without nameQuery and use the devices with a similar name or label as candidates. No match or more than one: show the name, label, and type of each candidate and ask the user before you read data. Do not select a device only because its name is similar. In the answer, state the device name and label.
4. Call get_string_daily_analytics with view for_date and date D. D is a Plant-local date. Use yesterday if no date is given. Rank strings by normalized power across the Plant and within each inverter. The lowest strings are candidates. Call a string weak only with the peer value it was compared with; state that value. If an inverter is given, review candidates from that inverter. A candidate is a hypothesis, not a fault.
5. For missing rows or null values, say 'no reported value'. Never show 0 for missing data. If D is older than about 72 days, say string data at 5min is not kept for that date. Stop for that date.
6. Call query_string_5min with metrics Idc and Udc, and inverterIds set to the candidate's inverter ID. Use D 00:00 to the next day 00:00 in Plant time at 15min. Then use 11:00 to 13:00 on D at 5min. For 15 strings, expect about 735 rows for the day and 360 rows for two hours. The tool refuses more than 1,000 rows. If refused, narrow the window. Reuse these rows for all candidates in that inverter.
7. At the same timestamps, compare each candidate's Idc and Udc with its MPPT pair and the inverter median. If the MPPT pair is not known, say it was not checked. Report patterns only. Low Idc with normal Udc, low Udc, or zero Idc while peers are not zero are observations. Zero Idc can suggest a disconnection. Low values for only part of the day can suggest shading or a time-bound cause. Give possible causes as hypotheses. Never confirm a cause.
8. Report the Plant, D, timezone, inverter, candidates with values and units, peer comparison, coverage, and ranked next site checks. State each limit below.

## Limits

NOT CHECKED in every answer: work orders, irradiance per string, module temperature, I-V curve, site inspection. Not read by this procedure; read only if the user asks: alarm history (list_alarms).
