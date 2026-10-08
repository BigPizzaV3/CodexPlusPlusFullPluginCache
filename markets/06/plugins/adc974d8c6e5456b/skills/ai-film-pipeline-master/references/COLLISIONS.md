# COLLISIONS — same-tier disagreements, and what was chosen

[`PRECEDENCE.md`](./PRECEDENCE.md) §3 says that when two cards land on the same tier the order is
silent, the choice belongs to whoever is holding the shot, and the choice is to be recorded rather
than closed. Until this file existed there was nowhere to record it, so the instruction asked for
something the package could not do and the collisions went unwritten.

This is that place. It is a log, not a rule file. **Nothing in here outranks anything.** A row says
what one person chose, on one piece, on one day, and the next project may choose the other way for a
good reason. The value of the log is entirely in the repetition: a pair that appears here three times
is telling whoever maintains the package that it is missing a distinction. During a run nothing here
is asked of the user: the run chooses, records the choice under `decisions` in `project.yaml`, and
carries on; rows are added here when the package itself is maintained.

**Add a row when** two cards you were actually holding landed on the same tier, could not both be
obeyed, and you chose. **Do not add a row** for a pair the tiers already separate, for a pair where
one card's own **Avoid when** line puts your case outside it, or for a collision you think might
happen one day. The log records collisions that were met, not collisions that were imagined.

**When a row becomes a card field instead.** The same pair, in the same case, choosing the same way,
**three times** — at that point it has stopped being a judgement and become a rule, and it belongs on
the cards as the `**Outranks:**` / `**Yields to:**` fields in [`PRECEDENCE.md`](./PRECEDENCE.md) §4,
with the case written into the card's prose as well. Whoever maintains the package writes it; the
rows stay here afterwards as the evidence the field was earned rather than assumed. A pair that keeps
being decided *differently* is the opposite finding and is never promoted — it means the case has not
been named finely enough yet, which is package maintenance and never a question during a run.

---

## The log

| Date | Card A | Card B | Tier both read at | The case | What was chosen, and why | Who chose it |
|---|---|---|---|---|---|---|
| not recorded — settled before this log existed | `comp.safe_areas` (Phase 6) | `vertical.safe_zones` (Phase 7) | 2 — delivery reality; both describe the surface the piece lands on | A vertical piece where both cards name margin numbers for the same frame, and the storyboard and the keyframe were being composed to two different sets | `vertical.safe_zones`, as the single carrier of the actual vertical numbers. **This column names the owner and does not repeat the figures** — it used to quote all three, which made the file that settles ownership into a fourth copy of the value, and it held a wrong figure until September 2026. `comp.safe_areas` keeps the principle and owns the *broadcast* numbers, so one number lives in one place and the board and the still agree | not recorded |
| not recorded — settled before this log existed | `kids.turn_to_camera` (Phase 3) | `expo.kids_repetition_ladder` (Phase 1) | 3 — audience fit; both are comprehension rules for the same child | A direct-address question to camera that is also the teaching ask of a repetition ladder, where the two cards set different lengths for the same silence | `expo.kids_repetition_ladder` for the length of the silence, because its reason is that a child not given long enough to answer has not been taught. `kids.turn_to_camera` keeps only the on-lens hold inside that silence, which is a shot decision and may be shorter if something covers the rest | not recorded |
| not recorded — settled before this log existed | `scene.chaos_to_silence` (Phase 3) | `cut.to_silence` (Phase 3) | 3 — audience fit; both are about what a viewer makes of a silence | A hard cut from peak noise into silence, where one card sets a five-second floor and the other a three-second ceiling | `cut.to_silence` and its three-second ceiling **only where the silence is truly digital and no bed survives**, past which the viewer reads a playback fault rather than a beat. Where wind, a ringing tone or room tone survives, the five-second floor of `scene.chaos_to_silence` stands. The split is by whether a bed survives, not by which card is stronger | not recorded |

**On the three rows above.** All three were found already settled inside the cards themselves, as
`**Yields to:**` fields with the case named — which is the endpoint this file describes, reached
before the log existed. They are seeded here so the shape of a row is shown with real pairs rather
than with invented ones, and so the promotion path has visible precedent. Neither the date nor the
decider survives in the record, and both cells say so rather than guessing. **A new row fills both.**

---

## The shape of a row

Copy this and fill it. Seven cells, and none of them is optional.

```
| YYYY-MM-DD | `a.card_id` (phase) | `b.card_id` (phase) | the tier both read at, and why |
the case, named narrowly enough that someone else can tell whether their shot is in it |
what was chosen, and the reason in the piece — the format, the platform, the audience, what the
shot was for | who chose it |
```

Three things that make a row worth having:

- **Name the case narrowly.** *On a vertical piece* is not a case; *on a vertical piece where the
  board and the keyframe were being composed to two different margin sets* is. A reader has to be
  able to tell whether their shot is the same shot.
- **Give the reason in the piece, not in the order.** The tiers are silent here by definition, so
  a row that says *chose A because A is more important* has recorded nothing. Say what about this
  project decided it.
- **Word it as a choice.** [`PRECEDENCE.md`](./PRECEDENCE.md) §3 is explicit: *"`a.card` and
  `b.card` are both tier 3 and disagree here; chose `a.card` because the piece is a phone-first reel.
  The order does not settle this."* A row worded as a rule will be read as one by the next person,
  and that is exactly the invented tie-breaker [`PRECEDENCE.md`](./PRECEDENCE.md) §3 forbids.
