---
name: event-outbound
description: Plan outreach around a conference or trade show - pick or add the event, list its published speakers, exhibitors and sponsors, match their companies to target accounts, and plan Event touches a person approves in Today.
---

# Event outbound

"Plan outreach around this conference." An event is a reason to meet in person: a target account's people are speaking, exhibiting or attending, and a short note before the event books a coffee or a booth visit. In Kenso each event holds its list of attendees, exhibitors, speakers and sponsors, and every row is matched to your target accounts by company domain.

Events have no tool in this app: the user adds the event, builds its list, plans the touches and imports people into a campaign in Kenso, under Accounts > Events (`https://app.ken.so/<workspace id>/demo/accounts/events`). You bring the judgement: which event, which of the user's target companies take part, what the list is missing, and what the note before the event says. The tools here help with two reads: the business roles at the exhibiting and sponsoring companies in Kenso Search, and replies in the inbox that name the event.

The list comes from what the event publishes (its speaker, exhibitor and sponsor pages) and from lists the user has the right to use. This guide never reads LinkedIn or another site's member or attendee lists, and never guesses where a person will be.

## Rules

- **A person approves every touch and launches every campaign.** Planned touches wait in Today; nothing here sends.
- **Write only what is public.** Name a person's part in the event only when the event published it ("Maya speaks at RevOps Summit on Nov 18") or they told the user themselves. Someone at an exhibiting company may not go: write "your team is exhibiting at <event>", never "saw you're attending".
- **Business contacts only.** Use a person's name, business title, company and work contact, nothing more. Honor opt-outs: someone who asks not to be contacted goes on the blocklist.
- **Delete only on request.** Removing an event, a row or a suggestion is the user's call.
- **Never invent** a booth number, a session time, a venue or a meeting slot. Use what the event page or the person gave you.
- Adding event people to a client's live campaign is a volume change: it needs a yes that names that client, with its source.

## Step 0 - Check what is on

Event outbound needs the Accounts and Event outbound flags. If `https://app.ken.so/<workspace id>/demo/accounts/events` does not open for the user, tell them in one sentence that Event outbound is not switched on for their workspace yet, and stop.

## Step 1 - Pick the event

The user opens `https://app.ken.so/<workspace id>/demo/accounts/events`:

- The table lists the workspace's events with their dates, city and how many target accounts are on each list. The Going and Suggested chips narrow it: a Suggested row is an event Kenso found for them, with its relevance and the target accounts seen on it.
- A new event: New event. Paste the event's link (Luma, Eventbrite, Sched or its own site) into Event link and click Fill from link, then fill what it left blank: Name, Start date, End date, Timezone, Format, City and Venue. Never invent one: ask the user.

Help them pick: an event where several target accounts speak, exhibit or attend beats a bigger one with none.

Ask whether the team is going: it changes the touches (meet in person, or follow up on the talks). They set it in Attending on the event.

## Step 2 - Build the list

Add rows from what the event publishes first. On the event's page (`https://app.ken.so/<workspace id>/demo/accounts/events/<event id>`), Add people has From a link, Paste a list, Upload a file, One person and Find with Ken.

**The event's own pages.** The speaker, exhibitor and sponsor pages: From a link reads one, with its Role. A sponsorship prospectus or "who attends" page names the companies, the job titles attendees hold and how many attend: keep those titles for Find with Ken. When a page is closed to the reader, the user pastes its text here: turn it into rows (full name, title, company, company domain, role) for Paste a list. Never add a row the page does not show.

**A list file the user has.** A CSV, an Excel sheet or a PDF, such as the exhibitor list the organizer sent. Ask whether they have permission to use the list for outreach; without it, leave the list out. They add it with Upload a file. A CSV or sheet maps its columns by name; a PDF is read by a model and can be misread, so they check its rows before adding them.

**Find with Kenso.** In Find with Ken, use People at the companies: the people who hold the right business roles at the exhibiting and sponsoring companies, by Job titles and Per company. Use the prospectus titles when you have them. They work there and may not go, so the note is about their company's part in the event. Last year's published speakers, sponsors and exhibitors help pick companies; companies come back more often than people.

Here you can check either side yourself: `list_inbox_threads(q="RevOps Summit", limit=20)` finds replies in the user's own inbox that name the event, and for an exhibiting company, `search_companies(body={"website": "acme.com", "page": 1, "pageSize": 1})`, then `search_people_at_companies(account_ids=[123456], current_titles=["VP Sales", "Head of Partnerships"])` shows who holds those titles there. The people search counts each profile against the workspace's Search browse quota.



## Step 3 - Match the list to your accounts

The event's page matches every row to the workspace's target accounts by company domain, and shows which rows are on a target account.

- An attendee who is on an account but not on its buying committee: suggest adding them to the committee on the account's page.
- A company on the list that should be a target account: suggest it to the user; they add it in Accounts on their yes.
- The rows that match no account are the campaign list (Step 5).

## Step 4 - Plan the touches

On the event's page, Plan Event touches.

It plans one Event touch per target account on the list ("Meet at <event>"), to the person on the list who is a stakeholder (speakers first), with a body naming the event, its dates and city and that account's people on the list. The touches wait for approval in Today. The default due time is 09:00 UTC fourteen days before the event.

- An account that already has this event's touch gets no second one, so it is safe to plan again after adding rows.
- Accounts whose stage is paused, not a fit or lost are left out, and so is one a Contact limits rule blocks.
- Speakers on the list also become event signals on their accounts.
- A past event cannot plan touches.

For a written email before the event, write it here with the user: name the event, its dates and city, and that person's part in it ("Maya speaks at RevOps Summit on Nov 18"), and ask for a coffee or a booth visit without inventing a slot. They add it as a touch on the account in Kenso, and approve it in Today: `https://app.ken.so/<workspace id>/today`.

## Step 5 - People not on an account

Rows whose company is not a target account can go into a campaign. Build or reuse a Draft campaign with copy about the event in Kenso (https://app.ken.so/<workspace id>/campaigns), then, on the event's page, Add to campaign, with the roles to import and the Campaign.

Rows with an email or a LinkedIn URL become contacts, at most 5,000. Rows on target accounts are left out, because the Accounts lane works them. A person launches the campaign.

## Step 6 - After the event

- Update the event with what changed: Attending on the event's page.
- Follow up on the people you met with the `accounts` skill, and on replies with the inbox.

Report: the event, the list by role and source, the target accounts on it, the touches waiting in Today, anything imported into a campaign, and what the person has to approve.

## What this skill cannot do yet

- Tell whether a person at an exhibiting company is going: write about their company's part in the event instead.
- Read LinkedIn or any other site's attendee lists.
