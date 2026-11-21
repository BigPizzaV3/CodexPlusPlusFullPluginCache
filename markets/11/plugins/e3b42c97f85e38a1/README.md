# IRM365

IRM365 is the CRM for real-estate brokerages in the UAE. This plugin connects Claude to your IRM365 account, so you can ask about your work in plain language. For example: which follow-ups are due today, which hot leads have gone quiet, what is in your pipeline, and what your team has been doing.

## What's included

- **IRM365 connector**, at `https://mcp.irm365.com/mcp`. It has read-only tools for leads, follow-ups, opportunities, activities, your team, and the workspace you are signed in to.
- **Skills**:
  - `get-started` explains what the connection can see.
  - `daily-briefing` builds a morning plan from overdue and due-today follow-ups, hot leads and deals closing this week.
  - `pipeline-review` summarises opportunities by stage, value and close date, and points out deals at risk.
  - `team-followups` shows a manager who in their team has overdue follow-ups.

## Use it

1. Add the plugin, then connect IRM365 from the plugin's Connectors tab.
2. Sign in with your IRM365 work email and password, and pick your company.
3. On the consent screen, choose which areas to share.
4. Then ask, for example, "What follow-ups do I have today?" or "Review my pipeline for this month."

Your company must have AI assistants switched on in IRM365 settings, and you need permission to use them.

## Data and privacy

- **What Claude sees:** only records you can already see in IRM365. An agent sees their own leads and a manager sees their team. Nothing from another company is ever reachable.
- **Read-only:** the connector never creates, changes or deletes anything.
- **What it does not send:** the dedicated phone and email fields of leads and customers.
- **Free text:** activity titles are sent as people typed them, and so are activity notes when your company switches them on and you tick them at consent. Anything typed there, including a phone number or email address, can reach Claude.
- **Where data goes:** it travels only between IRM365 (`mcp.irm365.com`, signed in through `auth.irm365.com`) and Claude. The plugin itself stores nothing and runs no code on your computer.
- **Control:** your company admin can see every connection and disconnect it at any time, and you can disconnect from IRM365 or from Claude.

Read the [privacy policy](https://irm365.com/privacy) and [terms](https://irm365.com/terms).

## Support

Contact us at support@irm365.com or through [irm365.com/contact](https://irm365.com/contact).
