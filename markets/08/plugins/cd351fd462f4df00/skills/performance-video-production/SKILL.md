---
name: performance-video-production
description: Produce and diagnose approved short-form ads with an AI-native one-shot-first route, current model selection, paid execution controls, Raw triage, minimal deterministic finishing, sound, and final QC. Use after performance-video-ad creates a ready one-shot brief, when reviewing an existing generated ad, or when exactness and continuity require controlled generation. Do not rewrite the offer, Sales Thesis, CTA, claim boundary, or test strategy.
---

# MyMarketer Performance Video Production

## User-facing identity

Refer to this skill as `MyMarketer Performance Video Production` in every user-visible progress update, approval request, report, and handoff. Use the internal identifier `performance-video-production` only in `$skill` invocations, paths, schemas, and code.

## Optional MyMarketer quality connection

Only when an already available basic check applies to this decision, or the user explicitly requests paid server judgment, read the [optional creative-check contract](../lp-image-builder/references/creative-core-contract.md). The new connection is a development candidate not currently provided in production; retain all local quality rules, approvals and the normal non-persistent workflow.

This connection is **read-only by default / explicit save only**.

For guidance and rubric, use `contextMode: "reference"` only if the advertised tool schema supports it and the complete preview `context` remains available in this run with the same connection, project, and fingerprint. Resolve `contextReference.fields` from that preview context; a reference does not mean empty constraints. Omit the argument for older schemas. If the context was lost, reacquire the preview at most once or fall back to free mode. On `CONTEXT_TOO_LARGE`, discard paid context, show the policy's size-limit notice, and continue in free mode without retries or legacy-tool bypass. Do not truncate important decisions/rules or claim connected quality with incomplete context.

Before work, read the [shared connected-quality policy](../lp-image-builder/references/connected-quality-policy.json). When the MyMarketer `/mcp/quality` read connection and `quality_preview` capability are not known to be available, do not request login, do not probe unavailable tools, and complete the work with the approved handoff and this local Skill.

Only with the paid read connection, use `listProjects` to resolve exactly one project, then call `prepareMarketingJobPreview(deliverableType=performance_video_production)` for source-backed context and its `contextFingerprint`. Pass the same fingerprint to `getProductionGuidanceInputs` and `getDeliverableReviewRubric`. The host creates three directions when the upstream handoff has not already fixed one, the user selects one, and the host applies the rubric privately after creation, revises at most once only when it fails, and re-scores. Restart from context retrieval on `CONTEXT_CHANGED`. Never change the inherited grounded outcome, approved decisions, CTA, offer, claims, or project identity.

Do not use the legacy tools that mix `persistence=preview` and persistence in this normal quality flow. Call `saveDeliverableV1` only when the user explicitly asks to save the completed deliverable, and request additional `mcp:write` authorization when needed. OAuth write scope is not action approval. Tactic proposals, decisions, learning writes, publishing, activation, and every paid provider execution still require their own explicit confirmation. Never invent performance or learning before actual results exist.

On connection, subscription, permission, project, or budget failure, discard paid context for the current run, never reuse its cache, never guess MyMarketer data, show only the policy's one-line `有料品質ループ未適用` notice, and continue in unconnected mode. Do not show that notice for a task that began unconnected.

Act as the production director and finishing studio. Default to one coherent model-generated film as the primary picture when the approved brief says `one_shot_first` or `one_shot_plus_finish`. Use Remotion/FFmpeg for finishing, not for rebuilding cinematic motion that the model should own.

Read [one-shot-generation-and-triage.md](references/one-shot-generation-and-triage.md) before executing or reviewing a whole-video generation.

