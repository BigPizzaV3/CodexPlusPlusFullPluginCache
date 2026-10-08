# Temporal usability and long-running controls

## Specify the user-visible promise

For a timer, transfer, irrigation run, media command, or queued operation, write the whole journey: initiate, receive feedback, monitor, leave and return, find the running operation, stop/cancel, and observe completion or failure. Decide where persistent status belongs and how many actions recovery should require from the actual design. Do not invent a requirement that every route must display a timer if the product intentionally uses a dedicated reachable status view.

For each phase separate four claims: the model says it is running; a DOM element exists; the user can perceive status in the current viewport; the user can reach and operate the relevant control. Prove the claims that matter to the task. The presence of `_timer`, a deadline in storage, or text in a hidden node proves none of the latter two.

An illustrative timer journey: tap Start once; inspect feedback immediately; watch several real elapsed seconds; scroll; open and dismiss a sheet; navigate away; return; verify the same deadline and a reachable Stop action; tap Stop; verify countdown and expiration callback cannot reappear after redraw or reload. Run expiry in a separate case. When pausing is unsupported, exclude it explicitly rather than failing a nonexistent control or pretending it ran.

## Measure visibility and reachability

Use `helpers.inspect(path)` for deep active focus, selection, serialized bounds, CSS/ancestor visibility, inert state, visual viewport intersection, and five sampled hit locations. `viewportFraction` measures rectangular viewport intersection only. `sampledHitFraction` measures whether the target or its descendant receives events at the sampled points; it is useful for interactive controls. Neither is a full pixel visibility measure. Rounded masks, filter effects, transformed clipping, obscuring transparent layers and assistive technology require additional evidence. Passive status text with `pointer-events:none` can be visible even when it fails hit testing.

Inspect screenshots at start, after the initial feedback disappears, after scroll/modal/navigation, and at failure. Cross-check displayed remaining time, text contrast/readability, clipping, layering, and user-reachable cancel control. Do not equate an automation framework's `visible` predicate with human visibility; Playwright's definition, for example, permits zero opacity. Use a specified design-appropriate visible fraction and hit requirement instead of an unexplained magic threshold.

Measure layout viewport and visual viewport separately when the keyboard/zoom changes them. Browser viewport shrink can test responsive layout; it is not real iOS keyboard, safe-area or WKWebView proof. Observe genuine supported input methods and document device gaps. Preserve pinch zoom and normal scrolling unless the intended control contract requires otherwise.

## Sampled temporal assertions

Use two kinds of expectation: `always` for an invariant that must remain true at every sampled observation, and `eventually` for a result that must arrive within a bounded observed interval. Do not use an eventual-passing assertion for focus retention or avoiding duplicate writes. If focus disappears and later returns, the always-held contract still failed.

`helpers.sample(path,{durationMs,intervalMs})` takes bounded, monotonic real-time snapshots without scrolling the control into view. It reports actual timestamps. A missing or ambiguous target throws; classify it and preserve evidence, do not turn it into an empty passing sample list. To measure several related controls/model fields atomically, implement a target-specific observation collector using one page evaluation and record its timing. To capture transient disappearance, include DOM mutation/route events and screenshots through an owned fixture observer, then remove the observer. Do not install live-device instrumentation from this workflow.

`assessTemporalTrace({samples,durationMs,maxGapMs,timeDomain,requirements})` refuses malformed timestamps, empty requirements and evidence-free oracle answers. Each requirement has `id`, `mode:'always'|'eventually'`, and `check(observation)` returning `{pass,evidence}`. Insufficient duration, fewer than two samples, or gaps larger than the declared limit yield inconclusive sustained evidence if no violation was observed. A real observed violation remains failed despite other sampling gaps. Record the interval and largest actual gap. Even a passing trace establishes only its sampled window, not continuous behavior between samples.

## Clock and background behavior

Name the time domain: monotonic real time for intervals/latency, wall time for civil schedules and absolute deadlines, virtual time for controlled boundaries. Do not mix different page time origins or turn a wall-clock rollback into a malformed monotonic trace. Set initial time/timezone before app initialization when necessary.

Where the permitted installed browser supports Playwright Clock, install it before timer-related calls. Fixed wall time and fake scheduler installation have different effects. Exercise `t-1`, `t`, and `t+1` around expiry, cancellation concurrent with expiry, clock forward/backward, midnight/DST where relevant, delayed callbacks, resume after suspension, and multiple overlapping timers. Confirm documented API semantics against the installed version. The Browserless starter does not implement a fake clock automatically; use supported native facilities or a reviewed fixture-only extension and label that evidence.

Keep a real-time countdown smoke test alongside accelerated cases. Virtual-time success does not prove background execution, native notification delivery, audio, locked-screen behavior or mobile battery suspension. A timer can legitimately reach its absolute deadline while the app is suspended, but the recovery UI and stale-alarm policy still need explicit testing. Track expiration/cancellation counts by stable timer ID so redraws, reloads or duplicate subscriptions cannot silently produce two completions.

For a completion toast or animation that should disappear, use a bounded presence-then-dismiss contract, not an always-visible contract. For a running status that disappears unexpectedly, capture both the last good and first bad sample and correlate app state, route, scroll, CSS and callbacks. Report the evidence resolution rather than asserting an exact disappearance time the sampling cannot establish.
