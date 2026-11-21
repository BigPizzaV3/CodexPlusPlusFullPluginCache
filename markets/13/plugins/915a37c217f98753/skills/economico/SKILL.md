---
name: economico
description: Keep an Economico business's books, record customer and vendor agreements, invoices, receipts and payments, and read financial reports.
---

# Economico in ChatGPT

Economico keeps one business's double-entry books as an evidenced, append-only history.
Connect an Economico account and business through OAuth before using its tools. Someone without
a business creates one on the free Solo plan while connecting.

1. Call `businesses` to find the business the user means and its approved permissions.
   Supply that business slug on each subsequent call.
2. Read `business_get` and inspect the relevant parties, contracts and records.
   Use the individual command tools' descriptions and input schemas to choose the operation.
   Reads are individual tools such as `parties_list`, `subjects_get` and `ledgers_list`;
   supply their advertised parameters without an `action` selector.
   Tool names use underscores: `parties_create` executes the `parties.create` command.
3. Record only facts supported by the user's evidence. Confirm missing amounts, dates,
   counterparties and accounting choices with the user. Money uses integer minor-unit strings
   and a named currency. Supply a UTC `effective_at` and a stable `idempotency_key`; retry the
   same operation with that same key after an uncertain response. Retrieve an existing receipt
   with `command_receipt` rather than recording the fact twice.
4. Read back the resulting records. Use the individually exposed report tools, such as
   `report_income_statement`, `report_balance_sheet` and `report_activity_claims`, to verify
   the accounting outcome. Each tool advertises its own parameters; do not send `action` or `kind`. Explain what was recorded
   and what remains unknown, linking any returned document or report URLs.

Recording a payment describes money that moved elsewhere. Distinguish recording financial
facts from instructions that trigger external actions; execute those only on the user's authority.
A `no_change` result is a successful domain no-op. `record_business_incorporation` records
an incorporation that already occurred; it does not register a company.
`record_payment_with_fee` records an existing payment and its processing fee.
`record_account_transfer` records a completed transfer between company accounts. Neither tool
initiates a payment or moves funds.

To add a coworker, the owner can call `members_invite` with their email and access (`reader`,
`bookkeeper` or `administrator`). Economico emails them a link; they sign in or create an account
with that address and accept it themselves, so tell the user nobody has access until then.
`member_invitations` lists pending invitations and `members_revoke_invitation` withdraws one.

When a feature is unavailable under the current entitlement, explain the restriction and offer
only the informational pricing URL returned by the tool. An already entitled account can use its
paid features here. Paid plan purchases are outside this plugin's interface.

## Agreements, invoices and bills

When a new invoice or bill lacks its amount, currency, service date or reference, ask for
those facts before recording it. An older agreement or bill does not establish a new one.

A priced service uses a right, a contract granting it, then evidenced phases of that same
obligation. Reuse matching existing records before creating any. Billing opens a receivable or
payable; delivery and recognition earn revenue or expense; payment is recorded separately.

For a fixed-price service, adapt this `activities_create` input to the evidenced amount,
currency and classification. This example is a USD 800 consulting service sold to a customer:

```json
{
  "definition": {
    "model": "priced-rights-v1",
    "name": "Consulting service",
    "terms": {
      "price": {"type": "integer", "unit": "USD", "default": "80000"},
      "currency": {"type": "text", "default": "USD"}
    },
    "facts": {},
    "ledgers": {
      "money": {"classification": "gaap", "unitKind": "currency", "unitCode": "USD", "decimals": 2, "accountTemplate": "gaap_startup"}
    },
    "price": {"treatment": "priced", "calculation": {"type": "fixed", "amount": "term:price"}, "currencyTerm": "currency"},
    "economics": {
      "kind": "service", "direction": "provide",
      "billing": {"timing": "arrears"}, "recognition": {"timing": "delivery"},
      "classification": {"monetaryLedger": "money", "revenueCategory": "consulting"}
    }
  }
}
```

