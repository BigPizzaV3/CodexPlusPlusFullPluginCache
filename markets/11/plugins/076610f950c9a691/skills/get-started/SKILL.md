---
name: get-started
description: Welcome a new Artboard user after they install the plugin and show them what they can do first.
---

# Get started with Artboard

1. Call `get_profile` to confirm the connected Artboard account, and greet the user by name.
2. Explain in two sentences what Artboard does:
   - It finds mockups, 3D models and animation templates and opens them in a full editor
     inside ChatGPT.
   - You can place their images, adjust the design and export images or videos for them,
     or they can edit by hand.
3. Offer three starting points and wait for the user to choose:
   - "Put my logo on a t-shirt and make an ad". Ask them to attach the logo, then follow
     the product-ad skill.
   - "Show me 3D device models". Call `open_artboard` with `view: "3d"`.
   - "Open my projects". Call `list_projects`.

Do not promote plans, upgrades or purchases. If the user asks about unavailable
features, explain the actual account restriction and offer normal account
navigation. If they ask to buy a plan or credits, explain that purchases are not
supported in this plugin and no purchase has occurred. Do not give pricing,
upgrade or checkout steps, even for an explicit purchase request; follow the
account-access boundaries in `artboard-mockups`.

## One plugin, natural requests
Explain that this one plugin includes the real mockup, 3D and motion editors and their tools. Offer examples in plain language: "Put my logo on this shirt", "Make the phone rotate once over three seconds", "Move the second image first", and "Export this as a PNG". Never tell the user to type internal tool names or underscores. The host may initially select Work from Try in chat; ordinary Chat is supported, so do not require a Work handoff to edit or export.


Native edits now return real rendered visual feedback. Inspect it before claiming
success; `inspect_project` captures a read-only frame without an export allowance.
Use a new `begin_project_edit` group for a multi-tool user request, and pass its
`history_group` so one undo restores that request. All three editors support
recorded native undo/redo across reopening. Exports have a persistent Download control for the original rendered file. Existing artwork placement remains a real editor
operation; native AI generation is for explicitly requested creative assets only.
