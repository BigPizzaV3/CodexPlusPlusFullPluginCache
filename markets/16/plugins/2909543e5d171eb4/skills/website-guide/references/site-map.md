# Website map

Snapshot from the FindAffiliates source on 2026-10-03. Base URL: https://www.findaffiliates.online. Use live page links and controls for current behavior.

| User goal | Route or resource | Access and behavior |
|---|---|---|
| Browse programs | `/` | Directory with program search, category filters, pagination, and commission sorting. Guest and free previews are limited; existing PRO access expands the catalog and presets. |
| Browse a category | `/affiliate-programs/{category}` | Public category page; use an observed category slug. Visible results depend on session access. |
| Read a program | `/{slug}-affiliate-program` | Public profile. Obtain the exact canonical path from a live link or search result. |
| Latest additions | `/latest-affiliate-programs` | Public preview of recent programs. |
| Choose a tool | `/tools` | Public tool index. |
| Personalized matching | `/tools/affiliate-program-finder` | Public quiz. Result retrieval/saving requires sign-in; visible matches and reruns depend on existing access. |
| Estimate earnings | `/tools/affiliate-commission-calculator` | Public interactive model. Program picker has access-based limits. |
| Compare offers | `/tools/affiliate-program-comparison` | Public comparison of visible programs. Picker and selection count depend on access. |
| Model content ROI | `/tools/affiliate-link-roi-calculator` | Public interactive model; access-limited program picker. |
| Plan company payouts | `/tools/affiliate-program-pricing-calculator` | Public model for fixed, percentage, and recurring commissions. |
| Check launch readiness | `/tools/affiliate-program-launch-checklist` | Public checklist with a readiness score and priority fixes. |
| Read guides | `/blog`, `/blog/{slug}` | Public guides; follow observed article paths. |
| Product and affiliate FAQs | `/find-affiliates-faq`, `/faq` | Public FAQs. |
| Saved programs and activity | `/profile` and directory bookmark controls | Signed-in PRO account, with bookmarks, scouting/applied stats, and finder context. No public creator profile directory. |
| Manage owned listings | `/my-programs` | Signed-in owner dashboard; verified company email required. Use only the current user's listings and requested actions. |
| Explain access | `/pricing` | Public information. Explain a relevant existing entitlement without displaying plan promotions, initiating subscriptions, or following checkout links. |
| Company listing purchase | `/submit` | Public paid package selection leading to external checkout. Excluded from automated plugin workflows. Prepare factual program information in chat only. |
| Editorial provenance | `/editorial-policy`, `/about/matthew-dc` | Public editorial policy and author information. |
| Privacy and terms | `/privacy-policy`, `/terms-of-service` | Public policies. Reading does not authorize accepting an agreement. |
| Companion app information | `/app` | Read current informational content when specifically requested. No new subscription purchase workflow. |
| Workflow completion pages | `/submit/success`, `/pro/success`, `/app/success`, `/whop-welcome-custom` | Contextual completion or welcome pages. Do not navigate directly as proof of purchase, entitlement, or completed action. |

## Discovery and readable content

- `/llms.txt`: page and guide discovery plus a partial set of featured/recent public programs. The current generator limits program entries to 30. Absence is not proof that a program is missing from the site.
- `/llms-full.txt`: product explanation and blog content; not a full program inventory. Some product/submission claims can be older than the current UI.
- `/sitemap.xml`: discover public page URLs when an index or relevant on-site link is insufficient. Do not crawl the full site for a simple lookup.
- `/.well-known/agent-skills/index.json`: three existing website-hosted skills. They are not the installed plugin and do not grant remote MCP access.
- `/tools.md`, `/tools/{slug}.md`, `/blog.md`, `/blog/{slug}.md`, `/latest-affiliate-programs.md`, `/faq.md`, `/{slug}-affiliate-program.md`: supported text twins for relevant public pages. Use only when the host's retrieval can read them; fall back to HTML when Markdown retrieval is unavailable.
- `/auth.md`: describes user-mediated browser sign-in. It is not an unattended account connection or credential-collection workflow.

Canonical route aliases: `/affiliate-program-finder` opens the finder, `/tools/affiliate-program-finder`; `/company-profile` redirects to `/my-programs`; `/blogs` and `/blogs/{slug}` redirect to `/blog` and `/blog/{slug}`. Prefer the canonical destination.

## Boundaries

There is no callable remote MCP server in this package. The website's existing WebMCP operations only navigate to the directory, a profile, or the paid submission page. Do not infer that they return catalog results, operate calculators, save bookmarks, or submit data. Do not use the submission navigation operation from the plugin.

Directory restrictions remain in place. Do not add caller-controlled entitlement parameters, query private APIs, extract session credentials, or use public text endpoints as a substitute for protected account access. Independently public program profiles can be read for relevant research; label the search's scope honestly.

Do not recommend or facilitate program categories prohibited by OpenAI's plugin policies, such as real-money gambling, adult sexual services, or illicit/regulated goods. Offer a relevant permitted research workflow when appropriate.
