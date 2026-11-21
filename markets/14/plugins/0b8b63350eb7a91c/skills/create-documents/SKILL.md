---
name: create-documents
description: Create PDFs, images and e-invoices with Dynamic Document API. Use when the user wants a document from one of their templates (an invoice, quote, certificate, report or social image), a PDF from HTML or Markdown, an e-invoice (XRechnung, ZUGFeRD, Factur-X), or several PDFs merged into one.
---

# Create documents with Dynamic Document API

The Dynamic Document API tools render documents in the workspace the user chose when they signed in. Each render
returns download links that expire.

## From a template

1. Call `list_templates` to find the template. Filter by name or type when the user names one; ask which template
   to use when several fit.
2. Call `get_template_schema` with its id. It returns the fields the template expects, which are required, and an
   example payload.
3. Fill the data from the conversation. Ask the user for required values that are missing instead of inventing
   them, such as customer addresses, amounts or invoice numbers.
4. Call `render_pdf_from_template` for PDF templates or `render_image_from_template` for image templates.

## Without a template

- `render_pdf_from_html` takes HTML and CSS, for layouts the user describes or pastes.
- `render_pdf_from_markdown` takes Markdown and a built-in theme, for notes, reports and letters.
- `create_einvoice` creates the XML of an e-invoice from invoice data and validates it. It needs a workspace plan
  that includes e-invoicing; on other plans it returns `plan_feature_unavailable`.
- `merge_pdfs` joins 2 to 200 PDFs from earlier renders or public URLs into one.

## Test renders and final documents

Renders are test renders by default: they carry a TEST watermark and are free. Show the user the test result first.
Render again with `test: false` only when the user asks for the final document; final renders count towards the
workspace's usage.

## Results

- A render result has the status `succeeded`, `failed`, `queued` or `processing`. Share the download link of each
  file when it succeeded, and the error message when it failed.
- A render that takes longer than 25 seconds keeps running. Call `get_render` with its id to collect the files.
- Download links expire. `get_render` returns new links for the same render.

## What the tools cannot do

The tools cannot send emails, edit or delete templates, change settings, or reach other workspaces. Say so when the
user asks for one of these, and point to the Dynamic Document API dashboard.
