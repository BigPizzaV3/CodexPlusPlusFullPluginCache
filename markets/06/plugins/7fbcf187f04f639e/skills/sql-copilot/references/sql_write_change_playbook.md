# SQL Write and Change Playbook

## Purpose

Use this file for INSERT, UPDATE, DELETE, MERGE, TRUNCATE, DDL, permissions, and schema changes.

The goal is to make the intended change visible, scoped, reviewable, and recoverable.

# 1. Preview first

For UPDATE/DELETE/MERGE, create a read-only preview using the same target scope and join predicates.

Example:

```sql
SELECT t.*
FROM target_table AS t
JOIN source_table AS s
  ON t.business_key = s.business_key
WHERE <same predicate>;
```

Validate:
- affected rows;
- distinct target keys;
- duplicate source matches;
- unexpected null keys;
- scope/date range.

# 2. UPDATE

Before updating:
- confirm predicate selectivity;
- confirm join cannot update one target from ambiguous source rows;
- preview old/new values when possible.

# 3. DELETE

Before deleting:
- preview exact rows;
- count them;
- confirm backup/restore or reproducibility;
- consider foreign-key/downstream impact.

Avoid broad deletes driven by an unverified variable/pattern.

# 4. MERGE

Before MERGE:
- confirm target key;
- deduplicate source if needed;
- define update/delete/insert semantics;
- validate source uniqueness;
- define ordering/version rules.

Ambiguous multi-match source rows are a correctness risk even when syntax is valid.

# 5. TRUNCATE / DROP

Treat as high risk.

Before use:
- verify object/environment;
- confirm scope;
- confirm backup/restore/rebuild path;
- verify transaction behavior for the dialect.

# 6. DDL

For ALTER/CREATE/DROP:
- identify locking/rewrite implications;
- compatibility with running applications;
- migration ordering;
- rollback or forward-fix path.

DDL transaction semantics differ by platform.

# 7. Transactions

Use transactions when they provide real rollback protection for the dialect and operation.

Do not assume:
- DDL is transactional everywhere;
- all warehouse operations can be rolled back;
- long transactions are harmless.

State platform-specific behavior when relevant.

# 8. Schema migrations

Prefer compatibility-aware sequencing:

1. additive schema;
2. compatible application/query update;
3. backfill;
4. validation;
5. switch consumers;
6. remove old schema later.

Avoid breaking producer and consumer in one irreversible step when staged migration is possible.

# 9. Permissions

For GRANT/REVOKE:
- identify principal;
- object/scope;
- exact privilege;
- inheritance/role implications;
- least privilege.

Do not use overly broad grants as a troubleshooting shortcut.

# 10. Final execution block

For high-risk changes, separate:

## Preview / validation

from

## Run only after validating the preview

Never mix both in one copy-paste block if accidental execution is plausible.
