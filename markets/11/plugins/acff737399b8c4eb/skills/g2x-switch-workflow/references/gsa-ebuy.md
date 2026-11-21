# GSA eBuy

These tools show exactly the GSA eBuy RFQs the signed-in person's own eBuy pages in G2X show them. They never return a direct file link and never send anything to GSA. Submit quotes through GSA eBuy.

When an RFQ is not available, the tool says why in the user's own terms: the plan does not include GSA eBuy, the account owner needs to grant access, or eBuy needs connecting in G2X. Repeat that next step instead of retrying.

### `g2x_search_ebuy`

Find GSA eBuy RFQs available to the user in G2X.

- Inputs: `keywords`, `agency`, `schedule`, `sin`, `closes_after`, `closes_before` (filter by deadline, agency, schedule or SIN); `cursor` (page number to continue; omit for the first page).
- Output: RFQ rows with the total and a cursor for the next page. An empty answer means no RFQs match these filters.
- Plan: accounts with GSA eBuy in G2X, when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"keywords": "IT services"}`

### `g2x_get_ebuy`

Read one GSA eBuy RFQ available to the user.

- Inputs: `rfq` (required, the RFQ reference from a search result; letters, digits, hyphens and underscores).
- Output: the RFQ with its buyer details, deadlines, amendments and questions. End with a reminder to submit quotes through GSA eBuy.
- Plan: accounts with GSA eBuy in G2X, when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"rfq": "<reference from an eBuy search>"}`

### `g2x_list_ebuy_attachments`

List the files attached to one GSA eBuy RFQ. File names only; there is no download through this tool.

- Inputs: `rfq` (required, the RFQ reference).
- Output: attachment rows for the RFQ, or a plain statement that it has no attachments. To open a file, send the user to the RFQ in G2X or GSA eBuy.
- Plan: accounts with GSA eBuy in G2X, when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"rfq": "<reference from an eBuy search>"}`
