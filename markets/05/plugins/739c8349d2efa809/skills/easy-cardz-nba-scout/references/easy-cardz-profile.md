# Easy Cardz default profile

Use these defaults unless the user overrides them for a run.

## Acquisition and target

- Buy on CardHobby.
- Keep the all-in acquisition cost between EUR 10 and EUR 250.
- Define all-in acquisition cost as card price plus visible CardHobby shipping, buyer fees, import costs, and currency costs.
- Require at least 20% expected ROI: `expected net profit / all-in acquisition cost`.
- Do not require a separate minimum euro profit.
- Show every requested in-scope card. Rank and classify cards, but do not return favorites only.

## Resale assumptions

- Primary channels: private eBay Germany and Instagram.
- Outbound shipping: EUR 6.19.
- Packaging cost: EUR 0 until the user changes it.
- Private domestic eBay sale fee: 0% by default.
- Instagram platform fee: 0% by default.
- Override the fee when the user uses promoted listings, paid payment protection, currency conversion, or international selling.

eBay states that selling on eBay.de within Germany is free for private sellers, while optional features and some other selling situations can incur fees. Because this rule can change, verify it from eBay's current official private-seller fee page when a live calculation materially depends on it:

`https://www.ebay.de/help/selling/fees-credits-invoices/selling-fees?id=4822`

## Tracker behavior

- Use the verified CardHobby listing ID as the deduplication key.
- Keep Buy, Watch, Too Expensive, Pass, and ended listings visible unless the user explicitly requests archival.
- Treat a user-entered maximum bid as maximum all-in CardHobby acquisition cost by default.
- Never place a bid or infer that the user won an auction without evidence.
