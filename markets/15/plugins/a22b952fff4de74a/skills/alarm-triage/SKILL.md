---
name: "alarm-triage"
description: "Review active alarms for one accessible Plant. Read-only. Compare alarm details with device telemetry. A read does not acknowledge or clear an alarm."
---

# Alarm triage

Use only the tools this server lists. Read-only.

## Procedure

1. Find the Plant: search_plants if the user names one, else list_accessible_plants. Use only a returned Plant ID. If exactly one result name is the same as the user's Plant name (any letter case), use it. If the user gives only the end of a Plant code, for example P043 or PR043, and not a full code such as NORTH-P043: search with the digits only, for example 043. If codes with different prefixes contain those digits, show all of them and ask. No match: stop and say so. Several matches: ask the user. If a tool returns the FORBIDDEN error, stop and say so; do not try another Plant ID.
2. Times: a clock time with no zone is Plant time. If the user names a zone, change the time to Plant time and state the two times. SG is UTC+8. VN is UTC+7.
3. Call list_alarms with status active. Use date D, or today in Plant time. Set start to D minus six days at 00:00 and end to the next day after D at 00:00, with Plant offsets. If the timezone is missing, ask for it. The window filters alarm creation time, not all alarms still active. Start at page 0. Read more pages while total says more, at most three pages. Say if more remain. If the user asks for history, repeat with status cleared in the same window and the same page limit. If the user asks about one device in a time window, use status all for that window.
4. Group alarms by device and alarm type. Order by severity, highest first, then start time, newest first.
5. Find the device: list_devices, with nameQuery when the user names a device. nameQuery matches the name and the label; letter case, spaces, and separators are ignored. Use only a returned device ID. Exactly one match: use it. No match: call list_devices again without nameQuery and use the devices with a similar name or label as candidates. No match or more than one: show the name, label, and type of each candidate and ask the user before you read data. Do not select a device only because its name is similar. In the answer, state the device name and label.
6. If a device is named, keep only alarms for its resolved ID. Call get_alarm for the top items with returned alarm IDs and the resolved Plant ID. Call query_device_telemetry for each alarm's device on the alarm day. Compare the curve around the start time. Reuse each device's day curve. A key with status no_points is not proof that the device has no data. If the reply gives a suggestion, call again with that key and state both keys. Otherwise, select a key from deviceKeys or say the key is not on the device. State the key you used. Null means no reported value, never 0 or the previous value. If a fault code is not zero in the window and list_alarms has no alarm for that device, report 'code seen, no alarm raised'. State coverage and warnings.
7. Report alarm, device, severity, status, start and clear time in Plant time, what the curve shows, and open questions. Do not treat a missing clear time as a real timestamp. An alarm that is not in the list is not 'cleared'. A duration from telemetry is a range between two sample times; state both times. Causes are hypotheses. Never say this read acknowledged or cleared an alarm. State each limit below.

## Limits

NOT CHECKED in every answer: work orders, site inspection, alarm rule configuration.
