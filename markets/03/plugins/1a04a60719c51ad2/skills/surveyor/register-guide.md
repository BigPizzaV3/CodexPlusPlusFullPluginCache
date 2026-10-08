# Register guide — concrete examples and rewrites

**When to read this:** before shipping any response. SKILL.md states the register rules in summary form; this file is the detailed reference with Good/Bad example pairs, the tool-name and engineering-term translation lists, and the two register-slip blocks. Use it to spot-check your draft answer, research log, and pre-tool narration before sending.

The plain-language watch-list itself lives in SKILL.md so it's always available. Read this file when you want concrete contrasts to verify your rewrites land in the right register.

---

## Internal labels — concrete Good/Bad pairs

(Rule: use plain-language term first; internal label in parentheses only when it adds audit value — honest-gap disclosures, error reporting, or disambiguation between specific API-level identifiers. SKILL.md has the rule statement; this section has the contrasts.)

- Good: *"Texas regulations (the law_key `TX-RR` in the API) returned no search results."* — honest-gap disclosure; naming the identifier helps audit
- Good: *"Searched Texas statutes for 'workers compensation': top results in the Insurance Code and Labor Code."* — successful lookup; plain-language form alone
- Good: *"Searched the New York Workers' Compensation Law compilation (`wkc` in the API)."* — disambiguates a specialty compilation that's easy to confuse with the broader NY-STAT
- Bad: *"Identified the law: Texas statutes (the law_key `TX-STAT` in the API); Chapter 406 lives in the Labor Code compilation."* — routine successful identification; the parenthetical adds noise without audit value. Drop the annotation: *"Identified the law: Texas statutes; Chapter 406 lives in the Labor Code."*
- Bad: *"Searched TX-STAT for 'workers compensation': top results returned."*
- Bad: *"TX-RR's index is unfilled."*
- Bad: *"the broken TX- law-key entry"* — pairs "law-key" with a bare internal code; rewrite as "the malformed Texas directory entry (the `TX-` key the API exposes)".
- Bad: *"compilation wkc, Article 2"* — bare compilation code; rewrite as "the Workers' Compensation Law compilation in New York statutes, Article 2".

---

## Raw division paths — concrete Good/Bad pairs

(Rule: never surface dot-separated internal path strings; translate to the human-readable hierarchy.)

- Good: *"Section 512 lives in Labor Code Division 2 (Employment Regulation), Part 2 (Working Hours), Chapter 1 (General)."*
- Bad: *"Section 512 lives at compilation_lab.division_2.part_2.chapter_1."* — raw path; rewrite as the Good form above.
- Bad: *"Drilled into compilation_la.title_5.subtitle_a.chapter_406."* — same shape in a research log; rewrite as *"Drilled into Chapter 406 of Title 5 of the Texas Labor Code."*

---

## Tool names and field names — translation table

(Rule: replace with verbs and phrases that describe what happened, not what was called.)

- `search_codified_law` → "searched" or "searched [the body of law]"
- `search_codified_law_balanced` → "searched across statutes and regulations"
- `resolve_citation` → "looked up by citation" or "retrieved the section"
- `get_division_by_path` → "retrieved the section" (by structural path rather than citation)
- `display_ancestors` → "the section's place in the structure" or "the citation hierarchy"
- `list_jurisdictions` → "checked OpenLaws's directory of jurisdictions"

---

## Citation provenance links — `openlaws_web_url` rendering

Every Division returned by `resolve_citation`, `get_division_by_path`, `search_codified_law` / `_balanced`, `survey_jurisdictions`, and `expand_hierarchy` carries an `openlaws_web_url` field — a clickable link to the same section on openlaws.us. When you cite a section in the answer or a research-log bullet, wrap your Bluebook citation as a markdown link with `openlaws_web_url` as the target.

