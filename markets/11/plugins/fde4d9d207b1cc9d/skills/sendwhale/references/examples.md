# SendWhale example workflows

Use the real tool catalog and granted workspace. These examples do not add tools or permissions. Reuse the user's known facts and current draft IDs; ask only when a necessary choice is missing.

## Draft and design

**“Import our website and draft a welcome email.”** Read `sendwhale_get_context`, import the supplied public website with `sendwhale_import_brand`, author HTML from verified brand facts, then save one draft with a stable key. Show import warnings and the actual review/canvas links. No audience or sending domain is needed.

**“Create a welcome email and send it to Sarah.”** Save and show the welcome draft, then use `sendwhale_prepare_publish` to open its native review. State that it remains unsent. The email address in the request does not turn this drafting connection into a sending API.

**“Design a Black Friday email with 40% off.”** Use the supplied offer as an accepted fact, saved brand assets and a known destination. Do not invent its end date, exclusions or product prices. Save a draft and show its subject and review link.

**“Create three emails for our July 15 launch: the big reveal, the deep-dive demo, and a final push for sign-ups.”** Give the emails distinct names and jobs. Use the same approved launch facts, product links and tone; do not add a fictional countdown or scarcity claim. Save all three in ONE `sendwhale_save_email_drafts` call with their named `emails` array and a short accepted `brief`. Retain each returned campaign ID and the shared conversation ID, and show all three review links plus the canvas link. This does not schedule July 15 delivery; ask for a year/timezone only when an actual schedule requires them.

**“Make the second email shorter and show me.”** Use the second email's saved campaign ID, read `get_campaign`, and call `update_campaign_draft` with `expected_updated_at` from that read. Preserve its role and agreed facts. Show its returned review link; reread after a conflict. A sent or locked campaign requires a new draft.

**“Create something similar to our welcome email.”** Locate the selected campaign with paginated `list_campaigns` and read its HTML. Use its design as reference while checking that the current offer and product facts still apply. Save the remix as a new draft; preserve the source email.

**“Create a follow-up to my last email.”** Resolve which prior campaign the user means from the existing conversation or recent campaign list. Keep the established goal and known facts, then save a follow-up draft. Use the same conversation only for that user's continued work. Do not infer a reply, purchase or open that was not recorded.

**“Save this style for next time.”** If the user means a lasting verbal design preference, read fresh context and save the accepted description with `remember_brand_fact`, category Design and its current brand revision. Confirm the saved memory. Do not report that the email was favorited or that a screenshot was stored: there is no hosted email-favorite tool. A request for an exact saved design reference needs the app's actual reference workflow.

## Import, files and app setup

**“Convert this HTML email into SendWhale.”** Use the supplied HTML in `sendwhale_save_email_drafts` with the provided subject and name. For several files, save them together. Extract HTML from an authorized `.eml` file first if needed. Show the saved results and disclose sanitization; do not promise lossless conversion or call a nonexistent import endpoint.

**“Export this email to HTML.”** Read the selected campaign and write its returned HTML to the requested local file. This is a file export, not mail delivery. For PNG, PDF, Klaviyo, Mailchimp or HubSpot, inspect an actual available native/provider integration; do not invent a hosted export tool or upload to a third party without authorization for that destination.

**“Add these contacts to our list.”** Read the known audience descriptions, then use the native subscriber-import flow for the authorized list. Preserve each contact's consent and suppression state. `create_audience` only creates an empty group; it is not a CSV import. If the app flow is unavailable, report the missing import capability without converting it into an unsupported bulk tool call.

**“Set up SendWhale to handle email in this app.”** Use `sendwhale-setup`: audit real product triggers, reuse or save matching drafts, and wire the backend through the actual transactional contract. Escape variables explicitly and use event-based idempotency keys. A saved campaign ID does not expand into a transactional template automatically.

**“Set up a sending domain.”** Use the native sending settings and verify the real sender/DNS state before calling it ready. Do not fabricate an instantly ready managed subdomain, domain-purchase tool or CLI command. Domain setup is unnecessary for drafting.

**“Set up a webhook to track email events.”** Inspect the app's real backend event handling and available provider contract. The hosted MCP exposes no webhook-creation operation. Do not claim an endpoint, event subscription or delivery signature was configured without a verified result.

## Review, delivery and results

**“Send that email to our VIPs.”** Match the approved audience by `list_audiences` when needed; do not assume a tag or segment tool exists. Use the selected campaign's returned native review link for audience, count, sender, subject, preview and real footer review. Delivery approval stays in SendWhale; the agent has not sent anything.

**“Create a launch email, check it, then send it to our launch list.”** Save and show the draft first. Check the authored facts, images, links and native preview/preflight before native sending review. Show unresolved issues plainly. There are no hosted validate-all or send-test tools, and browser checks do not establish real email-client rendering or inbox placement.

**“Send my investor update.”** Use only the supplied business figures and period; do not invent revenue or growth. Save an editable update, select the known audience for native review and show the exact subject and review link. The drafting connection cannot perform the final send.

**“Schedule a newsletter for next Tuesday.”** Resolve the intended date, local time and timezone when needed, then prepare native campaign review. Do not set a fictional scheduling argument on the draft-save tool. Use a fresh campaign read to confirm `scheduled_at` only after native scheduling has actually succeeded.

**“Track the status of my email.”** Read the selected campaign's real lifecycle status with `get_campaign`. Open its native report for delivery, opens and likely-human clicks. Saving a draft is synchronous; there is no generation job or batch-status endpoint to poll. Queued, accepted, delivered and inbox placement are different outcomes.

**“Did it land in spam?”** Delivery events cannot reveal recipients' inbox labels. Verify only a mailbox the user has authorized or an actually configured inbox-placement test. A spam/content check, open or SMTP acceptance is not proof of inbox placement.

**“Use engagement to improve it.”** Use the selected campaign's native Analytics, click map and audience insights. Improve with Swell prepares a new draft brief grounded in filtered evidence. Sparse evidence supports a hypothesis, not a guaranteed winner. It preserves the sent campaign and does not authorize another send. The hosted MCP does not currently expose that Swell-only tool.
