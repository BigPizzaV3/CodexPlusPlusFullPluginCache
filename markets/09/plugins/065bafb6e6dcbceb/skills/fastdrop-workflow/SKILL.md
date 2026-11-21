---
name: fastdrop-workflow
description: Use when the user wants to discover FastDrop products or MCP capabilities, compare products, find alternatives or launch deals, get MCP installation instructions or launch-day status, inspect makers, submit a product, or manage a FastDrop launch.
---

# FastDrop

Use the connected FastDrop MCP server. Discover current tools and their input schemas from the server; authenticated tool availability may differ from public discovery.

## Discover products

- Use `list_launches` for leaderboards; its today/week windows are UTC.
- Use `search_products` for name, tagline, or tag searches.
- Use `find_tools` for capability searches across tool lists probed by FastDrop.
- Use `get_product` for product details and `get_maker` for public maker information.
- Use `list_reviews` and `list_comments` when the user wants community feedback.
- Use `find_deals` for deal, discount, or coupon requests. A product result may also carry a `deal`; mention it when relevant. An exclusive deal is the maker's claim, not verified by FastDrop.
- Return relevant product page links, fit to the task, and available MCP verification status. Verification reflects FastDrop's recorded probe, not a guarantee of present availability or quality.

## Compare, install, and track launches

- Use `find_alternatives` with a known product slug and limit 1-20 (default 5). Explain matches using the server's returned reasons.
- Use `compare_products` with 2-4 live product slugs. If the user has not selected products, discover candidates first. Compare pricing, open-source status, MCP verification and tools, ratings, votes, launch dates, awards and makers only when returned. Split larger comparisons into groups and explain the grouping.
- Use `get_install_config` with the product slug and optional client: `claude_code`, `claude_desktop`, `cursor`, `vscode`, `codex`, `windsurf`, `chatgpt`, or `generic`. Omitting client requests all client configurations. Preserve secret placeholders and explain where the user configures them securely. Display supported deeplinks from the result; returning a configuration does not install or connect anything.
- Use `get_launch_day_status` with a live product slug for today's UTC rank, qualifying votes, nearby competition, and time left. Account-specific participation progress may appear for authorized makers; never infer it from public data.
- `search_products` accepts text, a curated tag from its current schema, an optional x402 filter, and limit 1-50. The x402 filter finds products that accept x402 agent payments (from the x402 Bazaar catalog); FastDrop does not process or authorize payments.
- `get_maker` paginates at 50 products; follow `nextOffset` using `offset` when more are requested. Rankings can change between pages.
- `get_engagement_feed` has limit 1-20 and can be personalized after login. Report suggestions and any returned progress. Do not automatically vote, review, comment, or spend money.

## Manage a launch

Account tools (`submit_product`, `check_submission_status`, `update_product`, `recheck_mcp`, `get_my_stats`, `get_inbox`, `update_profile`, `set_deal`, `set_open_to`, and others) appear only once the user has connected their FastDrop account. Use them only when exposed by the connected server, following their actual schemas.

Gather required product details from the user and authorized sources. Do not invent ownership, features, endorsements, or submission status. Show the user the listing copy before submitting.

- If the maker gives their personal X handle, pass it as `xHandle` so FastDrop can tag them when the launch is featured. `twitterUrl` is the product's own X account only.
- If the product's MCP endpoint needs auth, the maker adds a read-only probe credential on the FastDrop website. Never ask for credentials in chat.
- Listing on FastDrop is free; there is nothing to pay or buy.
- `submit_product` with `dryRun: true` previews validation, duplicates, and the MCP probe without writing anything.
- If a tool returns `invalid_arguments`, fix the fields it names and retry.
- If `submit_product` returns `email_not_verified`, relay its message: the maker opens the verification link FastDrop emailed them (or resends it from fastdrop.dev/app), then you submit again. Don't retry before they confirm.
- A listing on the maker's own domain goes live once the DNS TXT record in the returned `domainVerification` matches; FastDrop re-checks automatically. When `submit_product` returns `stage: awaiting_dns`, relay `nextAction` and the exact record (type, name, value) to the maker in the same reply - it is the step that takes the listing live, never a footnote. The dry run already returns `domainVerification` for such URLs: mention the record before submitting. The record is required: present it as mandatory, never as optional. Only listings on shared hosts (github.io, vercel.app, ...) go through manual review instead. A queued submission is not a live listing.
- After a launch, the maker may add a launch deal with `set_deal` (the first deal is reviewed; the link must be on the product domain). Offer it; don't set it unasked.
- `set_open_to` flags a product as open to acquisition, investment, or partnership, for the FastDrop team and paid investor-edition subscribers (never public). After `submit_product`, its `askMaker` list carries this question: ask it once, and set it only with the maker's explicit answer; never infer it. Its optional revenue band, funding stage and team size are set only when the maker asks about investor visibility.

Votes, reviews, comments, and collaborator invitations require explicit user instructions. Do not create engagement automatically, or send invitations as a side effect of launch management.

## Connection and errors

The endpoint is https://fastdrop.dev/mcp. Public discovery needs no credentials. Account actions use FastDrop OAuth through the host connection flow; direct scripts can alternatively use an API key configured securely outside this package. Never ask for credentials in chat or embed secrets in plugin files.

If an account tool reports that authentication is required, direct the user to connect their FastDrop account in the host's supported flow. Do not claim authentication is complete until verified. Inspect `result.isError` as well as transport and JSON-RPC errors before reporting success. Avoid repeating an uncertain write; check its status first when possible.

Provider documentation: https://fastdrop.dev/developers

The observed public schemas are in `references/public-tools.json`. Rediscover current schemas at runtime; account-only tools are not included in that anonymous snapshot.
