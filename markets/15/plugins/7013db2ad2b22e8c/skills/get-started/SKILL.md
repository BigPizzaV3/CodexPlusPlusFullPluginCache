---
name: get-started
description: Get a new Dalton user oriented right after they connect. Confirm the connection, show the accounts they can open, and suggest a first question about their store's analytics or A/B tests. Use when the user has just installed Dalton, asks what Dalton can do, or asks how to start.
---

# Get started with Dalton

Dalton is A/B testing for online stores. Through this plugin the user can read their store's analytics and test results and have you draft new A/B tests. You act as them and see only the accounts they're a member of.

## Steps

1. Call `whoami`. It confirms the connection and lists the accounts (customers) the user can open, each with its `customer_id`. Every account-scoped tool takes that id.
   - One account: use it without asking.
   - Several: name them and ask which store to look at.
   - None: tell the user their login isn't a member of any Dalton account yet, and to ask whoever manages their store's Dalton account to add them.
2. Give the user a short overview of what they can ask:
   - **Analytics:** conversion rate, revenue, the funnel and its weakest step, traffic by channel or device, and which pages win or lose visitors.
   - **Experiments:** how each A/B test is doing, the winners now deployed, and what Dalton has learned across tests.
   - **Drafting:** a new A/B test on a page, or a copy of an existing one on other pages.
3. Offer one concrete first question, for example "How did my store convert over the last 30 days?", and run it if they agree (`get_site_totals`).

## Keep in mind

- Results stay hidden until every variant has enough traffic and the test's planned window has run. Say "too early to call", not "no result".
- You never launch, pause or deploy a test. Drafts are launched by the user in the Dalton app, or with the Launch button in the experiment view.
- Before proposing a new test, read `get_learnings` so you don't suggest what was already tried.
- If an account shows no rulesets or experiments while the user is sure it has them, the account may not be on Dalton's current platform yet. Offer to pass that on with `suggestion_box`.
