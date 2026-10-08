# Synthesis — writing the answer

Use after research is complete. About *writing*, not routing or further searches.

## Quality rules
1. **Do not invent** statutes, cases, or propositions — everything cited comes from results.
2. **Check whether older case law still fits the current statute** — revisions sometimes survive, sometimes not.
3. **Stay close to the decisive facts.** Abstract doctrine without facts does not help.
4. **Do not overgeneralize from one case.** One BGer judgment is not a doctrine.
5. **Separate statute text, judicial holding, and application to facts** — collapsing these is the biggest legal-AI error.
6. **Read the Erwägungen, not the Sachverhalt** — never present party allegations as the holding.
7. **State uncertainty explicitly** where law or facts remain open. Honest hedging beats a confident wrong answer.
8. **Note source gaps** — if a tool was unavailable or a point is not covered by the corpus, say so plainly.

## Answer structure
Unless the user asks for something narrower:
1. **Ausgangspunkt** — the question and factual frame
2. **Gesetzliche Grundlagen** — governing statutes, by article reference
3. **Rechtsprechung** — leading judgments and what they hold (Leitentscheid first, then the newest applying judgment)
4. **Materialien** — Botschaft passages where the ratio legis matters (optional)
5. **Entscheidende Kriterien** — what actually decides the case
6. **Sachverhaltsrelevante Umstände** — how the user's facts map onto those criteria
7. **Offene Punkte / Unsicherheiten** — what is genuinely open
8. **Vorläufige Einschätzung** — your provisional take, clearly labeled

Answer in the language of the question; for German use Swiss legal terminology. The user is a Swiss legal professional.

For multi-part exam/mandate answers, use the Antwort-Bauplan in `methodology/exam-answer.md` instead of this generic structure (structure IS substance there — points are awarded per recognized problem element).

## Citation spec
Every source = a clickable inline Markdown link, placed where its content is used. The link is always the `lexplorer_url` field of the tool result (public Lexplorer source page with date/version and a link to the official source):
- Verdict: **cite the BGE form when it exists** (`BGE 140 III 86 E. 2.3`) — that is what exams, Musterlösungen and practitioners expect; a plain docket hit gets checked for a BGE sibling via `get_case_brief` before citing. `[BGE 140 III 86 E. 2.3](<lexplorer_url>)`. Every quote/E.-number/docket/date comes only from `read_chunk`/`read_section` output, never from a preview or memory.
- Federal statute article: `[Art. 336a Abs. 2 OR](<lexplorer_url>)` from `get_article`.
- Cantonal act/article: `[§ 12 PBG ZH](<lexplorer_url>)` from `get_cantonal_law`.
- Botschaft: cite as `Botschaft, BBl <Jahr> <Seite>`; link only if the result carries a URL.
- No `lexplorer_url` → cite by reference without a link. Never invent a URL.

**Verify-gate (mandatory before answering):** run `verify_citations([...])` over every judgment citation in the draft. It flags refs not in the corpus (remove, never keep an unverifiable citation) and returns the canonical Zitierform (BGE form when published) — fix the draft to match.

**Source tiers.** The value to a jurist is in the interpretive sources, not the statute. Tier 1 = Rechtsprechung and Materialien (Botschaften): cite prominently inline and list in the Quellenverzeichnis. Tier 2 = the statute article itself: cite inline; it does **not** appear in the Quellenverzeichnis.

## Quellenverzeichnis
End every answer with a `Quellenverzeichnis` listing **only Tier-1 sources**. One bullet per cited source, each a Markdown link via `lexplorer_url`, format `<identifier> - <3-5 word neutral description>`. Example:
```
- [BGE 132 III 115 - Entschädigung missbräuchliche Kündigung](https://law.lexplorer.ch/s/d/…)
- [4A_123/2024 - Fristbeginn bei Kündigung](https://law.lexplorer.ch/s/d/…)
```
If the answer turned up no Tier-1 source at all, the research is incomplete — go back to `find_leading_cases` / `get_article_case_law` before finalizing, rather than padding the list with statutes.

## Verification
Verifying the finished answer is a **separate, user-triggered pass**. When the user asks to review/verify/check the sources, read `review.md` and run the source-by-source audit there.
