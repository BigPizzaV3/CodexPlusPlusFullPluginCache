---
name: "daily-portfolio-check"
description: "Screen accessible Plants and review at most five flagged Plants. Read-only. Status is live and today. State the time of the read."
---

# Daily portfolio check

Use only the tools this server lists. Read-only.

## Procedure

1. Call list_accessible_plants. Use only returned Plant IDs. If date is omitted, use today in each Plant's timezone. If a timezone is missing, ask for it. Group Plants by date within the plantIds limit. Call get_portfolio_dashboard for each group with views site_overview, last_7_days_yield, devices_status_summary, and alarm_status. List Plants with low PR, low availability, offline devices, or active alarms. A supplied date anchors the yield window; status remains live.
2. Order flagged Plants by the size of the gap against the reported reference. State the reference and units. Do not compare gaps with unlike units. If no reference is reported, say the gap is not checked. Select at most five Plants for detail.
3. For each selected Plant, call get_plant_dashboard with views devices_detail and disconnected_strings. Name the offline or weak devices. Reuse each view's rows for all devices in that Plant.
4. For missing values, say 'no reported value'. Never show 0 for missing data. Data is live and today. State the time of the read, each Plant-local date, timezone, coverage, and warnings.
5. Report a table with Plant, issue, value with unit, and devices. Give next checks per Plant: string-fault-review for weak strings and plant-performance-review for low PR. Use alarm-triage for alarm detail only if it is served. State each limit below.

## Limits

NOT CHECKED in every answer: work orders, site weather. Not read by this procedure; read only if the user asks: alarm detail (get_alarm).
