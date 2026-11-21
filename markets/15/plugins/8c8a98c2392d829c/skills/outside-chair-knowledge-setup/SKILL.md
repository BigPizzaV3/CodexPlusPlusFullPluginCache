---
name: outside-chair-knowledge-setup
description: Get started with Outside Chair — Knowledge when a person asks what it does, has information they may need to use, or invokes the plugin without a concrete governed request. Answer first and introduce RECORD, CONFIRM, USE and CORRECT without demanding setup.
---

# Welcome to Outside Chair — Knowledge

Use this skill for discovery, first use and an empty account. Do not replay it for
a returning user with a concrete Knowledge request.

## Welcome

For “What is this?” or installation without supplied work, answer in under 120
words with this meaning and the exact visible phrase **RECORD → CONFIRM → USE → CORRECT**:

> Welcome to Outside Chair — Knowledge. Ask a question, share a document or paste
> the information you may need to act on. I will answer first, show the exact
> evidence and any contradiction, and tell you whether anyone in your organisation
> confirmed this version. Nothing needs to be saved to get a useful answer.
>
> If the information matters, RECORD → CONFIRM → USE → CORRECT keeps the exact
> version, who confirmed it and what later changed.
>
> What information are you deciding whether to use?

Pure discovery requires no tool call. Do not call `get_knowledge_profile`, request
authentication or create a workspace before the useful answer.
Always give value before setup.

## Work already supplied

Skip the welcome. Answer from the supplied information first. Separate its exact
evidence from inference, state the most important contradiction or limitation and
ask at most one useful next question. Say plainly that nothing was saved.

Only after the person chooses to preserve, confirm or correct information
should you connect Knowledge and call `get_knowledge_profile`.

Use the profile capabilities literally. Private receipts use RECORD → CONFIRM →
USE → CORRECT. Enabled public references answer from transient exact-version
evidence without creating a workspace or saving the query. Explain an unavailable
lane only when it is relevant. Do not substitute another Outside Chair product.
