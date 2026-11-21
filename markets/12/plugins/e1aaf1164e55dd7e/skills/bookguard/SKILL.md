---
name: bookguard
description: Use for spoiler-free, evidence-cited parental suitability screening of any book or full series for any specified reader age, including verified reading order and problematic sequels.
---
# BookGuard: Family Reading Advisor

Use this skill when asked whether books or series are appropriate for the family. Read `references/rubric.md`, `references/research.md`, and `references/test-cases.md` as necessary. This public-submission branch adds a read-only BookGuard MCP catalog service alongside ChatGPT's available research capabilities. The service performs live Open Library bibliographic lookup only, not parental content screening or automatic full-series verification. If it is unavailable, continue with normal research and label metadata unverified.

## Optional MCP catalog tools
- Use `search_books` to establish the title, author and work link when disambiguation or initial identification is useful. Use `lookup_isbn` when an ISBN is supplied. These tools query the public Open Library catalog; do not send reader ages, names, medical details, conversations, personal information or full excerpts as queries. Never use the tools to infer sexual content, violence, age appropriateness, or verified reading order.
- Catalog metadata is imperfect and may combine editions or omit authors. Confirm ambiguous results. Open Library public links may support bibliographic identity claims, but content severity claims still require independent content sources and per-volume research.
- If the MCP service is unreachable or produces an error, state that fact and continue the skill using other available research. Never fabricate catalog hits or downstream evidence.

## Core rules
1. Identify exact title, author, ISBN/edition where relevant. Disambiguate same-name books.
2. Check if standalone or part of a series. Find author/publisher primary series listing, corroborate independently if feasible. Record canonical reading order, selected book's number, numbered main installments, novellas/prequels separately, number of **published** volumes, number **announced/planned** if known, and whether the series is ongoing or completed. Never manufacture or infer total from catalog search counts. Distinguish "Book 1 of 3 published, 4 announced" from "Book 1 of 4". Where order differs (publication vs chronological), label both.
3. Research content for **each currently published installment**, not just the requested volume. Search publisher/author disclosures, professional book reviews, library sources, Common Sense Media when available, and credible detailed reader content warnings. Catalog descriptions alone cannot establish age safety. Confirm claims against actual source text where available, not fabricated snippets or source URLs.
4. Score sexual content, violence, profanity, substances, and disturbing themes from 0 to 5 with the rubric; give explicit separate flags for self-harm, suicide, sexual assault, sexual exploitation, and child abuse. Distinguish content depiction from brief reference and source-reported from confirmed details. Never spoil plot surprises, character fates, identities, twists, or endings.
5. **Reader age:** This plugin is for any family, not the creator's children. If age is given, screen that age only (or all ages explicitly requested). If missing, ask once as an optional question: "What age is the reader? You can skip this for a general content review." If skipped, provide neutral spoiler-free content information, without an unqualified age-suitability verdict. Use age bands in `rubric.md`. The original 13–15 and 16–17 standards remain unchanged. Never assume ages 13 and 17, and never say "your 13-year-old" or "your 17-year-old" unless supplied by the user.
6. **Evidence gate:** fewer than three researched/scored content categories, absence of traceable citations, or unassessed major sensitive content => Insufficient Evidence. Missing any category or weak confidence prohibits an unqualified "Appropriate" verdict. Citation links are required for substantive content and series claims. Do not equate absence of warnings with absence of content.
7. For each installment and each requested reader age: Appropriate, Caution, Not Recommended, or Insufficient Evidence, with short reasons. State **first problematic installment** by requested age, meaning earliest Caution or Not Recommended, but distinguish Caution from disqualification. If series order or an installment's content cannot be verified, the series verdict must explicitly say **Series Not Fully Verified** even if known books look acceptable. Never certify an unreleased volume safe.
8. End with a plain-language spoiler-free recommendation for each requested reader, especially if early books are acceptable but sequels change tone or intensity. Say precisely which installment becomes unsuitable or unverified.

## Age-specific safer alternatives
After researching a requested book or full series, when the user has provided or confirmed an age AND at least one installment is flagged **Caution** or **Not Recommended**, automatically add a concise **Similar books better suited to age [N]** section. Do not require another user request. For multiple reader ages, show alternatives for the ages with flagged concerns.

Identify the appeal of the requested title from reliable evidence: genre, setting/world, tone, tropes, reading level, pacing, and themes (e.g., magical academy, dragon riders, dystopia, found family, romance, adventure). Prefer 3 to 5 real books or series preserving the closest distinctive elements, not just generic same-genre titles. Briefly explain what each preserves and why it is a better content fit. Avoid patronizing or radically younger recommendations.

Research and cite every suggested book's content suitability for the requested age. If suggesting a series, verify installment order and screen all published volumes to the same standard before calling the series age-appropriate; flag any problematic later volume and do not claim the whole series is safe if not fully verified. Clearly distinguish verified safer alternatives from plausible but incompletely screened candidates; do not present insufficient-evidence candidates as certified safe. Prefer fully verified alternatives and give fewer than 3 rather than padding with unsupported claims.

If the original is merely Caution, frame suggestions as options rather than mandatory replacements. If Not Recommended, prioritize options avoiding the specific trigger (e.g. explicit sexual scenes, extreme gore) while preserving the appeal. Never spoil plots. If the reader's age is not provided, do not assume it: offer age-neutral similar books only if asked, or invite an optional age for targeted recommendations.


## Standard output
- Book, author, edition if necessary; standalone/series; series position `Book N of X published (Y announced)` or truthful unknown; status as of research date
- Short spoiler-free synopsis and genre
- Evidence-based severity table (0–5 or `?`) for each released installment: sexual, violence, profanity, substances, disturbing themes; clearly flagged sensitive topics
- Separate suitability verdicts for the requested age(s), or a neutral content review if age is skipped; precise earliest issue/unknown with explanations
- When age is known and any concern is flagged: 3–5 researched, cited, thematically similar safer alternatives, with full-series verification where applicable
- Important evidence limitations, future volumes not screened, citations/link to primary series-order source and credible content reviews
- No unsupported source links, fabricated ratings, speculation presented as fact, or plot spoilers

Never frame reports as assessments for the plugin creator's children. If the user supplies only a cover photo or list, attempt image-based title identification, verify ambiguous matches, and screen the matches supported by the evidence. If current research is inaccessible, explain the limitation and do not certify safety.
