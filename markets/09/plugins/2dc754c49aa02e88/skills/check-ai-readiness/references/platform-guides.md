# Platform guides

Where to find each fix on common website platforms. Menus get renamed, so describe where to look and invite the user to say what they see if it doesn't match. If you can browse the web, check the platform's current help pages before giving exact menu paths.

Fix names match `summary.topFixes[].title` and `checkId` values in the scan result.

## Any platform: security settings (when `scanBlocked` is set, or the user suspects their security blocks AI assistants)

- **Cloudflare** (many sites use it even if built elsewhere): in the Cloudflare dashboard for the domain, look under **Security → Bots**. Settings named like "Block AI bots" / "AI Scrapers and Crawlers", "Bot Fight Mode", or WAF custom rules that match user agents can turn AI assistants away. Allowing verified bots is usually enough.
- **Other hosts or firewalls** (Sucuri, Wordfence, Akamai, a hosting provider's "bot protection"): look for bot blocking or "AI crawler" settings, or ask the host's support to allow verified AI assistants such as OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User and PerplexityBot.

## Shopify

- **robots.txt** (robots-ai-search): Shopify generates it. To change it, edit the theme: **Online Store → Themes → … → Edit code**, then add or edit the `robots.txt.liquid` template. This is the one place where Shopify needs a bit of code, so offer a ready-to-paste snippet.
- **Title and page description** (title, meta-description): homepage under **Online Store → Preferences**. Products, pages and collections each have a **Search engine listing** section at the bottom of their edit screen.
- **Sharing image** (open-graph): **Online Store → Preferences → Social sharing image**.
- **Sitemap**: created automatically at `/sitemap.xml`. Nothing to do.
- **Business details for AI** (json-ld): many themes include some automatically. Otherwise an SEO or "structured data / schema" app from the Shopify App Store can add it.

## Wix

- **robots.txt**: Wix has a robots.txt editor in its SEO settings (search the dashboard for "Robots.txt Editor").
- **Title and description**: each page's **SEO basics** in the page settings, or the site-wide SEO settings.
- **Business details for AI** (json-ld): page SEO settings have an **Advanced SEO → Structured data markup** area. Wix also adds some business markup automatically if the business info is filled in.
- **Sitemap**: automatic.

## Squarespace

- **AI assistants blocked** (robots-ai-search): Squarespace has a site setting to block known AI crawlers (look under **Settings** for "Crawlers"). If it's on, it may block assistants they want, so explain what it does and let them decide.
- robots.txt itself can't be edited directly on Squarespace.
- **Title and description**: site-wide in the SEO settings (search the dashboard for "SEO"). Each page also has its own SEO tab in **Page settings**.
- **Sitemap**: automatic.

## WordPress

- **Page hidden from search** (meta-robots / x-robots-tag fail): check **Settings → Reading → "Discourage search engines from indexing this site"**. If it's ticked, untick it. This is the most common cause.
- **Title, description, business details, robots.txt**: usually handled by an SEO plugin such as Yoast SEO, Rank Math or All in One SEO. Each has fields for title and description on every page, a schema / structured data section, and a file editor for robots.txt.
- **Sitemap**: WordPress makes one at `/wp-sitemap.xml`, and SEO plugins make their own.
- **Security plugins** (Wordfence and others) can block bots. See "Any platform" above.

## Webflow

- **robots.txt and sitemap**: **Site settings → SEO** has a robots.txt box and an option to auto-generate the sitemap.
- **Title, description, sharing image**: each page's **Page settings** (SEO and Open Graph sections).
- **Business details for AI** (json-ld): paste a JSON-LD script in **Page settings → Custom code** (inside the `<head>` area). Offer the starter snippet from the `json-ld` check's `fix`.

## Framer, GoDaddy, Weebly, HubSpot, BigCommerce, Ghost and others

Most site builders have an **SEO** section in site settings and a per-page SEO panel for title and description. Sitemaps are usually automatic. For robots.txt or structured data, check the platform's help center for "robots.txt" or "structured data / schema". Some don't allow editing robots.txt at all.

## Custom-built sites (Next.js, Nuxt, Gatsby, or a developer built it)

The owner most likely needs their developer. Write a short, friendly message they can forward, built from the technical `message` and `fix` of the relevant checks. Keep it under ten lines.
