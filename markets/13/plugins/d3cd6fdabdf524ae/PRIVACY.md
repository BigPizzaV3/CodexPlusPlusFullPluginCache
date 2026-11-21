# Planets360 Plugin — Privacy Disclosure

This document describes how the Planets360 Vedic Astrology plugin handles data
when used inside ChatGPT / Codex. It supplements the
[Planets360 Privacy Policy](https://planets360.in/privacy-policy) and
[Terms and Conditions](https://planets360.in/terms-and-conditions).

## What data is used

- Only the fields the user provides for the requested calculation are
  transmitted: birth date, birth time, latitude, longitude, IANA time zone,
  date ranges, Moon sign, Nakshatra/birth star, Panchapakshi bird, or names
  used for compatibility lookups.
- No account is required and no email address or phone number is requested.
- The plugin never reads, stores, or reconstructs the chat log. It operates
  only on the explicit tool arguments the model sends for the current request.

## Where data goes

- Calculation requests are forwarded as HTTPS POST bodies to the Planets360
  calculation API (default host: `https://ephemeris.gopim.dev`), used solely
  to compute the requested astrology report.
- The article tool fetches public pages from `https://planets360.in` only
  (HTTPS, same-site hostnames, redirects refused) and returns extracted text.

## Storage and retention

- The MCP server stores no personal data: no database, no account system, no
  persistence between requests. In stateless HTTP mode each request is
  handled with a fresh server instance.
- The upstream calculation API processes requests ephemerally to return the
  result; it does not require user identity.
- Request data is not used for advertising, profiling, or marketing.

## Credentials

- The Planets360 API token lives only in the MCP server's environment
  (server-side). It is never returned to the client and must never be pasted
  into chat.

## Website analytics (not plugin usage)

- Google Analytics and Google Ads cookies apply only when a user browses
  `planets360.in` directly in a web browser. They are not triggered by plugin
  tool calls inside ChatGPT.

## Contact

- Privacy questions: support@planets360.in or
  https://planets360.in/contact-us
