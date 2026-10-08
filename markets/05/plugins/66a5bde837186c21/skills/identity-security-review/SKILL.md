---
name: identity-security-review
description: "Review user-supplied identity architecture, federation design and control documentation for defensive security gaps. Use for assurance and remediation planning; not for tenant discovery, account enumeration, login testing or credential activity."
---

# Identity security review

Review identity architecture from documentation and sanitised configuration summaries.

## Boundaries

- Do not discover tenants, enumerate users, generate login candidates, test authentication or request credentials.
- Do not infer a person's account status, employment or privileges from public information.
- Keep recommendations provider-neutral unless the user supplies the relevant platform context.

## Method

1. Map documented identity providers, federation boundaries, trust relationships, privileged roles and recovery paths.
2. Review MFA strength, conditional access, session controls, legacy authentication, service identities, joiner-mover-leaver controls and emergency access.
3. Identify trust concentrations, weak ownership, monitoring gaps and controls that depend on undocumented assumptions.
4. Distinguish design evidence from implemented-control evidence and operational-effectiveness evidence.
5. Recommend owner-performed verification using approved administrative logs and configuration exports.
6. Produce an assurance table with control objective, supplied evidence, gap, risk, confidence and remediation.
