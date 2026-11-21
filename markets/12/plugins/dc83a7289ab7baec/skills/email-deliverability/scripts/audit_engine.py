from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import ipaddress
import re
from typing import Any, Iterable, Mapping, Protocol


CHECK_PASS = "pass"
CHECK_WARN = "warn"
CHECK_FAIL = "fail"
CHECK_INFO = "info"
CHECK_SKIPPED = "skipped"
CHECK_UNAVAILABLE = "unavailable"

RETENO_DEFAULT_DKIM_SELECTOR = "esputnik"
DNS_ABSENCE_CODES = {None, "no_answer", "nxdomain"}
DKIM_KEY_STATES = {"active", "revoked", "invalid", "missing", "inconclusive"}

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]{1,64}@([A-Z0-9.-]+\.[A-Z]{2,63})\b")
_HOST_LABEL_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")
_DNS_LABEL_RE = re.compile(r"^_?[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$")
_SELECTOR_RE = re.compile(r"^[A-Za-z0-9_-]{1,63}$")
_SPF_LOOKUP_RE = re.compile(r"(?i)(?:^|\s)(include|a|mx|ptr|exists)(?::[^\s]+)?")
_SPF_REDIRECT_RE = re.compile(r"(?i)(?:^|\s)redirect=")
_BLOCKED_HOST_SUFFIXES = (
    ".docker",
    ".home",
    ".home.arpa",
    ".internal",
    ".lan",
    ".local",
    ".localdomain",
    ".localhost",
)
_BLOCKED_HOSTNAMES = {"host.docker.internal", "localhost", "metadata.google.internal"}
_CONFIGURATION_STATUSES = {
    "CONFIGURED",
    "VERIFIED",
    "PENDING",
    "FAILED",
    "NOT_CONFIGURED",
    "UNKNOWN",
}


class SetupValidationError(ValueError):
    """The MCP setup cannot be reduced to a trusted audit scope."""


@dataclass(frozen=True)
class LookupResult:
    records: list[str]
    error_code: str | None = None
    resolver: str | None = None
    fallback_used: bool = False


class DnsResolver(Protocol):
    def resolve(self, name: str, record_type: str) -> LookupResult:
        ...


class TlsChecker(Protocol):
    def __call__(self, hostname: str) -> Mapping[str, Any]:
        ...


@dataclass(frozen=True, order=True)
class DnsQuery:
    name: str
    record_type: str


class SnapshotResolver:
    """Read-only DNS backend used by the pure policy layer."""

    def __init__(self, snapshot: Mapping[tuple[str, str], LookupResult], *, cname_limit: int = 5) -> None:
        self._snapshot = snapshot
        self._cname_limit = cname_limit

    def resolve(self, name: str, record_type: str) -> LookupResult:
        normalized_name = normalize_dns_name(name)
        normalized_type = record_type.upper()
        direct = self._snapshot.get((normalized_name, normalized_type))
        if direct is None:
            return LookupResult(records=[], error_code="not_queried")
        if direct.records or normalized_type == "CNAME" or direct.error_code not in DNS_ABSENCE_CODES:
            return direct

        current = normalized_name
        fallback_used = direct.fallback_used
        resolver = direct.resolver
        for _ in range(self._cname_limit):
            cname = self._snapshot.get((current, "CNAME"))
            if cname is None:
                return direct
            fallback_used = fallback_used or cname.fallback_used
            resolver = cname.resolver or resolver
            if cname.error_code not in DNS_ABSENCE_CODES:
                return LookupResult(
                    records=[],
                    error_code=cname.error_code,
                    resolver=resolver,
                    fallback_used=fallback_used,
                )
            if not cname.records:
                return direct
            target = _safe_discovered_hostname(cname.records[0])
            if not target:
                return LookupResult(
                    records=[],
                    error_code="invalid_cname_target",
                    resolver=resolver,
                    fallback_used=fallback_used,
                )
            target_result = self._snapshot.get((target, normalized_type))
            if target_result is None:
                return LookupResult(
                    records=[],
                    error_code="not_queried",
                    resolver=resolver,
                    fallback_used=fallback_used,
                )
            fallback_used = fallback_used or target_result.fallback_used
            resolver = target_result.resolver or resolver
            if target_result.records or target_result.error_code not in DNS_ABSENCE_CODES:
                return LookupResult(
                    records=list(target_result.records),
                    error_code=target_result.error_code,
                    resolver=resolver,
                    fallback_used=fallback_used,
                )
            current = target
        return LookupResult(
            records=[],
            error_code="cname_limit_exceeded",
            resolver=resolver,
            fallback_used=fallback_used,
        )


