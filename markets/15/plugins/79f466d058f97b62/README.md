# Zenmoney: personal finance

Zenmoney is a personal finance app and expense tracker with automatic bank sync across the EU and Eastern Europe. It keeps your bank accounts, cards and cash in one place, in any currency. Connect Zenmoney to Claude and talk about your finances in your own words. Ask about your spending, budget and savings, share what matters to you, and figure out what works for you.

## Start with a financial brief

- Daily: what's changed since yesterday and anything worth a second look
- Weekly: how this week compared to a typical one, and what to watch next week
- Monthly: money in, money out, what's left, and how your spending has shifted

Ask for a financial brief any time ("Give me my weekly financial brief"), or get it on a schedule: "Send me my daily financial brief every day at 9:00".

## Think it through together

- "Can I afford a new laptop without dipping into my savings?" → "What if I wait till payday?"
- "Why am I running out of money faster than usual?"
- "I want to save for a spring trip, but I'm not giving up coffee or the gym."
- "What did that trip actually cost me, all in?"

## Get the everyday stuff sorted

Add or edit transactions, leave notes on payments, categorise stray expenses, set up or rename accounts — just say the word. Out and about? Log it by voice in a few seconds.

## Set up

1. Add the Zenmoney plugin in Claude under **Customize > Plugins**. In Claude Code, run `/plugin` and find Zenmoney under **Discover**, or install it from this repository with `/plugin install zenmoney --marketplace zenmoney/skills`.
2. On the plugin's **Connectors** tab, connect Zenmoney, sign in to your Zenmoney account, and approve access.
3. Try: "Give me my daily financial brief."

You need a Zenmoney account with an active subscription. Connect your banks or add transactions in Zenmoney first.

### Codex

```
codex plugin marketplace add zenmoney/skills
codex plugin add zenmoney@zenmoney
codex mcp login zenmoney
```

The last command signs you in to your Zenmoney account. In Codex, your financial data is processed by OpenAI under its terms and your privacy settings there.

## Data and privacy

- The plugin contains no scripts, hooks, or other code. It adds the Zenmoney connector, which Claude reaches at `https://api.zenmoney.app/mcp`, and the Financial Brief skill, which is a set of instructions for Claude.
- Access uses OAuth. Never paste passwords or access tokens into the chat.
- Claude can read your accounts, balances, transactions, categories, merchants, budgets, and planned payments. When you ask, it can also add, edit, or delete transactions and update accounts and categories in Zenmoney. The financial brief only reads your data.
- Your financial data is processed by Claude under Anthropic's terms and your Claude privacy settings.
- To stop access, open Zenmoney under **Connectors** in Claude and disconnect it. To revoke every existing Zenmoney authorization, change your Zenmoney password.

## Troubleshooting

- **Zenmoney won't connect.** Check that your Zenmoney subscription is active, then reconnect: in Claude, disconnect Zenmoney under **Connectors** and connect it again; in Codex, run `codex mcp login zenmoney`.
- **Transactions are missing, or the brief says it can't confirm your data is up to date.** The connector doesn't sync your banks. Refresh your bank data in the Zenmoney app, then ask again.
- **A large request fails.** Ask about a shorter period.
- **The brief doesn't arrive on schedule.** Scheduled briefs need an app that supports scheduled tasks. If Claude says it can't create one, ask for the brief when you need it: "Give me my weekly financial brief."

If none of these help, contact support.

## Support

Email [support@zenmoney.app](mailto:support@zenmoney.app) with the error details and the name of your AI client. Don't send passwords, access tokens, or unredacted screenshots of financial data.

Privacy policy: https://zenmoney.app/legal/privacy/

## License

MIT
