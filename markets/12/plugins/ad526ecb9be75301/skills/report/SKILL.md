---
name: report
description: Read measured Casually project results or save a campaign report for an explicit reporting period.
---

# Report actual results

Find the selected project/workflow with the available Casually tools. Use real IDs and the connected member's permissions.

For a read-only overview, use `get_project_performance` and state that its scope is all-time. For a saved campaign report, use `analyze_marketing_workflow` with explicit from/to timestamps and a stated timezone. That operation saves a report and its history; do not describe it as read-only. Clarify materially ambiguous dates.

Report only the actual queue, sends, measured opens/clicks, page views and form conversions returned. Keep missing rates null when denominators are missing. Distinguish queue acceptance, recorded send and confirmed inbox delivery. Do not infer revenue or causal lift from incomplete tracking, and do not attribute all LP conversions to email.

Include the reporting period, saved state and returned result links. Give a brief interpretation supported by the measurements and their limitations. Reporting does not authorize media generation, a campaign launch, changes to recipients, or spending on generation.
