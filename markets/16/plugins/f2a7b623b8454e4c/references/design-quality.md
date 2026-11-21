# Product-quality design standard — no templated AI slop

## Start with product intent
Identify whether you're building an editor, data dashboard, landing page, mobile utility, consumer app, administrative console, commerce flow or AI experience. Each needs different hierarchy, density and interaction patterns. Preserve the user's reference and brand. Ask whether user wants an original direction or faithful recreation.

## Design direction deliverable
Before making UI, capture typography roles, responsive container/grid, color roles with contrast checks, spacing and radius rhythm, information density, icon family, media treatment, motion principle, screen-state inventory and one signature visual behavior justified by the user flow.

## Typical failure patterns to correct
- Generic purple-on-white gradient, too many rounded cards and decorative badges.
- Hero sections that obscure actual app capabilities; fake dashboards and inert controls.
- Inconsistent typography, arbitrary padding and low information hierarchy.
- Beautiful default screen but missing empty/error/loading/permission/success states.
- Motion everywhere without semantic purpose or reduced-motion handling.
- Unreadable charts, misleading scales, inaccurate sample metrics and fabricated testimonials.
- Mobile layout that is just desktop squashed; native mobile app that looks like a web page.
- Copy-pasted gallery components with mismatched visuals or accessibility issues.

## Implementation rules
- Design systems are semantic: use tokens and variants; avoid one-off style guesses.
- Use realistic text and clearly identified sample data; do not fabricate claims.
- Responsive and adaptive: test narrow/wide screens, touch targets, long content, keyboard/screen reader and color contrast.
- Screens and flows: test empty/loading/error/success/permission/offline where relevant.
- Visual QA compares implemented renders to user reference or approved direction. Code analysis alone is not screenshot proof.
- Only animate to communicate transitions, state or focus; respect reduced motion and performance budgets.

## QA matrix
Score hierarchy, typography, composition, component consistency, interaction, accessibility and product completeness. Use specific evidence and a fix ledger; numeric subjective scores never replace real tests. For faithful visual work, compare screenshots at matching viewport; don't claim exact pixel fidelity without measuring.
