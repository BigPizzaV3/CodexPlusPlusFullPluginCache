# InvestorLists

The InvestorLists agent for startup founders raising capital. It connects ChatGPT to the InvestorLists database of US startup investors: VCs, corporate VCs, family offices, syndicates and accelerators, with their decision-makers, verified contacts, latest news and the latest fund on record from SEC filings. The database is updated monthly with new funds, news and SEC filings.

## What it does

- **Raise profile.** Reads your website, deck and LinkedIn profile URL and drafts a short profile of your company and your round. Only the version you approve is saved.
- **Investor shortlists.** Builds a pool of relevant firms from the whole database, then the firms to aim for first, with a sourced reason for each firm.
- **Investor briefs.** One to five firms: what they back, latest news, portfolio and possible conflicts, decision-makers, and meeting prep.
- **Path to connect.** One firm at a time: who can introduce you, and the direct paths (verified work emails, LinkedIn profiles, the firm's own submission form).
- **Investor messages.** Your pitch message, cold emails, LinkedIn messages, intro requests, follow-ups and replies, written for you to review.
- **Pipeline memory.** Where every investor stands, what is due, and what changed in the database for the firms on your lists.

## How to start

1. Add InvestorLists in ChatGPT.
2. In a new conversation, type: **Hi InvestorLists, let's get started.**
3. Sign in on investorlists.vc with the code emailed to you and approve the connection.

## What is inside

| Part | Purpose |
|---|---|
| `plugin.json` | Manifest and listing information. |
| `mcp.json` | One remote server: the InvestorLists MCP server at https://investorlists.vc/mcp, OAuth sign-in on investorlists.vc. The package holds no keys, tokens or secrets. |
| `skills/investorlists-agent` | The front door: onboarding on the first conversation, then where you stand and one next step. |
| `skills/il-shortlist` | Investor Shortlist. |
| `skills/il-brief` | Investor Brief. |
| `skills/il-path-to-connect` | Path to Connect. |
| `skills/il-messages` | Investor Messages. |
| `skills/il-pipeline` | Raise Pipeline, read from your notes. Includes `scripts/parse_notes.py` (Python 3 standard library, local files only, no network). |

## Data handling

**Sent to InvestorLists:** your sign-in email, the searches you run and the ids of the firms you open, and what you choose to save (lists, one-line notes per firm, workspace notes such as your approved raise profile). You can see, edit and delete them in your portal at investorlists.vc.

**Never sent to InvestorLists:** your deck or website text, your mailbox or calendar, investor replies, and your conversations.

Privacy policy: https://investorlists.vc/terms-of-service-and-privacy-policy#privacy
Terms of Service: https://investorlists.vc/terms-of-service-and-privacy-policy#terms

## Support

office@investorlists.vc. Documentation: https://investorlists.vc/ai

## License

Proprietary. Copyright 2026 Chosen V. Inc. All rights reserved. See LICENSE.
