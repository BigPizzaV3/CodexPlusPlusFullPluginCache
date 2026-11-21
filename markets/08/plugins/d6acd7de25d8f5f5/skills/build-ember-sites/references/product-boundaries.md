# Ember product boundaries

Use live MCP results for account, site, entitlement, usage, credit, and URL
facts. Product behavior here is durable guidance; `get_account` and `get_site`
override it whenever they differ.

## What Ember builds

Ember is for public, static content sites: marketing and service sites,
landing pages, blogs, documentation, portfolios, menus, event and project
collections, knowledge bases, and similar multi-page sites. It supports
responsive accessible layouts, structured Markdown collections, uploaded
imagery, visitor downloads, small vanilla-JavaScript enhancements,
third-party embeds, working forms that submit to the site's Forms inbox, and
gated access: shared-code protected paths and members-only areas where named
members the owner manages sign in with an emailed link (see the authoring
reference).

The host may research or fetch information while building. The finished site
stores that information as authored content; it does not stay connected to the
source.

Ember is not a visitor-facing application platform. Do not promise open
visitor registration (member areas admit only the owner-managed roster — no
self-signup), a live database, runtime server queries, custom API endpoints,
background jobs, React/Vue/Svelte hydration, native shopping carts, payment
processing, or custom form backends. A third-party embed may be an honest
workaround when it fits; explain that boundary. Member rosters are not editable
through these tools: the owner adds or removes members in the Ember builder under Site Settings →
Members, by asking the Ember chat agent (its `membership` tool), or with the
`ember sites members …` CLI. Adding members needs a plan with member-only
areas, even though building and previewing the area is free.

## Draft, publish, and management

The preview always shows the latest working tree. Public URLs serve the most
recent successful published snapshot, so editing does not change the public
site until the user publishes again. A failed check or publish leaves the
previous public snapshot intact.

Use `get_site` for the published URL, name, address, and design status. Use
`render_preview` for the private working tree. Its returned `previewUrl` is a
short-lived authenticated link that may be shared when the embedded view is
unavailable; call `render_preview` again after it expires. The raw builder
address remains internal and must never be invented or exposed. Use
`update_site` to rename a site, set/clear a vanity subdomain, or select an
attached hostname as the default used in site emails and links. Setting an
address does not publish. Use `list_sites` for selection,
and confirm before `delete_site`; deletion is soft and recoverable from Ember's
dashboard.

Use `get_account` for current plan, credits, limits, remaining capacity, and
publish eligibility. Never infer entitlements from a plan label or quote a
memorized price. If a server action returns a plan gate, explain the gate and
do not retry it in a loop.
