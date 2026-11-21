# Single Sign-On

Verified 2026-09-10.

HR Omni supports Login with Google and Login with Microsoft for organisational accounts, with paid verified-domain setup for company domains.

- Personal Gmail Google sign-in is available without paid company-domain setup.
- Paid domain SSO supports Google Workspace domains.
- Microsoft support is for Microsoft Entra ID / Microsoft 365 organisational accounts.
- Do not label the exact protocol as SAML or OIDC unless current official documentation verifies it.

A company proves domain ownership using either a file under `.well-known` or a DNS TXT record. On first successful verified-domain login, HR Omni can create the global user and associated company-user record and grant company access without invitation acceptance.

It does not automatically create employment, department, manager, schedule, product enrolment or elevated access.

SSO is optional and email/password remains available. There is no company-wide SSO enforcement, SCIM, directory sync, automatic role assignment or HR Omni-managed provider MFA/conditional access.

Prices are time-sensitive and must be checked live before quoting.
