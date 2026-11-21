# cubrik's rule format — the traps

`run_backtest` validates every field, and its JSON Schema describes each operand (periods, lines,
what each one measures). What the schema cannot tell you is when valid rules mean something other
than what the user said. These are those cases.

## Shape

```
name:      "EMA 20/50 cross"          short, shown nowhere but the result
summary:   "Long when the 20 EMA crosses above the 50 on 4h; 2% stop, 6% target."
symbols:   ["BTC/USDT:USDT"]          up to 8; one backtest job per symbol
timeframe: "1m" | "5m" | "15m" | "1h" | "4h" | "1D"
style:     "scalping" | "day_trading" | "swing" | "investing"
rules: {
  side:       "long" | "short" | "both"
  entry:      [condition, …]          all must hold (≤ 6)
  entryShort: [condition, …]          only when side is "both"
  exit: {
    stopLossPct:    number | null     % from entry; null = no stop
    takeProfitPct:  number | null     % from entry; null = no fixed target
    maxBarsInTrade: number | null
    signal:         [condition, …]    any one closes early (≤ 4)
    signalShort:    [condition, …]    for the short side of "both"
  }
  risk: { perTradePct?, leverage, marginMode? }
  accumulate?: { amount, every? }     a regular buy
}
management: { unit: "margin_roi" | "price", tiers: [{ at, action }] } | null
months: 1–60 (default 12)
```

A condition is `{ op, left, right, within? }` with operands such as `price`, `const`, `sma`, `ema`,
`rsi`, `atr`, `macd`, `bollinger`, `keltner`, `stochastic`, `adx`, `cci`, `mfi`, `roc`, `vwap`,
`ichimoku`, `psar`, `supertrend`, `highest`, `lowest`, `volume`, `volumeAvg`, `obv`, and the price
structure ones `swingHigh`, `swingLow`, `orderBlock`, `fvg`, `structure`.

## Traps

**Sequences.** All entry conditions are checked on the same bar unless one carries `within`. "RSI
under 30, then the close crosses above the 20 EMA" without a `within` on the RSI leg is two things
that almost never happen on one bar: the backtest returns zero trades and looks like a strategy
that never triggered.

**Scales.** The two sides of a condition must be in the same unit: an oscillator (RSI, stochastic,
CCI, MFI, ADX) against a `const` or another oscillator; a price-level operand (EMA, Bollinger band,
VWAP, SAR, swing levels) against `price` or another level. OBV is only ever compared with itself
(raw against its average).

**Lines.** Operands that draw several lines carry `line`. "MACD crosses above its signal" is two
`macd` operands — `line: "macd"` and `line: "signal"` — with `crossesAbove`.

**ADX has no direction.** Use it as a filter beside an entry (trend above 25), direction from
`plusDi` against `minusDi`.

**No target.** `takeProfitPct: null` lets the trade run until the stop, a management tier or a
signal exit. Never write `takeProfitPct: 200` to mean "no target".

**Both directions.** One strategy, `side: "both"`: long conditions in `entry`, short ones in
`entryShort`, early exits in `exit.signal` / `exit.signalShort`. One position at a time.

**Regular buys (DCA).** `accumulate: { amount }` with `side: "long"`, leverage 1, no `perTradePct`,
`management: null`, on the spot pair. `amount` is in the quote currency (USDT on BTC/USDT) — say so
when the user said euros. `every: 7` on a 1D chart is weekly. `entry` may be empty (buy every bar).
Report it from `metrics.accumulation`: invested, end value, return on what was put in, average
cost, the deepest the holdings fell below the money put in. If `cashOutAt` is set, the cash ran out
that day and later buys were not made.

**Management tiers.** `unit` is what the percentages are of: `margin_roi` (a 10× position up 5% in
price is +50%) or `price`. Ask which the user means — it changes the result. A `lock` must keep less
than the gain that triggers it; tiers go in ascending `at`.

**Margin mode.** `risk.marginMode` is the user's choice. Leave it null when they did not name one.

**History.** One-minute plans are measured over the last 90 days at most. Forex, metals and indices
start at one hour.
