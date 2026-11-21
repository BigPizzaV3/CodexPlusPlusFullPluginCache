# Codex Implementation Task — EW Manim Draw v0.3

## Goal
Upgrade the existing personal Skill (NOT a public Plugin, NOT an MCP service) to premium professional technical infographic quality while retaining v0.2 compatibility. Use the attached reference image only as a quality benchmark, not as a license to copy artwork or invent features.

## Source baseline
- Preserve the entire original v0.2.2 ZIP contents and existing stable JSON behavior.
- Read `ew-manim-draw/references/visual-design-standard-v0.3.md` and `ew-manim-draw/SKILL.md`.
- `ew-manim-draw/scripts/render_preview.py` is a Pillow fallback, not Manim. No MP4 implementation currently exists.

## Deliverables in order
1. Implement a backward-compatible v0.3 JSON extension: themes (`dark_tech`, `light`), grid layouts, node icon references, semantic groups, and `flow_light` timeline event. Reject unknown/unsafe paths and maintain strict graph semantics. Keep v0.2 inputs valid.
2. Implement deterministic layout for up to 15 numbered cards in multi-row grid. No overlap, clipping, tiny typography or unexpected cropping. Allow vertical continuous infographic layouts as a separate mode.
3. Implement dark-navy/cyan card rendering and true flowing light pulses along edges, with **all nodes visible from frame one** by default. Respect explicit `appear` animations in legacy v0.2.
4. Render static PNG and smooth animated GIF locally; optionally implement MP4 only if Manim/ffmpeg are truly available and tested. If unavailable, state that clearly and provide JSON + PNG/GIF.
5. Add font fallback for Traditional Chinese, Simplified Chinese and English; verify text metrics and contrast. Never package font files.
6. Add visual QA: bounding-box collision, overflow, minimum font sizes, contrast, edge direction, icon provenance, frame sequence continuity, dimensions, and technical content cross-check.
7. Produce three independent test outputs: 3-node legacy regression; 10-node industrial flow; 15-stage complex flow. Include automated tests and before/after image comparisons.
8. Update README, schema reference, and version markers. Keep Skills-only identity; no MCP endpoints, network calls, or fabricated visual claims.

## Acceptance gates
- v0.2 sample validates and renders unchanged with legacy renderer option.
- v0.3 dark-tech example renders with all nodes present on first frame, flow-light moving visibly between at least 3 successive frames.
- 15 cards remain readable without overlaps at declared target resolution.
- Text has no missing CJK glyphs or cropping; no invented equipment or logos.
- JSON parser never executes embedded code, shell or user-supplied paths.
- Unit tests pass, and rendered outputs are visually inspected at final size.
- User gets a complete updated ZIP and a truthful changelog. No claim of completion until tests pass.

## Explicit constraints
No external upload; no unrelated changes to other EW skills; do not replace the existing source of truth with generated images; no sprite sheets presented as final individual images.
