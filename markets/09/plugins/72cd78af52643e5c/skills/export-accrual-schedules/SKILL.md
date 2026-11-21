---
name: export-accrual-schedules
description: Help download the SnapAccruals Excel supporting schedule after a confirmed bonus accrual calculation and explain the workbook. Use for exporting calculated rows and exclusions; does not create or post accounting journals.
---

# Export accrual schedules

Use the user's existing confirmed SnapAccruals calculation. Respect explicit choices and prior consent.

1. Check that the requested file/sample, period, and accrual rate match the displayed result. If there is no completed calculation, guide the user through preparing it first.
2. Direct the user to **Step 4: Review and download** and the workspace's Excel download button. `export_bonus_pilot` and `export_bonus_file` are app-only tools: do not attempt to call them from conversation or fabricate a download link. Do not ask for an email; the ChatGPT export tools do not require one.
3. Explain that the workbook contains calculated employees, exclusions, source data, and policy/settings. Uploaded-file exports also include mapping and review items. It is a draft supporting workbook, not a journal posted to an accounting system.
4. File export re-fetches the authorized attachment and uses the confirmed calculation settings. If it fails, report the actual error and help the user upload again if the attachment has expired. Do not claim a download succeeded without evidence.
5. Sending the workbook elsewhere or sharing employee information requires a separate user request; downloading it is not authorization to email or publish it.

## Keep the result source consistent

The workspace and chat may have different access to attachments. A missing file reference in chat does not prove that no file was uploaded or calculated in the widget. Use the current widget model context or the Discuss results in chat summary to identify the source and confirmed settings. Aggregate summaries omit employee rows and file references; never reconstruct a file or invent a download URL from them.

For an existing uploaded-file result, keep the same workspace and direct the user to Step 4: Review and download → Download Excel. Do not request another upload while the workspace still has the file. If the workspace was reset or the attachment expired, ask the user to reselect the file and confirm its settings. Never use the sample tools as a fallback for an uploaded-file request. If the source is unclear, ask whether the user means their uploaded file or the fictional sample.

When inputs are marked outdated, do not describe a previous result as current. Preserve the confirmed file, mapping, period, units, eligibility method, denominator and accrual rate. A returned result or generated link is not proof that a browser download completed.
