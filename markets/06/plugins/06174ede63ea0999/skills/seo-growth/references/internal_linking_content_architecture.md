# Internal Linking and Content Architecture

## Goal

Internal linking should help both users and crawlers understand:
- hierarchy;
- importance;
- relationships;
- next useful action.

## Inventory

For important pages identify:
- URL;
- page type;
- parent/hub;
- inbound internal links;
- outbound related links;
- depth from navigation/home;
- orphan status;
- indexability;
- primary intent.

## Link opportunities

### Contextual
Link naturally where another page answers the next question.

### Hub → spoke
Topic/category pages link to detailed pages.

### Spoke → hub
Detailed pages link back to the useful parent or overview.

### Sibling
Related pages link to each other where the user journey supports it.

### Breadcrumb
Useful for hierarchical sites and navigation context.

### Product-led
Editorial pages link to the actual product/tool when the reader's task can be completed there.

## Anchor text

Prefer descriptive anchor text.

Avoid:
- "click here" everywhere;
- exact-match keyword repetition across hundreds of links;
- hidden links;
- giant SEO-only footer blocks.

## Orphan pages

A page in a sitemap but not meaningfully linked internally may be discoverable yet poorly integrated into the site.

Decide:
- add a real navigation/contextual link;
- consolidate;
- noindex/archive;
- delete/redirect.

## Crawlability

Important internal links should be normal crawlable links when search discovery matters.

JavaScript interactions that do not expose a crawlable destination can reduce link discovery.

## Architecture

Prefer a comprehensible structure such as:

`home → category/hub → detail`

over deeply nested arbitrary paths with no user meaning.

URL depth and click depth are different concepts. Prioritize real navigation/crawl paths.

## Content clusters

Create clusters around user problems, not keyword taxonomies alone.

Useful cluster:
- main problem/guide;
- sub-problems;
- comparison;
- implementation;
- FAQ/support where useful;
- product/tool.

Do not create thin pages just to fill every cluster node.

## Validation

After changes verify:
- links resolve;
- no redirect chains;
- canonical target is correct;
- anchor text is accurate;
- destination is indexable when intended;
- no massive template-generated link explosion.
