# juicy command reference

Generated from the CLI's command specs; do not edit by hand.

Global flags on every command: `--human`, `--compact`, `--progress`, `--api-url <url>`, `--help`, `--request-schema`, `--response-schema`, `--version`.

| Command | Purpose |
|---|---|
| `juicy auth help` | How to sign a user in — read this before asking them for anything |
| `juicy auth login` | Sign in with email and password |
| `juicy auth status` | Show the signed-in account and balance |
| `juicy auth logout` | End the local session and delete the credentials file |
| `juicy credits balance` | Show the account's credit balance |
| `juicy credits usage` | Credits spent, grouped by campaign, model, variant or day |
| `juicy catalog list` | List roles, the models each offers, and what every model is best for |
| `juicy catalog get` | Show one model's catalog row (price, limits, guidance), or its input schema |
| `juicy image generate` | Generate a first frame from a prompt |
| `juicy image edit` | Edit a reference image with an instruction |
| `juicy video generate` | Animate an approved first frame into a clip |
| `juicy audio music` | Generate a soundtrack |
| `juicy job get` | Show a job; with --wait, poll it; with --project, freeze its output |
| `juicy job cancel` | Cancel a queued or running job |
| `juicy sample list` | List the free sample assets (no sign-in needed) |
| `juicy sample get` | Download a sample into the project and record it (zero credits) |
| `juicy manifest verify` | Check that every manifest record points at a frozen local file |
| `juicy doctor` | Check the local setup: credentials, API, contract, catalog, samples, project |
| `juicy completion` | Print a shell completion script |
| `juicy skill` | Write the generated SKILL.md and command reference for agents |

### `juicy auth help`

How to sign a user in — read this before asking them for anything Prints the sign-in method this version supports and the exact steps to follow: what to ask the user for, the command to run, and what never to do with what they gave you. Callers follow this rather than remembering a mechanism, because it will change — a later version signs in through the browser.

```
juicy auth help
```

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: none; this command runs locally.

Example:

```bash
juicy auth help
```

### `juicy auth login`

Sign in with email and password On a terminal, prompts for the email and password (password echo off). Without a terminal, pass --email and --password-stdin. Writes ~/.juicylucy/juicy/credentials (mode 0600).

