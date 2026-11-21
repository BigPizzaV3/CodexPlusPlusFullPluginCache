"""Bounded SPF evaluation for explicitly identified envelope domains and sending IPs.

RFC 7208 order, qualifiers, include/redirect and DNS budgets are significant. Unsupported
macros/PTR produce unavailable evidence, never an invented authorization verdict.
"""
from __future__ import annotations

import ipaddress
import re


class SpfError(ValueError):
    pass


class SpfUnavailable(ValueError):
    pass


class Evaluator:
    def __init__(self, resolver):
        self.resolver = resolver
        self.lookups = 0
        self.voids = 0

    def lookup_term(self):
        self.lookups += 1
        if self.lookups > 10:
            raise SpfError("SPF evaluation exceeded ten DNS-lookup terms")

    def query(self, name, kind, *, count_void=True):
        response = self.resolver.resolve(name, kind)
        if response.error_code not in {None, "no_answer", "nxdomain"}:
            raise SpfUnavailable(f"DNS evidence unavailable ({response.error_code})")
        if not response.records and count_void:
            self.voids += 1
            if self.voids > 2:
                raise SpfError("SPF evaluation exceeded two void lookups")
        return response.records

    def record(self, domain):
        records = [x for x in self.query(domain, "TXT", count_void=False)
                   if re.match(r"(?i)^v=spf1(?:\s|$)", x)]
        if len(records) != 1:
            raise SpfError("Exactly one SPF TXT record is required on the envelope domain")
        terms = records[0].split()[1:]
        modifiers = {}
        for term in terms:
            if "=" in term:
                key, value = term.split("=", 1)
                if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", key) or not value:
                    raise SpfError("Invalid SPF modifier")
                key = key.lower()
                if key in modifiers:
                    raise SpfError("Duplicate SPF modifier")
                modifiers[key] = value
                continue
            body = term.lstrip("+-~?")
            if len(term) - len(body) > 1:
                raise SpfError("Invalid SPF qualifier")
            mechanism = re.split(r"[:/]", body, 1)[0].lower()
            if mechanism not in {"all", "include", "a", "mx", "ptr", "ip4", "ip6", "exists"}:
                raise SpfError("Unknown SPF mechanism")
            if mechanism == "all" and body.lower() != "all":
                raise SpfError("Invalid all mechanism")
            if mechanism in {"include", "exists"} and (":" not in body or not body.split(":", 1)[1]):
                raise SpfError("Missing SPF domain-spec")
            if mechanism in {"ip4", "ip6"}:
                try:
                    network = ipaddress.ip_network(body.split(":", 1)[1], strict=False)
                    if network.version != int(mechanism[-1]):
                        raise ValueError()
                except (ValueError, IndexError):
                    raise SpfError("Invalid SPF IP network") from None
            if mechanism in {"a", "mx"} and not re.fullmatch(r"(?i)(a|mx)(?::[^/]+)?(?:/\d+)?(?://\d+)?", body):
                raise SpfError("Invalid SPF address mechanism")
        return terms, modifiers

    def evaluate(self, domain, ip, stack=()):
        domain = domain.lower().rstrip(".")
        if domain in stack or len(stack) >= 11:
            raise SpfError("SPF recursive include/redirect loop")
        if "%" in domain:
            raise SpfUnavailable("SPF macro expansion needs complete SMTP identity evidence")
        terms, modifiers = self.record(domain)
        for term in terms:
            if "=" in term:
                continue
            qualifier = term[0] if term[0] in "+-~?" else "+"
            body = term[1:] if term[0] in "+-~?" else term
            mechanism = re.split(r"[:/]", body, 1)[0].lower()
            if "%" in body:
                raise SpfUnavailable("SPF macro expansion needs complete SMTP identity evidence")
            matches = False
            if mechanism == "all":
                matches = True
            elif mechanism in {"ip4", "ip6"}:
                matches = ip in ipaddress.ip_network(body.split(":", 1)[1], strict=False)
            else:
                self.lookup_term()
                if mechanism == "include":
                    result = self.evaluate(body.split(":", 1)[1], ip, (*stack, domain))
                    matches = result == "pass"
                elif mechanism == "exists":
                    matches = bool(self.query(body.split(":", 1)[1], "A"))
                elif mechanism == "ptr":
                    raise SpfUnavailable("PTR mechanism requires additional SMTP identity evidence")
                else:
                    match = re.fullmatch(r"(?i)(a|mx)(?::([^/]+))?(?:/(\d+))?(?://(\d+))?", body)
                    if not match:
                        raise SpfError("Invalid SPF address mechanism")
                    host = match[2] or domain
                    v4, v6 = int(match[3] or 32), int(match[4] or 128)
                    if v4 > 32 or v6 > 128:
                        raise SpfError("Invalid SPF address prefix")
                    hosts = [host]
                    if mechanism == "mx":
                        mx = self.query(host, "MX")
                        if len(mx) > 10:
                            raise SpfError("SPF MX mechanism exceeded ten records")
                        hosts = [record.split()[-1].rstrip(".") for record in mx]
                    for hostname in hosts:
                        addresses = self.query(hostname, "A" if ip.version == 4 else "AAAA")
                        if len(addresses) > 10 and mechanism == "mx":
                            raise SpfError("SPF MX host exceeded ten address records")
                        for address in addresses:
                            try:
                                matches |= ip in ipaddress.ip_network(f"{address}/{v4 if ip.version == 4 else v6}", strict=False)
                            except ValueError:
                                raise SpfUnavailable("Invalid DNS address evidence") from None
                        if matches:
                            break
            if matches:
                return {"+": "pass", "-": "fail", "~": "softfail", "?": "neutral"}[qualifier]
        if "redirect" in modifiers:
            self.lookup_term()
            return self.evaluate(modifiers["redirect"], ip, (*stack, domain))
        return "neutral"


