---
name: vet-a-counterparty
description: Check a buyer, supplier, freight forwarder or other trading company before the user ships goods or sends money, using TradeRepute's sanctions screening and verified trade references.
---

Use this when the user is about to trade with, pay, ship to or onboard a company and wants to know if it is safe or legitimate.

1. **Screen the name first** with `screen_company`. Pass the company's country as a two-letter ISO code whenever you know or can
   infer it (it sharpens matches and adds the FDA import-refusal check), and any other names it trades under as `aliases`.
2. **Read the status carefully:**
   - `match`: a strong, current listing. Tell the user not to trade until they have reviewed the listing, and name the list and agency.
   - `potential_match`: similar names are listed. Ask the user to compare the address, country and identifiers with their counterparty.
   - `historical`: only listings that have ended. Mention them; they can still matter for due diligence.
   - `clear`: nothing found on the lists searched. Say this is **not** proof the company is trustworthy.
   - `incomplete`: some lists could not be searched. Do not call it clear; suggest trying again later.
3. **Then look for trade references** with `search_companies` and `get_company`. These need the user to connect their TradeRepute
   account; if they have not, explain what they would get (verified, evidence-backed references from businesses that actually
   traded with the company) and let ChatGPT's sign-in prompt handle the rest.
4. **Report what references say without unmasking anyone.** Reviews are anonymous. Never guess or infer which business wrote one.
5. **Unlocking a report needs the user's explicit yes.** If a report is locked and the user wants it, call `unlock_report` with
   just the company id: it returns the price and their balance and charges nothing. Ask the user to confirm, and call it again with
   the `confirmation_token` only after they clearly agree. Never confirm on their behalf or unlock a report they did not ask for.
6. **Never buy credits or write reviews.** Neither is possible from ChatGPT; both happen on traderepute.com, where reviews are
   written by verified businesses.

Finish with a short recommendation that separates facts (list matches, reference scores) from judgement, and remind the user that
screening and references support due diligence but do not replace it.
