---
name: icanpreneur-persona-feedback
description: "Get a Buyer Persona's reaction to an offer, price, pitch, message, landing-page copy, feature or idea using the user's saved Icanpreneur research. Use when the user wants to test, pressure-test or get feedback from their buyer persona, compare options, anticipate objections, or improve material using the persona's reaction. Load `icanpreneur` first. Do not use to build a persona (`icanpreneur-build-research`), to generate positioning or pages (`icanpreneur-gtm-assets`), or to answer as a persona yourself."
---

# Ask your Buyer Persona

Put the user's work in front of a persona built from their research and get a reasoned reaction. The persona service writes the answer. Your job is to ask a good question, say how much weight the answer deserves, and help the user act on it. Load [icanpreneur](../icanpreneur/SKILL.md) first; its rules apply.

Done means the user has the persona's reaction, your reading of it, what to test with real customers, and a saved note if they want one. If there is no persona, go to `icanpreneur-build-research`.

## 1. Find the persona

1. Find the workspace (`list_ideas`), then `list_buyer_personas`. Each entry shows name, title, source research, segment and `status`.
2. One persona: use it and say which. Several: ask which, unless the user named one. Offer to ask each if more than one fits.
3. Read `get_buyer_persona`: Complete must also have populated profile content. Pending/Error may retain older or incomplete fields, not a guaranteed selectable historical snapshot. For the build you just triggered, wait for Complete and usable content; stop on Error. For an existing populated profile, disclose its state before an authorized question and stop if it fails. No usable persona: it comes from BuyerPersona research and analyzed interviews.

## 2. Know what it rests on

Once per persona per conversation (free): count the completed interviews in the persona's source research by `synthetic` and `imported`, paged to `totalCount` (procedure: `icanpreneur` → `references/evidence.md`). Keep one line: "The source research currently contains 8 completed interviews: 3 real (1 imported) and 5 synthetic." This is the research now, not proof of what the answering version was built from, so never say "this persona is based on…". A persona answer has no sources field: never invent citations. If everything is synthetic, say so before asking; the answer is a simulated view.

## 3. Ask

- Put the user's supplied text verbatim inside `question`. Include source URLs in `question`; the persona service may retrieve those public webpages. Uploaded attachments use `fileKeys` with usage ChatFile and actual bytes. Do not invent an attachment from a summary.
- **Before writing the question, read [references/question-patterns.md](references/question-patterns.md).** Ask open, specific questions about reaction, hesitation, missing information and what would convince them. No leading questions, no requests for numbers or shares, no "pretend you are".
- Check the credit balance before the first question (each is billable).
- Call `ask_buyer_persona`. Keep the returned `conversationId` for follow-ups. If `usesLatestPersona` is false, say the conversation started at an earlier persona revision and offer a new conversation. This does not establish an immutable historical evidence snapshot. A lost ID means starting a new one.
- To compare options, put them in one question labelled A, B, C (one charge). If the choice matters, offer a second run with the order changed.
- To test a different idea without the earlier conversation influencing it, start a new conversation.
- After an unknown outcome, do not ask again. Tell the user it may have gone through and ask whether to retry. On `INSUFFICIENT_AI_CREDITS`, explain that a positive AI-credit balance is required and stop.
- If the call fails, never answer as the persona yourself.

## 4. Present the answer

Keep three things separate:

1. **The persona's simulated answer**, faithfully, without added claims.
2. **Your reading**: what appeals, what creates doubt, what is missing, where the answer is thin. Mark your inference. Cover first reaction, what creates interest, what causes hesitation, what proof is missing, and what to check next, where the answer speaks to them. If the persona says it lacks evidence, call it directional.
3. **What to test with real customers**: one to three checks phrased as interview questions.

State the evidence line once. If the answer contradicts the user's hopes, say so plainly.

## 5. Improve and save

- Revise the user's text in the conversation when asked or clearly useful, against the platform definitions (`icanpreneur` → `references/definitions.md`). Never add testimonials, customers, metrics or proof you were not given; use a marked placeholder. A revision here is not a positioning document (`icanpreneur-gtm-assets`).
- Offer to run a revised version past the persona and wait for a yes; each question costs credits.
- At a conclusion, offer once to save a note (`create_note`): the direction, persona and version, the evidence line, main objections, what real customers have not yet supported, and next steps ([layout](../icanpreneur/references/team-and-notes.md)). Save only if the user agrees.
