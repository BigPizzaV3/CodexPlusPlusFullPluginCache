---
name: start
description: Route a live pet project through the atlas — take the reports of the existing SEO and GEO audits, merge them into one prioritised list, link the page that explains each item, and name three things to do this week. Use when the user says "nobody finds my project", "where do I start with SEO", "прогони проект по атласу", or pastes an SEO or AI-search audit of their site and asks what to fix first.
---

# start

**This skill runs no checks of its own.** It orders the output of two audits that already exist,
`seo-audit` and `geo-audit`, against the atlas route. Every finding below comes from one of their
reports. If you find yourself fetching `robots.txt` by hand, you have left this skill — stop and ask
for the report instead.

## 1. Ask two questions

Ask both before running anything, and wait for the answers:

1. **The URL of the live site.** Not a staging host, not localhost. The audits read what search reads.
2. **The language the audience searches in.** It decides which results pages matter and what language
   the recommended pages are written in. It is not the language of the interface.

If the project has no public URL — it lives only in Telegram, in a store, or in an app — say so and go
straight to [search inside the platform](https://atlas.smolevich.com/distribution/in-platform-visibility/).
The audits below need a page to fetch.

## 2. Get the two audit reports

`seo-audit` and `geo-audit` are open-source skills maintained by other people. They run in a coding
agent on the user's computer, not here. Ask the user to paste or upload the full output of both, run
on the URL from step 1. If either audit is available as a skill in this environment, run it on that
URL instead of asking.

If a report is missing, **say so and stop**. Do not substitute your own checks — a hand-rolled audit is
a worse audit that looks like a real one. Do not try to install anything. Give the user the install
lines to run in their own coding agent, and say who maintains each package:

```bash
npx skills add -g coreyhaines31/marketingskills
npx skills add -g zubair-trabzada/geo-seo-claude
```

`seo-audit` comes from `coreyhaines31/marketingskills`, `geo-audit` from `zubair-trabzada/geo-seo-claude`.
Neither is part of this plugin. Once the user has both reports, they bring them back here.

That is the whole answer when a report is missing. End it there: no questions about the site, no
"meanwhile" tip, no list, no route. The closing line about tagging links in section 6 belongs to a
finished run, not to this one.

What each tool is and where it comes from: <https://atlas.smolevich.com/tools/skills/>.

## 3. Read them, in this order

1. **`seo-audit`** first. Fetch, block, canonical, indexing, on-page, speed.
2. **`geo-audit`** second. Crawler access, citability, schema, `llms.txt`, platform readiness.

SEO first. Access and indexing decide whether anything else is even read. A citability score for a page
no agent can fetch is a score of a document nobody has.

Check that both reports are for the URL from step 1. If they name another host, say so before merging.

Keep both raw reports. You will cite lines out of them, not summarise them into adjectives.

## 4. Merge into one list

One list, not two. Drop the composite scores — a score moves when anything moves and tells the reader
nothing to do. Keep the individual findings.

Order by this rule, top down. The first rung that is broken outranks everything below it:

1. **Fetchable** — the page returns body text to a plain client. Any crawler, search or AI, that gets
   a 4xx, a 5xx, a challenge page or an empty body is on this rung, whatever produced it: a CDN or
   WAF rule answering 403 to `ChatGPT-User` is a fetch failure, not a directive.
2. **Allowed** — the page is fetched but tells the crawler to stay out: `robots.txt`, `noindex`,
   `X-Robots-Tag`.
3. **Indexed** — submitted, discovered, in the index.
4. **Findable** — the pages answer phrases people actually type.
5. **Quotable** — an assistant can lift a passage and attribute it.
6. **Attributed** — you can say which link sent the person.

Deduplicate across the two reports. Both audits flag crawler access; that is one row, not two.

Drop anything the audits report that this project cannot act on this month. A finding nobody will do is
noise in the list.

## 5. Link the page for every item

Each row gets exactly one atlas link. Route by symptom:

| Finding | Page |
|---|---|
| Not fetchable, blocked, `noindex`, wrong canonical, JS-only body | [Google does not see your site](https://atlas.smolevich.com/indexing/why-google-does-not-see-you/) |
| Not submitted, no sitemap, stale URLs, only the home page indexed | [Submit and verify](https://atlas.smolevich.com/indexing/submit-and-verify/) |
| AI crawler blocked, or a published `llms.txt` gone stale | [AI crawlers and llms.txt](https://atlas.smolevich.com/geo/llms-txt-and-crawlers/) |
| Low citability, no JSON-LD, no `sameAs`, assistants cite competitors | [Why AI answers cite someone else](https://atlas.smolevich.com/geo/citable-pages/) |
| No impressions, pages target phrases nobody types, pages compete | [What to write about](https://atlas.smolevich.com/content/keyword-clusters/) |
| Thin page, no answer up top, no failures block, weak titles | [What a page is made of](https://atlas.smolevich.com/content/page-templates/) |
| Page two everywhere, no external links, no mentions | [Where the first links come from](https://atlas.smolevich.com/distribution/catalogs/) |
| The product lives in a messenger or a store | [Search inside the platform](https://atlas.smolevich.com/distribution/in-platform-visibility/) |
| Cannot say which numbers to read, activation unnamed | [The numbers worth reading weekly](https://atlas.smolevich.com/analytics/what-to-measure/) |
| Links untagged, everything reads as direct | [Where the user came from](https://atlas.smolevich.com/analytics/attribution/) |
| It works and costs more than it earns | [What one user costs](https://atlas.smolevich.com/money/unit-economics/) |

A finding with no page in this table still goes in the list, marked as having no atlas page yet. Do not
invent a URL to fill the column. It keeps its rung: a slow page is still **Findable** and sits above every
**Quotable** row, not at the bottom because the link column is empty.

Output one markdown table: rank, finding, the audit line it came from, the page.

## 6. Close with three things for this week

Exactly three. Not five, not a backlog.

- Take them off the top of the merged list, highest broken rung first.
- Each one is a thing a person finishes in an evening. "Improve content" is not one.
- Each one names how you will know it worked — a command, a report, a number.

Add one line the author cannot get from an audit: **tag your outbound links today if they are not
tagged.** Attribution is the only item on the route that cannot be reconstructed later, so an untagged
week is a week of arrivals nobody will ever classify. That is
[attribution](https://atlas.smolevich.com/analytics/attribution/).

Then point at the full route for what comes after this week:
<https://atlas.smolevich.com/start/>.

## Rules

- Do not invent findings. Everything in the list traces to a line in one of the two reports.
- Do not report a score as an outcome. Report what to change.
- If an audit fails to run, say which one and why. A half audit presented as a whole one is the failure
  mode this skill exists to avoid.
