# Ads Structure And Context Playbook

Use this reference when helping a user plan, create, or revise campaign structure, ad-group scope, context hints, ads, or landing-page alignment. It provides advertiser best practices, not permission to broaden a requested write, invent facts, add unrequested fields, or override live tool schemas and safety contracts.

## Choose The Smallest Coherent Structure

Start with the business strategy, then keep each lower layer focused:

- A campaign groups ad groups that share one business strategy: objective, budget pool, geography, schedule or promotional period, campaign type, and any business-unit, regulatory, or compliance boundary.
- An ad group groups ads that share one coherent product, service, or customer need, plus compatible context, value, destination, and bidding economics.
- An ad tests one distinct message or creative angle within that focused ad-group scope.

Reuse an existing campaign or ad group only when the proposed work remains inside that scope. Create or recommend a separate:

- campaign when the objective, budget pool, geography, schedule, campaign type, or required business or compliance control differs;
- ad group when the product or service, product economics or bid strategy, customer need, use case, message, or landing-page journey differs enough that one set of context hints would no longer describe every ad accurately;
- ad when the same focused offering can be explained through a genuinely different benefit, offer, use case, message, image, or creative concept.

Do not fragment structure for cosmetic wording changes. Do not combine unrelated offerings merely to use the shortest create sequence. When a request spans several scopes but the active workflow supports only one focused create set, explain the recommended split and ask the user which focused scope to create first.

## Write Relevance Context, Not Targeting

Context hints supplement the ad and landing destination with useful advertiser knowledge. They help describe when the offering may be relevant; they are not keywords to bid on, exact-match controls, audience targeting, exclusions, delivery commands, or guarantees.

Each hint should:

- add meaningful information beyond what the title, body, and landing destination already make clear;
- be specific about a real product feature, service detail, price, availability, service area, customer need, or useful situation;
- explain a genuine connection between the offering and that need or situation;
- stay accurate to the supplied product, business, landing page, pricing, availability, service area, claims, and policy constraints;
- use one clear, natural phrase rather than a keyword list or a lengthy persona description;
- remain inside the ad group's one coherent product, service, or customer-need scope.

Use advertiser persona knowledge only to discover genuine needs and use cases, then translate it into product-focused relevance context. Do not write hints that assume the system can identify or infer sensitive personal information, protected traits, demographics, or predicted customer value for an individual user.

When a user wants hard geographic restrictions, schedules, platform restrictions, age exclusions, or other delivery constraints, use only the supported product control and applicable policy path. Do not disguise those constraints as context hints.

Do not impose a fixed hint count or word count. Prefer a small set of distinct, high-quality hints grounded in confirmed facts over padding with repetitions, broad labels, or invented details.

## Keep Ads And Landing Pages Aligned

Within one ad group, diversify ads through materially different, factual angles rather than minor rewrites. Each ad's title, body, image, and landing destination should continue the same audience need, use case, and promise.

Use the most relevant destination supported by the advertiser's facts rather than defaulting to a generic homepage. Do not claim that a destination is reachable unless a live tool or allowed browse result proves it. If different ads require different messages or landing destinations because they serve meaningfully different needs or journeys, treat that as an ad-group scope decision before creating anything.

## Draft And Review Before Writing

When the user asks for planning, recommendations, or help filling in missing structure:

1. Identify the offering, objective, budget or schedule boundary, geography, campaign type, customer need or use case, message, and destination already supported by the user's facts.
2. Propose the smallest coherent campaign, ad-group, and ad structure. State the reason for each split or reuse in user-facing language.
3. Draft or review context hints against the relevance rules above. For each drafted or supplied hint, explain the meaningful information it adds. When the user supplies draft hints, mark each one `Keep`, `Revise`, or `Remove` and explain why. Flag unverifiable claims, prices, availability, service areas, or policy-sensitive details instead of inventing or silently accepting them, then return the final revised set separately from the review notes.
4. Check that every proposed ad, hint, and landing destination fits its ad-group scope.
5. Preserve the normal confirmation and write-safety workflow. Best-practice advice never authorizes extra fields or additional creates.

For an explicit request to create or update only the fields the user named, keep the payload minimal. Offer best-practice guidance separately when it would help, but do not silently expand the approved mutation.
