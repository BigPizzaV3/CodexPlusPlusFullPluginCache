# Decision brief, criteria and procedures

## Decision brief

```markdown
# <Decision in one line>

**Recommendation:** <the actual decision, for example "prioritize segment A", "refine pricing", "defer the feature", "collect more evidence first">, and the one-sentence reason.
**Assessment of the evidence:** <Strengthening | Needs refining | Explore differently | Not enough evidence yet>
**Segment and workspace:** <name>
**What the evidence says**

- <Assumption>: <Supported | Contradicted | Mixed | Only simulated | Untested>. <Support counts, real/imported and synthetic, where established.> <A quote with the interview name, or the insight title, where available.>
  **Evidence mix:** <source research held N completed interviews: X real (Z imported), Y synthetic; analysis as of <updatedOn>; stage and analysis state noted separately>
  **Uncertainty:** <what could change this; what rests on one interview or synthetic only>
  **Alternative considered:** <option and why not now>
  **Next step:** <whatever fits the decision: interviews (research type, segment, who), usage data, existing transcripts, an experiment, or acting on what is already supported; and the question it answers>
  **Not yet supported by real customers:** <list>
```

Leave out sections the workspace gives nothing for, and say so. Leave missing quotes and counts missing. Separate observed findings from interpretation.

## Platform tests to apply before judging evidence

**Customer segment** (from the platform definition and the segment guide): a real group with shared needs, wants, behaviors or context; likely to care about the problem and willing to pay; defined by more than a job title or role; specific enough to direct research, interviews, positioning and go-to-market work; one solution, message and set of channels could work for all of them.

**Customer problem:** a real obstacle between the segment and what they need, want or value; important enough that customers may pay to solve it; not already well addressed by existing solutions; linked to one or more segments; distinct from the other listed problems; clear enough to validate through research.

If either test fails, say that first. Evidence about a badly defined segment or problem is hard to interpret.

## Choosing what to test first

Prioritize by impact if wrong and by uncertainty. Segment and problem assumptions come first when they are weak or the decision is about direction, because later choices depend on them. When the decision is about something else, prioritize the assumptions behind that decision. The platform gives no scoring method, so give your reasons in words.

## Reading research for a decision

Start with the analysis summary, then the categories that bear on the decision, then the supporting quotes and sources of the key insights, then the quality view for strengths, gaps and suggestions. Compare what you find with the Canvas assumptions and conclude whether the direction is strengthening, needs refining or should be explored differently.

Insight categories by research type: problem discovery (Job-to-be-Done, Triggering Events, Desired Outcome, Solution Search and Evaluation, Experience of Using the Chosen Solution, Additional); win/loss (Product in Focus, Triggering Events, Desired Outcomes, Solution Evaluation and Comparison, Reasons for Winning/Losing, Additional).

## Updating the Canvas after new evidence

Trigger: research has meaningfully changed the understanding of the customer, the problem or the direction.

1. Read the findings that changed the picture and confirm what the evidence actually shows.
2. Read the Canvas and find which items the evidence challenges.
3. If the target audience or the main obstacle changed, update customer segments and customer problems first (`update_canvas_customer_segment`, `update_canvas_item`). Move to the value proposition, channels, revenue streams, cost structure and key metrics only if the evidence changes how value is created.
4. Replace assumptions that no longer hold. Do not layer new text over old.
5. Read the Canvas again and check that it still fits together as a whole.
6. Name the assets that might be affected (Buyer Persona, positioning, landing page, sales deck). Read their content against the changed understanding and explain any mismatch. The tools do not record which asset depends on which Canvas item, and a Canvas edit alone does not show that an asset needs regenerating. A persona refreshes when its research changes. Positioning, landing pages and decks are independent snapshots and do not change by themselves.
7. Offer to save a note recording what changed and why.

`validate_canvas_item` checks an item against the platform's criteria. It is billable and advisory. Use it only when the user asks.

## Reviewing positioning after new evidence

Compare the current positioning document with the new buyer understanding on five points: core problem, desired outcomes, perceived barriers, decision criteria and the language customers use. Regenerate positioning only if it no longer reflects the latest understanding, and only if the user asks (`icanpreneur-gtm-assets`). Landing pages and decks are built from positioning, so regenerate them only after the positioning is settled.

## Checking a pitch, deck or set of claims

List the claims and sort them by type. Customer research can support claims about customer problems, buying behavior, alternatives and reactions. It cannot establish revenue, product capabilities, customer numbers, financial projections or market size; those need their own sources.

- For claims research can speak to, mark each supported, contradicted, mixed, only simulated or untested against the workspace evidence, with the sources available.
- For the others, say "not established by this research" and name the kind of source that would establish it. That is not a finding that the claim is wrong.
- Accept evidence the user supplies (a report, a dashboard figure, a contract), attribute it to them, and do not present it as Icanpreneur research.

Do not rewrite the pitch unless asked. Say which customer claims need real-customer evidence before they are used.

## Matching an assumption to a research stream

Whether the problem is real and important → problem discovery. Messaging, pricing, objections and decision criteria → buyer persona research. Why deals are won or lost → win/loss. Look for relevant findings across all types: a win/loss interview can contain problem evidence, and a problem interview can show buying criteria. Report which type each finding came from. If the best stream is missing, empty or synthetic-only for the segment, say so. A stream that cannot answer the question is not evidence either way.
