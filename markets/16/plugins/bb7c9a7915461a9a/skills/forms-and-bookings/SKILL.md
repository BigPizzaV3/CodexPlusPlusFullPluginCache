---
name: forms-and-bookings
description: Add contact, quote, newsletter and booking forms to a Frexy website, set the emails each one sends, and report how many people used them. Use when the person asks for a form, an enquiry or quote request, a booking or appointment page, form emails, or how many submissions arrived.
---

# Forms and bookings

Read `get_development_standards` with topic `forms` first: it holds the full contract.

1. **See what exists** with `list_forms` and `get_form`.
2. **Create one** with `create_form`: a `preset` (contact, quote, newsletter,
   callback, booking, scheduler), its fields, and `doneUrl`, a thank-you page in
   the site's own design, written first if there is none. A `theme` gives markup
   to start from: follow its `rules`, and fit it to the site's own design.
3. **A booking form** takes the owner's hours and time zone, asked from them,
   never guessed, in `config.booking`. Put `<div data-frexy-booking="<slug>"></div>`
   on the page; Frexy shows the free times and books them. The owner connects
   Google Calendar in Studio's Settings.
4. **Its emails.** `set_form_email` sets the notification to the owners and the
   confirmation to the visitor; `send_test_email` sends one to check it.
5. **How it is doing.** `get_form_activity` gives the counts and where people came
   from, and `get_email_activity` the emails' totals. You never read what people
   typed: the person does, in Studio.
6. `deploy_preview`, `get_deployment`, then send one test submission from the
   preview and give them the page's link.
