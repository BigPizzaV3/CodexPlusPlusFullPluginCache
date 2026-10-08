---
name: flipbook-access-control
description: Configure access to Heyzine flipbooks and bookshelves. Use when users ask to enable or disable protection, set a shared password, grant individual access, revoke credentials, or audit available access data.
---

# Access control for flipbooks and bookshelves

Protection has a publication mode and, for individual access, credential
entries.

## Inputs and boundaries

- Resolve the target from an id, public URL, short id, or an unambiguous title
  returned by `heyzine_list_flipbooks` or `heyzine_list_bookshelves`.
- Set `type` to `bookshelf` for a bookshelf and `flipbook` for a flipbook.
- If a title is ambiguous, show the candidates and ask which one. Never guess
  the target, protection mode, password, email address, or current access list.
- No MCP tool lists current access entries. If asked who has access, explain
  that the current list must be checked in the Heyzine access settings.

## Set the protection mode

Call `heyzine_access_setup` with `id`, `type`, and one of:

| Mode | Behavior |
| --- | --- |
| `everyone` | One shared password; requires `password` |
| `users` | Only entries added to the access list can open it |
| `disabled` | Removes the access gate and makes the publication public |

Optional `text_user` and `text_password` relabel the fields on the login
screen. Send them only when the user supplies the labels.

Use `everyone` for one password shared by all visitors. Use `users` when access
must be managed per person or credential. Before switching to `disabled`,
state the exact title and explain that the publication will become public,
then obtain confirmation unless the user already confirmed that exact change.

Never invent a password. If one is required, ask for it or offer to generate
one; generate it only after the user accepts.

## Grant individual access

Call `heyzine_access_add` with `id`, `type`, `access_type`, and the required
credential:

| `access_type` | Required input | Visitor flow |
| --- | --- | --- |
| `user_pass` | `user` and `password` | Username and password |
| `google` | `user` email | Google sign-in |
| `pass_only` | `password` | Password without a username |
| `otp` | `password` | Predefined one-time password |
| `email_link` | `user` email | Sign-in link by email |
| `send_code` | `user` email | Generated code sent by email |
| `email_code` | `user` email | Code delivered by email |

`email_link`, `send_code`, and `email_code` require a plan with password email
support. If the server rejects the plan, report its message and stop. Do not
silently switch to another access type.

For `users` mode, configure the mode before adding entries. For a batch, add
one entry per call and report each failure without changing the requested
credential type.

## Revoke individual access

Call `heyzine_access_remove` with `id`, `type`, and either `user` or `password`
to identify the entry. Confirm the exact publication and entry when either is
ambiguous. Do not disable the entire protection mode as a substitute for a
failed removal.

## Handle credentials

Do not write passwords into files or artifacts unless the user explicitly asks
for a credential document. Repeat a supplied or generated shared password only
when the user needs it for distribution. Never claim that an earlier
conversation entry reflects the current server-side access list.

## Report the result

State the publication, resulting mode, and the entry added or removed. For a
shared password, explain what visitors must enter without exposing unrelated
credentials.
