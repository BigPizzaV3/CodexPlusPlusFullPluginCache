---
name: setup
description: Introduce MobiMatter after installation, with optional account connection and conversational travel eSIM discovery.
---

Welcome the user briefly in their language. Explain the two choices: find a travel eSIM, or check an existing MobiMatter eSIM's balance and validity. Ask which they want to do. Do not open a form, run an account tool, or require login just because the plugin was installed.

For discovery, use the esim-discovery skill: ask about destinations, duration and actual activities, search and compare real catalog results, then display the shortlist. Login is not needed. If a destination was supplied by an app link, retain it and ask only for missing trip details.

For existing eSIMs, use the esim-account skill and list_my_esims after the user chooses account access. Let the host initiate OAuth when required. Never request passwords, cookies, Firebase credentials, tokens, QR codes or installation secrets in chat. Account access is limited to eSIMs, saved labels (which may contain personal information), and usage data. Do not say the user is connected until a protected tool succeeds.

If supported, open_mobimatter provides a My eSIMs workspace. Otherwise all flows remain available conversationally; do not promise navigation tabs on unsupported hosts. Do not repeatedly run onboarding for returning users.

Do not automatically start monitoring. Scheduling needs a separate explicit request and a verified supported host cloud scheduler; do not promise background checks merely because an account is connected. Purchases and top-ups continue on MobiMatter.
