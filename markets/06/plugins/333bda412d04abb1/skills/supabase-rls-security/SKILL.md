---
name: supabase-rls-security
description: Perform deep Supabase Row Level Security, Data API exposure, policy, view, function, and role analysis.
---

# Supabase RLS Security

Use for any Supabase database, Auth, Data API, Storage, view, function, or user-data review.

## Mandatory checks

- Enable RLS on every table in exposed schemas, including `public` by default.
- Confirm Data API exposure and explicit grants separately from row policies.
- Check every table's `SELECT`, `INSERT`, `UPDATE`, and `DELETE` model.
- For `UPDATE`, verify both `USING` and `WITH CHECK`; also verify the required `SELECT` policy.
- Reject `TO authenticated` without an ownership, membership, tenant, or capability predicate.
- Prefer `TO authenticated` or `TO anon` clauses; flag deprecated `auth.role()` checks.
- Never use user-editable `raw_user_meta_data` for authorization; use trusted server-controlled app metadata or database membership tables.
- Review views for `security_invoker = true` on supported Postgres versions or restricted access in an unexposed schema.
- Review `SECURITY DEFINER` functions for schema placement, explicit authorization, fixed search path, minimal grants, and default `PUBLIC` execute privileges.
- Check storage policies, including `SELECT`, `INSERT`, and `UPDATE` for upsert behavior.
- Review service-role usage and ensure it never reaches public clients.

## Findings format

Report table/schema, exposed role, operation, policy, predicate, bypass path, impact, and a safe SQL or application-level remediation. Never invent a policy without understanding the intended access model.