```
juicy auth login [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--email <email>` | string |  |  |  | Account email |
| `--password-stdin` | boolean |  | off |  | Read the password from the first line of stdin |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy auth login
```

### `juicy auth status`

Show the signed-in account and balance

```
juicy auth status
```

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

### `juicy auth logout`

End the local session and delete the credentials file

```
juicy auth logout
```

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

### `juicy credits balance`

Show the account's credit balance

```
juicy credits balance
```

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

### `juicy credits usage`

Credits spent, grouped by campaign, model, variant or day

```
juicy credits usage [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--group-by <campaign|model|variant|day>` | string |  | "campaign" | campaign \| model \| variant \| day | Grouping |
| `--since <yyyy-mm-dd>` | string |  |  |  | ISO date; default 30 days ago |
| `--limit <n>` | integer |  | 100 |  | Rows per page |
| `--cursor <cursor>` | string |  |  |  | Continue from a previous next_cursor |
| `--fields <a,b>` | string |  |  |  | Comma-separated fields to keep in the output |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy credits usage --group-by campaign --since 2026-09-01
```

### `juicy catalog list`

List roles, the models each offers, and what every model is best for Each role has a default model and, under `models`, the ones --model may pick (id or alias). `models` carries every listed model's price, limits and guidance. With --role, only that role and its models.

```
juicy catalog list [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--role <role>` | string |  |  |  | Only this role |
| `--refresh` | boolean |  | off |  | Bypass the one-hour cache |
| `--fields <a,b>` | string |  |  |  | Comma-separated fields to keep in the output |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy catalog list
```

### `juicy catalog get`

Show one model's catalog row (price, limits, guidance), or its input schema Takes a model id or alias. With --request-schema, prints the model's input schema from the provider (what `juicy image generate` ultimately sends). Without a <model>, --request-schema prints this command's own flag schema, like every other command.

```
juicy catalog get <model> [options]
```

Arguments:

- `<model>` — Model id or alias, e.g. kling-3-pro

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--refresh` | boolean |  | off |  | Bypass the one-hour cache |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy catalog get kling-3-pro
```

### `juicy image generate`

Generate a first frame from a prompt Freezes the result under .media/first-frames/<variant>.<ext> and appends the manifest record in the same call. Never overwrites: a repeat with a different seed gets -a2, -a3 …

```
juicy image generate --aspect <9:16|4:5|1:1|16:9|3:4|4:3|2:3|3:2|21:9> --variant <name> [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--role <first-frame>` | string |  | "first-frame" | first-frame | Catalog role |
| `--model <id|alias>` | string |  |  |  | Model for this role, by id or alias; `juicy catalog list --role <role>` shows the choices |
| `--prompt <text>` | string |  |  |  | The prompt |
| `--prompt-file <path>` | string |  |  |  | Read the prompt from a file |
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--campaign <name>` | string |  |  |  | Campaign label recorded in the manifest and ledger |
| `--max-cost <credits>` | integer |  |  |  | Refuse before submitting if the quote exceeds this many credits |
| `--preset` | boolean |  | on |  | Apply the ad-safe preset: no on-image text, logos or device UI |
| `--force` | boolean |  | off |  | Generate again even if the manifest already has this exact input |
| `--wait` | boolean |  | on |  | Poll until the job finishes |
| `--idempotency-key <key>` | string |  |  |  | Override the idempotency key (defaults to the input hash) |
| `--aspect <9:16|4:5|1:1|16:9|3:4|4:3|2:3|3:2|21:9>` | string | yes |  | 9:16 \| 4:5 \| 1:1 \| 16:9 \| 3:4 \| 4:3 \| 2:3 \| 3:2 \| 21:9 | Aspect ratio |
| `--seed <n>` | integer |  | 1 |  | Seed, recorded in the manifest; --force draws a fresh one unless this is given |
| `--variant <name>` | string | yes |  |  | Variant name; the output is .media/first-frames/<variant>.<ext> |
| `--resolution <0.5K|1K|2K|4K>` | string |  | "1K" | 0.5K \| 1K \| 2K \| 4K | Output resolution |
| `--format <png|jpeg|webp>` | string |  | "png" | png \| jpeg \| webp | Output format |
| `--timeout <duration>` | string |  | "5m" |  | How long to wait |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed · 4 still running (job JSON on stdout, run `next`) · 5 insufficient credits

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy image generate --role first-frame --aspect 9:16 --variant v03 --prompt "…" --project .
```

### `juicy image edit`

Edit a reference image with an instruction Uploads the reference image(s) and asks the edit model to change only what the prompt names. The preserve-list belongs in the prompt.

```
juicy image edit --variant <name> --image <path> [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--role <first-frame-edit>` | string |  | "first-frame-edit" | first-frame-edit | Catalog role |
| `--model <id|alias>` | string |  |  |  | Model for this role, by id or alias; `juicy catalog list --role <role>` shows the choices |
| `--prompt <text>` | string |  |  |  | The prompt |
| `--prompt-file <path>` | string |  |  |  | Read the prompt from a file |
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--campaign <name>` | string |  |  |  | Campaign label recorded in the manifest and ledger |
| `--max-cost <credits>` | integer |  |  |  | Refuse before submitting if the quote exceeds this many credits |
| `--preset` | boolean |  | on |  | Apply the ad-safe preset: no on-image text, logos or device UI |
| `--force` | boolean |  | off |  | Generate again even if the manifest already has this exact input |
| `--wait` | boolean |  | on |  | Poll until the job finishes |
| `--idempotency-key <key>` | string |  |  |  | Override the idempotency key (defaults to the input hash) |
| `--aspect <9:16|4:5|1:1|16:9|3:4|4:3|2:3|3:2|21:9>` | string |  |  | 9:16 \| 4:5 \| 1:1 \| 16:9 \| 3:4 \| 4:3 \| 2:3 \| 3:2 \| 21:9 | Aspect ratio (optional for edits; the model's auto otherwise) |
| `--seed <n>` | integer |  | 1 |  | Seed, recorded in the manifest; --force draws a fresh one unless this is given |
| `--variant <name>` | string | yes |  |  | Variant name; the output is .media/first-frames/<variant>.<ext> |
| `--resolution <0.5K|1K|2K|4K>` | string |  | "1K" | 0.5K \| 1K \| 2K \| 4K | Output resolution |
| `--format <png|jpeg|webp>` | string |  | "png" | png \| jpeg \| webp | Output format |
| `--timeout <duration>` | string |  | "5m" |  | How long to wait |
| `--image <path>` | string (repeatable) | yes |  |  | Reference image(s), up to 4, uploaded for you |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed · 4 still running (job JSON on stdout, run `next`) · 5 insufficient credits

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy image edit --image .media/references/ref-frame.png --variant v01 --prompt "Same framing, same light. Replace …"
```

### `juicy video generate`

Animate an approved first frame into a clip Image-to-video. The prompt describes only the motion. The default model always generates clip audio and takes 5–15 s. `juicy catalog list --role motion` shows every model, what it is best for and what it costs, and --model picks one. Output: .media/video/<variant>.mp4 with a manifest record whose `from` names the frame.

```
juicy video generate --image <path> --duration <n> --variant <name> [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--role <motion>` | string |  | "motion" | motion | Catalog role |
| `--model <id|alias>` | string |  |  |  | Model for this role, by id or alias; `juicy catalog list --role <role>` shows the choices |
| `--image <path>` | string | yes |  |  | The approved first frame (local path, uploaded for you) |
| `--prompt <text>` | string |  |  |  | The prompt |
| `--prompt-file <path>` | string |  |  |  | Read the prompt from a file |
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--campaign <name>` | string |  |  |  | Campaign label recorded in the manifest and ledger |
| `--max-cost <credits>` | integer |  |  |  | Refuse before submitting if the quote exceeds this many credits |
| `--preset` | boolean |  | on |  | Apply the ad-safe preset: no on-image text, logos or device UI |
| `--force` | boolean |  | off |  | Generate again even if the manifest already has this exact input |
| `--wait` | boolean |  | on |  | Poll until the job finishes |
| `--idempotency-key <key>` | string |  |  |  | Override the idempotency key (defaults to the input hash) |
| `--duration <n>` | integer | yes |  |  | Clip length in whole seconds; the range depends on the model (default model: 5–15) |
| `--seed <n>` | integer |  | 1 |  | Seed, recorded in the manifest; --force draws a fresh one unless this is given |
| `--variant <name>` | string | yes |  |  | Variant name; the output is .media/video/<variant>.mp4 |
| `--resolution <360p|480p|540p|720p|768p|1080p|4k>` | string |  | "720p" | 360p \| 480p \| 540p \| 720p \| 768p \| 1080p \| 4k | Output resolution; which values a model accepts is in the catalog |
| `--with-audio` | boolean |  | off |  | Let the model generate clip audio, on models with an audio switch (off by default); the default model always generates it |
| `--multi-clip` | boolean |  | off |  | Allow the model's multi-clip camera changes (off by default; models with a multi-clip switch only) |
| `--negative-prompt <text>` | string |  |  |  | Appended to the preset's negative prompt |
| `--timeout <duration>` | string |  | "20m" |  | How long to wait |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed · 4 still running (job JSON on stdout, run `next`) · 5 insufficient credits

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy video generate --image .media/first-frames/v03.png --duration 12 --variant v03 --prompt "slow push-in, hands lift…" --project .
```

### `juicy audio music`

Generate a soundtrack Text-to-music. The model has no seed, so the same prompt does not reproduce the same track; --force is the only way to get a second take and it is recorded as a new attempt. Output: .media/audio/<name>.<ext>.

```
juicy audio music --duration <n> --name <name> [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--role <soundtrack>` | string |  | "soundtrack" | soundtrack | Catalog role |
| `--model <id|alias>` | string |  |  |  | Model for this role, by id or alias; `juicy catalog list --role <role>` shows the choices |
| `--prompt <text>` | string |  |  |  | The prompt |
| `--prompt-file <path>` | string |  |  |  | Read the prompt from a file |
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--campaign <name>` | string |  |  |  | Campaign label recorded in the manifest and ledger |
| `--max-cost <credits>` | integer |  |  |  | Refuse before submitting if the quote exceeds this many credits |
| `--force` | boolean |  | off |  | Generate again even if the manifest already has this exact input |
| `--wait` | boolean |  | on |  | Poll until the job finishes |
| `--idempotency-key <key>` | string |  |  |  | Override the idempotency key (defaults to the input hash) |
| `--duration <n>` | integer | yes |  |  | Track length in whole seconds |
| `--name <name>` | string | yes |  |  | Track name; the output is .media/audio/<name>.<ext> |
| `--timeout <duration>` | string |  | "10m" |  | How long to wait |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed · 4 still running (job JSON on stdout, run `next`) · 5 insufficient credits

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy audio music --duration 30 --name bed --prompt "upbeat, bright, no vocals" --project .
```

### `juicy job get`

Show a job; with --wait, poll it; with --project, freeze its output The resume path after exit 4. With --project and a succeeded job, downloads the output, freezes it under .media/ and appends the manifest record exactly as the originating command would have.

```
juicy job get <job_id> [options]
```

Arguments:

- `<job_id>` — The job id

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--wait` | boolean |  | off |  | Poll until terminal |
| `--timeout <duration>` | string |  | "20m" |  | How long to wait |
| `--project <dir>` | string |  |  |  | Freeze the output into this project's .media/ |
| `--variant <name>` | string |  |  |  | Override the variant recorded at submit |
| `--name <name>` | string |  |  |  | Override the audio name recorded at submit |
| `--fields <a,b>` | string |  |  |  | Comma-separated fields to keep in the output |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed · 4 still running (job JSON on stdout, run `next`)

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy job get <job_id>
```

### `juicy job cancel`

Cancel a queued or running job

```
juicy job cancel <job_id>
```

Arguments:

- `<job_id>` — The job id

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

### `juicy sample list`

List the free sample assets (no sign-in needed)

```
juicy sample list [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--fits <blueprint>` | string |  |  |  | Only samples that fit this blueprint |
| `--kind <image|video|audio>` | string |  |  | image \| video \| audio | Only this kind |
| `--fields <a,b>` | string |  |  |  | Comma-separated fields to keep in the output |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy sample list
```

### `juicy sample get`

Download a sample into the project and record it (zero credits) Verifies the sha256, freezes the file under .media/ like a generated asset, and appends a manifest record with source "juicy-sample". Never overwrites.

```
juicy sample get <sample_id> [options]
```

Arguments:

- `<sample_id>` — From `juicy sample list`

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--variant <name>` | string |  |  |  | Variant name for an image or video (default: the sample id) |
| `--name <name>` | string |  |  |  | Name for an audio track (default: the sample id) |
| `--force` | boolean |  | off |  | Download again even if the manifest already has this sample |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy sample get person-clapping-9x16-12s --project . --variant v01
```

### `juicy manifest verify`

Check that every manifest record points at a frozen local file The mechanical Step 3 gate: every record's file exists and matches its sha256, nothing references a remote URL, every video's `from` is a recorded first frame. Exit 1 if any check fails.

```
juicy manifest verify [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--project <dir>` | string |  | "." |  | Project directory holding .media/ |
| `--require-video` | boolean |  | off |  | Every first-frame variant must also have a video record |
| `--strict` | boolean |  | off |  | Fail records whose source is not juicy or juicy-sample |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: none; this command runs locally.

Example:

```bash
juicy manifest verify --project .
```

### `juicy doctor`

Check the local setup: credentials, API, contract, catalog, samples, project

```
juicy doctor [options]
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--project <dir>` | string |  |  |  | Also check that this project's .media/ is writable |
| `--expect-version <x.y.z>` | string |  |  |  | Fail unless the installed version equals this |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: required. In a sandbox that blocks the network, allow it before running this command.

Example:

```bash
juicy doctor
```

### `juicy completion`

Print a shell completion script

```
juicy completion <shell>
```

Arguments:

- `<shell>` — bash or zsh

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: none; this command runs locally.

Example:

```bash
eval "$(juicy completion zsh)"
```

### `juicy skill`

Write the generated SKILL.md and command reference for agents Used by the plugin build, not by end users. Writes <dir>/juicy-cli/SKILL.md and <dir>/juicy-cli/references/commands.md from the command specs.

```
juicy skill --dir <path>
```

| Flag | Type | Required | Default | Values | Description |
|---|---|---|---|---|---|
| `--dir <path>` | string | yes |  |  | Output directory |

Exit codes: 0 ok · 1 API/network · 2 usage · 3 sign-in needed

Network: none; this command runs locally.

Example:

```bash
juicy skill --dir ./out
```
