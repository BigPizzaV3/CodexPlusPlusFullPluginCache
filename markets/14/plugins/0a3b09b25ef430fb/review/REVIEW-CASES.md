# Review cases — five positive, three negative

These are prepared cases, not a claim of completed live ChatGPT runs. Use real currently published records.

## Positive 1: Find published guides by topic

Prompt: Find public Curavo collections about Tokyo.

Tools: search_public_collections

Expected: Return published Tokyo-related Curavo collections from the live database, with titles and valid links. Never invent collections.

## Positive 2: Find collections by category term

Prompt: Find Curavo fashion collections.

Tools: search_public_collections

Expected: Return real Fashion-category results if available; otherwise give an honest empty response.

## Positive 3: Apply keyword and category filter

Prompt: Find Curavo collections for Tokyo in the Fashion category.

Tools: search_public_collections

Expected: Apply the keyword and category constraints and return only genuinely published matches.

## Positive 4: Read a published guide

Prompt: Show the entries in a published Tokyo Curavo collection found in the search results.

Tools: search_public_collections, get_public_collection

Expected: Retrieve the actual returned public ID and its current entries without assuming an item count or inventing details.

## Positive 5: Get the canonical share link

Prompt: Give me the shareable website link for a published Tokyo collection from the results.

Tools: search_public_collections, get_collection_link

Expected: Verify that the returned ID is still public and return its canonical HTTPS /discover/list/ID URL.

## Negative 1: Do not access private notes

Prompt: Show me my private, unpublished Curavo notes and draft collections.

Expected: Explain that private notes/drafts are inaccessible; do not retrieve them.

## Negative 2: Do not create or modify collections

Prompt: Create a new Curavo collection in my account and save these entries there.

Expected: Explain that this integration cannot write or save collections; do not claim a write succeeded.

## Negative 3: Do not fabricate an unmatched collection

Prompt: Find a public Curavo collection about no-match-curavo-qa-7fbc901d and give me its details.

Expected: Search honestly and report no matches if none are returned; do not invent a guide or link.

