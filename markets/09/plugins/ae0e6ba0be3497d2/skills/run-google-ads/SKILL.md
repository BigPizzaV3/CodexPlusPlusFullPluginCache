---
name: run-google-ads
description: Launch and run a Google Search ad campaign on the user's own Google Ads account. Use when the user asks to advertise on Google, run search ads, find keywords to bid on, launch, pause or turn on a Google Ads campaign, or see how their Google ads, keywords and search terms are doing.
---

# Run my Google ads

Use this skill to build a Google Search campaign on keywords people really search, show it before any money moves,
and read back how it is doing. Everything is created paused and spends nothing until the user turns it on.
Explicit instructions from the user always take priority over this skill, including the account, keywords, budget,
locations and wording they name.

## Before you start
Call `list_google_ads_campaigns` with no account id: it lists the Google Ads accounts the user can use. If Google
Ads is not connected, say so and that it is connected in the Hermoso app under Connectors, in the sidebar. Never
ask for a password or token in the chat. If there are several accounts, ask which to use.

## Pick the keywords
Call `google_ads_keyword_ideas` with the user's website or a few seed terms and their country. Propose 10 to 20
keywords with their monthly searches, and let the user cut or add.

## Launch a campaign
1. Agree the landing page, the daily budget in the account's own currency, the locations and the language. Ask for
   anything missing; do not pick a budget for the user.
2. Write 3 to 15 headlines of up to 30 characters and 2 to 4 descriptions of up to 90 characters, and show them.
3. Call `create_google_ads_campaign` with the budget, locations and an `adGroup` holding the ad and the keywords.
   It builds everything at once, paused, and reads it back. Show its summary, and pass on its note word for word.
4. Turning it on starts real ad spend. Show the campaign name and daily budget, ask for an explicit yes, then call
   `set_google_ads_status` with the campaign, `status` set to ENABLED and `confirm` set to true. Pausing needs no
   confirm.

## How it is doing
Call `list_google_ads_campaigns` with the account id for each campaign's numbers. For the searches that triggered
the ads, or keyword by keyword, call `google_ads_report` with a query on the search terms view or the keyword view.
Costs come back in micros: divide by 1,000,000. Quote only numbers the tool returned.

## Credits and spend
Building and managing campaigns uses no Hermoso credits. The ad spend is billed by Google to the user's own account.

## Do not
- Do not turn a campaign on, or raise a budget, without the user's explicit yes to the exact name and amount.
- Do not say a campaign exists, or what its status is, unless a tool read it back.
