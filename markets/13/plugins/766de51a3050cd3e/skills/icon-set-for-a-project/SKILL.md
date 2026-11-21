---
name: icon-set-for-a-project
description: Build a matching set of HubToolify icons for an app, website, slide deck or document. Use when the user wants several icons that belong together (a navigation bar, a feature list, a dashboard, a menu), or asks for icons for their project.
---

# Icon set for a project

Explicit instructions from the user always come first. If they name icons, a style, a size or a colour, follow that.

## Workflow

1. **List the concepts.** Turn the request into a short list of things the icons must show, one word or phrase each (for example: home, search, profile, settings, cart). If the user gave only a project type ("a food delivery app"), propose 6–10 concepts and go ahead with them; the user can change the list later.
2. **Pick one style for the whole set.** Use the style the user asked for, otherwise `line`. Every icon in the set uses the same style so they look like one family. Styles: line, solid, duotone, sharp-line, sharp-solid, sharp-duotone, imprint, pixel, slab, mellow, jass, 3d, draw, lineal, duo, flat.
3. **Search each concept** with `search_icons` (`query` = the concept, `style` = the chosen style, a small `limit` such as 6). Take the best match for each concept from the returned names.
4. **Report the set** as a short table: concept → icon name. Mention any concept with no good match and suggest the closest alternative instead of inventing one.
5. **Deliver files when asked.** Call `get_icon` for each icon the user wants, with the same `style`, plus `size` and `color` if the user gave them. The widget shows the SVG and its download link.

## Rules

- Use only icon names that `search_icons` returned. Never make up an icon name.
- Keep one style across the set unless the user asks to mix styles.
- If a result says a style is not included in the connected account, say so plainly and offer the same set in `line`, `solid` or `duotone`. Do not mention prices.
- HubToolify has no third-party brand logos. If the user asks for a brand's logo, say it is not available rather than presenting a generic icon as that logo.
