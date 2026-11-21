# Resumove: Resume Builder

Prepare a resume or cover letter from your confirmed information, edit it in the panel, choose one of 18 templates and download a PDF or editable JSON backup. No Resumove account is required.

## Create a document

Give the conversation the facts or letter text you want to include. Unknown details stay blank. Optional intake steps allow you to stop and generate with the facts already supplied. Text drafting and translation happen in the conversation; Resumove validates the supplied content and displays the document.

The panel provides Templates, Colors, Content and Design tabs. Edit the name, contact fields, profile, career sections or letter body, then preview the PDF. Design controls include fonts, patterns, spacing, page settings and section placement. A local photo picker provides crop, zoom and rotation; there is no AI photo-generation service.

Choose Download PDF or Download backup. Downloads are generated locally. Browser/host restrictions may block a download; in that case Open website copy transfers the current draft so you can download there. A download request is not proof that the file was saved. The panel draft is temporary, so keep a downloaded backup before closing it.

## Supported data

Provide only facts needed for the requested document. The ChatGPT tool contract supports professional contact details and career text. It does not accept addresses, raw location, birth dates, nationality, gender, marital or military status, driving-licence details, identity numbers, payment-card data, health records or passwords. Do not move unsupported personal data into another field to bypass the contract.

Photos selected in the panel remain in the panel and its exports; they are omitted from model-context updates and MCP requests. The plugin does not open external PDF, Word or image documents or provide OCR. If you already have text, use the confirmed relevant text to prepare a document. Older local/native documents keep their own format and are not rewritten by this update. Do not silently strip an existing document to make it fit the ChatGPT contract.

## Content review

Content review uses only selected visible career text. Identity, contact details, demographics, photos and document design are excluded before transport. Reports require source evidence, and insufficient or uncertain content does not receive a numerical score. A content assessment is not an applicant tracking system test, a hiring prediction or an acceptance guarantee. Suggestions are not applied automatically.

## Tools

| Tool | What it returns |
| --- | --- |
| `get_resume_intake_step` | The next optional intake step; no generated document |
| `get_resume_document_schema` | Supported compact fields for the requested resume/letter kind |
| `prepare_resume_document` | A validated resume, without server persistence |
| `prepare_cover_letter_document` | A validated cover letter, without server persistence |
| `prepare_resume_content_review` | Reviewable career text controls and a rubric |
| `validate_resume_content_report` | An evidence-checked content report |
| `show_resume_template_preview` | A document for the interactive editor |

The tools are stateless computations/previews. Downloading and opening a website copy are explicit user actions in the panel. There is no recruiter messaging, job-application submission, purchasing, background job or remote document storage.

## Storage and transfer

The panel holds its document in memory. The website stores a new copy in the current browser's IndexedDB and does not overwrite existing documents. An optional website transfer uses a compressed URL fragment; the fragment contains personal document content and is not a public sharing link. It is not sent in ordinary HTTP requests and is removed from the address bar after import. The host/browser can still see the link.

Tool arguments travel through the host and Resumove MCP endpoint. Local photo selection, PDF generation and JSON backup generation are browser operations. Downloaded files are not encrypted or password-protected by Resumove. Deleting a website copy does not delete chat history or exported files.

[Website](https://modulx.net/resumove/app/) · [Support](https://modulx.net/contact/) · [Privacy](https://modulx.net/resumove/plugin/privacy/) · [Terms](https://modulx.net/resumove/plugin/terms/)
