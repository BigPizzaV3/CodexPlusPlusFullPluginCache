---
name: get-started
description: How to take a screenshot of a public web page with localscreenshot, which option answers which request, and what a result does and does not show.
---

# Taking screenshots with localscreenshot

localscreenshot opens a public web page in a real browser and returns a picture
of it, with the page title, the final address after redirects and the HTTP
status the page answered with. Use it when the user wants to see a page, or
wants you to look at one before talking about it.

## Pick the option that matches the request

People rarely name an option. Translate what they ask for:

| What they say | What to set on `take_screenshot` |
| --- | --- |
| "a screenshot of this page" | `url` only |
| "on a phone", "on an iPhone", "on a tablet" | `device` |
| "the whole page", "all the way down" | `full_page: true` |
| "just the header", "only the comparison table" | `selector` |
| "in dark mode" | `color_scheme: dark` |
| "without the cookie banner", "without ads" | `block_cookie_banners`, `block_ads` |
| "as seen from Germany", "what do visitors in Japan get" | `country` with the two-letter code |
| "as a PDF" | `format: pdf` |

Combine them freely: "the full page on a phone from France" is one call with
`device`, `full_page` and `country` set together.

Call `list_countries` when you need the code of a country, or to check that a
country is available before promising a result.

Call `get_credits` when the user asks what is left on their account. Do not call
it before every screenshot: each screenshot answer already says what is left.

## Read the result honestly

- The picture shows the page as it answered this one visit. A page can change
  between two visits, and a website can serve a different page to an automated
  visitor.
- `country_observed` is the country the page was actually loaded from, observed
  at the time of the screenshot. Quote it, not the country that was asked for.
  It is a technical observation, not a legal proof.
- `page_status` is what the website answered. A screenshot of an error page is
  still a screenshot: say that the page answered 404 or 500 rather than
  describing it as the page the user wanted.
- A PDF comes back as a short-lived download link, not as an image.

## When a screenshot fails

Say what happened in plain words and do not retry in a loop.

- The page showed a bot check: the service does not solve them. Say so.
- The page could not be loaded from the requested country: nothing was taken.
  Offer to try again or to take it without a country.
- The address is not allowed: only public http and https pages can be opened.
- There are not enough credits on the account: say so, and nothing more. Credits
  are managed by the user on their localscreenshot account, outside the
  conversation.

## What this cannot do

It cannot log in to a website, type into a form, click on the page, solve a
CAPTCHA, get past a paywall, or open an address on a private network. When
someone asks for one of those, say so plainly instead of trying. Never ask the
user for a password.
