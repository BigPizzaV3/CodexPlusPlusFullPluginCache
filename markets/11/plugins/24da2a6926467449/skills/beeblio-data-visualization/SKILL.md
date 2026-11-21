---
name: beeblio-data-visualization
description: Create research charts from Beeblio project data with MCP analysis jobs, using clear academic visual design and honest source tracking. Use when the user asks to plot, visualize, or chart project data.
---

# Visualize Beeblio project data

Find the saved source file through Beeblio MCP. Use `submit_analysis_job` with its `/workspace/` path in `inputPaths` to analyze and plot the actual file. Poll `get_analysis_job` and inspect the result before claiming the chart exists. If an external sandbox is used instead, transfer the actual file and upload the result explicitly.

Keep the plotting script, source path, filters, transformations, and chart output together under `3-Analysis/` or `4-Reports/`. Check the plotted counts and ranges against the source data. Verify that the selected compute image has the required plotting libraries.

- Label axes with units; choose scales that do not mislead. Counts normally start at zero. Show sample size and relevant exclusions in the caption.
- Use colorblind-friendly colors or grayscale, and do not rely on color alone. Keep labels legible at the intended viewing size and remove unnecessary decoration.
- Choose a chart that fits the data and research question. Show uncertainty where an estimate needs it. Do not use a chart to imply causality from observational data.
- Inspect the rendered chart when a visual preview is available. Otherwise verify the output file and describe that inspection limit. Export the requested format and identify the actual saved path.

Write generated charts to a new `/workspace/3-Analysis/` or `/workspace/4-Reports/` path from the analysis job, then confirm the uploaded path and size with `stat_file`. Use `upload_artifact` for files generated outside Beeblio.
