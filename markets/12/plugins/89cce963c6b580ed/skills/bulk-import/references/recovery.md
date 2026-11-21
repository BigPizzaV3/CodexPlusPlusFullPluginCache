# Import receipts and recovery

Receipt states: saved-verified, saved-unverified, unchanged, rejected, deferred, not-attempted, outcome-unknown. Include source fingerprint/row, plan/version/operation, resource, target ID, dependencies, actual result and concise error. No tokens.

On 401 reconnect and revalidate context; a changed organisation invalidates the plan. On systemic 403/entitlement failure stop. On row validation/conflict hold that row/dependants; continue independent approved rows only under the preview's chosen policy. Honour 429 guidance. Never automatically retry an uncertain write.

For timeout, use returned ID if known; otherwise compare approved matching keys and the baseline/receipt. If uncertain, leave outcome unknown for review. A successful create might precede a lost response. Resume only after matching source fingerprint, plan version and context; do not replay already verified rows.

No automatic delete rollback. Do not claim an atomic batch, exactly-once operation, server job or cancellation of already saved records. Without durable checkpoints, provide bounded receipts before continuing and explain resumption limits.
