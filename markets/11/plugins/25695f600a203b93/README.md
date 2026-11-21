# Domus Aedes — ChatGPT / Codex plugin bundle

The OpenAI plugin package for Domus Aedes property search. It wraps the public MCP server at `https://ai.domusaedes.com/mcp` (no auth) with one skill.

## Layout

```
plugin.json                                   portable Agent Plugins manifest (+ extensions.com.openai.interface)
mcp.json                                      portable MCP config: domus-aedes → streamable-http https://ai.domusaedes.com/mcp
skills/domus-property-search/SKILL.md         the best-matches workflow (identical to the Claude bundle)
skills/domus-property-search/agents/openai.yaml
                                              OpenAI presentation + MCP dependency for the skill
assets/icon.png                               512×512 logo used by the manifest
.codex-plugin/plugin.json + .mcp.json         compatibility overlay for hosts that predate the portable layout
```

`plugin.json` validates against `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`; `mcp.json` against the matching `mcp.schema.json`. Skills are discovered from `skills/` automatically. When `extensions.com.openai` is present the `.codex-plugin/` overlay is ignored, so the two never conflict.

## Test in ChatGPT (developer mode)

1. ChatGPT → **Settings → Security and login → Developer mode** (on).
2. https://chatgpt.com/plugins → **+** → name "Domus Aedes", a one-line description, **Connection: Public endpoint** `https://ai.domusaedes.com/mcp` → create.
3. New chat → tools menu → add the Domus Aedes connection → "Domus Aedes: find me a villa to buy in Marbella under €3M with a pool."
4. After a server redeploy: https://chatgpt.com/plugins → open the connection → **Refresh**.

## Test the full bundle locally (Codex / ChatGPT desktop)

```
codex plugin marketplace add moss1337/domus-aedes-plugin
```
or add a personal marketplace entry at `~/.agents/plugins/marketplace.json` pointing `source.path` at this folder, restart the ChatGPT desktop app, then install **Domus Aedes** from the Plugins Directory under your local source.

## Submit

Portal: https://platform.openai.com/plugins (needs the **Apps Management: Write** role). The full runbook with every field pre-written lives in the server repo under `docs/SUBMISSION.md`.

## Behaviour contract

Up to six options per search, never a list. "More" → the assistant offers refinements (budget, area, bedrooms, features) and searches again. The assistant never states how many properties Domus Aedes has. Stays with nothing available for the dates → the Domus Aedes concierge (https://concierge.domusaedes.com). Facts, prices and amenities come only from tool output.

Privacy: https://ai.domusaedes.com/privacy · Support: contact@domusaedes.com · +34 930 34 46 10
