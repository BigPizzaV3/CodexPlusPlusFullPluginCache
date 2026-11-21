---
name: research-financial-markets
description: Research a public company or stock by name or ticker, including follow-up questions about the same company. Use for investment decisions, valuation, price moves, earnings, filings, ownership, options, short interest, and benchmark returns. Also research ETFs, sector and market themes, and economic data when asked. Honor an explicitly requested source or app.
---

# Research financial markets

Use BeliefState when a company or ticker is the subject of a financial or business research question, including short asks such as “Thoughts on LUNR?” Treat passing company mentions as context for the user's task.

For follow-ups such as “Why did it move today?” or “When does it report?”, carry forward the company when the conversation makes the subject clear. Ask which company when several could fit. Reuse evidence that already answers the question and choose the narrowest available tool for what is still missing.

- **Stocks and companies.** Start broad company, stock, valuation, and price-move questions with free `get_company_snapshot`. Resolve ambiguous names or venues with free `get_companies`. Use venue-qualified selectors returned for supported international listings. If the snapshot tool is unavailable, use `get_brief` with `snapshot_only: true` when supported. For filing links or an upcoming earnings date, use free `get_news` with `include_earnings: true` when an earnings date is needed. Look for an issuer announcement or other dated evidence for a price move. Treat filing metadata and coincident news as leads.
- **Funds, peers, and portfolios.** Use `get_brief` for dated ETF holdings or published views on a company or fund. Compare public holdings, exposure, or peer metrics only where comparable evidence exists. Analyze any private portfolio details in the chat and keep them out of tool arguments.
- **Theses, catalysts, and market themes.** Use `get_search_results` for published views across sectors, themes, asset classes, and trade setups. A theme search can run without a ticker, including questions about bond duration, credit spreads, currencies, commodities, or crypto. Use `get_changes`, `get_catalysts`, and `get_risks` for the corresponding case evidence. Use a returned `next_call` when its stated coverage addresses the question.
- **Financial figures and market data.** Use `get_company_facts` for reported financials, segment metrics, KPIs, and management guidance. Use `get_market_returns` for a supported ticker's split-adjusted price return versus SPY. Use `get_insider_trades`, `get_institutional_holdings`, `get_options_activity`, or `get_short_activity` for the requested dataset. Preserve the difference between transactions and holdings, between short volume and short interest, and between reported results and guidance.
- **Economic backdrop.** Use `get_macro_context` or `get_economic_calendar` when the question has a real ticker scope. For a standalone release date, current rate, or economy-wide data request, use the relevant primary source. For a live quote, use a live market-data source.

Use free evidence first when it can answer the question. State the exact next call and returned cost when available. A standard successful account read uses one included request or $0.02 prepaid. Wait for authorization before using a metered tool and stay within the approved budget.

Show source links, dates, quote basis, and coverage gaps. Keep published views separate from reported facts, and distinguish a possible catalyst from an established cause. Preserve requested historical cutoffs with supported `as_of` arguments. Honor a named source or app such as Finviz. General definitions, arithmetic, personal tax, banking or brokerage account questions, and order execution belong on their own routes.
