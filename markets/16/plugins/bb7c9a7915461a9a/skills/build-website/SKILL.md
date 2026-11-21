---
name: build-website
description: Build a new website for the person's business with Frexy, from a design they choose, a website they name or a picture they send, with their details, colours and logo, then show them a private preview. Use when they ask for a new website, or for Frexy to make one. To change a site they already have, use edit-website.
---

# Build a new website

1. **Where it goes.** If they have more than one workspace (`list_workspaces`), ask
   which one the site belongs in.
2. **Start from something they chose.** A website they name, or a picture of one,
   is a reference: give it to `capture_reference` and build from it, text as text.
   Otherwise call `show_designs` with kind `site`, `known` (whatever they already
   told you), `recommended` (the design you would pick for their business) and two
   or three colour pairs that suit it as `palettes`. Draw the one form its `next`
   describes: the websites with a picture and preview link, their details, colours
   and a logo upload with "Skip for now". Offer only Frexy's websites, never one of
   your own, and never choose for them.
3. **Their own site, somewhere else.** If they say it is theirs and want it on
   Frexy, `import_site` brings it in.
4. **Create it** with `create_project` (`choice`, or `starter` and `colours`), or
   `start_site` on a site that is still empty, as the result's `next` says. Add their
   logo with `add_image` (`use: "logo"`); if they skipped it, draw one as SVG and add
   it the same way.
5. **Fill in what is theirs.** Replace every sample word in square brackets with
   their own details, asked from them; never invent a name, figure, address or
   review. Bring pictures in with `search_images` and `import_image`, or theirs with
   `add_image`.
6. **Preview.** `deploy_preview`, then `get_deployment` until it is ready. Fix what
   `checks` lists, give them the link, and call `open_site_preview`.

Never call `deploy_production` unless they ask to publish. Frexy does not build
online shops through ChatGPT: offer a site with a contact or quote form instead.
