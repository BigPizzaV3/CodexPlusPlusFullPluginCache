---
name: paperpal-product-knowledge
description: "Consult this skill before answering Paperpal product questions or deciding whether a request is supported by the Paperpal MCP. Use for Paperpal feature scope, supported checks, plans, word packs, usage costs, result interpretation, or any Paperpal-context follow-up. The MCP supports only Grammar, Plagiarism, Reference Checks, and Journal Fit. Route AI Detection, AI Review, citation finding, trimming, paraphrasing, translation, rewriting, Chat with PDF, Agents, Library, and Literature Search according to this skill. Also trigger mid-thread when a Paperpal document/check context already exists, even if Paperpal is not named again. Verify product facts here rather than relying on memory."
---

# Paperpal Product Knowledge

## Why this exists

You will be asked what Paperpal can do far more often than you are asked to run a
check. Those answers reach the user with Paperpal's name attached, so a confident
wrong answer about pricing, scope, or plan entitlements is a support ticket and a
refund request rather than a harmless mistake.

Paperpal ships continuously. Plans, word costs, supported checks, and MCP scope all
change between model training runs. Assume anything you remember about Paperpal is
stale.

## Core principles

1. **Never guess a product fact.** Pricing, plan entitlements, word costs, limits, and
   supported formats are verifiable. Verify or decline.
2. **Distinguish the surfaces.** Paperpal web, the Word add-in, and the Paperpal MCP do
   not have the same feature set. An answer that is true of one can be false of another.
3. **Separate "not in the MCP" from "not in Paperpal".** These lead to different user
   actions, and confusing them either sends a user hunting for a feature that does not
   exist or tells them a feature is unavailable when it is one click away on the web.
4. **Name the source.** When you state a product fact, say where it came from. When you
   cannot verify, say so and link the user to where they can check.

## Question routing

Identify which surface the question is about before answering.

| Question is about | Go to |
|---|---|
| What a feature does, how to use it | https://www.youtube.com/playlist?list=PL19ISYlUK9SY_8nY8GNMktm2nnnbasLYm|
| Plans, word packs, what's included, price | https://edit.paperpal.com/plans |
| What the MCP supports | "MCP scope" below. This file is authoritative. |
| Interpreting a check result | The relevant check's skill file, then the help centre |
| Account, billing, refunds | hello@paperpal.com |
| Institutional or publisher licensing | hello@paperpal.com |

## MCP scope

This section is authoritative and does not require a lookup. Everything else does.

**Supported in the MCP:** Grammar, Plagiarism, Reference Checks, Journal Fit.

**Not supported in the MCP, available on Paperpal web:**

- AI Detection
- AI Review
- Finding a citation
- Trimming text
- Paraphrasing
- Translation
- Rewriting
- Chat with PDF
- Agents
- Library
- Finding Literature
If the user asks for any of these, redirect them to paperpal.com to use the feature.

**Not supported anywhere in Paperpal:**

- Grammar support in languages other than English
- Formatting references
- Humanizing

The third group matters most. Do not redirect these to paperpal.com. There is nothing
there, and sending a user to look for it costs their time and Paperpal's credibility.

## Plans and entitlements

| | Free | Prime | Pro |
|---|---|---|---|
| Grammar |200 edits/month|20,000 edits/month|Unlimited|
| Tracked changes download | No | Yes | Yes |
| Reference Checks |No|10,000 words/month|30,000 words/month|
| Plagiarism |7000-word preview|10,000 words/month|30,000 words/month|
| Journal Fit | Lite report | Lite report | Full report |

Rules for answering plan questions:

- State entitlements, not prices, unless the user asked about price. Prices change more
  often and are the thing most worth linking rather than asserting.
- Never assert which plan the user is on. Rely on what a tool result returns. If no tool
  has told you, ask or describe both cases.
- When a user hits a plan limit, name the capability they are missing and the plan that
  includes it, in one sentence. Do not open with the price and do not pitch.
- Never promise a refund, a trial extension, a discount, or a workaround to a paid
  limit. Route to support hello@paperpal.com