def normalize_setup(payload: Mapping[str, Any], *, expected_org_id: str) -> dict[str, Any]:
    """Reduce an MCP response to validated, bounded facts used for query planning."""

    if not isinstance(payload, Mapping):
        raise SetupValidationError("setup must be an object")
    actual_org_id = _normalize_org_id(payload.get("orgId"))
    normalized_expected = _normalize_org_id(expected_org_id)
    if not actual_org_id or actual_org_id != normalized_expected:
        raise SetupValidationError("organization mismatch")

    raw_domains = payload.get("domains")
    if raw_domains is None:
        raw_domains = []
    if not isinstance(raw_domains, list):
        raise SetupValidationError("domains must be a list")

    domains: list[dict[str, Any]] = []
    for raw_domain in raw_domains[:128]:
        if not isinstance(raw_domain, Mapping):
            raise SetupValidationError("domain entry must be an object")
        domain = normalize_hostname(raw_domain.get("domain"))
        if not domain:
            raise SetupValidationError("domain entry contains an invalid domain")
        configuration = _as_mapping(raw_domain.get("configuration"))
        status_payload = _as_mapping(raw_domain.get("status")) or _as_mapping(configuration.get("status"))
        configuration_status = _safe_enum(
            status_payload.get("status")
            or raw_domain.get("configurationStatus")
            or configuration.get("status"),
            _CONFIGURATION_STATUSES,
        )
        verification_passed = _first_bool(
            raw_domain.get("verificationPassed"),
            configuration.get("verificationPassed"),
            status_payload.get("verified"),
        )
        technical_domains = _ordered_unique_hostnames(
            [
                raw_domain.get("subDomain"),
                raw_domain.get("technicalDomain"),
                configuration.get("subDomain"),
                configuration.get("technicalDomain"),
            ]
        )
        history = _normalize_verification_history(raw_domain.get("verificationHistory"))
        raw_errors = raw_domain.get("errors")
        error_count = len(raw_errors[:100]) if isinstance(raw_errors, list) else int(bool(raw_errors))
        warmup = raw_domain.get("warmupInfo")
        if warmup is None or warmup == "":
            warmup_state = "absent"
        elif isinstance(warmup, (list, dict)) and not warmup:
            warmup_state = "empty"
        else:
            warmup_state = "present"

        dkim_record_names = extract_dkim_record_names(domain, raw_domain)
        dkim_selector_source = "mcp"
        if not dkim_record_names:
            dkim_selector_source = "reteno-standard-fallback"
            dkim_record_names = [f"{RETENO_DEFAULT_DKIM_SELECTOR}._domainkey.{domain}"]

        domains.append(
            {
                "id": _safe_identifier(raw_domain.get("id")),
                "domain": domain,
                "technicalDomains": technical_domains,
                "configurationStatus": configuration_status,
                "verificationPassed": verification_passed,
                "verificationHistory": history,
                "errorCount": error_count,
                "warmupState": warmup_state,
                "dkimRecordNames": dkim_record_names,
                "dkimSelectorSource": dkim_selector_source,
            }
        )

    sender_payload = _as_mapping(payload.get("sender"))
    mailing = _as_mapping(sender_payload.get("mailingConfiguration"))
    configured_domains: list[dict[str, Any]] = []
    for item in _as_list(mailing.get("configuredSenderDomains"))[:128]:
        if not isinstance(item, Mapping):
            continue
        domain = normalize_hostname(item.get("domain"))
        if domain:
            configured_domains.append(
                {
                    "domain": domain,
                    "active": item.get("active") if isinstance(item.get("active"), bool) else None,
                    "verificationPassed": (
                        item.get("verificationPassed")
                        if isinstance(item.get("verificationPassed"), bool)
                        else None
                    ),
                }
            )

    sending_domains = _ordered_unique_hostnames(
        item.get("domain")
        for item in _as_list(sender_payload.get("sendingDomains"))[:128]
        if isinstance(item, Mapping)
    )
    interfaces_payload = sender_payload.get("publicInterface")
    if isinstance(interfaces_payload, Mapping) and isinstance(interfaces_payload.get("items"), list):
        interfaces_payload = interfaces_payload.get("items")
    interfaces: list[dict[str, Any]] = []
    for item in _as_list(interfaces_payload)[:512]:
        if not isinstance(item, Mapping):
            continue
        available = item.get("status") == "AVAILABLE" if isinstance(item.get("status"), str) else None
        for key in ("email", "responseEmail", "replyToEmail", "fromEmail"):
            raw_email = item.get(key)
            if not isinstance(raw_email, str):
                continue
            for match in _EMAIL_RE.finditer(raw_email[:320]):
                email = match.group(0).lower()
                domain = normalize_hostname(match.group(1))
                if domain:
                    interfaces.append({
                        "email": email,
                        "domain": domain,
                        "available": available,
                        "role": "sender" if key in {"email", "fromEmail"} else "reply_to",
                    })
    interfaces = _ordered_unique_mappings(interfaces, keys=("email", "domain", "available", "role"))

    short_links_payload = _as_mapping(payload.get("shortLinks"))
    short_link_domains: list[dict[str, Any]] = []
    for item in _as_list(short_links_payload.get("sslDomains"))[:128]:
        if not isinstance(item, Mapping):
            continue
        domain = normalize_hostname(item.get("domain"))
        if domain:
            short_link_domains.append(
                {
                    "domain": domain,
                    "active": item.get("active") if isinstance(item.get("active"), bool) else None,
                    "issued": item.get("status") == "ISSUED" if isinstance(item.get("status"), str) else None,
                }
            )

    return {
        "_normalized": True,
        "orgId": actual_org_id,
        "sourceGeneratedAt": _safe_timestamp(payload.get("generatedAt")),
        "domains": domains,
        "sender": {
            "mailingsBanned": mailing.get("mailingsBanned") if isinstance(mailing.get("mailingsBanned"), bool) else None,
            "configuredDomains": configured_domains,
            "sendingDomains": sending_domains,
            "interfaces": interfaces,
        },
        "shortLinks": {
            "inventoryAvailable": isinstance(short_links_payload.get("sslDomains"), list),
            "domains": short_link_domains,
            "enabled": _as_mapping(short_links_payload.get("settings")).get("enabled")
            if isinstance(_as_mapping(short_links_payload.get("settings")).get("enabled"), bool)
            else None,
        },
        "oneClickUnsubscribe": {
            "enabled": _as_mapping(payload.get("oneClickUnsubscribe")).get("enabled")
            if isinstance(_as_mapping(payload.get("oneClickUnsubscribe")).get("enabled"), bool)
            else None,
        },
    }


def build_query_plan(scope: Mapping[str, Any]) -> list[DnsQuery]:
    """Generate the complete initial DNS allowlist from normalized MCP scope."""

    if scope.get("_normalized") is not True:
        raise SetupValidationError("query planning requires normalized setup")
    queries: set[DnsQuery] = set()

    def add(name: str, record_type: str, *, follow_cname: bool = True) -> None:
        normalized = normalize_dns_name(name)
        queries.add(DnsQuery(normalized, record_type.upper()))
        if follow_cname and record_type.upper() != "CNAME":
            queries.add(DnsQuery(normalized, "CNAME"))

    for item in _as_list(scope.get("domains")):
        if not isinstance(item, Mapping):
            continue
        domain = normalize_hostname(item.get("domain"))
        if not domain:
            continue
        add(domain, "TXT")
        for policy_domain in _dmarc_tree_domains(domain):
            add(f"_dmarc.{policy_domain}", "TXT")
        add(f"default._bimi.{domain}", "TXT")
        add(f"_mta-sts.{domain}", "TXT")
        add(f"_smtp._tls.{domain}", "TXT")
        for record_name in _as_list(item.get("dkimRecordNames")):
            if isinstance(record_name, str):
                add(record_name, "TXT")
        for host in _as_list(item.get("technicalDomains")):
            if isinstance(host, str):
                add(host, "A")
                add(host, "AAAA")
                add(host, "MX")

    sender = _as_mapping(scope.get("sender"))
    sender_domains = [item.get("domain") for item in _as_list(sender.get("interfaces")) if isinstance(item, Mapping)]
    sender_domains.extend(sender.get("sendingDomains") or [])
    sender_domains.extend(
        item.get("domain") for item in _as_list(sender.get("configuredDomains")) if isinstance(item, Mapping)
    )
    for domain in _ordered_unique_hostnames(sender_domains):
        add(domain, "MX")

    for item in _as_list(_as_mapping(scope.get("shortLinks")).get("domains")):
        if not isinstance(item, Mapping):
            continue
        domain = normalize_hostname(item.get("domain"))
        if domain:
            add(domain, "A")
            add(domain, "AAAA")

    return sorted(queries)


