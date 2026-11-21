---
name: product-ad-video
description: "Make a short product ad with Vidova, the AI video editor. Use when someone asks for a product ad, a UGC-style ad, a launch or drop video, or a promo with a price or offer, from product footage or photos, for Reels, TikTok, Shorts or a store page. Vidova cuts, captions, animates, adds music and renders the video in the cloud."
license: MIT
---

# Product ad

One product, one promise, one action, in the time it takes to scroll past.

## Steps

1. Check that the Vidova tools are available, for example with `get_active_project`. If they are not, ask the person to connect the Vidova plugin and sign in.
2. Make a project with `create_project`. If the person attached files in this chat, bring them in with `import_attached_files`. A file over 512 MB cannot be attached: call `create_upload_link` and give the person its link, where they add the file from their device. Use `import_asset_url` for a link to a file. Call `wait_for_asset` with every Asset ID until the files are ready. For a whole new edit from these files, call `start_routine` with routine `edit_prep` and the person's brief word for word before you read the footage. Call `wait_for_jobs` until it is done, follow its handoff, then go to the step that calls `check_edit`.
3. Read each file with `read_asset`: the best angle, the moment of use, where the product sits in the frame. Use `remove_background` on a logo that sits on a box.
4. Call `search_templates`. When a template fits, use `read_template` and `apply_template`, then adjust it with `patch_film`. When none fits, build the film with `patch_film`.
5. Cut on the downbeats of the music. Find a track with `search_stock` kind music, add it with `import_stock`, and read its beats with `detect_beats`.
6. Watch the result with `preview_timeline`, and with `preview_range` across the moments that move. Call `check_edit`, then `wait_for_jobs` with its Job ID, and fix what it names.
7. Call `render_video`, wait for it with `wait_for_jobs`, then give the person the project `url` and the link to the finished video.

## What makes it work

- The person's brief comes first: their order, song, length, format and rules. This skill fills in the rest.
- Show the product in use, or its best detail, in the first second. No logo first and no black frame.
- A 15 second ad has four parts: the hook to 1 s, the reason to 9 s (the problem and the fix, or three details, one idea per shot), the peak to 12 s with the offer said once, and the product still moving with the brand and the action to the end. Scale this to 6 or 30 seconds.
- Use 8 to 10 shots in 15 seconds, with lengths that follow the beat.
- Use only the person's facts. Never invent a feature, a price, a claim or a review. Add no medical or performance claim unless they wrote it.
- Keep the product's true colours, and keep it the sharpest thing in the frame. Text never sits on the product or on a face.
- Use 9:16 for Reels, TikTok and Stories unless they say otherwise, 1:1 or 4:5 for a feed, and 16:9 for YouTube or a website. For an app or a website, `search_stock` has device frames.
