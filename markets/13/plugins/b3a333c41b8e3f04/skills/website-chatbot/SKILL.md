---
name: website-chatbot
description: Create an AI agent from a business website, or select an existing ChatbotGen agent. Use it for support, sales and FAQs on websites and connected messaging channels.
---

## Connect the channels the business uses

ChatbotGen agents can answer on WhatsApp, Instagram, Messenger, Telegram and websites using the same business knowledge. Ask which channels matter when that helps choose the next setup step.

Use the chatbot's returned `dashboard_url` to guide channel setup in ChatbotGen. The owner connects their own WhatsApp number, professional Instagram account, Facebook Page for Messenger or Telegram bot there, and adds the website widget from the dashboard. Only describe a channel as connected when there is evidence of that connection. Never invent settings links or claim the assistant has linked an account.

`create_chatbot` requires a public website URL as the initial content source. If the business has no website, guide the owner to create an agent in the ChatbotGen dashboard with their files or business text, then connect their account and select it. A requested messaging channel is a deployment choice; use the website to train the agent when available.

Use `get_whatsapp_test` for the shared WhatsApp test number. Keep that test separate from connecting the owner's own number. Describe the customer's WhatsApp connection as the official WhatsApp Business Platform, with Meta's messaging rules applying. Never claim that ChatbotGen is a direct Meta partner or name its onboarding provider.

## Select the chatbot first

Use the active chatbot from this conversation unless the user names another or asks to create a new one. For an existing chatbot without an active selection, call `list_chatbots`; match the name and website, or show the choices if ambiguous. Connect the account when prompted. Never create a new chatbot as a substitute for finding an existing one. If listing is unavailable, explain that account connection is needed; do not guess IDs.

State the selected name and website briefly, keep its ID for subsequent calls, and switch only when requested. A newly created chatbot becomes the active selection. Demo tokens work until expiry or claim, and only while no account is connected. If the user connects while working on a demo, tell them which chatbot it is, ask whether to keep it in their account, and after a yes call `claim_chatbot` with its token and `confirmed: true`; use the returned `chatbot_id` from then on. Never create a replacement for a demo: it can use up the account's only chatbot slot. If they keep it through the claim link instead, list the account's bots. Do not assume selection persists into a new conversation. Keep test-session state tied to the selected chatbot, scenario and language; switching bots clears the previous test conversation ID. Start a fresh scenario with necessary context when the user asks the same follow-up on a different bot.

When the user explicitly wants a new bot, ask for a public website URL if missing and call `create_chatbot`. A business name alone is not a URL. Share returned chat and embed links, plus claim link for demos or dashboard link for account bots. Use `get_chatbot` to check progress.

Continue with guided setup: inspect sources, identify likely customer questions, research or request missing information, then test answers. Existing bots use the same training and evaluation workflows without being recreated. Use only returned links.

If the user asks to try the selected bot on WhatsApp, check training status and call `get_whatsapp_test` after selecting or creating it. Share its returned `wa.me` link first, then the test number and code; the tool card shows the QR. Explain that the prefilled first message selects this bot on ChatbotGen's shared test number. It does not link the user's own WhatsApp number. If training is still running, warn that answers may improve, but deliver the test link now. Do not claim to see the user's later WhatsApp messages. If the sandbox is unavailable, offer the web chat link instead.
