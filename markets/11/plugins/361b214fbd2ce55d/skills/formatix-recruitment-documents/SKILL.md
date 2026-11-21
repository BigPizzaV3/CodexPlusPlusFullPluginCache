---
name: formatix-recruitment-documents
description: General guide to Formatix for recruitment agencies and executive search firms - find the right template, see what a template needs, write search progress reports, appointment briefs, LinkedIn carousels and role teasers, draft "we have been retained" and appointment announcements, use a client's brand kit, start a role-briefing video, and change the firm's own template. Use for any Formatix request that the more specific Formatix skills (format CVs, shortlist pack, position specification, interview pack, fix a document, build our template, daily CV run, client submission email, blind profile, translate a profile) do not cover.
---

# Formatix recruitment documents

Formatix fills a recruitment firm's own branded Word, PowerPoint and Excel
templates with candidate and search details, on Formatix's servers, from the
user's own account. Results come back as download links.

Explicit instructions from the user take priority over this skill.

## Ground rules (every Formatix task)

- Reply in the language the user writes in. Documents follow the template's
  language and its extraction prompt; translate only when the user asks.
- Use only facts the user gave you or that are in a CV, note or message they
  shared. Never invent names, employers, dates, compensation, ratings, notice
  periods, quotes or client names. If something is missing, leave it out and say
  what the user could add.
- Credit-using steps: each tool says its cost. Say the cost before a step the user
  did not clearly ask for. If the account is short of credits, say so and that
  credits are managed in Formatix. Do not discuss prices, plans, trials or upgrades.
- Pass a `request_id` of your choosing on every credit-using call and reuse it on a
  retry: nothing is charged twice.
- If a tool says sign-in is needed, ask the user to connect Formatix and stop. If
  they have no account, point them to https://formatix.ai.
- Never put a client's name, logo or template in anything public. Never look up
  personal contact details of candidates or anyone else.
- When a document is ready, give the download links and a one-line summary, and
  remind the user to check it before it goes to a client or candidate. Do not show
  internal ids, raw tool output or technical error details.

## Which tool

| The user wants | Tools |
| --- | --- |
| The template that fits a need | `find_template` (plain-language request), else `list_templates`. No credits |
| What a template takes from a CV and the fields it fills | `get_template_schema` (template `id` and `type`) |
| A search progress report | `render_search_document`, `template_key` `search-progress-report` (0.5 credits): `funnel` (stage, count), `pipeline_rows`, `notes`, from the user's figures only |
| An appointment brief (candidate pack), then a LinkedIn carousel or role teaser | `render_search_document` `appointment-brief` (1 credit), then `linkedin-carousel` or `role-teaser` (0.5 each) with `payload` = the brief's returned `content` |
| The "we have been retained" LinkedIn post | `create_launch_announcement` (1 credit) |
| The appointment announcement at the end of a search | `announce_appointment` (1 credit), only after the user confirms the client agreed it can be announced |
| A document in a client's brand | `list_brand_kits`, then pass the kit's `id` as `kit_id`. Without it the firm's confirmed brand is used |
| A role-briefing video | `create_role_briefing_video`, then `get_video_status` |
| A change to the firm's own template | `refine_template` with one clear instruction and a `request_id` (`template_type` `cvtobios` for one saved with `push_designed_template`); `get_refine_status` if still working. Formatix keeps every earlier version |

For CVs, shortlists, position specifications, interview packs, corrections,
new templates, daily runs, submission emails, blind profiles and translations,
follow the matching Formatix skill.

## Briefs

`render_search_document`, `create_launch_announcement` and
`create_role_briefing_video` take a `brief`. `role` is required; add `location`,
`salary`, `reporting_line`, `must_haves`, `organisation_overview`,
`search_reference`, `jd_text` and `consultants` only when the user supplied them.

Confidential search: `brief.confidential = true`, the real client in
`client_name` (used only to check the output) and a neutral `client_descriptor`
such as "a listed European logistics group". Never write the client's name in your
reply, posts or documents.

## Out of scope - decline or redirect

- Posting to LinkedIn or publishing web pages: Formatix drafts, the user posts.
- Deleting templates, documents or data; changing templates Formatix set up for the
  firm (read-only): point to https://platform.formatix.ai.
- Buying credits or changing plans.
- Finding personal contact details, scraping LinkedIn or profiling individuals.
