#!/usr/bin/env python3
"""Process large AML report from generateAmlStandardReport / generateAmlEnhancedReport.

Converts a 300-500 KB report into a ~2-3 KB context-safe summary covering:
- Report info (address, risk score, grade)
- C-Score top risk factors
- Flagged counterparties
- Exposure summary by category
- Monitoring flags (sanctions, darknet, ransomware, mixer)
- Transaction stats
- Quick recommendations

Accepts both standard JSON and Lukka compact notation (unquoted keys and
bare-string values, which the hosted MCP servers emit).

Usage:
    python3 process_aml_report.py <file>
    python3 process_aml_report.py <file> --full-risks
    python3 process_aml_report.py <file> --format json
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lukka_notation import load as _load, rows_to_dicts as _shared_rows_to_dicts  # noqa: E402


HIGH_RISK_CATEGORIES = {
    "mixer", "tumbler", "coinjoin",
    "darknet", "dark market", "darkmarket",
    "ransomware",
    "sanctions", "ofac",
    "stolen", "hack",
    "scam", "fraud", "phishing",
    "child abuse",
    "terror", "terrorism",
    "no-kyc", "no kyc",
}


def walk(obj, path=""):
    """Yield (path, value) for every scalar leaf in nested dict/list."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    else:
        yield path, obj


def find_first(data, *keys):
    """Return first non-None value whose path ends with any of the keys."""
    for key in keys:
        for p, v in walk(data):
            if p.split(".")[-1] == key or p.endswith(f"]{key}"):
                if v is not None and v != "":
                    return v
    return None


def find_list(data, *keys):
    """Return the first list whose enclosing key matches any of keys."""
    if isinstance(data, dict):
        for k, v in data.items():
            if k in keys and isinstance(v, list):
                return v
        for v in data.values():
            r = find_list(v, *keys)
            if r is not None:
                return r
    elif isinstance(data, list):
        for v in data:
            r = find_list(v, *keys)
            if r is not None:
                return r
    return None


_rows_to_dicts = _shared_rows_to_dicts


def extract_risks(data):
    """Find the list of risk factors / risk indicators.

    Supports:
    - Lukka compact table under ``cscore_section.cscore_info`` (cols/rows).
    - Legacy list-of-dicts under ``risks``/``risk_factors``/etc.
    """
    cscore = None
    if isinstance(data, dict):
        cscore = data.get("cscore_section")
    if isinstance(cscore, dict):
        info = cscore.get("cscore_info")
        # scoring reports: cscore_info is already a list of dicts [{name,type,id},...]
        if isinstance(info, list) and info and isinstance(info[0], dict):
            return info
        # standard/enhanced reports: compact cols/rows table
        table = _rows_to_dicts(info)
        if table:
            return table
    for key in ("risks", "risk_factors", "riskFactors", "risk_indicators", "riskIndicators", "indicators"):
        lst = find_list(data, key)
        if lst:
            return lst
    return []


def normalize_risk(r):
    if not isinstance(r, dict):
        return {"name": str(r), "group": "", "impact": ""}
    impact = (
        r.get("impact") or r.get("severity") or r.get("weight") or r.get("score") or ""
    )
    if isinstance(impact, str):
        try:
            impact = int(impact)
        except ValueError:
            try:
                impact = float(impact)
            except ValueError:
                pass
    return {
        "name": r.get("name") or r.get("indicator") or r.get("title") or r.get("code") or "?",
        "group": r.get("group") or r.get("group_name") or r.get("category") or r.get("risk_group") or "",
        "impact": impact,
        "is_direct": bool(r.get("direct") or r.get("is_direct") or r.get("type") == 1 or r.get("type") == "1" or False),
    }


def extract_counterparties(data):
    for key in ("counterparties", "flagged_counterparties", "flaggedCounterparties",
                "risky_counterparties", "connections", "related_addresses"):
        lst = find_list(data, key)
        if lst:
            return lst
    return []


