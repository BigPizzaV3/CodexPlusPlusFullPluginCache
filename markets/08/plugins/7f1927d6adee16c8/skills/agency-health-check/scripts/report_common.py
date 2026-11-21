"""Shared helpers for build_report.py and build_client_pdfs.py."""

import json

STATUS = {
    "action": {
        "label": "Needs action now",
        "symbol": "✕",
        "rank": 0,
        "color": "C0392B",
        "tint": "F8D7DA",
    },
    "watch": {
        "label": "Keep an eye on",
        "symbol": "!",
        "rank": 1,
        "color": "B7791F",
        "tint": "FFF3CD",
    },
    "healthy": {
        "label": "Healthy",
        "symbol": "✓",
        "rank": 2,
        "color": "2F855A",
        "tint": "D4EDDA",
    },
}
CHECK_RESULT = {
    "pass": ("✓", "Passed"),
    "action": ("✕", "Needs action"),
    "watch": ("!", "Keep an eye on"),
    "not_enough_data": ("–", "Not enough calls to score"),
    "not_checked": ("?", "Not checked"),
    "not_applicable": ("–", "Doesn't apply"),
}
AREA_RANK = {"Setup": 0, "Website": 1, "Call volume": 2, "Call handling": 3, "Forms": 4}
SNAPSHOT = [
    ("calls", "Calls", ""),
    ("new_callers", "New callers", ""),
    ("answered_pct", "Answered", "%"),
    ("leads", "Leads", ""),
    ("forms", "Form submissions", ""),
]


def load(path):
    with open(path) as f:
        data = json.load(f)
    for c in data.get("companies", []):
        findings = [
            f for f in c.get("findings", []) if f.get("level") in ("action", "watch")
        ]
        findings.sort(
            key=lambda f: (STATUS[f["level"]]["rank"], AREA_RANK.get(f.get("area"), 9))
        )
        c["findings"] = findings
        c["status"] = findings[0]["level"] if findings else "healthy"
        snap = c.get("snapshot") or {}
        calls = snap.get("calls") or {}
        c["_prior_calls"] = calls.get("prior") or 0
    data["companies"].sort(
        key=lambda c: (
            STATUS[c["status"]]["rank"],
            -c["_prior_calls"],
            (c.get("name") or "").lower(),
        )
    )
    return data


def status_text(code):
    s = STATUS[code]
    return f"{s['symbol']} {s['label']}"


def trend(cur, prior, suffix=""):
    """Return (value text, change text) for a snapshot metric."""
    if cur is None:
        return "n/a", ""
    value = f"{cur}{suffix}"
    if prior is None:
        return value, ""
    if suffix == "%":
        diff = cur - prior
        if diff == 0:
            return value, f"= same as last month ({prior}%)"
        arrow = "▲" if diff > 0 else "▼"
        return value, f"{arrow} {abs(diff)} pts vs. {prior}%"
    if prior == 0:
        return value, ("= same as last month (0)" if cur == 0 else "▲ up from 0")
    pct = round((cur - prior) / prior * 100)
    if pct == 0:
        return value, f"= steady (last month {prior})"
    arrow = "▲" if pct > 0 else "▼"
    return value, f"{arrow} {abs(pct)}% vs. {prior}"


def period_text(data):
    cur = data.get("current_period", {})
    pri = data.get("prior_period", {})
    return (
        f"{cur.get('start', '')} to {cur.get('end', '')}, compared with "
        f"{pri.get('start', '')} to {pri.get('end', '')}"
    )


def wanted(c, include_all):
    return include_all or c["status"] != "healthy"
