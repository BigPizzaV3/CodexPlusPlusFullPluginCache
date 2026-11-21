---
name: accounts
description: Run the Accounts loop - add target accounts, research them, map the buying committee, scan signals, plan touches that a person approves in Today, and hand an account to a teammate.
---

# Accounts

Accounts is the 1:1 lane in Kenso: a short list of target companies, each worked by hand with touches to the people who buy. An account has its domains, a stage, an owner, a research dossier, a buying committee (stakeholders and open seats), signals and touches. Today in Kenso is where a person approves what goes out.

Accounts has no tool in this app: you cannot add, research, map, scan or plan an account, or create, approve or send a touch here. The user does each of those in Accounts, at `https://app.ken.so/<workspace id>/demo/accounts`. What you can do here: check a company's fit and research it in Kenso Search, check its signals, suggest who belongs on its buying committee, and write and grade touches, each with its source.

## The rule: a person approves every touch

You write touches. A person adds and approves them, in Kenso. Never say a touch is approved or sent because you wrote it.

- A touch with a body waits for approval until a person clicks Approve in Today. A touch an agent created always waits for a person, whatever the workspace's agent settings say.
- Never tell the user a touch was sent or approved because you created it. Say it is waiting for their approval in Today, and when it is due.
- Never invent a price, a meeting time or an offer in a touch. Use what Knowledge, the research or the user gave you, with its source.

Every tool here takes `workspace_id`. Send it on every call when the user can see more than one workspace (`list_workspaces()` lists them).

## Step 0 - Check what is on

Accounts is in beta. If `https://app.ken.so/<workspace id>/demo/accounts` does not open for the user, Accounts is not switched on for them yet: say so in one sentence, and stop. Research, committee mapping, signals, the touch plan, Kenso writing touches and hand-offs each sit behind their own flag: when a step's button is missing on the account's page, that part is not on for them yet. Skip it, say so, and carry on.

## Step 1 - Know what the workspace sells

Ask the user for the ICP, the offer, the proof points and their writing style, or to paste the Knowledge files that hold them (`https://app.ken.so/<workspace id>/demo/knowledge`). Use them to judge fit and to write in the workspace's voice, and cite what they give you.

## Step 2 - Add the accounts

The user adds them in Accounts with Add accounts, by domain; Kenso names each account from Kenso Search, and a domain another account owns is refused. Help them pick first: find each company (`search_companies(body={"website": "acme.com", "page": 1, "pageSize": 1})`) and say in one line whether it fits the ICP, and why.

- To set an account aside, its stage goes to Paused or Not a fit. Kenso plans and drafts no touch for a lost, paused or not-a-fit account.
- Delete and merge cannot be undone: only when the user asks.

## Step 3 - Research each account

When research is on, a new account starts its research run by itself, and the account's page shows the dossier: why now, angle, fit score, pains, stack and facts, each with its source. A run costs credits: before research runs on more than a few accounts, tell the user what it costs.

Add to it here, for free: `get_search_company(company_id=...)` (the id from Step 2) for size, industry, description and recent changes. Every fact you add names its source.

## Step 4 - Map the buying committee

The account's page holds the committee: Map people asks Kenso to map it (charged), and Add person adds one person. Here, find candidates with the company's Kenso Search id:

`search_people_at_companies(account_ids=[123456], current_titles=["vp revenue operations", "head of sales", "cro"])`

For a LinkedIn profile the user has, `lookup_person_by_linkedin_url(linked_in_url="https://www.linkedin.com/in/mayachen")`. Suggest each person with name, title, a role (champion, economic buyer, approver, evaluator, user, executive sponsor, blocker) and the source that places them there; never suggest a person with no source. The user adds the ones they keep with Add person. A person with no email cannot get an email touch.

## Step 5 - Check the signals

The account's page shows its stored signals, score and tier. Here, check the company's newest changes yourself:

- Funding: `search_funding_rounds(body={"companies": {"include": ["acme.com"]}, "reportedWithinDays": 180, "limit": 10})`.
- Hiring: `search_job_postings(body={"companies": {"include": ["acme.com"]}, "postedWithin": 30, "limit": 25})`.

Report per account: the new signals with their dates and sources, and the touch each one suggests.

What a signal means:

- A signal is the best reason for a touch. Give a touch it prompts `reason="signal"` and name the signal in the rationale.
- A funding round is not a buying event by itself. The money pays for a plan (hiring, a new market, a launch): write about that plan to the person who runs it, never "congrats on the raise".
- A job change of a known stakeholder is a new door: the person at their new company, and a gap on the old account's committee.

## Step 6 - Plan and write touches

Kenso's plan for an account is Start plan on its page: it places planned touches across the people it can reach (up to 9 over 90 days, or what the account's tier allows), and Kenso can write each one. A plan marked thin needs more people on the committee.

Your own touch: write it with the user, for one stakeholder on one channel (email, LinkedIn connect or message, call), with its reason and source in one line. That line is the rationale the person approving reads ("Acme is hiring three AEs for EMEA (careers page, Oct 14), paid for by its Series B. The touch is about ramping them, not the round.").

Check the copy before you hand it over: `grade_email_copy(subject_key="acme-maya-email-1", copy="...", channel="email")` grades it (`linkedin_connection` or `linkedin_message` for LinkedIn), and for an email `check_email_copy(subject="...", body="...")` checks it against the copy rules in code.

The user adds it as a touch on the account in Kenso. With a body it waits for approval; a Contact limits rule can refuse a due time and name the first one that passes.

## Step 7 - Hand over to a person

Send the user to Today in Kenso: `https://app.ken.so/<workspace id>/today`. Every touch is approved there, by their own click.

## Hand an account to a teammate

When an account is ready for someone else (a meeting booked, an AE taking over) and the user asks for the hand-off, they use Hand off on the account's page. It messages the teammate, so it goes only on the user's yes; help them write what the teammate needs: fit, why now, the engaged and planned stakeholders, roles not mapped yet, the last conversation and the angle.

## After a person approves

- An approved touch sends from the account's Sends from inbox or LinkedIn account when it is due. Retrying a failed send is the person's button.
- Snoozing, skipping and deleting a touch are the person's buttons too, in Today or on the account.
- A reply pauses the account's plan. Resuming or ending it is the user's call, on the account's page.

## Who did what

Every write a person makes in Kenso is recorded as theirs. A touch an agent created always waits for a person.

## Credits and errors

Adding accounts and grading a touch are free. Research runs, mapping runs, touch plans and Kenso drafts are charged, and an email find costs 1 credit per email found. Before research or mapping runs on more than a few accounts, tell the user what it costs.
