# Canonical report contract

`report.schema.json` is the machine contract. `validate_report.py` also checks source/entity references and semantic invariants. Each report is a dated, versioned snapshot. Keep optional account exports as normalized attachments with their provenance and merge intentionally.

Files: `report.json`, `report.md`, `brief.pdf`, `sources`, `evidence/` (sanitized publication-safe images), `collection/` (private raw files), `exports/` (private account files), and a short data request. Do not publish raw crawl text wholesale or copyrighted full articles. Preserve original screenshots; crop only for presentation with the full capture available and do not manipulate factual content.

Suggested five pages:
1. Recommendation, core observed metrics, 3–5 peer selection and unknowns that matter.
2. Website conversion and measurement, with a screenshot and performance context.
3. SEO performance table or explicit data gap, page inventory comparison and service/content opportunities.
4. Google/Meta/LinkedIn evidence, creative examples and a focused test recommendation.
5. Inquiry/email verification, prioritized workplan and a labeled opportunity illustration.

The webpage expands the same data with tabs, entity and page filters, ad-platform comparisons, expandable source evidence, screenshots and editable model assumptions. Do not bury uncertainty in a footnote or create charts from missing data. Avoid irrelevant login, chatbot or upload features.

Agent access: offer an index, complete JSON, readable Markdown, schema and a read-only query endpoint filtered by report, section, entity and optional text. Return matching source records and limitations with query results. Errors must distinguish unknown report/parameter from a valid empty result. Site access policy applies to machine routes. Private publication is not a publicly callable API.

`brief.pages` contains at most five objects with kicker, title, optional deck and blocks. Blocks are text (`text`, optional heading), table (`headers`, rows, optional widths), image (`path`, caption, optional height), or finding (`finding_id`). Each page has `source_ids`. The PDF renderer resolves finding blocks from the canonical findings, measures body height, fails on overflow, links sources and embeds supplied brand assets. Review all rendered pages after building.

## Reader

The client brief and main website are written for the business owner. Address the owner directly and connect each finding to a customer action, booked work or a spending decision. Put exporter instructions, workflow design, tool comparisons and agent endpoint documentation in supporting materials. Preserve machine-readable routes without making them the owner’s primary navigation.

Verify the owner’s name on a primary source and use a short opening paragraph addressed to that person. Frame focus areas as opportunities available to the business. Avoid author-centered language such as “I’d” or “we’ll,” provider staffing and engagement language. The report is not an agency proposal.

For account estimates, preserve report date, capture timezone, country, domain scope, model and any visible provider disruption notice. Collect all result pages and preserve unknown CPC or other cells as null. Separate Overview and Top Pages totals when those views differ. Keep generated design concepts outside the factual client report; use sourced company photography in the finished artifact.
