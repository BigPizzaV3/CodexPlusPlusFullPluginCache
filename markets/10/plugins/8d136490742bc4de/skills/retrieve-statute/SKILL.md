---
name: retrieve-statute
description: Retrieve full U.S. statute, regulation, or court-rule section text from LawDiver by Bluebook citation or authority key. Use when the user asks for the text of a code section, regulation, or court rule. Do not use for caselaw search or inventing statutory language.
---

# Retrieve statute / rule text (LawDiver)

Use LawDiver MCP tools only. Never invent statutory wording.

## When to use

- User asks for the text of a statute, regulation, or court rule (e.g. `42 U.S.C. § 1983`)
- User has an `authorityKey` from `check_citation` and wants the section body

## Steps

1. Call `retrieve_statute` with a Bluebook-style citation that includes a section number, or with `authorityKey` from a prior `check_citation` hit.
2. If the citation is incomplete (missing section), ask for the section number before calling.
3. Return the section body and identifying metadata from the tool. If truncated, follow any pagination fields the tool returns.
4. If the lookup fails, say the section was not found in LawDiver. Do not paste a guessed version of the statute.

## Do not

- Fabricate statutory text
- Use this skill for case opinions (use retrieve-opinion)
- Claim LawDiver covers every jurisdiction’s entire code if a lookup misses
