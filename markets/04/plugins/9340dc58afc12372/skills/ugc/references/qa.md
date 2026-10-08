# QA before delivery

Run this before calling an ad finished. **Inspect the actual output** — do not claim
quality you haven't observed. If you could not inspect it, say so plainly rather than
implying you did.

## Blocking — fix or disclose

| Check | Fails when |
|---|---|
| **Product fidelity** | Colour, shape, finish or included parts differ from the source photo |
| **Presenter identity** | The face changed between segments, or differs from the chosen avatar |
| **Claim discipline** | Any claim outside the user's allowlist, or derived from one |
| **Testimonial framing** | The presenter implies purchase, ownership, results, or lived experience |
| **Rendered text** | Any baked-in letterforms — models garble text; captions come from `generate_video_captions` |
| **Aspect and duration** | Not what was asked, and the substitution wasn't disclosed |

## Quality — worth a regenerate

| Check | Fails when |
|---|---|
| **Hook strength** | The first 1.5 seconds open with a greeting, the brand name, or "in this video" |
| **Setting plausibility** | Staged to the point of reading as a commercial rather than a person |
| **Continuity** | A later segment re-greets or re-introduces the product |
| **Hands and faces** | Distorted extremities — the most common generation artifact, and the most visible |
| **Product visibility** | The product is small, occluded, or off-frame for most of the clip |
| **Pacing** | Dead air at the start or a close that trails off |

## What to report

State three things:

1. **What was produced** — format, duration, resolution, in plain words
2. **Anything substituted** — model, duration, resolution, and why
3. **What you could not verify** — if you couldn't inspect the frames, say that rather than
   asserting it looks good

## When a check fails

Follow `references/errors.md`. In short: pending jobs get waited on, technical errors get
at most two retries, unsupported capabilities get stated plainly, safety refusals are never
routed around, and every material change is disclosed.

**Never resubmit a generation that is still pending** — it bills twice for one result.
