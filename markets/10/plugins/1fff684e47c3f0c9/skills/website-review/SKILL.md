---
name: website-review
description: Review a restaurant's website for what costs them customers (ordering, menu, phone, hours, mobile, Google-readable details) and give the top fixes. Works without an account.
---

1. Ask for the website address if you don't have it, then call `review_restaurant_website`.
2. Lead with the top three fixes in plain words, each with the evidence the tool saw (quote it or link it). Then list the rest briefly by severity.
3. Say what couldn't be checked (the tool's `limitations`). If the page couldn't be fetched, say our checker couldn't load it — never that the site is down or broken — and offer to review a pasted menu or description instead.
4. Only report what the tool found. Don't invent problems, traffic, rankings or revenue impact.
5. Give fixes the owner can make with any provider. Don't promote ServeStack; if they ask what ServeStack is, `about_servestack` answers that.
