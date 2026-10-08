# LeadDeck Preferred Opportunity Checker CSV Contract

Use exactly these lowercase, underscore-separated headers and this exact order:

```csv
address,address2,city,state,zip,county,property_type,expired_price,expiration_date,mls_number,opportunity_status,opportunity_rank,research_notes,owner_name,phone,phone_2,phone_3,email,email_2,email_3,notes
```

## Required for LeadDeck Import + Skip Trace

- `address` — street address only.
- `city` — city only.
- `state` — two-letter state abbreviation.
- `zip` — five-digit ZIP text; preserve leading zeroes.
- `address2` — optional, but use it for Unit/Apt/Suite and keep the unit out of `address`.

## Opportunity Checker fields

- `opportunity_status` — use exactly `EXPIRED_NOW_RENTAL` or `EXPIRED_OFF_MARKET`.
- `opportunity_rank` — numeric integer only: `1`, `2`, `3`, etc. Never `#1`, `A`, or `High`.
- `research_notes` — short factual explanation supporting qualification. Include the research date when practical, e.g. `Checked 2026-09-19. Expired 2026-05-12. No current for-sale listing or post-expiration sale found. Property currently advertised for rent.`

## Other fields

- `county` — preserve when available.
- `property_type` — preserve when available.
- `expired_price` — plain numeric amount without `$` or commas when available.
- `expiration_date` — use `YYYY-MM-DD` when available.
- `mls_number` — preserve source MLS/listing identifier when available.
- `owner_name`, `phone`, `phone_2`, `phone_3`, `email`, `email_2`, `email_3` — preserve legitimate values from the uploaded source; otherwise leave blank. Do not perform contact research merely to fill them.
- `notes` — preserve useful source notes that do not belong in `research_notes`.

## Formatting rules

1. One property per row.
2. Never combine the complete location into `address`.
3. Never duplicate a unit in both `address` and `address2`.
4. Use two-letter state codes.
5. Use five-digit ZIP text and preserve leading zeroes.
6. Use ISO dates (`YYYY-MM-DD`).
7. Use plain numeric prices when possible.
8. Leave unavailable values blank; never fabricate missing values.
9. Output only qualified opportunities. Ambiguous/listed/pending/sold properties do not belong in the final LeadDeck CSV.
10. Preserve complete source URLs in `research_notes` exactly as researched; do not shorten or omit them.
11. The final file should import with minimal or zero mapping interaction in LeadDeck → Import Sellers.
