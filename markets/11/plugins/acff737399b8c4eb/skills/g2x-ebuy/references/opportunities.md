# Opportunities and documents

Use these tools to find notices, open one record, and read its documents in full. Start from the calibrated company profile (see the skill). Pass its NAICS codes, agencies and set-asides on every search. A value the user names for one search replaces the profile value for that query only. Say which profile values you set aside, then go back to the profile.

Filter keys are per dataset. An unknown key is refused with the list that dataset takes. Do not reuse one dataset's keys in another. Carry record IDs, G2X links and cursors from one call to the next. Keep the difference between records shown, total matches and a cut result visible in what you report.

### `g2x_search_opportunities`

Search federal opportunities by keywords, with optional NAICS, fiscal year and date filters. Use it for a quick topical shortlist.

- Inputs: `query` (required, words from the title, agency or solicitation number); `naics_codes` (up to 5 codes, 2 to 6 digits each); `status` (`open` by default, `closed` for expired or archived, `any` for both); `fiscal_year` (one year or consecutive years); `posted_after`, `posted_before`, `response_deadline_before` (YYYY-MM-DD); `limit` (1 to 8, default 5); `with_readable_documents` (true keeps only notices with a document G2X has already read; the result then shows no total).
- Output: up to 8 bounded rows with G2X record links. It does not return notice bodies, summaries or attachments. A past period includes closed notices without setting `status`. An NSN as the query finds only the notices that name it.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"query": "cybersecurity", "naics_codes": ["541512"], "status": "open"}`

### `g2x_search_records`

Search one G2X dataset and get bounded rows with totals and coverage notes. Use it for structured filtering inside one catalog.

- Inputs: `dataset` (required: `opportunities`, `contracts`, `idvs`, `vehicles`, `protests`, `forecasts`, `grants`, `subawards`, `otas`, `entities`, `notices`, `agencies`, `naics` or `psc`); `query` (free text; for contracts an exact PIID resolves directly); `filters` (filter object, at most 10 keys; opportunities take `naics`, `psc`, `notice_type`, `agency_code`, `office_code`, `solicitation_number`, `set_aside`, `active`, `posted_after`, `posted_before`, `response_deadline_after`, `response_deadline_before` and `fiscal_year`; other datasets take their own keys); `page_size` (1 to 50, default 10); `cursor` (continuation from a previous call; resupply the same dataset, query and filters).
- Output: rows with a title, key facts and a G2X link where one exists, plus the total, a cursor for the next page and notes on what the answer covers.
- Plan: all plans. The `protests` dataset is included from the Starter Team plan up; below that the tool returns the plan note and no protest data. Read only. On the research endpoint: yes.
- Example: `{"dataset": "opportunities", "filters": {"naics": "541512", "agency_code": "VA", "set_aside": "SDVOSB"}}`

### `g2x_search_supplementary`

Search SAM, state and local, DLA DIBBS and SBIR/STTR opportunities together with the text inside their attachments. Use it to find requirement language that a title search misses.

- Inputs: `query` (required, what to look for in opportunity details and inside attachments); `source_families` (`sam`, `sled`, `dibbs`, `sbir_sttr`; default all four); `record_filters` (filter object, at most 10 keys, for example `naics`, `agency_code`, `active`, `posted_range`); `page_size` (1 to 50, default 10); `cursor` (continuation; resupply the same query, families and filters).
- Output: opportunity rows with G2X links. When the match came from a document, the matching passages come with the file name and page.
- Plan: all plans, when the connection offers it. Read only. On the research endpoint: yes.
- Example: `{"query": "zero trust architecture", "source_families": ["sam", "sled"]}`

### `g2x_get_record`

Read the public summary of one G2X opportunity or company. Use the document tools for solicitation text and attachments.

- Inputs: `record_type` (required: `opportunity` or `company`); `id` (required, the G2X record id from a search result); `unlock_ai_summary` (set true only when the user asks to unlock the opportunity briefing; it uses one of the Free plan's monthly briefings).
- Output: one record with its title, summary and key fields, and a link to the record. A notice also names its G2X page, its SAM.gov page and its attachments with SAM.gov file links, where they exist.
- Plan: all plans. Read only, except that an explicit briefing unlock spends one monthly Free plan briefing. On the research endpoint: yes.
- Example: `{"record_type": "opportunity", "id": "<id from a search result>"}`

### `g2x_opportunity_documents`

List the documents on file for an opportunity. This reads what is stored and starts nothing.

- Inputs: `opportunity_id` (required, the G2X opportunity record identifier); `offset` (continue the list from this row, default 0); `format` (`markdown` by default, or `json` for pages, tables and page numbers; chooses which parsed version each link opens).
- Output: document rows with each document's category, readiness and version, and links to its SAM.gov file, its G2X file and its parsed Markdown or JSON, where they exist. Show those links with the document.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"opportunity_id": "<id from a search result>"}`

### `g2x_opportunity_attachment_text`

Return the complete text of one opportunity document already on file. It serves stored content only and never starts a new parse.

- Inputs: `opportunity_id` (required); `attachment_id` (required, an attachment id from the document list); `format` (`markdown` by default, the stored parse byte for byte, or `json`, every page with its text and elements); `cursor` (continue from a previous result's next cursor; omit to start at the first byte); `page` (read only this 1-based page or section; omit to read the whole document).
- Output: the whole document in exact chunks, each naming the document's byte count and SHA-256, with a cursor to the next chunk until the last byte. Asking for one page returns that page or section instead. A page read does not satisfy a request for the entire document. Follow the cursor for the same document and version; never join different versions without saying so.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"opportunity_id": "<opportunity id>", "attachment_id": "<attachment id>", "format": "markdown"}`

For amendment comparisons, establish both versions first. Compare deadline, submission instructions, scope, quantities, evaluation criteria and changed requirements. Give old then new with file, page and section citations. Do not say "no changes" from partial text, and identify any document or page you could not read.
