# Mobile App Skill (native phone-screen design)

You are designing a **native mobile app screen** (iPhone / Android phone), not a website. A phone UI lives inside a physical device screen, so it has two structural requirements that desktop/web layouts don't — get these right *first*, then fill the content.

## Viewport

- Single screen, no scroll: **844–932px tall** at **390–430px wide** (e.g. 390×844 iPhone, 430×932 iPhone Pro Max).
- Scrollable feed / onboarding flow: **1400–2000px tall** at the same widths.
- Don't grow the width past ~430px — that stops reading as a phone.

## Rule 1 — the root frame is ALWAYS corner-rounded and clipped

A real phone has rounded screen corners. Every mobile root frame must carry a **`border-radius`** matching the device bezel, plus **`overflow: hidden`** so the status bar, content, and any full-bleed imagery clip cleanly to that radius.

- iPhone-class screens: **`border-radius: 44px`** (use ~40–48px; larger devices read fine at 47–55px).
- Android-class screens: **`border-radius: 32px`** (≈28–36px).
- Without `overflow: hidden` the radius is purely cosmetic — children paint past the rounded corner. Always pair them.

```html
<div aria-label="Screen" style="display: flex; flex-direction: column; width: 390px; height: 844px; border-radius: 44px; overflow: hidden; background-color: #ffffff; font-family: Inter;">
  <!-- status bar (Rule 2) goes here, first child -->
  <!-- then nav / content / tab bar -->
</div>
```

## Rule 2 — start every screen with a standard status bar

The **first child** of the root frame is the OS status bar: the time on the left, and the cellular / Wi-Fi / battery indicators on the right. Never ship a phone screen without it — a screen that begins straight into content looks like a cropped web page.

