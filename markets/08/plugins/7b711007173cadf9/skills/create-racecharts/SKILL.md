---
name: create-racecharts
description: "Create, preview and revise animated RaceCharts bar races, line charts and pie charts, including financial comparisons. Use the connected RaceCharts tools with presentation defaults that yield to the user's requested style, reference, chart type and orientation."
---

# Create and revise RaceCharts

Use the connected RaceCharts tools for native chart creation and editing. Check chart_capabilities for current tools, supported formats and the connection's save permissions.

## Choose presentation from the request

User instructions and supplied visual references take priority over every default here. Distinguish chart type, orientation, visual styling, duration and audio as independent choices.

- For an existing chart, preserve its current presentation and media. Apply only requested changes. Do not reapply creation defaults.
- When asked to copy or match a specific chart/example, use that reference. Preserve its design, replacing old topic-specific labels, units, captions and data only as the request requires.
- For every new chart, including a copy or a "similar chart", explicitly set form.guides:false unless the user asks for margin guides. These are editor-only safe-area overlays, not part of the chart's design; do not enable them for portrait or Instagram styling or inherit them from a reference. When editing an existing chart, preserve its guide setting unless the user asks to change it.
- For a new chart without a chosen reference, read [visual defaults](references/visual-defaults.json). These are fallback design settings, never mandatory styling.
- Apply explicit choices first when selecting compatible settings. A square request remains square; landscape/desktop/presentation requests use a suitable wide layout; portrait requests stay portrait. If neither format nor purpose indicates an orientation, use portrait.
- Use the requested supported chart type. Otherwise choose a suitable type from the data: line for change over time, bar race for rankings over time, pie for nonnegative shares. Do not force a line chart onto every request.
- Explicit themes, fonts, palettes, backgrounds, layouts, durations and instructions such as "no captions" override their corresponding defaults. Use supported alternatives from chart_capabilities. If an exact request cannot be represented, explain the limitation rather than silently ignoring it.
- Fill only unspecified, compatible design settings. Avoid a style questionnaire when a useful preview can be produced.

## Apply the bundled defaults

The JSON is style configuration, not a project or dataset. Build a new native document for create_chart_from_document from common.templateId and common.form, then add the selected type's form and the resolved chartType/orientation. For a portrait line chart, also include portraitLine.form. Never apply those portrait positions or dimensions to square/landscape charts, bars or pies. Use normal native layouts for those formats.

Apply explicit compatible user settings last. For a light design, choose a supported light template (for example soft-data-studio), disable an unwanted dark glow, and use colors with appropriate contrast. A user-specified reference or existing design replaces these defaults entirely.

Assign palette entries to the actual row names in data order unless the user specifies colors. Use short accurate display labels when full company names would crowd the plot. Generate the title/subtitle from the requested topic. Fit text and labels by rendering, not by assuming fixed positions always work.

Default to about 60 seconds for a new unspecified animation, using set_chart_duration after the dataset is installed. Duration is total video time, not seconds per observation. Preserve an explicitly chosen duration. Do not copy private audio IDs or music from an unrelated chart; music is a separate user choice.

## Data and financial comparisons

Use supplied data or the requested supported source. Preserve actual values, missing observations, units and period order.

For built-in financial data, read financial_data_capabilities, resolve companies, inspect financial_year_coverage, then call build_financial_dataset with the draftId and current revision. Use the default available provider (RaceCharts Financial Data); never silently substitute a provider. Applying the server's fresh result retains its source notes. For built-in financial data, the chart's source line is exactly "Source: RaceCharts Financial Data". Keep the returned source links, dates, coverage and warnings; do not replace attribution for other data sources. The builder resets cast-dependent colors/labels/captions and enables imported-header auto-fit, so set the new cast labels and restore the chosen presentation settings after building. For the bundled default, restore autoFitImportedHeader:false and titleSpacing:"". Keep the type, orientation and user-selected design; do not replace data or provenance in this presentation update.

For an investment-growth request, use totalReturn (dividends reinvested), the requested startAmount and startYear, and no extra deposits or withdrawals unless requested. Use available observations through the requested endpoint, or the latest available date when omitted. Monthly observations are a reasonable default for a long history. Keep the final partial period clear. Month-end balances may differ from the initial investment; do not change the numbers to make the first plotted month equal the starting amount.

Captions must describe the new data or verified events. Never retain an unrelated example's financial metric, units, captions, results copy, attribution or assets. Do not fabricate historical events or verification. If there is no supported story to tell, omit captions.

## Preview and saving

Render with preview_chart_draft and inspect real beginning/middle/end chart frames for readable titles, visible lines/bars/slices, labels, color contrast and correct units. Preview the actual final chart period when an end card would hide it. Correct layout problems in the draft, preserving the data.

"Show me a preview before saving", "preview only", "don't save" and equivalent requests mean: return the preview and STOP before commit_chart_edit or any video export, even if directSave is true. Wait for a subsequent user request to save. For other create/edit requests follow chart_capabilities and the server's save workflow. Never claim a chart was saved until commit succeeds, and never export without an explicit export request.
