# Read an operator profile

The first sentence should say what is distinctive and what drives it. Examples of sound structures: high Yield from deep reuse rather than output intensity; high output with little cache reuse; context construction growing alongside reuse; a large ratio caused partly by a tiny input denominator. Do not turn those into judgments of the operator.

Read only reported pillars for the stated period. I is fresh input, O is generated output, W is cache/context creation, R is returned cached context. A missing pillar stays unknown. In particular, zero W is observed absence of cache writing for that period; null W means it was not observed.

Use the returned **operating ratio** as the compact headline for an observed token-flow shape. It is `cache-read : fresh-input : output` (`R/I : 1 : O/I`), displayed by the app with rounded terms. For example, `19:1:0.09` means roughly 19 cache-read tokens and 0.09 output tokens per one fresh-input token for that period. The first term is rounded Leverage; the last is rounded Velocity. It does **not** include cache writing. State W separately and, when R>0, use Construction = W/R to describe how much new context was created relative to reuse. Never reverse the ratio, treat its parts as percentages, or recompute an exact metric from the rounded display string.

The public profile's I/O/W/R are **aggregate token counts**, not per-turn raw telemetry. For a deep read, show observed counts and denominator, compute shares of total only when all four pillars are present and comparable, and then explain how the mix produces the ratios. If a pillar is missing, do not construct a complete composition chart or infer a zero. The plugin has no access to prompt content, private local logs, or a session-level timeline.

Use canonical deterministic metrics:

| Name | Expression | What it can support |
|---|---|---|
| Leverage | R/I | Relative reuse of prior context |
| Velocity | O/I | Relative generation volume |
| Yield / Υ | R×O/I² = Leverage×Velocity | Joint reuse-generation token-flow structure |
| SNR / output_fraction | O/(I+O) | Output share of fresh input plus output |
| Construction | W/R | Cache writing relative to cached reading, when R>0 |
| 10xDEV / log_leverage | log10(R/I) for positive complete pillars under TTEOP reference policy | Log-scale reuse; omit on missing/zero boundary pending policy resolution |

All ratios are descriptive, not utility scores. Absolute activity volume does not establish a better operating structure. If I is tiny, explicitly show that ratios can become extreme without establishing stable behavior.

The current app's ten Build Archetypes classify a complete operating composition with precedence: Convergent (>74.6 leverage, >0.34 velocity, >0.0431 construction), Kinetic (velocity ≥0.8), active construction (construction ≥0.02: Builder if leverage <30, Recursive 30–<50, Amplifier ≥50), otherwise passive reuse depth (Input-bound <5, Priming 5–<10, Contextual 10–<15, Deep Reader 15–<23, Archivist ≥23). These are current implementation thresholds calibrated against a historical field cut; do not claim permanent normative status. Explain the decisive axes and precedence when a result could look like two types. Prefer the canonical `archetype` and `archetype_details` returned by the analyst tool. Explain its `description` and decisive `axes`, retaining the selected snapshot/window. `classifier_id` and `classifier_version` pin its implementation; `origin=computed_from_snapshot` identifies how the label was produced. If an older tool still returns null, a complete I/O/W/R calculation may be introduced as **derived under the packaged rules**, rather than a returned profile property. Missing W or R, or zero I/R denominators, means no full assignment; observed zero W remains a valid classification input. Read [archetype teaching](archetypes.md) for the detailed wiki and article connections.

Class tiers and ranks are separate from the Build Archetype. Do not call the ten archetypes ten classes. The older `operator_signature()` output is not the same taxonomy.

Field-relative language requires a named cohort, as-of date, window, denominator and compatible metric definition. If any are absent, describe the single profile without a percentile or rarity claim. A historical median can be cited as dated, cross-cohort context, never as a current percentile or rank.