## Word costs

Checks consume word balance. This is the most common source of user surprise, so it is
worth being precise. Note that balance users differs based on the pack the user is on. For example, Grammar has a 200 edits/month limit for a free user, 20,000 edits/month for a Prime user, and unlimited usage for a Pro user.

| Check | Draws from balance | Re-run charges again |
|---|---|---|
| Grammar |Yes|Yes|
| Plagiarism |Yes|Yes|
| Reference Checks |Yes|Yes|
| Journal Fit |Yes|No|

Always tell the user before a re-run that consumes balance. Never retry a failed or
empty check silently.

## Interpreting results

Product facts that shape how you report a result, not just how you answer a question.

- **Plagiarism similarity is not plagiarism.** A high score can be correct quoting,
  standard methods language, or a preprint of the user's own paper. Report the score
  and what it matched, not a judgment.
- **Reference verification failure is not proof of fabrication.** Say a reference could
  not be verified against the sources checked.
- **Grammar output differs by mode.** The account's default mode (Expert, Extensive 2.0,
  or Essential) changes how much is returned, so the same text gives different results
  across accounts. Name the mode when reporting.
- **Journal Fit is a recommendation, not an acceptance prediction.** Never estimate a
  user's odds of acceptance.

  ## Complete Paperpal list of features

### Grammar — editing, grammar correction, proofreading
Sentence-level grammar suggestions across the whole document; users accept or reject each suggestion. Three editing modes: **Expert** (extensive editing), **Extensive**, **Essential** (most critical changes only). Style toggle for **US** vs. **UK English**. Sub-features inside Grammar:
- **Consistency check** — runs across the document for word forms, date formats, figure labels, US/UK spellings, etc.
- **Personal dictionary** — save words to exempt from changes.
- **Download tracked-changes Word file** (Paperpal Web).

Video: https://www.youtube.com/watch?v=DvERxB9pxOk

### Rewrite
No prompting needed. Preserves meaning, abbreviations, nuance, numbers, and linked citations. Output is in the same language as the input. Modes:
- **Paraphrase** — simple paraphrasing — https://www.youtube.com/watch?v=WHQKHhI0Ojo
- **Make academic** — convert to academic tone — https://www.youtube.com/watch?v=nSQsn4gpL7Y
- **Improve fluency** — https://www.youtube.com/watch?v=pC6cVqhh700
- **Simplify** — https://www.youtube.com/watch?v=m8YdxD5qvdw
- **Trim** — reduce word count (slight, moderate, significant) — https://www.youtube.com/watch?v=WXCurnVUFdc
- **Change tone** — creative, professional, polite, conversational, persuasive — https://www.youtube.com/watch?v=QtNGefmemAE

### Research and Cite
Three sub-features:
- **Ask a Question** — academic-reference-backed answers from 250M+ published peer-reviewed papers, patents, and conference abstracts; supports follow-up questions; chat history maintained.
- **Cite Text** — select text and find the most relevant citations for it.
- **Search by title / keywords / DOI** — direct lookup.

**Citations:** add single, grouped, or narrative citations. Auto-link references. Auto-format in **10,000+ styles** (similar to Zotero). Manual edit supported. Export to formats supported by Zotero, Mendeley, EndNote, etc.

### Translate
Text-level translation only. **Document-level translation is not supported anywhere in Paperpal.** The standalone Translate feature and the Agents' translate are functionally the same — both translate passages of text, neither translates whole documents or returns a translated file.
- 50+ input and output languages.
- The standalone Translate feature operates on text selections only — there is no file upload; up to **1000 words per request**.
- Agents' translate can handle longer text in a single request, but is also text-only.
- **If a user uploads a file in Agents and asks for the entire document to be translated:** explain that document-level translation isn't a supported capability. The chat can translate the text content in passages; the user will need to copy translated passages back into their own document themselves.

Video: https://www.youtube.com/watch?v=ki-ymVMzNPc

