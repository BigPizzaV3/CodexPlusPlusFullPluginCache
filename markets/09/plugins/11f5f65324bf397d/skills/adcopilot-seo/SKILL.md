---
name: adcopilot-seo
description: Answer questions about the customer's organic search presence through Google Search Console — why pages are not indexed or not ranking, what people search to find them, which pages earn clicks, whether a sitemap is being read, and whether a page has been crawled recently. Use when the user asks about their own site's Search Console data, indexing, indexed pages, crawling, sitemaps, rankings, keywords they rank for, organic or SEO traffic, why their site does not show up in Google, or how the searches they pay for compare with what they already rank for.
---

# AdCopilot organic review

The customer wants to know how Google search sees their site. Answer it through
the AdCopilot connector at `https://mcp.adcopilot.cloud/mcp`.

Call `get_org_context` first, before any other tool, and take from its answer
alone which Google products are connected. `next_step` and `playbook` describe
the account's situation, not necessarily this request: do this request as
written here, pass on what it says about today's operations, and offer its step
afterwards unless this request already covered it. If it asks you to offer a
plan, a purchase, a scheduled task or a routine, or to install something in
another app, leave that part out: none of that is part of this skill. If Search
Console is not connected, say what connecting it would show and stop; the
connect step is the `adcopilot-connect` skill's, and the address to connect it
is the one the server's answer gives. If the server reports Search Console as
connected but needing to be signed in again, it cannot be read yet: say so and
send them to re-approve it at the address the server's answer gives. If it
reports it as connected but out of this connection's reach, the AdCopilot
connection in this client has to be removed and added again so that it asks for
the missing access; say so in the server's words and read nothing from it until
then. Invent nothing about a site you cannot read.

**One thing to get right about `cross_reads`.** It names the reads made OUTSIDE
Google Ads *in service of an ads answer* — on a live account it often says
"make no cross-product read" and names no Search Console read. That is not a
refusal of this skill. When the customer's question IS organic search, Search
Console is the answer and the reads below are the work.
`cross_reads.ads_reads_max` is how many Google Ads reads an ads answer starts
with, and no cap on the Search Console reads below. Follow `next_step` and
the `playbook` as usual, and read `cross_reads` for what it is: guidance for
the other direction.

## Six tools, and what they cannot do

`gsc_list_sites`, `gsc_list_sitemaps`, `gsc_search_analytics`,
`gsc_inspect_url` read. `gsc_submit_sitemap` and `gsc_request_indexing` write —
neither deletes anything, but both are proposed first (the exact site and the
exact address) and sent only after the customer says yes in this conversation,
like every other write. Submitting a sitemap is the right call when none is
listed at all. Resubmitting one is **not** the fix for a URL Google has merely
discovered: it already has the URL.

That is the whole surface, and the gaps matter more than the tools:

- **There is no SITE-WIDE coverage list — but there is a per-URL verdict.** You
  cannot ask for every page Google has not indexed, or a count. For any single
  URL, `gsc_inspect_url` returns exactly why: `coverageState` in Google's own
  words ("Submitted and indexed", "Discovered - currently not indexed",
  "Crawled - currently not indexed", "Excluded by 'noindex' tag"), plus
  `robotsTxtState`, `indexingState`, `pageFetchState`, both canonicals and
  `lastCrawlTime`. Read the whole block, not just the crawl date. For a
  site-wide count, ask the customer to open Search Console → Indexing → Pages
  and use **Export**, then read the CSV they send you — and until they do, say
  you have checked N pages rather than implying you know the site.
- **There is no manual-actions or security-issues read.** You cannot tell
  whether a site has a Google penalty or is flagged as hacked. Never say a site
  has no penalty — say you cannot see penalties and that the customer should
  look under Security & Manual Actions themselves.
- **`gsc_request_indexing` almost never does what its name suggests.** It calls
  Google's Indexing API, which Google documents as crawling only pages carrying
  JobPosting markup, or BroadcastEvent markup inside a VideoObject. For an
  ordinary page Google accepts the request and does nothing. It returns a
  success either way, so do not report it as "indexing requested" and do not
  offer it as the fix for a page that is not indexed. It is the right call only
  for a page that carries that markup, and then only as a proposal that waits
  for their yes. The real remedies for an ordinary page are below.

## Five readings that mislead

Each of these is easy to read wrongly. Do not repeat them.

1. **The sitemap's "indexed" count is dead.** `gsc_list_sitemaps` returns
   `"indexed": "0"` for every site; Google stopped filling that field years
   ago. It is never evidence of an indexing problem. Only the Pages export, or
   `gsc_inspect_url`, says whether something is indexed.