Paste this iOS-style status bar as-is, then adapt only the color (see below). It uses `justify-content: space-between` (supported here — it maps to Hana's auto-gap distribution) to pin the time left and the indicators right across the full screen width.

```html
<div aria-label="Status bar" style="display: flex; flex-direction: row; justify-content: space-between; align-items: center; width: 100%; height: 54px; padding: 0px 24px 0px 34px; background-color: transparent;">
  <span aria-label="Time" style="font-size: 17px; font-weight: 600; color: #000000;">9:41</span>
  <div aria-label="Indicators" style="display: flex; flex-direction: row; align-items: center; gap: 7px;">
    <iconify-icon aria-label="Cellular" icon="ion:cellular" width="18" style="color: #000000;"></iconify-icon>
    <iconify-icon aria-label="Wi-Fi" icon="ion:wifi" width="18" style="color: #000000;"></iconify-icon>
    <iconify-icon aria-label="Battery" icon="ion:battery-full" width="25" style="color: #000000;"></iconify-icon>
  </div>
</div>
```

### Android variant

For an Android screen, keep the same status-bar container but swap the three indicators for **Material Symbols** (`material-symbols:*`, Google's current Material You set) — solid signal bars, a fan-shaped Wi-Fi glyph, and a vertical battery, exactly as the latest Android renders them:

```html
<div aria-label="Indicators" style="display: flex; flex-direction: row; align-items: center; gap: 7px;">
  <iconify-icon aria-label="Cellular" icon="material-symbols:signal-cellular-4-bar" width="18" style="color: #000000;"></iconify-icon>
  <iconify-icon aria-label="Wi-Fi" icon="material-symbols:wifi" width="18" style="color: #000000;"></iconify-icon>
  <iconify-icon aria-label="Battery" icon="material-symbols:battery-full" width="16" style="color: #000000;"></iconify-icon>
</div>
```

### Adapting the status bar

- **Dark backgrounds / immersive screens:** flip every `#000000` above (the time's `color` and each `<iconify-icon>`'s `style="color:"`) to `#ffffff`. Light icons on a dark screen; dark icons on a light screen.
- **Keep the height at ~54px** and `background-color: transparent` so it sits over the screen's own background (the root frame's `overflow: hidden` clips its top corners to the device radius automatically).
- **Don't add a corner radius to the status bar itself** — only the root frame is rounded.
- Time is the canonical Apple demo value `9:41`; change it only if the brief calls for a specific time.

## Putting it together

Below the status bar, lay out the rest of the screen as flex columns/rows — a top nav/header, the scrollable content, and (for tabbed apps) a bottom tab bar as the last child. A typical skeleton:

```html
<div aria-label="Screen" style="display: flex; flex-direction: column; width: 390px; height: 844px; border-radius: 44px; overflow: hidden; background-color: #f5f5f7; font-family: Inter;">
  <!-- 1. Status bar (paste from Rule 2) -->
  <div aria-label="Status bar" ...>…</div>
  <!-- 2. App header / nav -->
  <header aria-label="Header" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between; padding: 8px 20px 12px 20px;">…</header>
  <!-- 3. Content -->
  <main aria-label="Content" style="display: flex; flex-direction: column; gap: 16px; padding: 16px 20px;">…</main>
  <!-- 4. Bottom tab bar (last child, tabbed apps) -->
  <nav aria-label="Tab bar" style="display: flex; flex-direction: column; background-color: #ffffff;">
    <div aria-label="Tabs" style="display: flex; flex-direction: row; justify-content: space-between; align-items: center; padding: 10px 32px;">…tab icons…</div>
    <div aria-label="Home indicator clearance" style="height: 20px;"></div>
  </nav>
</div>
```

## Immersive screens — full-bleed photo behind the UI

Many phone screens (onboarding, players, mood/wellness, maps, detail heroes) put a **full-bleed photo or 3D render behind the chrome**: the status bar, a translucent nav, and often a bottom sheet all sit *over* the image. This subset is flex-only — no `z-index`, no absolute positioning — so the image can NOT be a sibling `<img>` (that stacks it *above/below* the content). Put it on the **screen frame itself** as `background-image: ai("...")`; a frame's fill renders behind every child, and the content flows on top:

```html
<div aria-label="Screen" style="display: flex; flex-direction: column; width: 390px; height: 844px; border-radius: 44px; overflow: hidden; background-image: ai(&quot;serene translucent blue 3d figure seated, soft volumetric light, calming gradient sky&quot;); font-family: Inter;">
  <!-- status bar — white icons over the photo -->
  <div aria-label="Status bar" style="display: flex; flex-direction: row; justify-content: space-between; align-items: center; width: 100%; height: 54px; padding: 0px 24px 0px 34px;">
    <span aria-label="Time" style="font-size: 17px; font-weight: 600; color: #ffffff;">9:41</span>
    <div aria-label="Indicators" style="display: flex; flex-direction: row; align-items: center; gap: 7px;">
      <iconify-icon aria-label="Cellular" icon="ion:cellular" width="18" style="color: #ffffff;"></iconify-icon>
      <iconify-icon aria-label="Wi-Fi" icon="ion:wifi" width="18" style="color: #ffffff;"></iconify-icon>
      <iconify-icon aria-label="Battery" icon="ion:battery-full" width="25" style="color: #ffffff;"></iconify-icon>
    </div>
  </div>
  <!-- nav row, also over the photo -->
  <header aria-label="Nav" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between; padding: 8px 20px;">…</header>
  <!-- flexible spacer pushes the sheet to the bottom -->
  <div aria-label="Spacer" style="display: flex; flex: 1;"></div>
  <!-- frosted bottom sheet floating over the lower part of the photo -->
  <section aria-label="Mood sheet" style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 24px; background-color: rgba(255,255,255,0.55); backdrop-filter: blur(24px); border-radius: 32px 32px 0px 0px;">…</section>
</div>
```

- The chrome's icon/text color must contrast the photo — usually **white** over a vivid/dark hero (flip the status-bar colors as in §2).
- Pin top chrome and a bottom sheet apart with a `flex: 1` spacer (above) or `justify-content: space-between` on the screen column.
- Need the photo darker for legible text? Bake the darkening / vignette **into the `ai("...")` prompt** — you can't stack a scrim layer over an image fill.

## Pitfalls

- **Hero photo as an `<img>` block when content belongs over it** — stacks the image above/below the UI instead of behind it. Use `background-image: ai("...")` on the screen frame (or the section) so the chrome and sheet float on top. See "Immersive screens" above.
- **Missing root radius / `overflow: hidden`** — the #1 tell of a non-mobile-looking screen. Always both.
- **No status bar** — never start straight into content.
- **Wrong icon contrast** — black icons on a dark hero, or white on white. Match the icon/time color to the background underneath.
- **Bottom tab bar with no home-indicator clearance** — leave ~20px of empty space below the tabs so they clear the home indicator instead of hugging the very edge. Model that clearance as a **separate spacer child** (as in the skeleton), NOT as extra `padding-bottom` on the tab row: keep the tab row's own vertical padding symmetric so `align-items: center` actually centers the icons. Asymmetric top/bottom padding + `align-items: center` offsets the icons instead of centering them.
- Stay in the html-to-hana subset: no `position`, no `margin`, no `z-index` — pin and space with flex `justify-content` / `align-items` / `gap` / `padding`, exactly as the markup above does.
