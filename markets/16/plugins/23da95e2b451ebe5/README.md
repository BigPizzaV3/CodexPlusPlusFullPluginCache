# Token Tally — desktop prototype 0.4.6

Checking the signed-in account's reported token usage automatically exports a 1080 × 1350 PNG with a matching editable Tesseract composition.

## Status

Tested on macOS with the local Codex app server: live account retrieval and PNG export both passed. Not published, not reviewed for the public plugin directory, and not tested on Windows or Linux. The underlying app-server interface is experimental. Mobile can initiate work through a connected desktop; execution still happens on that desktop.

## Requirements

- A local ChatGPT Work/Codex environment with shell access.
- Python 3.10+ and the Codex CLI, signed in with an eligible account backed by Codex services. API-key-only accounts are not supported by this account-usage endpoint.
- For card export: Tesseract CLI **0.3.1**. Inter Display 4.1 fallback fonts are bundled under the SIL Open Font License; no separate font installation is required. Existing SF Pro Display fonts are preferred when present. The renderer is installed through guided setup and is not bundled.
- Network access for account retrieval, local app-server state permissions, and GPU access for rendering. Existing host approval rules still apply.

Official references:
- https://learn.chatgpt.com/docs/app-server#7-token-usage-chatgpt
- https://developers.openai.com/plugins/build/plugins
- Tesseract 0.3.1: https://github.com/mirage-hq/tesseract/releases/tag/v0.3.1

## Local installation

This folder is a portable plugin with `plugin.json` and a skill under `skills/token-tally/`.

Copy it into a local marketplace root as `plugins/token-tally`. Merge this entry into that root's `.agents/plugins/marketplace.json` (do not overwrite an existing catalog):

```json
{
  "name": "token-tally-local",
  "plugins": [
    {
      "name": "token-tally",
      "source": {"source": "local", "path": "./plugins/token-tally"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
      "category": "Productivity",
      "interface": {"displayName": "Token Tally"}
    }
  ]
}
```

Register the marketplace root with `codex plugin marketplace add /absolute/path/to/root`, then install from the desktop Plugins Directory. Restart/refresh the app if necessary. Local marketplace registration and installation passed using Codex CLI. The installed cached plugin passed live account retrieval and card export with bundled fonts. The desktop setup-button UI and first-time renderer download remain untested.

After installation, ask **“Check my token stats”** or **“Create my Token Tally share card.”**

## Direct use before installation

From this plugin folder:

```sh
python3 skills/token-tally/scripts/token_tally.py stats \
  --output /absolute/path/usage.json \
  --card-dir /absolute/path/new-card-folder \
  --tsrct /absolute/path/to/tsrct
```

The stats command generates the social card by default. Pass `--no-card` only for an explicit numbers-only request. If export fails, the JSON snapshot is retained; use the `card --snapshot ... --output-dir ... --tsrct ...` command to retry without re-fetching.

Use a fresh snapshot filename and card output directory. Existing exports are preserved. The `--codex`, `--font-regular`, and `--font-semibold`, and `--font-bold` flags allow explicit dependency locations.

## Data and design

The collector stores only returned usage summary fields, daily date/token buckets, retrieval time, and a source label. It does not extract credentials or conversation text, run a model turn, or upload data to a Token Tally service. The app server handles authentication and may update its normal local state.

Missing values remain unavailable, never zero. Daily records count returned buckets; it is not presented as active days. The card shows lifetime tokens, highest daily usage, current streak, and longest agent turn. Only lifetime usage has an exact total beneath the abbreviated number. Longest turn is one user request and the ensuing agent work, not user screen time; treatment of idle or approval waits is undocumented. Durations of an hour or more omit seconds. Snapshot dates are UTC. The encoded source marker is descriptive metadata, not tamper-proof verification.

The card's invitation is design copy; there is no public signup URL yet. No leaderboard, donation checkout, or recurring sync is enabled in this version. Public distribution still needs directory submission/review, onboarding integration testing, and testing across supported host environments.

The exported editable `.tsrct` embeds the chosen fonts. For SF Pro exports, distribute it only where the font license permits. Bundled Inter Display is provided under its included SIL Open Font License. PNG sharing does not distribute font files.


The card footer shows “@tokentally what’s my tally?” with instructions to install Token Tally and try it in a new Codex chat. This is intended release copy; this prototype has not been published to the plugin directory.

## Guided renderer setup

The manifest registers `skills/token-tally-setup/SKILL.md` as the onboarding workflow. It detects the pinned renderer, prepares the renderer as part of a card request when needed, downloads the matching public release, verifies SHA-256, installs with the official installer (in a separate Token Tally prefix on macOS), and checks the version before continuing. The card skill also routes to setup on first use. This is an agent-guided workflow, not a silent install-time hook. Host permissions still apply. Setup registration and instructions have been validated, and the package installed successfully through Codex CLI; the desktop onboarding UI has not been tested. Bundled Inter Display provides an automatic fallback when SF Pro is absent.

## Discreet record mark

The bottom-right mark replaces the human-readable source/date footer. Format: `T1A.<base36 exact tokens>.<base36 Unix seconds>.<8 uppercase SHA-256 hex characters>`. T1S denotes a supplied snapshot. The checksum covers all preceding ASCII characters, including dots. Date precision is one second in UTC. Null totals omit the mark.

Decode with `python3 skills/token-tally/scripts/token_tally.py decode MARK --tokens EXACT_VISIBLE_TOTAL`. The decoder reports the count, abbreviated display total, timestamp, declared source, checksum status, and optional exact-total comparison. It requires no renderer or network.

This detects a visible-number edit when the original mark remains intact, and checksum failures detect mark corruption. It is deliberately unsigned: someone who edits both can forge a consistent card. It authenticates neither the account nor the source. Trusted verification would require an independently trusted issuer/signing service; embedding a private signing key in a distributed plugin would not solve that problem.

Check dependencies without account access: `python3 skills/token-tally/scripts/token_tally.py doctor --tsrct /absolute/path/to/tsrct`. Pass `--font-set bundled` to test the portable font fallback.

The listing screenshot uses synthetic sample statistics, not an actual user account.

Successful card requests end with the inline PNG and its download link. Editable exports remain available on request. Routine setup does not add a conversational confirmation; host permission prompts still apply.