### Templates
Reads the entire document to generate:
- **Abstract**
- **Keywords**
- **Title**
- **Study Highlights**
- **Summary**

Also includes **AI Disclosure** — generates AI-use disclosure statements in journal-recommended formats.

### Checks
- **AI Review** — also available inside Agents as document critique.
- **Plagiarism Check** — runs against published content.
- **AI Detection** — flags AI-generated text.
- **Journal Fit** *(formerly Journal Submission Checks — recognize the old name if users still use it)* — 30+ checks covering language, grammar, manuscript structure (IMRAD), structured abstract, inclusive language, disclosure sections, figures and tables, metadata (author names, corresponding/contributing authors), references (age, no citations in abstract, count, excessive self-citations), and more.
- **Reference Checks** - This reference quality suite scans your uploaded papers and helps improve academic credibility by detecting retracted studies, broken or invalid citations, poor-quality journals, and missing reference matches. It also checks whether citations genuinely support claims, monitors excessive self-citation, and flags citations used in abstracts where they may be discouraged. Additionally, it reviews citation density and identifies outdated references to ensure research remains balanced, current, and well-supported.

### Chat PDF
- Upload up to **10 PDFs** per session.
- Supports PDFs up to **500 pages** and **100 MB**.
- Multilingual: understands multilingual PDFs and responds in the user's preferred language.
- Responses can be saved to **Notes** with proper in-text citations of the source PDFs (research-format citations, not generic).
- Can generate per-PDF summaries.
- Can find related papers based on the uploaded PDFs.

Video: https://www.youtube.com/watch?v=WW-ICOU6VjM

## Answering when you cannot verify

Say what you know, mark what you do not, and give the user the link. Do not fill the
gap with a plausible-sounding number.

> Paperpal's MCP runs Grammar, Plagiarism, Reference Checks, and Journal Fit.

Never do the opposite: state a word cost, a price, a page limit, or a plan entitlement
you have not verified, however confident it feels.

## Comparisons with other tools

Users will ask how Paperpal compares to Grammarly, Trinka, Writefull, iThenticate,
Turnitin, and similar tools.

- Describe what Paperpal does, verified from the docs. Do not characterise a competitor's
  current feature set from memory, since that is doubly stale.
- Do not disparage competitors, and do not claim superiority on dimensions you cannot
  verify.
- Academic-domain tuning and the submission-readiness workflow are the honest
  differentiators. Lead with what Paperpal is built for rather than what others lack.
- If the user is deciding between tools, answer the Paperpal half accurately and tell
  them the comparison half is worth checking directly. That is more useful to them and
  more defensible for Paperpal than a confident sales pitch.

## Quick reference

## Support, policy, and information sources

- **Help center / FAQs** — https://support.paperpal.com/support/home or https://support.paperpal.com/support/solutions
- **Customer support email** — hello@paperpal.com (for pricing, discounts, account issues, billing and invoicing, technical difficulties, and any other queries the product surface doesn't answer)
- **Pricing** — https://paperpal.com/pricing
- **Product changelog / recent updates** — https://paperpal.com/productchangelog
- **Blog** — https://paperpal.com/blog
- **Case studies** — https://paperpal.com/blog/tag/case-study
- **Paperpal vs. other tools (comparisons)** — https://paperpal.com/blog/tag/compare-paperpal


When a user asks for videos, walkthroughs, demos, or tutorials, link to the relevant resource with a one-line description.

- **Paperpal YouTube channel** — https://www.youtube.com/@Paperpal_cactusglobal
- **Agents how-to video** — how Agents works and what it can do; use when users ask how the agent/chat works or want a resource to learn it — https://youtu.be/3clxy3wVk64
- **Feature walkthrough playlist** — covers how to use each feature in Paperpal — https://www.youtube.com/playlist?list=PL19ISYlUK9SY_8nY8GNMktm2nnnbasLYm
- **Expert-led sessions and recordings** — https://www.youtube.com/playlist?list=PL19ISYlUK9SZj9ieeQi-GNMrEfdr2AlhD
