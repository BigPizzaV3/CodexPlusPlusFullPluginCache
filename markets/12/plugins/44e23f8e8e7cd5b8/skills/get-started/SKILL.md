---
name: get-started
description: Introduce Converge Bio and help the user run a first antibody lead search or patent extraction. Use when the user has just installed Converge Bio or asks what it can do.
---

# Get started with Converge Bio

Converge Bio has two features. Offer both and let the user pick one.

## Find a Lead

1. Ask for a protein target, for example PD-L1, HER2 or EGFR.
2. Call `find_leads` with that target. If the target is not covered, call `list_lead_targets` to suggest close matches.
3. The results show in an interactive table. Describe the top leads briefly; do not reprint the table.
4. If the user wants details on one lead, call `get_lead_report` with the lead from that result.

## Patent extraction

1. Ask for a patent number, for example US9193787B2.
2. Call `start_patent_extraction`. Tell the user it runs in the background, usually for 15 to 60 minutes, and that the card in the chat updates on its own.
3. To check on it later, call `get_patent_extraction`. To see past runs, call `list_patent_extractions`.

## Notes

- The user signs in with their Converge Bio account the first time a tool runs.
- Patent extraction needs a work email address.
- Converge Bio gives research data. Do not present it as medical advice.
