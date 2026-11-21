# Tradehand

Browse and book local tradespeople. UK only.

This [Agent Plugin](https://agent-plugins.org) connects [Cursor Marketplace](https://cursor.com/marketplace) and Grok Bot to Tradehand.

**Author:** Outside HQ LTD  
**Homepage:** [tradehand.com](https://tradehand.com)

## Use

Install Tradehand from Cursor Marketplace or Grok Bot Plugins, then ask for a tradesperson near you.

MCP: `https://tradehand.com/api/mcp` (Streamable HTTP). No API key in this package. Public listings work without signing in. Booking and payment continue on Tradehand.

A prepared quote is not a booked appointment. Do not say payment is complete unless Tradehand’s MCP response says so.

## Files

- `plugin.json` — Agent Plugins 1.0.0
- `mcp.json` — Tradehand MCP
- `skills/tradehand/SKILL.md`
- `logo.png` — Tradehand mark
