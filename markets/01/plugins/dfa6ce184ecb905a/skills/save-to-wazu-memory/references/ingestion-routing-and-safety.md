# Ingestion routing and safety

## Preconditions

Before any write, confirm:

- the user requested persistence
- the target is a real, authorized cohort
- the content and source context are understood
- the chosen operation matches the payload

If the target is ambiguous, stop. The synthetic Personal selector is not a valid cohort target.

## Choose the write operation

| Payload | Preferred operation |
|---|---|
| Structured summary, decision, update, task, note | `commit_summary_to_cohort` |
| Raw text, transcript, extracted document text | `ingest_text` |
| Document, image, audio, video, or other supported bytes | `ingest_media_base64` |

Preserve human-readable source, date, speaker or sender, and tags when the user provided them. Do not manufacture metadata.

## Idempotency and retry

Use a stable idempotency key when the caller or workflow supplies one. Current end-to-end duplicate suppression is not assumed to be proven, so do not automatically retry after an ambiguous timeout. First inspect the returned receipt or retrieve the expected item.

## Verify the write

A successful response should identify the stored item and target cohort and indicate whichever lifecycle stages completed:

- stored
- replicated
- enriched or indexed
- graph-linked
- retrieval-verified
- metered or receipted

If retrieval readiness is not explicit, call `get_item` with the returned item ID. Do not convert “accepted” into “fully indexed.”

## Handle failures

Report authorization, invalid cohort, unsupported media, payload size, metering, enrichment, and transport failures distinctly. Avoid repeating the write unless Wazu proves the first attempt did not commit.

Never include bearer tokens, raw base64 data, private payer identifiers, internal file paths, or server debug dumps in the user-facing result.