For a purchased service use `direction: "receive"` and the evidenced expense classification
instead of `revenueCategory`. Hosting uses `expenseAccount: 5210`; cost of revenue uses
`expenseFunction: "cost_of_revenue"`. Choose timing from the agreement; the example is earned
on delivery and billed in arrears. Price calculations reference declared terms or facts.

1. Create the customer/vendor party if absent (`parties_create`, with a stable `partyId`,
   `name` and `categories: ["customer"]` or `["vendor"]`). Create the service right above and
   retain its returned `documentId`.
2. Use `contracts_create` with an inline `definition`:
   `model: "priced-rights-v1"`, a descriptive `name`, `parties: ["customer"]`, the same
   `ledgers` declaration, and
   `activities: [{"key":"service","activityDocumentId":"<returned right documentId>","partyRole":"customer","ledgers":{"money":"money"}}]`.
   Alongside the definition supply `parties: {"customer":"<partyId>"}` and
   `ledgerBindings: {"money":"<existing matching GAAP ledger id>"}`. Substitute `vendor`
   for a purchase. Read the business's ledgers to obtain the actual binding.
3. Accept the returned draft with `contracts_accept`: `contractId`, its current
   `expectedDocumentId`, `expectedStatus: "draft"`, the evidenced acceptance `effectiveAt`,
   a stable `sourceFactId`, and
   `evidence: {"acceptance":[{"kind":"other","ref":"<agreement evidence ref>"}]}`.
4. Use `contracts_record` separately for each evidenced phase: `delivery`, `recognition`,
   and `billing`. Each supplies `contractId`, `activityKey: "service"`, the **same**
   `obligationKey` (e.g. the invoice reference), a distinct stable `occurrenceKey` and
   `sourceFactId` per phase, its actual `effectiveAt`, and `facts: {}` for this fixed price.
   Delivery and recognition use `evidence: {"service":[{"kind":"other","ref":"<delivery evidence ref>"}]}`;
   billing uses `evidence: {"billing":[{"kind":"other","ref":"<invoice evidence ref>"}]}`
   and the evidenced `dueDate` in `YYYY-MM-DD` format. Use the user's evidence refs literally;
   source fact identifiers name the distinct facts. Record recognition as well as delivery
   when the service is earned. Read outcomes and `report_activity_claims` to verify the amount,
   direction, outstanding balance and originating statement.

## Payments and reconciliation

Use `report_activity_claims` to establish whether invoices or bills remain open. An empty
`subjects_list` filtered by `record_type` alone does not establish the absence of priced-right
claims; inspect the relevant contract and its claim report before making that statement.

Read the open claim through `report_activity_claims` and find the matching counterparty,
contract, currency and invoice. Retain both its `claimId` and `component`.
Reuse the evidenced financial account, or register it with `accounts_register` using
`financialAccountId`, `name`, `currency` and `kind` (e.g. `checking`).
Use `payments_record` with that account, `direction: "in"` for a customer receipt or `"out"`
for a vendor payment, `amount` in minor units, `currency`, `partyId`, `effectiveAt`,
a stable `sourceFactId`, `evidence: [{"kind":"other","ref":"<payment evidence ref>"}]`, and
`allocations: [{"claimId":"<returned claimId>","component":"<returned component>","amount":"<allocated minor units>"}]`.
Read back the payment and claim to prove partial or full settlement. This records a transfer
that already happened; it does not initiate one.

For reconciliation run the available income statement, balance sheet and claim reports using
the requested period and cutoff. Verify cash using payment/collections reports and cash ledger
postings. Separate unrelated opening or platform entries. Explain
profit from earned revenue less recognized expenses, and cash from actual receipts/payments;
unpaid invoices and bills explain the difference. Read report parameter schemas for cutoff
semantics and show the remaining receivable/payable rather than treating them as cash.
