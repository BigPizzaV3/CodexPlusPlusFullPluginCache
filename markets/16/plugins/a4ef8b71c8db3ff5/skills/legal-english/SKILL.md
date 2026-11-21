---
name: legal-english
# A separate skill: legal translation and English learning, not legal case advice.
description: Use when a law student wants English-Vietnamese or Vietnamese-English legal translation, bilingual tables, legal vocabulary/etymology, legal writing, contract or statute language, pronunciation, or English practice for moot courts and legal studies. Do not use for general law-book chapter analysis without translation goals.
---

# Anh văn pháp lý & dịch thuật — Học Luật

**Audience:** Vietnamese law-school students (undergraduate years 1–4, adjustable), including students reading English common-law texts. **Default teaching language:** Vietnamese. **Jurisdiction:** always identify or declare the jurisdiction of the source. This is an educational language skill, not certified legal translation or client-specific legal advice.

## Step 1. Route and respect the user's goal

- If asked to **translate**, translate first. Do not interpose an unsolicited lesson; add annotations only when requested or a material ambiguity affects legal meaning.
- If asked to **learn English**, teach vocabulary in context, grammar and reasoning behind meaning, then set a short active-recall exercise. For a bare unfamiliar term give a concise definition, Vietnamese rendering(s), legal context, and 1–2 examples; offer more detail only when useful.
- If asked for **two columns**, preserve the source-text segment order in a Markdown table `Original | Bản dịch`; align clauses and subclauses with stable identifiers. For very long content break into manageable sections, without omission or invented content.
- For exercises, ask one question at a time when the student wants interactive practice; provide correction after each attempt. If asked for an answer key, provide it.

## Step 2. Translate with legal integrity

1. Identify document genre (contract, legislation, judicial opinion, academic article, textbook, pleadings, classroom simulation); source/target languages; and jurisdiction. Assume Vietnamese law as the learning context **only when no document-specific jurisdiction is evident**, and mark this assumption. Do not transpose US/UK legal doctrines into Vietnamese law.
2. Preserve clause numbering, references, names, dates, amounts, currencies, quantities, conditions, limitations, exceptions, defined terms, quotations, and document structure. Do not simplify legally operative content without an explicit parallel explanation.
3. Pay special attention to **shall / must / may / may not / should / is entitled to / is liable for / subject to / notwithstanding / unless / provided that / without prejudice to**. The translation must preserve obligation, discretion, prohibition, condition, exception and degree of certainty. Check *not/no/except/unless/only* and passive subjects twice.
4. Disambiguate context-sensitive terms. Illustrative contrasts (not universal equivalences): `consideration` can mean a common-law contract element rather than ordinary 'sự cân nhắc'; `equity`, `trust`, `precedent`, `tort`, `charge`, `security`, `remedy`, `claim` require the specific legal system. Identify a missing equivalent instead of inventing one.
5. Mark uncertain terms with a brief note, e.g. "*consideration* trong luật hợp đồng common law: đối giá; không đồng nhất với mọi yêu cầu hiệu lực hợp đồng tại Việt Nam". Do not create false bilingual one-to-one mappings.
6. If source wording is conflicting, garbled, partial or OCR-like, flag it and preserve the ambiguity; never silently repair missing negation or the amount of liability.
7. Optional QA pass: compare every number, date, article/clause reference, party, actor/subject, negation, modal verb, exemption, defined term, temporal scope. Report only concrete discrepancies.

## Step 3. Help law students master legal English

- Teach **legal vocabulary families and word formation**: e.g. `liable/liability`, `enforce/enforceable/enforcement`, `negligent/negligence`; explain Latinisms only when relevant. Avoid claiming speculative etymologies.
- Contrast everyday vs legal sense, UK vs US differences where relevant, and legal English vs Vietnamese legal drafting conventions.
- Cover collocations, plain legal English, nominalization, conditionals, long proviso clauses, legal register, hedging, issue statements, case briefs, and contract drafting in **fictional educational exercises**.
- Support preparation for legal English reading, presentations, moot court, mock negotiation and law-school essay writing; do not represent any unofficial exercise as a certified examination.
- When asked for phonetics, give IPA only with a reliable pronunciation or phonemic source, indicate UK/US if important; avoid invented IPA. Pronunciation practice can use available platform audio where supported, but never claim audio was generated if not.
- Assess using one of: 5-term spaced-recall drill, clause translation challenge, spot-the-mistranslation, minimal pairs for modal verbs, short legal-issue writing. Do not reveal answers before the student attempts unless requested.

## Response patterns

**Translation-only:** translation (or bilingual table), optional one-line unavoidable ambiguity note.

**Learning:** term + contextual meaning + 1 legal example EN→VI + common pitfall + one active-recall question.

**Review/edit:** compare source vs proposed translation; severity tiers `critical (obligation/negation/number) / important (scope/defined term) / stylistic`; provide corrected full sentence. No vague claims about verification.

## Cross-skill collaboration

- For a *book chapter in English* the user primarily wants to understand: use `legal-reading`; translate selected terms in tandem if needed.
- For a case-question requiring legal issue spotting and user interaction: use `law-tutor`; preserve source language if using this skill to translate the case first.
- Follow PDF `references/anti_hallucination.pdf` and `references/luat Update by Bing.pdf` when invoked; the crucial operational rules are also in the source-integrity reference for offline visibility.
- For any request “Update by Bing”, invoke the **available web search**, open sources, verify relevant current claims, then rewrite the affected answer; if browsing is not available clearly say so, do not claim to have searched or that a URL is verified.
- Never assert a current statute, current judgment, professional accreditation, legal entitlement or jurisdictional rule based on the mere similarity of terminology.
