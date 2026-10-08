# The environment, and why it does not go in a shell profile

Codex passes environment variables to the commands it runs from
**`~/.codex/config.toml`**, under `[shell_environment_policy.set]`. It does not source the user's
`.zshrc`.

That distinction is the single most confusing failure in this whole setup, because a variable
exported in `.zshrc` **looks correct**: the user opens Terminal, runs `echo $HYPERFRAMES_FFMPEG_PATH`,
sees the path, and reasonably concludes it is set. Meanwhile the app launched from the Dock never
read that file, so a render fails on a missing encoder that appears to contradict what they just
saw. Put it in `config.toml` and both agree.

## The block

```toml
[shell_environment_policy.set]
HYPERFRAMES_FFMPEG_PATH = "/Users/<you>/.juicylucy/node_modules/ffmpeg-static/ffmpeg"
HYPERFRAMES_FFPROBE_PATH = "/Users/<you>/.juicylucy/node_modules/@ffprobe-installer/darwin-arm64/ffprobe"
HYPERFRAMES_SKIP_SKILLS = "1"
HYPERFRAMES_NO_TELEMETRY = "1"
PATH = "/Users/<you>/.juicylucy/bin:/Users/<you>/.juicylucy/node/bin:/Users/<you>/.juicylucy/node_modules/.bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
```

`install.sh` prints this with the real paths already filled in. On an Intel Mac the ffprobe path ends
`darwin-x64/ffprobe` instead; on a machine that has Homebrew, `/opt/homebrew/bin` is appended last.

**`PATH` is the whole list, not an addition.** Codex does not expand variables in these values:
`${PATH}` and `$PATH` stay as those literal characters (verified on codex-cli 0.151), so a value
that ends in either replaces the entire `PATH` with our three directories and a junk entry. Every
command Codex then runs is missing `/usr/bin` — `curl`, `git`, `tar`, `python3` — and the failure
shows up far from its cause, as `command not found` in the middle of an ad run. Versions before
0.12.2 wrote exactly that, which is why the doctor's `config` line now checks for it.

**Merge, do not append.** If `[shell_environment_policy.set]` already exists — it often does — add
these keys inside it. A second table with the same name is invalid TOML and Codex will refuse the
whole file, which looks like a much bigger breakage than it is.

## What each one does

