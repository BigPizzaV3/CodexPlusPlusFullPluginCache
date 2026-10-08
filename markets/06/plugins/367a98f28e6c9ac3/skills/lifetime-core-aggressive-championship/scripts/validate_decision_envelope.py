#!/usr/bin/env python3
"""Validate the public, non-personalized Lifetime Core Championship Research Envelope v1.0.3."""
from __future__ import annotations
import json, sys
from pathlib import Path

DECISION_CLASSES={"TICKER_SPOTLIGHT","WATCHLIST","WAIT","RISK_ELEVATED","NO_SPOTLIGHT"}
CHAMPIONSHIP_RESULTS={"TICKER_SPOTLIGHT","CASH_WAIT"}
MARKET_PERMISSION={"GREEN","SELECTIVE GREEN","YELLOW","RED","BLACKOUT","UNKNOWN"}
TECHNICAL_STATES={"UNCONFIRMED","DEVELOPING","CONFIRMED","EXTENDED","DAMAGED","UNKNOWN"}
DATA_FRESHNESS={"FRESH","DEGRADED","STALE","UNKNOWN"}
COMPETITION={"SPOTLIGHT_1","WATCHLIST_2","WATCHLIST_3","WATCHLIST_OTHER","NOT_RANKED"}
PROHIBITED_KEYS={
    "account_equity","account_balance","portfolio_value","settled_cash","buying_power","holdings",
    "average_cost","open_orders","realized_pnl","unrealized_pnl","margin_status",
    "planned_dollar_risk","position_size","share_count","contract_count","allocation_percent",
    "max_affordable_shares","max_affordable_contracts","purchasing_capacity","order_intent","authorization",
    "entry_zone","stop","stop_loss","profit_target","order_type","order_price","order_timing","execution_readiness"
}
PROHIBITED_DIRECTIVES={"BUY","ADD","HOLD","TRIM","EXIT","SELL"}
FORBIDDEN_ARTIFACTS={"SVGCALLED","TOOLSVG"}

def fail(msg): raise ValueError(msg)

def validate(d):
    if not isinstance(d,dict): fail('Research Envelope must be a JSON object')
    required={"decision_class","championship_result","ticker","market_permission","watchlist_competition","technical_state","data_freshness","evidence_confidence","demotion_conditions","research_note"}
    missing=sorted(required-d.keys())
    if missing: fail('Missing required fields: '+', '.join(missing))
    if d['decision_class'] not in DECISION_CLASSES: fail('Invalid decision_class')
    if d['championship_result'] not in CHAMPIONSHIP_RESULTS: fail('Invalid championship_result')
    if d['market_permission'] not in MARKET_PERMISSION: fail('Invalid market_permission')
    if d['technical_state'] not in TECHNICAL_STATES: fail('Invalid technical_state')
    if d['data_freshness'] not in DATA_FRESHNESS: fail('Invalid data_freshness')
    if d['watchlist_competition'] not in COMPETITION: fail('Invalid watchlist_competition')
    if d['evidence_confidence'] not in {"HIGH","MEDIUM","LOW"}: fail('Invalid evidence_confidence')
    bad=sorted(PROHIBITED_KEYS & d.keys())
    if bad: fail('Public envelope contains prohibited personal/execution fields: '+', '.join(bad))
    text=json.dumps(d).upper()
    for term in PROHIBITED_DIRECTIVES:
        if f'"{term}"' in text: fail(f'Public envelope must not emit transaction directive {term}')
    for token in FORBIDDEN_ARTIFACTS:
        if token in text: fail(f'Public envelope contains raw tool artifact {token}')
    if d['decision_class']=='TICKER_SPOTLIGHT':
        if d.get('spotlight_rank') != 1: fail('TICKER_SPOTLIGHT requires spotlight_rank=1')
        if d['ticker'] in {'NONE','CASH / WAIT'}: fail('TICKER_SPOTLIGHT requires a security ticker')
        if d['watchlist_competition']!='SPOTLIGHT_1': fail('TICKER_SPOTLIGHT requires watchlist_competition=SPOTLIGHT_1')
    if d['decision_class']=='NO_SPOTLIGHT':
        if d['ticker']!='NONE': fail('NO_SPOTLIGHT requires ticker="NONE"')
        if d.get('spotlight_rank') is not None: fail('NO_SPOTLIGHT requires spotlight_rank=null')
        if d['championship_result']!='CASH_WAIT': fail('NO_SPOTLIGHT requires championship_result=CASH_WAIT')
        if d['watchlist_competition']!='NOT_RANKED': fail('NO_SPOTLIGHT requires watchlist_competition=NOT_RANKED')
    return []

def main():
    if len(sys.argv)!=2:
        print('Usage: validate_decision_envelope.py <research-envelope.json>',file=sys.stderr); return 2
    try:
        d=json.loads(Path(sys.argv[1]).read_text())
        validate(d)
    except Exception as e:
        print(f'FAIL: {e}',file=sys.stderr); return 1
    print('PASS: Public Research Envelope v1.0.3 is non-personalized, non-executable, and cleanly separated from CASH/WAIT.')
    return 0

if __name__=='__main__': raise SystemExit(main())
