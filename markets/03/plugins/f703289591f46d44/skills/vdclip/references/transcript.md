# Reading a clip's timed text

`get_transcript` answers "what is said, and when" for a clip that already has captions or
on-screen text.

```
get_transcript({ result_id, cursor? })
```

## What it returns

| Field | Meaning |
| --- | --- |
| `segments[]` | `{ text, startSeconds, endSeconds }`, in project order |
| `next_cursor` | Cursor for the next page; `null` on the last one |

Times are **seconds from the start of the project**, rounded to one decimal. Pagination is
by character budget, not by a fixed segment count — pass `next_cursor` back as `cursor` to
continue.

## What it is not

- It does **not** transcribe. It reads caption and text overlays that are already in the
  project. A project with no captions returns a plain "no captions or on-screen text"
  answer, not an empty list you should misread as a bug.
- It does **not** cut anything. Chat-driven editing is paused (see
  [editing.md](editing.md)), so the timestamps are for the user to act on — quote them and
  point at the editor.

To get captions in the first place, create the project with `type: "captions"`, or with
`type: "clipping"` and a caption preset — see [create-clips.md](create-clips.md).

## Good uses

- "What does this clip actually say?" — read it back, grouped, with times.
- "Where does it talk about pricing?" — find the segment and give the timestamp range.
- "Is the hook in the first 3 seconds?" — check the first segments against the clip's
  `score` from `list_clips`.

## Response style

Quote the text, not the raw array. Give a time range like `12.4s–15.1s` when the user asks
where something happens. Page through with `next_cursor` only when the user wants more —
do not dump a long transcript unasked.