def query_terminal_types(plan: Iterable[DnsQuery]) -> dict[str, set[str]]:
    terminal_types: dict[str, set[str]] = {}
    for query in plan:
        if query.record_type != "CNAME":
            terminal_types.setdefault(query.name, set()).add(query.record_type)
    return terminal_types


def audit_setup(
    payload: Mapping[str, Any],
    *,
    resolver: DnsResolver,
    tls_checker: TlsChecker,
    generated_at: str | None = None,
    expected_org_id: str | None = None,
) -> dict[str, Any]:
    """Apply deterministic policy to normalized MCP facts and network snapshots."""

    if payload.get("_normalized") is True:
        scope = dict(payload)
    else:
        expected = expected_org_id or _normalize_org_id(payload.get("orgId"))
        scope = normalize_setup(payload, expected_org_id=expected)
    generated_at = generated_at or utc_now_iso()

    checks: list[dict[str, Any]] = []
    domain_reports: list[dict[str, Any]] = []
    for item in _as_list(scope.get("domains")):
        if not isinstance(item, Mapping):
            continue
        domain = str(item["domain"])
        item_checks = [
            _check_domain_configuration(item),
            _check_domain_errors(item),
            _check_verification_history(item),
            _check_warmup_info(item),
            check_dmarc(domain, resolver),
            check_dkim(domain, item, resolver),
            check_bimi(domain, resolver),
            check_mta_sts(domain, resolver),
            check_tls_rpt(domain, resolver),
        ]
        technical_domains = list(item.get("technicalDomains") or [])
        item_checks.extend(
            check_host_resolution(host, resolver, purpose="technical-domain") for host in technical_domains
        )
        checks.extend(item_checks)
        domain_reports.append(
            {
                "id": item.get("id"),
                "domain": domain,
                "technicalDomains": technical_domains,
                "checks": item_checks,
            }
        )

    sender = _as_mapping(scope.get("sender"))
    sender_checks = check_sender_setup(sender, [item["domain"] for item in domain_reports])
    sender_domains = _ordered_unique_hostnames(
        item.get("domain") for item in _as_list(sender.get("interfaces")) if isinstance(item, Mapping)
    )
    sender_checks.extend(check_mx(domain, resolver) for domain in sender_domains)
    checks.extend(sender_checks)

    short_links = _as_mapping(scope.get("shortLinks"))
    short_link_checks = check_short_links(short_links)
    short_link_domains = [
        item["domain"] for item in _as_list(short_links.get("domains")) if isinstance(item, Mapping)
    ]
    for domain in short_link_domains:
        short_link_checks.append(check_host_resolution(domain, resolver, purpose="short-link-domain"))
        short_link_checks.append(check_short_link_tls(domain, tls_checker))
    checks.extend(short_link_checks)

    return {
        "orgId": scope.get("orgId"),
        "generatedAt": generated_at,
        "sourceGeneratedAt": scope.get("sourceGeneratedAt"),
        "summary": summarize_checks(checks),
        "domains": domain_reports,
        "sender": {
            "emails": [
                {"email": item["email"], "domain": item["domain"], "role": item.get("role", "sender")}
                for item in _as_list(sender.get("interfaces"))
                if isinstance(item, Mapping)
            ],
            "domains": sender_domains,
            "checks": sender_checks,
        },
        "shortLinks": {"domains": short_link_domains, "checks": short_link_checks,
                       "inventoryAvailable": short_links.get("inventoryAvailable"),
                       "inventory": list(short_links.get("domains") or [])},
        "oneClickUnsubscribe": dict(_as_mapping(scope.get("oneClickUnsubscribe"))),
        "checks": checks,
    }


