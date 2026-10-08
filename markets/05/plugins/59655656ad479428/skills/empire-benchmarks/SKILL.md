---
name: empire-benchmarks
description: Fetch current Artificial Analysis language-model benchmarks, join exact OpenRouter model identities, apply transparent weighted scoring and modality requirements, and render a sandboxed vertical comparison chart in supported Codex or ChatGPT surfaces. Use for current best-model questions, agentic or coding benchmark comparisons, route-fit visualizations, and benchmark-weighted model selection; do not use it to dispatch a model completion.
---

# Empire Benchmarks

Create a current, attributable benchmark view while Codex remains the analyst
and routing authority. This skill is read-only: it may call model metadata APIs,
but it must never dispatch an inference request, reserve project budget, send
repository evidence, or expose credentials to the generated UI.

## Build the benchmark view

1. Translate the request into a profile (`agentic`, `coding`, `balanced`, or
   `value`), requested input/output modalities, top-model count, and any explicit
   scoring weights. Preserve the user's date wording in the explanation. The API
   returns current data; do not claim it reconstructs a historical snapshot.
2. Resolve this skill's directory as `EMPIRE_BENCHMARK_ROOT`, then resolve the
   shared runner at `../../scripts/empire_benchmarks.py`.
3. For a current route-qualified agentic view with Pro/Commercial identity
   evidence, run:

   ```bash
   python3 "$EMPIRE_BENCHMARK_ROOT/../../scripts/empire_benchmarks.py" rank \
     --profile agentic \
     --route-qualified-only \
     --top 8 \
     --output /tmp/empire-benchmarks.json
   ```

   Add `--input-modality image` or another requirement only when the user needs
   it. Add repeatable `--weight agentic=45` style overrides when the user states
   priorities. The runner normalizes weights to 100% and reports them.
   Artificial Analysis Free omits `openrouter_api_id` and modality metadata.
   For that tier, omit `--route-qualified-only` to create an explicitly unverified
   research chart; never claim a qualified route or infer missing IDs. Explain
   that Pro/Commercial identity evidence is needed for exact joins. Do not
   upgrade a subscription or change the user's cost policy automatically.
4. The live command reads the Artificial Analysis credential and optional
   OpenRouter credential through Empire's existing environment/keyring boundary.
   If a key is missing or inaccessible, use `$empire-settings`; never ask the
   user to paste a key into chat or put one in a command argument.
5. Treat the returned JSON as the source of truth. Verify its source receipt,
   tier, index version, retrieval time, weights, evidence coverage, modality
   state, and exact OpenRouter match before recommending a route.

## Render inside Codex

When the current surface supports in-conversation visualizations, choose a
writable thread visualization path and run:

```bash
python3 "$EMPIRE_BENCHMARK_ROOT/../../scripts/empire_benchmarks.py" render \
  --input /tmp/empire-benchmarks.json \
  --output /absolute/thread/visualization/empire-model-benchmarks.html
```

Return the generated fragment with the host's visualization content reference.
The fragment is self-contained, embeds only sanitized benchmark fields and local
14 px model icons, performs no browser-side network requests, and lets users
adjust the scoring weights. Its follow-up button may ask Codex to compare the
leaders, but it may not dispatch an external model.

If the surface cannot render visualizations, rerun `rank` with `--view markdown`
and return the accessible Markdown table. Do not claim that Codex CLI or an IDE
extension rendered an interactive chart.

## Evidence and routing boundaries

- Artificial Analysis `/api/v2/language/models` is used for Pro or Commercial
  access. `auto` falls back to the documented `/api/v2/language/models/free`
  endpoint only after a tier-level `403`; every page is validated and bounded.
- Current benchmark indices, pricing, and performance come from Artificial
  Analysis. Empire's weighted score is an inference, not an Artificial Analysis
  rank. Always keep the visible attribution link.
- [Artificial Analysis API documentation](https://artificialanalysis.ai/data-api/docs)
  defines which fields each tier exposes. Missing identity or modality fields
  are a capability limitation, not permission to substitute fuzzy matches.
- OpenRouter is queried only through its authenticated user-visible model
  catalog. A model becomes route eligible only when
  `openrouter_api_id` matches an OpenRouter model ID exactly and required
  modalities pass. Fuzzy names may be discussed as unverified, never routed.
- Missing evidence reduces the weighted score; it is not silently converted to
  a zero benchmark. Incompatible modalities fail route eligibility.
- OpenAI models may be included with `--include-openai` as research baselines,
  but they remain ineligible as Empire partner models because Codex is the
  OpenAI lead.
- A chart is a read-only comparison. Before any later external completion,
  rerun the normal Empire route/review authorization flow and respect its cost,
  privacy, freshness, and project-budget gates.
- Artificial Analysis requires attribution, and API access or redistribution
  rights depend on the user's tier and agreement. Never package a live API
  response or benchmark snapshot into a release artifact.

## Useful prompts

- “Give me the best agentic-model benchmarks as of September 2026 and show the
  top eight in a vertical weighted chart.”
- “Compare current coding models with 50% coding, 25% agentic, 15% modality,
  and 10% cost weight. Require text and image input.”
- “Show the best-value non-OpenAI partners available to my OpenRouter account,
  then explain why the top two complement Codex.”
