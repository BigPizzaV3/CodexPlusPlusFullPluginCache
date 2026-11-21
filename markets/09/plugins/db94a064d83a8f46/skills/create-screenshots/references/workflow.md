# Server series workflow

Shared `design` and each `slides[].design` accept the fields from `list_screenshot_options`. Per-slide fields override shared ones. There is no local config file or setup step.

Example using two attached files (pass the host-authorized file objects in `files`):

```json
{
  "name": "Launch series",
  "design": {"resolutionId": "google-play-portrait", "deviceFrame": "iphone", "backgroundColor": "#EAF3FF"},
  "files": ["HOST FILE OBJECT 1", "HOST FILE OBJECT 2"],
  "slides": [
    {"sourceIndexes": [0], "design": {"title": "Your first headline"}},
    {"sourceIndexes": [1], "design": {"title": "Your second headline"}}
  ]
}
```

Replace example file placeholders with objects containing `file_id`, `download_url`, optional `mime_type` and `file_name` supplied by ChatGPT's authorized file interface. Never invent identifiers or upload URLs. Each sourceIndexes array selects one to three zero-based files in placement order. The tool also accepts `sources` data URLs as an alternative to `files`, subject to the same budget. Use only one source method.

Omitted sourceIndexes use the matching file by slide position (or the last file when there are more slides than files). Sources omitted entirely use the bundled habit tracker demo. The renderer does not obtain screenshots from other chats itself.

`create_screenshot_series` returns seriesId and projectIds. `export_screenshot_series` returns renderer `skia-wasm`, files with measured dimensions and persistent per-PNG `url`, persistent downloadUrl and render duration, plus a separate image block per slide when within the inline response budget. inlineImageMode states whether those blocks are originals, smaller previews, or links-only. The per-PNG URLs and ZIP always contain the full-resolution originals. The MCP Apps component displays those images side by side; the model can inspect or revise individual slides. ZIP members are sequential `01.png`, `02.png`, etc.

For a requested design revision, call `update_screenshot_series` with the series ID and the zero-based slide indexes/design fields to change, then export the same series again. Source images are preserved.
