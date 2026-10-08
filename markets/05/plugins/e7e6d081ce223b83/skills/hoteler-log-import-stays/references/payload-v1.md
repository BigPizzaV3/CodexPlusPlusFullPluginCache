# Hoteler Log external stay payload v1

Use one envelope per stay:

```json
{
  "version": 1,
  "importId": "UUID",
  "expiresAt": "UTC ISO 8601 instant",
  "source": "chatgpt",
  "stay": {
    "hotelName": "Hotel name",
    "checkIn": "YYYY-MM-DD",
    "checkOut": "YYYY-MM-DD",
    "bookingChannel": null,
    "priceAmount": "112400",
    "priceCurrency": "JPY",
    "pointsUsed": null,
    "notes": null
  }
}
```

The generator creates the envelope, UUID, expiration, compact JSON, and Base64URL. Do not construct or modify those values manually.

The plugin registration currency is JPY. Hoteler Log's v1 payload receives either a JPY price or no price:

- A clearly stated JPY source amount is copied unchanged with `priceCurrency` set to `JPY`.
- A clearly stated foreign amount for a check-in date that is today or earlier may become a whole-yen JPY amount only after the official-ECB procedure in `SKILL.md` succeeds. The generator input carries the original amount/currency plus the generator-only `exchangeRate` object. The generator verifies the cross-rate calculation and writes only the derived amount and `JPY` into the app payload. `exchangeRate`, its component rates, and the original foreign amount/currency are not payload fields.
- Otherwise both payload money fields are null. This includes future check-in dates, unsupported ECB currencies, no common official publication within the prior 10-calendar-day window, unavailable browsing, ambiguous money, and a user-stated app currency setting other than JPY. Money omission must not delay an otherwise link-ready stay.

The plugin cannot read Hoteler Log's main-currency setting. Every price-bearing plugin link therefore assumes the app's setting is JPY. If it is not JPY, generate a price-empty link and let the user enter the amount in the app. Never alter the app setting, attach a foreign currency to the derived amount, or label an unconverted foreign amount as JPY.

## Constraints mirrored from the app

| Field | Constraint |
|---|---|
| Payload | At most 16 KiB UTF-8 per stay |
| hotelName | Required after trimming; at most 100 characters; exact catalog/alias match, or an unlisted lodging name explicitly confirmed in the candidate table |
| checkIn/checkOut | Exact local `YYYY-MM-DD`; check-out later than check-in |
| Date range | From 1900-01-01 through 5 years after generation date |
| Stay length | At most 365 nights |
| bookingChannel | Optional; plugin permits only the exact known values below; omit unknown values |
| priceAmount | Optional non-negative decimal string. JPY source stays unchanged; successful foreign conversion becomes a half-up-rounded whole-yen string; otherwise null |
| priceCurrency | `JPY` whenever `priceAmount` is present; otherwise null |
| pointsUsed | Optional integer from 0 through 1,000,000,000 |
| notes | Optional; plugin permits one exact predefined non-sensitive tag below |
| Link expiry | 24 hours after generation |

For a foreign generator input, `exchangeRate` is a control object rather than an app field. It contains only `provider`, `rateDate`, `sourceUnitsPerEUR`, and `jpyPerEUR`. `provider` must be the exact value `ECB`, `rateDate` must be the latest common publication date on or before local check-in and no more than 10 calendar days earlier, and the two rate strings must be official observations for that same date. The generator computes `source amount * jpyPerEUR / sourceUnitsPerEUR` with decimal arithmetic and rounds half-up to a whole yen. Never put the object or either component rate in the envelope.

Known exact booking-channel values are `公式サイト`, `ポイント予約`, `一休.com`, `楽天トラベル`, `じゃらん`, `JTB`, `Yahoo!トラベル`, `Relux`, `Agoda`, `Booking.com`, `Expedia`, `Trip.com`, `Hotels.com`, `Amex FHR`, `Amex THR`, `Hotelux`, `Tablet Hotels`, `Mr & Mrs Smith`, `Virtuoso`, and `Visa Luxury Hotel Collection`. Do not translate, fuzzy-match, retain, or coerce an unknown value; set it to null and let the user select it in the app.

Allowed exact note tags are `朝食付き`, `夕食付き`, `朝夕食付き`, `素泊まり`, `返金不可`, `現地払い`, `事前決済`, `駐車場付き`, `クラブラウンジ利用`, `アーリーチェックイン`, and `レイトチェックアウト`. Set any other note to null. The user can safely add free text in the app after reviewing the source.

The bundled hotel-name catalog is generated from the app's canonical `PresetJapaneseHotels.json`. A catalog name is accepted directly. For an unlisted property, show the exact extracted name as `未登録` in the candidate table and obtain explicit user confirmation before setting the generator-only `unlistedHotelNameConfirmed` flag. The flag is never encoded into the payload. The generator rejects explicit personal/secret patterns, long payment-card-like numbers, URLs and dangerous URI schemes, invisible controls, generic placeholders, and instruction-like text. It does not reject a confirmed name merely because it uses kanji, kana, mixed scripts, spaces, or digits. Automated detection cannot prove that arbitrary text is a lodging name, so the unlisted-name confirmation and the app's final review are both mandatory.

The generated URL is:

```text
https://hoteler-log.pages.dev/import#payload=<unpadded-base64url>
```

Only the fragment carries the payload. Never put `payload` in the query string. The website must not decode the fragment.

For an exact catalogued lodging name, the user's request to add, import, register, or create Hoteler Log links authorizes immediate generation when the required fields are valid and no duplicate or required-field ambiguity remains. Show the sanitized fields alongside the link so the user can correct them. An unlisted lodging name still requires explicit confirmation before generation.

Base64URL is reversible encoding, not encryption. The link may remain in the ChatGPT conversation, clipboard, notification preview, or browser history. Keep its lifetime short and do not share it. Regenerating a corrected candidate creates a new UUID and expiry but cannot revoke the old stateless link; tell the user to use the new link and discard the old one, which remains technically usable until its original 24-hour expiry.

## Local JSON fallback

If Universal Links are unavailable, give the user this sanitized document for Hoteler Log's explicit paste screen:

```json
{
  "version": 1,
  "stay": {
    "hotelName": "Hotel name",
    "checkIn": "YYYY-MM-DD",
    "checkOut": "YYYY-MM-DD",
    "bookingChannel": null,
    "priceAmount": "112400",
    "priceCurrency": "JPY",
    "pointsUsed": null,
    "notes": null
  }
}
```

The fallback is one document per stay and follows the same gate and money policy as link creation: it may be shown immediately for a valid catalogued name, while an unlisted name still requires explicit confirmation. It contains no UUID, expiration, source, generator-only `exchangeRate`, or personal fields. Use null money fields in the fallback whenever the official foreign conversion was not already completed and verified.
