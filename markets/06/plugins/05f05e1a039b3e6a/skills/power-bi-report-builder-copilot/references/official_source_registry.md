# Official Source Registry

Last reviewed: 2026-09-23

Use official Microsoft documentation when current product behavior, licensing, limits, storage modes, or service capabilities affect the answer.

## Power BI Report Builder / paginated reports

- Paginated reports documentation: https://learn.microsoft.com/en-us/power-bi/paginated-reports/
- Expressions in Power BI Report Builder: https://learn.microsoft.com/en-us/power-bi/paginated-reports/expressions/report-builder-expressions
- Report parameter concepts: https://learn.microsoft.com/en-us/power-bi/paginated-reports/parameters/report-parameters-concepts-report-builder
- Export paginated reports: https://learn.microsoft.com/en-us/power-bi/paginated-reports/report-builder/export-reports-report-builder
- Export to Excel: https://learn.microsoft.com/en-us/power-bi/paginated-reports/report-builder/export-microsoft-excel-report-builder
- URL parameters / `rdl:` controls: https://learn.microsoft.com/en-us/power-bi/paginated-reports/report-builder-url-parameters

Current verified notes:
- Report Builder expressions are Visual Basic expressions evaluated by the report processor.
- Report parameters can filter data, control appearance, link reports, and can be created from dataset query variables.
- Paginated reports support multiple export renderers; renderer behavior differs, so export is part of report correctness.
- Current URL rendering controls use the `rdl:` prefix for rendering behavior such as format.

## Semantic models / DAX / modeling

- Star schema guidance: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
- DirectQuery model guidance: https://learn.microsoft.com/en-us/power-bi/guidance/directquery-model-guidance
- Incremental refresh configuration: https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-configure

Current verified notes:
- Microsoft recommends star-schema principles for semantic models optimized for performance and usability.
- DirectQuery performance depends on source, model, and report design; source-side optimization can be essential.
- Incremental refresh uses case-sensitive `RangeStart` and `RangeEnd` Date/Time parameters to define partition windows.

## Microsoft Fabric / Direct Lake

- Create a Power BI semantic model in Fabric: https://learn.microsoft.com/en-us/fabric/data-warehouse/create-semantic-model
- Direct Lake in Power BI Desktop: https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-power-bi-desktop
- Direct Lake semantic model tutorial: https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-power-bi-report

Current verified notes:
- Fabric supports Power BI semantic models using Direct Lake, Import, and DirectQuery depending on source and workflow.
- Direct Lake models are created in and edited against the Fabric workspace; current Desktop editing can be live against that workspace model.

## OpenAI plugin packaging references

- Package plugins: https://developers.openai.com/plugins/build/plugins
- Build skills: https://developers.openai.com/plugins/build/skills
- Submit plugins: https://developers.openai.com/plugins/deploy/submission
- Submission validation rules: https://developers.openai.com/plugins/deploy/submission-errors

Do not treat the notes in this file as permanent limits. Re-check the linked official documentation when the question is time-sensitive or feature-specific.
