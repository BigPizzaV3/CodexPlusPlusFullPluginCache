# EW Visual Design Standard v0.3 — 視覺工程規範

## Objective
Deliver information-design quality comparable to premium engineering infographics: coherent hierarchy, technical semantic correctness, readable typography, consistent icons, and motion that communicates causal flow. Do not confuse more glow with better information design.

## Layout and composition
- Layout first: determine narrative, numbered stages, hierarchy, arrows and semantic grouping before choosing icons.
- Use a 12-column grid (or a proportional grid for 16:9). Fixed card anatomy: index → heading → semantic illustration → 1-line key data → 1–2-line explanation.
- Default 16:9 1920×1080; for >8 stages prefer a multi-row overview with full visibility or a long vertical document. Do not compress 15 stages into a single unreadable 16:9 frame.
- Consistent gutters and alignment; no overlap, clipping, random decoration, or line crossings where avoidable.
- Support portrait A4 continuous HTML as a separate output type, without slide buttons or print UI unless asked.

## Color and text
- Dark palette (suggested): canvas #090F1B, surface #121E30, border #2C425A, text #F4F7FB, secondary #AFBDD0, accent #5DE0D0, information #5BBEF8, caution #F5C66A. All semantic text must remain readable without relying on hue alone.
- Light palette remains optional. Never enforce brand colors when the user has supplied a different palette.
- Text is deterministic typography. Use a CJK-capable font legally installed in the execution environment. Do not bundle proprietary fonts.
- For 1920×1080: heading 64–84 px, card title 26–34 px, card body 22–26 px; avoid tiny 12 px labels. Scale according to card count and viewing distance; if content cannot fit, change layout instead of shrinking below readability.
- Target WCAG AA contrast for normal text where practical; test 4.5:1 for text and 3:1 for large labels.

## Icons
- Prefer one consistent vector icon family. Distinguish process, data, authorization, runtime, evidence and audit using meaningful symbols.
- No fictitious industrial hardware or unauthorized alterations to logos. Source-supplied hardware images must be preserved, not regenerated.
- Use icon assets as separate layers with stable IDs, licensing provenance, and deterministic size.

## Motion
- Architecture overview default: all content visible at t=0; animate arrows as subtle moving cyan/white light pulses from dim to bright.
- Loop continuously with no flicker, no sequential box appearances, no dramatic camera movement. Flow direction must match the source graph.
- Timeline event `flow_light` is a proposed v0.3 extension. Existing v0.2 validator rejects it; do not claim support until Codex implements schema, renderer and tests.
- Prefer true interpolation at 24–30 fps for motion. Current Pillow fallback only uses discrete event frames; label it honestly.

## Truth & validation
- Derive graph facts only from source documents or approved user instructions. Mark uncertainties explicitly.
- Validate graph structure, arrows, RACI/technical facts, labels, text overflow, typography, aspect ratio, animation continuity, and brand assets.
- Save the final frame and a 3-frame contact sheet for automated inspection; contact sheets are QA artifacts only, never a substitute for separately requested output frames.
- No false claims of MP4 support, live Manim support, or completed quality checks.
