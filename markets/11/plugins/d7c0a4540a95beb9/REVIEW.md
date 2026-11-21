# Yumo Eats submission review notes

Package version: 0.1.1  
Review state: original 0.1.0 portal draft uploaded; revised review materials prepared. No formal submission or approval.

## What the app does

The MCP service exposes restaurant name search, current menu lookup, and cart draft preparation. A cart draft returns a time-limited Yumo Eats website link. The customer reviews current selections and completes any checkout steps on the website. No order, reservation, or payment is performed by the MCP tools. No customer account, private profile, or order-history tool is exposed.

## Authentication and reviewer data

Authentication: none. The integration serves public restaurant and menu information. Do not include private customer data, credentials, addresses, phone numbers, or payment details in test prompts. Reviewer credentials are not needed for this package.

## Test cases

The manifest contains five positive and three negative reviewer cases. On October 13, live protocol checks found Orion Poke by name and read 37 eligible menu items. One Lychee Fruit Tea produced a $5.75 draft; two Brown Sugar Milk Teas with Boba produced an $11.50 draft. The real website repriced/imported the latter and displayed final checkout total $14.09 including then-selected tip/tax. No final order confirmation was clicked. These amounts are captured evidence, not future price guarantees. Use currently returned IDs/options and generate fresh links (ten-minute expiry).

Unsupported order/payment/private-history tools were rejected, quantity zero failed validation, a nonexistent restaurant returned menu=null, foreign Origin was forbidden, and missing/invalid handoff URLs displayed safe errors. These are protocol/UI checks; ChatGPT's model-level invocation behavior for all eight prompts is not independently certified by these tests.

## Current live-service status

The configured endpoint is `https://yumoeats.com/mcp`. On October 13 production initialization and tool discovery returned HTTP 200. OpenAI Portal confirmed Domain verified, Configured, all three tools discovered and No findings in the latest MCP scan. The application remains unpublished and not submitted.

The video URL in the manifest points to a newly prepared static deployment artifact. It must become publicly accessible before formal submission. The 40-second video is explicitly a still-frame walkthrough of actual live website captures and protocol evidence, not a fabricated ChatGPT conversation or continuous screen recording. It contains no private customer contacts, payment data or credentials.

## Pending before formal review

- Deploy the new privacy/terms age alignment, eligible-result pagination correction and static walkthrough artifact. User retains manual deployment ownership.
- Verify the walkthrough URL is accessible and test empty-query pagination after deployment. Current production still has the earlier raw-pagination bug; name search works.
- Recheck model-level prompt behavior during development/review; protocol checks do not replace it.
- Publisher identity: the existing portal identity is Individual — DI CUI; developerName matches this identity. Category is Other, with the three actual capabilities declared. The portal requires these fields for this upload.
- Recheck that the support, privacy, terms, and website URLs resolve to the intended public pages.
