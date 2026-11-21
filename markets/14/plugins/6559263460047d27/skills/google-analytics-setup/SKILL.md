---
name: google-analytics-setup
description: Help the user start using TalkToData Google Analytics after installation, explain GA4 reports, and guide secure account connection from the conversation.
---

Help the user set up **TalkToData Google Analytics**, the plugin whose MCP server is `https://talktodata.navines.com/mcp/google-analytics`.

## Start the Google Analytics conversation

When invoked by the installation setup action, immediately call `getGoogleAnalyticsSetup` with no arguments. This is public setup information; it does not require authentication or inspect an account. Do not call a protected report merely to welcome the user.

Answer in the user's preferred language. Name Google Analytics 4 explicitly in the opening sentence. Explain concisely that after connecting their GA4 property they can review traffic and acquisition, popular pages and landing pages, audiences and devices, campaigns, events, ecommerce, period comparisons, and Realtime activity. This plugin reads reports; it does not edit GA4 or the website.

Give the clickable connection URL returned by the tool. Explain three steps: sign in to TalkToData, authorize Google and choose a GA4 property, then return to this conversation and ask for a report. ChatGPT may ask the user to connect this plugin when private report access is first needed. Do not imply that installation alone authorizes Google or that the public setup tool checked their connection.

Offer the returned WhatsApp and email support links for connection help or feedback. End with one concrete Google Analytics question they can try after connecting, such as: "Use TalkToData Google Analytics to show my traffic, acquisition sources and top pages for the last 7 complete days."

If the setup tool is temporarily unavailable, the public connection page is https://talktodata.navines.com/connect/analytics and support is https://talktodata.navines.com/contact. Explain that setup information is available but no account status has been verified.

## After connection

When the user asks for a private report, use this plugin's corresponding GA4 tool and follow its OAuth challenge if needed. Work from returned data only. Keep the selected property, date range, reporting time zone, aggregate totals and row limits clear. Label reviewer fixtures as synthetic sample data and never substitute them for unavailable customer data. Never request passwords, tokens or authorization codes in chat. Do not use another Analytics, merchant or seller plugin to answer this plugin's setup request.
