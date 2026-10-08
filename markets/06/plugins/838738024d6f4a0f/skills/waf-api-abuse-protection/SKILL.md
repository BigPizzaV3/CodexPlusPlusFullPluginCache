---
name: waf-api-abuse-protection
description: Review Cloudflare WAF, API Shield, bot controls, endpoint exposure, and abuse/rate-limit defenses.
---

# WAF, API, and Abuse Protection

Inventory public endpoints and classify by authentication, sensitivity, and business impact. Review managed/custom WAF rules, exposed credential detection if entitled, API inventory/schema validation, JWT validation, mTLS, rate limiting, bot controls, GraphQL protections, and relevant logs. Map controls to actual routes and methods; a WAF rule does not repair broken object authorization or unsafe application logic.

Check plan/entitlement availability before recommending a feature. Tune limits per endpoint and identity/session where possible; broad IP-only limits can affect shared NAT users and may not stop distributed abuse. Cloudflare rate limiting can have detection/enforcement delay, so do not promise exact origin request ceilings. Recommend log/challenge observation and false-positive review before blocking. Do not create, enable, or reorder rules without explicit approval, validated expressions, change window, and rollback steps.
