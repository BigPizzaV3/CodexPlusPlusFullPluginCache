---
name: wifi-and-contact-qr-codes
description: Create a CodeQR QR code that encodes something other than a web address - Wi-Fi credentials a scan joins, a contact card a scan saves, a WhatsApp chat, an email, an SMS, a phone number, plain text, or a crypto payment request. Triggers on QR code for my wifi, QR with my contact details, vCard QR, WhatsApp QR, or any QR request where the target is not a link. Not for a QR code that opens a URL, not for bulk creation across a list, and not for reading or decoding an existing QR image.
---

# QR codes that encode something other than a link

A CodeQR QR code can carry a Wi-Fi network, a contact card, or a message, not
only a web address. Create these with `create_qrcode` through the CodeQR MCP
tools. Never generate a QR image locally: a local image cannot be edited or
measured afterwards, which is the whole point of creating it here.

## Always send both `type` and the payload of the same name

`type` names what the code encodes. The payload field carries the content, and
it is **named exactly like the type** — `type: "wifi"` goes with a `wifi` object.

`type` defaults to `"url"` when omitted. Sending a `wifi` payload and forgetting
`type` therefore produces a link code with nothing to link to, which saves
without complaint. Pass both, every time.

| `type` | payload | minimum |
|---|---|---|
| `wifi` | `wifi` object | `ssid` |
| `vcard` | `vcard` object | — |
| `whatsapp` | `whatsapp` object | `number` |
| `email` | `email` object | `email` |
| `sms` | `sms` object | `tel` |
| `phone` | `phone` string | the number |
| `text` | `text` string | the text |
| `crypto` | `crypto` object | `address` |

`whatsapp.number` must be E.164 **without** the `+` and without separators —
`5511999999999`, not `+55 11 99999-9999`. The API rejects anything else, so
normalise whatever the user pasted before calling.

## Four field names that are not what you would guess

Payloads are stored as free-form JSON. A misspelled key **saves successfully**
and encodes nothing — there is no error to notice, and the failure only surfaces
when someone scans the printed code. These four are worth reading twice:

- **`email.cco`** is BCC. Not `bcc`. The name is Portuguese, from *com cópia
  oculta*.
- **`sms.subject`** is the **message body**. SMS has no subject line; the field
  is misnamed, not misused.
- **`crypto.address`** is the wallet address. There is a `crypto.email` field in
  the codebase and it is not this one.
- **`vcard`** only encodes `city`, `state`, `zipcode` and `country` when
  `address` is also present — they are assembled into a single address line.
  A city sent on its own is silently dropped.

For an open Wi-Fi network, set `wifi.encryption` to `"nopass"`. Leaving it out,
or inventing a value, produces a code that scanners cannot interpret. Valid
values are `WPA`, `WPA2`, `WEP` and `nopass`. There is no hidden-network option.

## Three types this connector cannot create

`pix`, `geo` and `facetime` exist in the CodeQR dashboard but are not offered
here, because a dynamic one does not currently work: a Pix scan lands on the
site root instead of a payment, a geo code encodes an undefined coordinate, and
FaceTime encodes an empty string.

If the user asks for one, say it is not available through this connector rather
than substituting a different type that looks similar. A Pix payment encoded as
`text` is not a Pix code, and the user finds out at the till.

## Every code created here is dynamic

The printed pattern encodes a short link. A scan resolves it and lands on a
CodeQR page that renders the content — the Wi-Fi join prompt, the contact card,
the payment request. Three consequences worth stating to the user:

1. **The content can be corrected after printing.** A wrong Wi-Fi password is
   fixed with `update_qrcode`; the printed code stays valid.
2. **The type cannot be changed afterwards.** Sending a `wifi` payload to a code
   created as `vcard` returns 200 and changes nothing. To switch, create a new
   code — and say so plainly, because the successful-looking response is exactly
   what would otherwise be reported back as done.
3. **The content is readable by anyone holding the short link.** It is served
   from a public page, so a Wi-Fi password in a QR code is as private as the
   link is unshared. Mention this once for Wi-Fi and crypto codes; do not repeat
   it for a vCard the user is handing out on purpose.

## Report back

Give the short link, and one line describing what a scan does — "joins the
network `Cafe-Guest`", "offers to save Marina Alves as a contact". The user
cannot verify a payload by looking at a QR image, so the sentence is the only
check they have before it goes to print.

Scans are counted the same as any other code: `get_analytics` with
`event: "scans"`.
