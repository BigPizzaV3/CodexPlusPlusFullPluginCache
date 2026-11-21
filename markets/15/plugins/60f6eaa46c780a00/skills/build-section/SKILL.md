---
name: build-section
description: Build or redesign one website section (hero, navbar, features or bento grid, pricing, testimonials, logo cloud, stats, how it works, FAQ, CTA, footer, sign-in, 404) starting from curated vibrant.design references the user picks. Use when the user asks to create, design, redesign, restyle or improve a section or block of a marketing site, landing page or homepage.
---

# Build a section from Vibrant references

Uses the Vibrant MCP server (`suggest_designs`, `show_designs`, `get_design_md`, `get_design_style`, `get_design_status`, `analyze_design`). If those tools are not available, tell the user they can connect Vibrant at https://vibrant.design/dashboard/agents, then build the section without references.

## 1. Read the project first

- Framework, styling system (Tailwind config, CSS variables, CSS modules), component library, and the sections that already exist.
- Look for a `DESIGN.md`, design tokens or a theme file. If the project has its own design system, keep its tokens (colors, fonts, radius, spacing) and take only structure, hierarchy, rhythm and motion from the reference.

## 2. Get options

Call `suggest_designs` with:

- `sections`: one kind. Map the user's words: header/nav/menu → `navbar`; logos/social proof/trusted by → `logo-cloud`; bento/feature grid/benefits → `features`; steps/process → `how-it-works`; plans → `pricing`; reviews/quotes → `testimonials`; numbers/metrics → `stats`; questions → `faq`; sign-up banner → `cta`; sign in/sign up → `auth`; error page → `not-found`.
- `style`: only when the user or the existing site has a clear style, e.g. `dark-mode`, `minimal`, `playful`, `editorial`, `gradient`, `glassmorphism`, `3d`, `retro`, `monochrome`, `neon`, `micro-interactions`, `scroll-animations`.
- `brief`: one sentence with the product, the audience and the mood.
- `motion: true` when the section should move (animated hero, scroll reveals, hover or micro-interactions): video designs rank first, and their `media.url` is the clip to study.
- `limit`: 4.

## 3. Let the user pick

Call `show_designs` with the options in order (`projectId` + a one-line `note` with the why, `title` such as "Hero options"), so the user sees the covers with View on Vibrant and Live site links. Then show them compactly in text, one per line block:

```
1. **Night Hero** · Hero design · Dark Mode style · DESIGN.md ready
   https://vibrant.design/p/night-hero
```

Do not write markdown images and do not link `media.url` to the user: `show_designs` shows the covers, and the user watches motion on the vibrant.design page. Give the live site link. Never use web or image search for pictures of a design. Credit the creator when the card has one.

Ask: "Which one should I build from? A number, 'mix 1 and 3', or 'you pick'." Then wait. If the user already said to just build it, take the top option and say why in one line. If the section came back with a `note` (no designs of that kind), say so and offer the website references or `search_designs`.

## 4. Get the guidance for the pick

Follow `nextSteps` from the response for the pick's `analysis`:

- `ready` and `access.designMd` true: `get_design_md projectId=…` (save as `docs/design/<slug>.DESIGN.md`) and `get_design_style projectId=…` (build notes). Free.
- `analyzing`: poll `get_design_status` every few seconds, then as above.
- `none` or `error` with a plan: call `analyze_design` **without** `confirm`, tell the user the credit cost and balance, and only if they say yes call it again with `confirm=true`. If they decline, continue from the cover image.
- No plan (`access.designMd` false): use the cover image and page as a visual reference. Mention once that a plan unlocks DESIGN.md and build notes (https://vibrant.design/pricing). Don't repeat it.

Then open the cover image and media links and look at them. The prose is a summary; the media is ground truth. Values marked inferred are estimates: tune them by eye. For motion, rebuild the effect with CSS transitions or animations, the Web Animations API, or the motion library the project already uses, with a calm fallback under `prefers-reduced-motion`.

## 5. Build

- Take from the reference: layout and grid, visual hierarchy, spacing rhythm, type scale and pairing, color roles, surfaces and depth, motion character, interaction details.
- Never take: its copy, logos, brand or product names, screenshots, illustrations or photos. Write the copy for the user's product and use their assets or neutral placeholders. Don't make a 1:1 clone.
- Mobile-first, semantic landmarks and headings, keyboard reachable, WCAG AA contrast, `prefers-reduced-motion` respected, sized media (no layout shift).
- Follow the project's conventions for components, naming and styling.

## 6. Wrap up

- List what came from the reference (one line per idea) and the files you changed.
- Offer to save the pick to a Vibrant moodboard so the rest of the page can follow the same direction (`create_board`, then `add_design_to_board`). For a whole page, use the `build-landing-page` skill instead.
