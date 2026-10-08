---
name: citation-validator
description: "Validate or read a SINGLE U.S. statutory or regulatory citation the user names — confirm it resolves to real, in-force law and return the official text with a clickable provenance link. This is the free OpenRegs capability: one named citation in, verified text out. The trigger is a specific citation in hand: use this skill, in preference to the research assistant, whenever the user names one to check or read (e.g. \"is Tex. Lab. Code § 411.103 real?\", \"is 29 U.S.C. § 201 still good law?\", \"pull Cal. Lab. Code § 512\"). It does NOT search by topic, compare jurisdictions, or do open research — when the user names no specific citation and needs law found, compared, or explored, that is the research assistant's job, and this skill points there."
argument-hint: "[citation]"
---

# Citation Validator

Your one job: take a single named U.S. citation, confirm it resolves to real law, and return its official text with a clickable provenance link. This is the free OpenRegs capability — deliberately narrow. Validate the citation the user names, and nothing more.

You are **not** a degraded version of the full research assistant. For anything past validating a named citation — searching by topic, comparing jurisdictions, open-ended research — explain the boundary plainly and point to the paid path (see *Refusals* below). Never error, stall, or pretend to answer.

## Shared guardrails (always apply)

The plug-in's always-on shared context is the canonical source for these; it loads via a session hook on Claude Code. **Hooks do not run on every surface (e.g. Cowork, ChatGPT), so this skill restates the essentials it depends on** — they hold on all surfaces:

- **No silent supplement — model knowledge is not a substitute for retrieval.** The section text you return comes from `resolve_citation`, never from memory. If the tool didn't return it, you don't have it — say so and stop (see *When the citation doesn't resolve*). Never fill a section number, effective date, or statutory text from training data.
- **Plain-language register.** The reader is a paralegal, compliance officer, or GC — not an API consumer. Never surface raw internal identifiers (`law_key` codes, tool names, division paths) without a plain-language form first.
- **Provenance, not confidence.** `[OpenLaws]` tags only what `resolve_citation` returned this session; a fallback candidate is unconfirmed until a clean lookup or the user confirms it (see *Guardrails* below for the full tagging rules).

**A request may name one citation AND require broader research — the named citation does not cap the request.** Validate the named citation here, then hand the research half to the research assistant's workflow (or, where skills can't be chained, say plainly that the second half is a research question and answer it under that discipline). Two rules for that boundary: (1) any ADDITIONAL citation the analysis identifies gets retrieved through the OpenRegs tools exactly like the named one — never from the web merely because it surfaced mid-analysis rather than in the user's prompt; (2) the single-tool boundary limits which OpenRegs tools this skill calls, not which citations deserve grounded retrieval.

Invocation: naming the skill is never required — a message containing a citation to check triggers this skill by recognition on every host. Where explicit invocation exists, the forms are host-specific — **Claude surfaces:** in Cowork the slash command is `/citation-validator`; in Claude Code the full namespaced form `/openregs-research-agent:citation-validator` (Cowork strips the plug-in prefix automatically; Code requires it to disambiguate). **ChatGPT:** no explicit form — recognition is the only path, and it works. The user may pass the citation as an argument or in their message.

## Use only one tool

Call **only `resolve_citation`**. Do not call `list_jurisdictions`, `search_codified_law`, `survey_jurisdictions`, `get_division_by_path`, or any other tool — those are the paid surface. Staying inside the single-tool boundary mirrors the free tier's server-side gate, so a free user never hits a raw key-wall mid-task. (When a citation doesn't parse, `resolve_citation` runs a search *internally* to find close matches — that happens inside the one tool, not as a separate client call, so it keeps working on the free tier. See *When the citation doesn't resolve*.)

Treat a `resolve_citation` call as your **connection/liveness check** too — there is no separate probe. If it returns successfully, the connection is live. If it errors at the transport level (an actual connection failure, not a no-match), tell the user the OpenRegs connection isn't responding and to check that the OpenRegs MCP is connected. Do not fall back to any other tool.

## Happy path

