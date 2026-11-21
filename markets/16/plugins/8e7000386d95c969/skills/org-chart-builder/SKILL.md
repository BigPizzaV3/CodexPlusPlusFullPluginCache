---
name: org-chart-builder
description: Make an org chart, organizational chart or team hierarchy from a team list, spreadsheet or CSV with MivoChart, and return an editable link.
---

# Org chart builder

When someone wants an org chart from a team list, collect each person's name, job title, and direct manager's name. A top-level leader should have no manager. Department, FTE (0 to 1), and whether a role is vacant are optional. Ask only for missing relationships that prevent a reliable hierarchy.

Call `build_org_chart` with the list and the user's preferred locale. If it reports a cycle or ambiguous manager, explain the affected names and ask for a corrected manager; then call it again. Mention any unmatched manager warnings because those people may be left unplaced. Present the returned link clearly and say it opens an editable chart in the browser.

For a file, use `get_csv_import_format`. For browsing, use `list_org_chart_templates`; when a template is chosen, use `open_org_chart_template`.
