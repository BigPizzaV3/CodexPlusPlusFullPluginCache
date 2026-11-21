---
name: add-ember-images-and-files
description: Add, upload, place, or troubleshoot existing images and downloadable files in an Ember site. Use for any image or static-asset work, especially portfolios, galleries, hero photos, source assets, researched stock photography, PDFs, or favicons. Preserves existing and real work, applies automatic optimization correctly, and covers public paths, truthful use, alt text, scrims, and verification.
---

# Add images and files to Ember

## Success criteria

Image work is complete when every intended visual slot renders a relevant,
high-quality image from a valid non-empty source, uses appropriate alt text,
fits its crop and layout across viewports, and remains truthful about what it
depicts. Keep any working existing image until an equal or better replacement
is ready. A finished site has no unfilled image placeholders. If truthful
imagery is unavailable, remove the unused placeholder or ask for the real
asset instead of presenting an empty frame as completed work.

## Choose a suitable source

Use a direct public HTTPS image URL, including a suitable Unsplash or other
stock URL; an existing path already in the site; or an Ember-managed
asset created with `upload_file`. Choose the option that best fits the request.
Use `upload_file` when a managed copy, optimization, stable local path, or
downloadable non-image asset is useful—not as a requirement for every image.

If calling `upload_file`, pass a complete short, descriptive destination
filename rather than only a directory, especially for signed or opaque source
URLs. Use `referenceInPagesAs` when the result supplies it; otherwise derive the
served path from the reported stored path. A small `data:` URI is suitable only
for compact assets such as an SVG icon.

Save visitor-facing assets under a typed `/public` directory, such as
`/public/images/`, `/public/files/`, or the `/public` root for a favicon. The
served path drops `/public`: reference `/public/files/menu.pdf` as
`/files/menu.pdf`.

Images sent through `upload_file` are resized and re-encoded automatically. The
optimizer may change the filename or extension, so reference the path reported
by the tool rather than the requested path. The MCP server cannot read the
user's local disk; a managed upload requires a publicly retrievable HTTPS URL
or a small data URI.

## Choose truthful existing imagery

Use the user's real portfolio, products, menu, team, location, and other
factual work whenever it is available. For generic atmosphere or editorial
support, use relevant existing stock or editorial photography,
but do not label or imply that it depicts the actual business, products,
people, work, or location. If a factual image is unavailable, remove the unused
placeholder or ask for the real asset rather than inventing one.

## Place assets well

- Give every `<img>` meaningful alt text; use an empty alt only for genuinely
  decorative imagery.
- Place asset sizing, cropping, overlays, and other visual rules in
  `components/theme.ts` using the selected design's tokens and classes.
- Put a scrim between text and any photographic hero/background, and verify
  contrast in light and dark themes.
- Add a favicon link and OG metadata in `PageShell` when the request calls for
  them.
- Use short descriptive filenames instead of camera defaults.

After placing assets, run `check_site` for normal site correctness, then inspect
the already-mounted live preview. Confirm that every intended image renders,
fits its crop and responsive layout, maintains contrast, and has appropriate
alt text. Call `render_preview` again for the final checked state or a fresh
shareable link.