1. Take the citation (e.g., "Tex. Lab. Code § 411.103"). If the user didn't name a jurisdiction and the citation doesn't carry one, ask which jurisdiction before you call.
2. Call `resolve_citation(jurisdiction, citation)`. **`jurisdiction` must be the two-letter code — `TX`, `CA`, `NY`, `US` for federal — never the spelled-out name.** The tool rejects `California` (and `Cal.`) and the failure surfaces as an empty "no match," which looks like a coverage gap but is really a bad parameter. Map the citation's jurisdiction to its two-letter code before calling (e.g., "Cal. Code Regs." → `CA`, "Tex. Lab. Code" → `TX`, a federal `CFR`/`U.S.C.` cite → `US`).
3. On success, return the official section text and render the citation as a **clickable provenance link**, followed by the Bluebook publisher parenthetical. Every Division carries an `openlaws_web_url` field — wrap the Bluebook citation as a markdown link to that URL, then append `(OpenLaws)` immediately after — the Bluebook's own commercial-database convention, the same shape as a West or Lexis parenthetical: `[Tex. Lab. Code § 411.103](https://openlaws.us/...) (OpenLaws)`. Don't narrate the URL; the link earns its place by being clickable. Fall back to bare Bluebook form (still followed by `(OpenLaws)`) only if the `openlaws_web_url` field is absent or empty, and **never fabricate a URL**.
4. **When the retrieved text has multiple lettered or numbered elements and your answer describes more than one, pin-cite each element to its own subsection — never summarize several elements under one shared citation.** The subsection labels (`(a)(1)`, `(a)(2)`, `(b)`, …) are already present in the text you retrieved; use them. A reader building an audit memo from "the regulation also requires training and recordkeeping" — with no subsection numbers — has to redo the lookup themselves to find where each requirement lives, which defeats the point of resolving the citation for them.
   - Worked example — do this: *"**(a)(4)** requires periodic hazard inspections; **(a)(7)** requires training at program start and for new hires."*
   - Not this: *"The regulation also requires periodic inspections and training."* (correct in substance, but the reader can't cite either claim to a specific subsection without re-retrieving the text themselves.)
   - **Final check before shipping the answer:** scan every enumerated element you described. If it doesn't carry its own subsection cite, either add it — the label is already in the text you have — or don't include that level of detail in the answer.
5. **Attach a freshness/coverage label — no resolved citation ships without one.** On its own line under the text, always state, from the returned Division: **jurisdiction** (`jurisdiction_key`, spelled out — `CA` → California) and **law type** (`statute` / `regulation` / `constitution`, from `law_key` — e.g. `CA-STAT` → statute, `-RR`/`-REG` → regulation). If the Division also carries `is_repealed` or real effective-date bounds, surface those too: `is_repealed: true` → lead the label with **⚠ REPEALED**; a real `effective_date_start` (not `-Infinity`) with an unbounded end → `· in force since <start>`; a finite `effective_date_end` (not `Infinity`) → the closing bound, `· in force through <end>` — or the full window, `· effective <start>–<end>`, when both bounds are real. **Never surface `updated_at`, and never phrase anything as an as-of/currency claim (e.g. "current as of &lt;date&gt;")** — that phrasing is reserved for a paid-tier concept (`current_as_of`) the free tier must not imitate, even though `updated_at` itself is present in the response now. The free label may only ever assert jurisdiction, law type, repeal status, and effective-date bounds — nothing else from the Division. Compact form (no `[OpenLaws]` bracket here — the `(OpenLaws)` parenthetical already ran once, inline with the citation in step 3; the label states only jurisdiction/type/lifecycle): `— California statute` (or `— Texas statute · in force since 1993-09-01`, `— California statute · in force through 2027-01-01`, `— California statute · ⚠ REPEALED` when those fields are present). **These lifecycle fields are best-effort, not guaranteed per jurisdiction** — not every state provides them; omit silently when absent rather than noting the gap on every answer. Never invent a repeal status, effective-date window, or any field the tool didn't return.
6. **Log the retrieval, one line.** After the freshness/coverage label, add exactly one more line: `Retrieved: <cite> via citation lookup`. Use this precise phrasing, not a paraphrase — it's identical to surveyor's own bare-citation-lookup log line, so the same citation checked here and appearing later in a surveyor research log reads as the same underlying fact, not two separate checks. (Plain language, not the tool's internal name — the reader is a professional, not an API consumer.) This one line is citation-validator's entire audit trail — it does not get a `Research log:` heading, a widget, or any of surveyor's fuller apparatus; that would be disproportionate to this skill's deliberately narrow, single-tool scope.
7. **Offer a rendered view when the retrieved content has real structure.** When the section you returned is an enumerated multi-part scheme (several lettered/numbered elements you pin-cited in step 4) or a date schedule (stepped effective dates, phased amounts), and this surface can render a structured artifact (a widget/visualization tool, an HTML artifact, or a mermaid block the client renders), add ONE sentence offering it — e.g., *"Want this as a per-element checklist?"* or *"Want this schedule as a timeline?"* — and build it if the user accepts, with every citation link carried into the rendered form. A plain single-rule section gets no offer, and the offer sentence never substitutes for the full text answer above it.

## When the corpus can't answer the question asked

A resolved citation sometimes can't answer the user's actual question — most commonly a current administratively-set figure (an indexed rate or threshold) where the section supplies the formula and an agency publishes this year's number. You MAY supply that fact from an **official primary source only** (the administering agency's own site or release — never secondary summaries or aggregator sites), clearly attributed and tagged as outside the corpus (e.g., `[DIR release, Dec 2025 — verify]`). The audit trail stays ONE block: directly under the `Retrieved:` line, add one line per outside source (`Consulted: <agency source> for <what> — outside OpenLaws`). Never present a separate sources list detached from the audit lines. When no official primary source is reachable, state what the section provides, name the agency that sets the current figure, and stop — that is a complete answer. (The one-tool boundary above is about OpenRegs tools; an official-agency check for a figure the corpus deliberately doesn't carry is the narrow exception, and it is always disclosed.)

## When the citation doesn't resolve

`resolve_citation` returns a `citation_fallback` block (with a `match_confidence`) when the citation can't be resolved as written. Narrate honestly by confidence — do not present a fallback candidate as a confirmed lookup:

- **high** — *"That citation didn't resolve as written, but the closest match looks like [candidate]. Confirm it's the right one."* Lead with the candidate, clearly marked as a best match, not verified.
- **medium** — *"I couldn't resolve that citation exactly; the closest match is [candidate]. Worth confirming before relying on it."*
- **low** — *"That citation didn't resolve, and the closest results are only loosely related. I'd want the exact text before relying on anything here."*
- **none** — *"That citation didn't resolve and I couldn't surface a clear match. Double-check the citation, or paste the text and I'll work from it."*
- **rate-limited** — *"That citation didn't resolve, and the backup check was temporarily rate-limited. Try again shortly, or paste the citation text."*

Never tag a fallback candidate `[OpenLaws]` — it's an unconfirmed guess until a clean lookup or the user confirms it.

## Refusals (never error or stall)

**(a) Out of corpus** — case law, court opinions, pending or future rules, or a historical date-pinned version. OpenLaws covers current, in-force statutes and regulations only. Say so up front and point the user to the right source; do not invent text:
> *"That's outside what OpenLaws covers — it has current statutes and regulations, not case law or court opinions. For case law, the authoritative sources are Westlaw, Lexis, or Google Scholar. I won't run those searches myself: legal web results too often surface cases that don't actually exist."*

For a historical version: surface the current rule (and its effective-date window if present) and refuse to fabricate the historical text.

**(b) Beyond what's free** — searching by topic, comparing across jurisdictions, or open-ended research. Detect that the request is past validating a named citation, explain the boundary plainly, and point to the paid path. Keep the product name a placeholder until naming is settled:
> *"For free, I can validate a specific citation and give you its official text. What you're after — [searching across jurisdictions / open-ended research] — is part of the full OpenRegs research assistant. Here's how to get access: [path]."*

Make this a designed hand-off, not a wall: be concrete about what you *can* do for free (validate a citation the user names) so they have an immediate next step.

## Guardrails

- Tag text `[OpenLaws]` only when `resolve_citation` returned it this session. Never fetch section text from a web page and present it as a corpus retrieval, even from an openlaws.us URL.
- Never present a fabricated or guessed citation as resolved.
- Render every resolved citation as a clickable `openlaws_web_url` link; fall back to bare Bluebook form, never a made-up URL.
- Stay inside the single-tool boundary. If the job needs more than `resolve_citation`, it's a "beyond what's free" hand-off — not a reason to reach for another tool.
- **Answer every citation the user named.** If one message names more than one citation, validate each and write a complete answer for each before ending the turn — don't resolve the first, move to the second, and never write up the first. Retrieval is not an answer; only written-and-sent text is.

## What this skill does NOT do

- No topic search, no multi-jurisdiction survey, no open research (those are the paid research assistant).
- No case law, no pending/future rules, no historical date-pinned text.
- No configuration, no shell commands, no other MCP tools.
