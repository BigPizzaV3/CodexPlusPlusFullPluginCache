---
name: monitoring-incident-response
description: Assess security observability and guide response to Cloudflare account, token, application, or data incidents.
---

# Monitoring and Incident Response

Review available security insights, audit events, Access events, WAF/API signals, Worker logs, deployment events, alerting, retention, and ownership. Check whether logs may contain authorization headers, cookies, tokens, presigned URLs, personal data, or request bodies. Do not reproduce sensitive values. Distinguish missing telemetry from absence of attack.

For suspected compromise, prioritize containment with the account owner: secure identity/email, revoke affected sessions, rotate/revoke exposed credentials, restrict access, preserve relevant logs, assess changes and data access, restore trusted deployments, and notify required stakeholders under applicable policy. Tailor sequence to avoid lockout and service destruction. Do not disable resources, delete evidence, or rotate credentials on the user's behalf without explicit action-specific approval. Include an incident timeline and unknowns where evidence allows.
