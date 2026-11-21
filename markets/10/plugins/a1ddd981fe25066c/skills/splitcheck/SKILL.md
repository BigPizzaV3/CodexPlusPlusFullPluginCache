---
name: splitcheck
description: Split a bill or receipt between people and save it to a SplitCheck group, create a group with an invite link, or check who owes whom. Use when the user wants to split, share or track group expenses, or mentions SplitCheck.
---

SplitCheck keeps a shared ledger for a group of people. Use its tools to save splits and read balances. Do the receipt reading and the arithmetic yourself, in the conversation.

## Who is who

- Call `list_members` before any expense. With no group it lists the user's groups; with a group it lists the members.
- The member marked `is_current_user: true` is the person you are talking to. Use it for "me", "I" and "my". Do not ask which member they are.
- Match other names to the member list. If a name is ambiguous or missing, ask.

## Splitting a receipt or bill

1. Read the receipt or the amounts the user gives. List the items, tax, tip and total.
2. Assign items to people as the user describes. Share tax and tip in proportion to each person's items unless the user says otherwise.
3. Work out one total per person. The shares must add up to the bill total exactly, to the cent. If rounding leaves a cent over, put it on the largest share and say so.
4. Show the per-person totals and who paid, and ask the user to confirm.
5. After they confirm, call `add_expense` with the bill's own currency and date. If there is no date, use today.

SplitCheck converts the amount to the group's currency. Report what was saved using the display amounts the tool returns.

## Everyone must have joined

An expense can only include people who are already members of the group. If someone is not a member, do not save anything and do not leave them out. Give the user the group's invite link and tell them to try again once that person has joined. Friends join from the link in a browser; they do not need the app or an account.

## New groups

Confirm the name, the type (trip, home, couple, friends or other) and the currency, then call `create_group`. Give the user the invite link to share.

## Balances

Call `get_balances` for one group. Present each debt with the display amount the tool returns. SplitCheck tracks balances only; it does not send money.

## Not available here

Editing or deleting an expense, recording that someone paid, and one-to-one splits outside a group are done in the SplitCheck app or at splitcheck.me. Say so plainly and do not try to work around it.

If a save returns an uncertain result, ask the user to check the group in SplitCheck before trying again, so nothing is added twice.
