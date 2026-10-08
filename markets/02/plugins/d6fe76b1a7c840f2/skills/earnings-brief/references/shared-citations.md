# Citations reference (inlined, self-contained)

This file is the single source of truth for how citations are authored and rendered in this
skill's HTML report. The canonical citations **CSS is already inlined** in this skill's
`assets/template.html` (between the `/* BEGIN shared-citations-css */` / `/* END shared-citations-css */`
markers) — you do **not** need to copy any CSS at emit time. This file documents the **authoring
rules** and the **literal HTML markup** you reproduce when emitting `[n]` references, the
end-of-document Citations block, and optional per-section recaps.

## Output contract (global rules)

1. Every report contains exactly one Citations block at the end of the document.
2. Numbering is a single global sequence `[1], [2], …` per document. The number `n` in any
   inline reference MUST equal the row position of the matching source inside `#{prefix}-sources`
   (1-indexed, in document order).
3. Internal MCP tool names are NEVER rendered in any citation row.
4. Plain `[n]` text in narrative content (not wrapped in `<a class="cite-ref">` or
   `<span class="cite-ref">`) is **not allowed**.
5. Citations are not embedded inside numeric/data cells of financial, valuation, ratings, risk,
   ESG, or YoY tables. This skill may extend the carve-out list in its own `SKILL.md`.

## 1. Inline reference markup

- **With URL** (default): use the anchor form and substitute `{source_url}` and `[n]`.
- **Without URL**: use the span form (fallback only when the source has no URL).
- `n` MUST match the row position of that source inside `#{prefix}-sources`. The same `n` may be
  reused multiple times for repeat references to the same source.

```html
<!-- with URL -->
<a href="{source_url}" target="_blank" class="cite-ref">[n]</a>
<!-- without URL -->
<span class="cite-ref">[n]</span>
```

## 2. End-of-document Citations block

Every report renders exactly one Citations block. `{prefix}` is this skill's prefix
(`ecs`, `pa`, `pib`, `sa`). The displayed heading is always the literal string `Citations`.
The container keeps its `#{prefix}-sources` id.

```html
<div class="sources-section">
  <div class="sources-heading">Citations</div>
  <div id="{prefix}-sources">
    <!-- one .source-item row per source, in [1], [2], … order -->
  </div>
</div>
```

Three row variants — pick based on which fields are present:

| variant | when to use |
|---|---|
| with URL | source has a URL **and** at least one of `source` / `date`. |
| no URL | no URL but at least one of `source` / `date`. |
| no meta | source has a URL but no `source` and no `date`. |

```html
<!-- with URL -->
<div class="source-item">
  <span class="source-num">[1]</span>
  <a href="{url}" target="_blank" class="source-title">{Title}</a>
  <span class="source-meta">({source} • {date})</span>
</div>
<!-- no URL — swap <a> for <span> so .source-title styling still applies -->
<div class="source-item">
  <span class="source-num">[1]</span>
  <span class="source-title">{Title}</span>
  <span class="source-meta">({source} • {date})</span>
</div>
<!-- no meta — omit the .source-meta span entirely -->
<div class="source-item">
  <span class="source-num">[1]</span>
  <a href="{url}" target="_blank" class="source-title">{Title}</a>
</div>
```

If only one of `source` or `date` is present, render only that field inside the `()`.

## 3. Optional per-section recap (opt-in)

Some skills render a short recap of the citations referenced inside a given section, immediately
below that section's content. This is **opt-in** (the CSS ships unconditionally). Skills that opt
in embed an empty target placeholder inside each section (`<div id="{prefix}-cite-{slot}"></div>`)
and later fill it with a recap or leave it empty if the section has no citations.

```html
<div class="section-citations">
  <span class="cite-label">Citations</span>
  <span class="cite-item"><span class="cite-num">[1]</span><a href="{url}" target="_blank">{Title}</a><span class="cite-meta"> ({source} • {date})</span></span>
  <span class="cite-item"><span class="cite-num">[2]</span><a href="{url}" target="_blank">{Title}</a><span class="cite-meta"> ({source} • {date})</span></span>
</div>
```

Numbers inside a recap MUST be the same `n` values used inline and in the end-of-document block —
a recap NEVER starts a new numbering sequence. Omit the recap entirely if the section has no
citations.

## 4. Source data shape

| field | required | notes |
|---|---|---|
| `id` | yes | 1-indexed integer matching the row's position in `#{prefix}-sources`. |
| `title` | yes | Human-readable title. Rendered inside `.source-title`. |
| `source` | no | Publisher / system (e.g. "Moody's Research Assistant Library"). |
| `date` | no | Display-formatted date (e.g. `2026-02-24` or `12 Sep 2026`). |
| `url` | no | Absolute URL. If absent, use the URL-less row variant above. |

Never render internal MCP tool names (e.g. `getCreditOpinion`) in `.source-meta`.

## CSS variable contract

The inlined citations CSS relies on `--accent`, `--navy`, `--g100`, `--g200`, `--g400`, `--g700`
being defined in this skill's `assets/template.html` `:root` (they are — defined in the inlined
chrome CSS).

## Quick checklist

- [ ] Every inline `[n]` is wrapped in `<a class="cite-ref">` (with `href` + `target="_blank"`)
      or, if no URL exists, `<span class="cite-ref">`.
- [ ] All `n` values resolve to a row inside `#{prefix}-sources` at position `n`.
- [ ] The Citations block heading reads exactly `Citations`.
- [ ] Each `.source-item` row uses `.source-num` + `.source-title` + optional `.source-meta`.
- [ ] No `.source-meta` renders an internal MCP tool name.
- [ ] No citation markup inside numeric/data cells excluded by this skill.
- [ ] Optional `.section-citations` recap, if used, reuses the same `n` values.
