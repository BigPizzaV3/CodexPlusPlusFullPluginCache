# Viral remixes, storybooks, and restyles

Three tools make a finished short video the way the app's tools of the same
name do. Each starts at once (or returns a quote under the same rules as
the generation tools) and returns a receipt with a `short_video_ref`, not an operation.

## Viral remix

`create_viral_remix` remakes a viral short with the user's own subject.

- Pass the source as `video_ref`: an upload, a library video, or
  `import_media` for a direct video-file link. A TikTok, Reels, or Shorts
  page link cannot be imported, so ask for the file.
- Pass `persona_ref` from `list_personas` and `product_ref` from
  `list_brand_kits` for who and what appears.
- The `prompt` says what changes and what stays: "Same hook, pacing, and
  camera moves. Swap the protein shaker for the product, keep the gym
  setting, and make the closing line about the cold brew."
- The length follows the source, up to 120 seconds.
- The default model refuses a photorealistic face, real or AI-generated, in
  the source or the Persona. For a photoreal presenter or Persona, pass a
  model that accepts faces as `option_ref`, such as `seedance_2_5`.

## Storybook explainer

`create_storybook` turns a `topic` into a narrated, illustrated explainer.

- Write the topic as an angle, not a subject: "Why coffee roasters taste
  beans before they buy them, told through one roaster's morning" beats
  "coffee roasting".
- Put the facts that must appear, and any source links, in the topic. Links
  are read as sources.
- `duration_seconds` is a multiple of 10, from 10 to 300. A minute fits one
  clear idea with three or four supporting facts.
- Leave `voice_ref` out for the default narrator.
- `resolution` sets only the generated clips (360p, 720p, or 1080p) and the
  price. The finished video always exports at 1080p.

## Restyle

`restyle_video` redraws a 3 to 60 second clip in a style and keeps its
speech. Pick `style_id` from `list_restyle_styles` first; name the style
the user picked back to them.

## Follow the result

They take several minutes. With `card_offered: true` the host was given a
card that follows the video and plays it once it lands, so say it is on its
way and stop. Otherwise, or when the user asks for it or cannot see the
card, call `get_short_video` with the `short_video_ref` on a later turn;
once `status` is `ready` it returns the `video_asset_ref` (and on MCP a
`video_url`). Starting the same video again to check on it charges twice.

```sh
sceneform remix --video media_abc123 --persona k57persona --max-credits 200
sceneform storybook --topic "How a coffee roaster picks its beans" --duration 60
sceneform restyle-styles
sceneform restyle --video media_abc123 --style claymation
sceneform short k57shortvideo
```