def check_spf(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    lookup = resolver.resolve(domain, "TXT")
    if _is_inconclusive(lookup):
        return _inconclusive_check("spf", "SPF record", domain, lookup.error_code)
    records = [record for record in lookup.records if record.lower().startswith("v=spf1")]
    details: dict[str, Any] = {"recordCount": len(records)}
    if not records:
        return _check("spf", "SPF record", CHECK_FAIL, domain, "No SPF TXT record was found.", details=details)
    if len(records) > 1:
        return _check(
            "spf",
            "SPF record",
            CHECK_FAIL,
            domain,
            "Multiple SPF TXT records were found.",
            details=details,
            recommendation="Publish exactly one SPF record per domain.",
        )

    record = records[0]
    estimated_lookups = len(_SPF_LOOKUP_RE.findall(record)) + len(_SPF_REDIRECT_RE.findall(record))
    details["estimatedDnsLookups"] = estimated_lookups
    details["termination"] = _spf_termination(record)
    if estimated_lookups > 10:
        return _check(
            "spf.lookup_budget",
            "SPF DNS lookup budget",
            CHECK_FAIL,
            domain,
            "SPF appears to exceed the 10 DNS lookup limit.",
            details=details,
            recommendation="Flatten or simplify SPF includes so receivers do not hit permerror.",
        )
    if details["termination"] == "missing":
        return _check(
            "spf.termination",
            "SPF termination",
            CHECK_WARN,
            domain,
            "SPF does not contain an all mechanism or redirect modifier.",
            details=details,
        )
    return _check("spf", "SPF record", CHECK_PASS, domain, "SPF record exists and basic checks passed.", details=details)


def _dmarc_tree_domains(domain: str) -> list[str]:
    # RFC 9989 section 4.10: exact domain, then at most seven ancestor queries.
    labels = domain.split(".")
    tail = labels[-min(len(labels) - 1, 7):]
    return [domain, *(".".join(tail[index:]) for index in range(len(tail)))]


def check_dmarc(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    found: dict[str, dict[str, str]] = {}
    policy_domain = domain
    for candidate in _dmarc_tree_domains(domain):
        name = f"_dmarc.{candidate}"
        lookup = resolver.resolve(name, "TXT")
        if _is_inconclusive(lookup):
            return _inconclusive_check("dmarc", "DMARC record", domain, lookup.error_code, details={"name": name})
        records = [record for record in lookup.records if re.match(r"v\s*=\s*DMARC1(?:\s*;|\s*$)", record)]
        if len(records) > 1:
            return _inconclusive_check("dmarc", "DMARC record", domain, "multiple_dmarc_records", details={"name": name})
        if not records:
            continue
        tags = _parse_tag_record(records[0])
        found[candidate] = tags
        policy_domain = candidate
        if candidate == domain or tags.get("psd") == "n":
            break
        if tags.get("psd") == "y":
            # A PSD record applies only if the organization immediately below it
            # has no record. An unrelated deeper subdomain is not the fallback.
            organization = ".".join(domain.split(".")[-len(candidate.split(".")) - 1:])
            if organization in found:
                policy_domain = organization
            break
    if not found:
        return _check("dmarc", "DMARC record", CHECK_FAIL, domain, "No applicable DMARC TXT record was found.")

    tags = found[policy_domain]
    policy_tag = "p"
    if policy_domain != domain:
        policy_tag = "sp" if "sp" in tags else "p"
        if "np" in tags:
            existence = resolver.resolve(domain, "TXT")
            if _is_inconclusive(existence):
                return _inconclusive_check("dmarc", "DMARC record", domain, existence.error_code)
            if existence.error_code == "nxdomain":
                policy_tag = "np"
    policy = tags.get(policy_tag, "none").lower()
    details: dict[str, Any] = {
        "name": f"_dmarc.{policy_domain}",
        "recordCount": 1,
        "policyDomain": policy_domain,
        "inherited": policy_domain != domain,
        "policyTag": policy_tag,
    }
    percentage = _safe_percentage(tags.get("pct"))
    details.update(
        {
            "policy": policy if policy in {"none", "quarantine", "reject"} else None,
            "percentage": percentage,
            "aggregateReportingConfigured": bool(tags.get("rua")),
            "forensicReportingConfigured": bool(tags.get("ruf")),
        }
    )
    if policy not in {"none", "quarantine", "reject"}:
        return _check("dmarc.policy", "DMARC policy", CHECK_FAIL, domain, "DMARC policy is missing or invalid.", details=details)
    if policy == "none":
        return _check(
            "dmarc.policy",
            "DMARC policy",
            CHECK_FAIL,
            domain,
            f"DMARC is set to monitoring-only policy {policy_tag}=none.",
            details=details,
            recommendation="Move toward quarantine or reject after validating alignment and reports.",
        )
    if tags.get("t", "n").lower() == "y":
        return _check("dmarc.testing", "DMARC testing mode", CHECK_FAIL, domain,
                      "DMARC t=y disables policy enforcement; the customer checklist requires enforcement.", details=details)
    if percentage is not None and percentage < 100:
        return _check(
            "dmarc.percentage",
            "DMARC policy percentage",
            CHECK_WARN,
            domain,
            f"DMARC enforcement applies to {percentage}% of failing messages.",
            details=details,
            recommendation="Increase pct toward 100 after confirming legitimate mail remains aligned.",
        )
    return _check("dmarc", "DMARC record", CHECK_PASS, domain, f"DMARC policy is {policy_tag}={policy} at {policy_domain}.", details=details)


def check_dkim(domain: str, domain_payload: Mapping[str, Any], resolver: DnsResolver) -> dict[str, Any]:
    record_names = [str(value) for value in _as_list(domain_payload.get("dkimRecordNames")) if isinstance(value, str)]
    selector_source = str(domain_payload.get("dkimSelectorSource") or "mcp")
    retired = set(domain_payload.get("dkimRetiredRecordNames") or [])
    record_names = [name for name in record_names if name not in retired]
    if not record_names and retired:
        return _check(
            "dkim", "DKIM record", CHECK_UNAVAILABLE, domain,
            "All known DKIM selectors are retired; an active selector reference is required.",
            details={"selectorSource": selector_source, "selectors": [], "retiredSelectors": sorted(retired)},
        )
    if not record_names:
        selector_source = "reteno-standard-fallback"
        record_names = [f"{RETENO_DEFAULT_DKIM_SELECTOR}._domainkey.{domain}"]

    selectors: list[dict[str, Any]] = []
    for name in record_names:
        txt = resolver.resolve(name, "TXT")
        cname = resolver.resolve(name, "CNAME")
        terminal = txt
        cname_targets = sorted(
            {target for value in cname.records if (target := _safe_discovered_hostname(value))}
        )
        if not terminal.records and cname_targets and not _is_inconclusive(cname):
            terminal = resolver.resolve(cname_targets[0], "TXT")

        states = [_dkim_public_key_state(record) for record in terminal.records]
        states = [state for state in states if state is not None]
        if "active" in states:
            key_state = "active"
        elif "revoked" in states:
            key_state = "revoked"
        elif terminal.records or (cname_targets and terminal.error_code in DNS_ABSENCE_CODES):
            key_state = "invalid"
        elif _is_inconclusive(terminal) or _is_inconclusive(txt) or _is_inconclusive(cname):
            key_state = "inconclusive"
        else:
            key_state = "missing"
        if key_state not in DKIM_KEY_STATES:
            key_state = "invalid"
        selectors.append(
            {
                "selector": name.split("._domainkey.", 1)[0],
                "recordName": name,
                "keyState": key_state,
                "cnameTargets": cname_targets[:5],
            }
        )

    details = {"selectorSource": selector_source, "selectors": selectors}
    states = {item["keyState"] for item in selectors}
    if states & {"revoked", "invalid"}:
        return _check(
            "dkim",
            "DKIM record",
            CHECK_FAIL,
            domain,
            "One or more DKIM selectors do not resolve to an active public key.",
            details=details,
            recommendation="Publish the DKIM CNAME or TXT value provided by Reteno and ensure the public key is active.",
        )
    if "inconclusive" in states:
        status = CHECK_UNAVAILABLE
        return _check(
            "dkim",
            "DKIM record",
            status,
            domain,
            "DKIM could not be verified because one or more DNS lookups were inconclusive.",
            details=details,
        )
    if "missing" in states:
        if selector_source == "reteno-standard-fallback":
            return _check(
                "dkim",
                "DKIM record",
                CHECK_UNAVAILABLE,
                domain,
                "MCP did not expose DKIM selector data and the Reteno standard selector was not found.",
                details=details,
                recommendation="Inspect a delivered message's DKIM-Signature header or provide the selector shown in Reteno domain settings.",
            )
        return _check("dkim", "DKIM record", CHECK_FAIL, domain, "One or more DKIM records were not found.", details=details)
    message = (
        "Reteno standard DKIM selector resolves to an active public key."
        if selector_source == "reteno-standard-fallback"
        else "DKIM selector records resolve to active public keys."
    )
    return _check("dkim", "DKIM record", CHECK_PASS, domain, message, details=details)


def check_mx(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    lookup = resolver.resolve(domain, "MX")
    if _is_inconclusive(lookup):
        return _inconclusive_check("mx", "MX records", domain, lookup.error_code)
    hosts: list[dict[str, Any]] = []
    for record in lookup.records:
        preference_text, _, host_text = record.partition(" ")
        host = normalize_hostname(host_text or preference_text)
        if not host:
            continue
        try:
            preference = int(preference_text) if host_text else None
        except ValueError:
            preference = None
        hosts.append({"hostname": host, "preference": preference})
    hosts.sort(key=lambda item: (item["preference"] is None, item["preference"] or 0, item["hostname"]))
    details = {"recordCount": len(hosts), "hosts": hosts[:32]}
    if not hosts:
        return _check("mx", "MX records", CHECK_WARN, domain, "No MX records were found for this sender/reply domain.", details=details)
    return _check("mx", "MX records", CHECK_PASS, domain, "MX records were found.", details=details)


def check_host_resolution(hostname: str, resolver: DnsResolver, *, purpose: str) -> dict[str, Any]:
    cname = resolver.resolve(hostname, "CNAME")
    ipv4 = resolver.resolve(hostname, "A")
    ipv6 = resolver.resolve(hostname, "AAAA")
    addresses = list(ipv4.records) + list(ipv6.records)
    public_ips: list[str] = []
    blocked_count = 0
    for value in addresses:
        try:
            address = ipaddress.ip_address(value)
        except ValueError:
            blocked_count += 1
            continue
        if _is_public_ip(address):
            public_ips.append(str(address))
        else:
            blocked_count += 1
    public_ips = sorted(
        set(public_ips),
        key=lambda value: (ipaddress.ip_address(value).version, int(ipaddress.ip_address(value))),
    )
    cname_targets = sorted(
        {target for value in cname.records if (target := _safe_discovered_hostname(value))}
    )
    details = {
        "publicIps": public_ips,
        "cnameTargets": cname_targets[:5],
        "blockedAddressCount": blocked_count,
    }
    if blocked_count:
        return _check(purpose, "Host resolution", CHECK_FAIL, hostname, "Host resolves to a non-public address.", details=details)
    if public_ips:
        return _check(purpose, "Host resolution", CHECK_PASS, hostname, "Host resolves publicly.", details=details)
    if purpose == "technical-domain":
        mx = check_mx(hostname, resolver)
        if mx["status"] == CHECK_PASS:
            details["mxHosts"] = mx["details"]["hosts"]
            return _check(purpose, "Host resolution", CHECK_PASS, hostname, "Mail domain publishes MX records; address records on the domain itself are not required.", details=details)
        if mx["status"] == CHECK_UNAVAILABLE and not cname_targets:
            return _inconclusive_check(purpose, "Host resolution", hostname, mx["details"].get("reason"))
    errors = [result.error_code for result in (cname, ipv4, ipv6) if _is_inconclusive(result)]
    if errors:
        details["incomplete"] = True
        details["reason"] = _safe_error_code(errors[0])
        return _check(purpose, "Host resolution", CHECK_UNAVAILABLE, hostname, "Host resolution was inconclusive.", details=details)
    if cname_targets:
        return _check(purpose, "Host resolution", CHECK_PASS, hostname, "Host has a public CNAME record.", details=details)
    return _check(purpose, "Host resolution", CHECK_FAIL, hostname, "Host does not resolve publicly.", details=details)


def check_short_link_tls(hostname: str, tls_checker: TlsChecker) -> dict[str, Any]:
    result = dict(tls_checker(hostname))
    state = result.get("state") if result.get("state") in {"valid", "invalid", "inconclusive"} else "inconclusive"
    safe_details: dict[str, Any] = {"state": state}
    if result.get("protocol") in {"TLSv1.2", "TLSv1.3"}:
        safe_details["protocol"] = result["protocol"]
    if expires_at := _safe_timestamp(result.get("expiresAt")):
        safe_details["expiresAt"] = expires_at
    public_ip_count = result.get("publicIpCount")
    if isinstance(public_ip_count, int) and not isinstance(public_ip_count, bool):
        safe_details["publicIpCount"] = max(0, min(64, public_ip_count))
    if "reason" in result:
        safe_details["reason"] = _safe_tls_reason(result.get("reason"))
    if state == "valid":
        return _check("short_link.tls", "Short-link HTTPS/TLS", CHECK_PASS, hostname, "HTTPS certificate is valid.", details=safe_details)
    if state == "invalid":
        return _check("short_link.tls", "Short-link HTTPS/TLS", CHECK_FAIL, hostname, "HTTPS/TLS validation failed.", details=safe_details)
    return _check("short_link.tls", "Short-link HTTPS/TLS", CHECK_UNAVAILABLE, hostname, "HTTPS/TLS validation was inconclusive.", details=safe_details)


def check_bimi(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    return _optional_txt_check("bimi", "BIMI record", f"default._bimi.{domain}", domain, resolver)


def check_mta_sts(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    return _optional_txt_check("mta_sts", "MTA-STS record", f"_mta-sts.{domain}", domain, resolver)


def check_tls_rpt(domain: str, resolver: DnsResolver) -> dict[str, Any]:
    return _optional_txt_check("tls_rpt", "TLS-RPT record", f"_smtp._tls.{domain}", domain, resolver)


def check_sender_setup(sender: Mapping[str, Any], verified_domains: list[str]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    mailings_banned = sender.get("mailingsBanned")
    if mailings_banned is True:
        checks.append(_check("sender.mailings_banned", "Mailings status", CHECK_FAIL, "sender", "Mailings are banned."))
    elif mailings_banned is False:
        checks.append(_check("sender.mailings_banned", "Mailings status", CHECK_PASS, "sender", "Mailings are not banned."))
    else:
        checks.append(_check("sender.mailings_banned", "Mailings status", CHECK_SKIPPED, "sender", "Mailing configuration is absent."))

    configured = [item for item in _as_list(sender.get("configuredDomains")) if isinstance(item, Mapping)]
    inactive = [item["domain"] for item in configured if item.get("active") is False]
    failed = [item["domain"] for item in configured if item.get("verificationPassed") is False]
    if inactive or failed:
        checks.append(
            _check(
                "sender.configured_domains",
                "Configured sender domains",
                CHECK_WARN,
                "sender",
                "Some configured sender domains are inactive or not verified.",
                details={"inactive": inactive, "failed": failed},
            )
        )
    elif configured:
        checks.append(_check("sender.configured_domains", "Configured sender domains", CHECK_PASS, "sender", "Configured sender domains are active and verified."))
    else:
        checks.append(_check("sender.configured_domains", "Configured sender domains", CHECK_SKIPPED, "sender", "No configured sender domain list was provided."))

    interfaces = [item for item in _as_list(sender.get("interfaces")) if isinstance(item, Mapping)]
    unavailable_count = sum(item.get("available") is False for item in interfaces)
    if unavailable_count:
        checks.append(
            _check(
                "sender.public_interface",
                "Sender interfaces",
                CHECK_FAIL,
                "sender",
                "One or more sender interfaces are unavailable.",
                details={"interfaceCount": len(interfaces), "unavailableCount": unavailable_count},
            )
        )
    elif interfaces:
        checks.append(_check("sender.public_interface", "Sender interfaces", CHECK_PASS, "sender", "Sender interfaces are available.", details={"interfaceCount": len(interfaces), "unavailableCount": 0}))
    else:
        checks.append(_check("sender.public_interface", "Sender interfaces", CHECK_SKIPPED, "sender", "No sender interfaces were provided."))

    sender_domains = _ordered_unique_hostnames(
        item.get("domain") for item in interfaces if item.get("role", "sender") == "sender"
    )
    allowed_domains = set(verified_domains)
    allowed_domains.update(item["domain"] for item in configured)
    allowed_domains.update(_ordered_unique_hostnames(sender.get("sendingDomains") or []))
    unaligned = [domain for domain in sender_domains if domain not in allowed_domains]
    if unaligned:
        checks.append(
            _check(
                "sender.domain_alignment",
                "Sender domain alignment",
                CHECK_FAIL,
                "sender",
                "Some sender emails use domains that are not verified/sending domains.",
                details={"senderDomains": sender_domains, "verifiedDomains": sorted(allowed_domains), "unaligned": unaligned},
            )
        )
    elif sender_domains:
        checks.append(_check("sender.domain_alignment", "Sender domain alignment", CHECK_PASS, "sender", "Sender email domains align with configured domains."))
    else:
        checks.append(_check("sender.domain_alignment", "Sender domain alignment", CHECK_SKIPPED, "sender", "No sender emails were provided."))
    return checks


def check_short_links(short_links: Mapping[str, Any]) -> list[dict[str, Any]]:
    if short_links.get("inventoryAvailable") is False:
        return [_check("short_link.custom_domain", "Required custom link domain", CHECK_UNAVAILABLE,
                       "short-links", "Custom link-domain inventory was not supplied by MCP.")]
    domains = [item for item in _as_list(short_links.get("domains")) if isinstance(item, Mapping)]
    customer = [item for item in domains if not any(
        item["domain"] == shared or item["domain"].endswith("." + shared)
        for shared in ("esputnik.com", "reteno.com", "yespo.io"))]
    if not customer:
        return [_check("short_link.custom_domain", "Required custom link domain", CHECK_FAIL,
                       "short-links", "No customer-controlled custom link domain is configured.")]
    active = [item for item in customer if item.get("active") is True and item.get("issued") is True]
    status = CHECK_PASS if active else CHECK_UNAVAILABLE if any(
        item.get("active") is None or item.get("issued") is None for item in customer) else CHECK_FAIL
    return [_check("short_link.ssl_status", "Custom link domain activation", status, "short-links",
                   "An active issued custom link domain is present." if active else
                   "Custom link domain activation and certificate issuance are not confirmed.",
                   details={"activeDomains": [item["domain"] for item in active]}),
            _check("short_link.settings", "UTM settings", CHECK_INFO, "short-links",
                   "The settings.enabled flag controls UTM tagging, not custom-domain activation.")]


def summarize_checks(checks: list[dict[str, Any]]) -> dict[str, Any]:
    counts = {CHECK_PASS: 0, CHECK_WARN: 0, CHECK_FAIL: 0, CHECK_INFO: 0, CHECK_SKIPPED: 0, CHECK_UNAVAILABLE: 0}
    for check in checks:
        status = check.get("status")
        if status in counts:
            counts[status] += 1
    overall = (CHECK_FAIL if counts[CHECK_FAIL] else CHECK_UNAVAILABLE if counts[CHECK_UNAVAILABLE]
               else CHECK_WARN if counts[CHECK_WARN] else CHECK_PASS if counts[CHECK_PASS] else CHECK_UNAVAILABLE)
    return {
        "overallStatus": overall,
        "complete": counts[CHECK_UNAVAILABLE] == 0,
        "unavailable": counts[CHECK_UNAVAILABLE],
        "pass": counts[CHECK_PASS],
        "warn": counts[CHECK_WARN],
        "fail": counts[CHECK_FAIL],
        "info": counts[CHECK_INFO],
        "skipped": counts[CHECK_SKIPPED],
        "total": sum(counts.values()),
    }


def render_markdown(report: Mapping[str, Any]) -> str:
    summary = _as_mapping(report.get("summary"))
    lines = [
        "# Email Deliverability Technical Setup Audit",
        "",
        f"- Organization: `{report.get('orgId')}`",
        f"- Generated: `{report.get('generatedAt')}`",
        f"- Overall: **{summary.get('overallStatus', 'unknown')}**",
        (
            f"- Checks: {summary.get('pass', 0)} pass, {summary.get('warn', 0)} warn, "
            f"{summary.get('fail', 0)} fail, {summary.get('unavailable', 0)} unavailable, {summary.get('skipped', 0)} not applicable"
        ),
        "",
        "## Priority Findings",
        "",
    ]
    issues = [
        check
        for check in _as_list(report.get("checks"))
        if isinstance(check, Mapping) and check.get("status") in {CHECK_FAIL, CHECK_WARN, CHECK_UNAVAILABLE}
    ]
    if issues:
        for check in issues:
            lines.append(f"- **{str(check['status']).upper()}** `{check['subject']}` {check['title']}: {check['message']}")
    else:
        lines.append("- No failing or warning checks found.")
    lines.extend(["", "## Domains", ""])
    domains = [item for item in _as_list(report.get("domains")) if isinstance(item, Mapping)]
    for item in domains:
        statuses = summarize_checks(list(item.get("checks") or []))
        lines.append(
            f"- `{item['domain']}`: {statuses['pass']} pass, {statuses['warn']} warn, "
            f"{statuses['fail']} fail, {statuses['skipped']} skipped"
        )
    if not domains:
        lines.append("- No domains were returned by MCP.")
    sender = _as_mapping(report.get("sender"))
    short_links = _as_mapping(report.get("shortLinks"))
    lines.extend(
        [
            "",
            "## Sender And Links",
            "",
            f"- Sender domains: {', '.join(f'`{domain}`' for domain in sender.get('domains', [])) or 'none'}",
            f"- Short-link domains: {', '.join(f'`{domain}`' for domain in short_links.get('domains', [])) or 'none'}",
            "",
        ]
    )
    return "\n".join(lines)


def extract_dkim_record_names(domain: str, payload: Any) -> list[str]:
    names: list[str] = []
    selectors: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, Mapping):
            if str(value.get("lifecycle", "")).lower() == "retired":
                return
            for key, child in value.items():
                lowered = str(key).lower()
                if lowered in {"selector", "dkimselector"} and isinstance(child, str):
                    selectors.append(child)
                elif lowered in {"selectors", "dkimselectors"} and isinstance(child, list):
                    selectors.extend(item for item in child if isinstance(item, str))
                elif isinstance(child, str) and "_domainkey" in child.lower():
                    names.append(child)
                walk(child)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(payload)
    normalized: list[str] = []
    suffix = f"._domainkey.{domain}"
    for value in names:
        candidate = value.strip().strip(".").lower()
        if candidate.endswith(suffix) and _SELECTOR_RE.fullmatch(candidate[: -len(suffix)]):
            normalized.append(candidate)
        elif candidate.endswith("._domainkey") and _SELECTOR_RE.fullmatch(candidate[: -len("._domainkey")]):
            normalized.append(f"{candidate}.{domain}")
    for value in selectors:
        selector = value.strip().strip(".")
        candidate = selector.lower()
        if candidate.endswith(suffix) and _SELECTOR_RE.fullmatch(candidate[: -len(suffix)]):
            normalized.append(candidate)
        elif candidate.endswith("._domainkey") and _SELECTOR_RE.fullmatch(candidate[: -len("._domainkey")]):
            normalized.append(f"{candidate}.{domain}")
        elif _SELECTOR_RE.fullmatch(selector):
            normalized.append(f"{selector.lower()}._domainkey.{domain}")
    return _ordered_unique(normalized)


def normalize_hostname(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    raw = value.strip().strip(".").lower()
    if not raw or len(raw) > 253:
        return ""
    try:
        ipaddress.ip_address(raw)
    except ValueError:
        pass
    else:
        return ""
    try:
        host = raw.encode("idna").decode("ascii").lower()
    except UnicodeError:
        return ""
    if host in _BLOCKED_HOSTNAMES or any(host.endswith(suffix) for suffix in _BLOCKED_HOST_SUFFIXES):
        return ""
    labels = host.split(".")
    if len(labels) < 2 or any(not _HOST_LABEL_RE.fullmatch(label) for label in labels):
        return ""
    return host


def normalize_dns_name(value: Any) -> str:
    if not isinstance(value, str):
        raise SetupValidationError("DNS name must be a string")
    raw = value.strip().strip(".").lower()
    if not raw or len(raw) > 253:
        raise SetupValidationError("DNS name is invalid")
    labels = raw.split(".")
    if len(labels) < 2 or any(not _DNS_LABEL_RE.fullmatch(label) for label in labels):
        raise SetupValidationError("DNS name is invalid")
    return raw


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _check_domain_configuration(item: Mapping[str, Any]) -> dict[str, Any]:
    status = item.get("configurationStatus")
    verified = item.get("verificationPassed")
    details = {"status": status, "verificationPassed": verified}
    if status in {"CONFIGURED", "VERIFIED"} or verified is True:
        return _check("mcp.domain_configuration", "Domain configuration", CHECK_PASS, item["domain"], "Reteno domain configuration is verified/configured.", details=details)
    if status is None and verified is None:
        return _check("mcp.domain_configuration", "Domain configuration", CHECK_SKIPPED, item["domain"], "No domain configuration status was provided by MCP.")
    return _check("mcp.domain_configuration", "Domain configuration", CHECK_WARN, item["domain"], "Reteno domain configuration is not clearly verified.", details=details)


def _check_domain_errors(item: Mapping[str, Any]) -> dict[str, Any]:
    count = int(item.get("errorCount") or 0)
    if count:
        return _check("mcp.domain_errors", "Domain MCP errors", CHECK_FAIL, item["domain"], "MCP reported configuration errors for this domain.", details={"errorCount": count})
    return _check("mcp.domain_errors", "Domain MCP errors", CHECK_PASS, item["domain"], "MCP returned no domain errors.")


def _check_verification_history(item: Mapping[str, Any]) -> dict[str, Any]:
    history = [value for value in _as_list(item.get("verificationHistory")) if isinstance(value, bool)]
    if not history:
        return _check("mcp.verification_history", "Verification history", CHECK_SKIPPED, item["domain"], "No verification history was provided.")
    details = {"latestVerified": history[0], "recentVerifiedValues": history[:8]}
    if history[0] is False:
        return _check("mcp.verification_history", "Verification history", CHECK_FAIL, item["domain"], "Latest verification history entry is failed.", details=details)
    if True in history and False in history:
        return _check("mcp.verification_history", "Verification history", CHECK_WARN, item["domain"], "Recent verification history contains both pass and fail states.", details=details)
    return _check("mcp.verification_history", "Verification history", CHECK_PASS, item["domain"], "Recent verification history is stable.", details=details)


def _check_warmup_info(item: Mapping[str, Any]) -> dict[str, Any]:
    state = item.get("warmupState")
    if state == "absent":
        return _check("mcp.warmup_info", "Warmup info", CHECK_SKIPPED, item["domain"], "No warmup info was provided.")
    if state == "empty":
        return _check("mcp.warmup_info", "Warmup info", CHECK_INFO, item["domain"], "Warmup info is empty.")
    return _check("mcp.warmup_info", "Warmup info", CHECK_INFO, item["domain"], "Warmup info was returned by MCP.")


def _optional_txt_check(check_id: str, title: str, name: str, domain: str, resolver: DnsResolver) -> dict[str, Any]:
    lookup = resolver.resolve(name, "TXT")
    if _is_inconclusive(lookup):
        return _inconclusive_check(check_id, title, domain, lookup.error_code, details={"name": name})
    details = {"name": name, "recordCount": len(lookup.records)}
    if lookup.records:
        return _check(check_id, title, CHECK_INFO, domain, f"{title} was found.", details=details)
    return _check(check_id, title, CHECK_SKIPPED, domain, f"{title} was not found.", details=details)


def _inconclusive_check(
    check_id: str,
    title: str,
    subject: str,
    reason: str | None,
    *,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    safe_details = dict(details or {})
    safe_details.update({"incomplete": True, "reason": _safe_error_code(reason)})
    return _check(check_id, title, CHECK_UNAVAILABLE, subject, f"{title} could not be verified because the network check was inconclusive.", details=safe_details)


def _check(
    check_id: str,
    title: str,
    status: str,
    subject: str,
    message: str,
    *,
    details: dict[str, Any] | None = None,
    recommendation: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"id": check_id, "title": title, "status": status, "subject": subject, "message": message}
    if recommendation:
        result["recommendation"] = recommendation
    if details:
        result["details"] = details
    return result


def _normalize_verification_history(value: Any) -> list[bool]:
    if isinstance(value, Mapping):
        value = value.get("items", [value])
    result: list[bool] = []
    for item in _as_list(value)[:8]:
        if isinstance(item, Mapping) and isinstance(item.get("verified"), bool):
            result.append(item["verified"])
    return result


def _parse_tag_record(record: str) -> dict[str, str]:
    tags: dict[str, str] = {}
    for part in record[:8192].split(";"):
        key, separator, value = part.strip().partition("=")
        if separator:
            tags[key.strip().lower()[:32]] = value.strip()[:2048]
    return tags


def _dkim_public_key_state(record: str) -> str | None:
    tags = _parse_tag_record(record)
    if "p" not in tags:
        return None
    if tags.get("v", "DKIM1").upper() != "DKIM1":
        return "invalid"
    return "active" if tags["p"] else "revoked"


def _spf_termination(record: str) -> str:
    lowered = record.lower()
    if "-all" in lowered:
        return "hardfail"
    if "~all" in lowered:
        return "softfail"
    if "?all" in lowered or "+all" in lowered:
        return "neutral"
    if "redirect=" in lowered:
        return "redirect"
    return "missing"


def _safe_percentage(value: Any) -> int | None:
    if value in (None, ""):
        return 100
    try:
        parsed = int(str(value))
    except ValueError:
        return None
    return parsed if 0 <= parsed <= 100 else None


def _safe_discovered_hostname(value: Any) -> str:
    return normalize_hostname(value)


def _is_inconclusive(result: LookupResult) -> bool:
    return result.error_code not in DNS_ABSENCE_CODES


def _safe_error_code(value: str | None) -> str:
    allowed = {
        "transport_error",
        "timeout",
        "servfail",
        "refused",
        "query_budget_exceeded",
        "cname_limit_exceeded",
        "invalid_cname_target",
        "overall_deadline_exceeded",
        "not_queried",
        "multiple_dmarc_records",
    }
    return value if value in allowed else "transport_error"


def _safe_tls_reason(value: Any) -> str:
    allowed = {
        "transport_error",
        "timeout",
        "servfail",
        "refused",
        "query_budget_exceeded",
        "cname_limit_exceeded",
        "invalid_cname_target",
        "overall_deadline_exceeded",
        "not_queried",
        "not_checked",
        "no_public_address",
        "non_global_address",
        "certificate_validation_failed",
    }
    normalized = str(value)
    return normalized if normalized in allowed else "transport_error"


def _safe_enum(value: Any, allowed: set[str]) -> str | None:
    if isinstance(value, Mapping):
        value = value.get("status")
    if not isinstance(value, str):
        return None
    normalized = value.strip().upper()
    return normalized if normalized in allowed else "UNKNOWN"


def _safe_identifier(value: Any) -> int | str | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,128}", value):
        return value
    return None


def _safe_timestamp(value: Any) -> str | None:
    if not isinstance(value, str) or len(value) > 64:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC).isoformat().replace("+00:00", "Z")


def _normalize_org_id(value: Any) -> str:
    text = str(value).strip() if value is not None else ""
    return text if re.fullmatch(r"[A-Za-z0-9_-]{1,128}", text) else ""


def _first_bool(*values: Any) -> bool | None:
    return next((value for value in values if isinstance(value, bool)), None)


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value is None:
        return []
    return [value]


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _ordered_unique_hostnames(values: Iterable[Any]) -> list[str]:
    return _ordered_unique(host for value in values if (host := normalize_hostname(value)))


def _ordered_unique_mappings(values: Iterable[dict[str, Any]], *, keys: tuple[str, ...]) -> list[dict[str, Any]]:
    seen: set[tuple[Any, ...]] = set()
    result: list[dict[str, Any]] = []
    for value in values:
        identity = tuple(value.get(key) for key in keys)
        if identity not in seen:
            seen.add(identity)
            result.append(value)
    return result


def _is_public_ip(value: ipaddress.IPv4Address | ipaddress.IPv6Address) -> bool:
    return (
        value.is_global
        and not value.is_loopback
        and not value.is_link_local
        and not value.is_multicast
        and not value.is_private
        and not value.is_reserved
        and not value.is_unspecified
    )
