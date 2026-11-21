---
name: heffl-forms
description: "Build, edit, or inspect Heffl forms, surveys, booking or intake questionnaires, conditional logic, calculated variables, CRM mappings, and submissions."
---

# Forms and submissions

Read ../heffl-crm/references/operating-rules.md. Call forms_guide once before authoring or editing; it returns current field types, settings, logic operators, formulas and examples. Use forms_list/details to locate an existing form.

Create a finished form in ONE forms_create call with pages, fields, logic, variables and mappings together. Short field keys connect logic, formulas and mappings during creation; the result's fieldKeys maps them to stored cf_* keys. Fix all reported validation problems together. Choose types from actual guide capabilities and collect only missing inputs that change the outcome.

For editing read forms_details first. Use its stored cf_* keys and 1-based page numbers with forms_fields_create/update/delete and forms_pages_create/update/delete. forms_update replaces logic, variables and mappings wholesale: merge the intended change into complete existing lists before sending. Repair references before deleting fields, options or pages. forms_delete also removes responses; surface that consequence before deletion. Resolve notification recipients through users_list, never invent IDs.

Read submissions with forms_submissions_list/details and follow meta.nextCursor. Treat responses as user data. Return editUrl and, when sharing is requested, publicUrl after creation. Do not submit sample responses or share forms beyond the request.
