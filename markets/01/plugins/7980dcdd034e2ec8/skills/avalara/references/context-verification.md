# Context verification

Four facts must be established before reading, and re-confirmed before any write:
**environment, account, company, role**. Getting one wrong is how a sandbox test lands in
production or a correction lands on the wrong subsidiary.

## 1. Environment

Sandbox and production are entirely separate accounts with separate credentials, account
numbers, and license keys. Settings do not sync between them. A familiar-looking screen
is not evidence of which one you are in.

For the AvaTax admin console, these documented hosts identify the environment:

| Host | Environment |
|---|---|
| `admin.avalara.com` | Production, live data |
| `sandbox.admin.avalara.com` | Sandbox, development |

Read the current address and the signed-in context. These mappings do not classify every
Avalara product or shared identity redirect. On another official host, verify the product
and environment from the final page and user context; ask if unresolved. Never construct
an environment URL by editing a host or infer it from branding alone.

If the user's stated environment disagrees with the host, stop and ask. Do not proceed on
whichever is more convenient.

State the environment in your first substantive response and keep it fixed. If a later
request only makes sense in the other environment, say so and let the user decide.

## 2. Account

One AvaTax account can contain many companies and many users, and a user may have access
to more than one account.

To read the account ID: sign in and select the profile picture at the top right. The ID is
displayed there.

Sandbox and production have different account IDs for the same organization, so an
account ID alone does not identify the environment unless the user has told you the
mapping. The host does.

## 3. Company, including hierarchies

A company represents a legal business entity. Companies can be arranged as a parent with
child or subsidiary companies, and that relationship changes behavior in ways that are
easy to miss:

- **Advanced company settings can be inherited.** When a child inherits from its parent,
  those fields are read-only on the child and a message points to the parent. Turning
  inheritance off makes them editable again. That detaches the company from centrally
  managed settings and is a consequential change, not a convenience toggle.
- **If the user lacks access to the parent, the parent's name and link are hidden** and
  a message tells them to contact their administrator. Read that message rather than
  concluding the setting does not exist.
- **Exemptions do not inherit.** Even when a child company uses the parent's tax
  settings, exemptions are managed per company and must be added to each one. Never
  assume a parent-level exemption covers a subsidiary.
- **A parent selection does not authorize its children.** Use the named entity alone
  unless the request includes subsidiaries. Ask only when that scope is unclear, especially
  for reports, imports, and nexus changes.
- **Data missing from one company often lives in a sibling.** That is a reason to ask,
  not a reason to browse other companies.
- **A company has a status, and it is not cosmetic.** Active calculates tax and files.
  Test calculates tax but cannot file. Inactive does neither. "Deactivate the old
  subsidiary" and "tidy up the company list" are ordinary-sounding requests that stop tax
  and filing for a legal entity, so treat a status change as consequential and read the
  current status before reporting on a company that looks empty.

Record the exact company name and code you are operating on and restate it in every
approval request. Confirm what the company selector currently shows rather than what you
selected earlier; selectors can reset on navigation.

## 4. Role and permissions

AvaTax account access is visible under **Accounts > Users and admins** where permitted.
Common account-level roles include the following; verify the actual role and company
scope rather than treating this as an exhaustive permission model.

| Role | What it can do |
|---|---|
| Account Administrator (Admin) | Full access to all subscribed features and settings: create and modify users, add companies, manage payments and account information |
| Account Viewer | View-only across subscribed features; can run reports |
| No access | Nothing |

What this means in practice:

- **Viewers can look but not change.** Transactions are view-only for a Viewer. Importing
  transactions is not available to them at all. Configuration areas are view-only: where you report
  tax, what you sell, exempt customers, child companies, custom rules, and advanced
  settings.
- **Voiding requires account administrator permission.** So does importing, adding users,
  generating license keys, and setting up returns.
- **A missing control may mean a Viewer role, not a missing feature.** Before concluding
  something cannot be done, consider that the account may lack the permission.

Other Avalara products and subscriptions can use different roles and company-level
permissions. Do not carry a capability assumption across products.

When a role blocks the task, name the blocked action and the access it would need. Do not
attempt it through a different company, product, portal, or environment.

## When something is ambiguous

Ask one specific question naming the candidates you actually saw. "I see two companies
with similar names, X and Y. Which one?" is useful. "Which company did you mean?" is
not.

While waiting, do not read further, pre-stage a change, or open other companies to narrow
it down yourself.

## Re-verification before writes

Context decays over a session. Before any save, void, status change, import, approval, or
submission, re-read from the current page: host, account, company, target record
identifier, and the values being changed. Confirm they match the authorized action. A
material change to target, values, scope, or consequence requires renewed confirmation.
