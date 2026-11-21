# Sample campaign for a prospect

Someone answered your outbound asking to see the work: "send the sample", "show me", "sure, build it", "what would this look like". This recipe keeps that promise. It builds a real sample campaign for the prospect, wraps it in a Studio page they can read and download, checks it, and leaves a draft reply with the link. Agencies run it to win their own clients; the same recipe sends each target in a list a sample.

Two rules hold on every path:

- **Their campaign, their buyers.** The sample sells the prospect's own product to the prospect's own buyers. Never build a campaign that sells your product, and never pick people who work at the prospect.
- **Nothing sends.** The reply is a draft a person reads and sends. The sample has no senders and no schedule.

Every tool here takes `workspace_id`. Studio and Accounts have no tool in this app: the account, its research, the page and its link are the user's steps in the app. You find the reply, check it, judge the page and write the draft.

## 1. Find the reply and the person

Find the thread: `list_inbox_threads(q="mitch@events.com")`, or by name. When a name matches more than one person, stop and ask which one, with company and campaign. Read the whole conversation with `list_thread_messages(thread_id="thr_...")`.

Write down: the thread id, the person (name, title, company, domain), the campaign it came from, and what your outreach promised, in its own words. The sample has to answer that promise.

## 2. Check it is a real ask

Read their words. Go on only when they ask to see something, ask how it works, or say yes. Stop and report instead on an out-of-office (it is not a reply), a bounce, an unsubscribe, a flat no, or a referral to a colleague (that is a new person and a new run: name them). Never build a sample on top of a rejection.

## 3. Make the prospect an account and research them

The user finds or adds the prospect in Accounts. Without Accounts, use the separate-workspace path in step 5.

Research is what makes the sample right about their business. The account's Research tab shows what exists; Refresh research there is charged (flag `accounts_research`), so say so first. What the user pastes from their site, and their company record in Search (`search_companies(body={"website": "events.com", "page": 1, "pageSize": 1})`, then `get_search_company(company_id=...)`), add to it. You need three things from a real source, quoted:

1. **Their buyers**: who they sell to, in their own words from their site.
2. **How they sell**: demo-led, self-serve or content-led. It decides what the sample's ask is.
3. **Hooks**: specific, checkable facts about the person and the company.

If you cannot name their buyers from a real source, stop and say exactly what is missing. Thin research is a stop, not something to paper over. A funding round is not a buying event: never build the sample's angle on it alone.

## 4. Build the sample page

Use the `rd-doc` starter (a doc with strategy, segments, a planning funnel, 8 to 10 real leads from Kenso Search and the first emails, downloadable as a PDF), or `rd-ken-native` for a lighter one-page version. Open its fill guide first (`references/rd-doc.md` or `references/rd-ken-native.md`): it lists what the page needs and why a page falls back.

1. Find the workspace's template in Studio, one made from `rd-doc` or `rd-ken-native`. With none, building one from the starter is the `studio-template` skill.
2. The user runs it on the one account: Create page from template on the account's Assets tab. It shows the credit estimate first: say the number, and run only on a yes.
3. When the fill ends, the account's Assets tab shows the page as Ready, Needs review or Failed.

## 5. Optional: the full campaign in a separate workspace

When the prospect asked for the campaign itself, not a page, build it for real where it cannot send:

1. A separate workspace for the prospect, never the workspace that sends your own outbound. This app cannot create one or set its plan: a person creates it in the app and checks it is on the Free plan, with no inboxes and no sending, before anything else happens there. Then pass its id as `workspace_id`.
2. Build the campaign in that workspace, aimed at the prospect's buyers: create it as a Draft with `create_campaign`, then the user builds its audience and copy on the campaign's page in the app. Never attach senders, set a schedule or launch.
3. Create an approval draft so they get an External approvals link to click through: `create_approval_draft(campaign_id=55, source="savedSearch", saved_search_id="ss_...", contact_limit=30)`. Read it with `get_approval_draft(approval_test_id=88)`; its link is ready when the draft is. A draft that is not ready is not a failure while its queue is still draining: record it and come back. Never write a reply that promises a sample that does not exist yet.

## 6. Gate the page before anyone sees it

The user opens the page (its card on the account's Assets tab) and pastes or describes it. Every check must pass:

- **Grade:** the page shows Ready. A Needs review page never goes out.
- **Filled:** every section shows real content, not the template's default text. On `rd-doc` only the hidden research fields and the offer paragraph may be empty.
- **Real numbers:** every number is real. The audience and lead counts come from what Kenso Search returned; the funnel is labeled as planning numbers; claims about the prospect's customers or results appear on their site word for word.
- **Confidentiality:** no email address or phone number of any lead (names and LinkedIn URLs prove the work; finding emails is the paid part), no other client's name, data or results, no vendor or tool names, and never "demo" or "reverse demo".
- **No poaching:** no lead works at the prospect itself, at your own company, or at one of your clients.
- **Read it:** once, top to bottom, on desktop and mobile.

There is no tool for the confidentiality and poaching checks: read what the user pastes, line by line. A page that fails one is refreshed once (Refresh on the page) or fixed by a person on its Customize screen; it is never linked as it is.

## 7. Link it and draft the reply

1. The user creates the person's link in the page's Links block (Create a link for) and pastes it here. The first link publishes the page and charges 1 credit. A doc page can also go out as a Google Doc or Word file with the `rd_docs` flag: Export on the page.
2. Check the thread for a draft first: `get_thread_draft(thread_id="thr_...")`. A draft a person wrote is theirs: do not replace it. Hand over the links in your summary instead.
3. Otherwise write the reply as a draft: `save_thread_draft(thread_id="thr_...", body="...")`. Short: thank them in their own terms, one line on what is in the sample, the link (and the External approvals link from step 5 when there is one), and one easy next step. No invented prices, times or offers. A person reads and sends it.

## 8. Report

In under 12 lines: who replied and what they said (quoted), which campaign it came from, the research sources, the page and its state, the gate results (leads kept, anything refilled or unresolved), the links, and that the reply is a draft waiting for a person to send. Name anything the draft promises that is not true yet.

## Stop and report instead of faking it

| When | Do |
|---|---|
| The reply is not a real ask | stop; say what it was |
| Research too thin to name their buyers | stop; say what is missing |
| The page fails the gate after one refill | stop; no link, no draft that promises a sample |
| Their buyers sit outside Kenso Search's countries (United States, United Kingdom, Canada, Australia, Ireland, New Zealand) | the leads will be empty: say so before you run |
| A person's draft is already on the thread | leave it; hand over the links |
