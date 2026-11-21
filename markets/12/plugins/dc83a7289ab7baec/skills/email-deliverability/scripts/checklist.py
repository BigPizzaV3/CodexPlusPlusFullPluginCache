"""Apply Reteno's October 6 customer checklist to explicit account reference evidence."""
from __future__ import annotations

from copy import deepcopy

from audit_engine import (
    _check, check_host_resolution, check_short_link_tls, normalize_dns_name,
    normalize_hostname, summarize_checks,
)
from spf_policy import check_authorization


def missing(check_id, subject, message):
    return _check(check_id, "Account reference evidence", "unavailable", subject, message)


def validate_references(org_id, references):
    if not isinstance(references, dict):
        raise ValueError("Checklist references must be an object")
    if str(references.get("orgId", org_id)) != str(org_id):
        raise ValueError("Checklist references identify a different organization")
    for section in ("spf", "dkim", "links", "technical"):
        rows = references.get(section, [])
        if not isinstance(rows, list) or len(rows) > 128 or any(not isinstance(row, dict) for row in rows):
            raise ValueError(f"Checklist {section} must contain at most 128 objects")


def bind_checklist_scope(scope, references):
    """Use explicit active selectors instead of an unsupported fallback guess."""
    validate_references(scope["orgId"], references)
    scope = deepcopy(scope)
    for domain in scope["domains"]:
        suffix = "._domainkey." + domain["domain"]
        active, retired = set(), set()
        for item in references.get("dkim", []):
            name = normalize_dns_name(item.get("name", ""))
            if not name.endswith(suffix):
                continue
            if item.get("lifecycle") in {"active", "in_flight"}:
                active.add(name)
            elif item.get("lifecycle") == "retired":
                retired.add(name)
        if active or retired:
            existing = set(domain["dkimRecordNames"]) if not active or domain["dkimSelectorSource"] == "mcp" else set()
            domain["dkimRecordNames"] = sorted((existing | active) - retired)
            domain["dkimRetiredRecordNames"] = sorted(retired)
            if active:
                domain["dkimSelectorSource"] = "account-reference"
    return scope


