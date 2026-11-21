---
name: author-a-template
description: Write, render, test and publish a react.email template for a company in Send & Retain, in that company's brand and voice. Use when the user wants a new email, a rewrite of an existing one, or a preview of how one looks.
---

# Author a template

1. Resolve the company (`email_list_projects`) and read its brand kit with
   `email_get_brand`. Templates use the **company's** brand, never generic
   styling. If the kit is empty, infer it from the website and save it with
   `email_update_brand` first.
2. Agree on the purpose. **Transactional** (receipts, shipping, password
   resets) still delivers to unsubscribed contacts; **marketing** (category
   `lifecycle`: welcome, win-back, promotions) does not. Agree the subject, the variables (name, type,
   required, fallback) and an outline.
3. `email_create_template` with TSX built from react.email components inside a
   `<Tailwind>` wrapper. Templates may import only `react` and
   `@react-email/components`.
4. `email_render_template` with example variables. Fix any compile error it
   returns and iterate until the HTML, text and subject read right. Show the
   user the result by opening `previewUrl` in the client’s browser panel when
   available, or show a clickable preview link. Do not open a saved HTML file
   in the source editor. The link expires after 15 minutes and anyone holding
   it can view the sample; never describe it as login-protected. If the link is
   unavailable, use the returned HTML and explain the fallback. A preview-only
   request stops here: nothing is sent or published.
5. `email_send_template_test` to the user's own inbox when sending is set up for
   the company, and ask them to check it in their mail client.
6. Publish with `email_publish_template_version` only on the user's explicit
   go-ahead, and never untested. Published versions are immutable: later edits
   create a new draft version.

To restyle every template after a brand change, use `email_restyle_template`.
To revise an existing one, `email_get_template` then `email_update_template`.
