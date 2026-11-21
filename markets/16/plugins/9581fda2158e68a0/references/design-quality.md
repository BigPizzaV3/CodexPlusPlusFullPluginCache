# Design quality gates for MCP Apps

## Design principles
- Task-first: primary action and meaningful data in view without scrolling through decoration.
- Host-aware: resizes gracefully inside constrained iframe surfaces and supports dark/light contexts where exposed.
- Purpose-built: choose product-specific typography, density, spacing, hierarchy, iconography and motion. Do not stamp one dashboard pattern on every app.
- Honest: real content, no fake metrics, loading/empty/error/permission/success states, truthful disabled actions.
- Interactive: explicit action semantics, feedback, keyboard and screen-reader support.

## Review rubric (0–4 per dimension)
1. Utility and information architecture: obvious user goal, minimal unnecessary steps.
2. Visual hierarchy and personality: deliberate typography, spacing, color, and content density.
3. Interaction completeness: handlers, confirmation, validation, feedback and recovery.
4. Responsiveness: narrow and wide host containers, overflow and touch targets.
5. Accessibility: contrast, labels, focus, keyboard, reduced motion.
6. Security of UI interaction: sanitized rendering, restricted CSP, server-authorized tool calls.

Score is *advisory*, not a substitute for executable checks. No release with unresolved critical UX failures (e.g., invisible button, trapped focus, broken action) regardless of average.

## Reference selection
Use `design-references.md` for sources. Translate a reference into **principles** (typographic scale, rhythm, hierarchy, interaction), not an unauthorized copied asset. Prefer 1–3 relevant references per project. Verify source licensing when reusing code. Never auto-import skills from third-party directories.
