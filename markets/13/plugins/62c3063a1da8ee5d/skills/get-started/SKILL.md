---
name: get-started
description: Sign in to Openline, then send or read mail, place calls, and send or read SMS only when the operator asks.
---

# Openline

Openline is Scalar Field’s product. An agent signs the operator in, then sends or reads mail, places and reviews calls, or sends and reads SMS, only when the operator asks.

Product page: https://staging.openline.scalarfield.io/site/
MCP server: https://staging.openline.scalarfield.io/mcp
This file: https://staging.openline.scalarfield.io/skill

## Rules

- Sign-in is OAuth. Never ask for a 6-digit code or a token in chat. Never pass a token to a tool.
- Never fetch `/v1/auth/otp` or `/v1/auth/verify`. Never use `request_otp` or `verify_otp`. Never call `/v1/mail`.
- When `signed_in` is true, an inbox and a phone number already exist. Do not ask the operator to connect Gmail or a carrier.
- `logout` signs this client out.
- Read a tool’s schema instead of guessing arguments.
- If a tool result includes `tell_the_user`, explain that to the operator in your own words.
- On `do_not_email`, `do_not_text`, `email_invalid`, `rate_limited`, `quiet_hours`, or `insufficient_credits`, stop and tell the operator. Do not work around consent, caps, or a zero balance.

## Sign in

1. If you have no Openline tools, the operator adds `https://staging.openline.scalarfield.io/mcp`, then you retry.
2. Call `connect` (or `auth_status`).
3. If the host shows Connect / Authorize, the operator signs in on Openline’s page. After the inbox code, the page says the sign-in email is already verified and can ask for a phone number. The phone number is optional; Skip continues.
4. Call `connect` again.
5. Continue only when `signed_in` is true.

## When the operator asks

Mail. `send_email` (`to`, `subject`, `body`). Then `list_emails`, then `get_email` (`message_id`). Confirm what you sent and from which address.

Calls. `call_phone` (`to`, `goal`) and pass the details the operator gives you. Review with `list_calls`, then `get_call`.

SMS. `send_sms` (`to`, `body`). History is `list_messages` and `get_message`.

Other tools cover contacts, scheduled calls, inbound policy, and credits. Use one when the operator asks.
