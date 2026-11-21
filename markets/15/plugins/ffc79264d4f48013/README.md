# Guide for Sales Navigator

Helps an agent use and explain LinkedIn Sales Navigator: account and lead search, Boolean filters, lists, alerts, InMail, CRM integrations, SSO, licenses, billing and troubleshooting. It works from 421 paraphrased notes on the public Sales Navigator help articles, each linking to its source, dated 2026-11-05.

This is an independent project. It isn't affiliated with or endorsed by LinkedIn. LinkedIn and Sales Navigator are trademarks of LinkedIn Corporation. The notes are a dated snapshot, so check LinkedIn's current documentation for anything that may have changed.

## Install

In Claude Code:

```
/plugin install linkedin-sales-navigator --marketplace khalidsaidi/skills
```

With the `skills` CLI:

```bash
npx skills add khalidsaidi/skills --skill linkedin-sales-navigator
```

## Example prompts

- "Find VP-level finance buyers at US logistics companies with 200 to 1,000 employees, and save the search."
- "Why can't this user see the Salesforce sync settings? Walk me through what to check."
- "What's the difference between an InMail, an Open Profile message and a first-degree message?"
- "Set up SCIM provisioning with Okta. Which fields stay controlled by the identity provider?"

## What it runs and sends

- **Scripts:** none. The skill is made up of instruction and note files.
- **Hosted service:** this version connects to a read-only service at https://khalidsaidi-skills.vercel.app/linkedin-sales-navigator/mcp. It receives your search text, article IDs and Boolean queries so it can return results. It has no sign-in and does not connect to LinkedIn.
- **Data:** the prospecting workflow can have your agent record the names, roles and related evidence of prospects in a workbook wherever it saves its work. See [PRIVACY.md](PRIVACY.md).
- **LinkedIn account:** the skill doesn't include a browser or LinkedIn connection. If your agent already has access to your account, the skill guides how it works there. It requires your approval of the recipients and text for each batch of messages, invitations or introduction requests.
- **External links:** the notes link to LinkedIn and vendor documentation. They're reference material, and the agent may open them to check current details if it has web access.

## Support

Report problems at [GitHub Issues](https://github.com/khalidsaidi/skills/issues).

## License

[MIT](https://github.com/khalidsaidi/skills/blob/main/LICENSE)
