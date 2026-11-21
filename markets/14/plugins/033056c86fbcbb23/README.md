# Kaus — meeting notes to action lists

**Version:** 1.1.0 · **Publisher:** Midchat · support@midchat.io · https://midchat.io/kaus/

Kaus turns meeting notes or a transcript into an action list: a table of owner, action, due date and source quote,
followed by ambiguities (missing owners, vague actions, missing dates) and draft follow-up messages you send yourself.

## Package layout

```
kaus/
├── plugin.json · mcp.json · phrases.md · README.md
├── assets/  icon(.png|-dark) logo(.png|-dark)
└── skills/meeting-actions/
    ├── SKILL.md
    ├── assets/action-table-schema.md
    └── references/extraction-rules.md
```

## Hosted tools

`mcp.json` connects the Kaus MCP server at `https://kaus.mcp.midchat.io/mcp` (no sign-in). All tools are read-only:

| Tool | Purpose |
| --- | --- |
| `find_action_candidates` | Sentences in the notes that look like commitments, with verbatim quotes and owner/due wording |
| `resolve_due_dates` | Deadlines such as "by Friday" or "EOD" against the meeting date |
| `check_action_items` | Missing or unclear owners, vague actions, missing due dates, quotes not found in the notes |
| `format_action_pack` | Action table + ambiguities + email or Slack follow-up drafts + optional CSV |

Meeting content is processed only to return the result and is not stored. Kaus does not send email or Slack messages,
create calendar events, or open tickets.

Privacy: https://midchat.io/kaus/privacy/ · Terms: https://midchat.io/kaus/terms/ · Support: https://midchat.io/kaus/support/