2. **"Average position" is not a rank.** It is averaged across every country,
   device and query where the page appeared at all. A site can show average
   position 3.6 for its own brand name and appear nowhere in the first thirty
   results in its own market. When the customer asks "where do we rank?", do not
   read the average out — narrow it: call `gsc_search_analytics` again with
   `dimensions: ["query", "country"]` (or `["page", "country"]`) and report the
   row for the market that matters to them. That is still their average position
   in that country rather than a live rank, so say which it is; a true rank
   needs a search from that country, which AdCopilot does not do.
3. **Impressions are not demand.** A page can take half a site's impressions on
   queries with no measurable search volume, at position 40-90, earning nothing.
   Before calling any page a performer, look at its clicks and its position, not
   its impressions.
4. **One URL inspection is not coverage.** Inspecting a page that happens to be
   indexed tells you nothing about the rest. Sample across page families — a
   product page, a blog post, a docs page, a newer page — or say you only
   checked one.
5. **The data is two to three days behind.** Search Console has not finished
   counting the last few days, and the missing days come back as absent rows,
   not zeros. So a seven-day window is really four or five days of data, and
   "clicks fell off a cliff this week" is usually the lag. Pass dates as
   YYYY-MM-DD, end the window three days before today, and say which dates you
   actually read.

## The sequence

Work in this order. When the server refuses a read at the daily limit: say
what ran and what it showed, then the server's own line about the limit, word
for word, every time, once however many reads it refused.

1. **Which property.** `gsc_list_sites`, then use the exact `siteUrl` it
   returns. A domain property and a URL-prefix property are different sites.
2. **Is the sitemap being read.** `gsc_list_sitemaps`: how many URLs are
   submitted, when Google last downloaded it, and whether it reports errors.
   Ignore the indexed column.
3. **Which pages earn anything.** `gsc_search_analytics` with
   `dimensions: ["page"]` over 28 days, and pass `row_limit` explicitly — the
   default is 1,000 and the tool cannot paginate, so a bigger site comes back
   silently cut. If the row count equals the limit you asked for, say the list
   is truncated and that the ratio is a floor, not the figure. Compare the pages
   that got a single impression against the number submitted; that ratio is
   usually the story.
4. **What people typed.** The same call with `dimensions: ["query"]`. Read it
   for two things: the queries worth winning, and the queries the site is
   attracting but cannot serve.
5. **Whether Google has looked recently.** `gsc_inspect_url` on the pages that
   matter — the home page and two or three pages the business earns from.
   `lastCrawlTime` is the figure to read out: a page last crawled weeks ago is
   being served to searchers as it was then, whatever the site says now.

## Reading the coverage export, when they send it

Two rows decide the diagnosis, and they mean opposite things.

- **"Discovered – currently not indexed"** — never fetched. Google's own words:
  "The page was found by Google, but not crawled yet. Typically, Google wanted
  to crawl the URL but this was expected to overload the site; therefore Google
  rescheduled the crawl." So the first cause to consider is the SITE's capacity,
  not the page's quality — how fast the host answers, and how much Google thinks
  it can take. Do not tell a customer their content was judged and found
  wanting; nothing has been read.
- **"Crawled – currently not indexed"** — Google fetched the page and decided
  against indexing it. That one is about the page.

So say which it is before proposing anything, and quote Google's wording rather
than paraphrasing a cause.

