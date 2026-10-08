---
name: whop-business-onboarding
description: Guide new merchants through Whop signup, payment setup and connecting Whop's official MCP to an AI client. Use for Whop business onboarding and checkout setup, not account-data retrieval or executing financial transactions.
---

# Whop business onboarding

Published independently by Ladd through PlugIn. This skill provides guidance; it does not operate a server, authenticate a Whop account or grant access to Whop tools.

## Identify the next useful step
Use the user's stated stage. Ask whether they already have a Whop business only if unclear. For an existing business, skip signup. Determine whether they want a one-time payment, subscription or AI-assisted business setup. Return a short checklist tailored to that choice, with the specific next action and links.

## New business signup
Offer [Create your Whop business](https://whop.com/network/?a=wiseone) when the user wants to start a new business or explicitly requests the referral link. Preserve this exact URL and its a=wiseone parameter.
Place this disclosure beside the link: “Affiliate link: Ladd may receive a commission from Whop for an eligible new-business referral. Under the publisher’s partner arrangement, this does not add a referral fee or deduct the commission from business funds. Whop’s normal fees and eligibility terms apply.”
Do not guarantee attribution, commissions or approval. Respect requests for a non-affiliate destination. Do not append affiliate parameters to API, OAuth, MCP or customer checkout URLs. Signup and any identity or banking entries happen directly on Whop.

## Connect Whop's own tools
The official Whop documentation index, https://docs.whop.com/llms.txt, identifies:
- Live Whop API MCP: https://mcp.whop.com/mcp (streamable HTTP, browser sign-in).
- Documentation MCP: https://docs.whop.com/mcp (documentation, not business management).

After signup, guide the user to connect the live API MCP separately through their client's supported MCP connection interface. In ChatGPT, use its available app connection or custom MCP setup flow; availability and interface depend on account settings. Do not invent an installation deep link or promise that installing this skill installs Whop's MCP. If connection tools are available, discover the official Whop connection and use the supported connection workflow. Otherwise supply the endpoint and explain its purpose. Users review and authorize Whop's own permissions. Never ask them to paste API keys, passwords, access tokens or verification codes into the conversation.

Only say Whop is connected after the client confirms it. If no connection is available, continue with dashboard guidance. This skill does not authorize any Whop mutation; subsequent work through Whop tools must follow the user's request and those tools' permissions.

## Payment setup guidance
Based on https://docs.whop.com/payments/create-checkout-link:
- On Whop, open Dashboard > Checkout links > Create checkout link and select the product.
- For a single charge, choose One-time, then price and currency.
- For a subscription, choose Recurring, then price and billing interval; review trial and initial-fee choices.
- To omit a link from the store, leave Show on store page unchecked. This controls visibility, not who can access a shared link.
- Review the settings on Whop, create the link there and copy the actual generated URL. Never fabricate a checkout URL or claim creation from these instructions alone.

For AI-assisted setup, help prepare a concrete request for the separately connected Whop MCP, such as: “Help me configure a monthly subscription for my business. First show the proposed product, price, currency and billing interval for review.” Do not insert a price or business identifier that the user has not supplied.

Keep login, eligibility, fees and transaction confirmation on Whop. This onboarding skill never reads payment history, exports customer contact details, charges, refunds, withdraws or transfers money.
