# Seguno Email

A Cowork plugin for drafting and revising Seguno marketing emails through a guided conversation, backed by the Seguno MCP server for real store data and email actions.

## What it includes

### Skill: `seguno-email-creator`

A conversational workflow that:

- Creates a new Seguno newsletter (or works from an existing newsletter on request)
- Interviews you for newsletter goal, audience, offer, featured products or collections, CTA, tone, and timing
- Uses Seguno store search tools to ground the email in real products, collections, links, and images
- Plans a section-based email and translates the plan into `update_email` actions
- Previews the saved newsletter so you can review it and request changes

Trigger phrases include: "draft a promotional email," "build a newsletter in Seguno," "write a product launch email," "create a post-purchase feedback email," and similar.

### MCP server: `seguno`

Connects to the Seguno MCP server at `https://api.seguno.com/mcp` over streamable HTTP. Authentication uses OAuth 2.1 with dynamic client registration — the first time you use a tool that touches the server, you'll be prompted to authorize; the client registers itself automatically.

Tools exposed by the server (used by the skill):

- Newsletter editing: `create_newsletter`, `get_current_sections`, `update_email`, `preview_newsletter`
- Store search: `search_products`, `search_collections`, `search_links`, `search_images`

## Using it

After installing the plugin in Cowork, just describe the email you want. For example:

> draft a simple post-purchase marketing email aiming to get positive engagement and responses...

The skill will pick up from there — asking focused follow-ups, pulling in store data, updating the saved campaign, and walking you through a preview for review.
