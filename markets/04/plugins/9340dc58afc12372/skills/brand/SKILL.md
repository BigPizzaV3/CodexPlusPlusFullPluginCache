---
name: brand
description: Logos, animated logo reveals, and full visual identity — palette, typography pairing, and brand applications. Use when the user is establishing or refreshing a brand, or wants a logo. Not for a single social graphic (use Social Studio).
---

# Brand Studio

Read `references/identity.md` for the identity method.

> **Partly implemented.** `generate_logo` and `generate_3d_logo_animation` are real tools.
> Palette generation, typography pairing and brandbook export are **not built server-side**.
> Produce those as structured text plus generated sample imagery, and say plainly which
> parts aren't exportable as files yet. Never imply a downloadable brandbook exists.

## Tokens

| Token | What it does |
|---|---|
| `/logo` | Static mark — three directions |
| `/logo-reveal` `/logo-3d` | Cinematic 3D animated reveal |
| `/palette` | Colour system with roles |
| `/typography` | Display + body pairing |
| `/brandbook` | The full identity, assembled |

## Truth gate — claims

- **The claims the user supplies are the complete allowlist.** Preserve each as written.
  Never strengthen, combine, or infer a new claim from them.
- **With no claims supplied**, write only about what is directly observable — materials,
  controls, how it is used, what is included.
- **No superlatives you cannot support** — "best", "revolutionary", "#1". They read as
  advertising and fail on review.
- **No comparison to a named competitor.**

## Logos

`generate_logo`. Ask for exactly three things: the **name**, what the **business does**,
and any **style direction**. If they gave the first two, infer the third and say what you
assumed. Don't run a questionnaire.

**Generate three distinct directions, not one.** Logo choice is comparative — name what
distinguishes each in a line.

## Logo reveals

`generate_3d_logo_animation` takes `logo_image_url` and runs the whole recipe in one call:
it converts the flat 2D logo to 3D (nano-banana-2), waits, then animates the reveal
(veo-3.1-fast).

**It blocks for up to a minute before returning.** Say so before calling it, or the wait
reads as a hang.

### When the reveal fails — observed recovery

`generate_3d_logo_animation` is a two-stage pipeline: 3D still first, then animation.
**Stage two can fail after stage one succeeded.** Observed in testing, along with what
actually worked:

| Attempt | Result |
|---|---|
| Full pipeline | 3D still succeeded, animation failed |
| Retrying the full pipeline | Timed out |
| Animating the **original** logo directly with `ltx-2.3` | Completed |

So the recovery, in order:

1. **Do not blindly re-run the whole tool.** Stage one already cost time and credits, and
   re-running it is what caused the timeout.
2. **Retry the full pipeline at most once.** If it fails again, stop retrying it.
3. **Fall back to direct animation:** `generate_video` with the logo as `image_url`
   (exactly one URL), `ltx-2.3`, duration `6`, resolution `1080p`. This produced a usable
   reveal when the dedicated tool could not.
4. **Say what you did** — the fallback is a different look from the 3D pipeline, and that
   is a material change the user needs to know about.

If the intermediate 3D still is recoverable from the assets list, animate *that* rather
than the flat original — it is closer to the intended result.

## Identity

Method in `references/identity.md`. The rule that matters:

**Every asset generated after the palette is set must use it.** A brand kit whose own
sample images ignore its palette is worthless. Carry the hex values into every subsequent
prompt, explicitly.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
