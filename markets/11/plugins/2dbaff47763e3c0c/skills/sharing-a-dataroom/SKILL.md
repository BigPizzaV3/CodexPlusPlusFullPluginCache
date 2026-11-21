---
name: sharing-a-dataroom
description: Use when giving someone access to a data room or to particular documents in it, changing or removing access they already have, or explaining what a role or member can currently see. Covers which tools to combine for each kind of grant, and how roles, overrides, hidden folders and links interact.
---

# Sharing a data room

Grant the narrowest access that satisfies the request. The tools' own
descriptions cover each call; this covers how they combine.

## CHOOSING THE GRANT

- Specific files -> a document share; the recipient sees only those files.
  - One file: `share_document`.
  - Several files, one link: `create_role(hidden=True)` -> one
    `set_document_override` per file -> `create_share_link(role_id=...,
    email=...)`. One link, not several. Leave `keep_watermark` at its
    default on each override; it matches `share_document`'s.
- The whole room -> `invite_member` (a participant) or `create_share_link`
  (an email invite carrying a role).
- A role with nobody to send it to -> `create_role`, plus an override per
  file if it should reach only some. Leave `hidden` off: it belongs in the
  role picker. `hidden=True` is only for the throwaway role behind a
  document share.
- Changing what someone has -> `assign_role`, or a new role shaped with
  `create_role` + overrides.

## BEFORE CREATING ANYTHING

- `list_members` first. If they already have access, say so rather than
  creating a duplicate; if they are a member, ask before changing their role.
- If they already hold a document share (`list_document_shares`), add the new
  file to that share's role with `set_document_override`. It appears on the
  link they already have.

## HOW THE PIECES INTERACT

- A document share works because `create_role` starts with `doc_view` off
  and each override then opens one file. Turning `doc_view` on to share a
  few files hands over the whole room, including documents added later.
- Claiming several document links MERGES their grants, and a full-access
  role always beats a hidden one. A smaller link cannot narrow access - to
  reduce it, change the role.
- A role grants nothing until a link or a member points at it.
- To withhold one document from a role that sees everything, set an override
  with `can_view=False`. Removing an override is a different act: it
  restores the role's blanket rule for that file.

## REPORTING WHAT SOMEONE CAN SEE

Read it from the role's flags, its overrides (`get_role`) and its hidden
folders together. Any one alone gives the wrong answer: an override changes
the blanket rule per file, and a hidden folder beats both.

## DON'T

- Don't send a second, smaller link to reduce access.
- Sharing emails the recipient by default. Say so when reporting back; pass
  `notify=False` only when asked to share quietly.
