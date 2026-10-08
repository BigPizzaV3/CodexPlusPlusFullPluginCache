---
name: what-next
description: Recommend the single best next step for the user's family in SAMRUM: take the test, invite someone, a report, or a focus track. Use when the user asks what to do now, which focus track fits, what report makes sense, or asks for a recommendation for one or two named people ("hvad skal vi gøre nu", "hvilket fokusspor passer os", "what should we do next", "what would you pick", "vad ska vi göra nu", "was sollen wir als Nächstes tun"). Do not use for explaining existing reports or tracks (use explain-report or focus-track-checkin).
---

Use this skill when the user asks for direction. Server-side recommendations are the source of truth; you pick one and explain it. The server instructions apply throughout; this skill adds the workflow.

## Steps

1. Call `get_family_overview` with `includeRecommendations: true`. Without it the result has structure only and no recommendations.
2. Read `availableNextSteps` and any `trackOptions` inside them. These are computed from family composition, completed tests and existing reports.
3. Pick exactly one recommendation:
   - If the user named one or two people, choose the step that matches them. Two names together is one pair request; do not split it into two personal recommendations unless the user asks for one per person.
   - If the user is an adult and names two other family members, treat it as a proxy pair request.
   - Otherwise choose the step that unlocks the most: usually a missing test before any report, and a report before a focus track.
4. Explain it in one short paragraph: what it is, what it would show for these people, and the item's own `link` from the result.
5. Offer one alternative only if the user asks for options.

## Output

- 2 to 3 short paragraphs, maximum 150 words, in the user's language.
- Name the people (nicknames) and the product. Be concrete.
- One recommendation, one link, one reason.

## Special cases

- No family or no completed test yet: this is activation, not an error. Say the connection works and that SAMRUM needs a family profile with at least one completed test before it can use personal data here. Give one next step: create the family profile and take the test. Do not mention reports or tracks yet.
- A named person has not completed the test: say so, give the test link, and stop there.
- Describe what a step gives the family, not what it costs. Do not quote prices, and do not offer to buy or start anything for the user; the link opens SAMRUM, where the user decides.
- The user already has an active track: consider whether the better next step is to continue it (hand over to focus-track-checkin) rather than starting something new.
- The user mentions an argument that just happened: switch to right-now-conflict first.

## Do not

- Invent focus track names, categories, report types, prices or links that are not in the result.
- Build a recommendation from profile or report interpretation when `availableNextSteps` is present.
- List everything that is available. One recommendation.
- Imply bad outcomes if the user does not follow the recommendation.
- Call `get_family_overview` with recommendations again in the same conversation unless the family structure changed or the user asks again what to do next.
