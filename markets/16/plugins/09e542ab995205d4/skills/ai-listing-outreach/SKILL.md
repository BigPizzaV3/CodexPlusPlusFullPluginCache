---
name: "ai-listing-outreach"
description: "Pick the cited pages that a business must get on first, and write a first message for each."
---

# AI listing outreach

Use this guidance to turn the Sources tab into a short outreach list. AI apps cite lists, reviews, and directories when they answer buyers. A business that those pages do not list is easy to leave out.

## Steps

1. Call `get_sources` for the project and the scan in the request.
2. Read `pages_to_get_on` and `reach`. Each page has a listing state in `you`: Present, Not present, or Check needed.
3. Keep only the pages where `you` is **Not present**. A page with Check needed is not confirmed. List those apart under "Check these first". Never tell the person to get listed on a page that is not confirmed.
4. Rank the pages that remain by Reach, then by how many answers cite them.
5. Sort each page into a type, and use the action for that type:

| Type | Action |
|---|---|
| Editorial list or review | Write to the author. Give specific facts that help their readers. |
| Directory or marketplace | Identify the listing page and prepare listing text for the person to submit. Keep the name, address, phone, and services accurate. |
| Community thread | Read the bundled `../community-replies/SKILL.md` and follow its rules. |
| A rival's or vendor's own site | Skip it. You cannot get on it. |

6. Find the right target. For a list, it is the author or the editor. For a directory, it is the category page or the signup page. It is never a rival's profile page.
7. Draft the first message for each page. Do not send messages, claim listings, or submit listings.

## The first message

- 80 words or fewer. One request.
- Say who the sender is and their real role.
- Name the page, and show that you read it.
- Give one specific, true fact that the page does not have and its readers can use.
- Ask to be considered for the list. Do not ask for a link.
- Offer nothing in return. No payment, no link exchange, no review trade.

## Never suggest

- Paid links, link schemes, or private blog networks.
- Fake reviews, or requests for reviews where the platform forbids them.
- Keywords or locations added to a business name, fake listings, or details that are not accurate.
- Any promise of a citation, a ranking, or a result. No method is proven to earn a citation. Each message is a bet that the data supports.

## Rules

- Use host browsing to read each target page. The Frontmost AI MCP does not provide public-page browsing. If browsing is unavailable, request the page text. Do not claim that you read an unavailable page. Leave its current state unverified.

- Copy each number from the data. Report it with its counts.
- `checked_on` is the day of the listing check. Say it when it is more than 7 days old.
- Link the `url` of the Sources tab.

## Output

A table of up to 10 pages: the page, why it is on the list (Reach, citing answers, the rivals that it lists), the type, the action, and the first message. Then the "Check these first" list.
