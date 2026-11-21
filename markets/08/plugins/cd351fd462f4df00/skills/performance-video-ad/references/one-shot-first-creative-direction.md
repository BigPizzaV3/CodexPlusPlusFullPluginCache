# One-shot-first creative direction

## Contents

1. Purpose
2. The compression test
3. Commercial and generation scores
4. Concept evidence
5. Route rules
6. Integrated prompt pattern
7. Exactness budget
8. Human interaction policy
9. Common failures

## Purpose

Design the commercial idea at the largest coherent unit the video model can solve. One-shot-first is not “write a vague prompt.” It is a deliberate contract:

- commercial meaning is narrow and explicit;
- the visual event carries the argument;
- only the exact details that affect truth or action are locked;
- filmmaking decisions with many valid answers remain delegated.

The desired outcome is a near-final complete candidate sooner, not fewer planning thoughts. Perform the analysis internally and compress it into a usable generation brief.

## The compression test

Before choosing One-shot, express the idea in this form:

> The intended viewer recognizes **[painful situation]** when **[visible event]** happens. Their usual response **[false response]** visibly fails. Then **[reframe]** becomes apparent through **[transformation/reveal]**, and **[offer]** appears as the credible next action.

PASS requires:

- the sentence describes one causal arc, not a list of services;
- the viewer can understand the tension without reading a paragraph;
- the visible event would still carry meaning with background UI blurred;
- small deviations in object placement would not destroy the premise;
- the ending can reveal the offer without becoming a separate unrelated ad.

FAIL when the concept requires exact email threads, several monthly labels, a detailed report, or multiple independent logical steps to be read in sequence.

## Commercial and generation scores

Score each candidate from 1–5.

### Commercial strength

- who relevance
- two-second problem comprehension
- semantic tension
- surprising reframe
- offer connection
- trust
- qualified click curiosity

### Generation solvability

- motion carries meaning
- single-world coherence
- low reading burden
- deviation tolerance
- identity feasibility
- ending feasibility
- audio-optional comprehension

Record exact-surface, identity, claim, privacy, and continuity risks as low, medium, or high. Do not average away a blocking risk. High privacy risk blocks external generation. High exact-surface dependency routes to controlled or deterministic production even when other scores are high.

## Concept evidence

Persist concept comparison before prompt construction. `concept-candidates.json` is the audit boundary between source-grounded ideation and production commitment.

- Use `comparison` with at least three candidates for internal comparison or a user-requested Taste discussion.
- Use `user_supplied_preference` with one or more candidates only when the user already supplied the preferred concept.
- Record source reuse explicitly. Reusing a verified Offer Source Lock is valid only when the offer, destination, CTA, funnel role, and claim boundary have not materially changed.
- Give every candidate separate commercial and generation scores. A visually solvable candidate can still be commercially weak; a strong sales idea can still require a controlled route.
- Record each candidate's opening event, causal motion, Reframe, offer role, end state, exactness budget, risks, copy lineage, and route recommendation.
- When the user asked to compare ideas, preserve `AWAITING_TASTE` until their choice is captured as `human_selected` with evidence.
- When comparison was internal, preserve the recommendation and selection as `agent_selected`; do not fabricate human approval.
- Reject a ready One-shot handoff when its `conceptId` differs from the selected candidate.

## Route rules

Choose one-shot-first when:

- motion is a major semantic carrier;
- one world and one emotional arc can contain the ad;
- the must-read copy fits in five short units;
- exact surfaces are low or medium risk and repairable;
- no confidential evidence enters the provider;
- the generated picture can own the look.

Choose one-shot-plus-finish when the same conditions hold but final logo, CTA, caption, price, legal line, or sourced proof must be deterministic.

Choose controlled-sequence when:

- the audience must read multiple exact work artifacts;
- one character must remain exact across incompatible worlds or long duration;
- continuity between a generated action and an exact surface is the viewer value;
- one-shot attempts repeat the same named failure;
- the provider cannot support the required duration or references in one unit.

Choose deterministic-demo when the product/UI behavior itself is the proof.

## Integrated prompt pattern

Write a provider-neutral prompt in this order.

### 1. Deliverable

State vertical format, duration range, platform, target viewer, language, and whether sound is desired.

### 2. Campaign idea

State one sentence with the Pain, visual concept, Reframe, and offer reveal.

### 3. World and protagonist

Describe only identity-defining details, the environment, emotional movement, and brand palette. Attach reference assets when identity matters.

### 4. Semantic-motion arc

Use four to eight chronological stages. Each stage must change what the viewer understands. Prefer verbs such as appears, grows, blocks, rejects, redirects, reveals, transforms, and resolves. Avoid a shot list full of show, display, and cut to.

### 5. Must-read copy

Limit to the smallest units required for Hook, Reframe, offer, and CTA. Mark source-backed exact copy separately from repairable creative copy.

### 6. Typography ownership

Assign one to three look-critical phrases to integrated generated typography only when their scale, material, depth, occlusion, or motion strengthens the causal event. Assign brand, CTA, price, legal copy, and proof to exact finishing. Choose `none`, `selective`, or `full_accessibility` captions deliberately; do not default to sentence-by-sentence bottom subtitles.

### 7. Sensory direction

Describe visual finish, camera energy, material behavior, contrast, sound intention, and emotional ending. Use a macro envelope rather than a camera instruction for every second.

### 8. Locks and no-gos

Name identity locks, forbidden deformations, prohibited guarantees, privacy exclusions, unwanted genre drift, and required end state.

### 9. Delegated freedom

Explicitly permit the model to design camera choreography, secondary motion, transitions, particles, and cut rhythm while preserving the semantic arc and copy order.

## Exactness budget

Classify each semantic surface:

- truth-critical: price, quantified claim, legal text, sourced proof; must be exact in final.
- action-critical: brand, service name, CTA; must be exact in final.
- comprehension-critical: Hook or Reframe copy; may be generated only when short and reviewable, then repair if needed.
- atmospheric: background UI, decorative labels, non-semantic numbers; need plausibility, not exact content.

Do not spend deterministic effort on atmospheric text. Do not let atmospheric hallucinations look like real client data.

## Human interaction policy

When the user asks only to make the ad:

1. resolve sources internally;
2. compare concepts internally;
3. show one concise recommended concept, the generation route, and the paid request;
4. stop for cost approval;
5. show the generated near-final candidate.

When the user explicitly asks to discuss the structure, show the three concept candidates before generation and wait for Taste.

## Common failures

- **Vague beauty prompt**: strong look, no commercial causality. Add the Pain, false response, Reframe, offer role, and ending state.
- **Miniature LP**: too many claims and labels. Reduce to one Sales Thesis and destination handoff.
- **Micromanaged prompt**: every object trajectory and cut is prescribed. Restore model freedom outside meaning locks.
- **Unrepairable exactness**: the idea depends on paragraphs of generated Japanese. Change the concept or route.
- **Subtitle wallpaper**: a premium generated film is covered by generic full-sentence overlays. Keep only intentional keywords, exact surfaces, or accessibility captions and integrate their visual language with the film.
- **Metaphor without mapping**: impressive creature or transformation, unclear business Pain. Make the first event and Reframe audience-native.
- **Offer pasted on**: cinematic story ends, then an unrelated card appears. Make the offer the agent or method that resolves the visible tension.
- **Spectacle as strategy**: the effect stops attention but reduces trust. Reduce visual intensity while keeping semantic tension.
