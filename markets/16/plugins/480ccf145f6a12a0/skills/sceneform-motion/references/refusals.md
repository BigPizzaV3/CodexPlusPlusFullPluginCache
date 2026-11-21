# When a motion call is refused

## Inputs that refuse, each once per session until read here

- `import_motion_asset` always takes `id` (the asset id your layers will
  name) and `kind` (`image`, `video`, `audio` or `font`), with `google_font`
  as much as with `asset_ref` or `url`.
- Each kind has its own tool (`generate_music`, `generate_speech`,
  `generate_sound_effect`, ...), and each takes `requests`, a list. A
  model's settings go under `settings` in the request: a track's length is
  `settings.duration`, not a top-level field. `query_generation_options`
  takes `action` (`recommend`, `search` for a model by name or keyword,
  `list`, `get`, `voices`) and the kind `music`, not `audio`.
- `preview_motion_project` takes a `width` of 320 or more.
- A blank timeline has no scenes: `addScene` comes before any root
  `addLayer`, or the engine answers "adopt it as a scene first".
- `addLayer` without `beforeId` lands at the back of its siblings, behind a
  full-frame background; the first sibling is in front, so pass `beforeId`
  or reorder after.
- Every effect carries an `id`; a drop shadow's size field is `blur`.
- Layer ids are unique within their scope (the root timeline, or one
  scene's composition), group children included; a child joins a group by
  `parentId` on its `addLayer`.
- The `actions` document is about 75 KB of JSON: save it to a file, or
  strip it in your sandbox, and query the action you need rather than
  reading it inline.

## Mistakes no call refuses, found only in a preview

- A rect, ellipse or text is drawn from its top-left corner: `position` is
  that corner unless `anchor` is set to half the size, so a centred shape
  takes `anchor: [w/2, h/2]` and an anchor track where its size animates.
- Children of a group draw in array order like siblings anywhere: the
  first is in front, so a card's background rect comes last among its
  children or it covers them.
- `ink` comes from one text layer read with `layer` and `at_ms`; a `scope`
  read of a scene returns none, so measuring several texts is one inspect
  each, or one preview frame.
- Film grain is strong: start a "fine grain" near 0.15, not 0.7.

## Refusals and what they mean

- "Wait for the current render of this video to finish": a draft render or
  an export holds the video. Check `get_motion_review` and try again once
  it is done.
- "The page already shows this version": the draft is rendered; nothing to
  do until the next edit.
- "This version is already rendered at full quality": there is nothing to
  export until an edit changes the draft.
- "This version has not been rendered yet": the export waits until the
  user has seen this draft version. Call `render_motion_draft`, show the
  result, and export when they approve it. A draft render that failed
  also opens the export, since the export is then the way to see it.
- "This edit session was replaced by a newer one": read
  `get_motion_review` and carry on with the new session.
- "There are not enough credits to run this call": the account cannot pay
  for another minute of engine time. Tell the user and stop editing.
- Other calls holding the session's engine time: wait for them to finish
  and retry.
- "Motion videos are offline right now": tell the user and try again later.
- "The price of this ... changed": prepare the call again for a fresh quote.
- "The engine could not complete this call": the engine failed, not your
  script. Inspect the project and try again; a refused script or import
  says what was wrong in the engine's own words instead.
- An edit lands only if the project keeps the video's canvas and a length
  between one second and ten minutes; a refused edit says what to set back.

If project creation times out, retry `create_motion_project` with the same
`request_id` and inputs. Recover a timed-out confirmation by calling
`confirm_actions` again with the same `action_ref`.

`render_motion_draft` answering `rendering` is not a refusal: the render
outlived the call's `timeout_seconds` and lands on its own. Read
`get_motion_review` until `rendered_version` is the draft version; its
`rendered_video_url` is the file. Do not edit and render again for a link.

A large `edit_motion_project` batch can outlive your host's own call
timeout and still land. After a timeout, call `get_motion_review`: if
`draft_version` moved, the edit applied, so inspect and carry on rather
than sending it again. To follow a render or an export, call
`get_motion_video` with `timeout_seconds` instead of polling in a loop,
which trips the rate limit.
