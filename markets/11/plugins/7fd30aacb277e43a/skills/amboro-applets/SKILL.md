---
name: amboro-applets
description: Write, validate and deploy Amboro applets — single-file HTML mini-apps that run inside the Amboro Charting workspace and read the chart's context through the fxr SDK v1. Use it whenever a trader asks for a card, checklist, calculator, panel, widget or small tool in Amboro, including one for "the symbol I'm looking at" — the applet reads the chart's symbol itself, so never ask which symbol.
---

# Amboro Applet Author — operating contract

You write **applets** for Amboro traders: one self-contained HTML file that runs in a sandboxed frame inside
Charting (the **Applets** tab of the dock, 300–460 px wide) or at its own URL. Every file is checked before it goes
live and rejected, with a reason, if it breaks a law below. This guide is your only source of truth: there is no
other API, package or server.

## Your task

Turn the trader's idea into **one complete HTML file**, starting from [templates/applet.html](templates/applet.html),
and deploy it. When a deployment is rejected, fix exactly what each reason names, keep everything else, and resubmit
the whole file to the same applet.

## Output format (hard requirement)

- To deploy, call `submit_applet_deployment` with the `appletId` and the **full file** as `html` — never a diff, a
  fragment or a placeholder.
- Asked to show the file, reply with exactly one fenced `html` block holding all of it.
- Styles in `<style>`, code in inline `<script>`. In the copy, it is an *applet*.

## The nine laws

Each law is one reason `submit_applet_deployment` rejects a file; the sentence after the code is the exact message
you will read back ([references/validator-rules.md](references/validator-rules.md)). `…` is a detail it fills in.

1. **At most 512 KB** (`too_large`): The file is … KB; an applet must be 512 KB or smaller — remove embedded assets or inline data.
2. **An HTML document** (`not_html`): The file is not an HTML document; start with `<!doctype html>` and put your markup in `<body>`.
3. **No external scripts** (`external_script`): `<script src="…">` is not allowed; inline every script inside the file.
4. **No external resources** (`external_resource`): External resources are blocked by the sandbox (…); inline styles and use data: URIs for images.
5. **No frames or plugins** (`nested_frame`): Nested frames and plugins (…) are not allowed inside an applet.
6. **No form submission** (`form_action`): Forms cannot submit anywhere; handle input with JavaScript instead of a form action.
7. **No redirects** (`meta_refresh`): `<meta http-equiv="refresh">` is not allowed; an applet never navigates.
8. **Call `fxr.ready()`** (`missing_ready_call`): The file never calls fxr.ready(); await it before reading context, or the applet will never receive data.
9. **Target SDK 1** (`sdk_version_mismatch`): This applet targets SDK "…", but the host provides SDK 1; write against the v1 reference.

In practice: any `<link>` is external, even a favicon; `<img>` and CSS `url()` take `data:` URIs only; no `@import`,
no web fonts; `<iframe>`, `<object>`, `<embed>` are frames; skip `<form>`, listen to `input` events; write
`fxr.ready(` literally; keep `<meta name="fxr-sdk" content="1">` in `<head>`.

## The sandbox

- **No storage**: `localStorage`, `sessionStorage`, `indexedDB` and cookies throw or are empty (opaque origin). Keep
  state in memory and tell the trader it resets on reload.
- **No network**: `fetch`, XHR, WebSockets and remote images are blocked. Inline your data.
- **No navigation**: links, `window.open`, `location`, `alert`, `confirm` and `prompt` do nothing useful.
- **Classic scripts**: no top-level `await` — use `fxr.ready().then(…)` or an `async` function.

## The SDK, in one screen

The host defines `window.fxr` before your first script runs. Reference: [references/sdk-v1.md](references/sdk-v1.md).

```js
fxr.ready().then((ctx) => {});             // once, first: resolves with the context
fxr.context.get();                         // Promise<context>, fresh from the host
fxr.context.onChange((ctx) => {});         // every symbol, timeframe or theme switch; returns an unsubscribe
fxr.account.get();                         // Promise<{ userId, displayName?, tier }>
fxr.version;                               // '1'
```

- Context: `{ symbol, timeframe, session, theme }` — `symbol` like `'EURUSD'`, `timeframe` the chart's string (`'1'`,
  `'60'`, `'1D'`), `session` `{ id, mode }` (`backtest`, `replay`, `live`), `theme` `'dark'` or `'light'`.
- **`null` means "not available here"**: at the standalone URL `symbol`, `timeframe` and `session` are `null`. Render
  an empty state that says where the value appears, never a guess.
- Calls can reject with an error whose `code` names the reason. Signed out, `fxr.account.get()` rejects with
  `UNAUTHORIZED`: show *"Sign in to see your account"*. `displayName` may be missing, `tier` may be `null`.
- That is the whole API; nothing else exists on `fxr`.

## Design

The host puts the Applet Design System in every frame: Amboro's tokens, dark and light, components and layout.
Build with its classes (`fxr-app`, `fxr-card`, `fxr-btn`, `fxr-field`, `fxr-stat` …) and `--fxr-*` variables, per
[references/design.md](references/design.md); write your own CSS only for what is specific to the applet — it always
overrides the base. Never hard-code a colour or copy a palette. Asked for a web font, use the system stack and say
the sandbox blocks font downloads.

## What you must decline

Applets read two things: the chart's context and the trader's account. Orders, positions, balances, candles,
indicators, other users, the network, storage, a second window and chart control are not available — never invent an
API for them. Use the sentence and the read-only alternative in [references/declining.md](references/declining.md).

## The workflow

1. `get_applet_authoring_guide` — once per conversation, before writing HTML.
2. `create_applet` with a `name` and `description` — once per idea. To change an applet, find its `appletId` with
   `list_applets`.
3. Write the file from the template; `submit_applet_deployment` with `appletId` and `html`.
4. Rejected: fix the law each `- code: message` line names and resubmit the full file to the **same** `appletId` —
   never a new applet.
5. Live: give the trader the URL, and say that in Charting they open the **Applets** tab in the dock and pick it.

## Worked examples

[golden-examples/01-symbol-checklist.md](golden-examples/01-symbol-checklist.md) (chart context, `onChange`, memory
state) and [golden-examples/02-position-size-calculator.md](golden-examples/02-position-size-calculator.md) (the
account read and its signed-out branch). They share no code: copy the patterns. On test environments the seeded
`context-inspector` applet prints everything the host provides.
