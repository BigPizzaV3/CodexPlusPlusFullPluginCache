---
key: mc-personal-behavioral-baselines
type: coaching
customer_visible: true
provenance: extension
source: "TeamOS/coaching-library/measurements/personal-behavioral-baselines.md"
last_verified: "2026-07-20"
---

# Coach Read: Personal Behavioral Baselines

Product measurement note: [[personal-baselines]]

## What this measures

A rolling per-person distribution of 11 conversational metrics (speaking rate, filler rate, response latency, turn length, backchannel rate, hedge rate, and others) over the last 20 sessions. This is not a score; it is the context that lets the report tell you whether a given session is normal or unusual for this person.

## What a high score means

There is no high or low here, only stable or not-yet-stable. After 10 or more recent sessions a person's baseline is stable enough to compute personal-deviation scores: this call's filler rate is one standard deviation above their normal, this latency is at their personal P25. Contribution to coaching is precision: generic norms wash out the individual; personal baselines make the change visible.

## What a low score means

With fewer than 4 recent sessions the baseline is too noisy to use, and the report falls back to corpus norms. Between 4 and 9 sessions the report blends the two. The opportunity for newer team members is simply more reps: as their session count climbs into double digits, coaching feedback gets dramatically more individualized.

## How the report uses this

Personal Behavioral Baselines is the substrate the report uses to mark sessions as personal outliers. It is not displayed as a primary number; it powers the "this is unusual for them" callouts wherever a metric appears in Sections 4 and 5.


## Related

[[personal-baselines]] · [[measurement-coach-index]] · [[research-home]]
