---
name: product-screen-illustrations
description: Choose HubToolify illustration scenes for the screens of an app or website, such as onboarding, empty states, errors, success messages, sign-up or help pages. Use when the user is designing a product and needs pictures that fit specific screens with one consistent look.
---

# Illustrations for product screens

Explicit instructions from the user always come first.

## Workflow

1. **List the screens** the user needs pictures for. If they only described the product ("a budgeting app"), propose the usual set: welcome or onboarding, empty state, success, error or offline, and help.
2. **Search per screen** with `search_illustrations`, using the screen's purpose plus the product's subject as `query` (for example "empty inbox", "welcome", "success", "no results", "team"). Use a small `limit` such as 6.
3. **Keep one look.** Each result has a `pack`. Prefer scenes from the same pack so the screens look like one product. Once a good pack shows up, search again with `pack` set to it for the remaining screens.
4. **Animated scenes** suit onboarding and success screens. Set `animated` to true when the user wants motion.
5. **Report** a short table: screen → scene name (pack). Point out any screen with no good match and offer the nearest scene instead of inventing one.
6. **Downloads when asked:** `get_illustration` with the scene name. Still scenes come as SVG; animated ones also as MP4, GIF and Lottie JSON.

## Rules

- Use only scene names that `search_illustrations` returned.
- When a result says illustration downloads are not included in the connected account, say so plainly; the previews stay available. Do not mention prices.
