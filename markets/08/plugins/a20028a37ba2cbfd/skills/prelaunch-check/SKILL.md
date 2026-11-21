---
name: prelaunch-check
description: Test what breaks when two users act at once on real PostgreSQL (last seat, double booking, counters, invites, credits, stock) and review Supabase migrations for row-access and grant gaps. Use the connected VibeRaven tools. Not for general SQL, unrelated stacks, or proof of live database security.
---

# VibeRaven

**Two users at once.** When the user asks whether a rule holds under concurrent use, call `race_two_users`:
- with the migration SQL (or a public GitHub repo at a resolved commit);
- with 2–3 actors and their SQL steps;
- with the rule as a SQL assertion.

Show the shortest broken order, the final rows and the fix. After a fix, run the test again on the fixed SQL and report the result. Say when a test was capped.

**Migration review.** For RLS, policy and grant gaps, call `check_supabase_migrations` with the SQL, or `check_github_repo` for a public repository.

**Errors and setup.** Use `search_guides`, `provider_playbook`, `recent_provider_changes` and `explain_finding`.

**Limits.** Tests run on an offline PostgreSQL instance built from the supplied SQL, not the live database. Public repositories only. A clean result is not a security audit. Do not ask for credentials or .env contents.

**In a local repo with a terminal:** `npx -y viberaven race --example`, then `npx -y viberaven race` and `npx -y viberaven check`.
