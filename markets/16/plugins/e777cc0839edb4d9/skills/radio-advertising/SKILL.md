---
name: radio-advertising
description: Plan a radio advertising campaign on emRadios — find stations, check their channels and reference prices, request quotes and follow the answers; or, for radio owners, answer the requests their stations received. Use when the user wants to advertise on radio, find radio stations in a city or region, or manage quotes as a station owner.
---

# Radio advertising on emRadios

emRadios is a catalog of online and FM/AM radio stations and a marketplace where advertisers ask stations for a price. Use the emRadios tools to move the user through the campaign.

## Advertiser workflow

1. **Clarify the goal** in one short message if anything is missing: region or stations, start and end dates, spot length and airings per day, and whether they also want social posts (Instagram, TikTok, WhatsApp, website).
2. **Find stations** with `search_radios` (by name or city, works without an account) or `radios_in_radius` (stations that have an owner and can answer, needs the account). Show a short list and let the user pick. Do not pick for them.
3. **Check a station** with `radio_details` before asking for non-audio channels: it shows the accepted channels and reference prices.
4. **Request quotes** with `create_campaign` only after the user confirms title, dates and stations. Non-audio channels need a briefing.
5. **Follow the answers** with `my_campaigns` and `get_campaign`. Present prices as returned; never estimate missing ones.
6. **Close** with `open_campaign_in_panel`: it sums the chosen quotes and returns the emRadios link. Accepting and paying happen only on the website.

## Radio owner workflow

- `my_radios` and `received_quotes` to see requests; `answer_quote` (price for the whole period, in BRL) or `decline_quote` only after the user confirms.
- `proposal_channels` / `set_proposal_channels` and `update_radio` to keep the station up to date; confirm before changing anything.

## Rules

- Never ask for or accept passwords, card or bank data in the chat. If the user is not connected, ask them to connect the emRadios account.
- Never invent stations, prices or audience numbers. If a tool returns nothing, say so and suggest broadening the search.
- Reply in the user's language.
