---
name: get-started
description: How to send a real paper letter with BeyondSky Post, from writing it to payment and tracking.
---

# Sending a letter with BeyondSky Post

1. Get the recipient's full postal address (name, street, postcode, city, country) and the sender's name and address. The sender address is printed on the letter and used for returns.
2. Write the letter with the user, or use the PDF or Word file they give you. Do not repeat the addresses or the date in the text: they are added automatically.
3. If the user asks about price, call `get_quote`. Registered mail is only available to France, Germany, Spain, Switzerland and Belgium.
4. Before calling `send_letter`, show the user the recipient, the sender, the service (plain or registered) and the full text, and ask them to confirm. Sending creates a real letter.
5. `send_letter` returns a preview link and a payment page on getpostmcp.com. Give both to the user. Nothing is printed before they pay.
6. Use `get_letter_status` to tell the user where their letter is.
