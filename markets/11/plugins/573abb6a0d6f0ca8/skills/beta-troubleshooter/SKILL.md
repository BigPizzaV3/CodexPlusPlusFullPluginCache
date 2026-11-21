---
name: beta-troubleshooter
description: Diagnose SigRank | SignalAF plugin or board beta problems, prepare reproducible bug reports, and submit a user-approved report to SignalAF support when the reporting tool is available.
---

# SigRank | SignalAF beta troubleshooter

Use this skill when a user reports a broken plugin tool, wrong board result, login problem, missing metric, or confusing SigRank answer. First identify the surface (ChatGPT, Codex, or website), requested window and board view/category when relevant, expected behavior, actual behavior, exact error code if already visible, and the smallest repeatable steps. Check live public facts with the available read-only tool before declaring a data bug. Do not treat an illustrative table, search snippet, cached result, or model-generated number as a live board placement.

Offer a concise explanation or workaround when supported. If the issue appears unresolved, draft a report with a short summary, 1–5 steps, expected and actual behavior, surface, plugin version if known, and the relevant tool/window if known. If the user did not identify the failing surface, mark it unknown and ask before sending rather than choosing website or plugin as fact. Show that draft to the user. Do not request or include credentials, raw logs, prompt or conversation contents, private telemetry, or another person's identifying data. A reply email is optional and must be supplied by the user; do not infer it from an account.

**Send only after the user explicitly asks to submit the displayed report.** If `report_beta_bug` is exposed, call it with `consent_confirmed: true` only then. Report the returned `SRB-...` reference and destination `hello@signalaf.com` only on a successful tool result. If the tool is absent or delivery fails, say that no report was confirmed sent and provide [SignalAF's contact form](https://signalaf.com/contact) plus the copyable draft. Do not retry automatically after an uncertain delivery result.

For an intentional beta delivery test, clearly label the summary **BETA DELIVERY TEST — no incident**, describe the test steps and expected reference, and state that delivery has not yet been attempted. Do not turn a hypothetical board-loading failure into a factual incident when live reads succeeded. Show the exact payload and obtain the same explicit approval as a real report. A success reference confirms the tool's delivery success path; receipt at the support inbox requires recipient-side confirmation. Do not retry an uncertain send automatically.

This is support triage, not a measurement or verification path. Never submit a profile, change a rank, or mark telemetry verified while troubleshooting.
