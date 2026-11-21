---
name: setup-custom-domain-email
description: >-
  Set up or resume initial custom-domain email with MailLogic: connect a domain,
  configure receiving/email forwarding, and optionally enable explicitly requested
  sending. Use for requests such as "set up my custom domain email", "connect
  example.com to MailLogic", "set up MailLogic for my domain", or "set up email
  forwarding for my domain". Excludes general troubleshooting, delivery-log analysis,
  ongoing address or catch-all administration, replies, arbitrary email sending,
  and billing management.
---

# Set up custom-domain email

Use existing MailLogic MCP tools to complete only missing setup work. This is a resumable workflow, not a fixed sequence. Preserve tool confirmation requirements, host approvals, backend authorization, and applicable email-testing restrictions. Existing authorization need not be requested again; permission to configure email does not imply permission to send a diagnostic.

## Establish intent and inspect

- Start/resume with `inspect_mail_setup` for the domain established in the conversation. For a fresh request without a domain, ask for the intended domain first: do not silently select the sole visible domain. Reuse an established domain on continuation.
- Determine the intended address, forwarding destination, and receiving/sending goal from the request and reliable context. Ask only for missing choices, when needed. Do not infer a new destination from another address, catch-all mapping, logs, or account identity. Display name is optional; omit it unless requested.
- Generic email setup means receiving/forwarding. Paid entitlement alone never implies sending intent. Enter the sending branch only for an explicit or clear sending request; ask once if genuine ambiguity affects the next mutation.
- Inspection is cached. `complete` describes the inspection, not completed setup. Visible selection confirms existence; `not_visible` does not prove absence. Unknown/null DNS observations are not false, and denied/unavailable sections are not empty. Follow address pagination only as needed; an incomplete page cannot establish that an address is absent.
- Use returned readiness, account capacity, SMTP entitlement/availability, address state, and DNS requirements. Preserve catch-all state without modifying it. Reinspect only for changed state, uncertainty, or resumption—not after every action.

## Choose the next unmet step

| State | Action |
|---|---|
| Domain already visible, including pending/revoked ownership | Reuse; do not recreate. |
| Requested domain not visible | Explain the visibility limit; use `create_domain` within the authorized setup. Backend restrictions/conflicts remain authoritative; new creation requires unrestricted credentials. |
| DNS already ready for the requested capability | Skip that DNS work. |
| DNS unchecked or changed externally | Deliberately use `check_domain_dns` when needed before prescribing redundant changes. It persists observations and can change ownership/routing; it is not read-only. |
| DNS incomplete | Configure unmet requirements using the automatic or manual route below. |
| Intended active address already has the intended destination | Reuse it. Preserve existing SMTP state even for a receiving-only request. |
| No intended address exists and ownership is verified | Use `create_email_account` with the exact address and forwarding destination. New receiving-only addresses use `smtp_enabled=false`. MX propagation need not finish before creation. |
| Existing destination conflicts, address is inactive, or state cannot be reconciled safely | Report the blocker; do not overwrite, delete/recreate, or change unrelated configuration. |
| Address capacity exhausted or permission denied | Report the blocker; do not delete resources, upgrade, or bypass restrictions. |

## Complete DNS with a human handoff

Use MailLogic's returned records and readiness rather than reconstructing DNS policy. Receiving needs ownership and MX readiness. Sending additionally needs the returned sending requirements, including valid DMARC. Free/no-entitlement users skip sending-only SPF/DKIM/DMARC work; paid receiving-only users do too. A full DNS mode is not sending intent.

When automatic setup is available and authorized, call `begin_automatic_dns_setup` with explicit `forwarding`, `sending`, and `dmarc` booleans matching the proposed work. Verification is always included; forwarding selects MX; sending selects SPF/DKIM together; DMARC requires sending. Skip satisfied groups where possible. Explain any included changes to existing routing. Do not silently omit unmet DMARC from a sending-completion claim.

Present the returned private authorization URL unchanged. Do not fetch/follow it, automate consent, or share it elsewhere. The human opens, authenticates, and approves it. Preparation/approval does not establish DNS readiness. After the user returns, use `check_domain_dns`; do not automatically generate another authorization URL. There is no consent-session polling API.

