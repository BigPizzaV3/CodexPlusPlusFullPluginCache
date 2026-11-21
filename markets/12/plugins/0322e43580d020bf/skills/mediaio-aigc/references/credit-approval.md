# Existing-credit behavior

Normal generation submits quietly and consumes the user's existing credits. Omit `approved_credit`; the server submits without calling the credit-estimation endpoint. Do not require an estimate, balance check, account card, quote token or per-task price approval. Batch requests and inferred cost sensitivity do not enable estimation automatically. Do not announce prices without the user's interest in cost.

When the user asks for an estimate, call the single `estimate_credits` with a static request matching one of the seven generation operations. Put the complete business request in `request.generation`. Use the same model, inputs and settings for any later generation. Estimating never authorizes or creates a task; if the user says "estimate only", stop after reporting the estimate.

`approved_credit` is an optional client amount guard for an explicit user preference. Only this field triggers pre-submission recalculation; a mismatch, including a change to or from zero, rejects with `CREDIT_CHANGED`. An unavailable estimate also blocks guarded submission. The check does not provide an atomic upstream quote guarantee. Never bypass a requested guard on retry. Normal generation omits it.

The creation receipt's optional `frozen_credit` comes from the upstream create response and reports frozen credits, not final settlement. A missing amount is unknown, not zero or free, and must not trigger a follow-up estimate. Optional `estimated_credit` is retained for explicit amount protection and legacy idempotent replays; it is never evidence of freezing or settlement. Older servers may return only that estimate field. Refresh tool definitions after upgrading and accept either credit field being absent. Do not claim a refund or zero actual debit from a failure alone.

Insufficient credits or entitlements mean the task is currently unavailable. Stop without transactions, purchase links, subscription or upgrade suggestions. Do not switch models, increase quantities, change request IDs or retry a task whose outcome is unknown. Existing paid entitlements remain usable.
