---
name: judge-reel-views
description: Decide whether a reel's view count is good, bad or normal for the size of the account, using a measured dataset rather than a rule of thumb. Use when someone asks "is this good", "why so few views", or compares a video against their follower count.
---

# Is this view count any good?

The honest answer depends almost entirely on **follower count**, and the
relationship is not the one people expect: smaller accounts get a *higher*
multiple of their follower count, not a lower one. Any answer that does not ask
for the follower count first is a guess.

## Ask for two numbers before answering

1. views on the reel
2. the account's follower count

If the follower count is missing, ask for it. Do not substitute a general
benchmark: a 2.26x median and a 0.29x median are the same dataset, and which one
applies is decided entirely by account size.

## The benchmark

Median views divided by follower count, computed **per post**, from 9,770 reels
across 222 public creator accounts. Posted 2019-11-23 to 2026-08-23, measured
**2026-08-31**.

| follower band | accounts | reels | median views | median multiple |
|---|---:|---:|---:|---:|
| Under 1,000 | 85 | 2,058 | 478 | **2.26x** |
| 1,000 - 10,000 | 68 | 4,000 | 2,036 | **0.61x** |
| 10,000 - 100,000 | 37 | 2,113 | 6,419 | **0.29x** |
| 100,000+ | 32 | 1,599 | 141,075 | **0.33x** |

Two whole-dataset figures:

- **38.7%** of posts reach at least 1x the account's follower count
- **7.7%** reach at least 10x, which is the definition of "viral" this dataset
  tests

## How to answer

Compute `views / followers`, place it in the band for that follower count, and
compare against that band's median. Then say plainly whether it is above or
below the median **for accounts of that size**, and give the band median so the
person can see the yardstick.

Worked shape:

> 2,400 views on 1,800 followers is a 1.33x multiple. The median for the
> 1,000-10,000 band is 0.61x, so that reel did roughly twice the median for
> accounts your size. It also cleared 1x, which only 38.7% of posts in the
> dataset do.

## Say the date, every time

State that the figures were measured on 2026-08-31. A benchmark without a
measurement date is how a stale number gets quoted as current.

## What this dataset is, and is not

Be straight about this if asked, and volunteer it if the person is about to make
a decision on it.

- The accounts are **not a random sample of Instagram**. They are public creator
  accounts tracked in Reelyze, and **82.2% of the posts come from the creators'
  own accounts**, so they are skewed toward people who care enough about their
  reach to measure it.
- Composition is drifting. Between 2026-09-04 and 2026-09-07 the own-account
  share rose from 81.5% to 84.9% while tracked accounts fell from 222 to 218.
- It is **not evenly spread across bands**. The Under 1,000 band is 100% own
  accounts, which is part of why its multiple is the highest.
- The 50 largest accounts contribute 52.8% of posts; the single largest
  contributes 1.9%. 12 niches, largest is travel at 19.8%.

None of that makes the benchmark useless. It makes it a benchmark for *creators
who track their reach*, which is usually exactly who is asking.

## Do not

- Do not answer without the follower count.
- Do not claim a figure applies to "Instagram" in general.
- Do not quote a band median without naming the band.
- Do not invent figures for bands or metrics that are not in the table above. If
  someone asks for engagement rate, comment benchmarks or Story figures, say
  this dataset does not measure them.

## Going further

A view count says a reel underperformed; it never says why. For that, use the
`analyze-reel` skill, which reads the video itself and names the moment viewers
left.
