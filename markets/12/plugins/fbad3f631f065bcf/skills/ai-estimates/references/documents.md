# Document rules

These match the estimate, quote, and invoice templates on vanreceipts.app.

## Estimate

- Date label: Valid until.
- An allowance is a budget for something the client has not picked, such as a fixture, lumber, or decking. If they pick something that costs more, the difference is a change, and the estimate says so.
- Put the allowance on its own line and set `allowance` to true.

## Quote

- Date label: Offer holds until.
- The price is fixed for the lines on the page. Do not add an allowance.
- Acceptance line on the PDF: "Accepted by client", unless the user supplies different wording.
- Deposit terms are the user's words, for example "30 percent to schedule. Balance when the work is finished."
- For USD, the server adds "This is not legal advice. Rules vary by state." For any other currency, it adds "This is not legal advice. Rules vary by location."
- These match the site quote templates: date label "Offer holds until", acceptance line "Accepted by client", and a deposit line in the notes.

## Invoice

- Date label: Due.
- Bill work that is finished or in progress. Do not add an allowance.
- Total label: Total due.

## PDF

Styles are classic, modern, and bold. The footer is "Made free with VanReceipts · vanreceipts.app". The user can edit lines in the widget before download. After an edit, call `build_document` again so VanReceipts recomputes the total.
