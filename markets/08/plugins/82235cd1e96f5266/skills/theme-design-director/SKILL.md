---
name: theme-design-director
description: Choose, inspect, generate or apply a Theme Emporium widget theme, safe font and palette directly through ChatGPT MCP tools.
---

# Theme Design Director

Use this skill when a user wants a visual direction, wants to browse Theme Emporium themes, asks to change the font/colors/background of the Theme Emporium plugin inside ChatGPT, or wants a new non-persistent theme preview.

## Goal

Turn a product brief into one clear visual direction without redesigning the product unnecessarily. Treat typography, background, color, and effects as a coordinated system rather than independent decorations.

## Inputs

Use the information the user already provided. Useful inputs include:

- product type and audience
- desired tone or mood
- light/dark preference
- readability or accessibility constraints
- typography preferences
- background or wallpaper preference
- colors to prefer or avoid
- desired glass, shadow, radius, or depth

Do not ask for every field when the brief is already sufficient. Make conservative defaults and state them when needed.

## Workflow

1. **Understand the brief.** Summarize the intended product feeling in one sentence.
2. **Prefer a catalog match when appropriate.** Use `list_themes` when the user wants options or has not named a theme. Shortlist only the most relevant candidates.
3. **Inspect before recommending.** Use `get_theme_details` for a named theme or shortlisted candidate before making detailed claims about its tokens.
4. **Apply when asked.** For commands like 'make Black Gold Luxe use Georgia and gold buttons', call `apply_theme_appearance` with the exact catalog slug and safe optional color/font/background parameters. ChatGPT provides the interpretation; no separate AI Gateway is necessary.
5. **Generate only when a new direction is needed.** Use `generate_theme` when the catalog does not fit or a new non-persistent preview is requested.
6. **Keep the system coherent.** Explain how typography, background, palette, and effects reinforce the same visual intent.
7. **Return a decision-ready handoff.** Make it easy for the user to understand what to use next.

## Output format

Return these sections when relevant:

- **Direction** — one-sentence visual concept.
- **Source** — existing Theme Emporium theme or generated preview.
- **Typography** — recommended font direction and why it fits.
- **Background** — color, gradient, or wallpaper direction.
- **Palette** — primary, secondary, background, and readable text direction.
- **Effects** — glass blur, radius, shadow/depth direction.
- **Key tokens** — concise structured token summary when available.
- **Why it works** — 2–4 concrete design reasons.
- **Next step** — inspect another catalog option or continue with the preview.

## Tool routing

- Use `list_themes` for catalog discovery.
- Use `get_theme_details` for factual details about an existing Theme Emporium theme.
- Use `generate_theme` only for a new structured preview.
- Use `apply_theme_appearance` for an explicit command to change the Theme Emporium widget appearance inside ChatGPT. Map natural language to `themeIdOrSlug`, `font` (`inter`/`system`/`georgia`/`mono`), and optional six-digit hex text/button/background colors and `solid`/`gradient` mode.

Never invent catalog themes or exact token values. Retrieve them when they matter.

## V1 boundaries

`generate_theme` is **non-persistent preview only**. Never tell the user that a generated preview was saved, published, purchased, added to the catalog, or attached to an account.

An appearance applied in this way changes the **Theme Emporium embedded widget only**. It does not and cannot restyle the ChatGPT shell, Chrome browser UI, or other unrelated websites. Its `widgetState` is per-widget, not a durable account-wide preference. Never say a change has synced across conversations or devices unless authenticated persistence has been separately implemented and verified.

The V1 plugin does not expose tools for:

- payments or subscriptions
- admin changes
- account mutation
- uploads
- public publishing
- destructive actions

If the user asks for one of those actions, explain that it is outside the current Theme Emporium V1 tool surface and continue with the safe design workflow if useful.

## Design principles

- Preserve an existing polished product shell unless the user explicitly asks for a redesign.
- Prefer perceptible, useful changes over decorative churn.
- Keep text/background contrast readable.
- Use one strong type direction, one dominant background direction, and one coherent palette before adding effects.
- Effects should support hierarchy, not obscure content or controls.
- When comparing directions, explain tradeoffs instead of declaring one universally superior.

## Stop conditions

Stop and ask for a missing decision only when it materially changes the result, such as mutually exclusive light/dark requirements or a required brand color that has not been provided. Do not block on optional preferences.
