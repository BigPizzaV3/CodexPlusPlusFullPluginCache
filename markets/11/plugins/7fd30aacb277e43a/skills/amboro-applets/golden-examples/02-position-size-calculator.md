# Golden example — position-size calculator

**Brief:** "Build a position-size calculator that greets me and shows my plan tier."

Points to notice:

- **The `account.get` error branch**: signed out, the call rejects with `code` `UNAUTHORIZED` and the header reads
  *"Sign in to see your account"*; `displayName` and `tier` each have a fallback.
- **Only what the SDK gives**: there is no balance in the SDK, so the trader types it; the symbol shows only when the
  chart provides one.
- **Inputs without a form**: each `<input>` recalculates on `input` — nothing to submit (law 6).
- **One layout, two widths**: `fxr-split` puts the four fields in two columns on the full page and one in the pane.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="fxr-sdk" content="1">
<title>Position size calculator</title>
</head>
<body class="fxr-app">
<header class="fxr-row fxr-row--between">
  <span id="greeting" class="fxr-heading">Hi, trader</span>
  <span id="tier" class="fxr-chip fxr-chip--accent" hidden></span>
</header>
<p id="symbol" class="fxr-caption">Waiting for the chart…</p>
<section class="fxr-card">
  <div class="fxr-split">
    <label class="fxr-field"><span class="fxr-field__label">Account balance</span>
      <input id="balance" class="fxr-input" type="number" min="0" step="any" placeholder="10000"></label>
    <label class="fxr-field"><span class="fxr-field__label">Risk per trade</span>
      <span class="fxr-input-group"><input id="risk" class="fxr-input" type="number" min="0" step="0.1" value="1"><span class="fxr-input-group__addon">%</span></span></label>
    <label class="fxr-field"><span class="fxr-field__label">Stop distance</span>
      <span class="fxr-input-group"><input id="stop" class="fxr-input" type="number" min="0" step="1" value="200"><span class="fxr-input-group__addon">points</span></span></label>
    <label class="fxr-field"><span class="fxr-field__label">Point value per lot</span>
      <input id="pointValue" class="fxr-input" type="number" min="0" step="any" value="1"></label>
  </div>
</section>
<section class="fxr-card fxr-card--raised fxr-stat">
  <span class="fxr-stat__label">Position size</span>
  <span id="lots" class="fxr-stat__value">—</span>
  <span id="detail" class="fxr-caption">Type your balance to size the trade.</span>
</section>
<script>
  const byId = (id) => document.getElementById(id);
  const fields = ['balance', 'risk', 'stop', 'pointValue'].map(byId);

  function positive(input) {
    const value = Number.parseFloat(input.value);
    return value > 0 ? value : null;
  }

  function recalculate() {
    const [balance, riskPct, stop, pointValue] = fields.map(positive);
    if ([balance, riskPct, stop, pointValue].includes(null)) {
      byId('lots').textContent = '—';
      byId('detail').textContent = 'Type your balance to size the trade.';
      return;
    }
    const atRisk = (balance * riskPct) / 100;
    const lots = Math.floor((atRisk / (stop * pointValue)) * 100) / 100;
    byId('lots').textContent = `${lots.toFixed(2)} lots`;
    byId('detail').textContent = `Risking ${atRisk.toFixed(2)} over ${stop} points.`;
  }

  function onContext(c) {
    byId('symbol').textContent = c.symbol
      ? `Sizing ${c.symbol}`
      : 'No chart here: the size works for any symbol.';
  }

  function onAccount(account) {
    byId('greeting').textContent = `Hi, ${account.displayName || 'trader'}`;
    byId('tier').textContent = account.tier ?? 'no plan';
    byId('tier').hidden = false;
  }

  function onAccountError(error) {
    byId('greeting').textContent = error?.code === 'UNAUTHORIZED'
      ? 'Sign in to see your account'
      : 'Your account is not available right now';
  }

  fields.forEach((input) => input.addEventListener('input', recalculate));

  fxr.ready().then((c) => {
    onContext(c);
    fxr.context.onChange(onContext);
    fxr.account.get().then(onAccount, onAccountError);
  });
</script>
</body>
</html>
```