def extract_exposure(data):
    if not isinstance(data, dict):
        return None
    for key in ("exposure", "exposures", "exposure_summary", "categoryExposure", "category_exposure"):
        if key in data and isinstance(data[key], (dict, list)):
            return data[key]
    for v in data.values():
        if isinstance(v, dict):
            result = extract_exposure(v)
            if result is not None:
                return result
    return None


def categorize_flags(risks):
    flags = defaultdict(int)
    for r in risks:
        label = (r.get("name", "") + " " + r.get("group", "")).lower()
        for cat in HIGH_RISK_CATEGORIES:
            if cat in label:
                flags[cat] += 1
    return dict(flags)


def truncate(s, n=60):
    s = str(s)
    return s if len(s) <= n else s[: n - 1] + "..."


def truncate_addr(addr):
    if not addr:
        return "?"
    addr = str(addr)
    if len(addr) < 16:
        return addr
    return f"{addr[:10]}...{addr[-4:]}"


def summarize(data, args):
    out = {
        "report_info": {},
        "cscore": {},
        "flagged_counterparties": [],
        "exposure_summary": {},
        "monitoring_flags": {},
        "tx_stats": {},
        "recommendations": [],
    }

    out["report_info"] = {
        "address": find_first(data, "address", "wallet_address", "walletAddress"),
        "blockchain": find_first(data, "address_type", "addressType", "blockchain", "chain", "network"),
        "report_type": find_first(data, "report_type", "reportType"),
        "version": find_first(data, "version", "report_version", "reportVersion"),
        "report_id": find_first(data, "report_id", "reportId", "report_uuid", "reportUuid"),
        "report_time": find_first(data, "report_time", "reportTime", "generatedAt", "generated_at",
                                  "timestamp", "createdAt", "created_at"),
        "risk_score": find_first(data, "risk_score", "riskScore", "cscore", "cScore", "score"),
        "risk_level": find_first(data, "risk_level", "riskLevel", "level", "grade", "letter_grade",
                                 "letterGrade"),
    }

    risks = [normalize_risk(r) for r in extract_risks(data)]
    top_n = len(risks) if args.full_risks else 10
    top_risks = sorted(
        risks,
        key=lambda r: -(r["impact"] if isinstance(r["impact"], (int, float)) else 0)
    )[:top_n]
    out["cscore"] = {
        "score": out["report_info"].get("risk_score"),
        "total_factors": len(risks),
        "direct_factors": sum(1 for r in risks if r["is_direct"]),
        "top_factors": [
            {
                "name": truncate(r["name"], 80),
                "group": truncate(r["group"], 40),
                "impact": r["impact"],
                "direct": r["is_direct"],
            }
            for r in top_risks
        ],
    }

    counterparties = extract_counterparties(data)
    top_cps = []
    for cp in counterparties[:10]:
        if isinstance(cp, dict):
            top_cps.append({
                "address": truncate_addr(cp.get("address") or cp.get("addr") or cp.get("wallet")),
                "risk": cp.get("risk_level") or cp.get("riskLevel") or cp.get("risk") or "",
                "category": truncate(cp.get("category") or cp.get("type") or "", 40),
                "amount": cp.get("amount") or cp.get("volume") or cp.get("value") or "",
            })
        else:
            top_cps.append({"address": truncate_addr(cp), "risk": "", "category": "", "amount": ""})
    out["flagged_counterparties"] = top_cps

    exposure = extract_exposure(data)
    if isinstance(exposure, dict):
        out["exposure_summary"] = {
            k: truncate(v, 80) if isinstance(v, str) else v
            for k, v in list(exposure.items())[:20]
        }
    elif isinstance(exposure, list):
        out["exposure_summary"] = {
            "items": len(exposure),
            "top": [truncate(str(e), 100) for e in exposure[:5]],
        }

    out["monitoring_flags"] = categorize_flags(risks)

    out["tx_stats"] = {
        "total_in": find_first(data, "total_inbound", "totalInbound", "inbound_count"),
        "total_out": find_first(data, "total_outbound", "totalOutbound", "outbound_count"),
        "total_tx_count": find_first(data, "tx_count", "transactionCount", "total_tx"),
        "largest_tx": find_first(data, "largest_transaction", "largestTransaction", "max_tx_amount"),
        "first_activity": find_first(data, "first_activity", "firstActivity", "firstSeen"),
        "last_activity": find_first(data, "last_activity", "lastActivity", "lastSeen"),
    }

    recs = []
    if out["monitoring_flags"]:
        recs.append(f"Address shows {sum(out['monitoring_flags'].values())} high-risk indicators across {len(out['monitoring_flags'])} categories.")
    if out["cscore"].get("direct_factors"):
        recs.append(f"{out['cscore']['direct_factors']} direct risk factors detected - treat as primary exposure.")
    if top_cps:
        recs.append(f"Review top {len(top_cps)} flagged counterparties before permitting outbound transfers.")
    if not recs:
        recs.append("No high-risk indicators detected in summary view. Review full report for context.")
    out["recommendations"] = recs

    return out


