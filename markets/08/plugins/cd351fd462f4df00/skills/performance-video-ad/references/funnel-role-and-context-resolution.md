# Funnel role and context resolution

Use this gate after offer sources and the live destination are available, before Creative Context, Hook writing, or Body design.

## Keep the boundary

The Skill owns the method: which facts are required, where to retrieve them, when to ask, how much message a stage may carry, and when to stop. It does not store a company's current strategy, pretend conversation memory is canonical, or invent an offer's funnel.

Resolve information in this order:

1. the current user request and any source the user marks canonical;
2. approved offer-specific decisions;
3. the current offer destination and product specification;
4. offer-specific research, sales calls, and VOC;
5. MyMarketer strategy when available;
6. attributable conversation memory, after checking that it is still current;
7. general method only for non-blocking defaults.

Do not ask for a fact that can be retrieved safely. Do not use a global strategy for a different offer to fill an offer-specific field. Conversation memory can support a value but cannot become canonical by itself.

## Ask only when the decision changes

Create `context-resolution.json`. A blocking field is `resolved` only when an authoritative source or the user confirms it. General inference cannot resolve a blocking field.

If a blocking field remains missing, conflicting, or low-confidence after retrieval:

- set the record to `NEEDS_USER_INPUT`;
- combine related fields into one question;
- ask one to three short questions;
- state what creative decision each answer changes;
- stop before Creative Context, Hook, Body, or Animatic work.

Do not ask about low-impact taste when a reversible default is safe. Record that default on the non-blocking field instead.

## Assign one job to the ad

Create `funnel-role-contract.json`. Separate what the current ad must accomplish from what the next destination must explain.

For a cold click-through ad whose next LP carries full persuasion, default to qualified curiosity:

- make the right viewer recognize the problem;
- create one honest and relevant open question;
- name the offer category or intervention enough to make the click intelligible;
- earn a qualified click;
- leave mechanism detail, objections, deliverables, pricing, and contract persuasion to the LP.

Use five core message roles: Pain, tension, surprising reframe, product category, and CTA. Allow at most one mechanism step and one proof item. These are stage defaults, not a universal 15-second law. Duration follows the resolved role, cognitive load, and placement.

A retargeting explainer, proof ad, or direct-response ad may carry more explanation when its audience, destination, and evidence justify it. Never apply the cold-click budget to every ad.

## Preserve qualified curiosity

Record:

- the question the ad creates;
- what the ad answers;
- what it intentionally leaves for the destination;
- how the destination's opening resolves or deepens that question;
- primary stage metrics and downstream guardrails.

Raw CTR is not the outcome. For cold click-through work, evaluate qualified outbound CTR and landing-page view rate first, then guard against worse LP engagement, consultation conversion, or qualified-lead rate.

The ad must not become a miniature LP, but it must also not become empty clickbait. It should create a correct expectation that the destination can fulfill.
