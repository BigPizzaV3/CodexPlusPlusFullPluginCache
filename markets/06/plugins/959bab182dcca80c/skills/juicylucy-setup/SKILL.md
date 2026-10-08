---
name: juicylucy-setup
description: "Set up or repair the local tools JuicyLucy's ad production needs — Node, the hyperframes CLI, ffmpeg, headless Chrome, the `juicy` generation command and its sign-in, and the environment Codex passes to commands. Use when an ad workflow's preflight (`doctor.sh --preflight`) reports the machine is not set up, when a render or generation fails because `hyperframes` or `juicy` is missing, when `juicy` reports no session or no credits, when a newer `juicy` is out or its skill is stale, when a first-time user asks to get started or a plugin update asks for setup again, or when ads aren't working on someone's machine. Also the home of references/extending.md and the brand template: read it when an ad workflow finds no brand installed, or to add or change a brand, the conventions, or how ads are made on this machine. Installs tools under ~/.juicylucy and a generated command skill under ~/.agents/skills, with no administrator password and no Homebrew. Formerly /adframes-setup."
---

# JuicyLucy setup

> **This runs in Codex on a Mac.** If there is no local shell here — the request came from
> ChatGPT on the web or on a phone — say that setup installs tools on the user's own Mac
> inside Codex, point them there, and stop.

Get one machine ready to make ads. The person running this is usually **not technical** — they want
working software, not a tour of the toolchain. So: check first, explain what is missing in plain
words, ask before installing anything, then verify.

Everything lands in **`~/.juicylucy/`**. No administrator password, no Homebrew, no Xcode tools.
Deleting that one folder undoes the whole install — plus one more, `~/.agents/skills/juicy-cli`,
which is not a download but the `juicy` command's own description of itself (Step 3).

**Older installs.** Before plugin 0.12.0 the same toolchain lived in `~/.adframes/`, under the
video side's old internal name. Nothing reads that folder any more. A machine that has one is set
up again from scratch here — the downloads are the same size as the first time — and the old folder
can be deleted once the doctor reads clean. Do not move or reuse it. The product is called
JuicyLucy; use that name for all of this when talking to the user.

## The rules of this workflow

1. **Diagnose before you touch anything.** Always run the doctor first, even if the user has told
   you what is broken.
2. **Ask before each install — and only before an install.** Downloading 200 MB onto someone's
   machine is a judgement call, so say what it is and roughly how big it is, and never install
   something the doctor did not report as missing. Everything else here — running the doctor,
   reading `config.toml`, re-running the doctor to verify — is reversible and decides nothing, so
   just do it. § Do not make the user click through your own work.
3. **Never use `sudo`.** If a step seems to need it, you have the wrong step — the whole design
   avoids it. Stop and say so.
4. **Explain in ordinary words.** "The video encoder is missing, I'll download it into your JuicyLucy
   folder" — not "ffprobe is not on PATH".
5. **Verify by re-running the doctor**, not by assuming the install worked.
6. **Never send the user to Terminal.** Nothing here needs it: no Xcode Command Line Tools, no
   Homebrew, no `xcode-select --install`, and not the sign-in either — `juicy` tells you how to do
   that from here. If a step seems to need Terminal, it is the wrong step — stop and say so.
7. **One restart, at the end.** Install everything, write `config.toml` once, check the file with the
   doctor, then ask for the restart. Never ask for one before Step 3 has finished.

## Do not make the user click through your own work

A first-time user reads every prompt as a decision they are supposed to understand. Spend that
attention only where their answer changes what happens.

**Ask when the answer changes the outcome:** installing software, editing `config.toml`, the paid
half of the smoke test, anything that costs money or cannot be undone by deleting `~/.juicylucy`.

**Do not ask — just do it, and say what you did:** running either script here, reading a file to
find out what is already configured, listing a directory, re-running the doctor. If the runtime
puts up its own approval prompt for one of these — a folder that happens to sit inside iCloud or
Google Drive, say — that is the sandbox asking, not a question you should be forwarding or
elaborating on. Approve what the step needs and keep going.

