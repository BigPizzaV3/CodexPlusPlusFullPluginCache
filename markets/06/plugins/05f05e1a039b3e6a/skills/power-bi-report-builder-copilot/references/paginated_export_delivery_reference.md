# Paginated Export and Delivery Reference

## Purpose

Use this file for PDF, Excel, Word, print, URL rendering, subscriptions, filenames, pagination, and delivery behavior.

# 1. Renderer-aware design

Paginated reports can render differently depending on output.

HTML preview generally follows soft-page-break behavior.

Physical formats such as PDF follow physical page size and hard-page-break behavior.

Design for the actual delivery target.

# 2. PDF

Check:
- page width/height;
- margins;
- report body width;
- hidden whitespace;
- page-break groups;
- repeated headers;
- images;
- font support.

A common horizontal blank-page cause is:

`body width + left margin + right margin > page width`

Also inspect items extending past the intended body boundary.

# 3. Excel

Excel is not just “PDF in cells.”

Check:
- merged cells;
- nested rectangles/tablix;
- page names/worksheet names;
- column alignment;
- hidden rows/columns;
- formulas vs rendered values;
- text vs numeric types.

Keep numeric values numeric when downstream Excel work is expected.

Avoid excessive decorative layout when Excel is the primary output.

# 4. CSV

CSV output is data-oriented.

Do not expect page headers, visual grouping, or rich formatting to behave like PDF.

Define the dataset/output fields needed for downstream use.

# 5. Print

Validate with the actual paper size, orientation, margins, and printer expectations.

Do not infer print quality from browser preview alone.

# 6. Page breaks vs separate files

A group page break creates sections/pages in one rendered report.

If the requirement is:
“one PDF per customer/site/region”

the solution generally requires separate executions, subscriptions, automation, or an external delivery process.

Do not claim a page break alone creates multiple files.

# 7. Subscriptions

When subscription behavior matters, verify current Power BI service capabilities and licensing.

Define:
- report;
- parameter values;
- schedule;
- recipient/destination;
- format;
- security;
- failure handling.

For regulated data, use organization-approved distribution channels.

# 8. Filenames

Prefer supported platform/subscription naming behavior.

If custom dynamic filenames require external automation, say so.

Do not rely on an RDL textbox value to control the exported file name unless the delivery mechanism explicitly supports it.

# 9. URL rendering

Power BI paginated reports support URL parameters for report parameters and rendering controls.

When constructing URLs:
- encode values correctly;
- distinguish report parameters from rendering parameters;
- verify current supported `rdl:` options;
- avoid exposing sensitive parameters in URLs when inappropriate.

# 10. Export validation

For important reports test:
- PDF;
- Excel;
- service view;
- print if required.

Validate:
- page count;
- row count;
- totals;
- section breaks;
- repeated headers;
- clipped text;
- numeric/date formatting;
- worksheet structure;
- file size/runtime.

Treat export as part of report correctness, not an afterthought.
