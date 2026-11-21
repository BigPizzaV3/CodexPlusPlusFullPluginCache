---
name: candidate-outreach
description: "Write personalized initial recruiting invitations and follow-ups using verified role and candidate facts, with clear calls to action and respectful stop conditions."
license: MIT
metadata:
  version: "0.2.4"
---

# Candidate outreach

Use for first contact about an opportunity, follow-up, or re-engagement. Use `interview-invitation` once an interview has been agreed.

## Inputs

Gather the approved role brief, candidate evidence, sender identity, channel, relationship history, language/tone, and the desired next action. Check existing replies, opt-outs, and duplicate outreach if available. If history is unavailable, say so before proposing a send or sequence.

## Procedure

1. Identify one specific, job-relevant reason for contact that the evidence supports. Cite that fact in the working notes. Do not imply personal familiarity, knowledge of job-seeking intent, or admiration you cannot substantiate.
2. Explain the role's relevant opportunity using confirmed facts. Include compensation and work arrangement when supplied and useful; do not invent a salary, urgency, exclusivity, or client permission to name the company.
3. Draft a short subject and a concise body. A useful default is 70–130 words, adjusted to the channel and user's request. Lead with relevance, explain the opportunity, and ask for one easy next step.
4. Prefer an interest check for cold contact. Do not demand a CV, application, and booking in the same first message. An existing candidate relationship can justify a more direct request.
5. If follow-ups are requested, make each add information rather than repeat “bumping this.” Propose timing as a draft, check existing sequences, and stop on a reply, opt-out, role closure, or the user's stated limit. Never manufacture a prior conversation or use a false `Re:` subject.
6. Review the draft for factual accuracy, relevance, readability, and pressure. Remove flattery, generic AI phrasing, sensitive personal observations, and unsupported claims.

## Output

Return the subject, ready-to-review body, factual personalization note, unresolved details, and any requested follow-ups. Clearly label draft status. Provide variants only when useful or requested.

## Fictional example

Confirmed inputs: Alex's profile describes building observability for payment services. Northbank is hiring a backend engineer to improve payment reliability; the role is hybrid in London. The sender is Sam, an authorized recruiter.

Subject: Backend reliability role at Northbank

Hi Alex,

Your work on observability for payment services caught my attention. I'm helping Northbank hire a backend engineer to improve reliability across its payments platform, and that experience looks relevant to the work.

The role is hybrid in London, with a focus on incident prevention and service ownership. Would you be open to a short overview so you can decide whether it's worth a conversation?

Best,
Sam

If this isn't relevant, let me know and I won't follow up.

Evidence note: the profile supports observability experience; it does not establish that Alex is job seeking or personally led incident response. Salary is not supplied, so no range is asserted.

## With Vitae

Use live candidate and job read tools to retrieve authorized context. This skill does not itself provide email delivery. If no verified send/draft-save tool is available, return the copy for the recruiter to use in Vitae. Do not call campaign import or workflow execution as an implicit send substitute. Respect previous explicit send authorization, recipient/sender scope, and server approval controls; never claim delivery without a confirming result.

## Completion and handoff

The draft is complete when claims are supported, the next action is clear, and recipient history has been checked or flagged. Record actual reply and send states separately from the copy. A positive response can lead to `interview-invitation` after the recruiter confirms the next stage.