def apply_checklist(report, references, resolver, *, tls_checker=None):
    validate_references(report["orgId"], references)
    checks = report["checks"]
    spf = references.get("spf", [])
    if not spf:
        checks.append(missing("spf.authorization", "sender", "Exact envelope/Return-Path domain and actual Reteno sending IPs are required; From-domain SPF is not proof."))
    for item in spf:
        domain = normalize_hostname(item.get("domain"))
        if not domain:
            raise ValueError("Invalid envelope domain reference")
        checks.append(check_authorization(domain, item.get("ips", []), resolver, item.get("expectedInclude")))

    dkim = references.get("dkim", [])
    if not any(item.get("lifecycle") in {"active", "in_flight"} for item in dkim):
        checks.append(missing("dkim.account_reference", "sender", "Active/in-flight selectors and expected TXT key or CNAME target are not exposed; standard-selector discovery is not account-reference verification."))
    for item in dkim:
        if item.get("lifecycle") == "retired":
            continue
        if item.get("lifecycle") not in {"active", "in_flight"}:
            checks.append(missing("dkim.account_reference", "sender", "Selector lifecycle is unknown."))
            continue
        name = normalize_dns_name(item.get("name", ""))
        kind = item.get("type")
        expected = item.get("value")
        if not name or "._domainkey." not in name or kind not in {"TXT", "CNAME"} or not isinstance(expected, str) or not expected:
            raise ValueError("DKIM reference needs an exact name, TXT/CNAME type and expected value")
        answer = resolver.resolve(name, kind)
        if answer.error_code not in {None, "no_answer", "nxdomain"}:
            checks.append(missing("dkim.account_reference", name, "DNS evidence is unavailable."))
        else:
            normalize = (lambda value: value.lower().rstrip(".")) if kind == "CNAME" else (lambda value: "".join(value.split()))
            matches = any(normalize(value) == normalize(expected) for value in answer.records)
            checks.append(_check("dkim.account_reference", "DKIM account record", "pass" if matches else "fail", name,
                                 "DKIM record matches the account reference." if matches else "DKIM record differs from the account reference."))

    links = references.get("links", [])
    if not links or not any(item.get("selected") is True for item in links):
        checks.append(missing("short_link.selected", "short-links", "The selected tracking domain, customer ownership and account-specific CNAME target need confirmation. destinationDomains are redirect destinations, not DNS targets."))
    known_domains = set(report["shortLinks"]["domains"])
    inventory = {item["domain"]: item for item in report["shortLinks"].get("inventory", [])}
    extra_domains = set()
    for item in links:
        domain = normalize_hostname(item.get("domain"))
        expected = normalize_hostname(item.get("expectedCname"))
        if not domain or not expected:
            raise ValueError("Link reference needs domain and expectedCname")
        if item.get("selected") is True:
            current = inventory.get(domain, {})
            shared = any(domain == host or domain.endswith("." + host) for host in ("reteno.com", "esputnik.com", "yespo.io"))
            if shared or item.get("customerControlled") is False or current.get("active") is False or current.get("issued") is False:
                status = "fail"
            elif domain not in known_domains:
                status = "fail" if report["shortLinks"].get("inventoryAvailable") is True else "unavailable"
            elif item.get("customerControlled") is True and current.get("active") is True and current.get("issued") is True:
                status = "pass"
            else:
                status = "unavailable"
            checks.append(_check("short_link.selected", "Selected custom link domain", status, domain,
                                 "Selected customer-controlled domain is active with an issued certificate." if status == "pass" else
                                 "Selected customer-controlled domain activation and certificate issuance are not confirmed."))
        if domain not in known_domains and domain not in extra_domains:
            extra_domains.add(domain)
            extra_checks = [check_host_resolution(domain, resolver, purpose="short-link-domain"),
                            check_short_link_tls(domain, tls_checker or (lambda host: {"state": "inconclusive", "reason": "not_checked"}))]
            checks.extend(extra_checks)
            report["shortLinks"].setdefault("checks", []).extend(extra_checks)
        lookup = resolver.resolve(domain, "CNAME")
        if lookup.error_code not in {None, "no_answer", "nxdomain"}:
            checks.append(missing("short_link.cname", domain, "CNAME evidence is unavailable."))
        else:
            matches = expected in [value.lower().rstrip(".") for value in lookup.records]
            checks.append(_check("short_link.cname", "Custom link CNAME", "pass" if matches else "fail", domain,
                                 "CNAME matches the account target." if matches else "CNAME does not match the account target."))

    technical_domains = {domain for item in report["domains"] for domain in item.get("technicalDomains", [])}
    technical = {normalize_hostname(item.get("domain")): item for item in references.get("technical", [])}
    for domain in technical_domains:
        expected = normalize_hostname(technical.get(domain, {}).get("mxTarget"))
        if not expected:
            checks.append(missing("technical.mx_target", domain, "Expected technical MX target is unavailable; conflicting documentation is not customer failure."))
            continue
        lookup = resolver.resolve(domain, "MX")
        if lookup.error_code not in {None, "no_answer", "nxdomain"}:
            checks.append(missing("technical.mx_target", domain, "MX evidence is unavailable."))
        else:
            matches = any(value.split()[-1].lower().rstrip(".") == expected for value in lookup.records)
            checks.append(_check("technical.mx_target", "Technical MX", "pass" if matches else "fail", domain,
                                 "MX matches the account target." if matches else "MX differs from the account target."))
    if not report["domains"]:
        checks.append(missing("sender.domains", "sender", "No sender domains were supplied for auditing."))
    report["summary"] = summarize_checks(checks)
    report["checklistVersion"] = "2026-10-06"
    return report
