---
name: check-canadian-citizenship
description: Help someone find out whether they or their child could be a Canadian citizen through a parent, grandparent or earlier ancestor, using the check_citizenship_by_descent tool, and connect them with a lawyer if they ask.
---

# Check Canadian citizenship by descent

Use this when someone asks whether they, or their child, could be Canadian through family (for example "my grandmother was born in Quebec, am I Canadian?").

## 1. Map the direct line

Build the line from the Canadian ancestor down to the person being checked. Every step must be a parent-to-child link.

- Ask who the Canadian ancestor is and how each generation connects down to the user.
- A cousin, aunt, uncle, sibling or spouse is not part of the line. If the Canadian connection came through one of them, find the ancestor the user shares with them, then follow the user's own branch.
- If the user is checking their child, end the line with the child and set `checkingFor` to `child`.

## 2. Ask for the essential facts, briefly

Ask in plain language, a few at a time:

- For each person: year of birth and whether they were born in Canada.
- For the ancestor: how they were Canadian (born in Canada, naturalized in Canada and roughly when, already Canadian through their own parent, or only a family story).
- For each link: is it a biological parent? (A legal parent at birth also counts; an adoption after birth or a step-parent is different.)
- Once for the whole line: did anyone renounce Canadian citizenship, have it revoked, lose it and get it back, or get born in Canada to a foreign diplomat?
- Only for a birth outside Canada on or after 15 December 2025: before that birth, had the Canadian parent spent at least 1,095 days in Canada?

If the user does not know something, mark it `unknown` or leave it out. Never guess or fill in a likely answer. Unknown facts become "facts to establish" in the result.

## 3. Screen and explain

Call `check_citizenship_by_descent`. Then:

- Explain the result in a sentence or two, and the first fact that could change it.
- Point to the document checklist in the card.
- Always present it as a screening, not legal advice or proof of citizenship. Never tell someone they are, or are not, a citizen.

## 4. Lawyer review (only if the user asks)

If the result offers a consultation and the user wants a lawyer to review it:

1. Ask for their full name, email, which country they live in (United States, Canada, United Kingdom or other), an optional phone number, and anything they want the lawyer to know.
2. Tell them their contact details and family-line answers will be shared with Cohen Immigration Law, who will contact them by email, phone or text message. Ask them to confirm.
3. Only after they confirm, call `request_lawyer_review` with the same line and `userAgreedToShare: true`.

Do not ask for passport numbers, government ID numbers or document scans.
