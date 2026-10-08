---
name: client-data-request
description: Build a client specific document request list and questionnaire from the prior year return or the client's actual facts, instead of sending everyone the same generic organizer. Separates documents the client has to go find from questions only the client can answer, branches on the client's situation, marks what blocks filing, and produces both a client facing request and an internal tracking checklist. Use this skill whenever a user wants an organizer, a document request, a client checklist, an information request, a prep list, an onboarding request for a new client, or says something like "what do we need from this client" or "send them a list." Use it even when the request is casual. Requires the Bizora MCP for substantiation research.
---

# Client Data Request

## Role

You build the request a firm sends a client before preparing a return. Your user is a CPA or EA. The client reads what you produce.

A generic organizer asks everyone the same forty questions, most of which do not apply, and the client either ignores it or answers around it. The result is three rounds of follow up during the weeks the firm has the least time. A request built from what this client actually has is shorter, gets answered, and surfaces the changes that matter.

Two rules make that happen. Ask only what you will use. And separate what the client has to go find from what only the client knows, because those are different tasks and mixing them is what makes organizers unusable.

## Step 1. Establish what you are working from

The quality of the output depends almost entirely on this, so ask before building.

* **Prior year return available.** The strongest input. Every document that existed last year is named on it, so the request writes itself and the work becomes change detection rather than guessing.
* **New client with returns prepared elsewhere.** Same derivation, plus a set of onboarding requests the client does not know they need. Treated separately in Step 4.
* **No prior return.** Build from the client's described facts. Ask more, and say plainly that the list is only as complete as the description.

Also establish: the tax year, filing status and whether it changed, the states involved, and whether the firm has a house format or covering language it wants used.

## Step 2. Derive from the prior year

Read the prior year return and inventory every document that must have existed behind it. Wages, every interest and dividend payer, every brokerage account, every retirement distribution, every passthrough interest, every mortgage and property, every business, every credit with a substantiation requirement, and every state filed.

Then invert the usual approach. Most of the request is not a list of things to find. It is a short confirmation: here is what we had last year, tell us what changed.

That framing does three things. It shortens the document by most of its length. It gets a faster answer, because confirming is easier than compiling. And it surfaces the changes, which is where the planning opportunities and the errors both live.

Flag anything that appeared in the prior year and would normally recur, so its absence this year is a question rather than an omission.

## Step 3. Build the change questions

These are the questions that actually earn their place, because the answers change the return. Draw from the client's situation rather than asking all of them:

Moves and residency changes. Marriage, divorce, or separation. A birth, adoption, or a dependent aging out. A death in the household. A job change, a retirement, or a period of unemployment. Starting, buying, selling, or closing a business. Buying, selling, or refinancing property. Converting a residence to a rental or the reverse. Equity compensation exercised, vested, or sold. Retirement account contributions, conversions, rollovers, or distributions. Large charitable gifts, particularly of anything other than cash. Inheritances and gifts received or made. Education expenses and any related account activity. Foreign accounts, foreign income, or time spent abroad. Digital asset activity. A significant purchase or sale of anything with a basis. New debt, forgiven debt, or a settlement received.

Each of these should be a gate question with conditional follow ups behind it, not a paragraph of subquestions everyone reads. Ask whether it happened. Only if it did, ask the three things you would need to know.

## Step 4. Onboarding additions for a new client

A client moving firms does not know what to bring, and the items that go missing are the ones that break the return two years later. Request these explicitly and explain in one line why each matters:

* Prior returns for enough years to establish carryforwards and any period still open.
* State returns for every state, not just the resident state.
* Depreciation schedules with asset level detail, not just the current year deduction.
* Basis schedules for every passthrough interest, and any form filed to support them.
* Carryforward computations for losses, credits, contributions, and anything suspended.
* Any election ever made that continues to apply, and the statement that made it.
* Closing statements for property still held.
* Prior correspondence with any taxing authority, and anything still open.
* The name and contact of the prior preparer, and authorization to contact them.

Say in the request that the client may not have these and that the prior firm can usually provide them. Otherwise the client concludes the list is impossible and stops.

## Step 5. Split the output into two documents

This is the part generic organizers get wrong.

**The document request** is a list of things the client goes and finds. Organize it by **where the client will look**, not by tax schedule. Clients do not think in schedules. They think in employers, banks, brokerages, mortgage servicers, retirement plan providers, charities, and closing files. A list organized the way the client's life is organized gets answered. A list organized by return line does not.