def print_table(summary):
    ri = summary["report_info"]
    print("AML Report Summary")
    print("=" * 60)
    print(f"Address:      {ri.get('address') or '?'}")
    print(f"Blockchain:   {ri.get('blockchain') or '?'}")
    print(f"Risk Score:   {ri.get('risk_score') or '?'}")
    print(f"Risk Level:   {ri.get('risk_level') or '?'}")
    print(f"Report ID:    {ri.get('report_id') or '?'}")
    print(f"Generated:    {ri.get('report_time') or '?'}")

    cs = summary["cscore"]
    print(f"\nC-Score: {cs.get('score') or '?'}   factors: {cs.get('total_factors')} (direct: {cs.get('direct_factors')})")
    if cs.get("top_factors"):
        print("\nTop Risk Factors:")
        for f in cs["top_factors"]:
            mark = "*" if f["direct"] else " "
            print(f"  {mark} {truncate(f['name'], 50):52s} {truncate(f['group'], 20):22s} {f['impact']}")

    flags = summary["monitoring_flags"]
    if flags:
        print("\nMonitoring Flags:")
        for cat, n in sorted(flags.items(), key=lambda kv: -kv[1]):
            print(f"  {cat:20s} {n}")

    cps = summary["flagged_counterparties"]
    if cps:
        print("\nFlagged Counterparties:")
        for cp in cps:
            print(f"  {cp['address']:25s} {cp['risk']:10s} {truncate(cp['category'], 30):32s} {cp['amount']}")

    exp = summary["exposure_summary"]
    if exp:
        print("\nExposure Summary:")
        for k, v in list(exp.items())[:10]:
            print(f"  {k:30s} {v}")

    tx = summary["tx_stats"]
    print("\nTx Stats:")
    for k, v in tx.items():
        if v is not None:
            print(f"  {k:20s} {v}")

    print("\nRecommendations:")
    for r in summary["recommendations"]:
        print(f"  - {r}")


def main():
    parser = argparse.ArgumentParser(description="Summarize AML standard/enhanced report JSON")
    parser.add_argument("file", help="JSON file from generateAmlStandardReport / generateAmlEnhancedReport")
    parser.add_argument("--full-risks", action="store_true", help="Include all risk factors (not just top 10)")
    parser.add_argument("--format", choices=["table", "json"], default="table", dest="fmt")
    args = parser.parse_args()

    try:
        data = _load(args.file)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, dict):
        print(
            f"Error: expected an AML report object (JSON/Lukka-notation dict), "
            f"got {type(data).__name__}. Is this a valid generateAml*Report payload?",
            file=sys.stderr,
        )
        sys.exit(1)

    summary = summarize(data, args)

    if args.fmt == "json":
        json.dump(summary, sys.stdout, indent=2)
        print()
    else:
        print_table(summary)


if __name__ == "__main__":
    main()
