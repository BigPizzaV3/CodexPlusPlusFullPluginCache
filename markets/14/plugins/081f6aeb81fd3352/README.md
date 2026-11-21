# Lyra — weekly client status reports

**Version:** 1.1.0 · **Publisher:** Midchat · support@midchat.io · https://midchat.io/lyra/

Lyra creates weekly client status reports from your notes, bullets, or metrics: a short client email plus a one-pager
with Wins, Progress, Blockers, Risks, and Next steps (owner, action, due), followed by open questions.

## Package layout

```
lyra/
├── plugin.json · mcp.json · phrases.md · README.md
├── assets/  icon(.png|-dark) logo(.png|-dark)
└── skills/weekly-client-report/
    ├── SKILL.md
    ├── assets/report-template.md
    └── references/examples.md
```

## Hosted tools

`mcp.json` connects the Lyra MCP server at `https://lyra.mcp.midchat.io/mcp` (no sign-in). All tools are read-only:

| Tool | Purpose |
| --- | --- |
| `check_report_inputs` | Lists what to ask before drafting (client, week, owners, due dates, figures behind trend statements) |
| `resolve_report_dates` | Reporting week and due dates such as "by Friday" against today's date |
| `compute_metric_changes` | Week-over-week changes from numbers or a pasted CSV |
| `format_weekly_report` | Client email + one-pager + open questions in the Lyra template |

Report items are processed only to return the draft and are not stored. Lyra does not send email or post to other apps.

Privacy: https://midchat.io/lyra/privacy/ · Terms: https://midchat.io/lyra/terms/ · Support: https://midchat.io/lyra/support/
