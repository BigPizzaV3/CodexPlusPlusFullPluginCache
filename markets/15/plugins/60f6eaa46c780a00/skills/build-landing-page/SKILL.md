---
name: build-landing-page
description: Plan and build a whole landing page, homepage or marketing site from curated vibrant.design references - an overall look plus a reference per section (hero, logos, features, testimonials, pricing, CTA, footer) that the user picks, optionally turned into a moodboard and design direction first. Use when the user asks to create, design or redesign a landing page, homepage, marketing site, product page or website.
---

# Build a landing page from Vibrant references

Uses the Vibrant MCP server. If its tools (`suggest_designs`, `create_board`, `get_design_md`, …) are not available, tell the user they can connect Vibrant at https://vibrant.design/dashboard/agents, then build without references.

## 1. Brief and project

- If the request misses the product, the audience or the mood, ask at most 3 short questions in one message. Ask which sections they want only if they mention something unusual; otherwise use the default page.
- Read the project: framework, styling system, components, any `DESIGN.md` or tokens. An existing design system wins over references for tokens; references give structure, rhythm and motion.

## 2. Suggest references

Call `suggest_designs` with `brief` (product, audience, mood in one or two sentences), `style` when one is clear (`dark-mode`, `minimal`, `playful`, `editorial`, `gradient`, `glassmorphism`, `3d`, `retro`, `monochrome`, `neon`, …) `motion: true` if the page should feel animated, and `limit` 3. Omit `sections` for the default page (hero, logo cloud, features, testimonials, pricing, CTA, footer), or pass the user's list in page order.

If the user has no direction yet ("show me what's out there first"), start with the `design-inspiration` skill, then come back here with what they liked.

Present it in two steps. For each step call `show_designs` with the options (`projectId` + a one-line `note` with the why, `title` such as "Overall look" or "Hero"), so the user sees the covers. In text keep it compact: name, why, the vibrant.design link, the live site, creator. No markdown images, no `media.url` links; never web or image search for pictures of a design:

1. **Overall look**: the `websites`. Ask the user to pick one.
2. **Per section**: 2–3 options each. Ask for one pick per section (for example "hero 2, features 1, pricing 3", or "you pick the rest"). Sections with a `note` have no gallery designs: they follow the overall look.

Wait for the picks.

## 3. Choose the path

Ask which path the user wants:

- **Quick**: build straight from the picks (go to step 5). Works for everyone.
- **Direction** (recommended for a whole site; needs a plan, and the build uses credits): one moodboard and one design direction, so every section shares the same system. Go to step 4.

## 4. Direction path

1. `create_board` with a short name and the brief as the description.
2. `create_group kind=page title="Home"`, then for each section `create_group kind=section role=<section> parentGroupId=<page id>`, and `add_designs_to_board groupId=…` with that section's picks. The overall pick goes in with no `groupId` (global). `add_note` for every hard constraint (brand colors, must-haves, things to avoid). If `create_group` is refused, keep every card global and add one note per section naming its cards.
3. `analyze_board_references`, then poll `get_build_status` until `analysis.readyToBuild` is true.
4. Tell the user `build_direction` uses credits and call it only after they say yes. Poll `get_build_status` until `direction.state` is `ready`.
5. `get_board_direction`: summarize the direction in a few lines and list every open conflict with its sides. Ask the user to decide each one and save the answers with `decide_conflict`. Never pick a side yourself.
6. `get_design_md boardId=…` and save it verbatim as `./DESIGN.md`. `get_board_direction section=sections` gives each section's guidance.

## 5. Quick path: guidance per pick

For each pick follow `nextSteps` from `suggest_designs`:

- `ready` with a plan: `get_design_md projectId=…` (save as `docs/design/<slug>.DESIGN.md`) and `get_design_style projectId=…`.
- Not analyzed, with a plan: `analyze_design` without `confirm`, tell the user the total cost for all picks, and only on yes call each with `confirm=true`.
- No plan: use the cover images and pages as visual references. Mention once that a plan unlocks DESIGN.md and build notes (https://vibrant.design/pricing).

Unify the picks into one token set (colors, type, spacing, radius, shadows) taken from the overall pick, so the sections look like one site.

## 6. Build top to bottom

- Open each reference's cover and media links and look at them before writing the section. The media is ground truth; values marked inferred are estimates.
- One section at a time, in page order, all sharing the same tokens. Check each one at mobile and desktop widths before the next.
- Take layout, hierarchy, rhythm, type scale, color roles, surfaces and motion. Never take copy, logos, brand or product names, screenshots, illustrations or photos, and don't make a 1:1 clone. Write the copy for the user's product.
- Semantic landmarks and one `h1`, keyboard reachable, WCAG AA contrast, `prefers-reduced-motion` respected, sized media, fast first paint.

## 7. Wrap up

Summarize the page: sections built, which reference informed each one, the files changed, and anything the user should check (inferred colors and fonts, placeholder images). On the direction path, point to `./DESIGN.md` as the source of truth for later UI work.
