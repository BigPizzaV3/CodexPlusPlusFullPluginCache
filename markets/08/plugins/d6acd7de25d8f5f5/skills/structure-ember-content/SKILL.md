---
name: structure-ember-content
description: Structure repeated authored content in an Ember site as independently editable Markdown collection entries. Use before building any set with two or more similar records, including products, dishes, services, events, projects, team members, reviews, FAQs, pricing, schedules, values, stats, posts, or fixed rows without detail pages. Prevents domain-content arrays and keeps additions data-only.
---

# Structure Ember content collections

Use a content collection for every set of two or more independently editable,
similarly shaped records. Fixed showcases qualify; entries do not need detail
pages or expected future growth. Navigation, footer links, decorative UI
mechanics, and attributes unique to one record may remain in code or config.

## Choose the presentation

- Use list-only entries for FAQs, services, team cards, menu dishes, hours,
  reviews, values, pricing rows, and similar records without their own URL.
  Do not add detail routes unless the user needs directly linkable or long-form
  records.
- Use list plus detail pages for long-form or directly linkable entries.

Use a separate collection for each repeated set with a different record shape
or purpose. For example, put services in `content/services/*.md` and pricing
plans in `content/plans/*.md`; do not combine them merely because they share a
page. For a pricing table, each plan is one record. Keep inseparable feature
bullets as a YAML array on that plan; do not make table cells or feature rows
separate entries unless they are independently authored records.

Before building, inspect `/content`, `/lib/content.ts`, and the relevant pages
and components. Reuse the selected design's rendering pattern, but move
qualifying authored records out of code even when demo files use arrays. Make
one content-model pass across the whole requested scope before authoring:
enumerate every repeated set, assign its collection and typed frontmatter
shape, classify it as list-only or list plus detail, and decide whether it
genuinely needs a Markdown body. Do not introduce a second inline content
system later in the build.

## Define the data contract

Create one `content/<collection>/<slug>.md` file per record. Put structured
values in YAML frontmatter and primary long-form prose after the closing `---`.
Use consistent field names and types, a stable `title` or `name`, `order` when
sequence matters, and only the fields the presentation needs: category, price,
role, date, rating, attribution, image, alt text, and so on. Quote ambiguous
YAML strings.

If a list-only record needs only short plain text, use a named frontmatter
field and leave the Markdown body empty; never author body prose that no
renderer consumes.

A repeated child with its own title/label and value is a record, not an array
inside a parent. Give each child an entry and group it with metadata such as
`category`. Nested arrays are only for inseparable attributes, such as one
plan's feature bullets. Put featured/pinned status and group order in entry
metadata, never in title allowlists in a page.

For a list-only collection, load every slug and sort the loaded entries by
metadata:

```ts
listEntries("services")
  .map((slug) => loadEntry<ServiceFrontmatter>("services", slug))
  .sort((a, b) => a.order - b.order)
```

Use the actual collection name and define a separate typed frontmatter contract
for each collection. `loadEntry` returns typed frontmatter plus `bodyHtml`.
That value is already rendered HTML, not raw Markdown or plain text: pass it to
the design's `<Prose html={entry.bodyHtml} />` component. Never place it
directly in JSX text, wrap it in `<p>`, escape it, or parse it again.

For details, use `pages/<collection>/[slug].tsx`, derive `getStaticPaths()`
from `listEntries`, and handle unknown slugs. Adding an entry must not require
editing route or component code.

## Verify

Build one representative entry and its real list/card/detail renderer first,
then run `check_site` before bulk-authoring the rest. This vertical slice must
prove the frontmatter type, `bodyHtml` handling, component props, and route
contract together.

Audit every repeated authored block before `check_site`. Search pages,
components, and content-bearing config for leftover domain-content arrays,
featured-title lists, authored group definitions, or duplicated records.
Confirm every non-empty Markdown body is rendered and a representative record
can be added by creating only one Markdown file. Run `check_site`, fix every
content, route, render, and type error, then render the preview.
