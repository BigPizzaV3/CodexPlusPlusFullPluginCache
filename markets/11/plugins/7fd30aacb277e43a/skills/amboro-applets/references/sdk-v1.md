# SDK v1 reference

The host defines `window.fxr` before your first script runs. It is the applet's only way to learn anything about
Amboro: every read is a message to the host, so every read returns a promise. Nothing else exists on `fxr`.

```js
fxr.version;                        // '1'
fxr.ready();                        // Promise<context> — once, first
fxr.context.get();                  // Promise<context>, fresh from the host
fxr.context.onChange((ctx) => {});  // returns an unsubscribe function
fxr.account.get();                  // Promise<{ userId, displayName?, tier }>
```

## `fxr.ready()`

Resolves with the context once the frame is connected to the host and the host has answered its first context read.
Call it once, before anything else, and render from what it returns. It is idempotent: every call returns the same
promise, so a second call costs nothing and never asks again. If the host never connects it rejects with `TIMEOUT`
after 10 seconds.

```js
fxr.ready().then(render).catch(showError);
```

## `fxr.context`

`fxr.context.get()` asks the host for the current context every time; it is never answered from a cache.

`fxr.context.onChange(callback)` calls `callback` with the **whole** context after every change of symbol, timeframe,
session or theme, and returns a function that stops the calls. Re-render from the argument; do not call `get()`
again. An error thrown by one callback is logged to the console and does not stop the others.

```js
const stop = fxr.context.onChange((ctx) => render(ctx));
```

| Field | Type | Value | `null` when |
| --- | --- | --- | --- |
| `symbol` | `string \| null` | The chart's symbol as the chart spells it, like `'EURUSD'` | Outside a chart — always at the standalone URL |
| `timeframe` | `string \| null` | The chart's own resolution string, unchanged (below) | Outside a chart, or the chart cannot report it |
| `session` | `{ id, mode } \| null` | `mode` is `'backtest'`, `'replay'` or `'live'` | Not on a session's chart |
| `theme` | `'dark' \| 'light'` | The theme of the page around the applet | Never |

**`null` means "not available here"**, never "not loaded yet": render a sentence that says where the value appears
(*"Open this applet inside a chart to see the symbol"*), never a guess and never a blank.

**Timeframes** are passed through exactly as the chart writes them: minutes as a number (`'1'`, `'15'`, `'60'`,
`'240'`) and days, weeks or months with a letter (`'1D'`, `'1W'`, `'1M'`). Show a value you do not recognise as it is;
never convert it by guessing.

## `fxr.account.get()`

Who is signed in, answered from what Amboro already knows. No token, cookie or credential ever reaches the applet —
these fields are everything it can learn about the trader.

| Field | Type | Notes |
| --- | --- | --- |
| `userId` | `string` | Stable for the trader; do not show it |
| `displayName` | `string`, optional | Missing for accounts without a name — greet "trader" |
| `tier` | `string \| null` | The subscription tier; `null` when the host cannot tell |

Signed out (a session that expired under an open page) it rejects with `UNAUTHORIZED`: show *"Sign in to see your
account"* and keep the rest of the applet working. `ENTITLEMENT_DENIED` is reserved for features a plan does not
include; SDK v1 never answers it.

```js
fxr.account.get().then(
  (me) => greet(me.displayName ?? 'trader', me.tier),
  (error) => (error.code === 'UNAUTHORIZED' ? askToSignIn() : showError(error)),
);
```

## Errors

A failed call rejects with an `Error` whose `code` names the reason and whose `message` is the host's fixed sentence
below. Branch on `code`, never on `message`; show the trader the sentence in the last column.

| `code` | When | `message` | Show the trader |
| --- | --- | --- | --- |
| `UNAUTHORIZED` | Nobody is signed in (`account.get`) | Sign in to Amboro to use this feature. | *"Sign in to see your account"* |
| `TIMEOUT` | No answer within 10 seconds | Amboro did not answer in time. | *"Amboro is not responding — reload the applet"* |
| `RATE_LIMITED` | More than 20 calls in a second | Too many requests; wait a moment and try again. | Nothing — call less often (use `onChange`, never a polling loop) |
| `INVALID_PARAMS` | Arguments were passed; v1 methods take none | This method takes no parameters. | Nothing — fix the call |
| `METHOD_NOT_FOUND` | The host does not know the method | This method is not available in SDK v1. | *"This applet needs a newer version of Amboro"* |
| `INTERNAL` | The host failed to answer | The host could not answer. | *"Something went wrong — try again"* |
| `ENTITLEMENT_DENIED` | Reserved; v1 never answers it | Your plan does not include this feature. | *"Your plan does not include this"* |
| `SCOPE_NOT_GRANTED` | Reserved; v1 never answers it | This applet is not allowed to use that feature. | *"Something went wrong — try again"* |
| `NOT_FOUND` | Reserved; v1 never answers it | That item was not found. | *"Something went wrong — try again"* |

## Limits

- **10 seconds per call**, counted from the call — including while the frame is still connecting (calls made that
  early wait for the connection and are then sent in order).
- **20 calls per second** per applet; the calls beyond it reject with `RATE_LIMITED`.
- **The sandbox**: an opaque origin, so no storage and no cookies; no network (`fetch`, XHR, WebSockets and remote
  images are blocked by the frame's Content-Security-Policy); no nested frames, forms or navigation. The trader's
  Amboro page is not reachable from the applet — `fxr` is the only channel.

## Theme variables

Each time a context arrives (`ready`, `context.get`, every change) the SDK applies the host's palette for `theme`:
the `--fxr-*` variables, `color-scheme` and `<html data-theme>`. They and the classes built on them are in
[design.md](design.md); each has a default, so nothing is unset before `ready`.

## Versioning

`fxr.version` is `'1'`, and the file declares it with `<meta name="fxr-sdk" content="1">`. SDK 1 is frozen: its
methods, fields and codes never change meaning. A later SDK adds methods under a new version number; until the
reference for it exists, everything beyond this page is absent from `fxr`.
