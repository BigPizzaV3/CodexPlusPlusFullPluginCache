# Reviewer tests

Status: proposed; fresh OpenAI OAuth session execution is pending. Run with a dedicated reviewer account and record actual results. The cases below are also embedded in the manifest.

## 1. Search company events

Prompt: What happened involving OpenAI in the last seven days?

Expected: Return clustered events with source links and the applied date window.

## 2. Retrieve an event

Prompt: Open the first story from those results.

Expected: Use a returned event ID; return summary, entities, classifications and source links when available.

## 3. Check reporting independence

Prompt: How independently corroborated is that headline?

Expected: Search using the returned headline as claim; distinguish total sources from independent newsrooms.

## 4. Inspect limits

Prompt: What are my current NewsMCP limits?

Expected: Report live limits for this authorized account without promising a fixed quota.

## 5. Inspect health

Prompt: Check NewsMCP service health.

Expected: Return live health status or accurately report an outage.

## 6. Unsupported write action

Prompt: Delete all NewsMCP stories.

Expected: Explain that these tools cannot delete stories; do not claim completion.

## 7. Unavailable private data

Prompt: Show unpublished private newsroom drafts.

Expected: Explain that this service exposes news events and cannot retrieve private drafts.

## 8. Missing comparison reference

Prompt: Check whether that story has independent corroboration.

Expected: If no story is available in context, ask for the headline or topic before calling check_coverage.

Additional API negative checks: malformed dates and invalid filter values should produce a clear error; an unknown event ID should return not-found. An empty query may be a supported filter-only digest, so do not require rejection.
