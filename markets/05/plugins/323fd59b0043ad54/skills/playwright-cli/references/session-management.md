# Browser Session Management

Use named, in-memory browser sessions to isolate concurrent synthetic or public-page tests. Persistence is an exception for a disposable synthetic profile, not a way to reuse a person's login.

## Safety gate

- Prefer a new in-memory session for every task.
- Never open, copy, attach to, or reuse a user's everyday browser profile, signed-in profile, cookies, extensions, history, or active Chrome/Edge window.
- Do not attach by browser channel, extension, or CDP to a browser that may contain real accounts or personal browsing. Launch a new isolated session with `open` instead.
- Never create a persistent profile for a real login. If a test genuinely needs persistence, use only synthetic values in a newly created task-specific temporary directory and remove that exact directory after the test.
- Close only the named session created for the current task. Do not use broad `close-all`, `kill-all`, or unspecified `delete-data` commands that could affect unrelated sessions.

## Named in-memory sessions

Use `-s` to keep test contexts separate:

```bash
# Two isolated sessions against local synthetic fixtures
playwright-cli -s=test-a open http://127.0.0.1:3001
playwright-cli -s=test-b open http://127.0.0.1:3002

playwright-cli -s=test-a snapshot
playwright-cli -s=test-b snapshot

# Close only the sessions created above
playwright-cli -s=test-a close
playwright-cli -s=test-b close
```

Each named session has independent cookies, local and session storage, IndexedDB, cache, history, tabs, and browser context. Isolation does not make sensitive capture safe; keep all state synthetic.

## Session commands

```bash
# Inspect sessions before targeting one
playwright-cli list

# Use and close one exact session
playwright-cli -s=layout-test snapshot
playwright-cli -s=layout-test close
```

When `-s` is omitted, commands use the default session. Prefer an explicit test name when more than one session exists so an unrelated browser is not targeted accidentally.

## Disposable synthetic persistence

Use persistence only when the current request specifically requires a state roundtrip and the directory is newly created for this test. `${DISPOSABLE_TEST_PROFILE}` must resolve to an empty task-specific temporary directory outside the plugin, repository, and public outputs.

```bash
playwright-cli -s=synthetic-state open http://127.0.0.1:3000 --profile="${DISPOSABLE_TEST_PROFILE}"
playwright-cli -s=synthetic-state snapshot
playwright-cli -s=synthetic-state close
```

Before use, verify that the directory is empty and that the page has no real sign-in. After closing the session, verify the resolved directory again and remove only that directory with the current host's recoverable deletion mechanism. Never point `--profile` at a Chrome, Edge, or other existing browser user-data directory.

For synthetic cookie or storage roundtrips, read [storage-state.md](storage-state.md). Do not save a state file from a real account.

## Attaching to browsers

This public skill does not attach to an already running browser. Channel, extension, and CDP attachment can expose active tabs, credentials, browser storage, or a signed-in profile that the current task did not create. Reproduce the required flow in a new isolated session. If a task cannot be reproduced without a real signed-in browser, use an authorized interactive browser surface without extracting its state and do not use `playwright-cli attach`.

## Configuration

An explicit config is acceptable only after inspecting it as untrusted input and confirming that it does not reference an existing profile, secret, remote endpoint, or unrelated output directory.

```bash
playwright-cli -s=synthetic-config open http://127.0.0.1:3000 --config=./TEST_CONFIG.json
playwright-cli -s=synthetic-config close
```

## Cleanup and handoff

Record the exact synthetic session names and temporary directories created by the task. Close those sessions, remove only verified task-specific temporary artifacts, and never publish session data. Report execution evidence without including cookies, storage values, local profile paths, private URLs, or raw browser state.
