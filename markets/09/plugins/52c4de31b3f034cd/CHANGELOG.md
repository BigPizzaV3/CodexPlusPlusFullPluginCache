# Changelog

## 1.0.0

- Add portable OpenAI plugin packaging for InvoiceVista Invoice Maker.
- Add the read-only business sidebar and aggregate billing navigation.

## 0.1.2

- `billing-operations` 1.0.1: the tool table now says when to use each tool
  in the words users ask with, matching the connector's rewritten tool
  descriptions. It documents that payment totals include every recorded
  payment whatever its status, that the overdue count covers invoices marked
  `OVERDUE` (a pending invoice past due appears only in the age buckets), and
  that a product's `tax` is null when none was set.
- Same eight read-only tools and the same customer and financial-data
  boundary.

## 0.1.1

- Source `billing-operations` from the canonical `@invoicevista/skills`
  package instead of maintaining a second copy here, and add the byte-identity
  guard that keeps them from drifting.
- Declare the agentskills.io `license`, `compatibility` and `metadata`
  frontmatter on the skill, so the same file is valid both as a plugin skill
  and as an entry in `npx skills add invoicevista/skills`.

## 0.1.0

- Add the hosted InvoiceVista OAuth connector.
- Add the aggregate-first `billing-operations` skill.
- Document customer/financial-data exclusions, source caps, signed amounts,
  read-only behavior and safe fallbacks.
