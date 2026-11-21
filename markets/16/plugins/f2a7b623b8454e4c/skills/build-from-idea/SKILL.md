---
name: build-from-idea
description: Build a complete working website, web app, PWA, native Apple app, Android app, or cross-platform app from a product idea, including design direction and actual verification where available.
---

# Build From Idea

Use when the user's intent is to **make/build/create/implement** an app. Do not respond only with a tech stack or mockup when code tools exist.

1. Read `../../references/platform-choice.md`, `../../references/execution-model.md` and `../../references/design-quality.md`. Capture user outcome, core workflow, intended platform, data/auth constraints and minimal complete vertical slice. Honor a requested framework; otherwise choose by needs and document the rationale.
2. Inspect repository/environment or create a new runnable workspace using current tool-supported commands. Existing code is authoritative over preferred defaults.
3. Design-first, not design-only: prepare a short reference-backed visual direction (type, composition, color, density, navigation, signature details); inspect user sources first. Read `../research-design-direction/SKILL.md` and `../create-design-system/SKILL.md`. If user requests concept selection, stop for approval; otherwise choose a defensible direction and implement it.
4. Specify key screens and functional states: initial, empty, loading, error, disabled, success, permission and mobile/large-screen behavior. Read `../design-app-flows/SKILL.md`.
5. Implement real navigation/state/data boundaries, not inert fake buttons. Choose the focused platform skill and `../design-backend/SKILL.md` if server/data work is needed.
6. Secure any user data and implement accessible controls. Read `../secure-app/SKILL.md` for authentication, uploads or sensitive integrations.
7. Run actual builds/tests. Capture browser or simulator renders and compare to design direction where tools permit. Use `../test-app/SKILL.md` and `../review-visual-ux/SKILL.md`; fix significant findings and rerun.
8. Use `../orchestrate-agents/SKILL.md` for genuine subagents when available; otherwise perform roles sequentially without fabricating reports.
9. Return source paths/links, commands and actual test output, design decisions, known failures and unverified items. Do not claim submission or deployment without actual action and permission.

Completion: one real user workflow executes successfully **when execution tools exist**, or disclose the precise execution blocker.
