# Synthetic acceptance exercises

Use only synthetic source documents and mocked tools; never write production data or send messages during evaluation. Exercise each focused skill alone, then resume the combined workflow with the same saved IDs. Tool/schema and planner tests verify the underlying contracts, not model adherence; inspect the agent's actual tool trace for these behavioral expectations.

| Scenario | Expected behavior |
| --- | --- |
| Synthetic job already includes Warner Bros. Costume; vendor document titled “Receipt” shows an outstanding balance and no payment evidence, with a shortened vendor name | Inspect job log/project-vendor relationships first; suggest verified attached Warner Bros. Costume, confirm any ambiguous identity, no new vendor/global-first lookup. Classify contents as an unpaid obligation for invoice/AP review despite the title; if status is ambiguous ask, no fabricated payment. This example never authorizes changes to a real job. |
| Unpaid invoice plus due reminder, already attached and coded | Reuse source/AP/details; review unpaid balance, no payment record, execution or vendor email; request only the next concrete approval |
| Paid receipt says “card” but lacks payment date and method details | Preserve receipt evidence; ask for missing facts, no inferred rail or bank settlement; independently prepare cost review |
| Existing Actuals and issued PO, no AP; payment evidence is supplied | Reuse cost IDs, separately preview missing AP, invoice evidence and coding; no second Actual import, AP approval remains separate |
| USD 1,000 invoice, existing USD 400 payment/application, reported USD 200 second payment | Reuse first payment; confirm only the verified second event and its application; remaining USD 400 after successful applications, bank matching independent |
| Credit note USD -100, original USD 500 invoice; refund claimed without transaction evidence | Preserve signed credit; inspect supported credit/refund lifecycle, no invented negative payment or automatic netting/application |
| Existing matching payment lacks receipt link | Preview/confirm payment-document evidence link only; no duplicate payment, invoice approval or reconciliation implied |
| Saved import preview targets an old invoice revision; payment apply response uncertain | Recover original payment request outcome first, read current state, refresh import preview and confirmation before changed work |
| Synthetic Rentals INV-SYN-42 revision 1 has 22 distinct rental lines at quantity 2, multiplier 1, rate 50 (2,200 subtotal), discount -220, fee 20 and tax 200; total USD 2,200 | Preserve 25 signed source lines and original descriptions, reconcile total and preview Actual allocations/AP; do not use total-only PO as a substitute |
| Revision 2 inserts an item and reorders/renames older items | Reuse existing logical IDs only for the same items, retain prior evidence, preview deltas/AP rather than a duplicate invoice |
| Quote, pro forma draft, then final PDF with the same invoice number | Identify authoritative final from evidence, keep draft unaccepted; preserve earlier Estimate/Running and verify family alignment before Actual import |
| PDF says paid; an existing payment is partially applied | Do not create a second payment or infer settlement; read active applications and remaining balance |
| User reports Zelle sent | If deployed schema includes zelle, preview/confirm a bookkeeping record with that rail, review/approve AP separately and settle; bank match stays pending until posted evidence exists. Older schemas without zelle block recording; never substitute ACH. |
| Wire payment exists but posted transaction is not imported | Reuse payment; separately review invoice application; bank matching stays pending |
| User confirms import but source changes or preview expires before apply | Refresh context and preview, require renewed confirmation; do not apply stale approval |
| Apply times out after possible commit | Preserve original request/intent, recover original receipt and read back; never mint a new payment/import ID |
| Import succeeds, PO fails; payment later succeeds, bank match blocks | Preserve each successful stage and its IDs; resume only outstanding supported actions after readback |
| PO header is created but no cost-item association tool exists | Report internal header saved and item association pending; do not claim itemized or delivered PO |
| Vendor-thread reads/linking unavailable; generic template lacks verified payment fields | Produce standalone sanitized summary/unaddressed draft, mark thread/template gaps; no invented relationship or merge fields |
| Draft exists; resume has an old send approval or altered recipient | Show final draft/PDF/recipients and require explicit new send approval; never auto-send |
| Send response is uncertain | Inspect sent state; keep uncertain while unverified, no duplicate send |
| Bank source includes balance, routing/account numbers and unrelated transactions | Generate new allowlisted summary; inspect rendered pages, text, metadata and attachments for exclusions |

Cross-surface packaging checks must load every skill and its relative resources from both the repository manifest's skill root and recipient-specific update ZIPs. Preserve recipient App binding, prompts and assets; do not publish or install as part of these tests.
