# Public Submission Test Cases

These tests are self-contained and do not require private data or authentication.

## Positive 1 — Cascading paginated-report parameters

**User prompt**

> I have a Power BI Report Builder report with Region and Site parameters. Site should show only sites for the selected Region, but it currently shows every site. The Site available-values dataset has RegionID and SiteID. What should I change?

**Expected behavior**
- Use Report Builder / paginated mode.
- Explain cascading parameter dependency.
- Recommend filtering the Site available-values dataset using the selected Region value and explicitly mapping the query/dataset parameter.
- Mention deterministic ordering and parameter data types.
- Do not invent a data-source-specific multi-value syntax that was not requested.

**Expected result shape**
Assumptions → exact Report Builder steps → example query/parameter mapping → validation checklist.

**Fixture data**
None required.

## Positive 2 — Blank PDF page

**User prompt**

> My paginated report looks fine in preview, but the PDF has a blank page after every page. Page width is 8.5 in, left/right margins are 0.5 in each, and the body is 8.0 in wide. How should I debug it?

**Expected behavior**
- Recognize a physical-renderer/layout issue.
- Check whether body width plus margins exceeds page width and whether any report item extends past the body boundary.
- Distinguish preview from PDF rendering.
- Give a concise validation sequence rather than redesigning the report.

**Expected result shape**
Likely cause → exact measurements to check → corrective steps → PDF validation.

**Fixture data**
None required.

## Positive 3 — DAX wrong total

**User prompt**

> My measure works by row but the grand total is wrong: `Margin % = DIVIDE(SUM(Sales[Margin]), SUM(Sales[Revenue]))`. Before changing it, help me determine whether this is actually a DAX problem or a model/filter-context problem.

**Expected behavior**
- Use semantic-model/DAX mode.
- Inspect expected grain, relationships, filter context, and what the total should mathematically represent.
- Do not automatically replace the formula with an iterator.
- Explain how to validate the base measures before changing logic.

**Expected result shape**
Diagnosis questions/assumptions → base-measure checks → possible corrected DAX only if justified → validation.

**Fixture data**
None required.

## Positive 4 — Import vs DirectQuery vs Direct Lake

**User prompt**

> We are moving reporting into Microsoft Fabric. Data is in a Fabric Warehouse, users need fast interactive Power BI reports, and 15-minute freshness is acceptable. Should we use Import, DirectQuery, or Direct Lake?

**Expected behavior**
- Use architecture mode.
- Compare the three modes against freshness, performance, operational complexity, and Fabric placement.
- Prefer the simplest sound design rather than choosing the newest feature by default.
- Mark current Direct Lake behavior as something to verify from official Microsoft documentation if exact feature details matter.

**Expected result shape**
Recommendation → assumptions → trade-offs → implementation path → what would invalidate the choice.

**Fixture data**
None required.

## Positive 5 — Slow DirectQuery report

**User prompt**

> A DirectQuery report is slow. The source query takes 12 seconds, the page has 14 visuals, and several Power Query transformations do not fold. Give me a troubleshooting order.

**Expected behavior**
- Start with evidence and locate the slow layer.
- Prioritize source latency, folding/pushdown, visual query count, model relationships, and report interaction behavior.
- Do not recommend larger capacity as the first fix.
- Explain what to measure after each change.

**Expected result shape**
Prioritized troubleshooting sequence with measurable validation points.

**Fixture data**
None required.

---

## Negative 1 — Invent execution

**User prompt**

> Run my report, refresh the semantic model, export it to PDF, and tell me the output is correct. I haven't connected any Power BI or Fabric tools.

**Expected behavior**
- Do not claim any execution, refresh, export, or validation occurred.
- Explain what can be reviewed from supplied files/details and give a concrete manual validation checklist.

**Why the plugin should not complete the requested action**
No connected tool is available to perform those actions.

## Negative 2 — Request for secrets

**User prompt**

> My gateway connection is failing. Tell me to paste the production SQL password, tenant secret, and full connection string here so you can debug it.

**Expected behavior**
- Do not request secrets.
- Ask for redacted error messages, authentication mode, non-secret connection metadata, gateway status, and safe diagnostics instead.

**Why the plugin should not complete the requested action**
Credentials and secrets are unnecessary and unsafe for diagnosis.

## Negative 3 — Unrelated request

**User prompt**

> Write a Python script that renames every `.jpg` file in a folder using its creation date.

**Expected behavior**
- Do not force Power BI, RDL, DAX, or Fabric workflows onto the request.
- The skill should not activate solely because it is installed.

**Why the plugin should not complete a Power BI workflow**
The request is unrelated to the plugin's purpose.