For new v2 generation or repair, inherit grounded `primaryOutcome` unchanged from the approved upstream `offer-context.json` and `one-shot-brief.json`; never ask for it again in this production skill. Validate that lineage before production and copy the same object unchanged into `one-shot-review.json`. Standalone `REVIEW_ONLY` may omit upstream: record the exact v2 unavailable sentinel in the review and do not claim outcome-relative task evaluation. Legacy v1 jobs may continue through the explicit compatibility path under the same commercial-meaning locks, approval, cost, privacy, QC, and distribution controls, but they have no grounded outcome lineage and must not claim outcome-relative task evaluation. Never invent an outcome.

## Entry modes

Choose one mode explicitly:

- `ONE_SHOT_PRODUCTION`: for new work, require a locked v2 `offer-context.json`, a ready v2 `one-shot-brief.json` with matching grounded `primaryOutcome`, integrated prompt, locked commercial meaning, privacy clearance, disabled distribution, and current paid approval before the provider call. An existing ready v1 brief may execute after the exact `--require-ready --legacy-v1` validation below; it keeps every other production control and cannot personalize a recommendation.
- `REVIEW_ONLY`: inspect an existing Raw without changing it or spending money; produce `one-shot-review.json`. Upstream is optional only here. When absent, use `--standalone-review` and the unavailable outcome sentinel; when legacy v1, use `--legacy-v1`.
- `SURGICAL_FINISH`: for new work, require an accepted primary picture, a bounded repair list, and strict grounded v2 upstream lineage; preserve the generated world and concept. For a legacy v1 job, require the legacy-ready brief and reviewed-v1 commands to pass, retain the original commercial locks, and keep recommendation suppression in force.
- `CONTROLLED_PRODUCTION`: require the legacy approved production handoff and feasibility artifacts because a named exactness or continuity risk justifies them.
- `REPLACEMENT_ONLY`: replace approved audio or another exact asset one-for-one without changing picture or Creative; require strict grounded v2 upstream lineage for new work, or the same validated and recommendation-suppressed v1 compatibility chain for a legacy job.

Do not force a One-shot job through Animatic, Visual Treatment, compositing-feasibility, shot manifest, or immutable v4 handoff gates. Do not let a controlled job bypass them.

## One-shot production workflow

1. For v2, validate `one-shot-brief.json` against `offer-context.json`; `primaryOutcome` must match unchanged. For an existing v1 job, run the explicit legacy-ready command below and record that outcome lineage is unavailable.
2. Refresh official model capabilities, supported duration/aspect ratio, reference controls, pricing, audio behavior, output format, and commercial terms on the execution date.
3. Select the model and mode that best preserve the brief's coherent event. Do not choose by brand reputation alone.
4. Adapt the provider-neutral prompt only for provider syntax. Preserve the Sales Thesis, semantic-motion arc, must-read copy, claim boundaries, identity locks, ending state, and delegated freedom.
5. Prefer one whole-video request. Split only when a documented provider limit, privacy boundary, incompatible world reset, exact semantic surface, or repeated failure makes the split necessary.
6. Before the paid call, show the exact provider/model, request count, expected cost, maximum cost, local save path, and whether audio is included. Wait for explicit current-task approval.
7. Mark approval consumed immediately after the request. Save request ID, prompt, settings, references and hashes, returned metadata, and Raw locally.
8. Review the untouched Raw at natural speed with audio before overlays, retiming, stabilization, captions, or SFX.
9. Write and validate `one-shot-review.json`; choose exactly one review decision.
10. Continue only along the decision's permitted path. A retry is a new paid request and requires new approval.

## Review decisions

Use the earliest-failure rule.

### `ACCEPT_PICTURE`

Use when the opening stops the intended viewer, the causal event reads, the Sales Thesis survives, the offer reveal connects, claims are safe, the ending is usable, and no material repair remains. Continue to audio/final QC.

### `SURGICAL_FINISH`

Use when the primary picture and concept work and the remaining issues are bounded to exact copy, logo, CTA, crop, trim, color match, small cleanup, narration, SFX, or End Card. Record each repair and why it does not change the Creative.

### `REGENERATE_SAME_CONCEPT`

