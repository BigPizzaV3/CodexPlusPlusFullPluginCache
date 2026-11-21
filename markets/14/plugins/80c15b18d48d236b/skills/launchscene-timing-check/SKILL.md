---
name: launchscene-timing-check
description: Check the on-screen text of a Remotion or HyperFrames launch video against Launchscene's measured corpus before rendering: display time, reading speed, size, margins and contrast, then render stills at the frames that matter. Use when the user asks whether text is readable, whether a hold is long enough, to review a launch video's timing, or before a full render. Requires the Launchscene MCP server.
---

# Launchscene timing check

Find holds that are too short and text that is too small before anyone watches the render. This skill reads the composition, asks Launchscene how the text compares with real launch videos, renders the frames worth looking at, and proposes scoped fixes. It never edits the composition on its own.

## 1. Inventory the text

Read the composition source. For each text element, record:

- the text, as rendered (longest variant if the copy is a variable);
- the global frame where it becomes visible and the frame where it disappears (add each `<Sequence from>` offset; local frame 30 in a sequence starting at 120 is global frame 150);
- the frame where its entrance ends, if it animates in (end of `interpolate` input range or when a `spring` settles);
- its box in canvas fractions `[x, y, width, height]` and its font size in pixels;
- foreground and background colors when they are solid.

Get `fps`, `width` and `height` from the `<Composition>`. If a value depends on runtime layout (text wrapping, auto-sizing), render a still to measure it rather than guessing.

## 2. Ask Launchscene

Call `readability_check` with up to 40 items:

- `in_ms`: the frame where the text is readable (entrance end, or arrival for static text), converted with `ms = frame * 1000 / fps`;
- `out_ms`: the last visible frame plus one, converted the same way;
- `box`, `line_height_pct` (font size / canvas height * 100), `foreground`, `background`, `large_text` when known.

The result places each item against per-video distributions of real launch videos and returns questions. These are context, not rules: a deliberate fast flash can stay fast.

## 3. Render the frames that matter

For each flagged item, render the landing frame and the last frame:

```bash
npx remotion still <CompositionId> out/check-<frame>.png --frame=<frame>
```

For HyperFrames, use `npx hyperframes snapshot` at the same times. Look at every still: is the text fully on screen, legible at phone size, not covered by a cursor or another layer?

## 4. Report, then wait

Write one correction per problem with four fields:

```plaintext
Location: composition, element, global frames a to b.
Observed: what the check or the still shows (cite the returned question and quartile).
Change: one scoped edit (extend the hold to frame n, shorten the copy, enlarge to n px).
Keep fixed: what must not move (press frame, reveal frame, audio cues, layout).
```

Order them: missing or unreadable text first, then timing, then visual detail. Do not apply the edits until the user approves them. After an approved edit, render the affected frames and the neighbouring scene boundary again.
