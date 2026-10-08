---
name: geo-content-engineering
description: >-
  Create or rebuild web content so generative engines (ChatGPT, Gemini,
  Perplexity, Google AI Overviews) extract, cite, and mention it. This is the
  discipline called GEO (Generative Engine Optimization), also known as AI
  visibility, LLM SEO, or answer engine optimization. Use this skill whenever the
  user wants to write, restructure, or optimize any web page, article, guide,
  landing page, pillar page, or FAQ for AI search visibility, citations, or brand
  mentions. Trigger it when they mention GEO, generative engine optimization, AI
  visibility, LLM SEO, answer engine optimization, semantic chunking, getting
  cited by ChatGPT or Perplexity, or making content "AI-readable"; and also when
  they ask softer versions like "help me write content that AI will recommend,"
  "why doesn't ChatGPT mention my brand," or "how do I show up in AI answers."
  Covers both new content creation and rebuilding existing pages, plus the
  Share-of-Mentions measurement loop.
---

# GEO Content Engineering

Build web content that generative engines will pull into their answers. The
goal is not ranking in a list of blue links. The goal is being the block of text
a model extracts, the source it cites, and the brand it names when a user asks a
question.

## Why this changes how you write

Generative systems do not read a page top to bottom. They split it into semantic
blocks (chunks), turn each block into a vector embedding, and for any given
prompt they retrieve the single block whose embedding is closest to the prompt.
That retrieved block is what gets quoted, summarized, or cited. One sharp,
self-contained paragraph often beats an authoritative domain, because the model
scores the block, not the whole site.

Everything in this skill follows from that mechanic. Full explanation in
`references/mechanics.md`. Read it once if the user is new to GEO.

Three layers have to be right, in this order. A perfect text on a page a bot
cannot read is invisible. So gate access first, then structure, then reputation.

1. **Access.** The bot must reach and render the content. See
   `references/crawler-access.md`.
2. **Content and structure.** The text must be chunkable, quotable, complete,
   and current. This is the bulk of the work below.
3. **Off-page grounding.** External mentions confirm the claims. See
   `references/offpage-mentions.md`.

## Pick the mode

**Mode A: New content.** The user is creating a page that does not exist yet.
Go straight to Build.

**Mode B: Rebuild an existing page.** The user has a live URL that underperforms
in AI answers. Do not touch the text until you have a baseline, or you will not
be able to prove the rebuild worked. Run these first:

1. Measure a baseline Share of Mentions for the target topic cluster before any
   edit. See `references/measurement.md`.
2. Check the access gate on the live URL. See `references/crawler-access.md`. If
   the bot cannot render the page, fix that first. Rewriting an unreadable page
   is wasted effort.

Then both modes converge on Build.

## Build

Use the page skeleton in `assets/page-structure.md` as the frame. Fill it by
applying six content rules. Each rule has a full reference file; read the file
when you need depth, not before.

1. **Semantic chunking.** One block, one claim. Answer first, then evidence.
   Every block has to make sense lifted out of the page on its own. Name the
   entity instead of using pronouns ("the Model X battery," not "it"). Phrase H2
   and H3 headings as the questions users actually ask.
   → `references/chunking.md`

2. **Dense, plain language.** Active voice, short sentences, no filler. Every
   wasted word blurs the block's embedding and makes it lose retrieval to a
   tighter competing block. When there is no blanket answer, state the condition
   directly ("if you need A, choose option 1") instead of hedging.
   → `references/language.md`

3. **Citation-worthiness.** Give the model something it cannot get elsewhere:
   concrete numbers, ranges, prices, technical parameters, and your own data.
   "42 percent faster" is quotable; "much faster" is not. Duplicate the key
   figure of any chart or calculator in plain text, or the model cannot read it.
   → `references/citation-worthiness.md`

4. **Query fan-out coverage.** Engines split one complex prompt into
   sub-questions and answer each separately. Cover the adjacent questions
   (price, risks, alternatives, step-by-step, common mistakes) as their own
   blocks and FAQ entries, so one page can feed several parts of one answer.
   → `references/query-fan-out.md`

5. **Recency.** Models favor fresh content, sometimes over better but older
   content. Put a visible date marker in the text ("As of 03/2026: ...") and
   keep a short "What changed" box. A CMS timestamp alone does not count, and
   changing the date without a real update is detectable and increasingly
   penalized.
   → `references/recency.md`