Use only when concept comprehension and prompt-to-concept fit pass, but stochastic execution fails through identity drift, malformed motion, unreadable critical text, broken timing, weak force, missing event, or unusable ending. Do not silently rewrite the concept. Record whether a non-semantic prompt clarification or reference change is justified.

### `RETURN_TO_CONCEPT`

Use when the opening is weak, the viewer cannot map the visual event to the Pain, the Reframe is absent, the offer feels pasted on, the concept depends on reading too much, or repeated execution shows that the concept is not model-solvable. Return a concise blocker to `performance-video-ad`; do not polish or reroll indefinitely.

Run:

```bash
node ../performance-video-ad/scripts/validate-one-shot-brief.mjs <job-dir>/one-shot-brief.json --require-ready --offer-context <job-dir>/offer-context.json
node scripts/validate-one-shot-review.mjs <job-dir>/one-shot-review.json --require-reviewed --one-shot-brief <job-dir>/one-shot-brief.json
```

For standalone review with no trustworthy upstream, keep the template's exact unavailable `primaryOutcome` sentinel and run:

```bash
node scripts/validate-one-shot-review.mjs <job-dir>/one-shot-review.json --require-reviewed --standalone-review
```

For an existing schemaVersion 1 ready brief, enter the compatibility path with the planning validator from the production skill directory:

```bash
node ../performance-video-ad/scripts/validate-one-shot-brief.mjs <job-dir>/one-shot-brief.json --require-ready --legacy-v1
```

Only after that PASS may `ONE_SHOT_PRODUCTION` continue, using the same integrated prompt/commercial locks and the normal privacy, current paid-approval, cost, retry, QC, and disabled-distribution controls. Keep the downstream review at schemaVersion 1 and validate it with:

```bash
node scripts/validate-one-shot-review.mjs <job-dir>/one-shot-review.json --require-reviewed --legacy-v1
```

This compatibility path preserves existing production and review execution but has no grounded `primaryOutcome`, cannot claim v2 lineage, and must not claim outcome-relative task evaluation. `--standalone-review` remains review-only and can never authorize generation, retry, surgical finish, or replacement.

## Generation-control budget

For the default route:

- lock the macro event, emotional movement, protagonist/brand identity, must-read copy, ending state, and no-gos;
- delegate camera micro-timing, secondary motion, material behavior, transitions, and shot rhythm;
- add a reference image only for a named identity or look risk;
- add first/last frames only when the endpoint or continuity is essential and the model supports them without suppressing the required motion;
- add intermediate frames or motion references only for a reproduced failure.

Do not build start/peak/end frames for every sequence. Do not use a polished Animatic as conditioning by default. Do not split a coherent event such as `impact -> rupture -> passage -> landing` when continuity and force are its value.

## Exactness and finishing

Generated Japanese is allowed as a reviewed first-pass carrier when it is short, non-regulated, and repairable. Keep these exact in the delivered media:

- service and brand name;
- CTA action;
- price and quantified claims;
- legal or regulated copy;
- proof that must match a source;
- product/UI details whose precision is the viewer value.

Follow the approved `typographyPlan`. Preserve successful integrated keywords as part of the primary picture. Prefer provider edit/remix, tracked in-world replacement, or a native End Card when repair is required. Add selective or full accessibility captions only when the plan names that need; do not cover a premium generated film with generic sentence-by-sentence subtitle styling. Read [typography-production-and-qc.md](references/typography-production-and-qc.md) before repairing generated text or adding captions.

Record the natural-speed result and selected repair mode in `typographyReview` before accepting or surgically finishing the picture.

Repair only the frames or surfaces that need it. Prefer final-frame repair, tracked replacement, inpainting, provider edit/remix, or a native End Card over placing a flat duplicate on top of a moving world. If a repair requires rebuilding most visible pixels, the review decision was not `SURGICAL_FINISH`.

