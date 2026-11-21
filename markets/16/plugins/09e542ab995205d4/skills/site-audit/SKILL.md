---
name: site-audit
description: 'Audit a whole website for AI search: whether AI apps and search engines can read and index each main page, whether the site states the facts that buyers ask about, and whether each page can be quoted. Returns an ordered list of exact changes. Use for "audit my site for AI search", an AEO or AI SEO site audit, or a site check before content work. Needs no Frontmost AI account.'
---

# Site audit

The `ai-readiness` skill checks whether AI apps can read the home page. This skill checks the main pages of the site, and what those pages say.

An AI app can quote only what a page states in text. So the audit has four parts: access, indexing, facts, and pages that can be quoted.

## 1. Pick the pages

1. Fetch `https://<site>/robots.txt`. Read its `Sitemap:` lines. If there is none, try `https://<site>/sitemap.xml`.
2. Fetch the home page, with its response headers.
3. Pick up to 12 pages: the home page, the pricing page, each main product or service page, the About page, the contact page, the comparison pages, and the guides that the home page links.
4. Add each page that the person names.
5. Say which pages you read. The audit covers those pages only.

## 2. Access

For each page, do the five checks of the `ai-readiness` skill for that page's path. Then check three more things:

| Check | Passes when |
|---|---|
| Status | The address returns the page itself. It does not return an error or a redirect to a different page |
| Canonical | The page's canonical link is the page's own address, or the address that the owner intends |
| No leftover block | No `noindex` remains from a test version of the site |

## 3. Indexing

Google's AI features read Google's index. Copilot reads Bing's index. A page that is in neither index cannot appear in those answers.

1. Check that the sitemap lists each picked page.
2. Check that the sitemap holds no address that redirects, returns an error, or has `noindex`.
3. Check that each page has a title and a meta description that say what the page is about.
4. Ask the person to read the index status of the main pages in Google Search Console and in Bing Webmaster Tools. Those two tools are the only sources of the real status.
5. If the person cannot open those tools, a `site:` search is a rough check. Say that it is rough.
6. Ask the person to read two reports, if their account shows them. Google Search Console has a generative AI performance report. Bing Webmaster Tools has an AI Performance report. On November 13, 2026, the Google report showed impressions only, and a small site can have no report. Record "not visible" when a report is absent.

If the site sends new addresses with IndexNow, a 200 response means "received". It does not mean "indexed".

## 4. Facts

A buyer asks an AI app about eight facts. For each fact, record the page and the exact sentence that states it, or write "not stated".

| Fact | The site states it when |
|---|---|
| What the business sells | One sentence gives the product or the service and its category |
| Who it is for | A sentence gives the buyer: a job, a business type, or a need |
| Where it works | A sentence gives the countries, the cities, or the service area |
| Price | A page gives the price, or the things that set the price |
| Limits | A page says what the product does not do, or who it does not fit |
| How it differs | A page compares the business with alternatives that it names |
| Proof | A page gives customers, reviews, or numbers, each with its source |
| Who is behind it | A page gives the people or the company, and a way to contact them |

Then check two things for each fact that the site states:

- **The fact is in the text.** A fact that is only in an image, a video, a PDF file, or a part of the page that needs JavaScript does not count.
- **The fact is the same on each page.** Compare the name, the one-line description, and each price across the pages. Report each conflict with both quotes and both addresses.

## 5. Pages that can be quoted

For each picked page, read the HTML that the server sends. Check:

| Check | Passes when |
|---|---|
| Direct answer | The first paragraph says what the page is about in two or three sentences that make sense alone |
| Clear headings | Each heading gives the subject of its section |
| Sections that stand alone | A section gives the name of the product or the business. It does not rely on "it" or "our tool" from an earlier section |
| Specific facts | The page gives numbers, names, and dates. It uses "best" or "leading" only with a source |
| One subject | The page covers one use, one product, or one question |
| A date | A page with facts that change, such as prices, shows when it was last checked |

To test a section, read it without the rest of the page. If you cannot tell which business and which product it describes, the check fails.

## Order of the changes

1. Access: a blocked crawler, a `noindex`, or text that needs JavaScript. A page that AI apps cannot read gains nothing from the other changes.
2. Indexing: the sitemap, the canonical link, and the missing titles and descriptions.
3. Facts that conflict, then facts that the site does not state.
4. Pages that cannot be quoted.
5. Pages to add. Use the `page-drafting` skill for each one.

## Rules

- Use evidence that you saw. Quote the line, the tag, or the sentence, with the page address.
- Not verified means that a check did not run. It is not a failure. Give no change for it.
- Make each change exact: the page, the text there now, and the new text.
- Never write a fact for the business. If a fact is missing, ask the person for it.
- If you work in the site's code and the person asks, make the changes on a branch for the person to review.
- Do not say that a change will raise citations or mentions.

## Never suggest

- `llms.txt` files or "AI schema" as a fix. They are unproven. Google states that its own AI features need no new files and no special markup.
- Text that only AI apps can see, or hidden text of any kind.
- A keyword repeated to fill a page.

## Output

1. A table of the pages that you read: the page, access, indexing, and the checks of part 5 that fail.
2. The eight facts, each with its sentence and page, or "not stated".
3. The conflicts, each with both quotes.
4. The changes, in the order above. For each one: the page, the evidence, and the exact change.
5. What you could not check.

End with one line: the audit shows what the site says. It does not show whether AI apps mention the business. For that, use the `mention-check` skill.