6. **Authorship and trust (E-E-A-T).** Named, verifiable authorship beats
   anonymous content in retrieval. Add an author box with name, credentials, and
   a profile link, and keep those details consistent with external profiles.
   → `references/author-eeat.md`

## Technical markup pass

Machines read code structure, not visual layout. Something that looks like a
table but is built from `div` containers is useless for extraction. Before
publishing, confirm:

- Semantic HTML tags (`article`, `main`, `header`) mark what is content and what
  is chrome.
- Comparisons are real `table` markup, not styled divs. Tables are among the
  most frequently lifted elements.
- Schema.org via JSON-LD is present: `Article` for posts, `Person` for authors,
  `FAQPage` for question blocks, `Product` and `Offer` for offerings.
- Core content is in the initial server HTML response, not injected by
  client-side JavaScript.

Full requirements in `references/semantic-html.md`. Paste-ready JSON-LD in
`assets/json-ld-snippets.md`.

## Anti-patterns pass (blocking)

Run the finished text against `references/anti-patterns.md` before calling it
done. Two failure classes matter most:

- **Structural failures** that break extraction: mechanical length-based cuts,
  claims trapped in images, fake tables, timestamp gaming.
- **Machine-tell language** that marks the text as AI-generated and erodes both
  reader trust and differentiation from mass-produced competitors. This is a
  registry of specific English words and phrasing patterns to strip out (delve,
  seamless, tapestry, testament to, navigate the complexities, and more). The
  irony is real: content built for AI visibility must not read as if a machine
  wrote it. Treat this pass as blocking, not cosmetic.

## Publish and register

When the page goes live, record the URL and publish date in an input register.
Without that record you cannot later attribute any change in visibility to this
work. The register entry is part of publishing, not an optional follow-up. Format
in `references/measurement.md`.

## Measure

Web traffic is a weak KPI here, because users get their answer inside the AI
interface without clicking (zero-click). Measure presence in the answers
themselves.

- **Share of Mentions (SoM):** share of tracked prompts whose answers mention the
  brand. This is the lead metric.
- **Share of Direct Citations:** share of prompts where the model links your site
  as a source.
- **Indirect Citations:** prompts where the model cites an external source that
  points to the brand.

Prefer shares over raw counts, benchmark the same prompts for competitors, and
validate sentiment by hand on a sample. Full algorithm and blind spots in
`references/measurement.md`.

## When there are many pages

If the user has to choose which pages to rebuild first, prioritize by prompt
demand, competitor gap, business value, and effort, after filtering out any URL
the bot cannot reach. See `references/prioritization.md`.

## Reference map

| File | Read it when |
| --- | --- |
| `references/mechanics.md` | The user is new to GEO and needs the why |
| `references/chunking.md` | Structuring text into extractable blocks |
| `references/language.md` | Tightening sentences and wording |
| `references/citation-worthiness.md` | Adding facts that force a citation |
| `references/query-fan-out.md` | Covering sub-questions and comparisons |
| `references/recency.md` | Date markers and update handling |
| `references/author-eeat.md` | Author boxes and trust signals |
| `references/crawler-access.md` | Checking or fixing bot access (gate) |
| `references/semantic-html.md` | Markup, tables, JSON-LD, architecture |
| `references/offpage-mentions.md` | External mentions and consistency |
| `references/measurement.md` | Baseline, tracking, Share of Mentions |
| `references/prioritization.md` | Choosing which pages to rebuild first |
| `references/anti-patterns.md` | Final blocking quality pass |
| `references/glossary.md` | Definitions and tool-terminology mapping |
| `references/worked-example.md` | A full before/after rebuild with rule map |
| `references/evidence-and-sources.md` | What is well-established vs still iterative |
| `assets/page-structure.md` | The page skeleton to fill |
| `assets/faq-block.md` | FAQ block template |
| `assets/update-box.md` | "What changed" box template |
| `assets/json-ld-snippets.md` | Paste-ready structured data |

## Honest limits

There is no industry standard for optimal chunk length, and different engines
cut and score differently, so the work is iterative: publish, measure, sharpen
the blocks that fail to get extracted. Retrieval is a black box with no
guarantees. This skill improves the odds; it does not promise placement.

---

Based on the OKF knowledge bundle "LLM-Content-Erstellung" by Eugen Ullrich
(eullrich.com), CC BY 4.0. Attribution required: Eugen Ullrich, eullrich.com.
Contact: hi@eullrich.com.