def check_authorization(domain, ips, resolver, expected_include=None):
    from audit_engine import _check

    try:
        parsed = [ipaddress.ip_address(ip) for ip in ips]
        if not parsed or any(not ip.is_global for ip in parsed):
            raise SpfUnavailable("Actual public Reteno sending IPs were not supplied")
        inspector = Evaluator(resolver)
        terms, modifiers = inspector.record(domain)
        before_all = []
        termination = None
        for term in terms:
            before_all.append(term)
            if term.lstrip("+-~?").lower() == "all":
                termination = term.lower()
                break
        if termination not in {"~all", "-all"} and "redirect" not in modifiers:
            raise SpfError("SPF requires a ~all/-all fallback or redirect")
        if termination is not None and termination not in {"~all", "-all"}:
            raise SpfError("SPF all mechanism grants excessive or neutral authorization")
        if expected_include and not any(term.lower() in {
            f"include:{expected_include.lower()}", f"+include:{expected_include.lower()}"
        } for term in before_all):
            raise SpfError("The account-required positive include is missing or unreachable after all")
        verdicts = []
        for ip in parsed:
            evaluator = Evaluator(resolver)
            result = evaluator.evaluate(domain, ip)
            verdicts.append({"ip": str(ip), "result": result, "lookupTerms": evaluator.lookups,
                             "voidLookups": evaluator.voids})
        passed = all(item["result"] == "pass" for item in verdicts)
        return _check("spf.authorization", "Envelope SPF authorization", "pass" if passed else "fail", domain,
                      "All supplied sending IPs are authorized." if passed else "SPF does not authorize every supplied sending IP.",
                      details={"evaluations": verdicts, "scope": "supplied sending IPs only"})
    except SpfUnavailable as exc:
        return _check("spf.authorization", "Envelope SPF authorization", "unavailable", domain, str(exc))
    except SpfError as exc:
        return _check("spf.authorization", "Envelope SPF authorization", "fail", domain, str(exc))
    except ValueError:
        return _check("spf.authorization", "Envelope SPF authorization", "unavailable", domain,
                      "Sending IP reference evidence is invalid.")
