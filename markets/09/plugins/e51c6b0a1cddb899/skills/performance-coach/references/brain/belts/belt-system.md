---
key: belt-system
type: belt
customer_visible: true
provenance: traceable
source: "belt-ground-truth.md (calculate_belt_progression, rs_belt_thresholds); CardHelpProvider.tsx#belt-system (descriptions only)"
last_verified: "2026-07-18"
---

# The Belt System

RapportScore uses a martial-arts-inspired belt system to guide your development through six progressive levels: [[white-belt]], [[yellow-belt]], [[blue-belt]], [[purple-belt]], [[brown-belt]], [[black-belt]]. Each belt is a genuine milestone, earned through measured performance on real calls plus completed training. Belts describe your whole rapport skill, never a single dimension: a dimension can have a score, but only your overall development has a belt.

## How promotion works: the three-gate model

Promotion is measured server-side after every completed lesson or roleplay, and it happens automatically the moment all three gates pass. There is no button to click and nothing to claim.

**Gate 1, Score.** All seven Rapport Dimensions ([[responsiveness]], [[active-listening]], [[mirroring]], [[emotional-acknowledgment]], [[curiosity]], [[trust-building]], [[engagement]]), averaged over your recent completed calls since your last promotion, must each clear the next belt's bar:

| Next belt | Every dimension must average at least |
|---|---|
| Yellow | 50 |
| Blue | 65 |
| Purple | 78 |
| Brown | 85 |
| Black | 89 |

One uniform bar per belt, applied to all seven dimensions. Your weakest dimension is what gates you.

**Gate 2, Training.** Every lesson at your current belt is completed with a passed Ask Alex roleplay **on RapportScore.ai**. A lesson passes at its own belt's score bar (White-belt lessons are floored at 50). Coach-side or agent roleplay does not replace this gate; see [[lesson-credit-and-practice]].

**Gate 3, Consistency.** Two parts: a minimum number of completed calls since your last promotion (White to Yellow 4, Yellow to Blue 6, Blue to Purple 6, Purple to Brown 8, Brown to Black 10), and a qualifying streak: your most recent consecutive calls (2 / 3 / 3 / 4 / 5 respectively) must all clear every one of the seven bars.

When all three gates pass, the promotion is recorded automatically and your progress resets toward the next belt.

## What belts change

- Higher belts unlock harder lessons: advanced content is not visible at lower levels.
- Lesson pass bars rise with the belt, so training difficulty tracks your level.
- Score displays are belt-aware, so growth stays visible at every level.

## About points

You do earn points for lesson videos, roleplays, and milestones. Points feed achievements and progress displays. Points do not gate belts: no point total promotes you, and no promotion is claimed manually. If you see an older description of a points ladder, the three-gate model above is what the product actually does.

## FAQ

**Why has my belt not moved when my average score is high?**
Belts gate on every dimension, not the average. One dimension below the bar holds the gate, as does an incomplete lesson or a streak that has not yet reached the required length. Ask the coach "what's blocking my next belt" for the specific gate.

**Can a bad call drop my belt?**
No. Promotion only moves forward. A rough call can extend the time to your next promotion by breaking a qualifying streak, but you never lose a belt you earned.

**Can my manager or coach promote me early?**
No. Belts are measured, not granted. The coach reads the data and cannot change it.

## Related

[[white-belt]] · [[yellow-belt]] · [[blue-belt]] · [[purple-belt]] · [[brown-belt]] · [[black-belt]] · [[determinism-and-gaming]] · [[score-bands]] · [[session-types]]
