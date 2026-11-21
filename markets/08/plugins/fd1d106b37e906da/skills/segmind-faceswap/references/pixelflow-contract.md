# Pixelflow contract

A **Pixelflow** is a saved multi-model graph: input nodes → one or more model
nodes → output nodes. Use one when the job is a pipeline someone already built
and tuned; use `run_inference` when a single model does the job.

## Tools

| Tool | Use |
|---|---|
| `list_pixelflows(search?, limit?, source?)` | Browse published flows, best match first, with `runnable` per row (broken flows sort last). `source="mine"` lists the user's own saved flows. |
| `get_pixelflow_spec(slug, inputs?)` | The runnable spec: `inputs` (each with `keyname`, `kind`, `feeds`, `is_list`, `example`), a ready-to-fill `inputs_skeleton`, `models`, `nodes`, `runnable`, and `estimated_cost` for one run. |
| `submit_pixelflow(slug, inputs)` | Start a run. Returns a `request_id` immediately. |
| `check_pixelflow(request_id)` | Collect it. Waits up to ~45 s on the server; `pending: true` means call it again straight away. |

## Rules

### 1. Always `get_pixelflow_spec` before running

A flow's input keys are **arbitrary names chosen when it was built** —
`video_in`, `image_kj3ba`, `Model_Image`, `select_clothing_in_reference_image`.
They cannot be guessed and they are not consistent between flows. Send a flat
object keyed by each `keyname`:

```
submit_pixelflow(slug="video-upscaler-bria-mcp",
                 inputs={"video_in": "https://..."})
```

### 2. There is no blocking run — always submit, then poll

A flow chains several models, so even an image-only flow can outrun the request
budget a blocking tool has to fit inside. `submit_pixelflow` → `check_pixelflow`
is the only path. Never resubmit a `pending` run; it is already billed.

### Polling happens inside your turn

After submitting, call the matching `check_` tool **repeatedly, in the same
turn**, until the job reaches a terminal state — then deliver the result in that
same reply. The server already waits up to ~45 s per call, so call again at once.

**Ending your turn with "it's queued, it'll be ready shortly" is a failure of
this skill.** The user then has to type "status" to get their own result, which
is worse than if they had used the website. Tell them up front it will take a
couple of minutes and that you are waiting, then actually wait.

Only hand the turn back if the job is genuinely long-running — past roughly
fifteen minutes. Then say so plainly, give them the `request_id`, and tell them
to ask you to check it. That is the exception, not the pattern.

### 3. A flow bills every model in its chain

Read `estimated_cost` from `get_pixelflow_spec` and say the total before
spending. When `min` is null, some step cannot be priced in advance: say the run
costs *at least* `known_min` plus the `unpriced_steps`, never that `known_min` is
the price. Pass the planned `inputs` to price steps that depend on a duration or
resolution.

### 4. Check the chain is alive before you recommend a flow

**A published Pixelflow is not proof its models still work.** `runnable: false`
in the listing or the spec means a chained model is retired: a run would bill
the steps before it and then fail. Don't run it; say which model is gone
(`not_runnable_reason`) and compose live models instead.

### 5. Read a node failure correctly

A failed flow names the node and the model's error:

```
"Node 53f6f0ab… failed with error: image not found"
```

`image not found` from a node whose inputs are correct means **that node's model
is broken**, not that your input was wrong. Do not retry it and do not go
hunting for a bad URL — report which model failed.

### 6. `COMPLETED` does not mean it worked

A flow can report `COMPLETED` and carry no output — the engine returns
`{"Output_Video": {"data": null}}` when a node finishes without emitting
anything. `check_pixelflow` raises on this rather than handing back a null URL,
but the lesson is broader: **check that an output value is actually present
before telling the user a run succeeded.** Measured on `anime-style-ad-wan-3`,
which ran for 10 minutes and returned `COMPLETED` with a null video.

Re-running an empty completion bills again for the same empty result. Treat it
as a flow bug and report it.

### 7. Fewer nodes is a feature

~10% of the published catalogue is broken, and always because **one node in the
chain rotted**. Every node added to a flow is another model that can be retired,
break, or start returning 400 — and a flow fails whole, after billing the nodes
that already ran.

So do not add a node for tidiness. Add one only when it does work the caller
would otherwise pay for separately, and prefer a short chain plus a second call
over a long chain. When a single model does the job, recommend the model.

### 8. Inputs and outputs are hosted URLs

Media inputs must be URLs the provider can fetch. Outputs come back keyed by the
flow's output `keyname`, as `https://images.segmind.com/outputs/...` — which can
be fed straight into the next flow or model, so chaining flows needs no upload.
