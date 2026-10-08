# Canva interface playbook

> **Observe, never assume.** Canva's layout changes by release, account tier and window
> size. Everything below describes *landmarks to look for*, not positions to click. Take a
> screenshot and find the thing. If what you see doesn't match this file, trust the screen.

## Generating artwork that leaves room for text

This is the highest-leverage step and it happens before Canva opens.

**Never let the model render text.** Prompt for composition with deliberate empty space:

| Destination | Ratio | Where to leave space |
|---|---|---|
| Instagram feed | `4:5` | Top third clear, subject in lower two-thirds |
| Story / Reel | `9:16` | Top quarter and bottom sixth clear |
| Landscape banner | `16:9` | One side clear — left or right, pick and say which |

Prompt pattern:

`{subject}, {setting}, clean unbroken negative space across the {top third}, subject
positioned in the {lower two thirds}, even lighting in the empty area so text will read,
commercial photography, no text, no letters, no watermarks`

The phrase **"no text, no letters"** matters — models add garbled signage unprompted.

Check the generated image before importing: if the empty area is busy or dark where light
text must sit, regenerate rather than fighting it in Canva.

## Landmarks

| Task | What to look for |
|---|---|
| Upload an asset | Left sidebar, an **Uploads** section with an upload button; drag-drop onto the canvas also works |
| Add text | Left sidebar **Text** section; heading / subheading / body presets |
| Change size | A **Resize** control in the top toolbar (paid feature — may be absent) |
| Export | **Share** in the top right, then a download option |
| Page management | Page thumbnails below or beside the canvas |
| Brand assets | A **Brand** section in the sidebar, when the account has a Brand Kit |

## Placing the artwork

1. Upload through the Uploads panel; wait until the thumbnail appears before continuing.
2. Click or drag it onto the page. It lands as a new element.
3. Size it to cover the page if it's a background — but **do not** drop it into an existing
   template frame; that replaces the user's content.
4. If it must sit behind text, send it backward rather than moving the text.

## Adding editable text

1. Add a text element from the Text section.
2. Click into it and type the real copy — never paste a screenshot of text.
3. Set size and weight so the headline reads at thumbnail scale.
4. Position it in the empty area the artwork was generated to provide.
5. Repeat separately for the CTA and any logo — **each its own element**, so a later edit
   can touch one without disturbing the others.

## Resizing for a second destination

Prefer duplicating the design and resizing the copy, so the original stays intact. After
any resize, **screenshot and check**: text commonly overflows, clips, or lands on the
subject's face when the ratio changes. Fix the position; don't shrink the type to nothing.

## Exporting

1. Open Share, choose the download option, pick the format (PNG for stills).
2. **Wait for the download to actually complete.** A started export is not a finished one.
3. Confirm by observation before reporting success.

## Verification checklist

After the design is built, screenshot once and confirm:

- [ ] Headline text is correct, spelled right, fully visible
- [ ] CTA present and readable
- [ ] Logo placed, not stretched
- [ ] Nothing important sits under the text
- [ ] No leftover placeholder elements
- [ ] Nothing pre-existing was deleted or replaced

Report anything you could not confirm rather than assuming it worked.

## Known failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Text is unreadable | Artwork too busy behind it | Regenerate with cleaner negative space |
| Element replaced the user's content | Dropped into a template frame | Undo, place as a new element instead |
| Text clipped after resize | Ratio change moved the safe area | Reposition, don't shrink |
| Garbled letters in the artwork | The model rendered text | Regenerate with "no text, no letters" |
| Export never arrives | Dialog still open or format unselected | Screenshot, complete the dialog |
