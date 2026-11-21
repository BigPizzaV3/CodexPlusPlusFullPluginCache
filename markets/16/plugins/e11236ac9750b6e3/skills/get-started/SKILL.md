---
name: get-started
description: Use when the user wants to create a legal document with Smarter Drafter. Explains how to find a form, fill it in, and give the user the generated files.
---

# Create a document with Smarter Drafter

Smarter Drafter turns a completed form into finished legal documents (DOCX, PDF and sometimes EML). The user only sees forms their firm has given them access to.

## Steps

1. Call `search_forms` to find the form. If more than one form matches, ask the user which one they mean.
2. Call `get_fields_by_form` to read the form's sections and fields. Ask the user for every required answer you do not have. Never make up client names, dates, amounts or other facts.
3. Show the user a short summary of the answers and ask them to confirm before you create the submission.
4. Call `create_submission`. Use a draft if the user wants to review or change answers first. Use `update_submission_answer` and `attach_submission_file` to change a draft, then `submit_submission` to finish it.
5. Give the user every generated file as a download. If a download returns 404 "Documents were not yet generated", call `get_submission_generated_documents_url` again every 5 seconds until they are ready. If you cannot download the files from the returned links, call `get_submission_generated_documents` to get them inside the tool result. If that also fails, give the user the submission link.

## Rules

- A completed submission cannot be changed. To change it, create a new submission.
- Document generation usually takes 5 to 60 seconds. Download links expire after 5 minutes; call `get_submission_generated_documents_url` for fresh links.
- Do not describe what a document says unless you opened and read it.
- Ask only for what the form's fields need. Leave the optional settings of `create_submission` and `submit_submission` empty unless the user asks for one of them.
- When a field's instructions say not to ask for a value, do not ask for it and do not send it. Save the submission as a draft and give the user the draft link, so they enter that value in Smarter Drafter.
