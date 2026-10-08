# React reference integration

The bundled `assets/react/TradingCard.jsx`, `useCardMotion.js`, and `Card.css` were extracted from ParallaxProj. Copy them together into the target app, then adapt names, text, art paths, colors, and dimensions. The JSX uses React and `Droplets`/`Sparkles` from `lucide-react`; replace icons if the target uses another library. Do not blindly replace its package manifest.

## Inputs and styles

The component expects `finish` (`holographic`, `gold`, or `silver`), `depth` (0–100), `autoRotate`, `foil`, `exploded`, `flipped`, `setFlipped`, and a `focusRef` created with `useRef(null)`. Supply every prop. Example parent setup:

```jsx
const [flipped, setFlipped] = useState(false)
const focusRef = useRef(null)
return <>
  <TradingCard finish="holographic" depth={70} autoRotate={false}
    foil={true} exploded={false} flipped={flipped}
    setFlipped={setFlipped} focusRef={focusRef} />
  <p id="card-instructions">Move over the card to tilt. Enter flips; arrow keys tilt; Home resets.</p>
</>
```

The source references `/assets/astral-world.png` and `/assets/astral-dragon.png`; change them to the actual supplied/generated assets and update the subject alt text and accessible name. For multiple cards, parameterize `card-instructions` and its `aria-describedby` to avoid duplicate IDs. Asset URLs must respect the target app's deployment base path.

The stylesheet expects a parent stage with space for the projected card, protruding subject, shadow, and optional exploded view. It is not a complete page stylesheet. Add scoped `box-sizing: border-box` to the card subtree, a suitable font stack, and accessible text/focus colors. Source typography uses Manrope and DM Serif Display; these are optional and not bundled. The back-face BrandMark needs the following styling or should be replaced with the requested logo:

```css
.brand-mark { display: inline-block; position: relative; width: 32px; height: 36px; flex-shrink: 0; }
.brand-mark i { position: absolute; inset: 6px 4px; border: 1.7px solid currentColor; border-radius: 3px; transform: rotate(-27deg); }
.brand-mark i:nth-child(2) { transform: rotate(-3deg); }
.brand-mark i:nth-child(3) { transform: rotate(21deg); background: var(--paper, #34594b); }
.brand-mark i:nth-child(3)::after { content: '✦'; position: absolute; inset: 1px; display: grid; place-items: center; font-size: 17px; }
.brand-period { color: #6e865c; }
```

For a standalone embedded component, scope the supplied class selectors to avoid collisions. Replace viewport-only widths with container-aware sizing when embedding in narrow panels; reserve room for the transformed bounds. The source widths are tuned to its gallery, not every possible host container.

## Motion contract

`useCardMotion({ depth, autoRotate, enabled })` returns `{ cardRef, bind, reset, reducedMotion }`. Attach `cardRef` and all `bind` handlers to the motion wrapper. Compose custom handlers with the supplied handlers as the JSX does; do not silently override pointer cancellation, blur, or keyboard reset.

The hook writes `--rx`/`--ry` (degrees), `--px`/`--py` (depth-scaled normalized displacement), `--mx`/`--my` (light percentages), and `--lift` (depth-scaled engagement). CSS multiplies displacement by fixed pixel distances, not by depth a second time. The hook disables tilt while the example card is flipped.

The reference already handles reduced motion, visibility changes, elapsed-time smoothing, frame settling, touch capture cleanup, and drag-versus-click suppression. Preserve those behaviors when extracting or porting it. When refining pointer tracking, prefer measuring a stable untransformed hit region to avoid feedback from the tilted element's changing bounding rectangle.

Exploded mode forces a front-facing presentation in the original parent. If adding controls, clear `flipped` when entering exploded mode and clear `exploded` when flipping, so the two presentations do not conflict. A settings reset should also call the motion reset when it promises to reset orientation, rather than only restoring props that may already have their default values.
