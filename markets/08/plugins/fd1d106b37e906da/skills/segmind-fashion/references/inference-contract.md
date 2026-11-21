# Segmind inference contract

Every Segmind skill obeys this file. It describes the MCP tool surface, the rules
that keep a run cheap and recoverable, and the failure modes that look like
something other than what they are.

## Tools

| Tool | Use it for |
|---|---|
| `list_models(search?, category?, sort?, max_cost?, limit?)` | Find and rank candidates. Rows carry `average_cost`, `latency`, `popularity`, `partner`, `price_drivers`. Also returns `total_catalog`, `total_matching`, `by_category`, `truncated`. |
| `compare_models(slugs)` | Put a shortlist side by side with each model's **base price table**. |
| `get_model_spec(slug)` | The chosen model's input schema. Call it for the model you will actually run, not for every candidate. |
| `run_inference(slug, params, timeout?)` | Fast models. Blocks up to ~45s (cap 50s) and returns the output inline. |
| `submit_inference(slug, params)` | Slow models. Returns a `request_id` immediately. |
| `check_inference(request_id)` | Collect a submitted job's output. The server long-polls, so one call usually waits out a short job. Results are kept ~1 hour. |
| `get_account()` | Balance (`credits`, `free_credits`, USD) **and which account pays** — `personal` or a named `team`, plus `other_accounts`. |
| `ping()` | Connectivity only. |

## The five rules

### 1. Never quote a price from `list_models`

`average_cost` is what past runs of that model *happened* to cost, driven by the
parameters those users chose (`price_drivers` names them) and skewed by low run
counts. It ranks; it does not price. Any claim about what something will cost,
or which of two models is cheaper, comes from `compare_models` — never from a
listing row.

Some rows carry a placeholder `average_cost` of exactly `1` (internal utility
nodes). Treat an `average_cost` of exactly 1 with `popularity` under ~50 as
missing data, not as a dollar.

### 2. Wait or submit — decide before you call, from `latency`

`run_inference` holds one request open. Its wait is capped at 50s on purpose:
MCP clients abort a call that has produced no response (60s is the common
default), and the server sits behind that ceiling too — the cap leaves room for
the submit and the final fetch to fit inside it alongside the wait.

- `latency` under ~30s → `run_inference`.
- `latency` at or over ~30s, or any video / 3D / multi-shot model → go straight
  to `submit_inference` and poll `check_inference`.

A `run_inference` that comes back with `pending: true` is **not an error**. It
carries the `request_id` and a `poll_after_seconds` hint — resume with
`check_inference`, never resubmit. Resubmitting bills the job twice.

Honour `poll_after_seconds`. It is derived from the model's observed latency,
so polling a 200-second video model every 5 seconds is forty wasted calls.

### Polling happens inside your turn

After submitting, call the matching `check_` tool **repeatedly, in the same
turn**, until the job reaches a terminal state — then deliver the result in that
same reply. Honour `poll_after_seconds` between calls.

**Ending your turn with "it's queued, it'll be ready shortly" is a failure of
this skill.** The user then has to type "status" to get their own result, which
is worse than if they had used the website. Tell them up front it will take a
couple of minutes and that you are waiting, then actually wait.

Only hand the turn back if the job is genuinely long-running — past roughly
fifteen minutes. Then say so plainly, give them the `request_id`, and tell them
to ask you to check it. That is the exception, not the pattern.

### 3. Check credits, state the cost, then spend

`models:invoke` spends the user's real money, silently. Before the first
generation of a session, call `get_account()`. Before anything expected to cost
more than **$0.50**, or before a batch whose total clears **$2**, say the number
and get a yes.

`get_account()` also names **whose** credits are about to go: `account` is the
user's `personal` balance or a named `team`. Say which one when it is a team —
spending a shared balance is a different decision from spending your own, and
`other_accounts` is what tells the user they could have billed elsewhere.

Sequential video renders add up fast: `seedance-2.0` averages ~$1.58 a run. Six
of those is a $9 mistake if the user only wanted to see one.

### 4. Inputs must be URLs the provider can fetch — upload local files first

Image and video inputs are `File (URL)` fields. What works:

- **A hosted `https://` URL — always.** Output from a previous run comes back as
  `https://images.segmind.com/...`; feed it straight into the next step. Chaining
  needs no upload.
- **A local file — mint an upload ticket first, without being asked.** There is
  no path argument on either tool, so do not invent one. Which route applies is
  decided by the host:
  - **ChatGPT** fills `file` from the attachment, so call
    `upload_media(file=...)` alone and the server fetches and re-hosts what the
    host served. Pass `filename` and `content_type` alongside it when you know
    them: without a filename the stored object keeps neither the user's name for
    it nor a content type derived from its extension.
  - **Codex and every other host** leave `file` empty, so call
    **`create_upload_ticket(filename, size_bytes)`** instead — it takes no `file`
    argument, which is the whole reason it exists. Measure the file's exact byte
    count: `create_upload_ticket(filename="sneaker.jpg", size_bytes=489626)`. You
    get back an `upload_url` and `required_headers` to PUT the bytes to, needing
    no Segmind credential of your own. (`upload_media` still accepts
    `size_bytes` and does the same thing, but it demands a `file` argument the
    host never filled.)

  Route 2 returns `status: awaiting_upload` and **no** `url`, because nothing is
  hosted yet: the model input is `url_after_upload`, usable only once the PUT has
  succeeded. Send every `required_headers` entry verbatim or the PUT fails with
  `SignatureDoesNotMatch`, and give a filename with a real extension, since the
  stored content type comes from it. `size_bytes` must be measured, never
  estimated — too large fails with a 400, but too small succeeds and silently
  stores a truncated file.

  Either way this is a reflex, not a decision: the moment you hold a file where a
  model wants a URL, upload it. Never ask the user to host the file themselves,
  and never tell them it cannot be used.
- **A `data:` URI — don't.** It only survives to about a 256px thumbnail
  (measured: a ~7KB body succeeds, ~11KB fails) and fails with a misleading
  `property input is required`. `upload_media` has no such limit.
- **Bare base64 — never.** Rejected with `422 ... Does not match format 'uri'`.

**Uploaded files are publicly fetchable by URL.** That is what lets the provider
read them, but it means anything uploaded is reachable by anyone holding the
link. Do not upload something the user would not want exposed that way, and say
so if they seem to assume otherwise.

### 5. The spec is a strong hint, not a contract

`get_model_spec` is generated from the public docs and drifts from the live API.
Observed: `utility-image-metadata` documents `operations` as a `string` while the
API requires a list of objects.

On a `422`, read the validation message — it names the field and the expected
type — correct the params, and retry **once**. If it fails again, report the
field and the message. Never loop on a 422; every retry that reaches the
provider can bill.

## Errors that lie

| What you see | What it usually is |
|---|---|
| `property input is required` from the provider | The payload was too large — almost always an oversized `data:` URI. Not a missing field. |
| `blocked by the provider's content moderation system` | Sometimes real, sometimes a misclassified upstream error. Retry once with a reworded prompt before telling the user their prompt was rejected. |
| `HTTP 500` | Can be a content-policy rejection rather than an outage. Read the error body before calling the model broken. |
| `pending: true` | Not an error. See rule 2. |

## Delivering results

Hand back the `https://images.segmind.com/...` URL from the result. Never hand
back a provider's signed link — those expire and leak the routing. Report the
`cost` from `metrics` when the user is tracking spend.
