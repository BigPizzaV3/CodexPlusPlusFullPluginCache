# Exayard for ChatGPT and Claude

Exayard turns construction drawings into quantities, prices and bids, right in the chat. Add a plan set and
Exayard measures and counts everything drawn on the sheets, for every trade alike. Price the quantities, build a
bid, compare two revisions of a plan set, or see which of your suppliers has the best price on a product.

## What is in this plugin

- `skills/`: short guides the assistant follows for each job: set up Exayard, take off a plan set, price a
  takeoff, build a bid, compare two revisions, and check a price.
- One connection to Exayard's server at `https://api.exayard.com/mcp/apps` (`mcp.json` for ChatGPT and other
  hosts that read Agent Plugins, `.mcp.json` for Claude).
- Two manifests: `plugin.json` (Agent Plugins 1.0, with ChatGPT's listing details under
  `extensions["com.openai"]`) and `.claude-plugin/plugin.json` (Claude).
- `.claude-plugin/marketplace.json`: makes this repository a plugin marketplace, so Claude Code, Cowork and Codex
  can install the plugin from it.
- `assets/`: the Exayard logo and icon.

The plugin holds no code. It runs nothing on your computer and sends nothing anywhere except through the one
Exayard connection above, which you sign in to with your Exayard account. What Exayard does with your data is
described in the [privacy policy](https://exayard.com/privacy).

## Install from this repository

- Claude Code: `claude plugin marketplace add exayard/exayard-plugin && claude plugin install exayard@exayard`
- Codex: `codex plugin marketplace add exayard/exayard-plugin && codex plugin add exayard@exayard`

In Claude Cowork, add `exayard/exayard-plugin` as a marketplace, then install Exayard from it.

## Getting started

Install the plugin, connect your Exayard account when asked, and say "set up Exayard". Then add a plan set to
start. Steps that use AI, such as a takeoff, show a proposal first and start only when you press Approve.

## Links

- Website: https://exayard.com
- Help: https://exayard.com/help
- Support: support@exayard.com
- Privacy policy: https://exayard.com/privacy
- Terms of service: https://exayard.com/terms

## Licence and trademarks

The files in this repository are released under the MIT licence (see LICENSE). The Exayard name and logos are
trademarks of RemoteAmbition, LLC and are not covered by that licence.
