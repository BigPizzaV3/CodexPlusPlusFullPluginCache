---
name: make-a-photo-book
description: Make a printed photo book with foto foto from the person's own photos. Use when someone wants to turn photos into a book or album, for example a holiday, a baby's first year, a wedding, a year of family photos, or a gift for a birthday or for grandparents. Also when they ask in Dutch, such as "fotoboek maken", "maak een fotoboek van mijn vakantiefoto's", "fotoalbum laten drukken" or "fotoboek als cadeau voor oma".
---

Use this skill when the person wants a printed photo book made from photos they are allowed to use. Explicit instructions from the person come first; the steps below fill in what they did not say.

1. Find the photos.
   - Photos attached in this chat: call `create_book` with them in `attachments`.
   - A public iCloud Shared Album link (`https://www.icloud.com/sharedalbum/#...`): call `create_book` with it as `sharedAlbumUrl`.
   - Direct image links: pass them in `photos`.
   - No photos yet: call `start_photo_book` so they can pick photos in the card, or ask them to attach photos or share a public iCloud Shared Album link. Never ask for passwords or social media logins.
2. Make the book with `create_book`.
   - Use the title they gave. Otherwise use a short title from the conversation, such as "Mallorca 2026" or "Oma 80".
   - Keep the order they gave. An album is used in date order.
   - Use a fresh random UUID as `idempotencyKey`, keep it private, and reuse it only to retry the same request.
3. After the book is made, the card shows it in foto foto's book viewer, where every page can be flipped through. Answer in one or two sentences. Do not repeat what the card shows.
   - Tell them they can flip through the book in the card, or open it full screen.
   - To keep or order it, they open "Save and order" ("Bewaren en bestellen" in Dutch) in the card and save it with their email on fotofoto.app. Cover, photo and title changes happen there too.
   - A book needs at least 24 pages to be printed. If the card says the book is too short, ask for more photos.
4. For the price, call `get_book` with the `bookId`, `bookToken` and the two-letter country code of the delivery country. Report the total including shipping.
5. Payment and delivery happen on fotofoto.app. Never ask for a delivery address, card details or an email code in the chat, and never share the `bookToken` or the claim link with anyone but the person.
6. Reply in the person's language. When they write in Dutch, answer in Dutch.

Do not use this skill to edit single images, write captions, or make digital-only albums.
