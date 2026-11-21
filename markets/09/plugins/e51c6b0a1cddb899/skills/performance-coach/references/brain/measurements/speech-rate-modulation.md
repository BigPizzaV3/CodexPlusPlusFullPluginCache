---
key: speech-rate-modulation
type: measurement
measurement_key: speech_rate_modulation
dimension: Mirroring
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#speech-rate-modulation; CardHelpProvider.tsx#pace-alignment; CardHelpProvider.tsx#communication-overview; registry"
last_verified: "2026-07-18"
---

# Speech Rate Modulation

## What it measures

Each speaker's words-per-second across time buckets, and whether the rates converge. A Pearson correlation between the speakers' rate curves summarizes the call: converging rates are a rapport signal, diverging rates can indicate mismatched energy. Research anchor: convergence of speech rate in conversation predicts cooperation (Manson, Bryant, Gervais and Kline 2013).

## Where you see it

The Speech Rate Modulation chart (per-speaker curves, bucket selector 30s to 240s), the Pace Alignment card (your WPM versus theirs), the speed arrows on Communication Timeline bars (an utterance faster or slower than that speaker's own baseline), and WPM rows in Speaker Statistics.

## How to read your number

- Correlation chip: r of 0.4 or above means converging (both speakers adjusting to each other in real time); r of -0.4 or below means diverging, for balanced calls. For primary-led calls (demos, pitches, one speaker at 75% or more), negative r is normal delivery structure and the divergence alert is suppressed.
- Pace Alignment: within 20 WPM of each other is "Aligned", which is associated with rapport. Larger gaps may signal mismatched energy or comfort.
- Absolute pace bands in shipped copy vary by card and are flagged for reconciliation: 140-180 WPM optimal (Communication Overview), 120-150 comfortable (Performance Dashboard), 120-160 comfortable (Pace Alignment), with above 200 risking losing listeners. The safest read is your own baseline plus the gap to your counterpart.
- Acceleration runs in the final third of a call can indicate pressure to close; the chart shades those runs so you can review the transcript there.

## What moves it

- Listening to their cadence for ten seconds, then matching it.
- Slowing down on complex topics; speeding up slightly when energy drops.
- Pausing after key points instead of accelerating through them.
- Stress moves it the wrong way: speeding up after complexity or objections is the most common tell (a positive WPM change after pressure moments).

## Drills

- Deliberate downshift: pick your next call's final third and consciously slow after each key point. Check for acceleration runs afterward. See [[drills-library]].
- Ten-second cadence read before your first substantive turn.

## FAQ

**I naturally talk fast. Is that a problem?**
Not by itself. The rapport signal is convergence, not an absolute speed. Fast-with-fast is aligned; fast-against-slow is the gap worth closing.

**Why did the chart ignore my demo's divergence?**
Call shape. Primary-led calls have structural divergence, so the card treats the correlation as descriptive rather than a rapport alarm there.

## Related

[[mirroring]] · [[entrainment]] · [[language-style-matching]] · [[timing-critical-moments]] · [[personal-baselines]] · [[drills-library]]
