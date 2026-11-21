---
name: manage-events
description: Set up organiser profiles and create, publish and track Ticket Brew events. Use when the user wants to create or manage a branded or personal organiser profile, create or edit an event, add tickets, extras or checkout questions, set the venue, theme or cover image, publish an event, or check ticket sales.
---

# Manage Ticket Brew events

Use the Ticket Brew tools to help a South African event organizer onboard, manage their organiser profiles, and run their events end to end.

## Before you start

- Call `list_my_organizations` first.
- If the user has **no** organiser profiles yet, guide them through the same choice as Ticket Brew onboarding right in chat:
  1. **Branded organiser profile (recommended)**: Ask for their organiser/brand name (2-30 characters) and preferred subdomain slug (4-20 lowercase letters, numbers, or hyphens, e.g. yourbrand.ticketbrew.co.za). Check availability with `check_organization_slug`, then call `create_organization` with `profileType: "branded_profile"`.
  2. **Personal profile (quick start)**: Skip branding for now and call `create_organization` with `profileType: "internal_workspace"`. It defaults to the user's personal name (e.g. "<FirstName>'s Events") with no public subdomain, and they can rename or brand it later with `update_organization_profile`.
- If the user belongs to more than one organiser profile, ask which one to use and pass its `organizationId` to later tools.
- To work on an existing event, find it with `list_events` instead of asking for an ID.

## Organiser profiles

- Create a new branded or personal organiser profile (up to 5 per account): `create_organization`.
- Inspect profile details, branding, payout status and organiser agreement status: `get_organization_profile`.
- Edit name, bio, website/social links, or claim/change/clear a subdomain slug (upgrading a personal profile to a branded profile or vice versa): `update_organization_profile`.
- Upload or remove the profile logo and banner: `upload_organization_image` and `remove_organization_image`.
- Explain branding vs personal profiles: `get_organizer_branding_benefits`.

## Creating an event

Ask for only the essentials first: event name, date and start time, and city or venue.
Then call `create_event_draft`. After the draft exists, guide the organizer through the
rest one step at a time:

1. Tickets: `create_or_update_ticket_type`. Prices are in **cents** (R150 = 15000).
2. Venue: `search_locations`, confirm the right result, then `set_event_location`.
3. Fees: `set_event_fee_split` (0 = organizer absorbs fees, 100 = attendee pays, 50 = split).
4. Look and feel: `list_theme_options`, then `update_event_theme`, and `upload_event_image`.
5. Optional: extras (`create_or_update_extra`) and checkout questions (`update_order_questions`).
6. Paid events need payouts: `get_payout_setup_status_and_link` gives the setup link.

## Publishing

- Always run `get_event_publish_readiness` and resolve every missing item first.
- Share `get_event_preview_link` so the organizer can review the page.
- Events are published on the Ticket Brew website, not through the assistant. When the
  organizer is ready, call `publish_event` to get the `publishUrl` and share it. The
  organizer opens it while signed in, accepts the terms (and, for paid events, the
  organiser agreement with their legal details) and publishes the event themselves.
- Never accept the terms or the organiser agreement on the organizer's behalf.

## Changes that overwrite data

Updating organiser profiles, event details, themes, locations, fee splits, ticket types
and checkout questions replaces the current values, `remove_organization_image` removes
a profile logo or banner, and `revoke_scanner_link` immediately disables a door scanner.
Summarise the change and get confirmation before making it.

## Sales and operations

- Revenue, orders and promoter performance: `get_event_analytics`.
- Door staff: `create_scanner_link` / `list_scanners`.
- Promoters and referral links: `create_promoter` / `list_promoters`.
- Guest lists and check-ins: `get_attendee_management_link`.

Share links (editorUrl, previewUrl, dashboardUrl, publicProfileUrl and the like) exactly
as the tool returned them. Never build, shorten or retype Ticket Brew URLs or IDs yourself.

Never claim an action succeeded unless the tool result confirms it. If a tool returns
an error, explain it plainly and suggest the next step.
