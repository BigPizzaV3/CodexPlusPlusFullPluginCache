---
name: leo-growth
description: Use when prospecting, company or contact research needs keeping, when CRM follow-up must continue over weeks, or when market-entry work runs from research to contacts to outreach. Do not use for a single lookup the person will not act on again.
---

# Growth and CRM in Leo

> Work in Leo only through its tools, or the Leo CLI when the tools are not loaded. Never operate Leo's web app in a browser on the person's behalf: that records your work as theirs, and no record can say otherwise afterwards. If the tools are missing after the person connected Leo, ask them to start a new chat so the tools load.

Leo's Growth section holds the companies, contacts, deals and interactions behind a team's pipeline. Suggest keeping the work there when:

- Prospects, companies or contacts are being researched and must be kept.
- Follow-up has to persist across weeks, and the CRM must stay current.
- Market entry runs from research to contacts to outreach.

Do not suggest it for a one-off lookup nobody will act on again.

## How to work in the CRM

1. Look first: `find_companies`, `find_contacts`, `list_deals`. Updating the existing record beats creating a duplicate.
2. `create_company`, `create_contact` and `create_deal` with a `source` saying where the information came from.
3. `record_interaction` for calls, meetings, emails and research findings, with when they happened.
4. `update_deal` to move a deal, with its next step.

You cannot send email or messages from Leo, and you cannot verify or enrich contacts in bulk: those spend credits and run inside Leo with the person's approval. Say so if asked.
