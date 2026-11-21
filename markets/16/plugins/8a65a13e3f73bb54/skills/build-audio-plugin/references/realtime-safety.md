# Processing and ownership review

Use this checklist on the changed processing path, not as a claim that a source
scan establishes real-time safety. No new audio implementation is included here.

Map the audio callback, UI/message thread, background work and object lifetimes.
For each piece of shared state, identify its writer, readers, publication point,
ownership and destruction thread. Check called helpers and library operations,
not only the visible callback body. An atomic variable alone does not prove that
the whole publication path is lock-free or safe on the target platform.

Prepare buffers and processing resources outside the audio callback. Keep
allocation/free, blocking synchronization, file/network access, UI calls and
unbounded logging/work off that path. Watch indirect work: container growth,
lazy initialization, callbacks and last-owner destruction. Define how bounded
queues behave when full; a real-time producer must not wait indefinitely.

State must evolve according to the intended time base. Handle actual sample
count, declared channel layouts, in-place processing and supported sample-rate
changes. Test block-size independence only where the design promises it, using
the same time-based control trajectory. Treat zero-length callbacks according
to the relevant interface contract; do not access samples that are absent.

For transitions, distinguish UI display smoothing, control publication, DSP
parameter ramps, dry/wet gain changes and replacement-engine warmup/crossfade.
Choose a policy suitable for each parameter; not every discrete mode can be
interpolated. Record startup, reset, bypass and return-to-wet behavior. A smooth
knob animation does not establish click-free audio, and a large crossfade patch
does not establish the cause of an audible failure.

Consider nonfinite values, extremely small signals and feedback stability where
they are relevant. Make the handling policy explicit without importing another
product's limits or sonic tuning. Distinguish defensive behavior from claimed
support for otherwise invalid inputs.

Use the narrowest useful checks: source review for ownership, isolated tests for
bounds/state, instrumented execution for allocation/races when available, and
exact-binary host/audio checks for acceptance. Keep instrumentation overhead and
sanitizer scope explicit. Passing mock fixtures, a compile, or average CPU
measurement does not prove absence of races, glitches or deadline misses.

Editor/browser teardown follows `engineering-lessons.md#teardown-order` and
`#webview-lifetime`. The historical Windows renderer issue remains separate;
do not introduce the unconsumed `JUCE_DIRECT2D` define as a safety fix.
