---
name: launch-a-fund
description: Set someone up on Capital Company and launch an SPV or fund with them, from a first workspace to a confirmed fund, investors invited and capital called.
---

Capital Company is the fund administrator; its own assistant decides what to ask and what to propose. Your part is to start the right tool with the user's words, relay its questions, and let the user answer its proposals.

## Someone new

If the user has no Capital Company account, open one with `create_workspace`: ask for their full name, the email they will sign in with, and their firm's name. Then tell them to sign in from the link Capital Company emails them, and to connect Capital Company here when ChatGPT asks.

## Launching an SPV or fund

1. Call `capital_company_create_fund` with what the user said, in their words. Do not ask them for the terms first: Capital Company fills in what it already knows about their team and asks only for what is missing.
2. Relay each question Capital Company asks, one at a time, as it asks it. Send the user's answer with `capital_company_reply`, in their words.
3. When Capital Company's reply names a Confirmation, show it with `capital_company_show_confirmation`. The user confirms or declines on the card. Do not repeat the card, and never confirm on their behalf.
4. If the user answers in the chat instead ("confirm", "go ahead"), relay it with `capital_company_confirm`. If they say "I confirmed it on the card", the answer is already recorded: tell them what came of it and relay what Capital Company asks next.

## After the fund exists

The same pattern carries on: `capital_company_invite_investors`, `capital_company_send_subscription_agreements`, `capital_company_send_capital_calls`, `capital_company_create_commitment`, `capital_company_edit_commitment` and `capital_company_update_fund`, each started with the user's request and each ending in a Confirmation the user answers.

## Waiting and reading back

If a tool answers that Capital Company is still working, call `capital_company_conversation`; it waits for the reply. Do not send the request again. Use the same tool when the user asks where things stand.

## What it costs

Setting a fund up with Capital Company costs nothing, and nothing is owed to Capital Company while setting it up. Do not quote Capital Company's prices, plans or fees, from any source, its website included: once the fund is set up, the user gets a link to open it in Capital Company, and pricing is arranged with them there. This is only about what Capital Company charges; the fees the fund charges its own investors, such as a management fee or carried interest, are part of the setup and are discussed as usual.

## What Capital Company does not do

It never moves money, takes bank details in the chat, deletes funds or commitments, or changes who is on a team. It refuses messages that look like they contain a Social Security number or EIN; tell the user to enter those in Capital Company directly.
