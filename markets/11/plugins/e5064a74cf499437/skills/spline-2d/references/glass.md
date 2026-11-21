# Glass Skill (`backdrop-filter: hana-liquid-glass(...)` / `hana-noise-glass(...)`)

Hana has two *real* glass backdrop effects — both distort whatever sits *behind* the element and both blur the backdrop natively. They're siblings of the backdrop blur, so html-to-hana exposes them as **functions on the CSS `backdrop-filter` property**, not as `data-*` attributes. They work on container `<div>`s, text elements, and `<img>`.

- **`hana-liquid-glass(...)`** — a smooth, refractive lens: it bends, lenses, and optionally **magnifies** the backdrop (the Apple-style "liquid glass" look).
- **`hana-noise-glass(...)`** — a procedural-noise distortion: it warps the backdrop with a noise field for rippled / textured / frosted-organic glass, water, or heat-haze.

## Which one?

- **Clean, polished lens** (UI chips, buttons, cards, magnifiers) → **liquid glass**.
- **Textured / organic / watery / rippled** distortion → **noise glass**.
- **Flat frosted panel** with no warping (plain nav bars / modals) → not glass at all; use `backdrop-filter: blur(<px>)` with a translucent `background-color`.

Both glass functions **blur the backdrop themselves** via their own `blur` argument — do **not** also stack a separate `blur()` in the same `backdrop-filter`. One glass function is the whole effect.

---

## Liquid Glass — `hana-liquid-glass(...)`

A bare `hana-liquid-glass()` already produces a complete, valid refractive-glass effect; every argument has a default.

```html
<!-- Default refractive glass over whatever sits behind this div -->
<div style="width: 200px; height: 200px; border-radius: 32px; backdrop-filter: hana-liquid-glass();"></div>
```

Arguments are a space-separated `key=value` bag:

| Key | Meaning | Notes |
| --- | --- | --- |
| `distortion` | how strongly the backdrop bends | default 15 |
| `depth` | apparent glass thickness | default 10 |
| `blur` | native blur of the refracted backdrop | default 10 — this is the only blur you need |
| `chromatic-aberration` | rainbow color fringing | default 0; try ~0.2–0.5 for a prism edge |
| `chromatic-edge-only` | confine the fringing to edges | boolean, default on; bare key ⇒ on, `false`/`0`/`no` ⇒ off |
| `profile` | edge falloff shape of the lens | default 0; leave at 0 unless asked |
| `magnification` | lens magnification of the backdrop | default 0; > 0 for a magnifying-glass look |
| `offset-x` / `offset-y` | shift the sampled backdrop (px) | default 0 / 0 |

```html
<!-- Glassy lens chip over a vivid hero — no border; the refraction makes the edge -->
<div style="width: 220px; height: 64px; border-radius: 32px; backdrop-filter: hana-liquid-glass(distortion=18 blur=6);"></div>

<!-- Magnifying badge -->
<div style="width: 120px; height: 120px; border-radius: 60px; backdrop-filter: hana-liquid-glass(magnification=0.5 distortion=10);"></div>

<!-- Prism-edged glass card -->
<div style="width: 320px; height: 200px; border-radius: 24px; backdrop-filter: hana-liquid-glass(chromatic-aberration=0.4 distortion=22);"></div>
```

---

## Noise Glass — `hana-noise-glass(...)`

A bare `hana-noise-glass()` already produces a complete, valid noisy-glass effect; every argument has a default.

```html
<!-- Default procedural-noise glass over whatever sits behind this div -->
<div style="width: 240px; height: 240px; border-radius: 24px; backdrop-filter: hana-noise-glass();"></div>
```

Arguments are a space-separated `key=value` bag:

| Key | Meaning | Notes |
| --- | --- | --- |
| `noise` | noise pattern | `simplex` (default, smooth organic), `fbm` (layered/cloudy), `voronoi` (cellular), `sine` (regular ripples) |
| `amplitude` | distortion strength | default 10 |
| `scale` | pattern frequency / zoom | default 4; smaller = larger features (sensible ~0.01–100) |
| `blur` | native blur of the distorted backdrop | default 0 — use this, don't stack `blur()` |
| `stretch-x` / `stretch-y` | anisotropy of the noise | default 1 / 1 (sensible 0–1) |
| `offset-x` / `offset-y` | pan the noise field | default 0 / 0 |
| `movement` | animation speed of the noise over time | default 0 |
| `seed` | RNG seed for a reproducible pattern | default 0 |

```html
<!-- Rippled water glass over a vivid backdrop -->
<div style="width: 280px; height: 180px; border-radius: 20px; backdrop-filter: hana-noise-glass(noise=sine amplitude=14 scale=8 stretch-y=0.4);"></div>

<!-- Frosted-organic privacy panel -->
<div style="width: 320px; height: 220px; border-radius: 24px; backdrop-filter: hana-noise-glass(noise=fbm amplitude=22 scale=3 blur=4);"></div>

<!-- Cellular / cracked-ice texture -->
<div style="width: 200px; height: 200px; border-radius: 100px; backdrop-filter: hana-noise-glass(noise=voronoi amplitude=18 scale=6);"></div>
```

Only the Uniform amplitude is exposed via `amplitude`; the Progressive (spatially-varying) amplitude is not authorable here — don't try to set it.

---

## Pitfalls (both)

- **Both need a visible, ideally colorful/detailed backdrop to read.** Like real glass, distortion over a flat white background shows almost nothing — place it over a vivid gradient, image, or busy content.
- **Don't put a `border` / stroke on a glass shape.** Unlike a flat `backdrop-filter: blur` panel (which wants a thin light border to sell the frosted look), these effects render their own distorted edge — a CSS border just sits flatly on top and fights it. Keep glass shapes stroke-free; reach for `distortion` (liquid) or `amplitude` (noise) to strengthen the edge instead of a border.
- **Don't stack `blur()`** alongside either — use the function's built-in `blur` argument.
- These are CSS function arguments, not `data-*` attributes and not a CSS `transform`.
- Unknown keys and unparseable numbers are warned and ignored (the field keeps its default).
- `offset-x` / `offset-y` shift the *sampled backdrop*, not the element's own box.
- **To animate a knob on `:hover` / `:hana-active`** (e.g. ramp `distortion` on hover), declare the glass on the base **and** restate the whole function in the pseudo rule — `backdrop-filter` is one CSS property, so the hover value replaces the base wholesale and omitted args revert to defaults. A pseudo-state can only modify an effect already on the base, not add one.
