---
name: app-screens
description: Design app or website screens in Builderii as a clickable prototype, such as onboarding, a checkout, a dashboard or every screen of an app idea, from a description, this conversation or a screenshot. Use when the user asks for screens, wireframes, a mock-up, a UI, a prototype or an app design in Builderii.
---

# Design app screens in Builderii

1. **Which board.** Use the board the user named (`search` / `list_boards`); otherwise `create_board` with kind `prototype` and a specific name.
2. **From a screenshot or sketch?** Call `generate` with `type: "app_screens"`, the `image_url` and a short prompt. Otherwise plan the screens yourself.
3. **Plan the flow.** 3 to 8 screens for an app (1 to 3 for a website), each with a short id (`home`, `detail`) and a name. Every screen reachable; each has one clear primary action.
4. **Draw them** with `create_app_screens`: `platform` (`mobile` unless it's a website: `web`), and each screen's components top to bottom with real content (names, prices, dates, no lorem ipsum). Mobile screens start with a `topbar` and end with a `tabbar` for the main sections; web pages start with a `navbar`. Put side-by-side components on the same `row`. Set `linkTo` on buttons, list items, cards and tabs so the prototype plays.
5. **Fix the links** with `link_screens` if a tap is missing, and set the `start` screen.
6. **Changes later:** `list_diagrams` → `get_diagram` → `update_app_screens` with only the screens that change (all their components) or are new.
7. **Confirm** in two or three lines: the screens, the main path through them, and the board's link (press Play in Builderii to click through).
