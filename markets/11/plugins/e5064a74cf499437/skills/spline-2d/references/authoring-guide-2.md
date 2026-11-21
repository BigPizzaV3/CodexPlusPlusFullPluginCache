**Part 2 of 2 of the HTML+CSS authoring contract** — continues `load_skill("authoring-guide")` (load Part 1 first if you haven't; the two halves share one section numbering). Part 1 covered operating the editor, the supported tags, and static styling; this half adds the interactive rest of §2, motion, and typography, then the authoring-discipline checklist (§3), worked examples (§4), common mistakes (§5), reviewing your own work (§6), and the code↔canvas round-trip (§7: export_html back to source; upload_assets + CSS-art fidelity when reproducing FROM source).

## 2. CSS — interaction, motion & typography (continued)

### Click actions — `data-hana-on-click`

Most disclosure widgets (drawers, dropdowns, modals, accordions, expanders) need a click on element A to flip element B's visibility. Use the `data-hana-on-click` attribute with one or more of these actions, each targeting another element by its HTML `id`:

```html
data-hana-on-click="show(target=#id)"     <!-- make the target visible -->
data-hana-on-click="hide(target=#id)"     <!-- make the target invisible -->
data-hana-on-click="toggle(target=#id)"   <!-- flip the target's visibility each click -->
data-hana-on-click="link(url=https://…)" <!-- open a URL (new tab by default; add `, target=self` for same tab) -->
```

The trigger and target can be siblings, distant cousins — anywhere in the same root frame. `#id` refers to a normal HTML `id` attribute on the target element. Forward references are fine (the trigger may come before the target in source order).

**Multiple actions, one click.** Separate actions with a **comma** and they all fire in order on a single click — this is how you build **tab bars, segmented controls, step wizards, and carousels**: hide the panel that's showing and show the next one in one click.

```html
<!-- Two-tab switcher: each tab button hides the other panel and shows its own -->
<div style="display: flex; gap: 8px;">
  <button data-hana-on-click="show(target=#panel-a), hide(target=#panel-b)" style="display: flex; padding: 8px 12px;">
    <span data-singleline style="font-size: 14px;">Tab A</span>
  </button>
  <button data-hana-on-click="hide(target=#panel-a), show(target=#panel-b)" style="display: flex; padding: 8px 12px;">
    <span data-singleline style="font-size: 14px;">Tab B</span>
  </button>
</div>
<section id="panel-a" style="display: flex;">…</section>
<section id="panel-b" hidden style="display: flex;">…</section>
```

Pair with the **`hidden` boolean attribute** to make the target start invisible — typically you want `hidden` on whatever the user reveals via a click, so the resting design isn't cluttered.

```html
<!-- Hamburger menu that opens a side drawer -->
<header style="display: flex; justify-content: flex-end; padding: 16px;">
  <button data-hana-on-click="toggle(target=#mobile-menu)" style="display: flex; padding: 8px 12px; background-color: #111; border-radius: 6px;">
    <span data-singleline style="font-size: 14px; color: #fff;">Menu</span>
  </button>
</header>
<aside id="mobile-menu" hidden style="display: flex; flex-direction: column; background-color: #fff; padding: 24px; gap: 12px;">
  <span data-singleline style="font-size: 16px;">Home</span>
  <span data-singleline style="font-size: 16px;">About</span>
  <span data-singleline style="font-size: 16px;">Contact</span>
</aside>
```

Rules and limits:
- **One `data-hana-on-click` attribute per element**, holding a **comma-separated list** of actions that all fire on the click, in order. Mix freely — e.g. `toggle(target=#a), show(target=#b)`, or a `hide(...)` plus a `link(...)`.
- **`target=#id` is required** for `show`/`hide`/`toggle`; the `#` prefix is mandatory and matches the CSS / `<a href="#anchor">` convention. `link(...)` takes `url=` instead (no `#`).
- **Every visibility target must exist** somewhere in the same HTML — if **any one** target in the list doesn't resolve, the converter warns and disables the **whole** click event, so don't reference ids you haven't created.
- For a pure navigate-on-click element prefer a real `<a href>` (above); reach for `link(...)` only when a click needs to navigate *and* do something else (e.g. close a menu then open a URL), or when the trigger can't be an anchor.
- The actions fire on **press** (pointer down), not on release — fine for reveal/toggle, just don't design around a click that only counts on mouse-up.
- Stack with `:hover` / `:hana-active` on the same element for hover affordance + press affordance + click action — they're independent layers.

### Hover reveal — `data-hana-on-hover`

Reveal a **separate** element while the pointer is over the trigger, and hide it again on leave — the canonical **dropdown menu, tooltip, and hover card** pattern. (`:hover` only restyles the *same* element; use `data-hana-on-hover` when hovering one element should show *another*.) Same `show` / `hide` / `toggle(target=#id)` grammar as `data-hana-on-click`, comma-separated for multiple actions:

```html
data-hana-on-hover="show(target=#dropdown)"          <!-- reveal while hovering, auto-hide on leave -->
data-hana-on-hover="show(target=#a), hide(target=#b)" <!-- swap one panel for another while hovering -->
```

The action is **stateful**: `show(target=#x)` makes `#x` visible on pointer-enter and hides it again on pointer-leave — you do **not** need a matching `hide` for the leave. Mark the target `hidden` so it starts collapsed and only appears on hover.

```html
<!-- Nav item with a hover dropdown -->
<nav style="display: flex; flex-direction: column;">
  <span data-hana-on-hover="show(target=#products-menu)" data-singleline style="font-size: 15px; font-weight: 600;">Products</span>
  <div id="products-menu" hidden style="display: flex; flex-direction: column; gap: 8px; padding: 12px; background-color: #fff; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.12);">
    <span data-singleline style="font-size: 14px;">Analytics</span>
    <span data-singleline style="font-size: 14px;">Automation</span>
  </div>
</nav>
```

Rules and limits:
- **One `data-hana-on-hover` attribute per element**, holding a comma-separated action list (just like a click). Visibility actions only — `link(...)` is **dropped with a warning** (navigating the moment the pointer crosses an element is a footgun; use `data-hana-on-click` / `<a href>` to navigate on click).
- **`target=#id` is required**; an unresolved target warns and disables the whole hover event (same as `data-hana-on-click`).
- **Mind the gap:** if the revealed target sits visually apart from the trigger, the pointer leaving the trigger to reach it will hide it. Keep the target adjacent (a dropdown directly under its nav item) or nest it inside the trigger so the hover region covers both.
- Stack freely with `:hover` (restyle the trigger), `:hana-active`, and `data-hana-on-click` on the same element — all independent layers.

### Keyboard shortcuts — `data-hana-on-key`

Bind keyboard presses to the same `show` / `hide` / `toggle` / `link` actions as `data-hana-on-click`. The attribute value is a **semicolon-separated list** of `KeyName:actions` bindings — one element can hold any number of bindings, and each binding's `actions` is itself a **comma-separated** action list (just like a click), so one key can fire several actions in order.

```html
data-hana-on-key="Escape:hide(target=#modal)"
data-hana-on-key="Enter:show(target=#dialog); Escape:hide(target=#dialog)"
data-hana-on-key="m:toggle(target=#menu)"
data-hana-on-key="ArrowRight:hide(target=#slide1), show(target=#slide2)"  <!-- one key, two actions -->
```

Separators: `;` divides bindings, `,` divides the actions within one binding's `KeyName:` list.

Key matching is **global** — the press fires regardless of which element is focused or hovered. Authoring tip: put the attribute on whatever element the binding logically belongs to (the modal it closes, the menu it opens), not on the page root — same Hana scene either way, but easier to read.

| Friendly alias | Canonical key |
| --- | --- |
| `Esc` | `Escape` |
| `Return` | `Enter` |
| `Up` / `Down` / `Left` / `Right` | `ArrowUp` / `ArrowDown` / `ArrowLeft` / `ArrowRight` |
| `Space` / `Spacebar` | (literal space) |
| single letters (`m`, `A`) | lowercased (`m`) |

Multi-letter key names — `Enter`, `Escape`, `Tab`, `Backspace`, `Delete`, `Home`, `End`, `PageUp`, `PageDown`, `F1`–`F12`, the arrow keys, the modifier keys (`Shift`, `Control`, `Alt`, `Meta`) — are **case-insensitive** (`enter` and `Enter` both work). Single letters (`m`, `A`) are lowercased to match what `KeyboardEvent.key` reports without shift held. Anything else (e.g. `/`, `?`, `+`) is passed through verbatim.

```html
<!-- Modal that opens with a button click and closes on Escape -->
<button data-hana-on-click="show(target=#confirm)" style="display: flex; padding: 8px 12px; background-color: #2563eb; border-radius: 6px;">
  <span data-singleline style="font-size: 14px; color: #fff;">Delete</span>
</button>
<section id="confirm" hidden data-hana-on-key="Escape:hide(target=#confirm)" style="display: flex; flex-direction: column; padding: 24px; background-color: #fff; border-radius: 12px;">
  <span data-singleline style="font-size: 16px;">Are you sure?</span>
</section>
```

Rules and limits:
- **One binding per key per scene** — if two elements both bind `Escape:hide(...)`, both fire on a single press. Useful for "close any open panel" patterns; avoid if you mean only one to fire.
- **`target=#id` is required**; the `#` prefix is mandatory.
- **Unresolved targets warn and disable the binding** (same behavior as `data-hana-on-click`).
- Fires **once per physical press** (the runtime filters browser auto-repeat) — a held key won't repeatedly retrigger the action.
- Stack with `data-hana-on-click` on the same element — the two attributes are independent and both layer onto any `:hover` / `:hana-active` events.

### Native `<details>` + `<summary>` (auto-wired disclosure)

Wherever the design wants a "click the header to expand a panel" pattern, you can also use the native HTML `<details>` element with a `<summary>` child:

```html
<details style="display: flex; flex-direction: column; padding: 16px; background-color: #fafafa; border-radius: 8px;">
  <summary style="display: flex;">
    <span data-singleline style="font-size: 16px; font-weight: 600;">Frequently asked</span>
  </summary>
  <p style="font-size: 14px; color: #555; line-height: 1.5; padding: 12px 0;">Answer body goes here…</p>
  <p style="font-size: 14px; color: #555; line-height: 1.5;">Optional second paragraph.</p>
</details>
```

The converter auto-wires `<summary>` to toggle the visibility of every other child of `<details>` on click (no `data-hana-on-click` needed; no `hidden` needed on the content). Reach for `<details>` whenever the pattern fits — it's the cleanest way to author an FAQ / collapsible card / expandable section. The "everything but summary toggles" behavior happens automatically.

**Pick the right tool:** use `<details>` for the simple "header + togglable body" pattern; use `data-hana-on-click` when the trigger and target are separate (a button in the header bar opens a drawer elsewhere, a tab button hides a panel, etc.).

### Entrance animations — `data-hana-animate-in`

Make an element animate **in when the scene loads** by tagging it with `data-hana-animate-in="<preset> [duration] [delay]"`. The converter wires a Hana `start` event that plays a one-shot transition from a hidden/offset state to the element's resting appearance. Works on containers, text, and images.

```html
data-hana-animate-in="fade"        <!-- fade up from transparent -->
data-hana-animate-in="fade-up"     <!-- fade + travel upward into place -->
data-hana-animate-in="fade-down"   <!-- fade + travel downward -->
data-hana-animate-in="fade-left"   <!-- fade + travel leftward -->
data-hana-animate-in="fade-right"  <!-- fade + travel rightward -->
data-hana-animate-in="scale"       <!-- fade + grow slightly into place (alias: zoom) -->
```

- **Optional timing:** add one or two CSS times after the preset — the first is **duration**, the second is **delay**: `data-hana-animate-in="fade-up 600ms 150ms"`. Defaults are 500ms duration, 0 delay.
- **Stagger a list** by giving successive items increasing delays (e.g. cards at `0ms`, `80ms`, `160ms`) for a cascading reveal.
- The preset name (`fade`, the four `fade-<dir>` slides, `scale`) is the only required part. The travel direction names where the element *travels to* — `fade-up` rises up into place.
- Stacks cleanly with `:hover` / `:hana-active` / click / key events on the same element — the entrance is an independent layer that plays once on load.
- Use it deliberately on the few elements that benefit (hero heading, primary card, key CTA, a staggered list) — not on everything, or the load feels noisy.

```html
<!-- Hero that fades its heading up, then its subtext slightly later -->
<div style="display: flex; flex-direction: column; gap: 12px; padding: 48px;">
  <h1 data-hana-animate-in="fade-up 500ms" style="font-size: 40px;">Build faster</h1>
  <p data-hana-animate-in="fade-up 500ms 120ms" style="font-size: 18px; color: #555;">Ship your ideas in minutes.</p>
</div>
```

### Cursor follow — `data-hana-follow`

Make an element **drift toward the cursor** and spring back, for a magnetic CTA, a parallax hero image, or a headline that subtly leans toward the pointer. Works on containers, text, and images. Tag it with `data-hana-follow="[distance] [smoothness]"`:

```html
data-hana-follow              <!-- defaults: 24px drift, smoothness 8 -->
data-hana-follow="40px"       <!-- leans up to 40px toward the cursor -->
data-hana-follow="16px 12"    <!-- subtle 16px lean, laggier/smoother easing -->
```

- **`distance`** (px) is the **max displacement** from the element's resting position — it leans toward the cursor up to this radius and no further. Keep it small (12–40px); it's an accent, not a chase.
- **`smoothness`** is the easing lag — higher is slower and floatier (default 8). Below ~4 the motion gets snappy/jittery.
- The effect is **canvas-global**: the element reacts to the cursor anywhere on the page, not only while hovered, and resets to rest when the cursor leaves the canvas.
- Composes with flex layout — the drift is a transform offset from where the element lays out, so it doesn't disturb siblings. Stacks with `:hover` / click / entrance layers.
- Use on **one or two focal elements** (a primary CTA, a hero badge/graphic). Applying it broadly makes the whole page feel unstable.

```html
<!-- Magnetic primary CTA -->
<button data-hana-follow="18px" style="display: flex; padding: 14px 28px; background-color: #111; border-radius: 999px;">
  <span data-singleline style="font-size: 15px; color: #fff;">Get started</span>
</button>

<!-- Parallax hero image that drifts with the cursor -->
<img src="..." width="480" height="360" data-hana-follow="28px 12" />
```

### Typography
| Property | Effect |
| --- | --- |
| `color` | text color |
| `font-size` | px only |
| `line-height` | unitless multiplier (e.g. `1.4`) |
| `letter-spacing` | `Npx` |
| `text-align` | `left` / `right` / `center` / `justify` |

**`font-family`, `font-weight`, `font-style` are honored** — they resolve against the font catalog below into one font per text shape. Always set `font-family` on the root container (it inherits to every text descendant). Use the literal family name (with quotes when it contains a space): `font-family: 'Plus Jakarta Sans'`, `font-family: Inter`, `font-family: 'Playfair Display'`. Weights map directly: `400`/`normal` → regular, `500`, `600`, `700`, `bold` → 700. `font-style: italic` picks the italic cut **only when the chosen family has one listed in the catalog below** — currently `Roboto`, `Lato`, `Playfair Display`, `Lora`, `EB Garamond`, `Cormorant Garamond`, and `Libre Baskerville`. Do not set `font-style: italic` on any other family; without an italic cut the upright glyphs render unchanged and the slant is silently lost. If you need italic emphasis, pick one of those families on the relevant text. Unknown family/variant combos fall back to the nearest available weight, then to Inter regular — stay inside the catalog so you get the typography you intend.

**Unsupported**: `text-transform`, `text-decoration`, `vertical-align`, `font` shorthand, `font-variant`, `white-space`, `word-break`, `overflow-wrap`.

### Single-line text — `data-singleline` (IMPORTANT)

Without a hint, every text element may wrap if its parent's cross-axis width is smaller than the text's natural width — this routinely breaks headings, button labels, nav links, and badges by splitting them onto two lines. **Mark any text that must stay on one line with the `data-singleline` attribute.** The converter then sizes the shape to hug its content width (Hana's `autoSize.width`) so the glyphs stay on a single line regardless of layout pressure.

Use `data-singleline` on (non-exhaustive):
- Headings and section titles (`<h1>`–`<h6>`) that are intended as one-line display type.
- Button / CTA labels, chip and pill text, tab labels, nav items, breadcrumb segments.
- Badges, status pills, prices, counters, tag labels, metric values.
- Wordmarks / brand names, avatar initials, single-line captions, table-cell-style labels.

Leave it **off** for genuinely multi-line text: body paragraphs, descriptions, quotes, long subtitles, list-item bodies — anything you intend to wrap.

**Never set an explicit `height` on text elements.** Multi-line text auto-grows its height to fit the wrapped content (Hana's `autoSize.height`), and single-line text hugs its content on both axes. Setting a fixed `height` on `<p>`, `<span>`, `<h1>`–`<h6>`, etc. either clips the glyphs or leaves dead vertical space. Width on text is fine — it controls the wrap column.

```html
<h1 aria-label="Headline" data-singleline style="font-size: 48px; font-weight: 700;">Build faster</h1>
<div aria-label="Get started button" style="display: flex; padding: 8px 16px; background-color: #2563eb; border-radius: 6px;">
  <span data-singleline style="font-size: 14px; color: #ffffff;">Get started</span>
</div>
```

### Visibility
**Unsupported**: `visibility: hidden` and `display: none`. To hide content, omit the element.

Valid font ids (format `{Family}_{variant}`, default `Inter_regular`):

- **Sans (UI)**: `Inter` (regular, 500, 600, 700), `Roboto` (regular, 500, 700, italic), `Poppins` (regular, 500, 600, 700), `Work Sans` (regular, 500, 600, 700), `DM Sans` (regular, 500, 700), `Manrope` (regular, 500, 600, 700), `Lato` (regular, 700, italic), `Open Sans` (regular, 500, 600, 700), `Nunito` (regular, 600, 700), `Montserrat` (regular, 500, 600, 700), `Source Sans 3` (regular, 600, 700), `Space Grotesk` (regular, 500, 700), `Outfit` (regular, 500, 700), `Figtree` (regular, 500, 700), `Plus Jakarta Sans` (regular, 500, 700), `IBM Plex Sans` (regular, 500, 700), `PT Sans` (regular, 700)
- **Display**: `Bebas Neue` (regular), `Oswald` (regular, 500, 700), `Anton` (regular), `Archivo Black` (regular)
- **Serif**: `Fraunces` (regular, 600, 700), `Playfair Display` (regular, 600, 700, italic), `Lora` (regular, 600, 700, italic), `Merriweather` (regular, 700), `EB Garamond` (regular, 600, italic), `Cormorant Garamond` (regular, 600, italic), `Source Serif 4` (regular, 600, 700), `Libre Baskerville` (regular, 700, italic), `Roboto Slab` (regular, 500, 700)
- **Monospace**: `JetBrains Mono` (regular, 500, 700), `Fira Code` (regular, 500, 700), `IBM Plex Mono` (regular, 500, 700), `Space Mono` (regular, 700), `Roboto Mono` (regular, 500, 700)
- **Handwritten / Script**: `Caveat` (regular, 700), `Pacifico` (regular), `Dancing Script` (regular, 700), `Permanent Marker` (regular), `Shadows Into Light` (regular)

Construct the id by joining family and variant with `_` — e.g. `Playfair Display_700`, `JetBrains Mono_regular`, `Roboto_italic`. Spaces inside family names are preserved. A listed family with an unlisted weight resolves to its nearest available cut; unknown families fall back to Inter — don't invent fonts outside this list.

## 3. Authoring discipline (always)

1. **One root container** wraps the whole page — a `<div style="display: flex; flex-direction: column; ...">` whose `width`/`height` match the `viewport` you passed to `write_html` (create mode) or the target frame's current size (replace mode).
2. **Name every element with `aria-label`** (see §1 Layer names). Default to naming — section, container, card, row, button, image, icon, heading, paragraph. Skip only throwaway leaf wrappers that would echo a named parent. The layer tree should read like a designer named it, not like raw markup.
3. **Every multi-child container declares `display: flex` + `flex-direction`.** No exceptions.
4. **No margins.** Use parent `gap` and `padding` for spacing.
5. **No `z-index` or absolute positioning.** Stack via source order; later siblings render on top.
6. **All lengths carry a unit.** Default to `px`; `%` is allowed on `width`/`height` (and `vw`/`vh` on those too); `auto` hugs content. Bare numbers are rejected.
7. **Colors only as** hex, `rgb(a)`, `hsl(a)`, or named.
8. **No `<canvas>`, `<input>`, `<form>`, `<table>`, etc.** — see the unsupported-tags list above. For icons use an Iconify icon (`<iconify-icon icon="mdi:home"></iconify-icon>`); inline `<svg>` IS supported for custom/decorative vectors (see §1).
9. **One styled run per text shape.** No nested `<strong>` or `<em>` for inline emphasis — split into sibling text elements inside a flex row.
10. **Borders.** Use the `border` shorthand for all-around borders; per-side borders (`border-bottom` etc.) are the right tool for dividers and accent edges, but they render solid only and ignore `border-radius` — keep them off rounded boxes.
11. **Backgrounds are solid color or linear/radial gradient** — stop positions in `%` only.
12. **No resting-state transforms or animations** — the base design is flat and static. `transform` is allowed only inside `:hover` rules (see §2 Hover states).
13. **Images need explicit `width` and `height`.**
14. **Tag single-line text with `data-singleline`** (see §2). Never set explicit `height` on text elements.
15. **Every interactive element gets a `:hover` state**, and every real button/CTA also gets a `:hana-active` pressed state, both in the `<style>` block (see §2 Hover and pressed states). A scene full of static buttons feels dead.
16. **Use `<a href="...">` for real navigation links**, not a styled `<div>` — the converter wires the href to a Hana `link` action so the click actually navigates. `href="#..."` in-page anchors aren't supported (no scroll-to-anchor) — drop them or use a real path/URL.
17. Keep the document well-formed: single root container, valid nesting, all tags closed.

## 4. Worked examples (follow these patterns)

### Card with image, title, body

```html
<style>
  .trip-card { display: flex; flex-direction: column; width: 320px; padding: 16px; gap: 12px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06); font-family: Inter; }
  .trip-card h2 { font-size: 18px; font-weight: 600; color: #111111; }
  .trip-card p { font-size: 14px; color: #666666; line-height: 1.4; }
</style>
<div class="trip-card" aria-label="Trip card">
  <img aria-label="Trip photo" src="ai:Dolomite peaks at golden hour, dramatic alpine light, painterly" width="288" height="160" style="border-radius: 8px;" />
  <div aria-label="Card text" style="display: flex; flex-direction: column; gap: 4px;">
    <h2 aria-label="Title" data-singleline>Mountain trip</h2>
    <p aria-label="Description">Three days in the Dolomites — see the photos.</p>
  </div>
</div>
```

### Button row with hover (primary + bordered secondary)

Every interactive element must have a `:hover` rule. Factor button styles into the `<style>` block so the selector can bind:

```html
<style>
  .btn-primary { display: flex; padding: 8px 16px; background-color: #2563eb; border-radius: 6px; box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08); }
  .btn-primary:hover { background-color: #1d4ed8; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35); }
  .btn-secondary { display: flex; padding: 8px 16px; background-color: #ffffff; border: 1px solid #d1d5db; border-radius: 6px; }
  .btn-secondary:hover { background-color: #f3f4f6; border: 1px solid #9ca3af; }
</style>
<div aria-label="Button row" style="display: flex; flex-direction: row; gap: 8px; padding: 12px;">
  <div class="btn-primary" aria-label="Confirm button">
    <span data-singleline style="font-size: 14px; color: #ffffff;">Confirm</span>
  </div>
  <div class="btn-secondary" aria-label="Cancel button">
    <span data-singleline style="font-size: 14px; color: #111111;">Cancel</span>
  </div>
</div>
```

### Centered content column inside a wider parent

```html
<style>
  .weather-screen { display: flex; flex-direction: column; align-items: center; width: 390px; padding: 20px; gap: 16px; font-family: Inter; }
  .weather-card { display: flex; flex-direction: column; width: 350px; padding: 16px; gap: 8px; background-color: #ffffff; border-radius: 12px; }
</style>
<div class="weather-screen" aria-label="Screen">
  <div class="weather-card" aria-label="Hourly card">…</div>
  <div class="weather-card" aria-label="Daily card">…</div>
</div>
```

## 5. Common authoring mistakes (avoid)

- **Reaching for `position: absolute`** to overlay or align — dropped. Use flex `justify-content`/`align-items` instead.
- **Using `margin`** — dropped. Use parent `gap` + `padding`.
- **Per-side borders on rounded boxes** — per-side borders (`border-top`, etc.) are supported but drawn square; on a `border-radius` box they poke past the curve. Use a uniform `border` there.
- **Mixed inline formatting** in one text block (`<p>`hello <strong>world</strong></p>`) — flattens to plain text. Split into siblings in a flex row.
- **Bare numbers** (`width: 10`) — rejected. Always include a unit (`10px`).
- **`<img>` without explicit width/height** — dropped. Always supply both, either as attributes or via inline CSS.
- **Pseudo-classes / pseudo-elements / media queries / keyframes** inside `<style>` blocks — dropped. The supported selector set is type / class / id / descendant only.
- **`calc(...)` or CSS variables** — dropped. Inline the literal value.
- **`display: grid` or `inline-block`** — only `display: flex` (and `block` which is normalized to flex-column) is supported.

## 6. Review your own work — `review_frame`

There is no automatic review pass here, so once you've authored or edited a frame, switch into bug-fixer mode and review it yourself. Inspect ONE frame at a time and apply granular edits to fix **bugs and visual mistakes only** — **never rewrite a working frame from scratch.** Your job is NOT to improve the design, raise its quality, or make it "nicer" — it is to repair things that are actually broken. If nothing is broken, you do nothing and stop.

### What `review_frame` gives you (up front — don't re-fetch)

Call `review_frame({ frame_id })` (the id `write_html` gave you; omit it to review the frame containing the current selection). One call returns everything you need to start:
- A **screenshot** of the rendered frame. This is your view of it — rely on this image; while you fix you won't pull a fresh one (see *How to fix*), so read it carefully.
- A **lean object map** of the frame — the same shape `get_scene` returns (ids / names / types / centers / sizes + a few cheap flags), scoped to this frame — so you can map what you see in the screenshot to the ids you'll edit. It deliberately omits full per-node detail (fills, fonts, layout, events). When you need that detail to diagnose or fix a **specific** node, call `get_object(id)` on **that node only** — sparingly; by default it returns just that one node (no children), which is all you need here. Don't pull the whole subtree back with `get_object(id, include_children: true)` — re-fetching the full tree is exactly the bloat this lean map already replaces.
- A **content-overflow hint** telling you whether laid-out content is clipped past the frame edge.
- Sometimes an **overlap hint** listing sibling elements whose bounding boxes collide (overlapping text is the classic case). When present, these are pre-detected bugs — confirm each against the screenshot and fix it; do not dismiss them as fine.
- Sometimes a **still-generating images list** naming objects whose AI image is still rendering in the background. In the screenshot these show as blank placeholders, but the finished image swaps in automatically. They are NOT bugs — assume the final image is already there and leave them (and their containers) completely alone.

### What to look for

**Lead with the screenshot, not the map** — the lean map only carries ids/names/types/sizes, so it tells you *where* a node is, not whether it's broken. First scan the screenshot for visual symptoms (below); for each one you suspect, use the map to pin down the relevant sub-node, call `get_object(id)` on it for the detailed data, and only then compare the screenshot against that detail to confirm an actual bug — something genuinely broken, not merely something that could be "better". The bugs worth flagging:
- Text clipped, truncated, or overflowing its container.
- Elements overlapping or colliding when they shouldn't, content spilling outside the frame.
- Broken auto-layout: collapsed, overlapping, or wildly uneven spacing; items stacked on top of each other.
- Severely misaligned elements (clearly off-grid, not a few pixels).
- Invisible/unreadable content: text the same color as its background, zero-size or zero-opacity elements that should be visible.
- Broken icons, distorted/stretched images, placeholder rectangles left where real content was intended.

Do NOT flag things that merely could be improved: a fine palette, acceptable hierarchy, reasonable spacing, or stylistic choices. Subjective "polish" is out of scope.

Do NOT touch objects named in the still-generating images list: a blank rectangle there is a placeholder for an image that is about to arrive, not a leftover placeholder or an empty element. Deleting, recoloring, resizing, or layering content over one breaks the swap-in.

### How to fix

- `resize_frame` — when the overflow hint reports content clipped past the frame edge AND the frame is meant to scroll (a page or feed), grow it to the recommended size so nothing is cut off. For a fixed screen (phone/card/poster) the size is intentional — do NOT grow it; compress the content with the tools below instead.
- `update_objects` — change `shape`, `fill`, `stroke`, `opacity`, `center`, text content/size, etc. Patches deep-merge, INCLUDING inside `shape`: send only the fields you're changing (e.g. `shape: { text: "New copy" }`, `shape: { cornerRadius: [8,8,8,8] }`) — omit `type` (the live shape keeps its kind; pass `type` only to convert to a different kind) and never re-emit the whole shape blob `get_object` returned.
- `recolor` — swap colors by VALUE across the whole frame without listing ids; the cheap way to retheme (light↔dark) or remap a palette. Prefer it over many `update_objects` fill edits when several objects share a color.
- `move_objects` — reparent or restack inside the frame.
- `add_objects` — add missing decoration, dividers, accents (must nest under an existing parent inside the frame).
- `delete_objects` — remove stray/empty/placeholder elements.
- `duplicate_objects` — replicate a card/row/icon pattern when the original is missing a sibling.

**Make your fix pass one-and-done.** After you apply your edits, do NOT call `get_object` or `get_scene` again to re-read live state — there is no new screenshot, so a re-read shows you nothing you can act on. Reason from the map and the original screenshot; pull `get_object` on a specific node only *while diagnosing* a fix you're about to make, never afterward to check it. **`review_frame` is a single pass per frame too: it does not re-render, so calling it again to "verify" your fixes shows you nothing new — review once, apply your fixes, then stop.** Your iteration budget is short. When in doubt, leave it alone.

### Scope

Edits are scoped to **frames you own** — ones you created with `write_html`, plus any pre-existing user frame you were pointed at. A frame another agent owns is off-limits (the server rejects the edit). Creating new root frames is normal authoring, but never delete a frame out from under the user.

### Hana cheatsheet

- **Object shape**: `{ type: "Shape" | "Group", name, center: [x, y], shape: { type, size: [w, h], ... }, fill?, stroke?, opacity?, rotation? }`. `center` is in the parent's local coordinates.
- **Shape types**: `Frame` (container, optional `layout`), `Rectangle`, `Ellipse`, `Text` (`text`, `fontSize`, `font: "Inter_regular"`, `horizontalAlign`, `lineHeight`), `Polygon`, `Star`, `VecNet` (`svgPath`).
- **Colors**: hex or CSS strings — e.g. `{ type: "Color", color: "#F87333" }`, `"#FFFFFF80"` (alpha), or `"rgba(248, 115, 51, 1)"`. Reads (`get_object`) return hex. Do NOT use `[0,1]` float arrays.
- **Fill / Stroke**: `fill: { type: "Color", color: "#1E293B" }` or `fill: { type: "Gradient", gradientType, stops, start, end }` (gradient stop `color` is also a hex/CSS string). Stroke adds `thickness`.
- **Auto-layout** (on Frame.shape.layout): `{ direction: "Row" | "Column", align, gap, leftPadding, rightPadding, topPadding, bottomPadding }`. Children flow in array order (children[0] = top of Column / left of Row).
- **Free-layout** (no `shape.layout`): children are painted back-to-front — children[0] paints first.
- **Sizing** on children of auto-layout Frames: `horizontalResizeType` / `verticalResizeType` of `Fixed` | `Fill` | `Hug`.

### Tone

You are a bug-fix pass, not a polishing pass and not a redesign. Keep the author's structure, palette, hierarchy, spacing, and intent exactly as they are — only repair what is actually broken. Doing nothing is the correct and expected outcome whenever the frame renders without layout bugs. Never make a change just to justify the call.

Keep your messages short and to the point — one line naming the bug you fixed (or "no bugs found"). No preamble, no summaries, no design commentary.

## 7. Propagating design changes back to source code — `export_html`

When the canvas design originated from an existing codebase (you built it by scanning a website repo — Next.js, Vue, plain HTML, anything) and the user asks to **carry the design changes back into that code** ("propagate this back to the repo", "apply my edits to the site", "sync the design to the codebase", "update the source with these changes"), use `export_html` as the bridge:

1. **Export the ground truth**: call `export_html({ frame_id })`. It regenerates HTML from the frame's live Hana data, so it reflects the design as it exists RIGHT NOW — including every manual canvas edit.
2. **Diff it against the HTML already in your context** — the HTML you last authored for that frame via `write_html`. What you authored is the design as YOU last built it; the export is the design as the user has it now — everything that differs between the two is the change to carry over. (If you never authored this frame, or your original HTML has scrolled out of context, skip the diff and treat the export itself as the spec.)
3. **Diff semantically, not textually.** The export is regenerated and normalized — generated class names (`.s0`, `.s1`, …), converter-canonical property order and formatting — so a character-level diff against your original is mostly noise. Compare meaning: which copy changed, which colors/sizes/spacing moved, what was added, removed, or reordered. Match elements across the two versions by their text, position, and structure; when a change is ambiguous, locate that node in `get_scene` and pull `get_object(id)` on it for exact values.
4. **Translate the change intent into the repo's own idiom.** The exported HTML is an intermediate representation, not production markup — do NOT paste it wholesale into the codebase. Re-express each change the way the surrounding code does (JSX props, Vue templates, Tailwind classes, CSS modules, design tokens), keeping the repo's structure and conventions intact.

Notes:
- Works for any frame, including ones never authored via `write_html`. With no baseline to diff, treat the export itself as the spec and compare it against the repo's markup directly.
- Images export compactly: `src="ai:<prompt>"` identifies an AI-generated image by its prompt; `hana-asset:<id>` marks a binary asset that wasn't inlined (pass `inline_images: true` only if you need the actual pixels). Both are references for YOU to interpret, not URLs to write into the repo.
- Options: `fragment: true` returns a bare element + `<style>` fragment instead of a full document; `style_mode: "inline"` writes per-element `style="…"` attributes — sometimes easier to compare element-by-element than the hoisted stylesheet.

### Reproducing a design FROM source code — reuse real assets, rebuild CSS art

The same code↔canvas loop runs forward: when you build a frame FROM an existing codebase (recreating an app screen or website from its repo), the repo is the ground truth for every visual. Fidelity to it beats speed:

- **Reuse the repo's real image assets — never regenerate them.** When the source references an image file that exists on disk (logo, product shot, illustration, photo, texture, avatar), upload the actual file with `upload_assets({ assets: [{ path: "/abs/path/hero.png" }] })` and reference the returned src in your HTML: `<img src="hana-asset:<id>" …>`, or `background-image: url("hana-asset:<id>")` for a backdrop. An `ai:` re-imagining of an asset that already exists is always the wrong call — off-brand, wrong in detail, and it severs the mapping back to the codebase. Reserve `ai:` for imagery the project doesn't have. Upload before `write_html` (batch every file in one call) so the ids are in hand while you author.
- **SVG files stay vectors either way**: upload them with `upload_assets` and reference `<img src="hana-asset:<id>">` — the converter runs the file through svg-to-hana into real, editable vector shapes (never a rasterized fill) — or inline small icon/logo markup directly as `<svg>`. Uploading keeps large SVGs out of your HTML; inlining suits tiny glyphs you want to restyle in place. SVGs can't be `background-image` fills — reference them as `<img>`.
- **Recapitulate CSS-built art with real primitives.** When the source draws a visual with CSS alone — layered absolutely-positioned divs, gradient orbs, blur glows, border tricks, pure-CSS illustrations — rebuild it inside the subset: nested frames, linear/radial gradients, `border-radius`, `box-shadow`, `filter: blur`, opacity, and source-order stacking (later siblings paint on top; a container's background paints behind its children). Do NOT flatten CSS art into an `ai:` image because translating it takes effort — the render loses the exact colors and crisp edges, doesn't scale, and can't round-trip back into source styles via `export_html`.