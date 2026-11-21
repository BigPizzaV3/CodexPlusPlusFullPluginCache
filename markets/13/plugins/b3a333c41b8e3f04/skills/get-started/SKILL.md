---
name: get-started
description: Get started with ChatbotGen agents for websites, WhatsApp, Instagram, Messenger and Telegram. Create or select an agent, improve its answers and guide channel setup.
---

Help the user get a useful chatbot with minimal repeated questions.

Prioritize the user's immediate goal. If they ask to try WhatsApp, select the bot and provide its real test link first; do not require a knowledge audit or a long setup questionnaire.

## Connect the channels the business uses

ChatbotGen agents can answer on WhatsApp, Instagram, Messenger, Telegram and websites using the same business knowledge. Ask which channels matter when that helps choose the next setup step.

Use the chatbot's returned `dashboard_url` to guide channel setup in ChatbotGen. The owner connects their own WhatsApp number, professional Instagram account, Facebook Page for Messenger or Telegram bot there, and adds the website widget from the dashboard. Only describe a channel as connected when there is evidence of that connection. Never invent settings links or claim the assistant has linked an account.

`create_chatbot` requires a public website URL as the initial content source. If the business has no website, guide the owner to create an agent in the ChatbotGen dashboard with their files or business text, then connect their account and select it. A requested messaging channel is a deployment choice; use the website to train the agent when available.

Use `get_whatsapp_test` for the shared WhatsApp test number. Keep that test separate from connecting the owner's own number. Describe the customer's WhatsApp connection as the official WhatsApp Business Platform, with Meta's messaging rules applying. Never claim that ChatbotGen is a direct Meta partner or name its onboarding provider.

## Select the chatbot first

Use the active chatbot from this conversation unless the user names another or asks to create a new one. For an existing chatbot without an active selection, call `list_chatbots`; match the name and website, or show the choices if ambiguous. Connect the account when prompted. Never create a new chatbot as a substitute for finding an existing one. If listing is unavailable, explain that account connection is needed; do not guess IDs.

State the selected name and website briefly, keep its ID for subsequent calls, and switch only when requested. A newly created chatbot becomes the active selection. Demo tokens work until expiry or claim, and only while no account is connected. If the user connects while working on a demo, tell them which chatbot it is, ask whether to keep it in their account, and after a yes call `claim_chatbot` with its token and `confirmed: true`; use the returned `chatbot_id` from then on. Never create a replacement for a demo: it can use up the account's only chatbot slot. If they keep it through the claim link instead, list the account's bots. Do not assume selection persists into a new conversation. Keep test-session state tied to the selected chatbot, scenario and language; switching bots clears the previous test conversation ID. Start a fresh scenario with necessary context when the user asks the same follow-up on a different bot.

For a new bot, get the website and call `create_chatbot`. Make the returned chat link ("Try your chatbot") the primary next action. Keep the embed snippet and demo claim link or account dashboard link available as secondary options; do not make installation or signup a prerequisite for seeing value. Explain background training and any returned limits.

For either new or existing bots, inspect `get_chatbot` and `list_knowledge`. Establish the intended audience and purpose from context; ask only what is missing. Check the essential topics for that business: offerings, prices, eligibility, hours/service area, buying or booking steps, policies, and reaching a human. Ask at most a few related questions at a time. Do not demand a questionnaire before making progress.

Use the train-chatbot workflow for gaps and evaluate-chatbot for answers. When the user wants the bot to do things for customers (check orders, start returns, answer account questions, open tickets) or to send leads to other tools, use connect-integrations. Offer the next concrete improvement based on evidence. Do not describe queued training as completed or a bot as ready based on status alone.

While training is pending, say what is being read and identify one consequential missing business fact from available sources. After training settles, demonstrate one useful customer answer, within the remaining allowance, before suggesting a larger audit. Respect explicit requests not to test or spend messages.

After a demonstrated success, offer one relevant next step: try another customer question, connect a chosen channel in the dashboard, or keep the demo, with `claim_chatbot` once their account is connected or its returned claim link otherwise. At a limit, summarize what already works and what remains unverified, then explain the specific account/plan step once. Claiming retains the same bot and knowledge; it is not a promise of free or unlimited capacity. Do not repeat upgrade pitches, manufacture urgency, or describe untested business outcomes.

When the user wants to try the selected chatbot from their own WhatsApp, check `get_chatbot` and call `get_whatsapp_test` with its current ID or demo token and the user's language. Give the returned `wa.me` link first because it works on the same phone, then the test number and code; the tool card displays a scannable QR for another device. Tell them to send the prefilled first message, then ask one real customer question. If training is pending, explain that answers may improve without delaying the link. This uses ChatbotGen's shared test number and does not connect their own number. WhatsApp answers use the bot's message allowance. The MCP does not show the assistant what the person later sends on WhatsApp, so do not claim to have observed that chat. After they report a useful test, offer one next step: keep the same demo bot in their account, or open the account dashboard to learn how to use their own number. Do not promote plans or checkout in ChatGPT. If the tool says the test number is unavailable, use the web chat link; never invent a number or code.