The failure this prevents: a setup that reads as an interrogation, where the user approves nine
things they cannot evaluate and then cannot tell which one mattered.

## Step 1 — diagnose

```bash
sh "$JUICYLUCY_SKILL_DIR/scripts/doctor.sh"
```

`$JUICYLUCY_SKILL_DIR` is this skill's own directory. If you do not know it, find it — the skill is
installed under a plugin cache, e.g.
`~/.codex/plugins/cache/juicylucy/juicylucy-ads/*/skills/juicylucy-setup`.

Each line is `name  ok|missing  detail`. Read the summary at the end. If everything is `ok`, say so
in one sentence and stop — do not install anything.

**Arriving from an ad run.** Both ad workflows run this doctor as `--preflight` before their
Step 0: the same lines, without the registry call, plus a final `preflight` line whose verdict and
exit code count only the toolchain — `node`, `hyperframes` and `hf-version`, `ffmpeg`, `ffprobe`,
`ffmpeg-on-path`, `adspython`, `juicy`, and `on-path`, whether the bare commands the skills run
resolve on Codex's PATH. A `preflight missing` is how a run that was asked for an ad
ends up here. Treat it as a first-time setup: run the full doctor anyway (rule 1), take every step
through to the restart, and say that the ad is asked for again after it — the ad run wrote nothing,
so nothing needs carrying over. A `preflight ok` beside other `missing` lines (a sign-in, a config
line, a newer `juicy`) never sends a run here on its own; the run names them in its reply, and they
are fixed here when the user asks.


## Step 2 — explain, and ask

Tell the user only about the things that are missing, in the order the doctor lists them, and what
each one is for. Before anything is installed, `ffmpeg-on-path`, `env`, `config`, `network` and
`writable` will all read `missing` — that is one item, the config block of Step 4, not five problems
to fix now:

| Missing              | Say roughly                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| `node`               | "The runtime everything else needs." Only downloaded when the machine has none v22+; say so.      |
| `hyperframes`        | "The program that turns the ad into a video file. About 200 MB with its extras."                  |
| `ffmpeg` / `ffprobe` | "The video encoder. About 80 MB."                                                                 |
| `chrome`             | "A headless browser used to draw each frame. About 150 MB, downloaded by hyperframes itself."     |
| `adspython`          | "A private copy of Python the static-ad checks run through. About 25 MB."                         |
| `juicy`              | "The command that makes the images, video clips and music. A small download."                     |
| `juicy-version`      | "A newer version of the generation command is out." The juicy step installs it; it is small and needs no sign-in again. |
| `juicy-skill`        | Not a decision for the user: the skill that tells the agent how to use `juicy` is missing, or was written by a different version than the one installed. Say so and re-run setup's juicy step, which writes it. |
| `juicy-login`        | "Signing in to your JuicyLucy account." Not a download; `juicy auth help` says what to ask for — § Signing in. |
| `env` / `config` / `network` / `writable` | "A settings block I write into Codex's config file, so commands find the tools and the generation command can reach the internet and keep its sign-in." Not a download. |
| `on-path`            | The same item, seen from the commands' side: the tools are installed but Codex's `PATH` does not reach them, because the block was never written or Codex was not restarted after it was. Step 4, then one restart. |

| `skills`             | Not a download. An extra `juicy-cli` copy overrides the generated command reference. Check it against the installed binary. Intentional workflow customizations are reported as `ok`; preserve them — `references/extending.md` § Changing how the ads are made. |

Then ask permission to install the ones that can be installed.

## Step 3 — install

```bash
sh "$JUICYLUCY_SKILL_DIR/scripts/install.sh"
```

