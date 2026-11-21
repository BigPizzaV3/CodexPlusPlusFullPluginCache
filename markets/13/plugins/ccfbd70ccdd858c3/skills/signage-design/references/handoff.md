# Hand-off to optisigns-operate

signage-design designs; optisigns-operate publishes. After the user approves the design and the
preflight, write this block exactly, then follow the optisigns-operate publish recipe.

```
## Ready to publish
- Content: <file or URL>, <pdf|pptx|png set|web page>, 16:9
- Asset name: <Name — YYYY-MM-DD>   Folder: </Signage/...> (optional)
- Duration: <s per page/slide>      Screens: <names>
- When: <now | daily 11:00–14:00 weekdays | from <date>>   Replace or add to what's playing: <ask>
```

## Fill it in

- **Content:** the exported file you can reach from code, or the public https URL of a web page.
  If the user still has to download and attach the file, say so here and wait for it.
- **Format:** `pdf` (default for slides), `pptx` (only if they'll re-edit), `png set`, or `web page`.
  Orientation: `16:9`, or `9:16` if portrait-native.
- **Asset name:** what the user will look for, plus the date. Use their wording.
- **Folder:** only if the user named one or their library clearly uses folders.
- **Duration:** seconds per page or slide from your slide list (default 10), and the total for a
  multi-page PDF (OptiSigns sets one duration per item and divides it evenly across the pages: 4 pages
  × 10 s = 40 s). A web page plays as one item; give its duration if it shares a playlist.
- **Screens:** the names the user gave; check them with `optisigns_screen_search` when signed in.
  Unknown screens: write "ask".
- **When:** now, a daypart, a date range. optisigns-operate turns this into a schedule; assign itself
  is now-only.
- **Replace or add:** leave "ask" unless the user already said. optisigns-operate asks on a screen
  that is already playing a playlist.

## How it maps to the tools (optisigns-operate runs these)

| Content | Tools |
|---|---|
| PDF / PPTX / PNG | The upload route in [host-tools.md](host-tools.md) → Export → upload |
| Web page | `optisigns_asset_create` with `url` and `name` |
| Built-in app | `optisigns_app_manifest` → `optisigns_asset_create` with `appType` + `appData` |
| Several items or durations | `optisigns_playlist_create` → `optisigns_playlist_item_add` |
| Days, hours, future start | `optisigns_schedule_create` → `optisigns_schedule_item_add` |
| Put it on screens | `optisigns_screen_assign_content` |

Live writes need approval. If the tool shows an approval card, the user approves there. If it returns a
confirm text, show it, get a yes, then re-call with `confirmed: true`. Never confirm on the user's behalf.

## Not signed in

If the OptiSigns tools aren't connected, the block still helps: give the user the file or URL and say
how to add it in the OptiSigns portal (upload the file, or add a Website app with the URL), then assign
it to their screens.

## Example

```
## Ready to publish
- Content: Easter services — 2026-04-05.pdf, pdf, 16:9
- Asset name: Easter services — 2026-04-05   Folder: /Signage/Church
- Duration: 10 s per page (1 page = 10 s)   Screens: Lobby TV, Fellowship Hall
- When: from 2026-03-22 until 2026-04-05     Replace or add to what's playing: ask
```
