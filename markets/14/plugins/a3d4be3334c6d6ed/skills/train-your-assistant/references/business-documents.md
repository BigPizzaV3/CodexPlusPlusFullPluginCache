# Customer-facing PDFs from approved facts

<!-- ChatGPT Codex — CODEX-V2-006. Working V2 source, not a public release. -->

Use the business-document tools to create an informational fact sheet or catalogue
when the owner asks. These generate actual PDFs; they do not send them, create a
public listing or change the AI knowledge. Photos, complex brochure designs, DOCX,
quotations with calculations and multilingual typesetting are separate capabilities.

1. Identify the connected company and read get_business_draft. Confirm that an
   approved snapshot exists. Never substitute the latest unapproved interview.
2. Ask only for document choices not already clear: selected offerings, title and
   optional brand colour. Keep courses, packages and add-ons distinct. Do not invent
   inclusions, price calculations, availability or tax treatment for the design.
3. Call create_business_document with expectedApprovedRevision and a stable requestId.
   Only confirmed customer-facing facts enter the file. Internal floors, notes,
   source text and unconfirmed claims are deliberately omitted. The current layout
   is text-based with the approved business name and selected colour; no logo/photos
   are automatically obtained or licensed.
4. Inspect all pages using inspect_business_document. Check wrapping, page breaks,
   currency, prices, units, inclusions and package distinctions. Some hosts do not
   show tool images to you (ChatGPT did not, 28 Oct 2026). If you cannot see the
   page image, say so plainly, never claim a visual check, check the content from
   review_business_document's exact content, and ask the owner to open the PDF to
   judge the layout. Get the actual PDF
   with get_business_document and show the owner the private draft link. It expires
   in ten minutes and is a bearer link: anyone holding it can read the file during
   that time. Do not publish or share it. It is not a permanent public asset.
5. Call review_business_document without confirm. Show the exact file/content and
   explain that it is still private and marked DRAFT. Only after the owner approves
   call again with the same documentId, previewId and confirm true. A review expires
   after 30 minutes. Changed approved business facts require a fresh document.
6. Approval removes the DRAFT label without changing the customer-facing facts.
   Get a fresh download link; the preview's older link cannot fetch replaced bytes.
   Sharing with customers, sending messages or publishing still needs a separate
   owner action through a supported workflow.
7. list_business_documents resumes the library and flags stale source revisions.
   Warn about stale documents and create a replacement for review; do not silently
   overwrite an old approved file or claim downloaded copies updated themselves.
8. Delete only when the owner requests removal, using confirm true. Deletion revokes
   existing links but cannot retract downloaded copies. Source facts and AI knowledge
   are separate and remain.

The library holds at most 20 PDFs and 20 MB, with each file limited to 2 MB and
24 pages. The renderer needs local ReportLab, DejaVu fonts and Poppler. Unsupported
glyphs/shaping fail explicitly; never silently remove text or pretend all languages
are supported. Review an English version through the ordinary fact-approval flow
if required. A rendering failure is not a generated file or approved document.
