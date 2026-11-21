---
name: competiscan-research
description: Competitive marketing research over Competiscan's archive of 20+ years of real US and Canadian marketing (direct mail above all, plus email, digital, social, search and print), using the Competiscan tools search_campaigns, read_piece, show_pieces and discover_filters. Use it whenever the user asks what a company or competitor is mailing or advertising; wants examples of offers or creative (balance transfer, 0% APR, sign-up bonuses, checking bonuses, pre-approved mail, rates, rewards); wants to compare companies' marketing; tracks how offers or messaging changed over time; asks how many campaigns or pieces something had; or names a piece by entry ID (like 2026-09-09-5185), even if they never say "Competiscan". Covers credit cards, banking, insurance, mortgage, investments, telecom, energy, retail, automotive, travel and other sectors.
---

# Competiscan research

Competiscan's archive holds real marketing pieces collected from a panel of US and Canadian consumers and businesses for more than 20 years: direct mail above all, plus email, online display and video, social, search ads, print and website captures, across 17 sectors. Each piece is scanned, its text read by OCR, and coded with structured fields: company, product, offer terms, mailing type, audience, targeting.

That makes it the record of what companies actually sent, to whom, when, and what it said. It does not hold response rates, spend, or total market mail volume. A count is the number of pieces the panel captured: a strong *relative* signal (company A vs. B, this year vs. last), not an absolute volume. Say so whenever you report a count.

## Tools

| Tool | Use it to | Limits |
|---|---|---|
| `search_campaigns` | Find pieces. Returns metadata rows: company, product, headline, channel, audience, mailing type, dates, `pdf_url`. Never the full text. | Needs at least one narrowing filter. No paging. |
| `read_piece` | Get the full printed text of specific pieces, for exact terms and fine print. | 25 ids per call. |
| `show_pieces` | Display pieces to the user as visual cards (thumbnail, headline, PDF button). The only tool whose output the user sees. | 8 ids per call. |
| `discover_filters` | Look up what filters accept: company spellings, the taxonomy under a sector, the advanced filter groups and their values. | — |

The usual flow is search → read a few → show the best examples → answer.

## 1. Frame the search

Turn the question into who / what / where / when before calling anything.

- **When.** For "lately", "now", "current", default to the last 90 days. Bound every search with dates. It keeps queries fast, and rows come back newest-first, so a long window with a small limit shows only the last few days of it.
- **Recent mail lags.** Direct mail reaches the archive roughly 2–4 weeks after it lands in mailboxes, so the most recent weeks are always thin. "This week" or "this month" for mail will undercount; widen the window and tell the user why.
- **Channel.** "Mail", "mailer", "mailing" → `media_channel=["Direct Mail"]`. "Marketing" or "advertising" in general → leave the channel open and break results down by channel.
- **Audience.** "Small business" → `Employer/Business Owner`; advisors or agents → `Insurance Producer/Financial Advisor`; brokers → `Mortgage Broker`; doctors or clinics → `Provider`. Otherwise `Consumer`, or leave it open.
- **Country.** The archive mixes US and Canada. Set `country="US"` (or `"CA"`) when the question is about one market; otherwise label the Canadian pieces.
- **Prospect offers vs. customer mail.** `mailing_type` separates Acquisition (offers to new customers) from Upgrade/Cross-Sell, Loyalty/Retention, Win-Back, Follow-Up and Statement. A question about "offers" or "acquisition" almost always wants `advanced_filters={"mailing_type": ["Acquisition"]}`. Without it, statements and servicing letters crowd the results, especially in older years.
- **Dates.** `search_date` (the default) is when the piece was received, which is the campaign date. Filter on it and describe timing with it; `approved_date` can trail it by months.

## 2. Prefer structured filters to keywords

Many questions that sound like keyword searches are already coded fields. Structured filters are fast, can be counted, and don't miss pieces where OCR garbled a word. Pass them in `advanced_filters` (a flat dict) and call `discover_filters(group=...)` for exact values before guessing one.

| The user asks about | Filter |
|---|---|
| Balance transfer or 0% purchase intro APR | `intro_pricing`: "BT Intro", "Purch Intro" |
| Sign-up bonus type | `incentive_type`: "Points - Fixed", "Miles - Fixed", "Cash Back - Fixed", "Gift Card", … |
| Rewards cards | `rewards_emphasis`: "Miles", "Points", "Cash-Back"; `rewards_program`: true |
| Pre-approved / pre-selected / invitation to apply | `application_type` |
| Card network or tier | `card_network`, `card_level` |
| Prospects vs. existing customers | `mailing_type` |
| Co-brand and affinity cards | `affinity_category` (Airline, Hotel/Resort, Union, Alumni/University, …), `affinity_name` |
| Who was targeted | `state` (the state the campaign targets), `age`, `income`, `target_market` (Hispanic, Military, Gen Z, …) |
| Mail format | `package_type` (Envelope, Postcard, Self-Mailer, Snap Pack), `delivery_type` (First Class, …) |
| Mortgage terms | `refinance`, `fha`, `va`, `jumbo_non_conforming`, `loan_amount_min` / `loan_amount_max` |
| Messaging intent | `communication_type` (Rates, Onboarding, Product Changes, Co-Brand, … 69 tags) |
| A segment within a sector | `category` / `subcategory` (typed parameters). Walk them with `discover_filters(parent="Banking")` |

Use `ocr_text` for words that aren't a field: a specific phrase, a competitor named in the copy, a feature, a rate. A keyword search is a scan rather than an index lookup, so its shape matters:

