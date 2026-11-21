---
name: onboarding
description: Set up Impulse and create a first branded event with registration, an attendee landing page, and an automatic confirmation email. Use for first-event setup or resuming unfinished onboarding.
---

# Set up an Impulse event

Help the user get a working event ready to share: one registration page, one attendee landing page, and one automatic confirmation email. Match their brand and event style, make sensible design decisions, and keep questions to essential facts and preferences you cannot infer. Everything can be edited later.

## Connect or resume

If Impulse is not connected, guide the user through the host's connection flow. They can create an account with verified email or Google there; return to setup after connection.

Use `get_account_context` to confirm the connected account and available capabilities. Check existing events with `list_events` before creating one. Resume an event already identified in this conversation; if several could be the unfinished setup, ask which one. Do not change an unrelated event.

Keep billing and advanced setup out of the way unless the current allowance prevents registration or the user asks. If a tool returns a capacity notice, report its actual used, total, and remaining allowance. The Free allowance counts distinct attendees across the organization; it is not a time-limited trial. For MCP connections, only direct the user to the portal Billing page when a limit has been reached and they ask about their plan. Use the environment-specific Billing link in the server instructions.

## Gather event details

Reuse the user's event description, website, flyer, images, and earlier answers. If the event is unclear, ask for its name or purpose in one short question and invite a website or brand reference. A brand reference is helpful, not required.

Infer colors, typography, tone, layout. Ask only for missing facts that would materially change the event. Do not invent dates, times, venues, ticket prices, agendas, or organizer contact details. Omit unknown details or use “to be announced.” Use the context timezone unless the user explicitly supplies another. Extract any known dates and times from the plain-text brief into `create_event.dates` (`start`, `end`, `timezone`). Use `YYYY-MM-DD` when only a date is known, a local date/time such as `2027-06-15T19:30` when both are known, or RFC3339. All schedule fields are optional; never invent a missing time or end date. Have the page ready before asking any remaining date/time questions in MCP. Portal onboarding has no chat window and proceeds without questions.

## Choose designs

When creating a new event, you MUST start its pages and emails from the starter/example library and customize those resources. Only create them from scratch if the user explicitly requests it. A request for custom branding or design does not override this requirement.

Use the chosen preset from the event context. When choosing a preset, read `list_event_presets` and select the one that creates registration, an attendee landing page, and one automatic confirmation email.

When choosing a registration design, search `search_page_starters` with `presetId` and `pageType=registration`. Show two to four relevant designs with `show_starter_gallery`. Inspect its image attachments; use the returned `imageIndex` to identify each design. Recommend one direction and let the user choose or ask you to choose. Continue with the chosen design when it is already in the event context.

Choose matching attendee and email starters yourself unless the user wants to choose them. Use `search_page_starters` and `search_email_examples` with the same `presetId`, and compare tags and actual previews. Read the selected documents with `get_page_starter` and `get_email_example`. Starter IDs from these searches work with `create_event`, which copies the catalog assets and binds links between its selected pages and email.

Choose the confirmation email to match the selected pages' typography, palette and tone. `default-email` is a versatile branded Impulse confirmation; use it when it fits the design. `basic-confirmation` is the minimal option for users who request that style. Inspect the email preview alongside the selected pages before creating the event.

## Create resources and drafts

For a new event, call `create_event` with the agreed name, preset, suitable URL slug, and starter selections requested by its schema. Read the result before continuing. Creation publishes the starters and enables registration confirmations; subsequent customization stays in private drafts until published.

Use the `pages` and `emails` resource references returned by `create_event` as tool targets. Pages are keyed by slug and emails by preset name. When resuming an existing event, discover its resources with `list_event_pages` and `list_email_templates`.

Read `get_skill_page_builder` and `get_skill_email_template` before editing, previewing or managing drafts. Follow their authoring requirements for document structure, personalization, assets and feature behavior.

After creating the event, create a draft for each resource with `create_page_draft` or `create_email_draft`. Pass the returned `draftId` in subsequent targets while editing, checking and publishing that resource.

## Customize the experience

Apply one consistent design across the three resources:

- Use the user's logo, colors, imagery, tone, and event name. Replace sample branding, event details, support addresses, social links, and offers.
- Keep registration short. Collect a required email address and the name fields the event needs. Include a phone number, waiver, or other extra fields only when relevant to the requested experience.
- Make the attendee page useful immediately: confirm registration, show known event details, and provide the relevant next step. If it includes photos, show a clear empty state until photos are available. Remove unrelated sample features.
- Write a confirmation subject and message that identify the event and explain what happens next.
- Format raw `event.dates.start` and `event.dates.end` with `formatDate` or `formatDateRange` from the page/email guide, using the template language and event timezone with empty fallbacks for unknown values. Read stored scheduling details with `get_impulse_event`; change them with `update_event_dates`. Missing dates never prevent registration, email delivery or Wallet use.
- Keep the pages usable on mobile, with legible text, visible labels, and clear form errors.

For user-uploaded files, use `create_editor_upload`, the returned upload URL, `finalize_editor_upload`, then `store_page_file`. Follow the authoring guides to use stored assets in pages and emails.

## Verify the registration flow

Verify that successful registration and the confirmation email open the event's attendee page with that attendee's identity preserved, unless the confirmation email does not require a link. Follow the authoring guides for the personalized links and redirect actions.

Use `list_template_tags` to confirm `sent-on-registration` is assigned to the confirmation email. If needed, use `assign_template_tag` with the confirmation email's ID. The preset sends this email once when a guest registers with an email address.

Read the saved drafts with `get_page_document` and `get_email_document` to check the registration actions, attendee links, and personalization against the intended experience.

Inspect `screenshot_page` for both pages and `screenshot_email` for the confirmation at desktop and mobile widths.

Show the finished work with `show_page_preview` and `show_email_preview`. Test the form in an available browser preview, including required-field errors, the success state, and the destination link. Preview submissions are simulated and do not create a real attendee. If browser interaction is unavailable, say which runtime checks remain untested.

Offer a real registration walkthrough or a test email to an address the user chooses. A test email sends real mail and needs their request; follow the email guide for test delivery.

## Publish and hand over

A request to create a live, working event includes publishing the finished customization. Carry that authorization through the three drafts without asking separately for each resource. Use `publish_page_draft` for both pages and `publish_email_draft` for the confirmation email, inspecting each result before reporting the customized event as live.

Finish with the public registration URL, a registration QR code from `download_registration_qr`, and the event's portal link for managing attendees and making changes. Use the portal origin returned by tools or the connected Impulse environment. Clearly state whether the customized resources are published, that confirmation sends automatically on registration, and any details or runtime checks still outstanding. Share the registration URL, not a personalized attendee link.
