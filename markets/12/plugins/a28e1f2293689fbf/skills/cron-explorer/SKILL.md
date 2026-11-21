---
name: cron-explorer
description: Explain numeric five-field cron and calculate upcoming runs from an explicit reference timestamp and IANA timezone.
---
Call `explore_cron` with `expression`, `timezone`, `reference`, and optionally `count` (default 5, maximum 20). Supply the timezone and timestamp explicitly; do not infer them. Timestamp includes seconds and Z or an offset. Runs are strictly after the reference.
Supported fields: minute, hour, day-of-month, month, day-of-week. Numeric wildcards, lists, ascending ranges, steps; Sunday 0 or 7. A number with a step runs from that number to the field maximum. If either day field begins with `*`, both must match; otherwise day-of-month OR day-of-week suffices (Vixie cron behavior). This distinction also applies to `*/steps`.
DST policy skips nonexistent wall times and includes both repeated instants, showing offsets. Other schedulers may behave differently. Search stops after 1,830 days and reports partial results. Reference years 1970–2095. No names, macros, seconds, years, ?, L, W, #, commands, execution, installation, or monitoring.
