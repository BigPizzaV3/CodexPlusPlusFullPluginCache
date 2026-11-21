# Design — the Applet Design System

Every frame already contains the **Applet Design System v1**, inserted by the host — never link it (law 4). Build
with its classes and variables; write CSS only for what is specific to the applet. Reference copy:
`/applets/api/v1/stylesheet/v1.css`.

- **Your CSS always wins**: the base is in cascade layers, so `.fxr-btn { border-radius: 4px }` or
  `:root { --fxr-accent: #f7a600 }` apply with no `!important`.
- **Dark and light are automatic**: the SDK sets the variables and `<html data-theme>` from the trader's theme. Use
  variables, never a colour literal; one theme only: `[data-theme="light"] .x { … }`.

| Variable | Use it for |
| --- | --- |
| `--fxr-bg` | The page background |
| `--fxr-fg` | Body text |
| `--fxr-muted` | Captions, hints, secondary values |
| `--fxr-accent` | The one highlight |
| `--fxr-border` | Control borders |
| `--fxr-font` | The body font stack |
| `--fxr-surface` | Cards, panels |
| `--fxr-surface-raised` | Controls on a card |
| `--fxr-surface-hover` | Hover fill |
| `--fxr-fg-secondary` | Labels |
| `--fxr-fg-disabled` | Disabled text |
| `--fxr-on-accent` | Text on accent |
| `--fxr-accent-hover` | Accent hover |
| `--fxr-accent-pressed` | Accent pressed |
| `--fxr-border-subtle` | Dividers |
| `--fxr-border-strong` | Emphasised borders |
| `--fxr-focus` | Focus ring |
| `--fxr-success` | Success |
| `--fxr-danger` | Error, destructive |
| `--fxr-warning` | Caution |
| `--fxr-info` | Information |
| `--fxr-up` | Gain, buy |
| `--fxr-down` | Loss, sell |
| `--fxr-font-mono` | Code |

Spacing `--fxr-space-{4,6,8,12,16,20,32}`, radii `--fxr-radius-{row,btn,control,md,modal,pill}`, type
`--fxr-font-size-{11,12,13,14}`.

## Classes

- **Layout** — `fxr-app` on `<body>` · `fxr-stack` (column) · `fxr-row` (`--between`, `--nowrap`) · `fxr-spacer` ·
  `fxr-grid` (tiles ≥ 140 px) · `fxr-split` (two columns from 560 px) · `fxr-only-narrow`, `fxr-only-wide`.
- **Type** — `fxr-title` · `fxr-heading` · `fxr-label` · `fxr-caption` · `fxr-value` (the headline number) · `fxr-num`
  (tabular) · `fxr-mono` · `fxr-muted` · `fxr-up` / `fxr-down`; headings, links and `<hr>` are styled.
- **Card** — `fxr-card` (`--raised`) with `fxr-card__header` / `fxr-card__title` · `fxr-divider`.
- **Button** — `fxr-btn` + `--primary` · `--ghost` · `--text` · `--danger`; `--sm` · `--lg` · `--block` · `--icon`.
  One `--primary` per view.
- **Form** — `fxr-field` > `fxr-field__label` + `.fxr-input` (on `input`, `select`, `textarea`; `--sm`) +
  `fxr-field__hint`; `fxr-field--error` turns the hint and border red · `fxr-input-group` + `fxr-input-group__addon`
  (units: *lots*, *%*).
- **Choice** — `<label class="fxr-check">` around an `input.fxr-checkbox`, `.fxr-radio` or `.fxr-switch` ·
  `fxr-segmented` (`--block`): radio inputs, each `<label><input type="radio" name="…"><span>…</span></label>`, or
  `<button aria-pressed>` · `fxr-tabs` > `button.fxr-tab[aria-selected="true"]`.
- **Status** — `fxr-chip` (`--accent` · `--success` · `--danger` · `--warning` · `--up` · `--down`) · `fxr-badge` ·
  `fxr-notice` (`--success` · `--warning` · `--danger`; info by default) with `fxr-notice__title` + `fxr-notice__body`.
- **Data** — `fxr-table-wrap` > `table.fxr-table` (`th.fxr-num` / `td.fxr-num` right-align) · `ul.fxr-list` (label left,
  value right) · `fxr-stat` > `fxr-stat__label` + `fxr-stat__value` + `fxr-stat__delta`.
- **Feedback** — `progress.fxr-progress` · `fxr-empty` · `fxr-skeleton` · `fxr-spinner`.
- **Native** — `details.fxr-disclosure` · `dialog.fxr-dialog` · `data-fxr-tooltip="…"` · `kbd.fxr-kbd` ·
  `fxr-sr-only` · `fxr-truncate` · `fxr-w-full` · `fxr-text-right` · `fxr-gap-{4,12,16}`.

## Rules

- **Width**: the pane is 300–460 px, the page wider. `fxr-app` on `<body>`; `fxr-split` and `fxr-grid` collapse to
  one column in the pane. No horizontal scroll.
- **Type**: 13 px body; web fonts cannot load (the sandbox blocks downloads).
- **Colour**: accent is the one highlight; `--fxr-up` / `--fxr-down` for gain and loss, never as the only signal.
- **States**: every `null` and every failed call gets a sentence in `fxr-empty` or `fxr-caption`
  (*"Open this applet inside a chart to see the symbol"*), never a blank.
- **Images**: inline `<svg>` (`fill="currentColor"`) or `data:` URIs.
