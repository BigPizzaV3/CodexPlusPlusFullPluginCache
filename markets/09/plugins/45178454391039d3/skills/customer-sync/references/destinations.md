# Destinations

Header names are the destination's own; its downloaded template wins when it differs.

| Tool | Zid connector | Import by file | Identifier and consent |
| --- | --- | --- | --- |
| Mailchimp | App 2733 | Audience → Add contacts → Import contacts → Upload a file (CSV or TXT); pick groups and tags, match columns, then choose email or SMS marketing status | `Email Address`; also `First Name`, `Last Name`, `Phone Number`, `Birthday`. Import subscribed contacts separately from unsubscribed ones |
| Klaviyo | App 3539 (its API keys go in the Zid dashboard, not chat) | Lists & segments → list → Manage List → Import contacts | `Email` or `Email Address` first, or `Phone Number`; other headers become profile properties. Uploading is not consent: answer the import's consent question per file |
| HubSpot | — | Data Management → Import data → Quick import (CSV, XLSX, XLS) | `Email` required; `First name`, `Last name`, `Phone number` (`+` country code). Set marketing contact status and legal basis in the import |
| Zoho CRM | App 6759 | Contacts → Import Contacts; XLS/XLSX up to 5,000 per batch | `Last Name` required; `First Name`, `Email`, `Phone`, `Mobile`, `Email Opt Out` |
| Brevo | — | Contacts → Import contacts; up to 1,000,000 lines | One of `EMAIL`, `SMS`, `WHATSAPP`, `EXT_ID`; `FIRSTNAME`, `LASTNAME`; phones with country code. The import can blocklist a channel for the whole batch |
| WhatsApp Marketing (BusinessChat) | App 2005; its Sync contacts setting copies store customers that have a valid phone and at least one order | Contacts → Create or Upload Contacts → Upload CSV, into a group | Phone in international format; opt-in required for campaigns |
| Karzoun, Cartat | Apps 655, 1397; Cartat syncs the customer and abandoned-cart lists | Not documented publicly | A Zid customer or cart is not WhatsApp consent |
| Spreadsheet | — | The merchant's own columns | Keep one consent column per channel |

## Matching

- Phone: strip spaces and punctuation, add `+966` to Saudi numbers that start
  with `05`, then compare. Email: lower-case and trim.
- One person, two records: prefer the record with orders; list the pair for the merchant.

## Building an automated sync

Each destination's API keeps its key in the automation tool's credential store:
Mailchimp Marketing API, Klaviyo `https://a.klaviyo.com/api` (profile import:
75 requests a second, 750 a minute), HubSpot CRM API, Zoho CRM API (OAuth), Brevo
`https://api.brevo.com/v3` (`api-key` header; `POST /v3/contacts` with
`updateEnabled` true updates). See the `zid-ops` skill for schedules.