- Both `date_from` and `date_to` are required. Start with 90 days or less.
- Write terms without punctuation, because the OCR text has none: "pre approved", "0 apr", not "pre-approved", "0% APR". Up to 5 terms, 3+ characters each.
- Leave `sort` unset and `include_total` false, and set `limit` to what you will actually read (10–30).
- `truncated: true` means only the newest matches in the window were read. Describe them as "the most recent N matches", not as what the whole period contains.

## 3. Get company names right

Company names are legal entities, not brands, and they aren't normalised.

- For a distinctive brand, use `company_match="contains"`. "Capital One" covers six entities, including Capital One 360 and Capital One Auto Finance. Then read `resolved.company_names` to see what was actually searched.
- For a short or common string, look it up first. "Chase" with `contains` matches about 60 companies (Chase Chevrolet, Fox Chase Bank, Riverchase Kia, …) and runs slowly. Call `discover_filters(field="company", query="chase")` and pass the exact names you want, e.g. `["Chase", "JPMorgan Chase & Co"]` with the default exact match.
- A piece matches every company mapped to it, so issuers appear on their partners' mail. A Capital One search returns Pottery Barn and Union Plus cards; Chase returns Amazon Prime Visa, United and Marriott cards. Decide whether the user means the issuer's whole book or its own-brand products, and label co-brands as such.
- Acquired brands keep their own name: Discover pieces now say "a division of Capital One". Mention it when it changes the picture.

## 4. Read selectively

Each search row carries a `product_headline`, a curated summary that is often enough for an overview. Use `read_piece` when the answer depends on exact terms: APR and intro period, bonus amount and spend requirement, fees, expiry, eligibility, fine print. Read a representative handful (5–15 distinct creatives), not every row.

OCR text has no punctuation, so numbers come apart: "0.36% APR" reads back as "0 36 APR", and "$1,500" can read "1 500". Interpret figures in context. If a number is ambiguous, say so and point to the PDF rather than guessing.

## 5. Deduplicate before counting or picking examples

The same creative arrives from many panelists, each with its own entry_id. One week can hold several copies of the same Capital One Venture mailer. Group rows by company + product name + headline, report "N pieces, M distinct creatives", and pick examples from distinct creatives.

## 6. Counts and trends

- For "how many", set `include_total=true`; without `ocr_text` this is fast. If `total_is_capped` comes back true, the figure is not reportable. Narrow the window, or add `exact_count=true` (slower).
- For change over time, run the same query once per period with identical filters and compare the periods. One search across many years returns only the newest rows of that window, so it cannot show a trend.
- Keep each period small enough to count and to sample fairly. Rows come back newest-first, so "limit 15" over a whole year is really a late-December sample, and a sector-wide count over a year often comes back capped. Comparing the same month across years (every September since 2020, say) solves both and removes seasonality.
- To compare offer terms over time, take a small sample per period (limit 10–20, Acquisition only) and read a few pieces from each.
- There is no paging. If you need more rows, narrow the window or the category. Don't re-run the same call.

## 7. When something goes wrong

- **No results.** Check the `resolved` block before concluding the archive has nothing. Common causes are a wrong company name, a window too recent for mail to have arrived, punctuation in `ocr_text`, or filters that AND together to nothing.
- **400.** The error lists the valid values. Pick from them, or use `discover_filters`.
- **504 / timeout.** The query ran past the 3-minute limit; it does not mean "nothing found". Narrow it (shorter window, add a sector or channel, use exact company names instead of `contains`) and retry. Don't resend the identical request.

## 8. Present the answer

- Lead with the findings in 3–6 bullets, then the supporting detail.
- State the scope in one line: window, channel, country, key filters, and whether the results were truncated or sampled.
- For comparisons, use a table such as Company | Product | Offer (bonus / APR / fee) | Mailing type | Date | Entry ID.
- Show 2–6 representative pieces with `show_pieces`: the ones your answer cites, each placed next to the text it supports. Skip near-duplicates. When the user asks to see pieces, show them (up to 8 per call).
- Cite pieces by product name, date and entry ID. `pdf_url` opens the full piece as a PDF.
- Keep observation and interpretation apart: "Amex mailed 175,000-point Platinum offers in September" is an observation; "this suggests a push on premium acquisition" is an inference, so label it.

## Guardrails

- Everything you state should trace to a tool result. Don't invent pieces, entry IDs, offer terms, dates or counts.
- The archive is a panel sample of marketing, not the whole market. Say "not seen in the archive" rather than "X never offered" or "X stopped mailing", and only after checking a long enough window.
- If OCR wording is unclear, say so rather than silently correcting it.

## Examples

**"What has Capital One been mailing lately?"**
`search_campaigns(company=["Capital One"], company_match="contains", media_channel=["Direct Mail"], date_from=<90 days ago>, date_to=<today>, limit=50)` → group by product line (cards, auto loans, bank, Discover) and mailing type → read 3–5 distinct acquisition pieces for terms → answer by product line → `show_pieces` with 4–6 examples.

**"Compare Chase and Amex sign-up bonuses."**
`discover_filters(field="company", query="chase")` → one search per company with identical filters (exact names, sector Credit Cards, Direct Mail, mailing_type Acquisition, last 90 days) → read the distinct offers → table per card: bonus, spend requirement, annual fee → show the flagship piece from each.

**"How have balance transfer offers changed since 2020?"**
One search per year over the same month (September 2020, September 2021, …): sector Credit Cards, Direct Mail, `advanced_filters={"mailing_type": ["Acquisition"], "intro_pricing": ["BT Intro"]}`, `include_total=true`, limit 15 → read a few per year for intro period, BT fee and go-to APR → table by year → note that counts are panel captures, not market volume.

**"Show me 2026-09-09-5185."**
`show_pieces(["2026-09-09-5185"])`, then `read_piece` as well if they want it summarised.
