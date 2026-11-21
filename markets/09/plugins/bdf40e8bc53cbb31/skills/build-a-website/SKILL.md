---
name: build-a-website
description: Create a new website with Mondovo from a description of a business — gather a strong brief, generate three designs, help the user choose one, and publish it. Use when the user wants a new site, landing page or online presence.
---

# Build a website

There are two ways to make the design: Mondovo generates three designs from a
brief, or you design it yourself and Mondovo checks, hosts and publishes it.
`get_intake_questions` says which ones this connection offers.

## 1. Resolve an existing site only when needed
For an explicitly new website, go straight to gathering the brief. Do not list
sites as an automatic duplicate check. If the user asks to reuse or continue an
existing site, reuse its known `site_id`; only when it is missing, call
`list_sites` with a `query` for the named site.

## 2. Gather the brief
Call `get_intake_questions`. Pre-fill every answer you can infer from the
conversation, then ask only the real gaps, a few at a time, and show your
assumptions so the user can correct them. The quality of the site depends on the
brief, so get: business name, what they sell, location, who the customers are,
what makes them different, the tone of voice, and the one action the site should
drive (the `goal`, for example "book a consultation").

Leave colours and mood open unless the user has a clear taste — then the three
designs come back genuinely different. If they want a site like one they have
seen, pass its address as `design.source_url`.

For a ready-made business (a directory, for instance), call `list_packs` and use
a `pack_slug` instead of a brief.

## 3. Create
If `get_intake_questions` returned a `design_method` choice, ask the user which
they prefer.

**You design it.** Write the complete site from the brief (the `files` and
`content` shapes are in the tool description), check it with `validate_design`
and fix every issue it lists, then call `create_site_from_design`. Put the
business's supplied facts in `content` exactly. Do not invent its name or
contact details. When the owner supplied no proof or prices, plausible sample
content is allowed for their review; keep every planned section.

**Mondovo generates it** (or there was no choice): call `create_site`. It returns a `site_id` and starts building three designs.
This takes 3 to 15 minutes; the progress card in the chat updates itself. Tell
the user it is underway and roughly how long it takes. Poll `get_site` about
every 10 seconds when you need to know it has finished; only `ready` means all
three designs are done.

## 4. Choose a design
Call `list_variations` with the `site_id`. The designs appear as a picker with
screenshots. Let the user choose — never choose for them. If screenshots are
still rendering, call it again in about a minute.

## 5. Build on the chosen design
Adding pages (`add_page`, `add_pages`), a collection or appointments to a design
draft first copies the chosen design into its working site. Pass the user's
chosen `variation_id`. If a call returns `choose_design`, show the designs and
ask which to use, then retry with that ID.

Relay `build_transition.tell_user` and use the returned working `site_id` for
every later tool call, including publication. Another addition to the same
design reuses its working site. To build a different design as a separate site,
use the original design site's ID and that other design's `variation_id`.

If an edit returns `use_build_site`, continue on its `build_site_id`. Resolve
variation IDs on the working site when needed rather than assuming that a
source-design ID identifies the intended variation there.

## 6. Publish
Only when the user asks. Suggest a subdomain from the business name (lowercase,
hyphens) and confirm it. Call `publish_site` with the chosen design's
`variation_id` when publishing from the design draft. Publishing creates or
reuses that design's working site and returns its `site_id` — use it from then
on. If you already received a working site ID, publish that site directly.
Poll `get_site` on the returned ID about every 15 seconds until `published`, then share the live link. Never call `publish_site`
again to check on a publish that is already running.

If the response is `contact_info_needs_confirmation`, show the user the contact
details on the site and ask whether they are right before continuing.

If `chosen_design_lacks_edits` is returned, explain which design holds the
owner's work and ask how they want to proceed. Do not silently change their
selection. The response explains the editor path for deliberately publishing
an untouched alternative.
