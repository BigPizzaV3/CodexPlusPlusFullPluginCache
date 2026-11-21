# Cerca.me plugin 1.0.0

Connect your Cerca account to recall places, plan travel from personal taste
and friends' recommendations, and record saves, ratings and notes.

This package connects the existing Streamable HTTP server at
`https://cerca.me/mcp`. The host performs OAuth discovery and sign-in.
No bearer tokens, client secrets or reviewer credentials belong in the package.

- `plugin.json`: public listing, five positive and three negative review cases,
  and release notes.
- `mcp.json`: the production server connection.
- `skills/places-and-trip-planning/`: workflow guidance and tool reference.
- `assets/icon.png`: Cerca's existing 512 × 512 brand icon.
- `assets/icon-dark.png`: a 512 × 512 brighter blue variant for dark mode,
  rendered from the accompanying SVG with the original skyline geometry.
- Listing colors: `#0A84FF` for light mode and `#60A5FA` for dark mode,
  taken from Cerca's existing logo and dark-theme interface accents.
- `review-setup.md`: reproducible reviewer fixtures and walkthrough.
- Demo recording: <https://www.loom.com/share/bdfb3ef1293b43708d5f313b5ca34a5e>,
  included in the review metadata. Public playback was verified; full review-case
  coverage remains to be checked.

The source and draft archive are prepared for further submission work.
Readiness is tracked separately in `docs/reviews/cerca-plugin/preparation.md`
in the source repository. The publisher is Arvin Dang, the category is Travel,
availability is all supported countries, and commerce is declared false.
The empty countries array intentionally removes country restrictions.
Do not treat a structurally valid draft as ready for public review.
