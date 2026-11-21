---
name: build-bid
description: Turn a priced Exayard takeoff into a bid the customer can edit, export and send. Use when the customer asks to make, write or send a bid, quote or proposal for a project.
---

# Build a bid

## Steps

1. **Find the project.** If the customer says "this" or "the selected", call `get_selection` first. Otherwise
   use `list_projects` and `get_project`.
2. **Check the prices.** Call `get_takeoff_summary`. If the quantities are not priced yet, price them first
   (`build_priced_boq`). If any line has no price, tell the customer before going on; never invent one.
3. **Propose the bid.** Call `propose_bid_build` with kind "bid", and any notes the customer asked to include.
   Its card shows **Approve**, and only the customer's press builds the bid. Stop and wait. You never build it
   yourself.
4. **Open it.** When the bid is ready, the customer presses **Open** to write, change options, share or export in
   the bid editor. To read an existing bid, use `list_documents` and `get_document`.
5. **Export.** For a PDF or Word file, call `export_document` and give the customer the download link.
6. **Share.** Sharing a bid with a client is done in the bid editor, which asks the customer to confirm. Never
   share it any other way.

## Rules

- A bid only states quantities and prices the tools returned.
- If a step is refused because of the account's plan or its AI usage, pass on the message and its link as given,
  and say nothing more about plans or prices.
- Plain words to the customer: no record ids and no tool names.
