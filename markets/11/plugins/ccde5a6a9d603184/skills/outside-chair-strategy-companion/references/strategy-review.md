# Prepare and approve a strategy review

1. Call `prepare_review` once. Explain material changes, decisions, actions, outcomes, attention and gaps; show at most five and count the rest.
2. Classify the review. A baseline may complete FRAME; testing its evidence and dissent may complete CHALLENGE. Ordinary records and evidence complete neither. Restarting FRAME before LEARN needs an explicit reason.
3. Show the exact title, date, scope, narrative and lifecycle effect, then get confirmation before `prepare_review_approval`, which stores a proposal. Resolve the cycle internally; never ask for its review ID.
4. Show the returned exact summary, lifecycle consequence, hash and expiry. Obtain confirmation tied to that hash.
5. Call `approve_review` with only proposal ID, hash and a fresh idempotency key.
6. Read back with `get_approved_review`. Report frozen counts, lifecycle position and material decisions/actions, not the raw snapshot.
7. If context or cycle changed, or the proposal expired, explain and prepare again; never guess.
