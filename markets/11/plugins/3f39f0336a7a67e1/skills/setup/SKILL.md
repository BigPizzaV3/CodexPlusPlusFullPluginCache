---
name: setup
description: Connect your Shaupa account, understand the granted capabilities and check your current limits.
---

Use the host's normal Shaupa connection flow. The person signs in or creates
an account on Shaupa and chooses permissions. Never request passwords, Firebase
tokens, OAuth codes or cookies in chat. Never invent an authorization URL.

When available, call `shaupa_get_account_context` to learn the current account's
limits and connection link. Tools reflect the granted scopes. If a permission is
missing, explain that the person can reconnect with that permission through the
host. Do not claim that connecting changes a subscription or limit.

Explain the available workflows briefly: catalog search and product facts,
private saved products and boards, and reading existing canvases. Retailer links
may be affiliate links. Catalog stock, currency, price freshness, delivery and
size are known only when returned; the retailer is the source for checkout.

Nothing is purchased, published, deleted or created by setup. For disconnect,
use the host controls or the exact connection URL returned by Shaupa. Revoking
a grant does not remove the person's existing saved work.
