---
name: content-access
description: Fetch any trip1 content page (travel guides, help articles, hotel pages) as clean markdown by sending Accept, text/markdown. Also includes llms.txt and llms-full.txt indexes.
---

# Reading trip1 content as markdown

Every content page on trip1 is available as clean markdown when requested with the right Accept header. This avoids parsing HTML and strips component chrome.

## Per-page markdown

Send `Accept: text/markdown` to any content URL:

```
curl -H "Accept: text/markdown" https://trip1.com/travel-guides/spain/barcelona
```

The response is lean — headings, prose, and links only.

## Discovery indexes

- `https://trip1.com/llms.txt` — short overview, good for a first pass.
- `https://trip1.com/llms-full.txt` — longer index with destinations, travel guides (capped at 200 most recent), and help center categories.
- `https://trip1.com/sitemap.xml` — complete URL set.

## What's indexed

- Travel guides: `https://trip1.com/travel-guides/...`
- Destination pages: `https://trip1.com/travel-guides/<country>` and `https://trip1.com/travel-guides/<country>/<city>`
- Hotel pages: `https://trip1.com/hotels/...`
- Help center: `https://trip1.com/help/<collection>` and `https://trip1.com/help/<collection>/<slug>`

## When to use HTML instead of markdown

If you need structured data (hotel pricing, availability, booking links), use the MCP tools described in the hotel-booking skill. Markdown pages are for reading — they don't include live pricing.
