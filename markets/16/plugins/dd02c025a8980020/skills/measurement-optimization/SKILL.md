---
name: measurement-optimization
description: Build honest measurement and optimization plans from defined objectives, sourced data, valid denominators, and bounded experiments.
---
# Measurement and Optimization

Use to assess performance or decide what to improve. No metric should be reported as observed unless a real source was supplied or accessed and its scope is clear.

## Define before measuring

- State the decision and objective, target behavior or outcome, metric definition, numerator, denominator, time period, source system, owner, and data limitations.
- Separate leading indicators, operational quality, customer outcomes, and business outcomes. Views, clicks, leads, sales, retention, and profit are not interchangeable.
- Identify baseline, tracking coverage, attribution limits, missing data, and privacy constraints. If no operating data exist, report **NOT MEASURED / UNKNOWN** and propose instrumentation rather than inventing a baseline.

## Analyze supplied data

1. Verify the file/table scope and definitions; do not silently repair or infer missing rows.
2. Recalculate figures when data allow, state denominator and date range, and distinguish raw counts from rates.
3. Segment only when sample size, consent, and purpose make it appropriate. Avoid unsupported causal conclusions.
4. Compare with a baseline or predeclared target only if they are comparable. Flag tracking changes, seasonality, and confounders.
5. Look for counterevidence, quality issues, and unintended effects; include uncertainty and alternative explanations.

## Optimize with controlled learning

Prioritize the largest evidence-backed uncertainty. Write a small experiment with one decision, hypothesis, audience/source, change, primary metric, guardrail metric, denominator, time window, stopping rule, and interpretation limit. Do not claim statistical significance or generalizability without an appropriate design and data. Preserve results even when they contradict the preferred idea.

## Figure handling

Flag any unsupported figure and identify the missing source. If an amount or rate is contradicted, state the discrepancy and provide a reliable correction when available. The user retains editorial control, but known-false data must not be represented as factual. Label modeled scenarios as scenarios, not results or forecasts.

## Standard output

Give the decision, metric definitions and evidence source, bounded findings, data-quality/attribution limitations, strongest contrary signal, recommended experiment, and what remains unknown.
