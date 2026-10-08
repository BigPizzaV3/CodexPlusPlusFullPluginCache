---
name: supabase-auth-and-sessions
description: Review Supabase Auth identity, JWT claims, sessions, recovery, OAuth, and account lifecycle security.
---

# Supabase Auth and Sessions

Check SSR client usage, `getUser` versus untrusted session assumptions, cookie flags, token expiry and refresh, logout, recovery, OAuth redirect allowlists, email verification, MFA, anonymous users, user deletion, stale JWT claims, and session revocation. Never use user-editable metadata for authorization. For strict revocation requirements, validate the session lifecycle on sensitive operations.
