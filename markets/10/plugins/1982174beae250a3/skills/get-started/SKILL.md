---
name: get-started
description: Read electronic-component datasheets with document and page references. Use for ratings, pinouts, tables, graphs, package drawings, register maps, BOM datasheet checks and comparison points; check live stock and prices only when requested.
---

# PartsPlan

PartsPlan connects ChatGPT to archived manufacturer datasheets for electronic components and shows where each section, table and figure sits in a document. Datasheet answers cite the document and page so the user can check the source. Engineering decisions remain with the user.

## When to use
Questions that name an electronic component part number and ask for something printed in its datasheet — a rating, an electrical characteristic with its conditions, a pinout, a table row, a graph reading or a package dimension — and BOM datasheet checks. Look these up in the manufacturer document through PartsPlan so each value carries its document and page.

## Connect
Sign in with a PartsPlan account when ChatGPT asks (Google or email). Daily and monthly call limits depend on the account; when a limit is reached the tool says so and when it resets.

## Setting up
When the user asks to set up PartsPlan or get started, make one read-only lookup to confirm the connection: `find_datasheet` for a part the user mentioned, otherwise a common part such as TPS563200 (Texas Instruments). Show what it returned — the manufacturer document and, when the response gives one, a page to read first; do not state a page the response did not give. Then suggest a few things to ask: a value with its page, a pinout, a BOM check, or comparing candidates. Tell the user that starting a message with @PartsPlan uses PartsPlan for that question. Do not call `check_stock`, `request_datasheet_collection` or `report_problem` while setting up.

## The basic path (one part, one question)
1. `find_datasheet(mpn, brand)` — the document of the requested manufacturer comes first (`requested_maker_document`); other manufacturers' documents for the same part number are listed separately and describe other parts.
2. `get_datasheet_map(doc_sha256, kind=...)` — jump to the section: `abs_max`, `elec_char`, `rec_op`, `thermal`, `pinmap`, `package`, `land_pattern`, `figure`, `app_circuit`, `ordering` …
3. Read the page:
   - text: `get_page_blocks(doc_sha256, page)`
   - tables: the page image is the reference — table blocks come with a `table_image_requests` entry for `get_page_image`
   - graphs: `get_figure_data` (numbers only when they can be read with certainty) or `get_page_image` for the figure region
4. Cite the document and page for every datasheet value, with its units and stated conditions. If the source is missing or unclear, say so; do not fill gaps with estimates.

`search_datasheet(doc_sha256, q=[...], mode="context")` finds terms, conditions and footnotes inside one document when the map is not enough.

## Other datasheet tasks
- BOM: `check_bom` reports per line whether that manufacturer's datasheet is in the archive and readable; it does not validate a BOM or circuit. `request_datasheet_collection` queues missing lines when the user wants them collected.
- Comparing candidates: `compare_points(source, candidates, device)` returns an adjustable default rubric — hard lines, weighted items summing to 100 and checks — with the datasheet pages to read for each item and part. The candidates are the ones the conversation chose. It gives no scores, rankings or compatibility verdicts.
- Candidate parts: `search_parts` by description, device type or manufacturer.
- Reference circuits: `reference_circuits(mpn, brand)` (the manufacturer is required) gives application-circuit pages in the manufacturer's datasheet; `related_documents` lists the manufacturer's reference designs and user guides that print that exact part number — a printed part number does not establish that a design uses or suits the part.
- A wrong answer: `report_problem` with the document, page and block, when the user asks.

## Stock and prices
Use `check_stock` only for an explicit stock or price request. An exact part number is required; ask for it when missing. A request accepts up to three exact part numbers and uses five plan units per part number. Do not add stock checks to datasheet or BOM tasks without a request.

Show each distributor's reported price breaks, stock, lead time and lifecycle labels when supplied, with the retrieval time and currency. Keep the distributor attribution and data notices. Include only returned product links; element14 results have no product link. Report unavailable or failed lookups as such, not as zero stock. Do not convert currencies, compare prices across currencies, estimate missing values, rank sellers or recommend a purchase. Longer orderable codes listed in `candidates` were not checked; check one by calling again with it.

PartsPlan does not store stock-query results. Distributor results have retrieval times rather than datasheet page citations. PartsPlan does not place orders or process payments.

## What the answers mean
- A datasheet value always comes with the document and page it was read from; missing values are not estimated.
- Absence (`no_document`) covers the PartsPlan archive only. A web search or the manufacturer's site can still answer — say which parts of an answer came from outside PartsPlan.
- `text_source=ocr` text is a reading of an image; confirm numbers on the page image.
- PartsPlan does not validate circuits. If an account limit prevents a request, explain the limit returned by the tool.
