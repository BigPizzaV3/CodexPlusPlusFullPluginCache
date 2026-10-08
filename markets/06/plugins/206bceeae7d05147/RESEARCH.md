# Research basis

Research checked September 15, 2026; implementation resumed September 16 and finalized September 17, 2026. These sources inform the workflow; they do not establish that this plugin beats a market benchmark.

- [Agent design evidence and prompt techniques](references/research-agent-design.md): eight primary sources, concrete supported practices, reusable specialist/verification/reconciliation prompts and limits.
- [Investment methods and evidence controls](references/research-investment-methods.md): twelve primary sources on data, valuation, probabilities, sector methods and forecast accountability.

## Practices incorporated

| Practice | Reason and primary basis | Limit |
|---|---|---|
| Explicit objective, plan and output contracts | [OpenAI reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | No magic phrase guarantees deeper or correct analysis |
| Bounded specialists and central verification | [Agent-scaling research](https://arxiv.org/abs/2512.08296v3) | Gains depend on task; more agents can also propagate errors |
| Independent reconstruction before comparison | [Chain-of-Verification](https://aclanthology.org/2024.findings-acl.212/) | Factual benchmark evidence, not investment-performance evidence |
| Preserve dissent; reconcile by evidence | [Debate or Vote](https://arxiv.org/abs/2508.17536v2) | Consensus is not independent corroboration |
| Indexed evidence and narrow source packets | [Lost in the Middle](https://arxiv.org/abs/2307.03172v3) | Older-model study; applicability should be evaluated on the host |
| Original filings and non-GAAP bridges | [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [SEC non-GAAP guidance](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures) | Databases can omit custom facts and obscure periods |
| Reverse valuation and sector-appropriate methods | [Damodaran valuation examples](https://pages.stern.nyu.edu/~adamodar/pdfiles/dcfveg.pdf), [financial firms](https://pages.stern.nyu.edu/~adamodar/pdfiles/country/finsvce.pdf) | Teaching methods, not current assumptions or targets |
| Tail-aware scenarios and benchmark comparison | [Bessembinder stock-return research](https://www.sciencedirect.com/science/article/pii/S0304405X18301521) | Historical population results do not give a stock's forward odds |
| Immutable forecasts and proper scoring | [Gneiting and Raftery](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf) | Calibration needs enough resolved, appropriately evaluated observations |
| Separate testing from investment claims | [OpenAI evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices), [backtest overfitting research](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) | Structural correctness and synthetic tests do not demonstrate alpha |

The default thresholds, Pareto ordering, research artifacts and specialist division are design choices informed by these materials. They are not purportedly validated investment rules. Research memos summarize sources rather than reproducing their full text; each source's support and limits are identified there.
