# Orbit privacy policy

Effective November 4, 2026. Publisher: Kyle is Based. This policy covers the Orbit local desktop plugin. It does not cover separate hosted dashboards, OpenAI services or GitHub.

## Data and purpose

Orbit reads the signed-in Codex CLI account identity and subscription rate limits to calculate pacing and keep account histories separate. It hashes the account identifier or email locally and stores a pseudonymous account key, allowance labels, percentages, window durations, reset times and observation timestamps. A hash is not a guarantee of anonymity. Raw account emails, passwords and sign-in tokens are not saved by Orbit.

Orbit does not read Codex credential files, conversation contents or prompts. It does not run prompts or consume reset credits. Codex CLI manages its own sign-in and contacts OpenAI to retrieve usage.

## Storage and recipients

Usage records stay on your computer. Orbit does not send them to the publisher, operate a cloud storage service, or include advertising or analytics. Its dashboard listens only on the computer's loopback address. Other software running under your operating-system user may be able to read local files or access the local server.

Default data directories:

- Windows: `%LOCALAPPDATA%/PacePlugin`
- macOS: `~/Library/Application Support/PacePlugin`
- Linux: `$XDG_DATA_HOME/PacePlugin`, or `~/.local/share/PacePlugin`

The `PACE_DATA_DIR` setting can change this location. Browser preferences and cached readings are stored in local browser site data.

If you ask Codex about your pacing, usage values returned to that conversation are handled by the host under its own policies. If you voluntarily open a public GitHub support issue, its contents are visible to the publisher and the public and are handled by GitHub. Do not include private data in support issues.

## Retention and controls

Tracking starts when you request it, runs once per minute, and continues after closing the dashboard until stopped or the computer shuts down. Ask **Stop Orbit** to stop. Startup is off by default. If you explicitly enable Windows startup, Orbit saves a per-user Startup launcher and a stable copy of its runtime under the data directory. It then starts at Windows sign-in and recovers if the tracker stops. Disable Orbit startup removes that launcher. Stop Orbit pauses until you start it again or your next sign-in if startup remains enabled. Disable startup before uninstalling to prevent the retained runtime from starting. Missing observations are not reconstructed.

Local history remains until you delete it. To remove it, stop Orbit, remove its data directory, and clear browser site data for the dashboard's local origin. Back up history before deleting it if you want to keep a copy. Stopping or uninstalling the plugin does not itself delete history.

The publisher has no remote access to these local records and therefore cannot retrieve or delete them on your behalf. For questions about this policy, use the [support page](SUPPORT.md).
