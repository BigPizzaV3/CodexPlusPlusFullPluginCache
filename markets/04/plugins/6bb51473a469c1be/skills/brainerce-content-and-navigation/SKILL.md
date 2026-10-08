---
name: brainerce-content-and-navigation
description: "The words on a Brainerce storefront that are not product copy: static pages, FAQs, footers, the header and its navigation links, announcement bars, the blog, and the SEO around them. Use when the merchant asks where do I write my About page, how do I add a shipping policy, can I put a banner across the top, how do I change my menu, where does my blog live, or how do I get found on Google. Says which pieces exist, where each is configured, and which a storefront must be built to read before anything shows up. Nothing here is reachable from this connector, so it gives exact dashboard routes instead of pretending. For store owners and for developers wiring content in. Do not choose this for products, categories or tags, use brainerce-store-architecture. Do not choose this for product specs, use brainerce-custom-fields. Keywords: pages, about page, policy page, terms, FAQ, footer, header, navigation, menu, announcement bar, banner, blog, articles, SEO, meta description, Google, sitemap."
compatibility: ChatGPT, Claude Code, Claude Desktop, Cursor
maintainer: Brainerce
metadata:
  author: Brainerce
  version: "1.0.0"
---

Get the non-product words onto a storefront, and be exact about what the platform does and does not do for you.

## Core principle

Everything in this skill is **data, not a rendered page**. Brainerce stores the words and exposes them through the SDK; the storefront decides where they appear. A merchant who writes an FAQ and sees nothing on their site does not have a broken FAQ, they have a storefront that is not asking for it yet.

That distinction is the answer to most questions here, so lead with it rather than burying it.

⛔ **None of this is reachable from this connector.** There is no content tool, no page tool, no blog tool and no navigation tool on the Brainerce ChatGPT surface. Give the dashboard route, and never report a content change as done.

## When to use this skill first

- "Where do I write my About page / shipping policy / terms".
- "Can I put a banner across the top of my site".
- "How do I change my menu", "how do I add a link to the header".
- "Where does my blog live", "how do I publish an article".
- "How do I get found on Google", "where is my meta description".
- A developer wiring pages, footers or announcements into a storefront.

## When NOT to use this skill first

- Products, categories, tags, variants: `brainerce-store-architecture`.
- Product specs and structured data on products: `brainerce-custom-fields`.
- Per-product SEO slug and meta description while adding a product: `brainerce-product-onboarding`.
- The SDK calls that fetch any of this: `brainerce-sdk`.
- Building the storefront that renders it: `brainerce-storefront-build`.

---

## The two places words live

### Content

The dashboard's **Content** section holds reusable pieces. Edit once, and every storefront reading that entry updates. Six kinds:

| Type | What it is for |
|---|---|
| **FAQ** | A list of question and answer pairs |
| **Footer** | Footer columns, links, copyright, social links |
| **Header** | Logo, navigation links, and a call to action |
| **Announcement** | The bar across the top: sales, shipping cut-offs, holiday notices |
| **Rich text** | A block of formatted copy a storefront can drop anywhere |
| **Page** | A full static page: About, Shipping Policy, Terms |

Create with **New content**, pick the type, write it. Every entry is **Draft** or **Published**, and only published entries reach a storefront.

### Blog

**Blog** publishes articles. **New post**, write, publish. Brainerce stores the article and exposes it; the layout belongs to the storefront.

### Which one

- Part of the furniture of the site, so footer, header, announcement bar, FAQ block: **Content**.
- An article with a date: **Blog**.
- A description of something you sell: neither, that is a product.

## Navigation, precisely

**There is no visual navigation builder in Brainerce.** Merchants ask for one, so say what there is instead of implying a page they will go looking for.

A storefront menu comes from two sources, and they do different jobs:

1. **The category tree.** Parent and child categories are the browsable structure: "Mobile" with "iPhone" and "Samsung" under it. Each category has its own landing page and a breadcrumb on every product in it. A storefront fetches the tree and renders it. This is where the shape of the menu is decided, and it is a catalog decision, so `brainerce-store-architecture` owns it.

2. **A Header content entry.** The `HEADER` type carries an optional logo, a list of navigation items as label plus URL pairs, and an optional call to action. This is where links that are not categories go: About, Contact, the blog, a landing page.

So "add Contact to my menu" is a Header entry edit, and "add Laptops to my menu" is a category. Ask which kind of link it is before answering.

## Static pages

A **Page** entry carries a slug in lower-kebab form, a title, the body, and its own SEO block: title, description and social image. That is what an About page, a Shipping Policy or a Terms page is.

The storefront still has to route it. A Page entry is not automatically live at `/about`; the storefront reads the entry and decides. If a merchant has published a page and cannot reach it, that is a storefront routing gap, not a content problem.

⛔ **Merchant-authored HTML is not sanitized by the server**, deliberately, because some merchants embed things a strict sanitizer would strip. Rich text bodies, page bodies and FAQ answers all arrive raw. A storefront rendering them must sanitize before injecting, and this is worth saying to a developer unprompted.

## Announcements