It is idempotent: it skips whatever is already present, so it is safe to re-run after a failure.
Pass `--only node`, `--only tools`, `--only juicy`, `--only chrome`, or `--only python` to do one
part. The juicy step is the exception to "skips whatever is present": it asks the registry for the
newest published `juicy` every time it runs, which is how an update happens, and then has that
`juicy` write the skill describing itself into `~/.agents/skills/juicy-cli` — the one thing setup
writes outside `~/.juicylucy`. Codex reads a user's own skills from that folder, and a skill there
with a shipped skill's name replaces the shipped one, so the flags the agent reads are always the
flags of the command it runs; the plugin's own `juicy-cli` skill is only the fallback until this
step has run. Codex reads the folder at launch: on a first setup that is Step 4's restart; after a
later update of `juicy` alone, it is one more quit-and-reopen. The python step provisions `adspython`, the interpreter the statics engine's QA scripts run through —
a standalone Python unpacked under `~/.juicylucy/python`, the same way Node is. It never runs the
Mac's own `python3`, which on a fresh machine is a stub that opens Apple's Command Line Tools
installer and asks the user to finish in Terminal.

It never edits any config file. When it finishes it prints what still has to go into
`config.toml` — carry that into Step 4.

## Step 4 — the environment, the network switch, and the sign-in

Codex passes environment variables to commands from `~/.codex/config.toml`, **not** from the user's
shell profile. A GUI-launched app does not reliably read `.zshrc`, so a value exported there will
look set in a terminal and be missing in the app. Read `references/environment.md` and merge the
block `install.sh` printed into `[shell_environment_policy.set]` — merge into the existing table if
there is one, never add a second table with the same name.

**Write `PATH` exactly as printed.** Codex takes the value literally and does not expand `${PATH}`
or `$PATH`; a value that ends in either leaves every command Codex runs without `/usr/bin`, which
surfaces later as `curl: command not found` in the middle of something unrelated. The printed list
already includes the system directories.

**The sandbox table goes in the same file.** Codex's sandbox blocks every network host and every
write outside the project folder by default, which is fine for rendering and fatal for `juicy`: it
has to reach the generation service, and it keeps its session and catalog cache under
`~/.juicylucy`, and setup's juicy step writes `juicy`'s skill under `~/.agents/skills`. Merge the
`[sandbox_workspace_write]` table `install.sh` printed — `network_access = true` and
`writable_roots = ["…/.juicylucy", "…/.agents/skills"]` — into `config.toml`, into the existing
table if there is one, adding to an existing `writable_roots` list rather than replacing it.
`references/environment.md` § The sandbox says why; without it the sign-in fails with a permission
error, every generation call either fails to connect or asks the user to approve it, one call at a
time, in the middle of an ad, and the juicy step cannot write its skill.

**Then re-run the doctor before asking for a restart.** Its `config`, `network` and `writable` lines
read the file, not the process, so a wrong `PATH` or a missing line shows up now — while it costs
one edit — instead of after a restart as an `env` failure that costs another. `env` itself will
still read `missing` until the restart; that is expected. Fix anything those three name, then go on
to the sign-in.

### Signing in

Generation is paid for by the user's JuicyLucy account, and `juicy` keeps the session for it in
`~/.juicylucy/juicy/credentials` — one file on this machine, mode 600, outside any project or git
repository, and never anything in `config.toml`.

**How a user signs in belongs to `juicy`, not to this skill**, because it will change — today it is
an email and a password, given here in the conversation; a later version opens the browser instead.
So do not work from memory. Run

```bash
~/.juicylucy/bin/juicy auth help
```

— the full path, because the restart that puts `~/.juicylucy/bin` on `PATH` has not happened yet —
and follow what it prints: the method this version uses, what to ask the user for, the exact
command, and what never to do with what they gave you. Say what happens before you ask, in your own
words: the session stays on this Mac in that one file, `juicy` sends it only to JuicyLucy's own
service on their own generation requests, and `juicy auth logout` or deleting `~/.juicylucy` ends
it. Whatever method `auth help` names, three things hold:

