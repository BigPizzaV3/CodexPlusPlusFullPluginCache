---
name: check-citation-or-quote
description: Read the regulator's text for a mortgage citation the user already has, or check whether a quoted passage really appears in Fannie Mae, Freddie Mac, FHA, VA, USDA, Ginnie Mae, SBA or CFPB text. Use when a user names a specific citation to read or confirm (for example B3-4.3-04, 4000.1 II.A.4.c, Freddie Mac Guide 5306.1, M26-7 Chapter 4, HB-1-3555 11.3, 12 CFR 1026.43, 38 U.S.C. 3709) or pastes a passage, policy excerpt or AI-generated quote and asks whether it is accurate, current or verbatim.
---

# Check a citation or quote

Two jobs: read back a citation the user has, or verify a passage against the source.

## A citation to read or confirm
1. Call `lookup_citation` with the citation as the user wrote it.
2. On `ambiguous`, ask the user which document they mean; do not guess. On `not_found`, say the citation is not in the corpus and show what was parsed.
3. Read the section with `get_obligation` (page until `next_offset` is null) or, for a narrow question, `find_in_section`.
4. Quote it verbatim with its `canonical_citation`, link `page_url`, and state any `currency` warning: two versions in force, superseded, pending revision, or changed by a later letter.

## A passage to verify
1. Call `verify_quote` with the passage, and the `register_id` if the user named the source.
2. Report the outcome plainly:
   - exact or normalized: it appears in the source; give the citation.
   - composed: it stitches together text from different places; list the `omissions`. A dropped word such as "not" can reverse the meaning.
   - not_found: it is not a quotation of the regulator's text.
   - superseded: it matches only a prior version; show the current text.
   - update-18-optional: it matches the FHA Update 18 version; say so.
   - rescinded: it matches text that is no longer in effect.
3. When the passage is wrong or outdated, quote the correct current text with its citation.

## Output
- Verbatim quotes with citations, then a summary labeled "Summary". Mention the research-only `notice` once per conversation.
- The user's own document text stays in the chat: only the passage being checked is sent to the tool.

## Do not
- Do not call a passage accurate without a `verify_quote` result.
- Explicit user instructions take priority over this skill.
