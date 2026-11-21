---
name: build-a-page
description: Use when someone wants a link-in-bio page, a simple one-page website for their links, or wants to change their Exclusively Me page.
---

# Build or change an Exclusively Me page

1. **Not connected to an account** (the account tools say to connect): ask only for
   their name or business name, the links they want (handles, numbers with country
   code, web addresses) and the feel (dark, light or violet). Never ask for an email
   or a password. Call `drafts_create`.
2. Show them the page in a short list (name, bio, each link) with the `previewUrl`.
   Offer `usernameSuggestions` if no username was kept. Changes: `drafts_update`
   with the whole draft again.
3. When they're happy, give them the `claimUrl`. They sign up, agree to the
   terms and the page becomes theirs. It goes public once they confirm their email.
4. **Connected to an account**: call `account_get` first and say which account you're
   connected as. For a new page or website, ask: a sub-page on this account
   (`pages_save`), or a separate page with its own address (`drafts_create`)?
5. Every change to a connected account is a proposal: list what will change, give
   the preview link, and call `changes_confirm` only after they say yes.
6. Call `help` whenever you're unsure which tool to use.