For *Discovered*, in this order: how quickly the host answers and whether it is
under load (Google's own stated reason for rescheduling); then fewer thin URLs
competing for the same crawl, since a site asking Google to fetch hundreds of
near-empty pages gets less of what matters fetched; then links to the page from
pages Google already crawls often; then `lastmod` in the sitemap so a changed
page announces itself. Submitting the sitemap again changes nothing — Google
already has the URL, which is what "discovered" means. For one page the customer
cares about, they can also press **Request indexing** in Search Console's URL
Inspection screen themselves; Google limits how many they can send a day.

For *Crawled*, Google adds "no need to resubmit this URL for crawling" — it has
been read and not chosen, so the page itself has to become worth indexing.

## Does the page say what people typed

For any page ranking far down on a query it should own: **does the page contain
the query?** AdCopilot cannot fetch a page. If the page's text is already in this
conversation — the customer pasted it, or you can already read the page — read
it; otherwise ask the customer for the title, the main heading and the opening
sentence. Never describe a page's wording you have not read. Then look for the
phrase people actually typed. A page can be long, well-built and entirely about
the subject while never once writing the sentence the searcher wrote, and
position 60-80 is exactly where Google puts a page it finds topically close but
not an answer. No amount of linking fixes a phrase the page never says, and it is
usually a one-line edit.

## The answer

Use the names Google prints on its own screens (Indexing, Pages, Performance),
not tool or field names.

**One headline line.** Clicks, impressions and click-through over the period,
and how many pages earned anything out of how many submitted.

**Then at most three findings, biggest first,** each with its numbers: the page
or query, the position, the clicks. Say plainly what each means — "impressions"
are how often it appeared, "position" is where in the list on average.

**Then one recommendation**, as a proposal they say yes or no to, with what it
takes to do and what leaving it risks. Name the page and the change.

**Then what you could not see:** coverage, penalties, security. Ask for the
Pages export if coverage is the question they actually asked.

## When they also run ads

If Google Ads is connected as well, the comparison worth making is which terms
they pay for and already rank for. Three buckets: paying and ranking well, where
the paid click may be buying a visit the site already earns without it; paying
with no organic presence, where paid is the only route; ranking well without
bidding, which is often the cheapest visit on the list.

Run it with `paid_vs_organic`. It sets the account's Google Ads search terms
beside one Search Console site's queries over the same dates. Pass the account's
`customer_id` from `get_org_context` (ask which account if several are switched
on and the customer named none), `site_url` as the exact Search Console site
(if several are switched on and none is named, it asks which — put that question
to the customer), and `days` (7 to 90; it defaults to 28). It groups the terms
as: paid and ranked in the top three; paid and ranked lower; no Google Ads search
term found for a query the site ranks top three on; the same for a query it ranks
4 to 20 on, which are the candidates to test an ad; and paid with no Search
Console row. Say which bucket each term is in, and name any paid term where the
site ranks in the top three. Read its limits out with the answer:

- Only identical wording is matched, so "shoe" and "shoes" are different terms.
- "Paid, no Search Console row" means no row was found, not that the site has no
  page for it: Search Console withholds rare queries and lags about three days.
  If the Search Console reply was cut at the most rows the look-up reads, the
  tool says so and withholds that count; do not make one up.
- "No Google Ads search term found" means none in the search-term report, which
  hides low-volume terms and does not show Performance Max terms, so the query
  may already have an ad.
- A term containing the site's own name is marked as brand and set aside.
  Whether to pay for one's own name is a different decision from the rest of the
  list, and it can be worth paying for.
- Position is an average, not a rank (reading 2 above).

If you quote what a term costs, mind the money: the tool's cost figures are
already in the account's currency (`get_org_context` says which one), and its
`cost_micros` fields are millionths of it, so never print a micros number as
money. A raw `search` returns `metrics.cost_micros` the same way: divide by
1,000,000 once and name the currency. The spend and results of each *keyword*
(as against each search term) stay a raw `search` read over `keyword_view`,
because no lens returns them. `analyze_search_terms` and `analyze_waste` show
only the paid search terms and campaigns that spent with no conversions, which is
the "paying but no result" bucket.

When a `search` on `campaign` or `search_term_view`, or `analyze_waste` or
`analyze_search_terms`, ends with `related_reads`, run the ones that bear on the
comparison, at most three, then answer from all you hold; never repeat a read you
hold, and offer, do not chase, the `related_reads` those reads bring back. They
are reads only: a change is still only proposed.

## What breaks

Reporting average position as a rank. Turning the rows into a verdict — "Google
shows you at the top", "your name wins" — when a row exists only for a search where
the site was shown, so the data cannot say where people searched and did not see you.
Calling a high-impression page a good page.
Telling a customer their pages are indexed on the strength of one inspection, or
not indexed on the strength of the sitemap's dead column. Offering to request
indexing as though it worked. Promising a site has no penalty when you cannot
see penalties. Every one of these reads as a confident answer and sends the
customer the wrong way.

## What is next

Offer, in this order: the one-line page edit you found; the links that would get
the uncrawled pages crawled; and the Pages export, so the next review can say
what is actually indexed.

Once they say the edit is live, invite them to ask again in a few days and
inspect that page then: `lastCrawlTime` says whether Google has fetched the new
version, and the coverage verdict whether it changed anything. That second look
is how they learn whether the edit worked.

If Google Ads is connected and this reply has not already compared paid and
organic, offer it as a question: which of the searches they pay for already
bring them organic clicks, how many, and what those paid clicks cost — the
comparison in "When they also run ads". Propose a change from it only where
the Ads numbers for those searches show no results, with the money both ways,
pausing rather than removing, and applied only on their yes.
