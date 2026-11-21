---
name: boords
description: Work in the user's Boords account on video pre-production: scripts, shot lists, storyboards, frames and client feedback. Use when the user names Boords, asks to write or edit a script, break a script into shots, build or change a storyboard, or make sense of written comments on frames. Also use for requests about a Boords project, storyboard or frame referred to only by id or name, and when a Boords request asks for something the tools cannot do, such as generating or restyling images, so the reply explains that boundary. Do not use for video editing or for general writing that will not go into Boords.
---

# Boords

Boords is the Boords team's workspace for scripts, storyboards and feedback. The Boords tools read and write the user's real account, and the Boords panel beside the conversation is where the user looks at work and approves changes.

## Find the work first

1. Call `list_teams`, then `list_projects` for the team the user means. Most users have one team; ask only when there is more than one and the request does not say which.
2. Call `open_boords_panel` once, with `view: picker` when the document is not known yet, or with the storyboard or script id when it is. The panel refreshes itself afterwards, so do not reopen it after every tool call.
3. Read before you change anything: `get_script` for text and `list_frames` for a storyboard. Keep the returned `revision` values; writes need them.
4. When the user has selected frames or a passage in the panel, that selection is the context for the request. Edit only what was selected unless the user says otherwise.

## Scripts

- Draft scripts in plain prose with one scene or beat per paragraph. For AV scripts keep the audio and visual columns side by side.
- To change an existing script, call `propose_script_edits` with exact anchored replacements or inserts, then `open_boords_panel` with `view: proposal` and the returned proposal id. The user approves in the panel; nothing is saved until they do.
- Proposals preview plain text only. If the user wants Markdown or AV table formatting written directly, say so and, once they confirm, use `edit_script` with the latest `expected_revision`. That saves without a panel review.
- Use `create_script_version` before a large rewrite when the user wants a copy to return to.

## Storyboards and frames

- One shot per frame. Map what is heard to the sound field and what is seen to the action or description field.
- To build a storyboard from a script, call `propose_storyboard` with the rows in shot order and `script_id` set, then open the proposal view. The storyboard is created only when the user approves.
- To change frame text, call `propose_frame_edits` with the exact new values per frame, then open the proposal view.
- Selecting frames in the panel shares their text only. To see a frame's image, call `get_frame_image` with its `storyboard_id` and `frame_id` before describing composition, style or continuity.
- Reorder with `update_frame_order` and pass every active frame id, not only the ones that move.

## Images

- Boords tools look at frame images (`get_frame_image`) and attach existing ones (`attach_frame_image` with an HTTPS URL the user gives, or an image from the team's Asset Library). They cannot generate, edit or restyle images.
- When a request asks for a generated image, say so in your first reply and offer to attach an image the user already has. Do this even when another part of the request fails, for example when a project is refused.

## Feedback

Handle frame feedback in one reply, without waiting for the user to ask for each step:

1. Read the comments with `list_comments`, or `list_frames` with `include: ["comments"]`. Bodies may be stored as HTML from the Boords editor; read them as text.
2. Call `get_frame_image` for the frame before describing its composition. It returns the original image, without the comment's drawing.
3. A comment's `annotation` is drawing data, not an image, and you cannot see it. The user can see it in the Boords panel (`open_boords_panel` with `document_type: storyboard`, `document_id`, `view: feedback`, `comment_id`); "Explain this feedback" there sends only the written comment. Work from the comment text. Do not infer arrow direction, placement or other drawing details, and do not wait for the drawing before proposing.
4. Explain what the reviewer is asking for in production terms.
5. If the comment text asks for a concrete change, prepare it in the same reply with `propose_frame_edits` for that frame only, changing only the fields the text supports. Record a visual change (move, framing, timing) in the frame's action or a direction note. Then call `open_boords_panel` with `view: proposal` so the user can approve it. Do not change the frame image, and do not save the edit directly.
6. If a change depends on the drawing, say that you cannot see it and ask the user to describe it in words or upload an image of the marked-up frame to the conversation.
7. Mark a comment complete only when the user asks.

## Approvals, direct saves and destructive calls

- Proposals are the default for script text, frame text and new storyboards. The user approves them in the Boords panel, and nothing is saved until they do; you cannot apply a proposal yourself.
- Use `edit_script`, `update_frame` or `create_storyboard` directly only when the user explicitly asks to save without reviewing. Pass `expected_revision` from the latest read to `edit_script` and `update_frame`.
- Reordering frames, attaching images, comments and library changes have no proposal step. They save as soon as the call runs, so make them only when the user asked for that change, and say what will change. Whether ChatGPT shows its own approval prompt first depends on the user's settings; do not promise one.
- Delete, archive and `revert_proposal` require `confirm: true`. Ask the user and wait for their reply before sending it. A request not to be asked is not confirmation.
- If a proposal comes back stale, the document changed in Boords. Read it again and propose from the latest version rather than retrying.

## Answering

- Give the storyboard or script `edit_url` so the user can open it in Boords.
- Say what was proposed and that it is waiting for approval in the panel. Do not report a change as saved until the apply result confirms it.
- When a tool refuses for permissions, plan limits or a read-only connection, tell the user plainly what they can do instead in Boords. Do not suggest upgrading.
- When a team, project or storyboard returns `forbidden` or `not_found`, say the connected account cannot open it. Do not guess at its contents, and do not suggest that getting access would add capabilities Boords tools do not have.
- Answer every part of a request in the first reply, including the parts Boords tools cannot do.
