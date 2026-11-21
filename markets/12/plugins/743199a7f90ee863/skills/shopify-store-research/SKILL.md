---
name: shopify-store-research
description: Research Shopify stores with Undercart's tools - build prospect lists by revenue, category, country and installed apps, profile a store's revenue and tech stack, find similar stores, and review a store's live ads and marketing emails.
---

# Shopify store research with Undercart

Use the Undercart tools when the user asks about Shopify stores as businesses: who they
are, how big they are, what apps they run, how they advertise, or how they email their
customers. Every Undercart tool is read-only.

## Pick the tool

| The user wants | Tool |
| --- | --- |
| A list of stores matching criteria (size, category, country, apps, traffic) | `search_stores` |
| Everything about one store | `get_store` |
| Only a store's apps and technologies | `list_store_technologies` |
| Competitors or lookalikes of a store | `find_similar_stores` |
| The ads a store runs on Meta, Google or TikTok | `get_store_ads` (pass `platform` to see the creatives) |
| A store's newsletter emails and discount codes | `get_store_emails`, then `get_store_email` for one email |
| The category names `search_stores` accepts | `list_store_categories` |

## Workflows

**Prospect list.** Turn the request into one `search_stores` call with every filter the
user gave: `category`, `country`, `revenueMin` / `revenueMax` (annual USD), `tech` for
apps the store runs, `techAdded` / `techRemoved` with `techDays` for recent changes,
`rankMax` for traffic. One well-filtered search answers better than several narrow ones.
Present the stores as a table: name, domain, estimated annual revenue, country and the
apps that matter to the user. Link each one with its `undercartUrl`.

**Store profile.** Call `get_store` with the domain as the user wrote it. The tool
normalizes URLs and `www.` prefixes. Lead with what the user asked about. Give revenue as
annual first, then monthly.

**Competitive set.** Call `find_similar_stores` for the reference domain. It matches on
category and a 0.5x to 2x revenue window. Compare the results on the dimensions the user
cares about.

**Ad research.** Call `get_store_ads` without `platform` for the cross-platform
summary, or with `platform` (`meta`, `google` or `tiktok`) for the actual creatives.

**Email research.** Call `get_store_emails` for subjects, dates, discount codes and send
cadence. Call `get_store_email` with an email id to read one email in full.

## Reading the results

- Revenue, orders, traffic rank and ad spend are modeled estimates, not reported
  financials. Say so when the user relies on a figure.
- `enriched: false` marks a store Undercart holds only public-web data for: apps,
  description, country, traffic rank, and a preliminary `revenueBand` instead of a
  revenue estimate. It has no ads, emails or social data yet.
- An error that a domain is unknown means the store isn't in Undercart's catalog. Tell
  the user rather than guessing.
- A monthly-limit message means the user's plan allowance is used up. Relay it as
  written, including when it resets.

## Out of scope

Undercart can't buy products, place orders, send or unsubscribe from emails, or change
anything on a store. It holds data about stores as businesses, not about private
individuals. Don't use it to look up personal contact details of people.
