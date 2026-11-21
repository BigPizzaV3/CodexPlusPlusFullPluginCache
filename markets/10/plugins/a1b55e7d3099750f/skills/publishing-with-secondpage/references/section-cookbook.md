# File bundle cookbook

SecondPage publishing accepts static file bundles, not renderer sections.

## Minimum page

```json
{
  "title": "Project Brief",
  "files": [
    {
      "path": "index.html",
      "content_type": "text/html; charset=utf-8",
      "content_base64": "PCFkb2N0eXBlIGh0bWw+PGh0bWw+Li4uPC9odG1sPg=="
    }
  ]
}
```

## Multi-file app

Use normal relative asset references from `index.html`:

```html
<link rel="stylesheet" href="styles.css">
<script src="app.js" defer></script>
<img src="assets/chart.png" alt="Revenue chart">
```

Then submit all referenced files:

```json
{
  "title": "Interactive Dashboard",
  "entrypoint": "index.html",
  "files": [
    { "path": "index.html", "content_type": "text/html; charset=utf-8", "content_base64": "..." },
    { "path": "styles.css", "content_type": "text/css; charset=utf-8", "content_base64": "..." },
    { "path": "app.js", "content_type": "text/javascript; charset=utf-8", "content_base64": "..." },
    { "path": "assets/chart.png", "content_type": "image/png", "content_base64": "..." }
  ]
}
```

## Semantic edit targets

For fresh generated pages, stamp important editable regions with stable names.
Use readable `id`, useful `aria-label`, and `data-review-target-id` attributes
on sections, hero blocks, headings, CTAs, repeated cards, charts, tables, forms,
nav items, and deck frames. These markers help Turner understand comments like
"make this card more premium" or "rewrite this CTA" without guessing from a
generic `<div>`.

```html
<section id="hero" data-review-target-id="hero" aria-label="Hero section">
  <h1 id="hero-heading" data-review-target-id="hero-heading">Launch plan</h1>
  <a id="hero-primary-cta" data-review-target-id="hero-primary-cta" href="#contact">
    Book a walkthrough
  </a>
</section>
```

## Deck bundle

For new decks, prefer `prepare_deck`; it creates this supported structure
without changing slide HTML:

```html
<!doctype html>
<html data-sp-document-type="deck">
  <body>
    <main data-secondpage-deck data-sp-canvas-width="1280" data-sp-canvas-height="720">
    <section id="sp-slide-slide-1" data-sp-frame data-sp-slide-id="slide-1">
      <h1>Opening idea</h1>
    </section>
    <section id="sp-slide-slide-2" data-sp-frame data-sp-slide-id="slide-2">
      <h1>Second idea</h1>
    </section>
    </main>
  </body>
</html>
```

Every slide root needs a stable `data-sp-slide-id`. Publish with
`presentation: { "intent": "deck" }`. A successful publish is not readiness
evidence; only `presentation.status: "ready"` verifies presentation controls for
that version.

## Updating safely

1. Read the current complete bundle. If `file_bundle` is null, export it and
   retain the exported version ID and manifest; verify referenced file bytes
   before editing.
2. For a default-route bundle, submit every file with the matching
   `base_version_id`.
3. For custom entrypoints or routes, follow [Publishing and revisions](publishing-shape.md)
   and preserve the manifest in both signed-upload calls. If the client cannot
   PUT files, hand off that upload.
4. On `version_conflict`, re-read/export and reconcile before retrying.

Do not send only the changed file. Updates are full bundle replacements.

## Practical guidance

- Use `index.html` as the entrypoint unless there is a strong reason not to.
- Keep asset paths stable between versions when possible.
- Put generated CSS and JS in separate files for easier future updates.
- Inline only tiny assets. Use `create_media_upload` for larger images or
  original video files, and keep normal CSS/JS/fonts/data as separate bundle
  files when they fit the payload limits.
- When using direct media uploads, reference the returned `asset_url` in HTML
  and pass the completed IDs as `media_asset_ids` on `create_page` or
  `update_page` when you want explicit claiming.
- If the user gave you an existing HTML export, publish the export as-is rather
  than translating it into a SecondPage-specific structure.
