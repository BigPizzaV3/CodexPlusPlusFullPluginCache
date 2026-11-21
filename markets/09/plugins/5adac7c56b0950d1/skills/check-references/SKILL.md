---
name: check-references
description: Check whether references really exist and match their DOIs using CitedEvidence. Use on any reference list the user shares or asks you to verify, and on references you wrote yourself before presenting them.
---

# Check references

1. Split the list into one string per reference, keeping each reference's full text (authors, year, title, journal, DOI). Don't fix or reformat entries before checking them.
2. Call `verify_references` with up to 25 references at a time. For longer lists, check in batches and combine the results.
3. Report by status:
   - **verified**: say so briefly;
   - **details differ**: name the field that differs (year, author or DOI) and give the correct value from the matched record;
   - **DOI mismatch**: the DOI points to a different paper; give the correct DOI if one was found;
   - **possible match**: a similar paper exists; ask the user to confirm;
   - **not found**: no matching paper in CitedEvidence Scholar or Crossref. Say the reference could not be found and may not exist. Don't call it fabricated with certainty.
   - **not checked**: it timed out; offer to check it again.
4. Offer to produce a corrected list. Build corrections only from matched records, then use `format_citations` in the user's style.
