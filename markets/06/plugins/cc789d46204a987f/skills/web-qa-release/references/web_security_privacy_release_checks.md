# Web Security and Privacy Release Checks

## Purpose

Use this file for pragmatic release-oriented security review.

Use current OWASP guidance when detailed verification is required.

# 1. Authentication

Check changes involving signup/login, password reset, MFA, sessions, account recovery, logout, and invalidation.

Verify failure paths as well as happy paths.

# 2. Authorization

Check:
- object/resource ownership;
- tenant boundaries;
- admin-only actions;
- server-side authorization;
- ID manipulation;
- role changes.

Hiding UI is not authorization.

# 3. Sessions/cookies

Review when relevant:
- Secure;
- HttpOnly;
- SameSite;
- lifetime/expiry;
- rotation;
- logout invalidation;
- cross-site flow requirements.

# 4. Input/output

Check for injection, XSS, unsafe HTML, SQL/command injection, path traversal, open redirect, SSRF, and unsafe deserialization.

Use framework-native safe APIs where available.

# 5. Uploads

Check type/size validation, storage location, content serving, executable content, filename/path handling, access control, and malware scanning when required.

# 6. Secrets

Check repository, frontend bundles, source maps, CI logs, environment files, error output, and browser storage.

Client-side secrets are not secrets.

# 7. Dependencies

If dependencies changed:
- inspect dependency diff;
- known vulnerabilities;
- unexpected transitive changes;
- package origin;
- lockfile.

Do not block solely on severity labels without context, but do not ignore critical known vulnerabilities.

# 8. Security headers

Depending on architecture, inspect CSP, HSTS, framing protections, content-type protections, referrer policy, and permissions policy.

Do not apply headers blindly if they break legitimate flows.

# 9. Privacy

Review personal data collected, purpose, retention, analytics/tracking, consent where applicable, deletion/export, logs, and third parties.

Minimize data collection.

# 10. Release classification

Use:
- **Block release** — confirmed material vulnerability/exposure.
- **Must verify** — security-critical behavior lacks sufficient evidence.
- **Follow-up** — hardening without material release risk.

Do not claim a release is “secure” based only on an automated scan.