- **The user never leaves this conversation for it.** No Terminal (rule 6).
- **What the user gives you is for that one command.** Never repeat it back, never write it into a
  file, a project or `config.toml`, never keep it once the command has run.
- **Accounts are created by a JuicyLucy administrator; there is no sign-up.** A user without one asks
  their account owner, and this setup stops here until they have it.

Then check it took: re-run the doctor and read `juicy-login`. It runs `juicy auth status`, which asks
the service whose session this machine holds, so `ok signed in as …` means the sign-in worked, before
any restart. From a sandbox with the network off the question cannot be asked, and the line says
exactly that — `ok`, a session is on this machine, *not confirmed* — rather than `missing`. **Only
`missing not signed in` means the user has to sign in.** Never ask for an email or a password on any
other wording of that line: run `juicy auth status` with the network approved and read its answer.

### Then restart Codex

**`config.toml` is read once, at startup.** Nothing you just wrote is in effect until Codex is
restarted, and Step 5's doctor will report `env missing` on a stale process — which reads like the
edit failed when it only has not been loaded. This is the only restart in the whole setup: the
environment block and the sandbox table both landed in the file in this step, and the doctor's
`config`, `network`, `writable` and `juicy-login` lines already confirmed them, so nothing should
need a second one.

**The sign-in itself needs the restart first** when `writable` was missing: until Codex reloads the
file, its sandbox still refuses `juicy` the folder it writes the session to, and `juicy auth login`
fails with a permission error. In that case ask for the restart now, and sign in as the first thing
after it — then verify.

This is the one point in the whole setup where the user has to do something you cannot do for them.
Say so plainly — *"quit Codex and open it again, then tell me and I'll check the rest"* — and stop
there. Do not run Step 5 in the same session and do not present the restart as optional.

## Step 5 — verify

Once Codex has been restarted, re-run the doctor. Every line should read `ok` — `env` now that the
process has the block, `config`, `network`, `writable` and `juicy-login` as they already did (or
sign in now, if the restart came first — § Signing in), and `juicy-version` now able to reach the
registry, which it may not have been before `network` was on. Then confirm the toolchain agrees:

```bash
PATH="$HOME/.juicylucy/node/bin:$PATH" "$HOME/.juicylucy/node_modules/.bin/hyperframes" doctor
```

The `PATH` prefix is harmless when `~/.juicylucy/node` does not exist — the installer only creates it
when the machine had no suitable Node of its own. Its own report should show FFmpeg, FFprobe, and
Chrome all found. Ignore the optional rows it flags
— whisper-cpp, Kokoro, MusicGen, and Docker are not needed to make an ad.

A session that exists is not yet a session that works, and a machine that runs `juicy` is not yet
one that reaches the service. Finish with two commands in a scratch folder. The first is free and
proves the download path; the second spends a few credits and proves generation, so say so and ask
before it (rule 2):

```bash
juicy sample get person-clapping-9x16-frame --project /tmp/juicy-smoke
juicy image generate --role first-frame --aspect 9:16 --variant smoke --max-cost 100 \
  --prompt "a plain grey studio backdrop with soft light, empty, no people" --project /tmp/juicy-smoke
```

Each prints one JSON record with a `path`; a file at that path means the setup is done. Exit `3`
means the sign-in did not take — back to § Signing in. Exit `5` means the account has no credits,
which is the account owner's to fix, not this machine's. Anything else: send the JSON it printed to
whoever maintains the plugin. Delete the scratch folder afterwards.

Tell the user they are ready, and that the next thing to say is what ad they want.

## Extending it, on this machine

When an ad workflow finds no brand installed, when the user asks for a brand that is not
installed, wants a shipped brand or the conventions changed, or wants the ads made differently,
read `references/extending.md` before doing anything. The short version: the plugin is read-only,
and every folder of it is replaced by the next update. The user's own skills live in
`~/.agents/skills`, and a skill there with a shipped skill's name replaces the shipped one on this
Mac. A first brand is made there from `references/brand-template/`; brands may be added or
replaced that way, and conventions and workflow skills may be customized the same way.
Explain that local replacements survive updates but do not receive later shipped changes.
Keep intentional customizations during setup and repair.
The doctor's `skills` line is the inventory of what is local. A local change reaches teammates only
by sharing it internally under the licence or landing it in the plugin's repo. Remove a local
copy only when the user wants to return to the shipped behavior.

