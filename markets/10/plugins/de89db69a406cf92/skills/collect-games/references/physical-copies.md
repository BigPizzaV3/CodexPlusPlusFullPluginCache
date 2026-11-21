# Physical copies (所有ソフト, PREMIUM)

A library row describes "I own this game". Physical copies are rows; each row has a `quantity` (how many identical copies it stands for) and its own condition, purchase details, edition (通常版 or a バージョン違い). One row is active, and its values are shown on the library row. Many users never use copies; do not create them unless the user wants per-copy detail or has more than one copy.

Always start from getPhysicalCopies unless the previous successful write gave you the current revision.

| What the user says                                                              | Operation                                                                                                                            |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| "I want to record the condition and details of the copy I have" (no copies yet) | addPhysicalCopy `mode: "materialize"` — turns the library values into the first copy                                                 |
| "I bought another one"                                                          | addPhysicalCopy `mode: "additional"` — with no copies yet, this keeps the existing one as a copy and adds the new one                |
| "Make this one the main copy"                                                   | updatePhysicalCopy `makeActive: true` — the library row's purchase info, rating and memo change to this copy's values; tell the user |
| "I sold / gave away one copy" (the row has quantity 2 or more)                  | updatePhysicalCopy with the new `quantity` — keeps the row, edition and purchase details. Do not delete the row                      |
| "I sold / gave away this copy" (the row has quantity 1, or all of that row)     | removePhysicalCopy — deletes the whole row, including its quantity. The game stays in the library even when the last row is removed  |
| "I don't own this game any more"                                                | removeFromLibrary — also deletes play records and copies                                                                             |

If the user's intent is unclear between materialize and additional, ask. Do not decide from the number of rows.

When the user gives away copies, check the row's `quantity` first. If it is unclear which row or how many copies, ask before changing anything.

Editions: set the edition only when the user says which one they own. A barcode match on an edition identifies the parent game; it does not record the edition by itself. Custom games have no editions.

App reference: https://docs.retrogather.com/features/library/
