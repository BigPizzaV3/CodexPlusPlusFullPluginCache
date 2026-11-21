# Output Template: Tender Pricing Report (tender-pricing Step 5)

Then report, applying Pattern 8 for the `TP-[NNN]` ref (session-local; increment on a prior
`TP` ref in this conversation, else `001`):

```
TENDER PRICING BUILD-UP — [Tender Name]
Ref: TP-[NNN]
Bill: [source file, per boq.md] | Rate library: [sweep date(s), or "none read"] | Quote register: [rows cited, or "none read"]
```

1. **SUMMARY** — two sentences: priced total, count/value of UNPRICED items, and the LOW BASIS
   exposure subtotal (£ and %).
2. **SECTION BUILD-UP TABLE** — the Step 2 per-section roll-up, each cell's element(s) and
   source label(s) visible, UNPRICED lines shown with billed quantity, not omitted.
3. **UNPRICED ITEMS** — the Step 4 list, in full.
4. **LOW BASIS EXPOSURE** — the subtotal and which norms drive it.
5. **PRELIMS, OH&P AND RISK** — the Step 3 lines, each labelled "user-stated commercial
   decision" or "REQUIRED, not stated this session".
6. **ASSUMPTIONS REGISTER** — the Step 4 table, in full.
7. **FILES WRITTEN** — `tender/pricing.json` + `tender/pricing.md`, with the sensitivity
   reminder.
8. **NEXT STEPS** — `$quote-levelling` for any package with more than one quote on
   file (level before adopting one into Step 2(c)); the Bid Advisor's settle mode to review
   this build-up against the bill and quote coverage before submission.
9. **STANDING CAVEAT**, always, unmodified:

> This is a pricing build-up assembled from your achieved norms, your quotes, and your stated
> commercial decisions — **it prices the bill you gave it and nothing else**. UNPRICED lines
> are gaps, not zeros, and must be closed (by a norm, a rate, a quote, or a stated OH&P/risk
> figure) before this build-up is relied on for submission. No rate in this document was
> invented, assumed "typical", or drawn from a market source. Ref: TP-[NNN] is a session-local
> sequence number for cross-referencing.

---

