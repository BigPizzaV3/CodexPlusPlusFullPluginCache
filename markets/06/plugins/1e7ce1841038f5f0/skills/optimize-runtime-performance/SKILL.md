---
name: optimize-runtime-performance
description: Measure and optimize a verified runtime bottleneck across browser, frontend, backend, API, database, network, asset loading, memory, startup, GPU, or interaction latency while protecting product behavior and visible quality. Use when performance is the primary measured problem. Do not use for vague requests to make code better, premature optimization, capacity planning without implementation, or changes that trade away approved design without authority.
---

# Optimize Runtime Performance

Improve the real bottleneck, not a fashionable metric or an assumed cause.

## Measurement contract

1. Define user-facing symptom, workload, environment, device or infrastructure tier, baseline, target, measurement method, variance, and acceptance.
2. Reproduce under controlled conditions and retain raw evidence.
3. Profile the relevant layer: browser main thread, rendering, network, assets, memory, GPU, server, API, queue, database, cache, startup, or interaction.
4. Identify the dominant constraint and competing hypotheses. Distinguish throughput, latency, tail latency, responsiveness, memory, energy, cost, and visual frame stability.
5. Reject optimization when evidence does not show a material bottleneck.

Use current authoritative tool documentation when commands, versions, or platform behavior are time-sensitive. Do not fabricate benchmark results.

## Authority and trade-offs

Apply the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md). Prefer changes invisible to product behavior and approved experience. Any optimization that changes visible fidelity, UX, correctness, consistency, security, durability, architecture contracts, or supported scope requires trade-off review and appropriate authority.

For realtime graphics, separate perceptual quality from frame-time metrics. A faster but visibly degraded experience is not a pass unless the degradation is explicitly approved. Use the shared [perceptual quality gates](../../shared/expert-system/perceptual-quality-gates.md).

For visual and realtime systems, read the shared [representation strategy contract](../../shared/expert-system/representation-strategy-contract.md). Optimize the representation and production boundary before accumulating runtime tricks: detail cost follows screen-space value, realtime must earn its cost, and a Source Master need not equal the published runtime asset. Changing representation or visible quality outside approved bounds remains an authority decision.

## Optimization loop

1. Make one evidence-backed intervention or tightly coupled set.
2. Measure with the same baseline method and representative workload.
3. Check statistical or practical significance and unintended shifts elsewhere.
4. Run functional, visual, security, data, and regression tests relevant to the change.
5. Keep, revise, or revert based on evidence.
6. Stop when target is met, gains are immaterial, risk exceeds value, or authority is required.

Do not cache incorrect data, remove safeguards, weaken consistency, lower image or rendering quality, skip work, or change user behavior merely to improve a metric.

When evidence identifies visual-runtime cost, test only relevant publishing tiers, render-lifecycle states and first-contact interventions. A tier may change internal cost without changing the approved experience. Resting, offscreen or hidden work may be reduced only when behavior remains correct. Precompile, prewarm, prefetch or preload only after measuring shader compilation, upload, decode, entry or first-interaction cost; include bandwidth, memory, energy and startup regressions. Do not introduce a generic tier/lifecycle framework for a local bottleneck.

## Output

Return baseline and environment, bottleneck evidence, hypotheses, implemented changes, before/after measurements with limitations, product and perceptual impact, regression results, cost effects, rollback, residual bottlenecks, and next highest-value action.