| Variable                                               | Why                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HYPERFRAMES_FFMPEG_PATH` · `HYPERFRAMES_FFPROBE_PATH` | Point hyperframes at the encoders we installed under `~/.juicylucy`, so no system ffmpeg and no Homebrew is needed. `packages/parsers` reads these before it scans `PATH`.                                                                                                     |
| `HYPERFRAMES_SKIP_SKILLS`                              | Stops `hyperframes init` and `skills update` from fetching upstream's skills into `~/.agents/skills`, where they sit at a higher priority than the plugin's copies and can shadow them. Without this the toolchain quietly reinstalls the problem the plugin exists to solve. |
| `HYPERFRAMES_NO_TELEMETRY`                             | **Not optional.** The CLI reports usage to PostHog by default. Our compositions carry client ad copy, so we opt out unconditionally.                                                                                                   |
| `PATH`                                                 | Our encoders first, then our Node and the `hyperframes` command, then the system directories spelled out, because nothing here is appended to an existing value. `bin/` leads even the Node directory: when the Node in use is Homebrew's, that directory also holds Homebrew's ffmpeg. |

## Why `~/.juicylucy/bin` is on that list

`ffmpeg-static` and `@ffprobe-installer/ffprobe` expose their binaries as package
exports and declare no `bin`, so npm writes no shim: `node_modules/.bin` ends up with
`hyperframes` and no `ffmpeg`. `install.sh` therefore symlinks both encoders into
`~/.juicylucy/bin` itself.

Without that directory, `HYPERFRAMES_FFMPEG_PATH` still makes *hyperframes* work while a
bare `ffmpeg` resolves to whatever the system has — which is the wrong program with
different filters, or on a machine set up by this script, nothing at all. The ad skills
run ffmpeg and ffprobe directly in several places (probing a reference, dumping a contact
sheet, pulling a first frame to edit, confirming a render is not silent), so both paths
have to lead to our build.

This is not hypothetical. On a real run the agent reached Homebrew's ffmpeg, which is
built without libfreetype, hit `drawtext: Filter not found`, and abandoned the render
path rather than the binary. `doctor.sh` now checks bare `ffmpeg` separately from
`HYPERFRAMES_FFMPEG_PATH` for exactly this reason, and reports which build won.

## The sandbox

Codex runs commands inside a sandbox whose default blocks every network host and every write outside
the project folder (plus `/tmp`). That is fine for rendering, which is local and writes into the
project, and fatal for `juicy` three times over: it has to reach JuicyLucy's generation service, it
keeps its session and catalog cache in `~/.juicylucy/juicy/` — observed as `EPERM: operation not
permitted, mkdir '…/.juicylucy/juicy'` at the sign-in, and as connection failures or an approval
prompt per generation call otherwise — and setup's juicy step writes the skill describing the
installed `juicy` into `~/.agents/skills/juicy-cli`, which a roots list holding only `~/.juicylucy`
refuses with `Operation not permitted` (measured on codex-cli 0.154.0). One table in the same
`config.toml` fixes all three:

```toml
[sandbox_workspace_write]
network_access = true
writable_roots = ["/Users/<you>/.juicylucy", "/Users/<you>/.agents/skills"]
```

`install.sh` prints it with the real paths — each folder's physical path, because Codex refuses a
root that resolves through a symlink and rejects the whole sandbox when one does. `writable_roots`
takes absolute paths and is a list: if one is already there, add ours to it rather than replacing
it. Merge into the table if it already exists. A machine set up before 0.20.0 has the first root
and not the second; the doctor's `writable` line says which is missing. Like everything else in this file it is read at startup, so it takes effect after the
restart; the doctor's `network` and `writable` lines read the file and report it before. The
sign-in is the first thing that needs it, so when `writable` was missing the restart comes before
`juicy auth login`, not after.

## Signing in

Nothing about generation goes in `config.toml`. `juicy` keeps the user's session in
`~/.juicylucy/juicy/credentials` (mode 600), written by `juicy auth login`. How that sign-in goes —
what to ask the user for, the command — is printed by `juicy auth help` and followed from there
(`../SKILL.md` § Signing in), because the method belongs to the CLI and will change. There is no key
to paste, no environment variable to set, and nothing for the agent to write into this file; the
doctor's `juicy-login` line runs `juicy auth status`, which reads that file and asks the service to
confirm it.

## Checking it took effect

Two doctor lines cover this block, and they answer different questions:

- **`config`** reads `config.toml`. It turns `ok` the moment the block is written correctly — every
  key present, `PATH` complete and free of `${PATH}` — and names what is wrong otherwise. Run the
  doctor right after writing the file, before any restart; this is what keeps the setup at one
  restart.
- **`env`** reads the running process. It turns `ok` only after Codex is restarted. If it still reads
  `missing` after a restart while `config` reads `ok`, the file Codex loaded is not the one that was
  edited — a second `[shell_environment_policy.set]` table it refused, or a different `CODEX_HOME`.

`network` and `writable` behave like `config`: they read the file, so they are `ok` as soon as the
table is written. `juicy-login` asks `juicy` about the session file `juicy auth login` writes — which
the sandbox only allows once Codex has reloaded the table, so on a machine that lacked `writable` the
order is: write the table, restart, sign in, verify.

Both `network` and `juicy-login` also say when the file and the process disagree. Codex marks a
process whose network it has cut with `CODEX_SANDBOX_NETWORK_DISABLED=1`. With the table written and
that mark still set after the restart, the Codex in use is not applying the table — a client that
sends its own sandbox with each thread does not read it (Codex Desktop, measured on 0.151–0.154:
every thread ran network-off with the table in place, while `codex sandbox` with
`sandbox_mode = "workspace-write"` honoured it, codex-cli 0.154.0). `network` then reads `ok … but this command ran with the network
off`, and `juicy-login` reads `ok … not confirmed` instead of claiming the user is signed out: the
session file is there, and `juicy` could not reach the service to confirm it. The remedy is approval
— `juicy` commands request the network and the user allows it — not another edit and not another
sign-in.
