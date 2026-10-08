# MailRambo for ChatGPT — local candidate 0.1.0

**Not published, not submitted and not yet usable as a live ChatGPT plugin.** This is the customer-only candidate package for the current ChatGPT Plugins system. Its declared service URL is planned on the existing MailRambo domain; the endpoint has not been registered or deployed. Do not upload it as a working service until hosting eligibility, deployment, domain verification and actual conversation tests are complete.

Intended flow: install MailRambo → securely link an existing MailRambo account → ask for screening, requested full verification, or your balance. No shared publisher API key, new customer database or separate billing system.

- Screening is real local/DNS screening and uses no verification credit. A passed screen has `deliverable: null`, not a confirmed mailbox.
- Full checks preserve existing MailRambo credits, refunds, caching and strict catch-all semantics. Customer consent on MailRambo sets a persistent limit of 0–10 attempts for a 30-day link; default 0 blocks full checks. The limit counts free/cached results and failures too, and refresh does not reset it. Attempts are not a credit pack or purchase.
- There is no email sending, contact discovery, payment or plan-change tool. Results cannot prove identity, ownership or consent.

The displayed public publisher name will come from the selected verified individual developer identity in OpenAI's portal; the brand metadata is not a company-verification claim.

This package contains no reviewer credentials, secrets, private research, repository history or customer contacts. Private reviewer access, five positive/three negative conversation cases and a real walkthrough remain required. Local mocked protocol tests are not ChatGPT acceptance tests.

Support: [developer documentation and contact](https://www.mailrambo.com/developers), hello@mailrambo.com. [Privacy](https://www.mailrambo.com/privacy) · [Terms](https://www.mailrambo.com/terms).
