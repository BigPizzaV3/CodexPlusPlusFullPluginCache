# Investminder MCP Server — AI investment research, strategy backtesting and portfolio tracking

[![MCP](https://img.shields.io/badge/MCP-remote%20server-6E56CF)](https://modelcontextprotocol.io)
[![Transport](https://img.shields.io/badge/transport-Streamable%20HTTP-0A7EA4)](#connection-details)
[![Auth](https://img.shields.io/badge/auth-OAuth-2EA44F)](#authentication-and-security)
[![Website](https://img.shields.io/badge/website-investminder.com-111111)](https://www.investminder.com)

**[Investminder](https://www.investminder.com)** is an independent investment strategy platform for individual investors. The **Investminder MCP server** brings it into your AI assistant through the [Model Context Protocol](https://modelcontextprotocol.io): ask Claude, Claude Code or ChatGPT to search stocks and ETFs, screen the market, compare securities, build a rules-based investment strategy, backtest it on historical data and keep track of your portfolios — in plain language.

```text
https://api.investminder.com/mcp
```

> One URL, no install, no API key. On Claude, add **[Investminder from the Claude directory](https://claude.ai/directory/investminder)**; on Claude Code and ChatGPT, add the URL above. Sign in to Investminder and start asking.

---

## Contents

- [What you can do](#what-you-can-do)
- [Quick start](#quick-start)
- [Example prompts](#example-prompts)
- [Available tools](#available-tools)
- [Connection details](#connection-details)
- [Authentication and security](#authentication-and-security)
- [Plans and limits](#plans-and-limits)
- [FAQ](#faq)
- [Support](#support)

---

## What you can do

| Use case | What you ask your assistant | Tools behind it |
|---|---|---|
| **Find a stock or an ETF** | "Find the MSCI World UCITS ETFs and give me their fees" | `searchSecurities` |
| **Analyze a security** | "Show me Apple's revenue, margins and dividends over 10 years" | `analyzeSecurities` |
| **Screen the market** | "S&P 500 stocks with ROE above 20 % and a P/E under 15" | `screenSecurities`, `listScreeners` |
| **Check diversification** | "How correlated are SPY, QQQ, GLD and TLT since 2015?" | `getCorrelationMatrix` |
| **Start from a proven strategy** | "Show me passive, highly diversified ETF strategies" | `listPreBuiltStrategies` |
| **Build your own strategy** | "Create a 60/40 ETF portfolio rebalanced every quarter" | `createStrategy`, `updateStrategy` |
| **Backtest it** | "Backtest it from 2008 with $10,000 plus $300 a month, against SPY" | `startBacktest`, `listBacktests` |
| **Track your portfolio** | "Create a GBP portfolio and record my 50 shares of ULVR.L at £45" | `createPortfolio`, `addPortfolioPosition`, `addPortfolioCash` |
| **Sync your broker** | "Connect my brokerage account" | `listInstitutions`, `connectPortfolio` |
| **Get started** | "What can Investminder do for me?" | `startOnboarding` |

Coverage includes stocks, ETFs and forex listed in the United States (Nasdaq) and on the London, Frankfurt, Paris, Amsterdam, Madrid and Zurich exchanges, with constituents of the S&P 500 🇺🇸, Nasdaq-100 🇺🇸, Russell 2000 🇺🇸, MSCI World 🌍, STOXX Europe 600 🇪🇺, Euro Stoxx 50 🇪🇺, CAC 40 🇫🇷, DAX 🇩🇪, FTSE 100 🇬🇧, IBEX 35 🇪🇸, AEX 🇳🇱 and SMI 🇨🇭, and UCITS 🇪🇺 / PEA 🇫🇷 eligibility filters for European investors.

Responses are available in **English, French, Spanish and German**.

---

## Quick start

The server is a **remote MCP server** (Streamable HTTP). It is supported on Claude, Claude Code and ChatGPT.

- **Claude** (web, desktop and mobile): open **[Investminder in the Claude directory](https://claude.ai/directory/investminder)** and connect it.
- **Claude Code**: `claude mcp add --transport http investminder https://api.investminder.com/mcp`
- **ChatGPT** (web): in [Plugins](https://chatgpt.com/plugins), click **+ → Add custom MCP server** with the URL `https://api.investminder.com/mcp` and OAuth authentication.

Then sign in to Investminder and ask: *"What can Investminder do for me?"*

Step-by-step setup and troubleshooting for each client: [docs/clients.md](docs/clients.md).

---

## Example prompts

Copy any of these into your assistant once the connector is enabled:

- *"Start the Investminder onboarding and recommend a strategy that fits me."*
- *"Find UCITS ETFs that track the S&P 500, listed in Amsterdam or Frankfurt, and compare their 5-year performance."*
- *"Screen Nasdaq-100 stocks with a gross margin above 60 %, debt/equity below 0.5 and positive 12-month momentum."*
- *"Give me Microsoft's quarterly income statements and P/E history since 2019."*
- *"Compute the correlation matrix of VWCE.DE, EUNA.DE, IGLN.L and SPY over the last 5 years and tell me what actually diversifies."*
- *"Take the best-rated trend-following pre-built strategy, swap its ETFs for UCITS equivalents and backtest it from 2007 against SPY."*
- *"Build a dividend strategy on 5 ETFs, buy when RSI 14 drops below 35, and backtest it with $500 a month."*
- *"Show me my portfolios with their positions and cash."*

More recipes, from first steps to advanced strategy design: [docs/examples.md](docs/examples.md).

---

## Available tools

| Tool | Description | Investminder profile needed |
|---|---|---|
| `startOnboarding` | Guided introduction and first steps | No |
| `upsertUser` | Create or update your Investminder profile (country, currency, language, investor profile) | No |
| `searchSecurities` | Find stocks, ETFs and forex pairs by name, ticker or ISIN | No |
| `screenSecurities` | Filter securities on fundamentals, valuation, momentum, index, country, UCITS 🇪🇺 / PEA 🇫🇷… | No |
| `analyzeSecurities` | Quotes, performance, technical indicators, volume profile; financial statements, dividends and P/E history | Partly |
| `getCorrelationMatrix` | Pearson correlation of daily returns for 2 to 20 tickers | No |
| `listScreeners` | Your saved screeners | Yes |
| `listPreBuiltStrategies` | Catalog of ready-made strategies, filterable by approach, diversification and activity | Yes |
| `createStrategy` / `updateStrategy` / `deleteStrategy` | Build and edit rules-based strategies (rebalanced or progressive) | Yes |
| `listUserStrategies` | Your strategies and their drafts | Yes |
| `startBacktest` / `listBacktests` | Run a backtest with contributions and withdrawals, then read its results vs. a benchmark | Yes |
| `createPortfolio` / `addPortfolioCash` / `addPortfolioPosition` | Track a manual portfolio | Yes |
| `listPortfolios` / `listPortfolioTransactions` | Read portfolios, positions, cash and history | Yes |
| `listInstitutions` / `connectPortfolio` | Connect a broker or bank, read-only, through a hosted flow run by licensed open banking partners. Investminder never sees your banking credentials | Yes |

Full reference with parameters and tips: [docs/tools.md](docs/tools.md).

---

## Connection details

| | |
|---|---|
| **Server URL** | `https://api.investminder.com/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | OAuth (sign in with your Investminder account) |
| **Languages** | en, fr, es, de |
| **Local install** | None — the server is hosted by Investminder |

---

## Authentication and security

- You sign in on Investminder's own page. Your assistant never sees your password.
- **Investminder has no access to your banking information.** Broker and bank connections go through two licensed open banking partners, [Powens](https://www.powens.com) 🇪🇺 and [SnapTrade](https://snaptrade.com) 🇺🇸: you authenticate on their hosted authorization page, never on Investminder's.
- **Broker and bank access is read-only.** Investminder can read your positions, cash and transactions to keep your portfolios up to date. It cannot move money or place orders.
- **Never send banking information in a chat, and never send it to the Investminder team** (password, code, card number, IBAN…). Neither the assistant nor anyone at Investminder will ever ask you for it.
- Every tool is scoped to the signed-in account: an assistant can only read and change your own strategies and portfolios.
- **Investminder never places orders.** It helps you decide; your broker executes. See [the place of Investminder in your financial ecosystem](https://help.investminder.com/en/how-to-use/the-place-of-investminder-in-your-financial-ecosystem-1wm3ccl/).

This repository contains documentation and configuration examples only. The server itself is closed source and operated by Investminder.

---

## Plans and limits

Market data tools (search, screening, quotes, performance, technical indicators, correlation) work as soon as you sign in, even before you create your Investminder profile. Financial statement and dividend history depth, the strategy catalog, the number of strategies, backtests, portfolios and broker connections depend on your Investminder plan. When a limit applies, the assistant tells you.

Compare the plans on **[investminder.com/pricing](https://www.investminder.com/pricing)**.

---

## FAQ

**What is an MCP server?**
The [Model Context Protocol](https://modelcontextprotocol.io) is an open standard that lets AI assistants call external tools. The Investminder MCP server exposes Investminder's market data, strategy builder, backtesting engine and portfolio tracker as tools your assistant can use.

**Do I need an Investminder account?**
You sign in once when you connect, which identifies you to Investminder. Market data tools work right away. To build strategies or track portfolios you also need an Investminder profile (country, currency, language): the assistant creates it for you through the onboarding.

**Which AI assistants are supported?**
Claude (web, desktop and mobile, from the [Claude directory](https://claude.ai/directory/investminder)), Claude Code and ChatGPT.

**Is it financial advice?**
No. Investminder provides data, analysis and simulation tools. Past performance and backtests do not guarantee future results. Decisions and their execution remain yours.

**Can the assistant trade for me?**
No. Investminder has no order execution. It records the trades you tell it about and synchronizes the accounts you connect, but it never sends orders to your broker.

**Where does the data come from, and how fresh is it?**
Every `analyzeSecurities` response carries `earliestDate` and `latestDate`, the first and last known quote dates of the security, so you always know the as-of date of the data.

---

## Support

- Website: **[investminder.com](https://www.investminder.com)**
- Claude connector: [Investminder in the Claude directory](https://claude.ai/directory/investminder)
- Help center: [help.investminder.com](https://help.investminder.com/en/)
- Getting started: [complete your onboarding](https://help.investminder.com/en/onboarding/how-to-complete-your-onboarding-and-get-your-first-strategy-recommendation-90expl/)
- Strategy builder: [how to build a strategy](https://help.investminder.com/en/how-to-use/how-to-build-a-strategy-ez04de/)
- Contact: email [support@investminder.com](mailto:support@investminder.com), or use the chat assistant once signed in to your Investminder account

---

<sub>Investminder is not a bank, a broker or an investment advisor. Content provided for information purposes only. Investing involves risk of capital loss.</sub>