If automatic setup is unavailable/unsupported or manual setup is preferred, present the returned record type, name/host, value, and priority. Preserve SPF `merge` and DMARC `preserve_or_create` semantics; do not blindly replace existing records. Explain MX routing consequences before changes. Unknown provider hints are advisory: a deliberate automatic attempt can validate fresh authority if desired, but do not loop on provider failures or use direct provider APIs. After external edits, deliberately check DNS. Preserve partial progress while propagation continues.

## Optional sending setup

Only for requested sending: check entitlement and distinguish configuration readiness from current sending availability. If not entitled, explain the limitation and complete authorized receiving work; do not attempt billing/upgrade actions. Suspension, billing operations, or exhausted credits can block sending even when configured. An availability-only blocker need not prevent authorized configuration that the backend permits; never bypass a mutation denial.

For a new address on an entitled account, `create_email_account` with `smtp_enabled=true` can configure SMTP and issue one private setup email, avoiding a second mutation. For an existing address with SMTP disabled, use `enable_smtp`. If already enabled, reuse it; never call creation with default SMTP false as a way to resume.

Have the user complete the password privately through the emailed setup link. Never request a password or private setup link in chat. Do not automatically call `request_password_setup` after creation/enablement or when submission is uncertain. Use it only for a deliberate replacement request, explaining that previous usable links are replaced and respecting cooldowns. Pending state does not prove email delivery; absence of pending state does not prove password completion.

## Optional forwarding diagnostic

Use `create_forwarding_test` only when the user wants verification/diagnosis, the exact route is authorized under applicable testing restrictions, and the address is eligible. Inspection of a route is not permission to send to it. Do not mine production data for test recipients or use an arbitrary email-send tool.

Before calling, retain the exact address, locale, and non-secret idempotency key in conversational state; then retain the returned test ID and replay expiry. After uncertainty, inspect setup as needed and deliberately recover with the identical address/locale/key within replay retention—never a fresh key. If the ID is known, use `get_forwarding_test`. Respect `poll_after_ms`, use bounded checks, and return pending rather than polling indefinitely. Lost key/ID is not permission to start another diagnostic.

Acceptance/202 is only durable request acceptance. Queued/submitting/checking are pending. Confirmed means observed destination SMTP acceptance, not inbox placement, lasting forwarding health, or SMTP sending readiness. Preserve failure codes; failed/expired monitoring does not prove nondelivery. A 404 can reflect visibility or retention, not absence.

## Resume and report

Keep a concise conversational checkpoint: domain, intended address/destination, requested capabilities, completed milestones, outstanding human action, and any diagnostic key/ID/expiry. Do not store passwords or private links in a separate state file.

For unknown mutation outcomes, inspect before a deliberate retry and follow the tool's retry guidance. A matching observation does not attribute the prior write or prove its email was sent. For partial/persisted failures, preserve the resource and synchronization warnings; follow returned recovery actions rather than recreating it. Honor retry timing. Scope/capacity denials are blockers, not invitations to bypass controls. Do not automatically resend uncertain password emails or repeat authorization flows.

Report these milestones separately, only as supported:

- **Domain/ownership:** identity exists; ownership verified or still pending/revoked.
- **Receiving DNS:** `forwarding_ready=true` at the reported observation time; not guaranteed delivery.
- **Address configured:** exact intended active address and destination saved; disclose unresolved synchronization issues.
- **Receiving setup complete:** ownership, receiving DNS, and intended address ready, without known unresolved setup/synchronization blockers. A forwarding test is optional.
- **Forwarding test:** not requested, pending, confirmed destination SMTP acceptance, or ended without confirmation.
- **Sending DNS/domain readiness:** `smtp_ready=true`; not password setup or SMTP authentication proof.
- **Address SMTP:** enabled or still pending configuration.
- **Private password handoff:** awaiting the human, or completed according to their report; never claim API-verified password completion/authentication.
- **Current sending availability:** account sending state, including entitlement, suspension, billing, or credit blockers; configuration alone is insufficient.

Stop at the next required human action or blocker, with the specific resume step. Do not expand into general troubleshooting, logs, catch-all changes, address administration/deletion, replies, arbitrary sending, or billing management.
