# Box Doc Gen

## Template requirements

- `create_docgen_template` registers an existing `.docx` or `.pptx`; it does not insert placeholder tags. The file must already contain valid tags, and the acting user needs edit permission.
- Use `list_docgen_templates` to find registered templates and `get_docgen_template_by_id` to inspect one. The lookup uses `template_id`, while `create_docgen_batch` uses the template's referenced `file_id`.

## Generate documents

1. Resolve the registered template and its `file_id`.
2. Provide `destination_folder_id`, `output_type`, and one `document_generation_data` entry per output document.
3. Match every `user_input` key to a template placeholder and use distinct `generated_file_name` values.
4. Submit all documents using the same template in one batch. Use a separate batch for each additional template.
5. Record the returned batch ID and verify the expected filenames and count in the destination folder.

`output_type` is required. If neither the request nor approved input specifies `pdf` or `docx`, ask that single question before submitting the batch; do not infer the output type from the template extension.

Ask for the destination or input values only when they are missing or ambiguous. If the destination is externally shared and that exposure was not already authorized, explain it before generating.

If placeholder names are unknown, do not infer them; have the user inspect the source file or Template Creator and provide the exact keys.

Doc Gen batches are [asynchronous](https://developer.box.com/reference/v2025.0/post-docgen-batches). If outputs are not immediately visible, wait and check the destination again rather than resubmitting and potentially creating duplicates.

## Failures

- If registration fails for permissions or format, report the exact requirement rather than attempting a workaround.
- If tags are missing or invalid, guide the user to fix the source file:
  1. For `.docx`, open the file in Microsoft Word and install or open the [Box Doc Gen Template Creator add-in](https://support.box.com/hc/en-us/articles/36587535449747-Installing-the-Template-Creator-add-in-for-Microsoft-Word). Use its **Document Tags** panel to insert placeholders such as `{{customer_name}}`.
  2. For `.pptx`, add `{{variable_name}}` placeholders directly to text in slide shapes, tables, or WordArt.
  3. Ensure each placeholder name exactly matches a key that will be supplied in `user_input`. Use the [tagging guide](https://support.box.com/hc/en-us/articles/36152048850067-Adding-Template-Tags) for images, tables, lists, conditions, or calculations.
  4. Save the file, upload it to Box as a new version, and retry `create_docgen_template`.
- If input keys do not match the placeholders, surface the mismatched field names and correct them before retrying; guessing can produce silently blank output.
