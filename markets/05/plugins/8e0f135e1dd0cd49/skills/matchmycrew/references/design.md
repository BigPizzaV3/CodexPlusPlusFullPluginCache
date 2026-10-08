# MatchMyCrew design reference

MatchMyCrew's implemented visual language is a production sheet: strict editorial
grid, fine rules, compact utility labels, and expressive monochrome production imagery.
It is not a generic SaaS dashboard, default shadcn theme, or decorative mood board.

## Non-negotiables

- Use semantic tokens `ink`, `paper`, `soft`, `quiet`, and `line`; do not introduce a
  competing neutral palette, brand accent, gradient, glass effect, or coloured status
  treatment.
- Use Instrument Sans for reading/display type and DM Mono only for eyebrows, locations,
  prices, counters, and concise metadata. Headings are tight and declarative.
- Default geometry is 3px radius, 1px rules, and approximately 45px interactive height.
  Avoid soft card shadows; the primary landing search and map markers may use the
  established hard ink offset shadow.
- Public pages use generous editorial rhythm and CSS grid. Design mobile first at the
  560px and 900px thresholds, with the discovery map's explicit mobile tabs and desktop
  side-by-side layout respected.
- Provider cards are image-led and low-chrome: near-square grayscale imagery, then
  location/rate, name/verification, role, service tags, and rating or “New”.
- Keep motion as short state feedback only; respect reduced-motion preferences.

## Accessibility and interaction

Every control needs an accessible name, visible focus, keyboard operation, adequate
contrast, and a usable touch target. Never make the map the only way to reach a result.
Keep active filters visible and individually removable. Empty, loading, success, and
error states should say what happened and what the user can do next.
