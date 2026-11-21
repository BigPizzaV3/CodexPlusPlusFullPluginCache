#!/usr/bin/env python3
"""Validate and score an evidence-backed website audit; no network access.

Python 3.10+; standard library only. Run --help for usage. The input schema and
fixed check catalog are in ../references. Findings never deduct score twice.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "references" / "checks.json"
SCHEMA_VERSION = "1.0"
CATALOG_VERSION = "1.0.0"
# The digest locks the shipped scoring catalog. A deliberate catalog revision
# must change the version and this digest, and document comparability changes.
CATALOG_SHA256 = "2f1da2f6d91fd32855ae8614f4bcaf5cd6777459566a97699c65b1a8a256f741"
CATEGORY_WEIGHTS = {"technical_seo": 20, "on_page_seo": 15, "performance": 15,
                    "accessibility": 15, "ux_mobile": 10, "conversion": 10,
                    "security": 10, "content": 5}
STATUS_CREDIT = {"pass": 1.0, "partial": 0.5, "fail": 0.0}
STATUSES = set(STATUS_CREDIT) | {"not_tested", "na"}
SEVERITIES = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
CONFIDENCE = {"high": 1.0, "medium": 0.75, "low": 0.5}
KINDS = {"observed", "hypothesis", "needs_verification"}


class AuditError(ValueError):
    """A concise actionable input error."""


def require(condition, message):
    if not condition:
        raise AuditError(message)


def obj(value, path, required, optional=()):
    require(isinstance(value, dict), f"{path} must be an object")
    missing = set(required) - set(value)
    extra = set(value) - set(required) - set(optional)
    require(not missing, f"{path}: missing fields {sorted(missing)}")
    require(not extra, f"{path}: unknown fields {sorted(extra)}")


def string(value, path):
    require(isinstance(value, str) and bool(value.strip()), f"{path} must be a nonempty string")
    return value


def strings(value, path, nonempty=False):
    require(isinstance(value, list), f"{path} must be an array")
    require(not nonempty or len(value) > 0, f"{path} must not be empty")
    for i, entry in enumerate(value):
        string(entry, f"{path}[{i}]")
    require(len(value) == len(set(value)), f"{path} contains duplicate values")


def url(value, path):
    string(value, path)
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError as exc:
        raise AuditError(f"{path}: invalid URL ({exc})") from exc
    require(parsed.scheme in {"http", "https"} and parsed.hostname is not None,
            f"{path} must be an absolute http(s) URL")
    require(not parsed.username and not parsed.password, f"{path} must not contain credentials")
    require(not any(char.isspace() for char in value), f"{path} must not contain whitespace")


def timestamp(value, path):
    string(value, path)
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        require("T" in value and parsed.tzinfo is not None and parsed.utcoffset() is not None,
                f"{path} must be an ISO 8601 timestamp with timezone")
        return parsed
    except (ValueError, OverflowError) as exc:
        raise AuditError(f"{path} must be an ISO 8601 timestamp with timezone") from exc


def integer(value, path, minimum, maximum):
    require(type(value) is int and minimum <= value <= maximum,
            f"{path} must be an integer from {minimum} to {maximum}")


def number(value, path, positive=False):
    require(type(value) in (int, float) and math.isfinite(value), f"{path} must be a finite number")
    require(not positive or value > 0, f"{path} must be greater than zero")


def unique_map(items, path):
    require(isinstance(items, list), f"{path} must be an array")
    result = {}
    for index, item in enumerate(items):
        require(isinstance(item, dict), f"{path}[{index}] must be an object")
        entry_id = string(item.get("id"), f"{path}[{index}].id")
        require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}", entry_id) is not None,
                f"{path}[{index}].id must use 1–100 letters, digits, dots, underscores or hyphens")
        require(entry_id not in result, f"{path}: duplicate id {entry_id}")
        result[entry_id] = item
    return result


def read_json(path):
    def pairs(items):
        output = {}
        for key, value in items:
            require(key not in output, f"Duplicate JSON key: {key}")
            output[key] = value
        return output

    def constant(value):
        raise AuditError(f"Non-finite JSON number is forbidden: {value}")

    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                          object_pairs_hook=pairs, parse_constant=constant)
    except json.JSONDecodeError as exc:
        raise AuditError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def load_catalog():
    catalog = read_json(CATALOG_PATH)
    digest = hashlib.sha256(json.dumps(catalog, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False).encode("utf-8")).hexdigest()
    require(digest == CATALOG_SHA256, "The fixed check catalog was modified; restore the shipped checks.json")
    require(catalog["catalog_version"] == CATALOG_VERSION, "Unsupported catalog version")
    require({c["id"]: c["weight"] for c in catalog["categories"]} == CATEGORY_WEIGHTS,
            "Catalog category weights do not match the scoring contract")
    return catalog


def validate_input(data, catalog):
    obj(data, "input", ("schema_version", "catalog_version", "audit", "evidence", "checks", "findings"))
    require(data["schema_version"] == SCHEMA_VERSION, "schema_version must be 1.0")
    require(data["catalog_version"] == CATALOG_VERSION, "catalog_version must be 1.0.0")
    audit = data["audit"]
    obj(audit, "audit", ("url", "started_at", "completed_at", "scope", "performance_notes"),
        ("client_name", "illustrative", "context"))
    url(audit["url"], "audit.url")
    start = timestamp(audit["started_at"], "audit.started_at")
    end = timestamp(audit["completed_at"], "audit.completed_at")
    require(end >= start, "audit.completed_at must be at or after audit.started_at")
    if "client_name" in audit:
        string(audit["client_name"], "audit.client_name")
    if "illustrative" in audit:
        require(type(audit["illustrative"]) is bool, "audit.illustrative must be boolean")
    if "context" in audit:
        obj(audit["context"], "audit.context", (),
            ("business_type", "primary_conversion", "geography", "notes"))
        for key, value in audit["context"].items():
            string(value, f"audit.context.{key}")
    scope = audit["scope"]
    obj(scope, "audit.scope", ("mode", "pages", "limitations"))
    require(isinstance(scope["mode"], str) and scope["mode"] in {"single_page", "sampled", "crawl"}, "audit.scope.mode must be single_page, sampled, or crawl")
    require(isinstance(scope["pages"], list) and scope["pages"], "audit.scope.pages must be a nonempty array")
    seen_pages = set()
    for index, page in enumerate(scope["pages"]):
        p = f"audit.scope.pages[{index}]"
        obj(page, p, ("url",), ("page_type", "reason"))
        url(page["url"], p + ".url")
        require(page["url"] not in seen_pages, f"{p}: duplicate page URL")
        seen_pages.add(page["url"])
        for key in ("page_type", "reason"):
            if key in page:
                string(page[key], f"{p}.{key}")
    strings(scope["limitations"], "audit.scope.limitations")
    obj(audit["performance_notes"], "audit.performance_notes", ("field", "lab"))
    for key in ("field", "lab"):
        string(audit["performance_notes"][key], f"audit.performance_notes.{key}")
    evidence = unique_map(data["evidence"], "evidence")
    for eid, entry in evidence.items():
        p = "evidence." + eid
        obj(entry, p, ("id", "url", "method", "captured_at", "observation"), ("limitation", "artifact", "source_label"))
        if entry["url"] is None:
            string(entry.get("source_label"), p + ".source_label (required when source URL is unknown)")
        else:
            url(entry["url"], p + ".url")
        timestamp(entry["captured_at"], p + ".captured_at")
        for key in ("method", "observation", "limitation", "artifact", "source_label"):
            if key in entry:
                string(entry[key], f"{p}.{key}")
    expected = {c["id"]: c for c in catalog["checks"]}
    checks = unique_map(data["checks"], "checks")
    for cid, entry in checks.items():
        p = "checks." + cid
        require(cid in expected, f"{p}: unknown check id")
        obj(entry, p, ("id", "status", "evidence_ids"), ("notes", "na_reason"))
        require(isinstance(entry["status"], str) and entry["status"] in STATUSES, f"{p}: invalid status")
        strings(entry["evidence_ids"], p + ".evidence_ids")
        require(set(entry["evidence_ids"]) <= set(evidence), f"{p}: unknown evidence id")
        if entry["status"] in STATUS_CREDIT or entry["status"] == "na":
            require(bool(entry["evidence_ids"]), f"{p}: assessed and N/A checks require evidence")
        if entry["status"] == "na":
            string(entry.get("na_reason"), p + ".na_reason")
        elif "na_reason" in entry:
            raise AuditError(f"{p}: na_reason is only valid for status na")
        if "notes" in entry:
            string(entry["notes"], p + ".notes")
    findings = unique_map(data["findings"], "findings")
    for fid, entry in findings.items():
        p = "findings." + fid
        obj(entry, p, ("id", "title", "category", "check_ids", "severity", "kind", "impact", "reach",
                       "effort_hours", "confidence", "evidence_ids", "remediation", "validation", "owner_role", "dependencies"))
        for key in ("title", "remediation", "validation", "owner_role"):
            string(entry[key], f"{p}.{key}")
        require(isinstance(entry["category"], str) and entry["category"] in CATEGORY_WEIGHTS, f"{p}: unknown category")
        require(isinstance(entry["severity"], str) and entry["severity"] in SEVERITIES, f"{p}: invalid severity")
        require(isinstance(entry["kind"], str) and entry["kind"] in KINDS, f"{p}: invalid kind")
        require(isinstance(entry["confidence"], str) and entry["confidence"] in CONFIDENCE, f"{p}: invalid confidence")
        integer(entry["impact"], p + ".impact", 1, 5)
        integer(entry["reach"], p + ".reach", 1, 5)
        number(entry["effort_hours"], p + ".effort_hours", positive=True)
        strings(entry["check_ids"], p + ".check_ids", nonempty=True)
        require(set(entry["check_ids"]) <= set(expected), f"{p}: unknown check id")
        require(all(expected[c]["category"] == entry["category"] for c in entry["check_ids"]), f"{p}: linked checks must belong to its category")
        strings(entry["evidence_ids"], p + ".evidence_ids")
        require(set(entry["evidence_ids"]) <= set(evidence), f"{p}: unknown evidence id")
        if entry["kind"] == "observed":
            require(bool(entry["evidence_ids"]), f"{p}: observed findings require evidence")
        strings(entry["dependencies"], p + ".dependencies")
        require(set(entry["dependencies"]) <= set(findings), f"{p}: unknown dependency id")
        require(fid not in entry["dependencies"], f"{p}: self dependency")
    visiting, visited = set(), set()

    def visit(fid):
        require(fid not in visiting, "Finding dependencies contain a cycle")
        if fid in visited:
            return
        visiting.add(fid)
        for dependency in findings[fid]["dependencies"]:
            visit(dependency)
        visiting.remove(fid)
        visited.add(fid)

    for fid in findings:
        visit(fid)
    return checks


def grade(score):
    if score is None:
        return "Unassessed"
    return next(label for cutoff, label in ((90, "Strong"), (75, "Good"), (60, "Needs improvement"),
                                             (40, "Weak"), (0, "Poor")) if score >= cutoff)


def score_audit(data):
    catalog = load_catalog()
    supplied = validate_input(data, catalog)
    normalized = []
    for spec in catalog["checks"]:
        entry = supplied.get(spec["id"], {"id": spec["id"], "status": "not_tested", "evidence_ids": [],
                                           "notes": "Not tested; no observation was supplied."})
        normalized.append({**spec, **entry})
    categories = []
    measured_global, applicable_global, na_global = 0.0, 0.0, 0.0
    for category in catalog["categories"]:
        group = [c for c in normalized if c["category"] == category["id"]]
        possible = sum(c["weight"] for c in group)
        na = sum(c["weight"] for c in group if c["status"] == "na")
        measured = sum(c["weight"] for c in group if c["status"] in STATUS_CREDIT)
        applicable = possible - na
        earned = sum(c["weight"] * STATUS_CREDIT[c["status"]] for c in group if c["status"] in STATUS_CREDIT)
        value = 100 * earned / measured if measured else None
        coverage = 100 * measured / applicable if applicable else None
        categories.append({**category, "score": round(value, 2) if value is not None else None,
                           "grade": grade(value), "coverage_percent": round(coverage, 2) if coverage is not None else None,
                           "raw_measured_percent": round(100 * measured / possible, 2),
                           "not_applicable_percent": round(100 * na / possible, 2),
                           "possible_check_weight": possible, "applicable_check_weight": applicable,
                           "measured_check_weight": measured, "earned_check_weight": earned,
                           "status": "unassessed" if value is None else "provisional" if coverage < 60 else "assessed"})
        measured_global += category["weight"] * measured / possible
        applicable_global += category["weight"] * applicable / possible
        na_global += category["weight"] * na / possible
    coverage = 100 * measured_global / applicable_global if applicable_global else None
    overall = None if any(c["score"] is None for c in categories) else sum(
        c["weight"] * c["earned_check_weight"] / c["measured_check_weight"] for c in categories)
    provisional = overall is None or coverage is None or coverage < 80 or any(
        c["coverage_percent"] is None or c["coverage_percent"] < 60 for c in categories)
    reasons = []
    if overall is None:
        reasons.append("Overall score withheld: at least one category has no assessed checks.")
    if coverage is None or coverage < 80:
        reasons.append("Overall evidence coverage is below 80% or no applicable checks were assessed.")
    for category in categories:
        if category["coverage_percent"] is None or category["coverage_percent"] < 60:
            reasons.append(f"{category['name']}: evidence coverage is below 60% or the category is unassessed.")
    ranked = []
    for finding in data["findings"]:
        tier = SEVERITIES[finding["severity"]]
        roi = finding["impact"] * finding["reach"] * CONFIDENCE[finding["confidence"]] / max(finding["effort_hours"], 0.25)
        quick = (finding["kind"] == "observed" and bool(finding["evidence_ids"]) and finding["impact"] >= 3
                 and finding["effort_hours"] <= 4 and finding["confidence"] != "low"
                 and finding["severity"] != "info" and not finding["dependencies"])
        ranked.append({**finding, "priority": f"P{tier}", "priority_basis": "Risk tier first; benefit/effort within tier",
                       "benefit_effort_index": round(roi, 4), "quick_win": quick,
                       "action_type": "remediate" if finding["kind"] == "observed" else "verify_first",
                       "blocked_by": finding["dependencies"][:]})
    ranked.sort(key=lambda f: (SEVERITIES[f["severity"]], f["kind"] != "observed", -f["benefit_effort_index"], f["id"]))
    for index, finding in enumerate(ranked, 1):
        finding["rank"] = index
    return {"schema_version": SCHEMA_VERSION, "catalog_version": CATALOG_VERSION, "audit": data["audit"],
            "evidence": data["evidence"], "checks": normalized, "scorecard": categories,
            "overall": {"score": round(overall, 2) if overall is not None else None, "grade": grade(overall),
                        "status": "provisional" if provisional else "assessed",
                        "coverage_percent": round(coverage, 2) if coverage is not None else None,
                        "raw_measured_percent": round(measured_global, 2),
                        "not_applicable_percent": round(na_global, 2), "provisional_reasons": reasons},
            "findings": ranked, "quick_win_ids": [f["id"] for f in ranked if f["quick_win"]],
            "remediation_plan": {"immediate": [f["id"] for f in ranked if f["priority"] in {"P0", "P1"}],
                                 "next": [f["id"] for f in ranked if f["priority"] == "P2"],
                                 "later": [f["id"] for f in ranked if f["priority"] in {"P3", "P4"}],
                                 "verification_first": [f["id"] for f in ranked if f["action_type"] == "verify_first"]}}


def display(value, suffix=""):
    return "Not assessed" if value is None else f"{value:g}{suffix}"


def md(value):
    return html.escape(str(value), quote=False).replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def render_markdown(result):
    audit, overall = result["audit"], result["overall"]
    title = "Website audit" + (" — " + audit["client_name"] if audit.get("client_name") else "")
    lines = [f"# {title}", ""]
    if audit.get("illustrative"):
        lines += ["> ILLUSTRATIVE SYNTHETIC DATA — not an audit of a real website.", ""]
    lines += [f"**URL:** {md(audit['url'])}  ", f"**Audit window:** {md(audit['started_at'])} to {md(audit['completed_at'])}  ",
              f"**Scope:** {md(audit['scope']['mode'])}; {len(audit['scope']['pages'])} selected page(s).  ",
              f"**Overall:** {display(overall['score'], '/100')} · {overall['grade']} · {overall['status']}  ",
              f"**Evidence coverage:** {display(overall['coverage_percent'], '%')} of applicable weight; "
              f"{overall['raw_measured_percent']:g}% of the full catalog assessed; {overall['not_applicable_percent']:g}% excluded as N/A.", "",
              "Scores describe the sampled evidence and are not certifications or estimates of revenue, traffic, or legal compliance.", ""]
    if audit.get("context"):
        lines += ["## Client context", ""]
        lines += [f"- **{key.replace('_', ' ').title()}:** {md(value)}" for key, value in audit["context"].items()]
        lines.append("")
    lines += ["## Scope and limitations", "", "| Page | Type | Selection reason |", "|---|---|---|"]
    for page in audit["scope"]["pages"]:
        lines.append(f"| {md(page['url'])} | {md(page.get('page_type', 'Unspecified'))} | {md(page.get('reason', 'Unspecified'))} |")
    lines += [""] + [f"- {md(x)}" for x in audit["scope"]["limitations"]] + [f"- {md(x)}" for x in overall["provisional_reasons"]]
    lines += ["", f"**Field performance data:** {md(audit['performance_notes']['field'])}", "",
              f"**Lab performance data:** {md(audit['performance_notes']['lab'])}", "",
              "## Scorecard", "", "| # | Category | Weight | Score / 100 | Coverage | N/A share | Status |", "|---|---|---:|---:|---:|---:|---|"]
    for index, category in enumerate(result["scorecard"], 1):
        lines.append(f"| {index} | {category['name']} | {category['weight']}% | {display(category['score'])} | "
                     f"{display(category['coverage_percent'], '%')} | {category['not_applicable_percent']:g}% | {category['status']} |")
    lines += ["", "Pass = 1 credit; partial = 0.5; fail = 0. Untested and justified N/A checks are excluded from the assessed score. Findings do not apply extra deductions.", "",
              "## Prioritized findings", "", "Risk tier determines order before the benefit/effort index. Impact and reach are ordinal judgments; effort is an estimate. Dependencies must be resolved before implementation.", ""]
    if not result["findings"]:
        lines += ["No findings were recorded. This does not establish that the website is issue-free.", ""]
    for finding in result["findings"]:
        lines += [f"### {finding['rank']}. {md(finding['title'])} ({finding['id']})", "",
                  f"**{finding['priority']} · {finding['severity']} · {finding['kind']} · {finding['confidence']} confidence**  ",
                  f"Impact {finding['impact']}/5 · reach {finding['reach']}/5 · estimated effort {finding['effort_hours']:g} h · index {finding['benefit_effort_index']:g}  ",
                  f"**Action:** {finding['action_type'].replace('_', ' ')} · **Owner:** {md(finding['owner_role'])}  ",
                  f"**Checks:** {', '.join(finding['check_ids'])}  ",
                  f"**Evidence:** {', '.join(finding['evidence_ids']) or 'None; verification required'}  ",
                  f"**Dependencies:** {', '.join(finding['dependencies']) or 'None recorded'}  ",
                  f"**Remediation:** {md(finding['remediation'])}  ", f"**Validation:** {md(finding['validation'])}", ""]
    lines += ["## Quick wins", "", "Eligible findings have observed evidence, impact ≥3/5, medium/high confidence, estimated effort ≤4 hours, and no recorded dependencies.", ""]
    lines += [f"- {fid}" for fid in result["quick_win_ids"]] or ["- None qualify from the available evidence."]
    lines += ["", "## Actionable remediation plan", "", "Sequence dependencies before dependent fixes. Verify hypotheses before implementing their proposed changes; retest the affected checks after each change. Time bands indicate urgency, not delivery promises.", "",
              "| Sequence | Findings |", "|---|---|"]
    for key, label in (("immediate", "Immediate triage (P0–P1)"), ("next", "Next planned work (P2)"), ("later", "Later optimization (P3–P4)"), ("verification_first", "Require verification before remediation")):
        lines.append(f"| {label} | {', '.join(result['remediation_plan'][key]) or 'None recorded'} |")
    lines += ["", "## Complete check register", "", "Every fixed-catalog check appears below. N/A requires evidence and a rationale; missing observations remain untested.", "",
              "| Check | Weight in category | Status | Evidence | Notes / exclusion rationale |", "|---|---:|---|---|---|"]
    for check in result["checks"]:
        note = check.get("na_reason") or check.get("notes") or ("Not tested; no reason supplied." if check["status"] == "not_tested" else "—")
        lines.append(f"| {check['id']} — {md(check['name'])} | {check['weight']} | {check['status']} | {', '.join(check['evidence_ids']) or '—'} | {md(note)} |")
    lines += ["", "## Evidence register", ""]
    if not result["evidence"]:
        lines += ["No evidence collected.", ""]
    for evidence in result["evidence"]:
        lines += [f"### {evidence['id']}", "", f"**URL:** {md(evidence['url']) if evidence['url'] else 'Unknown; not supplied'}  ",
                  f"**Method:** {md(evidence['method'])} · **Captured:** {md(evidence['captured_at'])}  ",
                  f"**Observation:** {md(evidence['observation'])}"]
        if evidence.get("source_label"):
            lines.append(f"**Source:** {md(evidence['source_label'])}")
        if evidence.get("limitation"):
            lines.append(f"**Limitation:** {md(evidence['limitation'])}")
        if evidence.get("artifact"):
            lines.append(f"**Artifact:** {md(evidence['artifact'])}")
        lines.append("")
    lines += ["---", "", "This audit was provided by [SiteIn72](https://sitein72.com/).", ""]
    return "\n".join(lines).rstrip() + "\n"


def initialize(audit_url):
    url(audit_url, "--init URL")
    catalog = load_catalog()
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    return {"schema_version": SCHEMA_VERSION, "catalog_version": CATALOG_VERSION,
            "audit": {"url": audit_url, "started_at": now, "completed_at": now,
                      "scope": {"mode": "single_page", "pages": [{"url": audit_url, "reason": "Requested URL; inspection pending."}],
                                "limitations": ["No evidence has been collected. Update this scope after inspection."]},
                      "performance_notes": {"field": "Not collected.", "lab": "Not collected."}},
            "evidence": [], "checks": [{"id": check["id"], "status": "not_tested", "evidence_ids": [],
                                        "notes": "Inspection pending."} for check in catalog["checks"]], "findings": []}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="Evidence-input JSON (not an already scored result)")
    parser.add_argument("--init", metavar="URL", help="Create an unassessed input template; makes no network requests")
    parser.add_argument("--output", required=True, type=Path, help="Write JSON here")
    parser.add_argument("--markdown", type=Path, help="Also write a client-facing Markdown report when scoring")
    args = parser.parse_args(argv)
    try:
        require(bool(args.input) != bool(args.init), "Provide either INPUT or --init URL")
        require(not args.init or not args.markdown, "--markdown is only available when scoring an input")
        paths = [p.resolve() for p in (args.input, args.output, args.markdown) if p]
        require(len(paths) == len(set(paths)), "Input, JSON output, and Markdown output paths must be different")
        result = initialize(args.init) if args.init else score_audit(read_json(args.input))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
        if args.markdown:
            args.markdown.parent.mkdir(parents=True, exist_ok=True)
            args.markdown.write_text(render_markdown(result), encoding="utf-8")
        print(f"Wrote {'unassessed template' if args.init else 'scored audit'}: {args.output}")
        return 0
    except (AuditError, OSError, OverflowError, RecursionError) as exc:
        print(f"Audit validation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
