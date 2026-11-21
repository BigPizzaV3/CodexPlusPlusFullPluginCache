---
name: onboarding
description: Get started with Frexy. Choose how previews work, then open your websites or build your first one. Use when the person has just installed Frexy, or asks how to start with it.
---

# Set up Frexy

Frexy hosts the websites you build for this person: you write the site, Frexy
stores it, deploys an unlisted preview, and publishes it to a live address when
they ask.

1. Call `list_projects` with `{}`.
   - If it fails with `unauthorized`, tell them Frexy needs to be connected and
     stop; do not guess at their sites.
2. Call `read_settings` with `{}`. Briefly say what the two settings do, in
   plain words, and ask whether to keep them:
   - **Preview after changes** — you deploy a preview when you finish a set of
     changes to a site.
   - **Show previews in the chat** — once a preview is ready, you open it beside
     the conversation.
   If they want either off, call `update_settings` with only what they changed,
   for example `{"set":{"showPreviewInChat":false}}`. Confirm from the values the
   tool returns; never say a setting was saved if the call failed.
3. If they already have sites, call `open_frexy` with `{}` so they can see them,
   and ask which one they want to work on.
4. If they have none and they named a website or sent a picture to look
   like, give it to `capture_reference` and build from it: there are no designs
   to choose then. Ask only for the business details you still need (name,
   what it sells or does and where, how customers reach it). Otherwise call
   `show_designs` with kind `site` and `known`: whatever they already told you.
   Draw the one form its `next` describes: whole websites with a picture and
   preview link, the rest of their details, their theme colours as swatches or
   their own from colour pickers, and an upload for their logo with "Skip for
   now". Under the form, give its `choose` link to see every website larger
   on Frexy; if they say they chose there, call `create_project` with `choice`
   alone. Build from what they gave or chose
   (`create_project` with `choice`, or with `starter` and `colours`, then the
   logo) as its `next` says,
   `deploy_preview`, poll `get_deployment` until it is ready, and call
   `open_site_preview` with the project's id so they see it in the chat.

Never call `deploy_production` during setup. Publishing is only ever done when
the person asks for it.

If they installed Frexy in the middle of another task, finish that task in the
same conversation instead of starting this setup over it.
