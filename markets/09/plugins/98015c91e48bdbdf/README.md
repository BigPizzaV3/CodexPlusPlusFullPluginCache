# Recovr

Recovr connects an authorised staff account and studio to member data, analytics, conversations and follow-up tools.

Version: 1.4.2. The internal package identifier remains `recovr-retention` to preserve the existing package identity; the displayed name is **Recovr**.

## Included MCP guides

- [recovr-member-lookup](skills/recovr-member-lookup/SKILL.md): find members and interpret profiles, risk and history.
- [recovr-analytics](skills/recovr-analytics/SKILL.md): attendance, counts and structured analysis; explains the Builder boundary.
- [recovr-messaging](skills/recovr-messaging/SKILL.md): conversation lookup, drafts and explicitly approved sending.
- [recovr-follow-up](skills/recovr-follow-up/SKILL.md): flags, snoozes, assignment, contact preferences and notes.

The skills contain public usage instructions. Authentication happens through the host's connection flow. This package contains no login credentials and needs no embedded API key.

The MCP endpoint is configured in `mcp.json`. Builder creation/editing, bookings, payments/refunds and bulk sending are outside the current published tool surface.

Publisher: Recovr Pty Ltd. [Website](https://recovr.com) · [Support](https://support.recovr.com) · [Privacy](https://retention.recovr.com/privacy) · [Terms](https://retention.recovr.com/terms).

Proprietary. See [LICENSE](LICENSE).