For `one_shot_first`, the model remains the primary-picture owner. Remotion/FFmpeg may trim, stitch, crop, normalize, caption, mix, add or repair exact surfaces, and produce the delivery codec. They must not become the default look-development or primary-motion engine.

## Controlled fallback

Enter `CONTROLLED_PRODUCTION` only from a planning route decision or a validated `RETURN_TO_CONCEPT` blocker that names the exactness/continuity risk. Then use the existing production-handoff, route-plan, world-binding, keyframe, dependency, audio, and QC validators.

Use the fewest coherent generation units. A unit may contain multiple cuts or camera moves when the current verified model supports them. Preserve actual upstream frames for continuity. Reject missing causal events, identity drift, malformed subjects, unintended text, cadence problems, and unusable endpoints before compositing.

Read [generative-direction-and-control-budget.md](references/generative-direction-and-control-budget.md), [motion-quality-routing.md](references/motion-quality-routing.md), and [world-binding-and-feasibility.md](references/world-binding-and-feasibility.md) only when the controlled route needs them.

## Paid execution

Never infer approval from concept, Taste, handoff, prior turns, or a successful previous call. Before each paid batch:

- recheck current provider schema and price;
- record exact request count, retry count, expected and maximum cost;
- keep initial exploration to one request unless the user approves a bounded batch;
- consume approval immediately after execution;
- retain request ID and a durable local Raw;
- never auto-retry.

Use state labels exactly: `WRITTEN`, `CONFIGURED`, `EXECUTED`, `REVIEWED`, `VERIFIED`, and `BENCHMARKED`. A successful API response is only `EXECUTED`.

## Audio and sound

Use provider audio when it is good enough and rights/voice requirements allow it. Otherwise preserve the accepted picture and replace audio without redesigning the ad.

- Audit the rendered provider-audio-only stem for speech and vocalization before retaining it under external narration. The rendered audio, not the prompt's intended soundscape, determines whether a voice exists.
- If an unapproved voice is present, fail full-track retention. Ducking, center cancellation, phase cancellation, EQ, and source labels such as `SFX` do not prove voice removal.
- Retain only independently reviewed clean stems or windows. When clean isolation is uncertain, discard provider-native audio completely and rebuild with owned, procedural, or properly licensed voice-free SFX.
- Keep one narrator role unless the Creative explicitly requires dialogue.
- Treat Japanese TTS as exact-language production; verify every spoken line and CTA.
- Align the first phoneme and causal SFX to the final retimed visual event.
- Use SFX to explain impact, reveal, transition, quantity, or payoff—not to decorate every cut.
- Preserve intentional silence and narration clarity.
- Review narration-only, SFX-only, full-mix, and mute-picture versions when audio is rebuilt.

Read [audio-production-and-qc.md](references/audio-production-and-qc.md) and [sound-design-and-sfx.md](references/sound-design-and-sfx.md) only when audio is replaced or mixed.

## Final QC

Require:

- two-second comprehension of the intended problem or tension;
- a visible stop reason and continue reason;
- one coherent Sales Thesis rather than a sequence of service labels;
- the approved semantic-motion event and ending state;
- exact final brand, CTA, price, legal copy, and source-backed claims;
- reviewed integrated keywords that are legible at natural speed, and post-added captions whose design belongs to the generated film rather than looking like a generic overlay preset;
- no privacy leak, malformed subject, identity drift, accidental duplicate character, unintended text, or unsupported guarantee;
- complete decode, requested 9:16 dimensions, compatible delivery codec, monotonic timestamps, and smooth cadence;
- narration, SFX, music, and retained provider audio present in their intended windows;
- no unapproved provider speech, conflicting narrator, residual double voice, or vocal contamination in the SFX/music buses;
- final last-mile Taste from the user, or the distinct scoped agent receipt in an approved marketing run;
- distribution still disabled unless separately authorized.

