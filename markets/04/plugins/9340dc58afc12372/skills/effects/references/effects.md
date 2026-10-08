# Effects preset library

Starter set. Each entry: what it looks like, then the generation settings.

Weave the user's actual subject into the prompt — these read as templates, not literals.

## Before you use any of these

- **Durations are per-model and silently fall back.** `ltx-2.3` accepts only 6/8/10;
  `wan-2.6` accepts 5/10/15; `seedance-2.5` accepts any whole second 4–30. A value outside
  the list becomes the model's default with no warning.
- **`seedance-2.5` image-to-video ignores `aspect_ratio`** — it adopts the source image's
  ratio. The `9:16` below is a target, not a guarantee. If the user needs true vertical,
  say the output follows their photo's shape, or use a model that honours the ratio.
- **Always pass `resolution`.** Omitting it renders at the model's *lowest* tier —
  `seedance-2.5` defaults to 480p. This is the single biggest quality lever here.
- **People are the common failure.** See "Model refusals" in `SKILL.md`.

---

## /zoom-punch — aggressive push-in
Hard, fast dolly toward the subject; motion blur at the edges; the subject stays locked.
- prompt: `rapid dolly-in toward {subject}, aggressive push, motion blur at frame edges, subject locked in centre, cinematic, high contrast`
- model: `seedance-2.5` · duration: `5` · resolution: `720p` · framing follows the source image
- fallback: `seedance-2.0` (duration `5`, resolution `1080p`)
- If the source shows a person, skip `seedance-2.5` entirely and open on `seedance-2.0`.

## /main-character — hero turn
Slow rise, subject turns toward camera, shallow depth, warm rim light.
- prompt: `slow rising camera, {subject} turns toward the lens, shallow depth of field, warm rim light, confident, cinematic portrait energy`
- model: `seedance-2.0` · duration: `5` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `ltx-2.3` (duration `6`, resolution `1080p`), then `pixverse-v6` (duration `5`, resolution `1080p`)
- **Person-centric.** Never use `seedance-2.5` here — it refuses human subjects, including illustrated ones.

## /liquid-melt — surreal morph
The subject dissolves and reforms in a fluid, glossy material.
- prompt: `{subject} dissolving into glossy liquid and reforming, fluid simulation, surreal, iridescent highlights, smooth loop`
- model: `seedance-2.0` · duration: `5` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `ltx-2.3` (duration `6`, resolution `1080p`)

## /orbit — clean 360
Smooth lateral orbit around the subject, even light, no cuts.
- prompt: `smooth 360 degree orbit around {subject}, even studio light, steady motion, no cuts, product-video quality`
- model: `seedance-2.0` · duration: `5` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `ltx-2.3` (duration `6`, resolution `1080p`)
- Best on products and objects — the safest preset in this set.

## /crowd-turn — everyone looks
Background figures turn to look at the subject; subject stays still.
- prompt: `background crowd turns to look at {subject}, {subject} remains still and centred, shallow focus, cinematic, dramatic`
- model: `seedance-2.0` · duration: `5` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `ltx-2.3` (duration `6`, resolution `1080p`)
- **Person-centric** (a crowd). Never `seedance-2.5`.

## /slow-burn — ember drift
Embers and haze drift past; slow push; deep shadows and warm key.
- prompt: `slow push toward {subject}, embers and haze drifting through frame, deep shadows, warm key light, moody`
- model: `ltx-2.3` · duration: `6` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `seedance-2.0` (duration `5`, resolution `1080p`)

## /glitch-cut — digital break
Datamosh and RGB split pulses on beat; subject re-forms clean at the end.
- prompt: `{subject} with digital glitch, datamosh and RGB split pulsing, resolving to a clean frame, high energy`
- model: `seedance-2.0-fast` · duration: `5` · resolution: `720p` · aspect_ratio: `9:16`
- fallback: `seedance-2.0` (duration `5`, resolution `1080p`)

## /drift — cinematic parallax
Gentle parallax as if the still were a 3D scene; almost imperceptible drift.
- prompt: `subtle 3D parallax across {subject}, gentle camera drift, depth separation between foreground and background, filmic`
- model: `ltx-2.3` · duration: `6` · resolution: `1080p` · aspect_ratio: `9:16`
- fallback: `seedance-2.0` (duration `5`, resolution `1080p`)

---

## Known model refusals

`seedance-2.5` rejects any source it believes "may contain real person" — **including
illustrated and cartoon characters**. Confirmed in live testing across three separate
uploads. Never open a person-centric preset on it.

Every preset above lists a `fallback`. Use it only for a clearly established unsupported
input capability, with **its stated duration and resolution**, and disclose the model
change and any duration or resolution change. On a safety or content refusal, stop and
offer a different subject; do not switch models to bypass it. If the reason is unclear,
stop and clarify it.

## Resolution ceilings (why model choice is a quality choice)

Omitting `resolution` gives you the **first** value, which is the lowest. Always pass one.

| Model | Allowed | Ceiling |
|---|---|---|
| `ltx-2.3` | 1080p, 1440p, 2160p | **2160p** |
| `veo-3.1`, `veo-3.1-fast` | 720p, 1080p, 4k | **4k** |
| `seedance-2.0` | 480p, 720p, 1080p | 1080p |
| `happy_horse` | 720p, 1080p | 1080p (requires an image — good for this skill) |
| `seedance-2.5` | 480p, 720p | **720p — lowest ceiling of the usable models** |

`seedance-2.5` has strong image adherence but caps at 720p. When output quality matters
more than adherence, prefer `seedance-2.0` at 1080p or `ltx-2.3` at 1080p+.
