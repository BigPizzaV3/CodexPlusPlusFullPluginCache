---
name: compare-model-tradeoffs
description: Compare Codex model, reasoning-effort, and Standard/Fast combinations using the live Codex catalog, official OpenAI pricing and evaluations, and optional matched local measurements. Use when a user asks which Codex model or effort to choose, what a setting gains or loses, whether Fast mode is worth it, which combinations are supported, asks to turn Model Compass on or off, requests its companion view, asks for an evidence-backed interactive comparison, or requests a controlled model duel on their own task.
---

# Compare Model Tradeoffs

Produce a decision receipt that separates what OpenAI establishes, what the
user's own runs establish, what is derived, and what remains unknown.

## Display state

Model Compass is quiet by default. Maintain a conversational preference named
`model_compass_visual` for the current thread:

- Default `model_compass_visual` to `off` in every new or forked thread.
- `Show Model Compass`, `Visualize this comparison`, and clear equivalents are
  one-shot requests. Render once without changing the preference.
- `Enable Model Compass for this thread`, `Turn Model Compass on`, and clear
  equivalents set the preference to `on`. Acknowledge the change; render
  immediately only when the same turn also asks for a comparison.
- `Disable Model Compass for this thread`, `Turn Model Compass off`, and clear
  equivalents set it to `off`. The latest explicit instruction wins.
- Treat a bare `turn off` as Model Compass only when no competing target is
  active in the conversation. Otherwise ask one short clarification.
- When resuming the same thread, recover the latest explicit preference from
  its history. If history does not establish a value, use `off`.
- When writing a handoff or compaction summary, preserve exactly one state
  line: `Model Compass visual: on` or `Model Compass visual: off`.

This preference is transcript-backed rather than durable host state. Never
claim stronger persistence than the available thread history establishes.

When the preference is `off`, provide an ordinary model-choice answer as a
concise text decision receipt without an inline visualization. End with one
unobtrusive sentence offering `Show Model Compass` when a visual would help.
When it is `on`, render only on relevant model, effort, speed, cost, or latency
decision turns. A one-turn `text only` request does not change the preference.
Disabling affects future responses; do not claim to remove visuals already in
the transcript.

`Open Model Compass companion view` is a one-shot request. Render the
narrow-friendly delta racetrack, then explain once that the desktop app can pop
out the active chat and optionally keep it on top. Do not change
`model_compass_visual` unless the user also explicitly enables it.

Do not persist the display preference to files or other threads. Do not
automatically open, move, resize, pin, or keep a window on top. Do not render a
visual on unrelated turns merely because the preference is on.

Pets are a separate user-controlled ChatGPT desktop feature. A plugin cannot
detect that the app was minimized, wake or tuck away a pet, replace the pet
activity tray, or put this visualization inside the pet overlay. If the user
asks for pet integration, explain that an awake pet can show cross-chat status
and return them to ChatGPT, but `/pet`, **Wake Pet**, and **Tuck Away Pet** stay
under user control.

## Workflow

1. Read `references/evidence-policy.md` and
   `references/companion-mode.md`.
2. Infer the task shape, billing surface, current choice, and hard constraints
   from the conversation. Use GPT-5.6 Sol + medium + Standard as the documented
   Power baseline when the user gives no baseline.
3. Discover valid choices from the live Codex catalog:

   ```bash
   node scripts/get-codex-catalog.mjs
   ```

   The helper starts the local Codex app server and calls only its read-only
   `model/list` method. It does not read credentials or Codex files directly.
   If the sandbox blocks that exact helper command, do not request broader
   filesystem access. Use current host tool metadata when it exposes model
   combinations; otherwise use the dated packaged baseline and mark live
   compatibility as unknown. Never run Codex debug-dump commands or parse
   Codex SQLite, rollout logs, `models_cache.json`, global state, or
   application bundles.
4. Refresh material official facts through the OpenAI developer-docs tools.
   Use only OpenAI-operated sources. Start from
   `references/openai-baseline.json` when remote docs are unavailable, and show
   its `asOf` date. Re-check at least model guidance, Speed, pricing, and the
   latest model launch when freshness could change the decision.
5. Join catalog choices to official facts by exact model ID. Let the catalog
   determine supported efforts and service tiers. Keep desktop presets separate
   from model-level defaults. Present Ultra as multi-agent delegation, not as a
   scalar effort value.
6. Classify every metric as `official-exact`, `official-proxy`, `local`,
   `derived`, or `unknown`. Preserve benchmark version, evaluation effort when
   known, source, and date.
7. When the current display state permits a visual, render one compact
   interactive comparison. Choose the view that best matches the decision:
   - `assets/neon-constellation.fragment.html` for a broad model landscape and
     Pareto-style exploration. Use it when a one-shot `Show Model Compass`
     request does not identify a concrete comparison.
   - `assets/effort-field.fragment.html` for inspecting the complete
     OpenAI-published GeneBench-Pro model × effort matrix.
   - `assets/delta-racetrack.fragment.html` for a selected-versus-baseline
     decision receipt. Prefer this view when the user is comparing one concrete
     choice.
   - `assets/tradeoff-lab.fragment.html` remains the compact general-purpose
     fallback.
   - Copy it to the thread-scoped visualization directory under a new
     lower-case hyphenated filename.
   - Patch the embedded catalog and official snapshot before displaying it.
   - Keep all data inline; do not fetch from the fragment.
   - Use the exact `::codex-inline-vis{file="name.html"}` directive.
   - Keep controls to model, effort, and Standard/Fast unless another input is
     essential to the user's stated decision.
   - For a Companion one-shot request, prefer
     `assets/delta-racetrack.fragment.html`; it is designed to remain legible
     in a narrow popped-out chat.
8. Lead with a tradeoff receipt:
   - selected and baseline configurations;
   - exact price, credit, availability, and Fast facts;
   - closest comparable published proxy;
   - domain-specific effort evidence, if relevant;
   - local evidence and sample size;
   - explicit unknowns;
   - cheapest useful next experiment.

## Matched measurement

Run a model duel only after the user explicitly asks to measure configurations
and accepts any material credit or API cost.

- Pin prompt, inputs, repo state, tools, permissions, timeout, and success
  criteria.
- Use isolated worktrees or disposable copies for code-changing trials.
- Interleave configuration order and use at least three trials when practical.
- Record wall time, output and reasoning tokens, tool time when observable,
  retries, failures, and deterministic test or artifact results.
- Treat fewer than five trials as exploratory.
- Use a blinded rubric only when deterministic grading is not possible.
- Keep raw proprietary prompts and code out of persistent telemetry by default.

Do not automatically apply model, effort, or Fast settings. Offer the exact
configuration command or setting after the comparison and require confirmation
before changing persistent defaults.
