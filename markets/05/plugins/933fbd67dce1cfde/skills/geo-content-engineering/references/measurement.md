# Measuring success with Share of Mentions

A measurement algorithm that ties content rebuilds causally to brand presence in
generative answers.

## Why traffic fails as a KPI

Generative systems answer prompts inside their own interface, so users often get
what they need without clicking (zero-click). Measure presence in the answers
themselves, not visits.

## Lead metrics

- **Share of Mentions (SoM):** share of tracked prompts whose answers mention the
  brand. The central success metric for content rebuilds.
- **Share of Direct Citations:** share of prompts where the model links your site
  directly as a source.
- **Indirect Citations:** number of prompts where the model cites an external
  source that points to the brand (see `offpage-mentions.md`).

Prefer shares over absolute counts. The prompt pool shifts over time; percentages
stay comparable and protect the trend from distortion.

## The algorithm

1. **Keep an input register.** Record which URLs or sub-topics were rebuilt into
   chunk form and published, and when. Without this register you cannot attribute
   an SoM change to any action. The register entry is part of publishing.

2. **Build a representative prompt pool.** Per rebuilt topic cluster, define a
   limited, representative set of prompts with informational or transactional
   intent.

3. **Aggregate at the URL or cluster level.** Do not judge SoM per single prompt;
   bundle all prompts of a cluster. Aggregation links the operational work to the
   measurable result and shows whether the rebuild works systematically.

4. **Set up tooling.** Configure a tracking platform (Peec AI, Rankscale, SISTRIX
   AI Prompt Tracking, Otterly.AI) for daily collection. Terminology warning: the
   same metric is called "Visibility" in Peec AI and "Brand Coverage" in
   Otterly.AI. Keep an internal term mapping for reporting (see `glossary.md`).

5. **Benchmark competitors.** Track SoM for the relevant competitors on the same
   prompts. If your value rises while competitors stay flat, the effect is
   proven. Where a competitor is mentioned and your brand is missing, analyze
   that competitor's chunk quality.

## Risks and blind spots

- **Fragmentation.** The same prompt can return different answers depending on
  dialog context and session history, with or without a brand mention.
- **Sentiment automation.** Tools usually classify tone with word lists and get
  it wrong regularly. Plan for sample-based manual validation.
- **Position metric.** The position of a mention in an answer is worthless
  without context; first place can sit inside a warning list. Only Share of
  Mentions combined with validated sentiment is reliable.
- **Attribution gap.** Users see the brand in an AI answer and search for it
  directly later, without clicking. Web analytics cannot map that path, so
  measured ROI understates the real effect.
