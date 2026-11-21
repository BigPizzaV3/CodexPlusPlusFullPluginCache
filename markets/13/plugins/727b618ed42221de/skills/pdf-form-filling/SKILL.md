---
name: pdf-form-filling
description: Fill a PDF form (W-9, I-9, W-2, 1099, SS-4 and other official or template forms) with the user through PDFFormly. Use when the user wants to fill, complete or sign a form and get the PDF. Asks the form's questions in the chat, signs with a saved signature, shows a review, and creates the PDF only after the user confirms.
---

# Fill a PDF form with PDFFormly

The user's answers are saved as a draft in their PDFFormly account. Every tool except `search_forms` needs the account linked (OAuth); ChatGPT starts the link when a tool asks for it.

## Hard rules

- **Never invent answers.** Ask for every value. Never guess dates of birth, addresses or amounts.
- **ID numbers stay out of the chat.** Questions marked `enterOnSite` (SSN, EIN, ITIN, TIN, passport, A-Number…) are never asked, accepted or repeated here. When the other questions are done, give the user `idUrl` once: a short PDFFormly page (no sign-in) for just those numbers. Continue when they say they are done.
- Never ask for passwords, card numbers or bank details. Payment happens on pdfformly.com only.
- **Signatures:** only sign with a saved signature the user picked in this conversation. With no saved signature, give the `signUrl` so they sign on pdfformly.com.
- **Review before PDF:** call `review_document`, show the answers, and ask "Is everything correct?". Call `create_pdf` with `confirmed: true` only after a clear yes.
- If a tool returns `AUTH_REQUIRED`, let ChatGPT link the account, then retry.
- Answer in the user's language and pass it as `locale` when it is en, es, fr, tr, vi or zh-Hans.

## Workflow

1. **Pick the form.** If the user names an exact form, use `search_forms` with that name to get its slug; otherwise search by purpose and let them choose from the cards.
2. **Start.** `start_form` with the slug. Keep the returned `documentId` for the whole conversation; do not start the same form twice.
3. **Ask the questions.** Go section by section, two to five questions at a time, in plain language. Use each question's `help`, `options` and `type`:
   - `yes_no` → true/false · `choice` → one of `options` · `date` → YYYY-MM-DD · `digits` → all `length` digits (for example an account number). Skip `enterOnSite` questions.
   - Optional questions: offer to skip them.
4. **Save.** `fill_answers` with `{ questionId: value }`. Ask again about anything in `errors`. Some questions appear only after earlier answers; call `get_form_questions` with `onlyMissing: true` to see what is left.
5. **Sign** (when `signatureLines` is not empty and `wetInkSignature` is false): `list_saved_signatures` → the user picks → `apply_signature`. No saved signature → share `signUrl`. Wet-ink forms are signed by hand after printing; say so.
6. **Review.** `review_document`, then ask whether everything is correct. Fix answers with `fill_answers` if not.
7. **PDF.** `create_pdf` with `confirmed: true`:
   - `ready` → share `downloadUrl` (valid 30 minutes).
   - `processing` → `get_pdf` with `outputId` after a few seconds.
   - `payment_required` / `email_unverified` → share `actionUrl`; the answers are already saved there.

## Do not

- Do not create a PDF before the review is confirmed, or call `create_pdf` for informational questions.
- Do not give legal or tax advice beyond what the question's `help` text says; suggest the issuer's instructions or a professional.
