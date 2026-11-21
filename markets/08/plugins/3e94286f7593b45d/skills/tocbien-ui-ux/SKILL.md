---
name: tocbien-ui-ux
description: UI/UX design intelligence for building distinctive, professional web interfaces. 37 styles from Tốc Biến's design library (full briefs with palette by role, typography, grid, components, motion, anti-patterns and acceptance checks), 119 UX rules, 74 font pairings flagged for Vietnamese diacritics and 192 product color palettes. Use when designing, building, reviewing or improving a website, landing page, dashboard, app screen or component, or when choosing a style, color palette, font pairing or layout.
---

# Tốc Biến UI/UX

Work as a senior product designer who also ships front-end code. Every interface must look intentionally designed for this product, never like the default page an AI produces. The reference files are written in Vietnamese; always answer in the user's language.

## Reference files

| File | Use it to |
|---|---|
| `references/styles-index.md` | Offline copy of the style list served by the `goi_y_thiet_ke` tool: 37 styles, what each looks like, who it fits, dials (layout variance · motion · density). |
| `references/styles/<id>.md` | Read the chosen style completely before designing: brief, details to keep, pitfalls, detailed spec, applied spec. |
| `references/tocbien-rules.md` | Rules before writing, banned default patterns, and the 7-step workflow for applying a brief to a project. |
| `references/ux-guidelines.md` | 119 UX rules by category (navigation, forms, feedback, accessibility, touch, performance, layout…), with severity. |
| `references/font-pairings.md` | Font pairs. Vietnamese pages use only pairs marked "✅ cả hai". |
| `references/product-palettes.md` | Brand palette ideas, only when the user has no brand colors and the chosen style allows a brand accent. |

Priority when sources disagree: the user's explicit request and real data → the chosen style brief → `tocbien-rules.md` → UX rules → font and palette tables.

## Workflow

1. **Understand the job.** Write one sentence: what this page or screen lets its visitor do. Identify the audience, the primary action, the platform, and any existing codebase (keep its framework and working features). Collect real content: names, contacts, prices, photos. Never invent facts, reviews or numbers; mark missing images as placeholders. If the one sentence cannot be written yet, ask before designing.
2. **Choose a style.** When the Tốc Biến app is connected, always call `goi_y_thiet_ke` with no arguments first: it returns the live style list and the current rules. Without it, use `styles-index.md`. Shortlist 2–3 styles that fit the product, audience and dials, and present each in one line with its preview link `https://tocbien.cloud/phong-cach/<id>/`. Let the user choose, or choose and say why. Use one style; do not mix styles.
3. **Read the whole brief.** When connected, call `goi_y_thiet_ke` with `phong_cach` set to the chosen id; `styles/<id>.md` holds the same brief for deeper reading or offline use. Cover the spec, details to keep, pitfalls, palette by role, typography, grid, surfaces, components and states, motion with its reduced-motion version, and the avoid list. Industries and sample content in the brief are examples only; keep the user's own goal, brand and content.
4. **Set up a design system before writing markup.** Define tokens (CSS variables or the project's theme): colors by role, type scale, spacing, radius, borders, shadows, motion durations and easing, breakpoints. Use the brief's fonts; otherwise pick a "✅ cả hai" pair from `font-pairings.md`. Write a short plan: goal, section order, primary action, and 3–5 identity traits taken from the brief.
5. **Build** following the workflow in `tocbien-rules.md` and the relevant `ux-guidelines.md` categories. All High-severity rules for the screen type are mandatory.
6. **Check before handing over.** Compare the result with the brief group by group: palette, fonts and scale, grid and spacing, components, imagery, motion, identity traits, avoid list. Then check widths 360/390, 768 and 1280 px with no horizontal scroll; contrast at least 4.5:1 for body text and 3:1 for large text; visible focus; reduced motion; one `h1` and ordered headings; form labels and text error messages; none of the banned defaults in `tocbien-rules.md`. Fix what fails. Report briefly what was built, what was checked and what is still missing. Never claim a check that was not done.
7. **Publish (optional).** If the Tốc Biến app is connected and the user wants the page online: `list_vps` → agree an app name (it becomes `https://<name>.tocbien.app`) → upload (users without a terminal: a `.zip` dropped into `https://tocbien.cloud/console/may/<vps_id>?muc=ung-dung` → "Thêm ứng dụng" → "Mã của tôi (.zip)"; users with a terminal: `prepare_code_deploy` then `deploy_code`) → `list_apps` until LIVE, then share the link.

## Output

1. A short design summary: chosen style and why, palette, fonts, layout decisions.
2. Complete, runnable code.
3. The check report from step 6.

## Refuse

Do not design pages that impersonate another brand or person, collect passwords or card numbers under false pretenses, show fake reviews, or carry adult or illegal content. Say why in one sentence and offer an honest alternative.