The `ANNOUNCEMENT` type carries the message, a severity of info, warning or success, whether it can be dismissed, an optional start and end time, and an optional call to action.

Two things to tell a merchant:

- The **start and end times are filtered by the storefront**, not enforced by the server. A storefront that ignores them shows the banner forever.
- **Unpublish rather than delete** when a sale ends. See the next section for why.

## ⛔ Deleting is permanent, and storefronts fall back to nothing

Delete a content entry and it is gone. A storefront that expected it renders whatever it was built to show when there is nothing, which is usually nothing at all. Deleting a blog post is permanent too.

The reversible move is **Unpublish**. Recommend it every time a merchant says "take this down", and only mention delete if they say they want it gone for good.

## Blog SEO, and what happens automatically

Every post carries:

| Field | What it controls |
|---|---|
| **Slug** | The address, `/blog/summer-care-guide`. Auto-derived from the title, editable |
| **SEO title** | The headline in search results; falls back to the post title |
| **SEO description** | The snippet under it; 150 to 160 characters works |
| **OG image** | The image shown when shared; falls back to the cover image |

Static Pages carry the same three SEO fields.

**Renaming a slug is safe.** The old address redirects with a 301 to the new one, so the ranking it earned is not lost. Merchants hesitate over this; tell them it is fine.

Published posts go into the sitemap on their own, and Brainerce pings search engines the moment a post goes live, so nothing needs submitting by hand.

## Getting found on Google

### What a Brainerce storefront does by itself

A storefront built from the current template, or built by following the integration guide, ships with a sitemap covering products, categories, posts and pages; schema.org structured data on products so prices and star ratings can appear in results; instant indexing so a new post is crawled in minutes; and automatic 301 redirects when a slug is renamed.

One caveat that applies to all four: **they live in the storefront, not the platform.** A site built before those features existed, or built by hand without the guide, may be missing some. If in doubt, that is a question for whoever built the storefront.

### What Brainerce does not do

Say these plainly, because merchants assume otherwise:

- Brainerce does **not** run ads. Everything here is organic search.
- Brainerce does **not** guarantee a ranking, and nobody can.
- Brainerce does **not** submit the site to Google. Verifying the domain is the owner's job.

### The three things only the merchant can do

1. **Write the homepage meta description.** In **Settings**, the **Homepage SEO** card. Fifty to 160 characters saying what the shop sells and for whom. Without it Google picks text off the page at random. There is a Create with AI button.
2. **Verify the domain in Google Search Console.** Add the domain in Search Console, choose the HTML tag method, copy the tag. In Brainerce go to **Apps, then Google and YouTube**, pick the sales channel, open the **Merchant Center** tab, and paste it into **Google site verification**. ⛔ It is NOT in the sales-channel settings, which is where everyone looks first. The storefront renders the tag within a few minutes, then click Verify.
3. **Give every product a slug and a meta description.** Both live on the product. The **SEO column** on the Products page scores each one and offers one-click fixes, including AI-written descriptions and image alt text.

### SEO Autopilot

⛔ **Not switched on yet.** A store-wide SEO audit with a ranked issue list is documented ahead of release, and merchants sometimes ask for it by name. If it is not in the sidebar, nothing is broken. What exists today is the per-product SEO score in the products table, which is a different and smaller thing.

## Response shape

> Your About page goes in **Content**, as a Page entry. New content, pick Page, give it the slug `about`, write the body, and fill in the SEO title and description while you are there.
>
> Two things to know. It saves as a Draft, so publish it or nothing sees it. And a Page entry is data: your storefront has to be built to fetch and route it, so if `/about` still 404s after publishing, that is a change on the storefront side rather than something to fix here.
>
> To get it into the menu, add it as a link in your **Header** content entry.
>
> I cannot do any of that from this conversation, so those are steps for you in the dashboard.

## Rules

- Never report a content, page, blog or navigation change as done. There is no tool for any of it here.
- Lead with "this is data, your storefront renders it" whenever a merchant reports that something does not appear.
- Recommend Unpublish, not Delete. Deletion is permanent and storefronts fall back to nothing.
- Do not invent a navigation builder. It is the category tree plus a Header entry.
- Give the exact dashboard route, including the tab. The Search Console tag in particular is somewhere nobody guesses.
- Write the negative space. If a merchant asks for something Brainerce does not do, ads or ranking guarantees or SEO Autopilot today, say so rather than answering with generic advice that reads like a yes.
- Tell developers that page, rich text and FAQ HTML is unsanitized, before they render it.

## Reference files in this skill

- `references/content-shapes.md`: the payload shape of each of the six content types, the sanitisation rule, and how a menu is assembled from the category tree plus the header entry. For developers.

## Cross-skill connections

- The category tree that is half the menu: `brainerce-store-architecture`.
- Structured data attached to products: `brainerce-custom-fields`.
- Per-product SEO while adding a product: `brainerce-product-onboarding`.
- The SDK calls that fetch content and posts: `brainerce-sdk`.
- Routing and rendering it in a storefront, including sanitisation: `brainerce-storefront-build`.

Route once, and do not bounce back and forth.
