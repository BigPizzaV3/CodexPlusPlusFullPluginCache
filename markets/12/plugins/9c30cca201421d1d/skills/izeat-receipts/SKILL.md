---
name: izeat-receipts
description: Present results from IZeat tools so customers can identify which facts were read from or recorded in their IZeat account.
---

# Present IZeat results

Whenever an IZeat tool result contributes to a customer-facing reply, begin the visible reply with
the exact prefix `IZeat ·`.

The prefix identifies the facts returned by IZeat. It reassures the customer that information was
read from or recorded in their IZeat account rather than inferred from the assistant's conversation.

Treat the returned `statement` as the authoritative receipt. Preserve every fact it contains and
keep the prefix unchanged when presenting those facts in the customer's language. If the reply also
includes general assistant guidance, put the signed IZeat information first and clearly separate the
guidance that follows.

An IZeat interactive report accompanies a day or period result. A day report shows calorie and macro
totals, targets and remaining amounts, every recorded meal, and each food's quantity, calories,
macros and source. A period report shows coverage, calorie and macro averages, targets, and the daily,
weekly or monthly trend.

Do not add the prefix to a question asked before any IZeat tool has been called. Do not expose tool
names, connector names, request fields, identifiers, tokens, schemas, or other implementation details
in customer-facing text.

## Catalogue and preparation results

Offer catalogue recipes only in response to the customer's request for meal ideas.
Use the returned recipe references and plate sizes when they choose a recipe, including
through the “I'll cook it” button. A choice requests preparation; it is not evidence
that the customer ate anything. Wait for their actual consumption and quantities
before recording a meal.

Present ingredients scaled to the selected plate. The returned steps are the original
method for the whole recipe: do not confuse quantities in those steps with the scaled
plate ingredients. Credit the creator or inspiration exactly as returned.

A catalogue proposal records a deduplicated view. A successful complete-method request
records a separate deduplicated use for creator royalties. Neither is proof of cooking
or consumption, and a later meal log does not add another recipe use.

Show the interactive recipe and report cards when supported by the host. Do not claim
a card rendered successfully without observing it. If the host cannot display a card,
answer from the returned data and explain the display limitation without inventing data.
