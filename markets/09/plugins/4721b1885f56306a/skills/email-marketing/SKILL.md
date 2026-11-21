---
name: email-marketing
description: Work in a Sequenzy email marketing workspace. Use when the user asks about their Sequenzy subscribers, campaigns, automated sequences, templates or email performance.
---

# Sequenzy email marketing

Use the Sequenzy tools to help the user run email marketing in the workspaces
they connected. Act only on what the user asked for.

## Choose the workspace

- Tools act on the selected company by default, so call them directly. Call
  `get_account` when the user asks which companies they can access, names a
  different company, or a tool reports that a company must be chosen; then
  use `select_company` or pass `companyId`.
- Use `get_app_urls` when the user wants a link to a page in the Sequenzy
  dashboard.

## Read before you write

- Answer reporting questions with read-only tools: `get_stats` for audience
  size and overall rates, `list_campaigns` with `get_campaign_stats` for
  campaigns, and `list_sequences` with `get_sequence_stats` for sequences.
- Find contacts with `search_subscribers` or `get_subscriber`. Reuse existing
  attribute names from `list_subscriber_attributes` before you set new ones.
- Check an audience with `get_segment_count` before you send to a segment.

## Draft, then confirm

- Create campaigns as drafts with `create_campaign`, and sequences with
  `create_sequence`; new sequences start disabled.
- Show a preview with `render_email`, or send the user a test with
  `send_test_email` or `send_sequence_test_email`.
- Generators such as `generate_email` and `generate_subject_lines` return
  drafts and send nothing. A company's first generation saves its inferred
  email design direction. `generate_email` and drafting from a prompt or goal
  (`create_campaign`, `create_sequence`) can read pages at URLs in the prompt.
- Before `schedule_campaign`, `enable_sequence`, enrolling subscribers, or any
  delete, cancel or bulk change, state the audience and the effect, and get
  the user's explicit confirmation. These actions can email real contacts or
  cannot be undone.

## Data the user should not share

Do not put payment-card data, health data, government identifiers, passwords,
API keys or other secrets, sensitive demographic data or precise location into
subscriber fields, events, notes or email content. Sequenzy blocks
recognizable values of these in contact names, tags applied to contacts,
attributes, notes, events and conversation replies. If a tool rejects data as restricted, do not
retry it under another field name, attribute, note or event; explain that
Sequenzy does not store this kind of data.

## Managed in the dashboard

API keys, outbound webhook secrets, data warehouse and export credentials, and
push notification credentials are entered and viewed only in the Sequenzy
dashboard. Web tracking keys are publishable browser keys, not API keys. If the
user asks for one of these, say so and offer the dashboard link from
`get_app_urls` instead of attempting it in chat.
