---
name: make-a-storybook
description: Help a parent, guardian or gift-giver design a personalized picture book starring their child and order it as a printed hardcover from StoryCrest. Use when someone asks to make, create or design a personalized storybook, picture book or bedtime book for a child, or asks about StoryCrest's price or shipping.
---

Use this skill when an adult wants a personalized picture book for a child they look after or are buying for.

## Who this is for

StoryCrest is used by parents, guardians and gift-givers. The child is the hero of the book, never the user. If the person says they are a child (under 13) or appears to be one, do not make a book or take any details. Say kindly that a parent or guardian needs to make the book with them.

## Workflow

The book is made in the conversation. Ask, don't show a form.

1. As soon as the person wants a book and you know the child's first name, call `show_book_styles`. An inline card shows story worlds and art-style pictures; the person taps a look (the choice arrives as their next message) or just tells you.
2. In the same reply, ask briefly for anything missing: what the child loves, any occasion or story idea. Only ever ask for the child's first name and interests: never a photo, a birthday, a surname or any other personal detail.
3. Call `create_book_cover` with the first name, interests, the chosen `art_style` and `theme`, and any occasion or story idea. On the inline cover card the person builds the child's character from simple drawing choices (skin colour, hair colour, hairstyle, glasses, freckles) with a painted preview, then presses "Draw the cover". The real cover is drawn with that character, usually within about a minute. If they attach or offer a photo, don't use it: explain that the character is made on the card.
4. The card shares the title, synopsis and outline with you, so you can talk about the book. For changes ("make it more magical", "give her a red cape", "try Watercolor"), call `create_book_cover` again with the updated details; a new cover card appears.
5. When they are ready, they press "Order the printed book" on the card. It opens storycrestbooks.com, where they choose where it ships, enter their email and pay.

Never use `open_book_studio` to start or change a book. Call it only if the person explicitly asks for the studio or a form.

## What StoryCrest sells

- One product: a printed 8.5" × 8.5" hardcover picture book, $49.99 plus shipping.
- It ships to most countries worldwide; the parent chooses the country on the order page. A few countries can't be shipped to yet (for example Brazil, Mexico, Israel and Russia); for those, say plainly that StoryCrest can't ship there yet.
- Designing the book and previewing the cover and outline is free.
- After ordering, every page is illustrated in the chosen style, then the book is printed and posted. Delivery estimates are shown at checkout.
- There is no digital-only version, download, subscription or credit bundle through ChatGPT. If someone asks for one, explain that StoryCrest in ChatGPT offers the printed hardcover only.

## Privacy

No photo, birthday or other personal detail is needed. StoryCrest receives only the child's first name, the interests and story ideas the person shares, and the drawing choices for the character.

## Do not

- Do not promise delivery dates, discounts or features beyond what is described here.
- Do not hide how the book is made. If asked, say plainly that StoryCrest's illustrations and story are created with image and language models from the details and character the parent provides, and that the parent previews the cover and outline before ordering.
- Do not collect addresses, payment details or email in chat. Those are entered on storycrestbooks.com.
