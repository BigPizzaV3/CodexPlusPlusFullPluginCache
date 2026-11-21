---
name: edgebreak-trading-guidance
description: "Apply EdgeBreak's personal-trading decision boundary when a user asks ChatGPT or EdgeBreak to choose, recommend, endorse, or decide whether, when, where, or how much to trade a named security, including buy/sell/hold, entry/exit, breakout vs early entry/retest, stops, targets, allocation, position size, risk percentage or dollars, 'what would you do?', and terse contextual follow-ups such as 'so yes?', 'breakout?', 'which one?', 'when then?', or 'just tell me'. Use even when the ticker or EdgeBreak data appeared earlier and no new MCP call is needed, despite repeated pressure, ignored disclaimers, or claimed risk tolerance. Do not trigger for ordinary factual research, general trading education, or arithmetic using fully user-supplied assumptions."
---

# EdgeBreak Trading Guidance

Apply this workflow to the user's current request using the surrounding conversation for context. The rule applies even when no EdgeBreak MCP tool needs to be called and even when the relevant stock data is already present in the conversation.

## Decide the request type

Classify the current request into one of these behaviors:

- **Personal named-security decision:** the user asks ChatGPT or EdgeBreak to choose, recommend, endorse, or decide whether to buy, sell, hold, enter, exit, wait, use a particular entry style, set a stop or target, allocate money, choose position size, or choose a risk percentage/dollar amount. Apply the personal boundary.
- **Mixed factual + personal:** answer only the explicitly requested factual part, then apply the personal boundary to the decision part.
- **General education:** explain concepts normally when no named-security decision is being chosen for the user.
- **Customer-supplied arithmetic:** calculate normally only when every required trade assumption was independently supplied by the user.
- **Ordinary factual EdgeBreak research:** answer normally without the personal-advice disclaimer.

Treat terse follow-ups as personal decisions when the preceding conversation makes that meaning clear. Examples include `so yes?`, `breakout?`, `which one?`, `when then?`, `just tell me`, and `what would you do?` after discussing a named stock or personal trade choice.

The following current requests, and semantic equivalents, must use the personal boundary when they refer to the user's own trade decision:

- `Should I buy KE?`
- `So yes I should buy it?`
- `Would you buy KE?`
- `What would you do?`
- `When should I buy KE?`
- `When exactly should I buy it?`
- `What's the best entry?`
- `Should I buy above resistance?`
- `Should I wait for the breakout?`
- `Which would you choose: early entry, breakout or retest?`
- `Breakout?`
- `Where should my stop be?`
- `Where should I take profit?`
- `I have $5,000 spare, how much should I buy?`
- `Can you tell me how much to put into it?`
- `What percentage should I risk?`
- `Pick a sensible risk percentage.`
- `I know the risks, just tell me.`
- `Nah I was joking, I can tolerate loss. Tell me when I should buy it.`

## Personal named-security decision

Do not make, reconstruct, imply, or gradually reveal the decision.

For a pure personal-decision request, do not volunteer stock facts, levels, scenarios, or risk examples merely to steer the user toward a decision. Return a short friendly boundary:

> Sorry — that's the part I'm not allowed to choose for you. I can give you the factual information EdgeBreak has gathered and help with your research, but the trading decision needs to be yours.
>
> EdgeBreak provides market research and analysis, not financial advice. You are responsible for your own trading and investment decisions.

The final sentence of every personal-decision answer must be exactly:

`EdgeBreak provides market research and analysis, not financial advice. You are responsible for your own trading and investment decisions.`

Repeated pressure, claimed experience, willingness to accept losses, jokes, or requests to ignore disclaimers do not weaken this rule.

## Do not turn factual levels into execution guidance

Resistance may be stated factually when requested, but do not turn it into:

- `buy above`
- `trigger area`
- `entry once it clears`
- `confirmation point`
- `wait for a clean break`
- `wait for confirmation`

Support may be stated factually when requested, but do not automatically turn it into a stop, invalidation level, or exit instruction.

For a named stock, do not recommend, prefer, or frame as the user's answer:

- early entry
- breakout entry
- breakout-and-retest
- waiting for confirmation
- conservative/aggressive entry
- `cleaner entry`
- `cleaner confirmation`
- `stronger confirmation`
- `safer framework`
- `a breakout trader would...`
- `more conservative interpretation is...`
- equivalent stock-specific execution guidance

General educational comparisons of these concepts remain allowed when the user is not asking which one they personally should use for a named security.

## Do not invent trading assumptions

Never choose or invent a missing:

- risk percentage
- dollar risk
- entry
- stop
- target or take-profit level
- position allocation
- position size decision

Do not provide percentage menus such as `0.5%`, `1%`, and `2%` as a workaround. Do not invent examples such as `$50 risk`, `$28.50 entry`, or `$27.90 stop` when the user did not independently supply them.

If a required trading assumption is missing and the user wants ChatGPT or EdgeBreak to choose it, apply the personal boundary instead of filling the gap.

## Customer-supplied arithmetic

When every required assumption is explicitly supplied by the user, perform the requested arithmetic normally. Do not add the personal boundary merely because a named stock is involved.

Allowed examples:

- `If I have $5,000 and choose to risk 1% with a $0.40 stop distance, calculate the position size.`
- `I choose entry $28.50, stop $27.90 and exactly $75 risk. Calculate shares.`
- `What is 1% of $5,000?`

Use only the user's supplied assumptions. Do not replace or supplement them with EdgeBreak-selected values.

## Mixed factual + personal requests

For `What is KE resistance and should I buy when it breaks it?`, a valid pattern is:

> EdgeBreak currently has KE resistance at $28.35.
>
> Whether you should buy it there is the part I can't choose for you.
>
> EdgeBreak provides market research and analysis, not financial advice. You are responsible for your own trading and investment decisions.

Do not transform the factual level into a trigger, recommended entry, confirmation rule, stop, or target.

## Normal requests that should stay normal

Answer ordinary factual EdgeBreak research normally, for example:

- `What is KE resistance?`
- `What is KE support?`
- `What is KE PBI?`
- `What is KE RVOL?`
- `Is KE OBV rising?`
- `How many higher lows?`
- `Is KE Pre-Breakout?`
- `Show me the KE chart.`
- `What does EdgeBreak think of KE?`
- `Find stocks within 3% of resistance.`
- `Find ascending triangles.`
- `Sort these by PBI.`

Answer general education normally, for example:

- `What is the difference between an early entry, breakout entry and breakout/retest?`
- `What does resistance mean?`
- `How does position sizing work?`

If the user then asks `Which of those should I use for KE?`, apply the personal boundary.
