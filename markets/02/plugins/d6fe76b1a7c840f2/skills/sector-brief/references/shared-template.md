# Template reference (inlined, self-contained)

This file documents the page-chrome contract (document head, cover, table of contents, section
block, sources-section wrapper, footer, outlook-badge, design tokens) for this skill's HTML
report. The canonical chrome **CSS is already inlined** in this skill's `assets/template.html`
(between the `/* BEGIN shared-template-css */` / `/* END shared-template-css */` markers) — you
do **not** copy any CSS at emit time. This file documents the **authoring rules** and the
**literal HTML markup** for the chrome. Citations rules live in `references/shared-citations.md`.

## Lookup-order rule (non-negotiable)

Before authoring any CSS, HTML scaffold, class name, or design token for visual chrome, check
this reference first. Do not invent CSS or HTML scaffolds for chrome elements this contract
already provides (cover, TOC, section, sources-section wrapper, footer, outlook-badge), and do
not silently restyle them.

## Output contract

1. The canonical chrome CSS is already present in `assets/template.html`. Do not duplicate it,
   and do not re-define chrome rules elsewhere.
2. Use the literal markup snippets below for the document head, cover (one of `cover-simple` /
   `cover-multi`), TOC, section block, sources-section wrapper, and footer. Class names and
   attribute order are invariant.
3. This skill picks **exactly one** cover variant. Variants do not mix within a single report.
4. Per-skill CSS overrides live **above** the marker region in `assets/template.html` — never
   inside it.

## Design tokens (defined in the inlined `:root`)

- `--navy`, `--accent` — primary palette.
- `--gray-100..700` and short aliases `--g100..g700` (both families resolve).
- `--text` — body text color.
- `--positive`, `--negative`, `--neutral` — semantic colors used by `.outlook-badge` and tables.

## Cover variants

| variant | used by | shape |
|---|---|---|
| `cover-simple` | issuer-brief, sector-brief | 1-column navy cover, top "logo + title" / bottom `.cover-meta`. |
| `cover-multi` | earnings-brief, peer-analysis | 2-region grid: `.cover-top` (navy `.cover-left` + optional `.cover-strip` image + `.cover-bar-top`); `.cover-bottom` optional landscape band. |

`cover-multi`: add `has-cover-image` to `.cover-top` / `.cover-bottom` **only** when an `<img>`
is populated. `.cover-companies` lists per-skill chips (peer-analysis marks the target with
`class="company-chip target"`; earnings-brief lists the issuer first). `.cover-companies-label`
text is per-skill (e.g. `PEERS`, `COMPANIES`).

`cover-simple`: one `.cover-meta` row at the bottom; populate as many
`<span><strong>Label:</strong> value</span>` pairs as needed.

## Outlook badge

Pastel background + colored text. Five variants: `stable`, `positive`, `negative`, `review`,
`na`. The label text is uppercased by CSS, so inner text may be mixed-case. Do not re-define
`.outlook-badge` rules locally or use solid-fill/inline-color overrides.

## Markup snippets

