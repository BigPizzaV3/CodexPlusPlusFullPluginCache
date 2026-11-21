---
name: edit-a-website
description: Change an existing Mondovo website — text, prices, images, layout, styling, new pages — and undo changes. Use when the user wants to update, fix, redesign part of, or add to a site they already have.
---

# Edit a website

Reuse the `site_id` already in the conversation or returned records. Only if it
is missing, find the site with `list_sites`, using a `query` for its name.
Then pick the lightest tool that does the job:

| The user wants | Use |
|---|---|
| Different words, prices, FAQ answers, links or image addresses | `patch_variation_content` — instant, no redesign |
| A layout, style or section change ("make the hero darker", "add testimonials") | `refine_site` with the request in plain words |
| A new page (About, Services, Contact…) | `add_page`, or `add_pages` for several |
| To go back to how it was | `list_versions`, then `restore_version` |

- On a design draft, adding pages, a collection or appointments first builds
  the chosen design into its working site. Pass its `variation_id`; on
  `choose_design`, show the designs and ask the user which to build from.
  Relay `build_transition.tell_user` and use its returned working `site_id`
  for every later call, including publish. Repeated additions reuse that site.
- If an edit returns `use_build_site`, retry on its `build_site_id`. Read that
  site's designs when a variation ID is needed rather than assuming that a
  source-design ID identifies the intended variation there.
- `refine_site`, generated `add_page` calls and `add_pages` return a `job_id`.
  An `add_page` call with authored `code` saves immediately without a job.
  For generated changes, the chat shows a
  progress card that updates itself; poll `get_job` about every 10 seconds when
  you need the result. A finished job can still list items in `failed` — tell the
  user about each one.
- To show a reference image for a change, upload it with `upload_asset` and pass
  the returned address in `image_urls`.
- If a site is busy with another change you get `site_busy` with that job's id —
  wait for it, then try again.
- Every change is saved in the site's version history and can be undone. If a
  response carries `history_warning`, tell the user the change saved but was not
  recorded before making more edits.
- Changes are not live until the site is published again. Offer to publish after
  a round of edits (see the `build-a-website` skill, step 6).
