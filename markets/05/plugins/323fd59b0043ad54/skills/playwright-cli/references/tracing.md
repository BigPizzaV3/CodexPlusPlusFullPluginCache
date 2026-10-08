# Tracing

Capture detailed execution traces only in a disposable test profile on a public demo, local fixture, or synthetic page. A trace can contain DOM text, screenshots, typed values, URLs, console output, request and response data, headers, and cached resources. Treat the entire trace directory as sensitive even when the intended test input is harmless.

Never trace a real sign-in, payment, health, education, private-message, admin, or personal-account flow. Do not trace a user's everyday browser profile or reuse real authentication. If a failure exists only in a live signed-in flow, reproduce the smallest relevant state with synthetic data or debug without tracing.

Keep traces in a task-specific temporary directory outside the plugin, repository, and public outputs. Do not upload, attach, publish, or share a raw trace. Inspect only the minimum local fields needed, redact any unexpected identifier before quoting a finding, and remove the temporary trace after the test.

## Basic Usage

```bash
# Start trace recording
playwright-cli tracing-start

# Perform actions
playwright-cli open https://demo.playwright.dev/todomvc
playwright-cli fill "getByPlaceholder('What needs to be done?')" "TEST_ITEM"
playwright-cli press Enter

# Stop trace recording
playwright-cli tracing-stop
```

## Trace Output Files

When you start tracing, Playwright can create a `traces/` directory with several files. Exact contents vary by version; assume any of the following may contain sensitive page data.

### `trace-{timestamp}.trace`

**Action log** - The main trace file containing:
- Every action performed (clicks, fills, navigations)
- DOM snapshots before and after each action
- Screenshots at each step
- Timing information
- Console messages
- Source locations

### `trace-{timestamp}.network`

**Network log** - Recorded network activity may include:
- HTTP requests and responses
- Request headers and bodies, including authorization material if the test was unsafe
- Response headers and bodies
- Timing (DNS, connect, TLS, TTFB, download)
- Resource sizes
- Failed requests and errors

### `resources/`

**Resources directory** - Cached resources:
- Images, fonts, stylesheets, scripts
- Response bodies for replay
- Assets needed to reconstruct page state

## What Traces Capture

| Category | Details |
|----------|---------|
| **Actions** | Clicks, fills, hovers, keyboard input, navigations |
| **DOM** | Full DOM snapshot before/after each action |
| **Screenshots** | Visual state at each step |
| **Network** | All requests, responses, headers, bodies, timing |
| **Console** | All console.log, warn, error messages |
| **Timing** | Precise timing for each operation |

## Use Cases

### Debugging a Synthetic Failed Action

```bash
playwright-cli tracing-start
playwright-cli open https://demo.playwright.dev/todomvc

# This click fails - why?
playwright-cli click e5

playwright-cli tracing-stop
# Open trace to see DOM state when click was attempted
```

### Analyzing a Public Demo

```bash
playwright-cli tracing-start
playwright-cli open https://demo.playwright.dev/todomvc
playwright-cli tracing-stop

# View network waterfall to identify slow resources
```

### Capturing Local Test Evidence

```bash
# Record only a synthetic flow in a disposable profile
playwright-cli tracing-start

playwright-cli open https://demo.playwright.dev/todomvc
playwright-cli fill "getByPlaceholder('What needs to be done?')" "TEST_ITEM"
playwright-cli press Enter

playwright-cli tracing-stop
# Review locally; never attach or publish the raw trace
```

## Trace vs Video vs Screenshot

| Feature | Trace | Video | Screenshot |
|---------|-------|-------|------------|
| **Format** | .trace file | .webm video | .png/.jpeg image |
| **DOM inspection** | Yes | No | No |
| **Network details** | Yes | No | No |
| **Step-by-step replay** | Yes | Continuous | Single frame |
| **File size** | Medium | Large | Small |
| **Best for** | Debugging | Demos | Quick capture |

## Best Practices

### 1. Minimize the Trace Window

```bash
# Trace the smallest synthetic sequence that reproduces the issue
playwright-cli tracing-start
playwright-cli open https://demo.playwright.dev/todomvc
# ... only the necessary synthetic steps ...
playwright-cli tracing-stop
```

### 2. Clean Up the Exact Temporary Trace

Traces can consume significant disk space and may retain page data. Verify the resolved path is the task-specific temporary trace directory, close the trace viewer, and remove only that directory with the current host's recoverable deletion mechanism. Never use a broad glob, repository root, home directory, or shared Playwright data directory as the deletion target.

## Limitations

- Traces add overhead to automation
- Large traces can consume significant disk space
- Some dynamic content may not replay perfectly
- Redaction after capture cannot guarantee that all copies of a secret were removed; prevent sensitive capture in the first place
