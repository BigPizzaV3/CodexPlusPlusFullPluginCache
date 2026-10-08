# Retry and Recovery Details

Use after a failed or ambiguous upload or create result.

For sibling ad creates, continue after a definitive failure because the remaining approved creates are independent, but stop after an ambiguous failure to avoid creating an unknown duplicate. Report `Succeeded`, `Failed`, and `Not attempted` outcomes for each ad when the set does not complete.
