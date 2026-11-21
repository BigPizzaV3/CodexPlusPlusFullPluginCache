---
name: product-video
description: Make a short marketing video for a software product with Wevi. Plan a storyboard from the product's own pages, build one project from published motion templates, capture the product's real interface into the scenes that need it, render with music and an AI voiceover, review the result and share the MP4. Use when the user asks for a product video, launch video, feature explainer, product demo clip, social promo or call-to-action outro for their product or website.
---

# Make a product video with Wevi

Wevi builds short marketing videos (3 to 6 scenes, 15 to 45 seconds) from published motion templates. Each scene is one template whose text, colors, logo and image slots are filled for the product; scenes that show real product UI are captured from a live page. Wevi renders every scene in the cloud and joins them into one MP4 with background music and an AI voiceover.

## Before building, ask what is missing

- The product's website or domain: the logo, colors and fonts are read from it. With no website, ask for a public logo image URL.
- The goal of the video (launch, feature explainer, social promo, call to action), the audience and the tone.
- Length or number of scenes, the key messages, whether there should be a voiceover, and brand colors if the user has them.
- Export quality, asked once before the first render and only when the account has paid access (`paidAccess` in `wevi_get_credits`): 1080p is the default; offer 4K only when the user wants it or the video is for a large screen. Free accounts export at 720p with a watermark, so do not ask there.

## Steps

1. Open the product page with `wevi_open_page`. The outline lists `productUi` (the interface on screen), `appEntry` and `authWall`. A product video should show the product's real interface, which is usually behind a login: when `appEntry.looksLikeMarketing` is true and candidates exist, offer to capture inside the app, send the user `loginUrl`, and call `wevi_wait_for_login` with the `sessionId`. Use public marketing pages only when there is no app to reach, the user declines, or the scene is about the website itself.
2. Plan with `wevi_generate_storyboard`, passing the `sessionId`, so the plan uses templates built for the interface actually on that page. Show the plan, adjust it with the user, then pass `createPayload` to `wevi_create_project`: all scenes in one project, with `brand: { websiteUrl }` (or `logoUrl`). Never one project per scene.
3. For each scene in `scenesNeedingCapture`, reach the view that shows that scene's message (`wevi_go_to`, `wevi_click`, `wevi_scroll`), then call `wevi_capture_scene` with the `sessionId`. Check the numbered screenshot it returns; if the pick looks wrong, re-pick with `wevi_select_capture` (free). The `capture-product-ui` skill has the full procedure.
4. Fix every issue listed in `planReview` with `wevi_update_scene`, then `wevi_trigger_render` with the chosen quality and poll `wevi_get_render_status` until `phase` is `completed`.
5. Read `review` on the render status: it lists what a look at the rendered scenes found (a tiny or blurry logo, cut-off or overlapping text, placeholder copy, a broken layout) with a suggested fix per scene. Repair with `wevi_update_scene` and render again; only changed scenes re-render. Share `videoUrl` when `review.status` is `done` and it lists no issues; if an issue cannot be fixed, tell the user what it is.
6. Call `wevi_close_page` when the site is done.

## Revising

`wevi_update_scene` changes one scene's copy, parameters or narration. `wevi_add_scene`, `wevi_remove_scene`, `wevi_reorder_scenes` and `wevi_swap_template` revise the project without rebuilding it. Each scene's `templateCopy` lists text layers still showing the template's own words; set those when the copy matters. `wevi_list_music` and `wevi_list_voices` give the choices for `musicTrackId` and `voiceId` on `wevi_trigger_render` (paid access only); otherwise Wevi picks a track for the brand's tone and the default narrator. `wevi_get_scene_previews` shows single rendered scenes.

## Rules

- One planned story, never a list of features. Open with what the product is and who it is for, or with the viewer's problem and the product by scene 2. Close with a call to action that names the product. Never open cold on a feature claim.
- A different template for every scene; only plain text title templates may return. All scenes in a video share one aspect ratio.
- Narration per scene fits `voiceoverBudget` (about 2.4 words per second, complete sentences). On-screen titles are 6 words or fewer; one idea per scene; narration says what the visual shows.
- Leave the animation IN and OUT parameters unset unless the user asks for a specific move: cuts between scenes are matched automatically.
- Never ask the user for a password and never type one. Sign-in happens in the user's own browser session through `loginUrl` and `wevi_wait_for_login`.
- Check `wevi_get_credits` before large batches. When an action needs more credits than the account has, say how many it needs and how many are available; credits are managed in the user's Wevi account.
- Outside Wevi's reach: free-form or generative footage (people, characters, animals, scenery), editing the user's own video files, changing a template's animation or layout, mixing aspect ratios, vertical video, cloning a voice. Say so plainly and offer what Wevi can do instead.
