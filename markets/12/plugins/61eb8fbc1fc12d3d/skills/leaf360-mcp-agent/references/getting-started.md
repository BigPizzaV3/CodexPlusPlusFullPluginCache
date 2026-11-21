# Getting Started

Use this reference when a loan officer is new to Leaf360, asks where to start, or asks what is left to set up.

## Flow

1. Call `leaf360_setup_status_get` first. Do not guess at what is configured.
2. Summarize in one or two sentences: what is done, what is missing, and the single most important next step.
3. Offer at most three next steps from `nextSteps`, in the order returned. For each, say whether you can do it now or it happens in Leaf360.
4. Do the steps you can do: `leaf360_lead_create`, `leaf360_partner_create`, `leaf360_setup_starter_pack_create`, template and automation drafts.
5. For app steps, give the path from `appPath` prefixed with `links.webBaseUrl` (the Leaf360 web app, normally `https://app.leaf360.com`) and say what to do there. Never show an API or backend host such as `app.leaf360.io`; if a link does not start with the web app origin, use the relative path instead. Never ask for passwords, verification codes, billing details, or system credentials, and never offer to enter them.
6. After the user reports a step is done, call `leaf360_setup_status_get` again and continue. Stop nudging once `nextSteps` is empty.

## What the assistant can do in chat

- Create leads and partners.
- Create the starter pack: five email templates, three SMS templates, and two automations, all as drafts. Run it once, then point the user to the review paths. Repeat runs report `exists` instead of duplicating.
- Draft more templates and automations on request.
- Explain any profile gap from `profile.checks` and why it matters, using `why` and `affects`.

## What happens in Leaf360

- Connecting email, buying a phone number, finishing texting registration, two-factor, billing, loan origination system credentials, spreadsheet import, profile fields, and the Brand Wiki.
- Activating automations. The starter pack leaves them as drafts on purpose.

## Readiness rules

- `phone.ready` requires an active texting-capable number and an approved texting registration. If registration is pending, say texts to borrowers may not be delivered yet.
- `profile.checks` that fail break the merge fields listed in `affects`; mention this when drafting templates.
- `brand.ready` false means templates use default colors; say so and point to the Brand Wiki.
- Onboarding steps are verified live where the backend can verify them; `verifiedBy: "stored"` means the user ticked it in the app and it could not be confirmed from data.
