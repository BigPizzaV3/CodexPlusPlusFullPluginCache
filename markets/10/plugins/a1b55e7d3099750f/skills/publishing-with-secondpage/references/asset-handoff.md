# Asset handoff: media and rich content in a Page bundle

**Architectural invariant**: agents own asset generation and bundle assembly;
SecondPage stores and serves the exact files they submit. SecondPage does not
generate images, scrape the web, render section objects, or inject a chart or
map runtime. Choose the right asset path, include accessible HTML, and validate
the completed bundle before publishing.

## Include ordinary assets in the bundle

For CSS, JavaScript, fonts, small images, charts, maps, and data files, use
normal relative paths and submit every referenced file with the Page. A static
map can be an image; an interactive map, chart, or table is HTML and JavaScript
that you author and ship with the bundle. Do not assume SecondPage has a
provider key, an installed UI library, or a renderer for a section type.

```html
<figure id="neighborhood-map" data-review-target-id="neighborhood-map">
  <img src="assets/tokyo-map.webp" alt="Six Tokyo neighborhoods on a map">
  <figcaption>Six neighborhoods we toured</figcaption>
</figure>
```

Use semantic structure and a text alternative for rich visuals. An interactive
control must work with a keyboard and preserve a useful non-JavaScript reading
path where practical.

## Direct media uploads

For larger images or original video files, do not put the bytes into the Page
bundle as base64. Use `create_media_upload`, upload the file bytes to the
returned `upload_url` with HTTP `PUT` and the returned `required_headers`, then
call `complete_media_upload`. Reference the returned `asset_url` in the Page:

```html
<img src="/_sp/media/asset-id/photo.webp" alt="Product detail">
<video src="/_sp/media/asset-id/demo.mp4" controls></video>
```

Uploaded media is Page-scoped. It inherits the Page's visibility after the Page
is published or updated with that `asset_url`. For deterministic claiming, pass
the completed asset IDs as `media_asset_ids` on an `html` or inline-file
`create_page` or `update_page` call; the server also detects approved
`/_sp/media/...` URLs in submitted HTML.

## Page upload continuations

For a multi-file Page when HTTP is available, use the same Page tools with an
upload continuation. For one self-contained document use `html`; use inline
files only when HTTP is unavailable:

1. Call `create_page` or `update_page` with `upload_files`, including every
   file's relative `path`, `content_type`, `byte_size`, and lowercase SHA-256.
2. Upload only files whose response status is `upload_required` using HTTP
   `PUT` to `upload_url` and the returned `required_headers`.
3. Call the same tool again with `upload_session_id`, retaining the original
   metadata and, for updates, the required `base_version_id`. A manifest is
   optional for the default `index.html` route; include one for multiple routes
   or a custom entrypoint. Include `asset_paths` when known.
4. Use the returned deployment status, or `read_page`, to confirm the Page.

Page deployment assets are content-addressed and deduplicated within the
organization by SHA-256. Re-deploys should upload only changed files. Scalable
Pages are static-only in v1.

## What SecondPage never does

- Call Mapbox, Tavily, Firecrawl, OpenAI Image Generation, Replicate, or other
  external APIs on your behalf
- Generate images or scrape web pages
- Transform, repair, or add functionality to the HTML, CSS, JavaScript, or
  media the agent supplies
- Host arbitrary unclaimed files. SecondPage stores Page-scoped image/video
  uploads claimed by a Page and deployment assets claimed by a verified Page
  deployment; everything else remains in your tool environment or at an
  external URL.

These concerns remain in **your tool environment**. SecondPage's job is to
publish the complete, validated Page bundle you produce.
