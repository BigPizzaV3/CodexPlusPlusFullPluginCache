---
name: create-creatives
description: Generate ProductByte product images and carousel decks from catalogue products and brand playbooks. Use for standalone creative briefs or campaign assets; generating an asset does not itself create posts.
---

Use the ProductByte MCP tools from this plugin. Tool names below are the server names; use the corresponding names exposed by the host.

- Use the selected project, or read `workspace-get` and resolve it by name before generation. Read `playbook-list` for its creative direction and `channel-list` when the asset has a publishing destination.
- Resolve product references through `product-semantic-search`, or inspect `product-field-list` before field-based `product-search`. Use `product-get` for details needed by the brief. Choose products with the customer when their reference is ambiguous, and use verified catalogue facts for claims in the creative.
- Carry forward the customer's actual goal, products, offer, copy language, visual direction, format and asset count. Ask for missing choices that affect the result. A request for a carousel means a deck, not several unrelated stills; keep the requested slide count within the generation tool's limits.
- Apply playbooks with `auto_select` when their descriptions fit. Use other playbooks when named by the customer. Pass the applicable `brief.image` or `brief.carousel` as generation `instructions`, use relevant picture keys as `playbook_pictures`, and include the complete current brief in `prompt`: the composer cannot read the chat or fetch playbooks itself.
- When the customer asks to save how their brand looks or sounds, change a fitting playbook or create one with `playbook-put` after they confirm.
- Call `creative-still-create` once per requested still or `creative-carousel-create` once per requested deck. Pass returned product IDs and the required ratio. A request to find or reuse an existing asset goes through `creative-list` instead.
- Save the returned generation and creative IDs. Follow generation events when the host supports them; check with `creative-generation-get` when the event arrives or the customer asks for progress. A running generation is still composing, and a failed or uncertain response does not authorize another paid generation.
- When creating posts was also requested, attach the returned creative ID without waiting, as the generation tool instructs. For an image-only request, return the asset or its generation status without creating a campaign or post.
- Report each requested asset's actual state. A request to revise a result needs a new complete brief carrying the requested changes and the original constraints; use only revision or reference inputs supported by the available tool. Explain when a new generation is required rather than claiming to have edited the existing asset.
