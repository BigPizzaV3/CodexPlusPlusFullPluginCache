---
name: check-citation-good-law
description: Verify U.S. case, statute, or specialty citations against the LawDiver corpus and report match status plus good-law / treatment signals when available. Use when the user asks if a cite is real, still good law, or overruled. Do not invent treatment signals.
---

# Check citations and good law (LawDiver)

Use LawDiver MCP tools only.

## When to use

- User asks whether a citation is real or in the corpus
- User asks if a case is still good law, overruled, or negatively treated
- User pastes cites to validate before relying on them

## Steps

1. Call `check_citation` with the citation string(s) the user provided.
2. Report match vs no-match clearly. For case hits, include good-law / treatment signals from the tool result when present.
3. If the user wants more on a matched case, call `retrieve_case` and/or `get_good_law` with the `caseId`.
4. For statute/rule or specialty hits that include `authorityKey`, use `retrieve_statute` when the user wants the section text.
5. If nothing matches, say so. Do not substitute a “similar” invented cite.

## Do not

- Invent Shepard’s-style treatment or claim a case is good law without tool support
- Pretend a no-match cite exists in LawDiver
- Delete, edit, or “fix” citations in any database (tools are read-only)
