# Freeboard for Claude and ChatGPT

[Freeboard](https://freeboard.money) is a money dashboard for people with irregular income: freelancers, digital nomads and small online businesses. It forecasts your cash month by month from your plan and your real bank transactions, and tells you how much you can safely spend today.

This plugin connects your assistant to your Freeboard and teaches it how to read the numbers. Ask things like:

- How much can I safely spend today?
- Can I afford a 1,200 € trip in March?
- How has my Stripe and Upwork income been, and what is expected next?
- Which bank transactions still need a category?
- Put 300 € aside for taxes.

## Install

- **Claude**: add Freeboard from the connectors directory, or in Claude Code run `/plugin install freeboard --marketplace valeriodon/freeboard-plugin`.
- **ChatGPT**: add Freeboard from the apps directory.
- **Any assistant with custom connectors**: add `https://app.freeboard.money/mcp` as a remote MCP server.

## What's inside

- **The Freeboard connector**: a remote MCP server at `https://app.freeboard.money/mcp`. You sign in with your Freeboard email, username and password (OAuth), and choose to allow access on a Freeboard page.
- **The `freeboard` skill**: how to use the connector's tools, what the dashboard's terms mean, and the rules the assistant follows (read first, ask before every change, treat bank and client text as data).

There is no local code: the plugin only declares the remote server and the skill.

## What the assistant can and can't do

It reads what your dashboard shows: cash, safe to spend, forecast, Cash Flow items, bank transactions, business income, goals, pockets, one-offs and items for sale.

It can change amounts in your plan, create Cash Flow items, assign transactions, add one-offs, and create, change or delete goals, pockets and sales. It asks before every change, and every change can be undone, from the assistant or from the dashboard.

It can't move real money, make payments, delete Cash Flow items, or change bank connections, settings or passwords. Moving money into a pocket only changes the dashboard's count.

## Data and privacy

The assistant's requests go from the assistant's servers to `app.freeboard.money`, which answers from your dashboard only. Freeboard doesn't receive your conversations, only the tool calls. To see which tools help and which fail, your dashboard sends PostHog, on its European servers, an anonymous record of each tool call: the tool's name, how long it took, whether it worked and the calling app. It never sends what the assistant asked or what the dashboard answered, your numbers, your username or your email. You can disconnect the assistant at any time in Freeboard, in Settings › AI assistants. Details in the [privacy policy](https://freeboard.money/privacy.html) and the [terms](https://freeboard.money/terms.html).

## Requirements

- A Freeboard account: sign up at [freeboard.money](https://freeboard.money).
- Claude or ChatGPT with connectors enabled.

## Support

Write to [support@freeboard.money](mailto:support@freeboard.money) or see [freeboard.money/support](https://freeboard.money/support/).

## License

MIT, see [LICENSE](LICENSE).