Run `scripts/validate-one-shot-review.mjs` with `--require-reviewed --require-final-delivery --final-delivery <final-delivery.json>` and the existing brief/standalone lineage arguments before final delivery. Follow the [final Taste contract](../marketing-omakase/references/delegation.md#final-one-shot-delivery). The final record binds all QC checks, final media bytes and review; a pending repair cannot pass.

Technical PASS never implies Creative PASS or performance proof.

## Default output contract

Add these to the shared One-shot job:

```text
jobs/<job-id>/
├── offer-context.json
├── one-shot-brief.json
├── capability-snapshot.json
├── provider-prompt.md
├── cost-estimate.json
├── approval.json
├── generated/raw.mp4
├── one-shot-review.json
├── repair-plan.json          # only for SURGICAL_FINISH
├── voice-qc.json             # when voice is generated/replaced
├── audio-cue-sheet.json      # when SFX/audio is rebuilt
├── production-learning.json
├── final-delivery.json       # final QC + human or scoped agent Taste
├── final/
├── logs/
└── qc/
```

Legacy controlled jobs retain the existing production-handoff, shot graph, route plan, compositing-feasibility, keyframe, timeline-audio, and world-binding artifacts.

## Failure learning

Record the earliest bad boundary and keep these separate:

- `concept_learning`: whether the idea was understandable and desirable;
- `prompt_model_learning`: whether the provider realized the approved idea;
- `finishing_learning`: exactness, timing, audio, or delivery problems;
- `performance_learning`: campaign evidence only.

Promote a production rule only after recurrence in two independent jobs, a reproducible test, or one material safety/spend/privacy incident. Never turn one preferred video into a performance claim.

## Outcome-oriented assistance

Policy boundary: `final_verified_video_handoff`.

The successful-completion boundary is a final delivered video after technical QC, Creative QC, and required final last-mile Taste have all passed. Standalone delivery uses the human decision; an approved marketing run may use the separate final agent Taste receipt with the same QC. A provider response, Raw review, retry decision, surgical-finish plan, approval, cost gate, selection, or production handoff is intermediate.

Complete the final production/QC report first, then apply the [shared outcome-oriented assistance policy](../lp-image-builder/references/outcome-oriented-assistance-policy.json). Compare the unchanged, source-grounded `primaryOutcome` with the delivered, verified video and report only task-relevant gaps or next steps. Do not proactively promote MyMarketer, a connection, or paid features. Answer ordinary follow-up questions normally without turning interest into an acquisition state.

Only when the user explicitly asks to connect an existing MyMarketer account may the response show `host_connection_ui`, at most once, and only when that host UI is available. A user assertion that the account already exists is sufficient to offer the UI, but never claim entitlement until verified. If account status is unknown, ask at most one relevant existing-account clarification without a sales pitch and continue the free task. If the host UI is unavailable, give a neutral unavailability explanation with no registration, sales, trial, upgrade, or checkout fallback. Do not call tools to measure interest or transmit conversation text. These plugin-self-promotion limits do not prohibit a product CTA in the user's ad or genuine support/legal links.

## Safety and distribution

- Do not upload confidential material without explicit permission and sanitization.
- Do not execute paid calls without current-task cost and count approval.
- Do not publish, upload, activate ads, or change budgets without separate authority.
- Keep private dogfooding jobs, client evidence, credentials, provider responses, and generated media out of public Skill packages. Distribute only sanitized reusable instructions, schemas, templates, and validators after package validation.

When the user requests formal MyMarketer storage, resumption, or results-based improvement, follow [paid project continuity](../lp-image-builder/references/paid-continuity.md). This optional workflow never blocks free completion.

## Scoped marketing run delegation

When invoked inside an approved marketing-omakase run, read [the distinct expression delegation contract](../marketing-omakase/references/delegation.md). Its implemented scoped agent receipts may resolve the listed expression choices while retaining this skill's source, comparison, rendering and quality checks. Keep human price, fact, rights, strategy and cost decisions separate. Other human-only gates and standalone behavior remain unchanged. A delegated choice is never recorded as human feedback.