(Rule: link the Bluebook cite silently. Don't narrate the URL; don't mention the field name; don't fabricate.)

- Good: *"[Tex. Lab. Code § 406.033](https://static.openlaws.us/...) requires the carrier to..."* — strict Bluebook citation as the link text; URL as the target. The reader sees a clickable cite; the prose stays clean.
- Good (research-log bullet): *"Looked up [Tex. Lab. Code § 406.033](https://static.openlaws.us/...) by citation: returned successfully."* — same pattern in a log bullet.
- Bad: *"Tex. Lab. Code § 406.033 — you can verify at https://openlaws.us/..."* — narrating the URL is noise; the link earns its place by being clickable, not by being announced.
- Bad: *"Source: openlaws.us — Tex. Lab. Code § 406.033"* — `Source:` footers are narration in a different shape. Inline the markdown link on the cite itself.

**Fallback:** if `openlaws_web_url` is missing or empty for a record, render the bare Bluebook citation without a link. Never fabricate a URL.

**Why this matters:** the link is provenance. A skeptical reader can click and verify against the actual statute page without leaving Claude. This is the trust-floor analogue to the refusal floor — the answer earns its claim to ground-truth by being one click from the source.

**First-occurrence-only linking — concrete Good/Bad pairs**

(Rule: link the first mention of an authority; later short-form references to the same authority may stay unlinked. An authority mentioned only once must still be linked.)

- Good: *"[29 U.S.C. § 2619](https://static.openlaws.us/...) requires... Section 2619 also provides..."* — first mention linked, the repeated short-form reference bare.
- Good: *"Failure to comply may violate [29 C.F.R. § 825.300(e)](https://static.openlaws.us/...); § 825.300(e) further permits..."* — same pattern with a pincite.
- Bad: *"[29 U.S.C. § 2619](...) requires... [29 U.S.C. § 2619](...) also provides..."* — relinking the same authority on every mention is visual noise, not extra rigor.
- Bad: an authority that appears exactly once, left bare — the one-occurrence rule has no brevity exception.

**Tables are not exempt — concrete Good/Bad pairs**

(Rule: a table identifying a controlling authority needs a linked authority cell of its own; a linked list elsewhere in the answer does not cover the table.)

- Good: a table with a dedicated `Authority` column, each cell a link — e.g. `| Eligibility notice | [29 C.F.R. § 825.300(b)](https://static.openlaws.us/...) |`.
- Bad: the same table with a bare `29 C.F.R. § 825.300(b)` cell, even when the answer's prose links the same citation elsewhere — the table is its own provenance surface and must carry its own link.
- Not required: linking every citation mentioned inside a dense explanatory table cell — a dedicated linked authority column/cell is the target, not exhaustive in-cell linking.

**Fallback preserves links — concrete Good/Bad pairs**

(Rule: falling back from the rendered widget to the plain-text `Research log:` form changes presentation only — it must carry the same citation links, not a stripped-down summary.)

- Good (fallback bullet): *"Retrieved [29 U.S.C. § 2619](https://static.openlaws.us/...): exact section match."*
- Bad (fallback bullet): *"Retrieved 29 U.S.C. § 2619: exact section match."* — the link silently dropped in the transition from widget to plain text; this is a content loss, not a formatting choice.

---

## Publisher parenthetical — `(OpenLaws)` — concrete Good/Bad pairs

Immediately after the citation link, append `(OpenLaws)` — the Bluebook's own commercial-database convention, the same shape as a West or Lexis parenthetical. This retires the old ad hoc `[OpenLaws] <jurisdiction> <law type>` bracketed template; the freshness/coverage label (jurisdiction + law type + lifecycle fields) still follows, just without the redundant `[OpenLaws]` prefix — `(OpenLaws)` already establishes the source.

(Rule: `(OpenLaws)` sits right after the citation link, before the em-dash and the coverage label. One parenthetical per cite, not one per group.)

- Good: *"California requires a written program under [Cal. Code Regs. tit. 8, § 3203](https://static.openlaws.us/...) (OpenLaws) — California regulation."* — link, then publisher parenthetical, then plain coverage label.
- Good: *"Under [Tex. Lab. Code § 411.103](https://openlaws.us/...) (OpenLaws) — Texas statute · in force since 1993-09-01, ..."* — lifecycle field still appends to the label, unchanged.
- Bad: *"[Cal. Code Regs. tit. 8, § 3203](https://static.openlaws.us/...) — [OpenLaws] California regulation."* — the retired bracketed form; `[OpenLaws]` no longer belongs inside the trailing label.
- Bad: *"[Cal. Code Regs. tit. 8, § 3203](...), [Cal. Code Regs. tit. 8, § 3204](...), and [Cal. Code Regs. tit. 8, § 3205](...) (OpenLaws) — California regulation, each."* — one shared parenthetical/label for a group of cites; each cite gets its own.
- Bad: *"[Cal. Code Regs. tit. 8, § 3203](https://static.openlaws.us/...) — California regulation."* — dropped the `(OpenLaws)` parenthetical entirely.

---

## Engineering / search-system terms — translation table

(Rule: don't surface these; describe what they do in plain language.)

- envelope, lean result, chunking → describe the content directly
- BM25, Vespa → don't surface; just describe the search behavior
- corpus → "body of law" or just name the law (Texas statutes, Texas regulations)
- ancestors, path-based → "the section's place in the structure" / "by structure"

---

## Register slip: log bullets that narrate API or search-system behavior

Bullets describing what a search did, what the API returned, or why a result looks the way it does are the most common slip points — the local pressure to describe implementation precisely overrides the register rule. Rewrite these to describe the user-visible behavior, not the implementation. Concrete contrasts:

- Good: *"Top search hits were ancillary procedural provisions, not the controlling rule — expected on a broad query."*
- Bad: *"Top BM25 hits were ancillary procedural provisions — expected behavior for BM25 on a broad query."*
- Good: *"OpenLaws didn't recognize any Bluebook form I tried for New York Workers' Compensation Law citations."*
- Bad: *"Every Bluebook variant rejected in OpenLaws's citation parser."*
- Good: *"Case law isn't covered by OpenLaws."*
- Bad: *"Case law isn't in the corpus."*
- Good: *"Retrying with phrase matching to work around the apostrophe issue in the title."*
- Bad: *"Retrying with phrase mode given the apostrophe tokenization gap."* — `phrase mode`, `tokenization` describe the search system's mechanism; describe what you're doing, not what the engine is doing. The same applies to plan-narration shapes like *"using default mode"*, *"BM25 ranker matched"*, *"compilation-scoped search"* — rewrite as *"using the default search"*, *"the search matched the chapter titles"*, *"searching within the law"*.

---

## Register slip: log bullets that describe the tool's mechanism instead of the research action

When narrating what you did, describe the *research move* ("looked up", "drilled into", "checked for", "navigated to") — not the *tool's internal shape* ("expanded the hierarchy", "ran a hierarchy expansion", "fired a hierarchy expansion"). The tool exists to support the research move; the log should narrate the move, not the tool's mechanics. Especially watch words like *hierarchy*, *expansion*, *subtree*, *tree*, *descendants*, *structural drill-down*, *database-backed*, *the hierarchy tool* when they appear as the subject or verb of a log bullet — they're describing the tool, not the work. Concrete contrasts:

- Good: *"Drilled into each of the eight subchapters in parallel to surface their sections."*
- Bad: *"Fired eight parallel hierarchy expansions, one per subchapter."*
- Good: *"Checked directly whether Title 99 exists under Texas regulations."*
- Bad: *"Tested for existence directly via the hierarchy tool."*
- Good: *"Looked up Chapter 110 to see what's directly inside."*
- Bad: *"Ran a hierarchy expansion on Chapter 110."*
- Good: *"Reused the Chapter 406 section list from earlier in this conversation; no re-fetch needed."*
- Bad: *"Reused the Chapter 406 section list rather than re-firing 8 hierarchy lookups."* — same rule applies in negation/avoidance constructions: describe what you did (or didn't need to do), not the tool's mechanism for what you avoided.
