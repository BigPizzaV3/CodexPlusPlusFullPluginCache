---
name: predis-ai
description: Create and iterate on ads and social creatives with the connected Predis.ai MCP server.
---

# Predis.ai creative workflow

Use the connected Predis.ai tools when the user asks to create or revise advertising or social-media creative. The available tools are provided by the Predis.ai MCP server; inspect their current descriptions and input requirements rather than assuming a particular tool name or parameter set.

## Workflow

1. Clarify the product, audience, channel, format, and desired number of variations when the request leaves those details ambiguous. A product URL, uploaded reference, or concise brief can be a useful starting point.
2. Use the user's connected Predis.ai account and its saved brand kit or products when relevant. Do not claim that a creative has been published; this server creates assets, while publishing requires a separate service.
3. Before starting a generation or batch that consumes credits, check the available cost and balance when the tools expose them. Tell the user the cost and wait for their go-ahead before proceeding. If the server's own tool flow explicitly obtains approval, follow it.
4. Report the result links or assets returned by Predis.ai, the formats created, and any remaining steps. Do not claim an asset was created unless the tool confirms it.

## Useful request patterns

- Create static ads from a product page in the user's brand style.
- Make product or UGC-style video ads from a product brief.
- Turn an idea or article into a carousel.
- Rebuild an ad structure from a reference.
- Create headline or opening-hook variations while keeping other creative elements consistent.
- Revise a particular frame or element in an existing video when the connected tools support it.
