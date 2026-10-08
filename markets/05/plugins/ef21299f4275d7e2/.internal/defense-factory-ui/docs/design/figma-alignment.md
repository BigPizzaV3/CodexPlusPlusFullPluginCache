# Codex Security Cloud visual direction

## Design thesis

Codex Security Cloud should read as a compact Codex workbench: quiet surfaces, clear
finding titles, and restrained security-status color. Use shared `@oai/ds`
controls and semantic tokens, with plugin-owned styling and layouts for findings and
reports. Match the Figma hierarchy without suggesting data or actions the
plugin cannot provide.

## Reference frames

[First hill designs](https://www.figma.com/design/AmdtyAkWNu0rKaKbbSz0iV/-2026.08--Defense-Factory---First-hill?node-id=1111-222044):
overview 1231:91788, findings 1231:92738, report 1437:136460.

## Visual system

- Colors: shared light/dark surfaces and text tokens; severity/status colors
  convey meaning. No decorative gradients or invented accent palette.
  Critical uses danger/red, High warning/orange, and Medium caution/yellow
  across badges and severity charts. The combined Medium or lower summary stays
  neutral; it is not a single severity. Keep text labels alongside color.
- Typography: bundled OpenAI Sans; 14px regular navigation, search, and controls;
  12px semibold table headers; 13px semibold badges; 14px finding titles;
  12px secondary metadata and footer captions; 16px report title; and tabular
  dashboard numbers. Pagination controls, which are not in the reference frame,
  use the same 14px control scale.
- Layout: 24px desktop / 16px mobile insets for navigation, controls, and table
  content. Collection table header backgrounds and row dividers reach the page
  edges, without an outer gutter. Tables within detail panels stay within those
  panels. Report and metadata columns stack on narrow screens.
- Depth: light borders and modest corner radii; existing control shadows only.
  Dropdowns use the shared opaque elevated surface so page content stays hidden.
- Motion: reuse shared control behavior; no additional animation.

The plugin owns its palette and compact typography in `src/theme.css`, layered
over `@oai/ds/styles`; it does not import Codex application styles or require
whole-window attributes. The existing bridge supplies light/dark theme updates.
Compact utility text remains 12px for `text-sm` and 11px for `text-xs`;
feature-specific classes apply the larger Figma control and content sizes.
The build bundles OpenAI Sans from the existing shared font assets directly.

## Reuse and custom work

- Shared plugin controls (`workbench/controls.tsx`) apply the same 34px height,
  8px corners, and 14px text to toolbar buttons and single-line inputs. All
  collection searches use a plugin-owned search wrapper, including its search
  icon, accessible label, and clear action. Keep search first in each toolbar.
  Reuse these wrappers instead of selecting separate component defaults per page.
- Findings, Repositories, and Scans share 8px toolbar gaps, 16px section gaps,
  flat collection tables with 60px desktop rows, 12px headers/footer captions,
  and 14px primary row text. Mobile rows grow to fit their content. Settings
  fields and popover controls use the same type scale without changing their
  form semantics or replacing searchable pickers with separate inputs.
- Shared library imports: buttons, badges, inputs, tooltips, icons, and the DS
  styling foundations. Local wrappers preserve the current appearance without
  importing internal Codex source files.
- Plugin-owned presentation: compact palette and typography, toolbar styling,
  search/clear layout, and pill navigation composed from real route links.
  Keep focus handling, menu behavior, and virtualization in their existing libraries.
- Existing platform controls remain where appropriate: popovers, menus,
  checkboxes, avatars, and date input.
- New Scan uses one searchable repository picker, not a search field stacked
  above a second selector. Remote loading must not interrupt typing.
- Overview follows frame 1231:91788: a four-cell summary strip, compact pipeline,
  Needs attention table, then paired chart cards. Unlike the collection pages,
  its cards remain inset and bordered. The table previews eight open findings,
  server-sorted by severity and discovery date, and links to the full scoped list.
  Summary counts use configured (or selected) repositories, current open and fixed
  findings, and repositories with continuous scanning enabled. No fixes-verified
  count is invented. Open findings uses count-and-badge groups for Critical,
  High, and Medium or lower (medium, low, informational), with Unknown separate
  when present. These are actual severities, not the design's P0/P1/P2+ priorities.
  The summary columns accommodate the full severity labels on one line without
  reducing the type scale. On mobile, Open findings occupies a full-width row
  with counts above their badges instead of wrapping groups inside a half-cell.
  Current severity bars and daily discoveries use existing
  aggregates; the discovery chart retains date/severity controls and exact daily
  values for screen readers.
- Charts use small plugin-owned HTML/CSS renderers with shared theme colors.
  The host chart screen depends on the web widget runtime, so it is not imported.
- The Overview pipeline follows the compact flow-band treatment in node
  1402:116471, with native finding statuses and current totals across the selected
  repositories. Band thickness reflects status counts, not transition history.
  Smooth curves connect the counts at each column center; equal counts stay flat
  and zero counts narrow to zero, without adding decorative volume.
  The seven totals come from bounded `findings_list` count requests. The header's
  period picker reuses the UI kit calendar with All time, 7/30-day presets, and a
  custom UTC date range. It filters discovery dates while grouping by current
  status; it does not reconstruct historical transitions. Its URL-backed period
  is independent of activity dates and all-time summary counts. Drill-through
  links preserve the date/repository scope, including pagination and export.
- Findings places an experimental severity-to-status Sankey above the table.
  Its proportional bands summarize only the visible page, with an explicit
  page/total caption and an exact-count table for screen readers. It follows the table's
  filters and pagination without fetching every finding or inventing aggregates.
  Both diagrams are isolated feature components that can be removed independently.
- Plugin-owned: page composition, table columns, filters, report/metadata
  layout, overview summaries, routing, and MCP data binding.
- The standalone bundle has no dependency on Codex application internals.
  The plugin bridge still owns host interactions. Any future extraction of
  shared host controls should be a separate package change, not a raw-source
  build export.

## Data and interaction boundaries

Show actual severity, finding status, repository, revision, timestamps, and
available detail assignment. Do not substitute finding status for an external
issue's status. Priority, due dates, issue-tracker status,
and a global Configure workflow are omitted because the API does not support
them. The Sankey and pipeline are explicitly native-finding adaptations of
Figma nodes 1402:113878 and 1402:116471, not linked-issue charts.
The project/priority bar chart is represented by explicitly labeled
severity counts. The trend plots discoveries only: `new_currently_fixed` is a
current-status total for a discovery cohort, not a daily fix series. Do not
invent a Fixed trend line or issue-pipeline counts from those fields. Existing
per-repository monitoring settings remain available.

Preserve keyboard row activation, visible focus, labels, URL-backed filters,
pagination, authorized mutations, and read-only repository results. Status
meaning must not depend on color alone.
