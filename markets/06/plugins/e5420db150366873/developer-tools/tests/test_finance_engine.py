import importlib.util, math
from pathlib import Path

p=Path(__file__).resolve().parents[1]/"finance_engine.py"
spec=importlib.util.spec_from_file_location("finance_engine",p)
f=importlib.util.module_from_spec(spec); spec.loader.exec_module(f)

def test_dcf():
    r=f.dcf_fcff([100,110,121],0.10,0.03,net_debt=50,diluted_shares=10)
    assert r["enterprise_value"] > r["pv_explicit_fcff"]
    assert math.isclose(r["equity_value"], r["enterprise_value"]-50)
    assert math.isclose(r["equity_value_per_share"], r["equity_value"]/10)

def test_pvm_reconciles():
    r=f.price_volume_mix_bridge(100,10,110,11)
    assert math.isclose(r["total_change"], r["reconciliation"])

def test_scenario_probability_guard():
    try:
        f.scenario_expected_value([1,2],[0.4,0.4])
    except ValueError:
        pass
    else:
        raise AssertionError("expected probability sum error")

def test_reverse_gordon_identity():
    flows=[100,110,121]
    ev=f.dcf_fcff(flows,0.10,0.03)["enterprise_value"]
    g=f.implied_perpetual_growth(ev,flows,0.10)
    assert abs(g-0.03)<1e-9
