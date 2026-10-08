# Evidence policy

Use this policy whenever a comparison presents a number or recommendation.

## Evidence classes

1. **Official exact** — live catalog fields, token prices, credit rates, Fast
   multipliers, supported efforts, and context limits.
2. **OpenAI-published measurement** — a named benchmark with its version,
   harness notes, evaluation setting when known, source URL, and publication
   date.
3. **Locally measured** — matched runs on the user's task, with sample size,
   elapsed time, token usage, grader, failures, and configuration.
4. **Derived estimate** — arithmetic based on published or local inputs. Show
   the formula, assumptions, and an interval when uncertainty is material.
5. **Unknown** — no defensible numeric value. Keep it visible as unknown.

## Non-negotiable rules

- Never turn the model-card 1–5 capability or speed icons into percentages.
- Never invent a universal intelligence score or average unrelated benchmarks
  into one.
- Never infer an effort-specific score when the evaluation does not identify
  its effort.
- Never assume quality is monotonic with effort.
- Never convert 1.5× model speed into one-third less wall-clock task time unless
  the model-time share is known.
- Never mix ChatGPT credits, API dollars, included plan messages, or legacy
  per-message rates.
- Never compare benchmark rows across different versions or harnesses without
  an explicit comparability note.
- Treat fewer than five local trials as exploratory.
- Preserve a last-known-good official snapshot if refresh parsing fails, and
  show its retrieval date.

## Configuration semantics

- Treat the desktop **Power** preset separately from model-catalog defaults.
  Current docs define Power as GPT-5.6 Sol + medium reasoning.
- Treat **Max** as more single-agent reasoning time.
- Treat **Ultra** as a topology change that delegates to multiple agents, not
  another scalar effort level.
- Treat **Fast** as a service tier. Read supported tiers from the live catalog
  and keep internal aliases such as `fast` and `priority` out of the user-facing
  label.

## Recommendation rule

Recommend a configuration only when the evidence supports the user's task and
constraints. If missing evidence can change the choice, recommend the smallest
matched experiment that resolves it instead.
