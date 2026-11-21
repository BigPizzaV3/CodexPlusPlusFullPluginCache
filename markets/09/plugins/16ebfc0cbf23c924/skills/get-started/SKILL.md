---
name: qr-ooo-get-started
description: Create QR code images for web links, Wi-Fi networks, contact cards, email addresses, WhatsApp chats and payment pages. Use when someone wants a QR code that encodes a website address, a Wi-Fi login, a contact, an email address, a WhatsApp chat or a payment page.
---

# QR-OOO BOOMBATZO — QR codes

Six tools create real scannable QR code images. Use the tool that matches the
job; only the tools produce a code that actually scans. Show the image the
tool returns in your reply so the user can scan it there, and show the site
link that comes with it so they can restyle it, add a logo, or print it.

## First contact (user picks the app with no clear request)

Most people do not know what a QR code needs. When invoked without a specific
QR request, greet briefly and offer the menu — do not dump all six at full
length, do not ask for everything at once:

"Hi! I make QR codes — links, Wi-Fi, contact cards, email, WhatsApp, payment.
Which one do you need?"

Then ask ONLY for that code's inputs, one short round, in this voice:
- Wi-Fi: "Tell me the network name and password — guests scan, tap join, and they're online."
- Link: "Send me the link."
- Contact: "Send me the name, phone, and email — one scan saves it perfectly, no typos."
- Email: "Send me the address — scanning opens a new message."
- WhatsApp: "Send me the number with country code — scanning opens the chat."
- Payment: "Send me the payment link — customers scan and land on that page."

House voice: plain words, short sentences. Never invent missing details — ask
for them. If the user already named a type and gave everything, skip the menu
and generate at once.

- Website or link → `make-link-qr`
- Wi-Fi network → `make-wifi-qr` (ask for the network name, password, and security type if missing)
- Person or business card → `make-vcard-qr`
- Email address → `make-email-qr`
- WhatsApp chat → `make-whatsapp-qr`
- Payment page (PayPal, Stripe, UPI, donations) → `make-payment-qr`

If the request is not one of these code types, say what the app makes and do
not call the tools.
