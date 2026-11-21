# Layer Noise Skill (`filter: hana-layer-noise(...)`)

Hana's Layer Noise effect (`LayerNoise`) warps the element's **own layer** — its background fill, text glyphs, or image pixels — with a procedural noise field, for wavy / rippled / melting / heat-haze / organic-warped looks. It operates on the layer itself (a sibling of `filter: blur` and `drop-shadow`), so html-to-hana exposes it as a **function on the CSS `filter` property**, not as a `data-*` attribute. It works on container `<div>`s, text elements, and `<img>`.

## Layer Noise vs. Noise Glass — pick the right one

- **`filter: hana-layer-noise(...)`** distorts **the element itself** (this skill). Use it to ripple a shape's fill, melt some text, or add heat-haze to an image.
- **`backdrop-filter: hana-noise-glass(...)`** distorts **whatever sits behind** the element (frosted/rippled glass over a backdrop — see the `glass` skill).

Same noise knobs, different target. If the brief is "make *this thing* wavy/distorted," it's layer-noise; if it's "warp what's *behind* this panel," it's noise-glass.

## Usage

A bare `hana-layer-noise()` already produces a complete, valid effect; every argument has a default.

```html
<!-- Default procedural-noise warp of this div's own fill -->
<div style="width: 240px; height: 240px; border-radius: 24px; background: linear-gradient(135deg,#6366f1,#ec4899); filter: hana-layer-noise();"></div>
```

Arguments are a space-separated `key=value` bag:

| Key | Meaning | Notes |
| --- | --- | --- |
| `noise` | noise pattern | `simplex` (default, smooth organic), `fbm` (layered/cloudy), `voronoi` (cellular), `sine` (regular ripples) |
| `amplitude` | distortion strength | default 10 |
| `scale` | pattern frequency / zoom | default 4; smaller = larger features (sensible ~0.01–100) |
| `blur` | native blur of the distorted layer | default 0 — use this, don't stack `blur()` |
| `stretch-x` / `stretch-y` | anisotropy of the noise | default 1 / 1 (sensible 0–1) |
| `offset-x` / `offset-y` | pan the noise field | default 0 / 0 |
| `movement` | animation speed of the noise over time | default 0 |
| `seed` | RNG seed for a reproducible pattern | default 0 |

## Recipes

```html
<!-- Rippled / watery shape -->
<div style="width: 280px; height: 180px; border-radius: 20px; background: #38bdf8; filter: hana-layer-noise(noise=sine amplitude=14 scale=8 stretch-y=0.4);"></div>

<!-- Melting / liquid text -->
<h1 style="font-size: 88px; font-weight: 800; color: #f97316; filter: hana-layer-noise(noise=simplex amplitude=10 scale=3);">MELT</h1>

<!-- Heat-haze over a photo -->
<img src="..." style="width: 320px; height: 220px; border-radius: 16px; filter: hana-layer-noise(noise=fbm amplitude=8 scale=5 movement=1);" />

<!-- Cellular / cracked texture on a fill -->
<div style="width: 200px; height: 200px; border-radius: 100px; background: #a78bfa; filter: hana-layer-noise(noise=voronoi amplitude=18 scale=6);"></div>
```

## Pitfalls

- **It warps the element's own content** — the element needs something visible to distort (a `background`, text, or image). An empty, transparent box shows nothing.
- **Don't confuse it with `hana-noise-glass`** (backdrop) — that's in the `glass` skill and needs a vivid *backdrop* instead.
- **Don't stack a separate `blur()`** in the same `filter` — use the built-in `blur` argument.
- Only the Uniform `amplitude` is exposed; the Progressive (spatially-varying) amplitude is not authorable here — don't try to set it.
- These are CSS function arguments, not `data-*` attributes and not a CSS `transform`.
- Unknown keys and unparseable numbers are warned and ignored (the field keeps its default).
- `hana-layer-noise` is a `filter` function only — it is **not** valid in `backdrop-filter` (use `hana-noise-glass` there).
