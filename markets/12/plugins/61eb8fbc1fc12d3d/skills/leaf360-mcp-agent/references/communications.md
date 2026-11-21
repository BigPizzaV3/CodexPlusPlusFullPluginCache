# Communications

Outbound communication has compliance and reputation risk. Draft first, send only through Leaf360 controls.

## Drafting

Use `leaf360_message_draft` when the user asks to write an email, SMS, or call script. Include:

- Channel
- Target record type and ID
- Purpose
- Subject for email
- Body or script

Drafts do not send anything.

## Sending Email

Use `leaf360_email_send` only when the user wants dispatch and has approved exact content. The tool requires a server-signed approval token for the exact email, recipient, record, user, and company.

If approval is missing or invalid, the correct result is `approval_required`; explain that Leaf360 needs approval before dispatch.

## Sending SMS

Use `leaf360_sms_send` only when the user wants dispatch and has approved exact content. Respect SMS consent, quiet hours, opt-out behavior, and the existing Leaf360 communication layer.

Keep texts short, clear, and action-oriented. Avoid sensitive loan details unless clearly appropriate and consented.

## Calls

Use `leaf360_call_start` only when the user wants to start a call and approval is present. For call preparation, use `leaf360_message_draft` to create a call script instead.

## Recipient Overrides

Only use `toEmail` or `toPhone` when the value already belongs to the visible CRM record. Never use arbitrary contact details supplied in chat as overrides.

## Good Communication Judgment

- Mention the reason for outreach.
- Avoid sounding automated.
- Do not overpromise underwriting, rates, approval, or closing dates.
- For partners, focus on relationship value and next steps.
- For borrowers, focus on clarity, confidence, and what they need to do next.
