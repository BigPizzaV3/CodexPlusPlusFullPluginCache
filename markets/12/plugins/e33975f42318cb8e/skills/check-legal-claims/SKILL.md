---
name: check-legal-claims
description: Check the legal claims in a document or text against the official Dutch and EU sources through LexAgent - a decision (besluit), objection (bezwaarschrift), contract, advice memo, letter or draft. Use when the user asks whether a text is legally correct, asks to verify or fact-check its legal statements or references, or asks "klopt dit?".
---

# Checking legal claims with LexAgent

Goal: for every legal claim in the text, a verdict that rests on the official source, so the user can
see at a glance what holds, what does not and what could not be checked.

## 1. List the claims

Go through the text and pick out each **legal claim**: a statement about what a rule says, requires or
allows, a reference to an article, regulation or ruling, a deadline or competence derived from law.
Facts about the case (names, dates, what someone did or plans) are not legal claims; skip them.
Quote each claim exactly as it appears, one sentence or clause at a time.

## 2. Verify each claim

For each claim, read the source that governs it with the LexAgent document tools, following the
`dutch-legal-research` skill: the article itself for the right peildatum, then case law where the
claim depends on interpretation. Check the reference too: an article number that moved or a
regulation that was repealed or replaced is a finding in itself.

Also check what a text must say but does not. For a decision (besluit) of a government body that is
at least:

- **Statement of reasons** (art. 3:46 and 3:47 Awb): the grounds and, where possible, the legal basis.
- **Objection clause** (art. 3:45 Awb): that objection or appeal is possible, the period, and the body
  to send it to. A wrong period is a claim to check; a missing body is an omission to report.

Report an omission as its own row, quoting the passage it should have been part of.

## 3. Give one verdict per claim

Use exactly one of these statuses:

| Status | Meaning |
|---|---|
| **Klopt** | The cited source supports the claim. |
| **Onjuist** | The cited source contradicts it. |
| **Twijfel** | Partly supported, depends on facts not in the text, or rests on a weaker source such as council information. |
| **Niet gevonden** | You searched the sources that should cover it and none supports it. |
| **Niet te controleren** | The governing source is not available through LexAgent (for example an omgevingsplan, or case law that is not in the open data). |

Klopt, Onjuist and Twijfel always carry the citation the document tool returned. Give a one- or
two-sentence explanation per claim in the language of the text, and for Onjuist the correct wording
or reference.

## 4. Report

Present a table (quote, status, explanation, source), followed by a short summary: the claims that
need attention first, then what could not be checked and why. Do not rewrite the user's document
unless asked.
