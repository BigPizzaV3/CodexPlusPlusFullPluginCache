# Semantic HTML and structured data

Machine-readable code structure so AI systems interpret blocks, tables, and
entities correctly.

## The core problem

Machines do not see visual design, they read code structure. Content that looks
like a table but is built from `div` containers is useless for extraction.

## Requirements

1. **Semantic HTML tags.** Use `article`, `main`, `header`, and `footer` instead
   of meaningless `div` and `span` containers. The tags mark what is main content
   and what is chrome.

2. **Real tables and lists.** Mark up comparison tables with `table`, `thead`,
   `tbody`, `tr`, and `td`. Only then can AI systems extract the data by row and
   column. Tables are among the most frequently lifted elements (see
   `query-fan-out.md`).

3. **Schema.org via JSON-LD.** Structured data is mandatory: `Person` for
   authors, `Article` for posts, `Product` and `Offer` for offerings, `FAQPage`
   for question blocks. JSON-LD is separate from the visual HTML and easiest for
   machines to process. This markup feeds the Google Knowledge Graph, among
   others, which AI Overviews draw on. Paste-ready snippets in
   `../assets/json-ld-snippets.md`.

4. **Cluster architecture.** Organize content as a pillar page with supporting
   detail articles. Internal links carry descriptive anchor text ("analysis of
   click depth" instead of "read more"), so the target context is handed over
   machine-readably.

## Connection to editorial

Code structure is the technical counterpart to the chunking rules: heading
hierarchy, real lists, and tables define the boundaries at which retrieval
systems cut blocks. Verified source: schema.org.
