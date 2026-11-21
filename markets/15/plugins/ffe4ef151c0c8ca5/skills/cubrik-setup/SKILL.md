---
name: cubrik-setup
description: First steps with cubrik in this AI app. Use when the user has just connected cubrik, asks what cubrik can do here, asks how to get started, how to connect a broker or exchange, why a tool says no platform is connected, or what their plan allows. Reads the account (plan, credits, agents, connected platforms) and walks the user to the next useful step — connecting a platform in cubrik, a first backtest, a first agent or a Library copy — without asking for any key or password in the chat.
---

cubrik runs AI trading agents on the brokers and exchanges a person connects to their cubrik
account, and backtests trading ideas on historical candles. This app reaches that account through
cubrik's tools. Start from what the account actually holds, then offer one next step.

## 1. Read the account

Call `get_account` and `list_platforms` (both read-only, no credits).

- `get_account` gives the plan, the credits left this month and when they renew, how many agents
  may be active and how often they may run.
- `list_platforms` gives every connected broker or exchange, its status and whether agents can use it.

## 2. Say where they stand, in two or three lines

- Plan and credits, plainly: "You are on Demo: 125 credits this month, 1 active agent, 1 platform."
- What is connected: name the platforms, or say that none is connected yet.
- What already exists: if `list_agents` shows agents, name how many are active.

## 3. Offer the one step that fits

| Where they are | Offer |
|---|---|
| No platform connected | Connecting one, in cubrik: call `connect_platform` (optionally with the platform's name) and give the link it returns. Keys and sign-ins are entered on that page, never in this chat. |
| A platform, no agent | A backtest of an idea they have (skill `cubrik-backtesting`), or a ready-made agent from the Library (skill `cubrik-library`). |
| Agents running | A check of how they are doing (skill `cubrik-performance-review`) or of the open positions (skill `cubrik-portfolio-check`). |

## Rules

- Never ask for an API key, a password, a seed phrase or a card number in the chat, and refuse one
  if the user pastes it: tell them to remove it and to connect on cubrik's page instead.
- No tool moves money into or out of an account; deposits and withdrawals happen at the broker.
- Plan limits are cubrik's: when a tool refuses for the plan (an agent limit, a schedule too fast,
  credits), say what the limit is and what can be done within it. Do not invent prices.
- cubrik is a tool for running the user's own strategies. It does not give investment advice, and
  neither do you on its behalf.
