---
name: evaluate-answer
description: Evaluate one AI answer the user selected with the connected zenture engine — it checks the answer against its original task and checks factual statements against the sources the answer cites. Also retrieves and explains existing zenture evaluations. Use only when the user asks to check, verify or evaluate an answer (with zenture); writing or improving an answer is not a request to evaluate it.
---

# zenture · evaluate an answer

Write the brand as **zenture** (lowercase). Reply in the user's language. zenture is the evaluation authority: report what the engine returned, never your own review as if it were an engine result.

## When to use — and when not

**Use** when the user asks to check, verify, evaluate or "run zenture on" an answer — a pasted text, a selected message, or an unambiguous reference such as "check your last answer". Also use to fetch or explain an earlier zenture run.

**Do not use**
- for writing, rewriting or improving an answer (that is not an evaluation request);
- to evaluate an answer the user did not select — never pick one from history yourself;
- for samples, smoke tests or "let's see if it works" runs without the user asking — every run costs credits (guests: limited free runs);
- to replace the engine: do not pre-check, fact-check or "fix" the answer yourself before or instead of a run.

## The tools

| Tool | What it does | When |
|---|---|---|
| `run` | Starts one evaluation of one answer against its task. Returns `run_id` immediately. | Once per evaluation the user asked for. |
| `get_run` | Reads a run. With `wait_seconds=30` it waits (free) until the run is done or 30 s pass. `view="full"` adds per-statement evidence. | After `run`, repeatedly until terminal; to show details. |
| `list_runs` | Lists the user's recent runs. | Only to find a run whose ID or key you lost, or when the user asks for past runs. Not before starting a new run. |
| `cancel_run` | Requests a stop. | Only on the user's explicit request. Then read the run again for its final state. |
| `record_run_outcome` | Stores the user's feedback on a finished run. | Only on explicit user feedback, never from silence. |

## What to do

1. **Identify the input.** You need the original task (with every explicit requirement: length, format, language, sources, exclusions) and the exact answer. If either is unclear, ask — do not guess.
2. **Explain the cost once** before the first run (account: credits by profile; guest: free trial runs). The user's request to evaluate authorizes that one run.
3. **Start the run.**
   - `task`: the user's original instruction verbatim, plus explicit follow-up constraints. Do not summarise, add standards or turn it into "write a better answer".
   - `artifact`: `{"type":"text","value":"<the answer unchanged, including citations and formatting>"}`. Not a bare URL. Limits: task 20,000, answer 50,000 characters — never truncate or split silently.
   - `idempotency_key`: create a random key **before** calling `run` and keep it.
   - `profile`: omit for **standard**. Use `fast` or `detailed` only if the user asks (guests: no `detailed`).
4. **Wait for the result:** `get_run(run_id, wait_seconds=30)` until the status is terminal. No sleeping, no rapid polling.
5. **Explain the result** (below), then offer the next step the engine returned.

## Errors and recovery — the important rules

- **Never start a replacement run** because of a delay, timeout, disconnect or retryable error. The original run keeps going.
- **Retryable error on `get_run` / `list_runs`** (e.g. `dependency_unavailable`, `retryable: true`): call `get_run` again with the same `run_id`.
- **Uncertain start** (the `run` call failed or timed out): call `run` again with the **same key and unchanged inputs** — the same key returns the same run. Without a key, find the run with `list_runs` first; do not start blind.
- Follow `error.next_action`. Missing or expired authorization → the host's connect/OAuth flow. `accept_legal_terms` → the account owner accepts the update in the zenture web app (Account → Terms update), then resume. Credit top-ups happen only in the web app.
- If repeated waits return without progress, report the current state and the `run_id`; do not loop forever.

## Explaining the result

Lead with the **decision** and its main reason. `status: completed` only means the run finished — not that the answer passed.

| Decision | Meaning |
|---|---|
| `ready` | All assessed requirements met; every factual statement supported by its cited source. |
| `revise` | A requirement is not met, or a statement is contradicted or has no source. |
| `human_review` | Requirements are ambiguous or conflicting, or statements could not be verified. |
| `insufficient_evidence` | A required check could not be done (e.g. a needed input or source is missing, or coverage is incomplete). |

`technical_status: degraded` means the run finished with reduced coverage; say so next to the verdict.

Then show what matters: the requirement or statement, its assessment, the evidence, and what to change. Keep task fulfilment, factual correctness and source support apart. A missing source is a finding, not proof the statement is false; an unavailable source is not a contradiction.

**Only report what was returned.** Check `safe_result_content` first; if it is unavailable or expired, say so and show only the decision. Never invent findings, quotes, scores or confidence values. Link only URLs from the answer or the result (evidence refs are not URLs). Report credits only from `billing_summary`. For failed, cancelled or expired runs, explain the technical outcome — no verdict, no assumed refund.

## After the result

- If the user wants a correction, draft it from the findings and label it as a revision — it is **not** evaluated until the user asks for a new run. Then pass the old run as `predecessor_run_id`.
- Feedback on a finished run → `record_run_outcome` with finding refs from the full result. `edited` needs a real `artifact_ref`; if file upload is unavailable in this host, say so instead of inventing one.
