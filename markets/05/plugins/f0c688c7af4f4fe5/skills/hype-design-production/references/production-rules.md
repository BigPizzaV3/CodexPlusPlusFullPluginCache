# Hype production rules

## Fixed visual system

- Use `assets/canvas.html` for record and featured posters.
- Use `assets/promotion-certificate.html` for promotion certificates.
- Treat those exact HTML files and bundled logos as executable production assets, not visual references.
- Never call image generation, image editing, or Canva. Never create a substitute PNG/JPG/WebP or invent a new visual.
- Never permanently modify the bundled templates for one output.
- Keep the fixed page size, boxes, colors, spacing, logo frame, and text-fitting JavaScript.
- Brand colors are navy `#0A2146`, orange `#CC7F30`, and pure white `#FFFFFF`.
- Use the bundled logo assets only. CTFS, STC, and Hype share the template's fixed logo frame.
- Logo backgrounds must visually merge into the pure-white page. Do not introduce pink, beige, gray, transparent, or black page regions.

## Request parsing

For normal records, extract:

- `brand`: `ctfs`, `stc`, or empty only when the request truly has no brand.
- `title`: the record phrase without its terminal period phrase. Example: `Most Profit`.
- `subtitle`: normally `In a Day`, `In a Week`, or the period phrase explicitly provided.
- `value`: preserve symbols and units exactly, such as `$300`, `4 Days`, or `35`.
- `name`: optional only when the record is explicitly for a team rather than a person.
- `date`: preserve the requested date wording and ordinal suffixes.

Brand selection is explicit: CTFS uses `ctfs.png`, STC/Save the Children uses `stc.jpg`, and Hype Events uses `hype.png`. Do not guess a missing brand.

If the source is an email, use this same PDF workflow after the email project has extracted the fields. Do not create Canva, TXT, workflow notes, or a reduced text document.

## Featured Hype awards

- `New Kids on the Block This Week` and `Best Leader of the Week` always use the Hype logo.
- They have no separate numeric value. Put the person's name in the main value area and hide the lower duplicate name area.
- Keep the date in the normal date area.
- Use `featured` mode, not `record` mode.

## Promotion certificates

- Use landscape Letter format and the central safe area because the user prints on pre-printed bordered paper.
- Keep the lower-left area empty and the signature area at lower right.
- Company name and logo are Hype Events.
- Default role is `Corporate Trainer`; use another role, including `Assistant Manager`, only when explicitly requested.
- Do not add extra congratulatory paragraphs.

## Output and naming

- Every deliverable is a single-page PDF.
- A run is successful only when the bundled generator returns a path ending in `.pdf`; any image result is a failed workflow.
- Normal record: `Title-Name-Value-Date.pdf`; omit only fields that are intentionally absent.
- Featured: `Title-Name-Date.pdf`.
- Promotion: `Promotion Certificate-Name-Date.pdf`.
- Save final PDFs to `result`. Keep no temporary HTML after success.
- Never output TXT files.

## Completion behavior

- If the request contains enough information, execute immediately without asking whether to continue.
- Complete template generation, Chrome export, one-page verification, saving, and cleanup before replying.
- If blocked, state the failed step and keep the temporary HTML for recovery.
