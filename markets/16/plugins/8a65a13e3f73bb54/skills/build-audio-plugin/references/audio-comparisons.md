# Controlled audio comparisons

Use one explicit hypothesis per comparison. Choose the smallest useful input,
control trajectory and acceptance rule before running it. This procedure does
not add a test host, audio analyser or arbitrary-source build path to Dispro.

## Make the comparison reproducible

Record the exact binary/package hashes, source/dependency identities, actual
loaded plugin, format, host/version, OS/architecture, sample rate, block schedule,
channel layout, state, seed if applicable, latency and render boundaries.
Retain the input and output PCM plus a small receipt. Verify that a reference
file contains real audio rather than a placeholder or missing large-file object.

Choose a signal that exposes the question: silence for leakage/startup, an
impulse for timing/tails, a tone or sweep for response, or fixed-seed noise and
an automation trajectory for time-varying behavior. Test the declared operating
range; do not automatically sweep every conceivable rate or buffer size.

Keep the same input, state, timing and build settings between comparisons except
for the one intentional variable. If stochastic/time-varying behavior prevents
sample equality, define the repeatability or statistical property being tested.
Mark uncontrolled differences as limitations rather than tuning until it passes.

## Choose the acceptance rule in advance

| Claim | Suitable comparison approach |
|---|---|
| Exact preservation | Sample equality/null difference when exactness is actually required |
| Floating-point equivalence | Predetermined absolute/relative tolerances with a near-silence rule |
| Response or envelope behavior | Declared level/frequency/time measurements and tolerance |
| Stateful or randomized behavior | Reproducible seed when available; otherwise declared statistics and bounds |
| Bypass/latency | Known alignment against dry input and explicit warm/startup/tail boundaries |
| Block-independent processing | Same signal and sample-timed controls under different valid partitions |

Report at least the chosen metric, threshold, measured result and context.
Include peak difference or another suitable worst-case measure when averages
could hide a click. Check finite output and unexpected clipping when relevant.
Do not silently normalize, shift, trim or discard startup/tail samples to hide
failure. Alignment must follow the known latency hypothesis, not a search for
the best-looking result.

## Keep failures useful

Retain the failed output and receipt. A later passing test closes only the claim
it actually exercises. API bypass and a host route that suspends AU rendering
are different cases; neither substitutes for the other. Normal editor/project
close and forced termination are also different outcomes.

When a sonic change is intentional, preserve the prior golden reference and
document the approved change, provenance and before/after result before creating
a new reference. Never regenerate goldens merely to turn a failing gate green.
Existing unchanged-wet controls should be reused; choose the next independent
control instead of exporting the same material again.

For optimization, compare the same build mode, signal, rate and block conditions,
and check sound as well as timing. Set a bounded warmup/repetition budget based
on the uncertainty being measured; do not enforce arbitrary universal run counts
or CPU promises. One platform's result does not qualify another.
