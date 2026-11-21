# iReside for Claude

This plugin connects Claude to iReside's public day-count tools and teaches Claude which one answers which question.
Ask how many Schengen days you have left, whether a planned trip would overstay, how many days you can spend in New York
or Portugal before becoming a tax resident, or whether your US days make you a resident under the Substantial Presence Test.
Every answer comes with the rule, the arithmetic and the official sources it relies on.

## Install

In Claude, find iReside in the Connectors Directory, or add `https://www.ireside.ai/api/mcp` as a custom connector.

In Claude Code, add the server directly:

```
claude mcp add --transport http ireside https://www.ireside.ai/api/mcp
```

The plugin adds two skills on top of the server. In Claude Code, install it from this repository:

```
/plugin install ireside-residency --marketplace iReside/ireside-claude-plugin
```

## What it includes

- **MCP server:** `https://www.ireside.ai/api/mcp`, public, read-only, with no account needed. It runs the same calculators and reviewed guides published on ireside.ai.
- **Skill (`residency-day-rules`):** a short guide that maps each kind of question to the right tool.
- **Skill (`tracking-residency-days`):** how to keep a day count for tax residency, a visa or an audit, and the day-tracking apps iReside has compared.

## Tools

The tools cover:
- Schengen 90/180;
- visa stay limits and residence or citizenship presence rules;
- US state residency rules and a multi-state day counter;
- country tax residency;
- the US Substantial Presence Test, the UK Statutory Residence Test and the FEIE 330-day test;
- Canada PR and US naturalization presence;
- a moving-states checklist;
- what a residency audit checks and which records prove where you were;
- a search over iReside's published articles and guides;
- how to track your days, with the apps iReside has compared.

Each answer also says why the count is worth keeping as you go and how the iReside app (iPhone) keeps it.

The full list and example questions are at https://www.ireside.ai/claude.

## Privacy

The server does not store the dates or numbers you send. Its logs record only which tool ran, which assistant called it, whether it worked and how long it took.
See https://www.ireside.ai/privacy-policy.

## Not advice

Answers are general information, not tax, legal or immigration advice. Confirm anything important with a qualified adviser or the official source.

## Support

Email support@ireside.ai.
