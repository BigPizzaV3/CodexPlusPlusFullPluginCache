---
name: segmind-faceswap
description: >
  Swap a face into a video or an image with Segmind, using a reference photo of
  the face to put in. Use when the user wants someone's face put onto footage or
  a picture, a character recast, a cameo inserted, or a face replaced — including
  as a follow-on step after upscaling or generating a clip. Do not use for
  changing an expression, for reposing or restyling a person, for generating a
  talking avatar from a photo, or for anything involving a real person who has
  not consented.
---

# Face swap with Segmind

Read [pixelflow-contract](references/pixelflow-contract.md) and
[inference-contract](references/inference-contract.md) first.

## Consent gate — check this before anything else

A face swap puts a **real, identifiable person** into footage they were not in.
Before running one, the user must be swapping a face they have the right to use:
their own, a consenting subject's, or a synthetic face.

If the target or the source looks like a public figure, or the request is
framed around making someone appear to say or do something, **stop and say
plainly that you will not make that** — a convincing video of a real person doing
something they did not do is the harm, whatever the stated purpose. Offer a
synthetic face instead. Do not negotiate the point across turns.

This is a hard gate, not a disclaimer to append to the output.

## Set expectations first — this is not a reliable identity swap

Measured on a real pair (a studio portrait as the source, a period film still as
the target): the swap ran, completed and billed, and the output face came back
**softened and slightly altered but still recognisably the original person**, not
the reference. All three `model_name` variants (`hyperswap_1a`, `1b`, `1c`) gave
the same result, at two different detector thresholds. The enhancer was ruled out
— swap-only output is equally weak.

The likely cause is the distance between the two faces: pose, framing, lighting
and face size all differed sharply. So:

- **Tell the user this may not transfer the identity convincingly**, before
  running it, rather than presenting the result as a finished swap.
- **Match the pair as closely as you can** — a source photo shot at a similar
  angle, similar lighting, and with the face at a similar size in frame is the
  single biggest lever available.
- **Run one short clip and show it** before spending on length or resolution.
  Never batch this.

Do not describe the output as "your face swapped in" without the user having
looked at it.

## Models

| Job | Model | Cost |
|---|---|---|
| Face into a **video** | `video-faceswap-by-facefusion-labs` | GPU-time billed at $0.0072/s; runs average **~$0.10 in ~67s** |
| Face into an **image** | `faceswap-v5` | $0.05 flat |

GPU-time billing scales with clip length and frame rate, so the average above is
a starting point, not a quote — a long or high-fps clip costs well past it.

Video: `source_image` (the face to put in) + `target_video` (the footage).
Image: `source_image` + `target_image`.

**The names are the trap.** `source_image` is the face being *inserted*, not the
footage being changed. Swapping them silently produces a result that looks
almost right, so state which is which back to the user when you run it.

Useful optionals on the video model: `model_name` (`hyperswap_1a` is the
default and works), `face_detector_score` (lower it below 0.5 if the face is not
being found), `target_face_index` (which face in a multi-person shot, 0-based).

## After upscaling

**Swap first, then enhance.** Two ways to get there, and they do not cost the
same:

- **The two models, in order.** `video-faceswap-by-facefusion-labs`, then
  `segmind-video-upscale` on its output URL. This is the cheap route and the
  one to reach for by default.
- **The `face-swap-studio` flow** — inputs `video`, `face`, `scale`; output
  `video_out`. One call, but ⚠️ **its swap node is `videofaceswap`, not the
  HyperSwap model priced above** — a different model that averages **~$1.14 and
  ~300s** against HyperSwap's **~$0.10 and ~67s**. Roughly 11x the cost for the
  convenience of one call. Price the flow from its own `models` list
  (`get_pixelflow_spec` → `compare_models`), never from the table above, and do
  not reach for it just because it is one step.

The flow also pins the target face to index 0 internally and does not expose it.
For a multi-person shot where the face to replace is not the first one detected,
run `video-faceswap-by-facefusion-labs` directly with `target_face_index`, then
enhance its output with `segmind-video-upscale`.

### The enhance step is not cosmetic, and the order is not arbitrary

Measured on one 5s clip, with sharpness taken **after resampling every output
back to 768x512** so resolution cannot flatter the result:

| Variant | Dims | Mbps | Sharpness @768x512 |
|---|---|---|---|
| source, no swap | 768x512 | 0.74 | 30.7 |
| swap only | 768x512 | 0.63 | **28.7** |
| **swap → enhance** | 1536x1024 | **10.17** | **86.5** |
| enhance → swap | 1536x1024 | 2.45 | 83.7 |

Two things to take from this:

- **The swap softens the footage** (30.7 → 28.7). Enhancing afterwards does not
  merely enlarge it — detail survives a round-trip downsample at ~3x the source,
  so the enhancer is reconstructing real high-frequency content.
- **Whatever runs last sets the bitrate.** Putting the swap last re-encodes at
  the swap model's own bitrate and throws away four fifths of the enhancer's
  headroom (10.17 → 2.45 Mbps) for almost identical sharpness. That is the real
  reason to enhance last.

Cost barely moves either way — the swap on pre-upscaled frames is only **+6%
cost / +9% time**, because its GPU time is dominated by per-frame detection at a
fixed working resolution rather than by input pixels. So order for the bitrate,
not for the money.

**On the two-model route the enhance dominates the bill**, at $0.05 per input
video-second against ~$0.10 for the whole HyperSwap. Quote the total, and pass
`scale: 4` — it costs the same as 2 (see `segmind-video-upscale`). On the
`face-swap-studio` flow that ordering reverses: its `videofaceswap` node
averages ~$1.14 and is then the larger half of the bill by far.

Run it as **two steps** instead when the user should see and approve the swap
before paying for the enhance: `submit_inference` the swap, show it, then
`segmind-video-upscale` on its output URL.

## Workflow

1. **Consent gate** (above). Then get URLs for both inputs. The face photo is
   almost always a file on the user's disk — run it through `upload_media`
   (contract rule 4) without asking, and do the same for the footage if it is
   local too.
2. **Say which image is the face and which is the footage**, so a swapped pair
   is caught before it is billed rather than after.
3. **Submit, then poll in this turn** — a face swap is per-frame work and scales with clip
   length; poll it in-turn rather than using `run_inference`.
4. **Deliver** the output URL and the total cost.

## Rules

1. **Consent first, every time.** No exceptions for "it's a test" or "it's for
   fun".
2. **`source_image` is the face going in.** Restate the mapping before running.
3. **One clip first.** Confirm the swap looks right on a short clip before
   running it over long footage.
4. **A face that is not detected is not a model failure.** If the swap comes back
   unchanged, lower `face_detector_score` or set `target_face_index` before
   declaring the model broken.
5. **Never `run_inference`.** Submit, then poll in-turn until terminal — do not
   end the turn on "queued".
