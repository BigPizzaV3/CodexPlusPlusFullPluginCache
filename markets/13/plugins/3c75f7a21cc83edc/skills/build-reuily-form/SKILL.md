---
name: build-reuily-form
description: Create, revise, publish, share or unpublish a Reuily form, survey, questionnaire or quiz (feedback, NPS, registration, RSVP, intake, application, lead screening, booking, consent with signature) using the Reuily tools.
---

# Build a Reuily form

Reuily forms are conversational: usually one question per page, with optional
branching between pages. Use this workflow whenever the user wants a real,
shareable form rather than a list of questions in chat.

## Create

1. If the request is vague, ask at most one or two clarifying questions (who
   fills it in, what decision the answers support). Otherwise just build it.
2. If the user mentions a common use case and wants a head start, you may call
   `list_templates` and offer a match; use `create_form_from_template` only if
   they pick one.
3. Otherwise call `create_form`:
   - `request`: the user's request in their own words, including every question,
     option, branch and style they asked for. Reuily checks the form covers it.
   - `form`: the complete design, following the page catalog and rules in the
     tool description. Use the matching page template per question (nps for
     recommendation, rating for stars, contact-info for grouped contact fields).
   - **Quiz:** set `formKind: "quiz"` and give every scored question its
     `quizAnswers` (option values). Add `settings.quiz.passPercent` only when
     the user named a pass mark, and keep the pass mark in `request`: Reuily
     drops one the request doesn't mention. Reuily adds pass and fail endings
     for a pass mark; for the user's own copy, put thank-you pages after the
     default one with `quizEnding` `{kind: "passed"}` or `{kind: "failed"}`,
     or `{kind: "range", min, max}` for a score band.
   - **Lead screening:** set `formKind: "lead"` and ask 4–6 qualifying choice
     or number questions on what separates good customers (need, budget,
     timeline, fit, authority), then name, email and phone if a call follows.
     Tag each qualifying question (Reuily refuses a lead form with fewer than
     3 tagged, or with most choice and number questions neither tagged nor
     `leadSkip`; when the user listed the questions, theirs are enough. A lead
     form of only the contact fields the user listed is saved as a plain form):
     `leadTags` `{optionValue: "good" | "no_fit"}` on choices, leaving answers that are neither untagged (neutral: they rule
     nobody out but don't count toward hot). On numbers or
     ratings use `leadRule`: `goodMin` when more is better or `goodMax` when
     fewer is better, and `noFitMax` or `noFitMin` for numbers that rule
     someone out. One `no_fit` answer rules a person out whatever else they
     answer, so keep it for real deal-breakers; doubt, early research or a
     shared decision is never one, and Reuily clears such tags unless the
     request rules those people out. Set `leadMustHave: true` on at
     most one question whose good answer a hot lead needs (such as a required
     budget), and `leadSkip: true` on choice or number questions that don't
     affect the lead. Set `settings.lead.picky` (`relaxed`, `normal`, `picky`)
     only when the user says how strict to be, and `settings.lead.stopEarly`
     or `bookingHotOnly` only if asked (say so in `request`: Reuily drops an
     early stop the request doesn't mention). For a different message or link
     per fit, put thank-you pages after the default one with `leadEnding`
     (`hot`, `warm`, `no_fit`); don't route to them, Reuily picks the ending
     from the lead's level.
   - **Look:** `themeSelection.presetId` picks a gallery theme that fits the
     form. If the user gives brand colours or asks to recolour something
     ("green buttons"), keep a fitting preset and add `colors` with `#RRGGBB`
     values for just those parts: `formBgColor`, `textColor`, `headingColor`,
     `fieldLabelColor`, `descriptionColor`, `buttonColor`, `buttonTextColor`,
     `inputBgColor`, `inputBorderColor`, `cardBgColor`. Never guess brand
     colours.
   - **Logo and images:** `logo: {url, placement, size}` shows a logo on every
     page (placement `top-start`, `top-center`, `top-end` or a `bottom-`
     corner; size `small`, `medium`, `large`). A page takes
     `branding: {backgroundImage, layout, backgroundSize}` for a cover or
     background, and questions and choice options take `imageUrl`. Use only
     HTTPS image links the user gave you or that you found, such as the logo
     on their website; Reuily refuses links that aren't images.
   - **Kiosk mode:** when the form runs on one shared screen used by person
     after person (a tablet at a booth, front desk or event check in), set
     `settings.kioskMode: true`. After each response the form starts over at
     its first page. If the result says kiosk mode isn't available on the
     plan, tell the user the form works as normal; don't suggest upgrading.
4. If the tool returns validation problems, fix exactly those and call it again.
5. Reply with a short outline of the form and the `edit_url`. Mention any
   `automatic_fixes` that change what the user asked for.

The form is saved as an unpublished draft. Do not publish it in the same turn
unless the user explicitly asked for it to go live.

## Revise

- For a draft created in this conversation, call `get_form`, edit its `form`
  object, and send the whole result to `update_draft_form`, keeping each
  ending's `leadEnding` or `quizEnding`, and the `logo`. Include
  `themeSelection` or `colors` only if the user asked for a different look;
  `get_form` returns the current theme and colours in `style`. To hide the
  logo, send `logo: {show: false}`.
- `update_draft_form` refuses published forms and forms with responses so
  collected answers stay consistent. In that case explain why and give the
  `edit_url` so the user can change it in the Reuily builder.

## Publish or unpublish

- Call `publish_form` only after the user clearly asks to publish, share or go
  live. Then give them the `public_url`.
- If `publish_form` says a lead form has questions that aren't tagged, name
  them. Tag them, or set `leadSkip` on ones that don't affect the lead, with
  `update_draft_form`. Only if the user agrees their answers shouldn't count,
  call `publish_form` again with `allow_untagged: true`.
- If they will share it in several places, offer one link per place so Reuily
  can report where responses came from: append `utm_source` (for example
  `instagram`, `newsletter`), optionally `utm_campaign` and `utm_medium`, or
  `ref` for a person or partner, to the `public_url`, e.g.
  `<public_url>?utm_source=instagram&utm_campaign=spring`. Use lowercase,
  hyphenated values and never put personal data in a link.
- `unpublish_form` stops new responses and keeps existing ones.
- For a readable link like `reuily.com/@team/spring-survey`, use `set_form_link`
  when the user asks for a custom link. If the form already had a custom link,
  say the old one will stop working. If it says custom links aren't available
  on the plan, tell the user the form keeps its standard link; don't suggest
  upgrading.
- `update_form_settings` changes kiosk mode (`kiosk_mode`, and
  `kiosk_restart_seconds` from 5 to 20), whether the form accepts responses,
  its closing date (`closes_at`), response limit (`submission_limit`) and the
  message people see once it's closed. It works on published forms too.
  Confirm before closing a form or setting a limit, since both stop new
  responses. `get_form` shows the current settings.
- Integrations (Google Sheets, Slack, Discord, webhooks) and notification settings are set up
  in the Reuily app from the form's `edit_url`; they aren't available here.

## Rules

- Never invent form IDs, links or content: get them from tool results.
- Do not ask for or accept passwords, payment card numbers or government IDs as
  form questions unless the user insists and understands the sensitivity.
- If a tool says the user's role or plan does not allow an action, say so
  plainly. Do not try other tools to get around it.