## When it still does not work

- **A render fails on a codec or format.** The bundled encoder is an older build (ffmpeg 6). It is
  enough for ordinary ads; if a specific render rejects it, a current ffmpeg from Homebrew and a
  matching `HYPERFRAMES_FFMPEG_PATH` is the fallback.
- **`hyperframes` is found but skills keep changing.** `HYPERFRAMES_SKIP_SKILLS` is not reaching the
  command. Re-check Step 4 — this is almost always a shell profile that Codex never reads.
- **`juicy` exits `3` (`no_credentials`, `session_expired`).** The session is missing or was revoked;
  nothing is broken. Sign the user in again (§ Signing in: `juicy auth help`). Do not reinstall
  anything.
- **`juicy` exits `5` (`insufficient_credits`).** Nothing on this machine is wrong: the account has no
  credits, and the account owner adds them. Say that and stop — do not retry, and do not look for
  a plan or a checkout; there is none in the plugin.
- **The doctor says `juicy-version missing`.** A newer `juicy` has been published than the one
  installed. `install.sh --only juicy` installs it and rewrites its skill; it is quick, it needs no
  sign-in again, and Codex reads the new skill after one quit-and-reopen. When the line instead
  reads `ok` with "could not reach the registry", nothing is wrong with the machine — the check
  needs the `network` line on, and a Codex restart after it was written.
- **The doctor says `juicy-skill missing`.** `~/.agents/skills/juicy-cli` is absent, or was written
  by a different version of `juicy` than the one installed — after an update, or on a machine set
  up before the step wrote it. Same fix: `install.sh --only juicy`, then quit and reopen Codex.
  Never edit that folder by hand; `juicy` regenerates it whole.
- **Every generation call asks for approval, or cannot connect.** The `network` line: `config.toml`
  lacks `network_access = true` under `[sandbox_workspace_write]`. Add it (Step 4) and restart
  once. When the line reads `ok` *and* adds "this command ran with the network off" after that
  restart, the file is right and this Codex is not applying it — a client that sends its own sandbox
  with each thread (Codex Desktop, measured on 0.151–0.154) never reads the table. Nothing on the
  machine needs fixing: request the network for each `juicy` command and let the user approve it,
  once per command or for `juicy` as a whole. `juicy` fails with `network` (exit 1) until then.
- **The doctor says `juicy-login ok … not confirmed`.** A session is on this machine and the doctor
  could not reach the service to confirm it — almost always the case above. **The user is signed
  in as far as anyone can tell; do not ask them to sign in again.** `juicy auth status`, run with
  the network approved, prints the account and the balance.
- **The sign-in fails with `EPERM` / "operation not permitted" on a `mkdir` under `~/.juicylucy`,
  or the juicy step fails the same way under `~/.agents/skills`.** The `writable` line: the sandbox
  refuses `juicy` its own folder, or setup the skill folder. `writable_roots` in
  `[sandbox_workspace_write]` must list both absolute paths (Step 4) — a machine set up before
  0.20.0 has only the first; restart once, then sign in or re-run the juicy step.
- **`curl: command not found`, or `git`, or `tar`, inside Codex — on a machine set up before
  0.12.2.** The config's `PATH` ends in `${PATH}`, which Codex never expanded, so the commands have
  no `/usr/bin`. The doctor's `config` line names it. Replace the `PATH` value with the full list
  `install.sh` prints (re-run it with `--only python` if you need the print-out; it changes
  nothing already installed) and restart once.
- **Nothing at all runs after installing.** The user may be on an Intel Mac; the doctor prints the
  architecture it detected. Everything here supports both, but check that line before digging.