```html
<!-- document head — {report_title}. The <style> block contains skill-specific overrides
     ABOVE the inlined shared-template-css and shared-citations-css regions. -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{report_title}</title>
  <style>
    /* skill-specific overrides (body font-size, .page max-width, skill-only tables/charts) */
    /* BEGIN shared-template-css ... */  /* … canonical chrome CSS (already inlined) … */  /* END shared-template-css */
    /* BEGIN shared-citations-css ... */ /* … canonical citations CSS (already inlined) … */ /* END shared-citations-css */
  </style>
</head>
<body>
<div class="page">
  <!-- cover, toc, report-body, report-footer -->
</div>
</body>
</html>

<!-- cover (simple) — issuer-brief, sector-brief -->
<div class="cover cover-simple">
  <div>
    <div class="cover-logo">Moody's<div class="cover-agentic">AGENTIC SOLUTIONS</div></div>
    <div class="cover-title">{Cover Title — use <strong> for the entity / topic name}</div>
  </div>
  <div class="cover-meta">
    <span><strong>Date:</strong> {YYYY-MM-DD}</span>
    <span><strong>Type:</strong> {report type label}</span>
  </div>
</div>

<!-- cover (multi) — earnings-brief, peer-analysis -->
<div class="cover cover-multi">
  <div class="cover-top">
    <div class="cover-left">
      <div>
        <div class="cover-logo">Moody's<div class="cover-agentic">AGENTIC SOLUTIONS</div></div>
        <div class="cover-title">{Cover Title — use <strong> for the entity / topic name}</div>
        <div class="cover-companies-label">{COMPANIES LABEL e.g. PEERS / COMPANIES}</div>
        <div class="cover-companies">
          <span class="company-chip">{Entity 1}</span>
          <span class="company-chip">{Entity 2}</span>
          <!-- peer-analysis flags the target with class="company-chip target" -->
        </div>
      </div>
      <div class="cover-meta">
        <span><strong>Date:</strong> {YYYY-MM-DD}</span>
        <span><strong>Type:</strong> {report type label}</span>
      </div>
    </div>
    <div class="cover-strip"><!-- optional <img src="..."> --></div>
    <div class="cover-bar-top"></div>
  </div>
  <div class="cover-bottom">
    <div class="cover-landscape"><!-- optional <img src="..."> --></div>
    <div class="cover-bar-bottom"></div>
  </div>
</div>

<!-- table of contents — one <li> per section; {prefix} = ecs/pa/pib/sa. Trailing row is Citations. -->
<div class="toc-page">
  <div class="toc-heading">Contents</div>
  <ul class="toc-list">
    <li><span class="toc-num">01</span><a href="#{prefix}-section-a"><span class="toc-label">{Section A label}</span></a><span class="toc-dots"></span></li>
    <li><span class="toc-num">{NN}</span><a href="#{prefix}-sources-anchor"><span class="toc-label">Citations</span></a><span class="toc-dots"></span></li>
  </ul>
</div>

<!-- section block — {prefix}, {slug}, heading. Inner content is skill-specific.
     The #{prefix}-cite-{slot} div is opt-in (per-section citation recap). -->
<div class="section" id="{prefix}-section-{slug}">
  <div class="section-heading">{Section Heading}</div>
  <div class="section-content">
    <!-- skill-specific content -->
    <div id="{prefix}-cite-{slot}"></div>
  </div>
</div>

<!-- sources-section wrapper — rows inside #{prefix}-sources use the markup in references/shared-citations.md -->
<div class="sources-section" id="{prefix}-sources-anchor">
  <div class="sources-heading">Citations</div>
  <div id="{prefix}-sources"></div>
</div>

<!-- report footer — {YYYY-MM-DD} -->
<div class="report-footer">
  <span class="footer-logo">Moody's <span style="font-weight:400;color:#8fa8d0;">AGENTIC SOLUTIONS</span></span>
  <span>Report generated {YYYY-MM-DD} • Confidential</span>
</div>

<!-- outlook badge — variant ∈ {stable, positive, negative, review, na} -->
<span class="outlook-badge {variant}">{label}</span>
```

## Per-skill overrides (kept above the marker region in assets/template.html)

| skill | allowed local overrides | cover |
|---|---|---|
| earnings-brief | none | cover-multi |
| peer-analysis | `.page { max-width: 1050px }` | cover-multi |
| issuer-brief | `body { font-size: 12.5px }`, `.page { max-width: 920px }` | cover-simple |
| sector-brief | none | cover-simple |

Skill-specific table/chart classes (`.yoy-table`, `.pa-table`, `.fin-table`, `.data-table`,
chart helpers, `.credit-badge`, etc.) stay local to each skill's `assets/template.html`.

## Quick checklist

- [ ] No duplicated copy of the chrome CSS anywhere outside the inlined marker region.
- [ ] Exactly one cover variant, matching this skill's declared variant.
- [ ] `cover-multi`'s `.cover-top` / `.cover-bottom` only carries `has-cover-image` when an `<img>` is populated.
- [ ] All `.outlook-badge` instances use canonical pastel variants — no solid-fill / inline-color overrides.
- [ ] The TOC's last row points to `#{prefix}-sources-anchor` with label `Citations`.
- [ ] Footer uses `.report-footer` + `.footer-logo` markup verbatim.
