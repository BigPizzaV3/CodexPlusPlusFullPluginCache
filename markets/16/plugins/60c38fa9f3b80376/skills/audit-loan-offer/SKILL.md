---
name: audit-loan-offer
description: Check a loan sanction letter, offer, quote or Key Facts Statement (KFS) for hidden costs and breaches of RBI rules, compare several offers by true cost, and check whether a loan app is legitimate. Use when the user uploads or pastes a loan offer or KFS, asks "is this a good offer", "is this loan app safe", or "which of these offers is cheaper".
---

# Audit a loan offer

Explicit instructions from the user override this workflow.

## One offer
1. Read the document the user shared. Extract: lender and lender type (bank / NBFC / HFC / digital app), loan type and purpose, sanctioned amount, rate and fixed/floating, tenure, EMI, APR, processing fee (and whether GST is included), other upfront charges, insurance premium and whether it is mandatory, prepayment/foreclosure charge, how late-payment penalties work, cooling-off period (digital loans), and where the money will be disbursed.
2. If a field is not in the document, leave it out — don't assume. Ask only about things that change the verdict: whether a fee was demanded before disbursal, and whether a KFS was given.
3. Call `audit_loan_offer`.
4. Present: the verdict and headline first; then a table of findings ordered violation → warning → ok, each with the RBI source link; then the questions to ask the lender (as a ready-to-send message).
5. If the verdict is `walk-away` because of an upfront payment demand or third-party disbursal, say plainly not to pay, and give the reporting routes from the result.

## Several offers
Extract each offer the same way, then call `compare_loan_offers`. Lead with the cheapest offer by total cost and say explicitly when a lower headline rate is not the cheaper loan. If tenures differ, say the totals aren't like-for-like and compare APR.

## Loan apps
For a digital loan app, call `check_loan_app_safety`. Ask the unanswered questions in one message (yes / no / unsure). If the verdict is `stop`, tell the user not to share contacts/photos access or pay anything, and link the RBI directory from the result.

## Don't
- Don't call a lender's conduct illegal unless the finding is a `violation` with a cited rule; otherwise say "worth questioning".
- Don't repeat account numbers, PAN, Aadhaar or addresses from the document back to the user.
