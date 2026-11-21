# Golden example — symbol checklist

**Brief:** "Make me a pre-trade checklist card for the symbol I'm looking at."

Points to notice:

- **The `null` state**: outside a chart the header says *No chart*, a hint says where the symbol appears, and the
  checklist still works.
- **The `onChange` re-render**: `fxr.ready()` once, then `fxr.context.onChange(showSymbol)` re-runs the same render
  on every switch; each symbol keeps its own ticks in a `Map` — memory only, and the copy says so.
- **No CSS of its own**: the card, list, checkboxes, progress and chip are the design system's classes, so the
  applet follows dark and light with no colour in the file.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="fxr-sdk" content="1">
<title>Symbol checklist</title>
</head>
<body class="fxr-app">
<section class="fxr-card">
  <div class="fxr-card__header">
    <div class="fxr-row fxr-gap-4">
      <span id="symbol" class="fxr-title">Loading…</span>
      <span id="timeframe" class="fxr-chip" hidden></span>
    </div>
    <span id="count" class="fxr-caption fxr-num">0 of 5 ready</span>
  </div>
  <p id="hint" class="fxr-caption" hidden>Open this applet inside a chart to see the symbol.</p>
  <progress id="fill" class="fxr-progress" max="5" value="0"></progress>
  <ul id="list" class="fxr-list">
    <li><label class="fxr-check"><input class="fxr-checkbox" type="checkbox"> Higher-timeframe trend agrees with the trade</label></li>
    <li><label class="fxr-check"><input class="fxr-checkbox" type="checkbox"> Entry is at a planned level, not a chase</label></li>
    <li><label class="fxr-check"><input class="fxr-checkbox" type="checkbox"> Stop sits where the idea is proven wrong</label></li>
    <li><label class="fxr-check"><input class="fxr-checkbox" type="checkbox"> Risk is 1% of the account or less</label></li>
    <li><label class="fxr-check"><input class="fxr-checkbox" type="checkbox"> No high-impact news in the next hour</label></li>
  </ul>
  <div class="fxr-row fxr-row--between">
    <span class="fxr-caption">Ticks last until the applet reloads.</span>
    <button id="reset" class="fxr-btn fxr-btn--ghost fxr-btn--sm" type="button">Reset</button>
  </div>
</section>
<script>
  const boxes = [...document.querySelectorAll('#list input')];
  const ticked = new Map(); // symbol → ticked rows, in memory: the sandbox has no storage
  let symbol = null;

  function rowsOf(key) {
    if (!ticked.has(key)) ticked.set(key, new Set());
    return ticked.get(key);
  }

  function showProgress() {
    const done = rowsOf(symbol).size;
    document.getElementById('count').textContent = `${done} of ${boxes.length} ready`;
    document.getElementById('fill').value = done;
  }

  function showSymbol(ctx) {
    symbol = ctx.symbol;
    document.getElementById('symbol').textContent = symbol ?? 'No chart';
    document.getElementById('hint').hidden = symbol !== null;
    const timeframe = document.getElementById('timeframe');
    timeframe.textContent = ctx.timeframe ?? '';
    timeframe.hidden = !ctx.timeframe;
    const rows = rowsOf(symbol);
    boxes.forEach((box, i) => { box.checked = rows.has(i); });
    showProgress();
  }

  document.getElementById('list').addEventListener('change', (event) => {
    const row = boxes.indexOf(event.target);
    if (event.target.checked) rowsOf(symbol).add(row);
    else rowsOf(symbol).delete(row);
    showProgress();
  });

  document.getElementById('reset').addEventListener('click', () => {
    rowsOf(symbol).clear();
    boxes.forEach((box) => { box.checked = false; });
    showProgress();
  });

  fxr.ready().then((ctx) => {
    showSymbol(ctx);
    fxr.context.onChange(showSymbol);
  });
</script>
</body>
</html>
```
