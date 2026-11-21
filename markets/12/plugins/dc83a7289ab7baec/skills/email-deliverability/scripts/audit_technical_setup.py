#!/usr/bin/env python3
"""Audit fresh Reteno MCP setup using bounded public DNS and TLS evidence."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import ssl
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
from transfer import PinnedHTTPSConnection, atomic_write, verified_tls_context
from receipts import payload
from audit_engine import LookupResult, audit_setup, normalize_dns_name, normalize_setup, render_markdown
from checklist import apply_checklist, bind_checklist_scope


class RealDnsResolver:
    def __init__(self, timeout=3.0, max_queries=256, deadline_seconds=120):
        import dns.resolver
        self.module = dns.resolver
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = timeout
        self.resolver.lifetime = timeout
        self.fallback = dns.resolver.Resolver(configure=False)
        self.fallback.nameservers = ['1.1.1.1']
        self.fallback.timeout = timeout
        self.fallback.lifetime = timeout
        self.cache = {}
        self.max_queries = max_queries
        self.deadline = time.monotonic() + deadline_seconds

    def resolve(self, name, record_type):
        name = normalize_dns_name(name)
        key = (name, record_type.upper())
        if key in self.cache:
            return self.cache[key]
        if len(self.cache) >= self.max_queries or time.monotonic() >= self.deadline:
            return LookupResult([], error_code='budget_exhausted')
        result = self._resolve(self.resolver, *key, fallback=False)
        if result.error_code in {'timeout', 'servfail'} and time.monotonic() < self.deadline:
            result = self._resolve(self.fallback, *key, fallback=True)
        self.cache[key] = result
        return result

    def _resolve(self, resolver, name, kind, *, fallback):
        import dns.exception
        try:
            answers = resolver.resolve(name, kind)
            records = []
            for answer in answers:
                if kind == 'TXT':
                    records.append(b''.join(answer.strings).decode('utf-8', errors='replace'))
                else:
                    records.append(str(answer).rstrip('.'))
                if len(records) > 128:
                    return LookupResult([], error_code='record_budget_exhausted')
            return LookupResult(records, resolver='public-fallback' if fallback else 'system', fallback_used=fallback)
        except self.module.NXDOMAIN:
            code = 'nxdomain'
        except self.module.NoAnswer:
            code = 'no_answer'
        except self.module.NoNameservers:
            code = 'servfail'
        except dns.exception.Timeout:
            code = 'timeout'
        except (dns.exception.DNSException, OSError, ValueError):
            code = 'dns_error'
        return LookupResult([], error_code=code, fallback_used=fallback)


def check_https_tls(hostname):
    connection = PinnedHTTPSConnection(hostname, 443, timeout=5, context=verified_tls_context())
    try:
        connection.connect()
        certificate = connection.sock.getpeercert()
        return {'state': 'valid', 'protocol': connection.sock.version(),
                'expiresAt': datetime.fromtimestamp(ssl.cert_time_to_seconds(certificate['notAfter']), timezone.utc).isoformat() if certificate.get('notAfter') else None}
    except ssl.SSLCertVerificationError:
        return {'state': 'invalid', 'reason': 'certificate_invalid'}
    except ValueError:
        return {'state': 'invalid', 'reason': 'non_public_address'}
    except (OSError, ssl.SSLError):
        return {'state': 'inconclusive', 'reason': 'network_error'}
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--organization-id', required=True)
    parser.add_argument('--references', type=Path)
    parser.add_argument('--output-dir', type=Path, default=Path('output/email-deliverability'))
    args = parser.parse_args()
    try:
        raw = payload(json.loads(args.input.read_text()))
        scope = normalize_setup(raw, expected_org_id=args.organization_id)
        references = json.loads(args.references.read_text()) if args.references else {}
        scope = bind_checklist_scope(scope, references)
        resolver = RealDnsResolver()
        report = audit_setup(scope, resolver=resolver, tls_checker=check_https_tls)
        report = apply_checklist(report, references, resolver, tls_checker=check_https_tls)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        # A fixed numeric account boundary keeps filenames independent of MCP text.
        org = str(int(args.organization_id))
        base = args.output_dir / f'technical_setup_{org}_{stamp}'
        atomic_write(base.with_suffix('.json'), (json.dumps(report, indent=2, ensure_ascii=False)+'\n').encode())
        atomic_write(base.with_suffix('.md'), render_markdown(report).encode())
        print(json.dumps({'summary': report['summary'], 'json': str(base.with_suffix('.json')), 'markdown': str(base.with_suffix('.md'))}))
    except (ValueError, OSError, ImportError) as exc:
        parser.exit(1, f'Audit could not complete: {exc}\n')


if __name__ == '__main__':
    main()