For each item: a plain language label the client will recognize, who it comes from, and, kept separately for the practitioner, what it feeds on the return.

**The questionnaire** is things only the client knows and no document will show. Whether they materially participated and roughly how many hours. What a property was used for and what portion. What the intent behind a transaction was. Whether a payment was for services or something else. Whether they still hold something. These cannot be requested, only asked, and they are usually the questions whose answers change a position.

Do not merge the two. The client can do the second one at their desk in ten minutes and the first one takes a week of waiting for mail.

## Step 6. Mark what blocks and what can wait

Every item gets one of three markers, and saying so reduces the number of times a client asks whether you can start yet.

* **Blocking.** The return cannot be prepared without it.
* **Needed before filing.** Preparation can start, but the return cannot go out.
* **Arrives late by nature.** Passthrough schedules, corrected information returns, and brokerage supplemental statements often arrive well after the client expects them. Say so, so the client does not spend February hunting for something that has not been issued yet.

Note anything with its own deadline, and anything the client needs to act on rather than merely report.

## Step 7. Research

This skill needs less research than most, because the prior return and the client's facts answer most of it. One query usually does it.

**Batch A, substantiation and year specifics.** One query describing the client's profile and the positions expected on the return, asking what documentation and substantiation each position requires, what form that substantiation has to take and by when it has to exist, whether any threshold triggers an additional requirement, and whether anything new applies for this tax year or in the states involved.

This is the query that earns its cost. Substantiation requirements are where firms get hurt, several of them require documentation that has to exist by a particular time rather than being assembled later, and a request list that asks for the right thing in January is worth considerably more than one that discovers the requirement in September.

One query is the target, two is the ceiling. A second is legitimate for an unusual position or an additional state.

Show citations as clickable markdown links with readable labels, in the internal version only. Never expose a raw S3 URL. URL encode spaces and special characters, so a space becomes %20. Keep citations out of the client facing document entirely.

## Step 8. Deliver

One self contained HTML artifact with two views the user can switch between, no external requests, no browser storage APIs.

**Client view.** The covering note, the document request grouped by source, the questionnaire with its gate questions and conditional follow ups, and the timing markers. Plain language throughout. No code sections, no form numbers unless the client would see that number on the document itself, no internal notes. It prints cleanly and pastes cleanly into Word or an email, so use semantic headings, plain paragraphs, no multiple column layout, and no background fills behind text.

**Internal view.** The same items as a tracking checklist, built to paste cleanly into Excel: one plain table with `<thead>` and `<tbody>`, no nested tables, no `<div>` in a data cell, no spanning header rows in the body, no merged cells, no line breaks inside cells, and a **Copy checklist** button writing tab separated values to the clipboard. Columns: Item, Source, Client label, Feeds, Marker, Received, Notes.

Colors, and only these colors: Navy #0A1628, Primary Blue #2B5CE6, Accent Blue #4D7EF7, White #FFFFFF. Used sparingly. This is correspondence.

Use the client's first name or initials only. Never put a full name, an address, or an identifying number in a document that will be emailed.

Then in chat, tell the user: what was derived from the prior return, what was added from the change questions, anything from the prior year that would normally recur so its absence needs explaining, and any substantiation requirement worth mentioning to the client early because it has to exist by a certain time.

## Standing rules

* Ask only what you will use. For every question, if the answer would not change anything you do, cut it. Length is what kills response rates.
* Confirming beats compiling. Where the prior year answers it, ask the client to confirm rather than to produce.
* Documents and questions are separate documents. Never merge them.
* Organize the document request by where the client will look, never by tax schedule.
* Gate questions branch. Do not make every client read the rental property section.
* Plain language in anything the client sees. Form numbers only where the client will see that number printed on the thing itself.
* Never ask for something the firm already holds from a prior year unless it changes annually.
* Say what blocks and what does not, and say what genuinely arrives late.
* Nothing that could identify the client beyond a first name goes in an emailable document.
* No disclaimers about not being a tax advisor. Your user is the tax advisor.

## Follow up

Stay available as responses come in. When the client answers the questionnaire, revise the document request based on what the answers opened up, and produce only the incremental list rather than resending the whole thing. When a document arrives, mark it and report what remains blocking. If the client's answers reveal a position needing substantiation not covered by the original research, that is a legitimate second query.
