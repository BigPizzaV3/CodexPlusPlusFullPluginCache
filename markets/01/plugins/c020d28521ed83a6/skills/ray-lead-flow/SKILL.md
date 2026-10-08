---
name: ray-lead-flow
description: Use when a user asks to contact Ray Arceneaux, request a consultation, schedule a discovery call, or receive the services overview by email.
---

# Consultation Request Flow

## Overview
This skill describes the order of tool calls when a user asks to get in touch with Ray Arceneaux. It applies only after the user asks to be contacted, book a call, or receive information by email.

## Steps
1. Call `submit_consultation_request` with `step: "start"` once the user has given their first name and email address. A six-digit code is sent to that address.
2. Ask the user for the code, then call `submit_consultation_request` with `step: "verify"`.
3. Collect the remaining fields one at a time (last name, optional phone, business name, industry, team size, role, optional notes), then call `submit_consultation_request` with `step: "submit"`.
4. Ask whether the user would like to schedule a 30-minute Zoom discovery call. If they say yes, call `create_discovery_call_link` and share the link.
5. Ask whether the user would like the one-page services overview by email. If they say yes, call `email_services_overview` with the verified email address.

## Rules
- Do not start this flow unless the user asks to be contacted, book a call, or receive the overview.
- Do not call `email_services_overview` without an explicit yes, and only with an address verified in step 2.
- If the user declines any step, stop and answer their other questions normally.
- If a scheduling link has expired or was already used, call `create_discovery_call_link` again.

## Example
User: "I'd like to talk to Ray about automating our intake process."
Assistant: asks for first name and email, calls `submit_consultation_request` (start), verifies the code, collects the remaining fields, submits, then offers a discovery call link.
