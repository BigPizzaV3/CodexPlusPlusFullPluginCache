---
name: gradient-backgrounds
description: Use when the person wants a background, gradient, hero image, OG image, launch or social graphic, or slide background for their project. Designs variations with Gradients Studio, lets the person pick and approve one, then saves the files into the repo and, when asked, sets the image as that section's background.
---

# Gradient backgrounds with Gradients Studio

## Loop

1. **Propose.** Call `design_background` with the person's brief in their own words. If the brief doesn't say what it's for, ask once: hero, OG image, launch set, slide, or a size.
2. **Show.** If a widget appears, the person picks, tweaks and approves there, and it exports by itself when they press Approve. Otherwise show the contact sheet image and ask for a number (1–6).
3. **Refine.** For requests like "warmer" or "more grain", call `design_background` again with `from` set to the chosen variation's `settings` and the request as `brief`. You may also edit `settings` yourself (for example exact brand colours as #RRGGBB).
4. **Approve.** Without a widget, do not export until the person approves by saying so. Confirm the sizes before exporting. With a widget, the Approve button is the approval.
5. **Export.** Without a widget, call `export_background` with the approved `settings` exactly as returned (do not retype values), the `sizes`, and `proposed` if present. If it asks to connect an account, tell the person and wait.
6. **Save.** For each file with `status: "ready"`, run `curl -fsSL -o <path> "<url>"` from the project root. Adjust the static folder if needed:
   - Next.js, Vite and Astro: keep `public/`.
   - Otherwise find the folder the project serves static files from; if unclear, ask.
   Create directories as needed. Report each saved path. URLs expire in 24 hours.
7. **Wire, only when the brief named the place** ("hero background", "behind the features section"):
   - Find that section's component.
   - Set the image as its background using the project's existing styling convention (Tailwind `bg-[url(/hero.jpg)] bg-cover bg-center`, a CSS module, or an inline style, whichever the file already uses).
   - Change nothing else: no copy, layout, colours or meta tags.
   - Show the diff.
   If the brief didn't name a place, save the files and ask where they go.

## Never

- Commit, push or deploy.
- Edit meta tags (`og:image` and the like) unless asked.
- Export before approval, or export more sizes than were approved.
