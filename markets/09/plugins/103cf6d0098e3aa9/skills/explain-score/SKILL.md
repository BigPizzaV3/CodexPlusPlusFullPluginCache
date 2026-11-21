---
name: explain-score
description: Explain in plain language what a Glippy GEO score, grade and each of the 16 categories mean, and why a site scored the way it did.
---

# Explaining a Glippy score

Use this when the user asks what their score means, why a category is low, or what a term in the report means.

## Work from the actual report

Explain the report in this conversation. If there is none, ask which domain to check and run `analyze_domain`. Quote the site's real category scores and failing checks; do not explain in the abstract when the data is there.

## The score and grade

The overall score runs from 0 to 100 and is built from the 16 category scores. Grades: A+ from 90, A from 80, B from 70, C from 60, D from 40, F below 40. It measures how easily AI search engines and agents can find, read and cite the homepage. It is not a measure of traffic or of how often AI engines cite the site today.

## The 16 categories in one line each

- **Structured Data & Schema:** JSON-LD that tells machines what the page and organisation are.
- **Semantic HTML:** headings, landmarks and lists that give the page a clear structure.
- **Accessibility for Agents:** alt text, form labels, landmarks, a declared language and descriptive link text.
- **Internal Linking:** navigation, breadcrumbs and descriptive links to the site's key pages.
- **Meta & Discoverability:** title, meta description, canonical, Open Graph and Twitter tags, hreflang and the URL slug.
- **Machine Readability:** whether AI crawlers may and can read the page: robots.txt rules per AI crawler, robots meta and X-Robots-Tag, opt-out signals, content present in the HTML without JavaScript, feeds and llms.txt.
- **Entity & Authority:** who is behind the site: organisation details, about and contact pages, consistent identity signals.
- **Citability & Answer-Readiness:** passages an answer engine can quote: direct answers, definitions, sections that stand alone.
- **Performance & Crawlability:** render-blocking scripts, image sizing and lazy loading, DOM size. Low priority for GEO.
- **Agent Interactivity:** machine-readable files for AI agents, such as agent cards, API catalogs and commerce protocols. Low priority for most sites.
- **Content Positioning:** whether the main point appears early and clearly.
- **Content Freshness:** dates and signs the content is maintained, where the page type calls for them.
- **Information Density:** concrete facts, numbers and specifics rather than filler.
- **Factual Verifiability:** sources, evidence and verifiable claims.
- **Content Comprehensiveness:** whether the page covers its topic with enough depth for its type.
- **Multimodal Content:** images, video and tables with the text that lets machines understand them.

## Explaining why a category scored low

- Point to the checks that failed or warned in that category, by label, and translate each into plain language: what is missing and why an AI engine cares.
- Some checks are shown but not scored. A check marked beta, or one marked not scored with a reason, did not move the score; say so instead of treating it as a problem.
- If the report says the page type was not confirmed, the checks that depend on page type were not scored. The user can ask for the analysis again with the right page type.
- Content checks adapt to the page: a homepage is not penalised for lacking an author or publication date.

## Keep it honest

- The report covers the homepage and discovery files only. A low score there does not mean every page is weak.
- A high score improves the odds of being understood and cited. It does not guarantee AI visibility.
- Offer next steps: draft the top fixes (draft-fixes skill) or compare with competitors (competitor-benchmark skill).
