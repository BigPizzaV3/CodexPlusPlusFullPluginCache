---
name: vrm
description: Answer questions about the user's Victron Energy installations (solar, batteries, inverters, GX devices) using Victron Remote Management (VRM) data - live status, energy totals, alarms, firmware, Dynamic ESS schedules, logged data and exports.
---

# Working with Victron VRM

Victron Remote Management (VRM) is Victron Energy's portal for solar, battery and inverter installations. Every call runs as the signed-in VRM user and only sees the installations that user can open in VRM.

## Find the installation first

- Most tools need an installation ID (`idSite`). Get it from `list_installations`, or use `search_installations` for large fleets or when the user gives a VRM Portal ID, device serial, product, user name or email.
- Results are paged. Keep following `next_offset` until it is null before concluding an installation does not exist.
- If the user has several installations and does not say which one, ask, or answer for all of them when that is what they want (for example "which of my sites have alarms").

## Pick the right tool

- Current values (battery SoC, voltage, power, solar, grid, AC loads, system state): `get_live_status`. To find one value, use its `filter` with a code, a description word or a D-Bus path, and page before saying it is missing.
- Energy totals in kWh for a day, week, month or year: `get_energy_stats`.
- Detailed time series: `get_data_log`, at most one day per call. List the available columns first, then pick the ones you need.
- Alarms, warnings and faults: `get_alarm_log`.
- Devices, products and firmware versions: `get_system_overview`.
- Dynamic ESS status and plan: `get_dess_schedule`.
- Files for the user: `export_data` returns a short-lived download link (up to one day) or has VRM email the export (up to a year). The user can download the file and upload it back into the chat for analysis.

## Report clearly

- Always state units (%, V, A, W, kWh) and the installation's local timezone. Use local time unless the user asks for another timezone.
- Say how old the data is when it is not current (last seen / data age).
- A missing or stale value is unknown. Never report it as zero or off.
- Not every GX setting is logged in VRM. If a value cannot be found, say it is not available in VRM rather than that it is off.
- Never invent attribute codes.
- Keep raw data in answers to what the user needs; summarise long series.

## Changes to VRM

- Only two tools change anything: `add_site` (adds an installation by its VRM Portal ID) and `clear_alarm` (clears an active alarm, recorded in the VRM event log).
- Confirm with the user before calling either one.
- They need read and write access. If VRM refuses, tell the user to reconnect the plugin and choose "Read and write".
- The plugin cannot change device settings, switch inverters or chargers, or control ESS. Say so and point the user to VRM or the GX Remote Console instead of attempting it.

## Privacy

- Never ask for the user's VRM password, API tokens or one-time codes. Sign-in happens through the plugin's OAuth connection.
