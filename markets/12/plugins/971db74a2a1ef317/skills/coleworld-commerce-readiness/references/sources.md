# Primary sources and eligibility snapshot

Checked 2026-10-16. Recheck before giving a current eligibility decision.

- [OpenAI plugin checkout](https://developers.openai.com/plugins/build/monetization): at this check, general guidance supports external checkout for eligible physical goods; ChatGPT payment-sheet access is limited to selected partners. External hosting alone does not establish eligibility for digital goods or subscriptions.
- [OpenAI commerce](https://developers.openai.com/commerce): a separate commerce integration route whose onboarding and capabilities must be verified, not assumed from plugin installation.
- [Stripe fulfillment](https://docs.stripe.com/checkout/fulfillment.md?payment-ui=stripe-hosted): verify payment and implement reliable fulfillment instead of trusting only a success redirect.
- [Stripe webhooks](https://docs.stripe.com/webhooks): signature verification, duplicate events, ordering and retry handling.

A merchant website can be assessed independently, but do not advertise a blocked ChatGPT purchase path as approved merely because its billing works on the website. Record product category, surface, current rule, and actual account capability separately.
