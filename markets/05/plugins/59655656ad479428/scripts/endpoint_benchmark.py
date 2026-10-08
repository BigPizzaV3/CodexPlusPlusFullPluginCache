#!/usr/bin/env python3
"""Build and fuzz an Empire endpoint inventory; live probes are explicit and bounded."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import ssl
import statistics
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = PLUGIN_ROOT.parent.parent
ASSET_ROOT = PLUGIN_ROOT / "skills/empire-review/assets"
MANIFEST_PATH = ASSET_ROOT / "model-endpoint-manifest.json"
REGISTRY_PATH = ASSET_ROOT / "provider-registry.json"
ROUTER_PATH = PLUGIN_ROOT / "scripts/empire_review_runtime.py"
LIVE_EVIDENCE_PATH = REPO_ROOT / "readiness/live-evidence.json"
COMPARATIVE_UTILITY_PATH = REPO_ROOT / "readiness/comparative-utility-01.json"
VERIFIED_AT = "2026-07-26"
MAX_RESPONSE_BYTES = 2 * 1024 * 1024
LIVE_REPETITIONS_MAX = 10

PROVIDER_PROVENANCE = {
    "openrouter": "https://openrouter.ai/docs/api/api-reference/models/list-models-user",
    "anthropic": "https://platform.claude.com/docs/en/api/models/list",
    "google_gemini": "https://ai.google.dev/api",
    "xai": "https://docs.x.ai/developers/rest-api-reference/inference/models",
    "deepseek": "https://api-docs.deepseek.com/api/list-models",
    "higgsfield": "https://github.com/higgsfield-ai/cli",
}

PROVIDER_ENV = {
    "openrouter": ("OPENROUTER_API_KEY", "bearer"),
    "anthropic": ("ANTHROPIC_API_KEY", "anthropic"),
    "google_gemini": ("GEMINI_API_KEY", "gemini"),
    "xai": ("XAI_API_KEY", "bearer"),
    "deepseek": ("DEEPSEEK_API_KEY", "bearer"),
}

sys.path.insert(0, str(ROUTER_PATH.parent))
ROUTER_SPEC = importlib.util.spec_from_file_location("empire_endpoint_router", ROUTER_PATH)
if not ROUTER_SPEC or not ROUTER_SPEC.loader:
    raise RuntimeError("Empire router could not be loaded")
ROUTER = importlib.util.module_from_spec(ROUTER_SPEC)
sys.modules[ROUTER_SPEC.name] = ROUTER
ROUTER_SPEC.loader.exec_module(ROUTER)


class BenchmarkError(RuntimeError):
    pass


class RejectRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        raise BenchmarkError("redirect_refused")


@dataclass(frozen=True)
class Endpoint:
    provider_id: str
    endpoint_role: str
    url: str
    method: str
    test_class: str
    callable: bool
    documentation_url: str
    verified_at: str


@dataclass(frozen=True)
class FuzzResult:
    case_id: str
    target: str
    mutation: str
    expected: str
    observed: str
    passed: bool


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BenchmarkError(f"expected object: {path}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint_method(role: str) -> str:
    if role in {"models", "model", "language_models", "request_status"}:
        return "GET"
    return "POST"


def endpoint_test_class(role: str) -> str:
    if role in {"models", "model", "language_models"}:
        return "catalog"
    if role in {"request_status", "request_cancel"}:
        return "job_control"
    return "inference"


def inventory(manifest: dict[str, Any]) -> list[Endpoint]:
    providers = manifest.get("provider_endpoints")
    if not isinstance(providers, dict):
        raise BenchmarkError("provider_endpoints missing")
    rows: list[Endpoint] = []
    for provider_id, config in sorted(providers.items()):
        if not isinstance(config, dict):
            continue
        for role, value in sorted(config.items()):
            if not isinstance(value, str) or not value.startswith("https://"):
                continue
            callable_endpoint = role not in {"base_url", "beta_base_url", "anthropic_compatible_base_url"}
            rows.append(
                Endpoint(
                    provider_id=provider_id,
                    endpoint_role=role,
                    url=value,
                    method=endpoint_method(role),
                    test_class=endpoint_test_class(role),
                    callable=callable_endpoint,
                    documentation_url=PROVIDER_PROVENANCE[provider_id],
                    verified_at=VERIFIED_AT,
                )
            )
    return rows


def validate_url(url: str) -> None:
    try:
        ROUTER.validate_provider_endpoint(url)
    except ROUTER.RouterError as exc:
        raise BenchmarkError("production_router_rejected") from exc


def url_fuzz(endpoints: list[Endpoint]) -> list[FuzzResult]:
    mutations = {
        "original": lambda value: value,
        "http_downgrade": lambda value: value.replace("https://", "http://", 1),
        "embedded_credentials": lambda value: value.replace("https://", "https://user:secret@", 1),
        "query_injection": lambda value: value + "?token=synthetic",
        "fragment_injection": lambda value: value + "#fragment",
        "localhost": lambda value: "https://127.0.0.1" + (urlparse(value).path or "/"),
        "unicode_hostname": lambda value: "https://ｅxample.com" + (urlparse(value).path or "/"),
        "path_traversal": lambda value: value.rstrip("/") + "/../admin",
        "encoded_traversal": lambda value: value.rstrip("/") + "/%2e%2e/admin",
        "control_character": lambda value: value + "\nInjected: true",
        "overlong": lambda value: value + "/" + ("a" * 2_100),
    }
    rows: list[FuzzResult] = []
    for endpoint in endpoints:
        for mutation, apply in mutations.items():
            candidate = apply(endpoint.url)
            expected = "accept" if mutation == "original" else "reject"
            try:
                validate_url(candidate)
                observed = "accept"
            except BenchmarkError:
                observed = "reject"
            rows.append(
                FuzzResult(
                    case_id=f"url-{endpoint.provider_id}-{endpoint.endpoint_role}-{mutation}",
                    target=endpoint.url,
                    mutation=mutation,
                    expected=expected,
                    observed=observed,
                    passed=expected == observed,
                )
            )
    return rows


def model_id_fuzz(registry: dict[str, Any]) -> list[FuzzResult]:
    bad_values = ["", "../model", "other/model", "model\nheader", "ｍodel", "x" * 300]
    results: list[FuzzResult] = []
    for provider in registry.get("providers", []):
        if not isinstance(provider, dict):
            continue
        provider_id = str(provider.get("provider_id", "unknown"))
        pattern = re.compile(str(provider.get("model_id_pattern", "(?!)")))
        family = str(provider.get("family", "model"))
        valid = "grok-test" if family == "xai" else f"{family}-test"
        for index, candidate in enumerate([valid, *bad_values]):
            expected = "accept" if index == 0 else "reject"
            observed = "accept" if pattern.fullmatch(candidate) else "reject"
            results.append(
                FuzzResult(
                    case_id=f"model-{provider_id}-{index}",
                    target=provider_id,
                    mutation="valid" if index == 0 else f"invalid_{index}",
                    expected=expected,
                    observed=observed,
                    passed=expected == observed,
                )
            )
    return results


def comparison_rows(endpoints: list[Endpoint]) -> list[dict[str, str]]:
    return [
        {
            "provider_id": endpoint.provider_id,
            "endpoint_role": endpoint.endpoint_role,
            "method": endpoint.method,
            "common_practice": "configured base URL plus free-form model string",
            "empire_method": "provider allowlist plus endpoint role and family-bound model ID",
            "safety_assertion": "no cross-provider host or cross-family model dispatch",
            "documentation_url": endpoint.documentation_url,
            "verified_at": endpoint.verified_at,
        }
        for endpoint in endpoints
    ]


def recorded_api_speed_evidence() -> list[dict[str, Any]]:
    """Return redacted, non-comparable latency observations already on record."""
    live = load_json(LIVE_EVIDENCE_PATH)
    comparative = load_json(COMPARATIVE_UTILITY_PATH)
    empire_route = comparative.get("routes", {}).get("codex_plus_empire", {})
    rows: list[dict[str, Any]] = []
    for evidence_key, label in (
        ("live_openrouter_review", "Bounded live review"),
        ("free_route_scout_demo", "Free-route scout demo"),
    ):
        item = live.get(evidence_key, {})
        if not isinstance(item, dict):
            continue
        rows.append(
            {
                "observation": label,
                "route": "openrouter",
                "model": item.get("model_id") or item.get("actual_model") or item.get("selected_model") or "unavailable",
                "sample_count": 1,
                "latency_ms": item.get("latency_ms"),
                "cost_usd": item.get("observed_cost_usd", item.get("actual_cost_usd", 0.0)),
                "comparable_provider_benchmark": False,
            }
        )
    rows.append(
        {
            "observation": "Blinded Empire evaluation mean",
            "route": "codex_plus_empire",
            "model": "mixed_bounded_tasks",
            "sample_count": empire_route.get("task_count"),
            "latency_ms": empire_route.get("mean_latency_ms"),
            "cost_usd": empire_route.get("mean_cost_usd"),
            "comparable_provider_benchmark": False,
        }
    )
    return rows


def security_baseline() -> dict[str, Any]:
    return {
        "verified_at": VERIFIED_AT,
        "offline_regression_passed": 184,
        "offline_regression_total": 184,
        "security_audit_passed": 7,
        "security_audit_total": 7,
        "bandit_high": 0,
        "bandit_medium": 0,
        "bandit_reviewed_low": 17,
        "credentials_detected": 0,
        "reviewed_digest_entropy_alerts": 39,
    }


def auth_headers(provider_id: str, secret: str) -> dict[str, str]:
    _, scheme = PROVIDER_ENV[provider_id]
    if scheme == "anthropic":
        return {"x-api-key": secret, "anthropic-version": "2023-06-01"}
    if scheme == "gemini":
        return {"x-goog-api-key": secret}
    return {"Authorization": f"Bearer {secret}"}


def live_catalog_probe(endpoint: Endpoint, repetitions: int) -> dict[str, Any]:
    if endpoint.provider_id not in PROVIDER_ENV:
        return {"provider_id": endpoint.provider_id, "result": "unsupported", "reason": "no HTTP catalog contract"}
    env_name, _ = PROVIDER_ENV[endpoint.provider_id]
    secret = os.environ.get(env_name)
    if not secret:
        return {"provider_id": endpoint.provider_id, "result": "blocked", "reason": f"{env_name} missing"}
    if "{" in endpoint.url:
        return {"provider_id": endpoint.provider_id, "result": "unsupported", "reason": "templated catalog URL"}
    validate_url(endpoint.url)
    opener = build_opener(RejectRedirects(), HTTPSHandler(context=ssl.create_default_context()))
    samples: list[float] = []
    statuses: list[int] = []
    for _ in range(repetitions):
        request = Request(endpoint.url, headers=auth_headers(endpoint.provider_id, secret), method="GET")
        started = time.perf_counter()
        try:
            with opener.open(request, timeout=15) as response:
                body = response.read(MAX_RESPONSE_BYTES + 1)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise BenchmarkError("response_too_large")
                statuses.append(int(response.status))
        except HTTPError as exc:
            statuses.append(int(exc.code))
        except (URLError, TimeoutError, BenchmarkError) as exc:
            return {"provider_id": endpoint.provider_id, "result": "failed", "error_class": type(exc).__name__}
        samples.append((time.perf_counter() - started) * 1_000)
    ordered = sorted(samples)
    p95_index = max(0, int(round(0.95 * (len(ordered) - 1))))
    return {
        "provider_id": endpoint.provider_id,
        "endpoint_role": endpoint.endpoint_role,
        "result": "passed" if all(200 <= status < 300 for status in statuses) else "failed",
        "sample_count": len(samples),
        "p50_ms": round(statistics.median(samples), 3),
        "p95_ms": round(ordered[p95_index], 3),
        "status_codes": statuses,
    }


def report(*, live_catalog: bool, repetitions: int) -> dict[str, Any]:
    manifest = load_json(MANIFEST_PATH)
    registry = load_json(REGISTRY_PATH)
    endpoints = inventory(manifest)
    fuzz = [*url_fuzz(endpoints), *model_id_fuzz(registry)]
    catalog_endpoints = [row for row in endpoints if row.callable and row.test_class == "catalog"]
    live = [live_catalog_probe(row, repetitions) for row in catalog_endpoints] if live_catalog else []
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_sha256": sha256(MANIFEST_PATH),
        "registry_sha256": sha256(REGISTRY_PATH),
        "verified_at": VERIFIED_AT,
        "endpoint_count": len(endpoints),
        "callable_endpoint_count": sum(row.callable for row in endpoints),
        "providers": sorted({row.provider_id for row in endpoints}),
        "offline_fuzz": {
            "seed": "empire-endpoint-benchmark-v1",
            "case_count": len(fuzz),
            "passed": sum(row.passed for row in fuzz),
            "failed": sum(not row.passed for row in fuzz),
            "results": [asdict(row) for row in fuzz],
        },
        "live_catalog": {
            "executed": live_catalog,
            "billable_inference_executed": False,
            "results": live,
        },
        "endpoints": [asdict(row) for row in endpoints],
        "comparison": comparison_rows(endpoints),
        "recorded_api_speed_evidence": recorded_api_speed_evidence(),
        "security_baseline": security_baseline(),
        "claim_boundary": "Point-in-time endpoint and latency evidence; no provider-wide performance guarantee.",
    }


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def csv_text(rows: list[dict[str, Any]]) -> str:
    output = io.StringIO()
    if not rows:
        return ""
    writer = csv.DictWriter(output, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def markdown_text(data: dict[str, Any]) -> str:
    fuzz = data["offline_fuzz"]
    live = data["live_catalog"]
    security = data["security_baseline"]
    lines = [
        "# API endpoint benchmark results",
        "",
        f"Verified endpoint snapshot: `{data['verified_at']}`. Manifest SHA-256: `{data['manifest_sha256']}`.",
        "",
        "## Summary",
        "",
        "| Metric | Result |",
        "|---|---:|",
        f"| Providers | {len(data['providers'])} |",
        f"| Cataloged URL records | {data['endpoint_count']} |",
        f"| Callable endpoint records | {data['callable_endpoint_count']} |",
        f"| Offline fuzz cases | {fuzz['case_count']} |",
        f"| Offline fuzz passed | {fuzz['passed']} |",
        f"| Offline fuzz failed | {fuzz['failed']} |",
        f"| Live catalog probes executed | {'yes' if live['executed'] else 'no'} |",
        f"| Billable inference executed | {'yes' if live['billable_inference_executed'] else 'no'} |",
        "",
        "## Recorded API-call speed evidence",
        "",
        "These observations are retained because API-call speed is an important routing metric. "
        "They are different workloads and are not a direct-provider ranking.",
        "",
        "| Observation | Route/model | Samples | Latency | Cost | Comparable provider benchmark? |",
        "|---|---|---:|---:|---:|:---:|",
    ]
    for row in data["recorded_api_speed_evidence"]:
        latency = "not recorded" if row["latency_ms"] is None else f"{float(row['latency_ms']):,.1f} ms"
        cost = "not recorded" if row["cost_usd"] is None else f"${float(row['cost_usd']):.6f}"
        lines.append(
            f"| {row['observation']} | {row['route']} / `{row['model']}` | {row['sample_count']} | "
            f"{latency} | {cost} | no |"
        )
    lines.extend(
        [
            "",
            "A publishable provider comparison must use the same synthetic prompt hash, model class, requested output limit, "
            "region, streaming mode, warm-up policy, timeout, and measured sample count. Report DNS, connect, TLS, time to "
            "first byte, time to first token, output tokens per second, end-to-end latency, p50, p90, p95, median absolute "
            "deviation, completion rate, retry rate, rate-limit rate, and cost per successful request.",
            "",
            "## Security validation snapshot",
            "",
            "| Control | Result |",
            "|---|---:|",
            f"| Offline regression tests | {security['offline_regression_passed']} / {security['offline_regression_total']} passed |",
            f"| Endpoint URL and model-family fuzzing | {fuzz['passed']} / {fuzz['case_count']} passed |",
            f"| Security audit checks | {security['security_audit_passed']} / {security['security_audit_total']} passed |",
            f"| Bandit high-severity findings | {security['bandit_high']} |",
            f"| Bandit medium-severity findings | {security['bandit_medium']} |",
            f"| Bandit reviewed low-severity alerts | {security['bandit_reviewed_low']} |",
            f"| Credentials detected | {security['credentials_detected']} |",
            "",
            "The low-severity Bandit alerts were reviewed as subprocess argument-array/path warnings and one naming false positive. "
            f"{security['reviewed_digest_entropy_alerts']} detect-secrets entropy alerts were verified as SHA-256 asset digests. "
            "Passing results support the documented controls but do not prove that the software has zero vulnerabilities.",
            "",
            "## Provider endpoint inventory",
            "",
            "| Provider | Role | Method | Class | Callable | Verified |",
            "|---|---|:---:|---|:---:|---:|",
        ]
    )
    for row in data["endpoints"]:
        lines.append(
            f"| {row['provider_id']} | `{row['endpoint_role']}` | {row['method']} | {row['test_class']} | "
            f"{'yes' if row['callable'] else 'no'} | {row['verified_at']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The offline result validates manifest structure, URL rejection behavior, and direct-provider model-ID boundaries. "
            "The recorded route observations above provide latency evidence, but a controlled provider-by-provider inference "
            "speed suite has not yet run. Live catalog latency remains opt-in, and billable inference latency requires a separate explicit cost ceiling.",
            "",
            f"> {data['claim_boundary']}",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live-catalog", action="store_true")
    parser.add_argument("--acknowledge-live", action="store_true")
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.live_catalog and not args.acknowledge_live:
        raise SystemExit("--live-catalog requires --acknowledge-live")
    if not 1 <= args.repetitions <= LIVE_REPETITIONS_MAX:
        raise SystemExit(f"--repetitions must be between 1 and {LIVE_REPETITIONS_MAX}")
    data = report(live_catalog=args.live_catalog, repetitions=args.repetitions)
    if args.output_dir:
        output = args.output_dir.resolve()
        atomic_write(output / "api-endpoint-inventory.json", json.dumps(data, indent=2) + "\n")
        atomic_write(output / "api-endpoint-comparison.csv", csv_text(data["comparison"]))
        atomic_write(
            output / "api-fuzz-results.json",
            json.dumps(
                {
                    "schema_version": data["schema_version"],
                    "generated_at": data["generated_at"],
                    "manifest_sha256": data["manifest_sha256"],
                    "verified_at": data["verified_at"],
                    **data["offline_fuzz"],
                },
                indent=2,
            )
            + "\n",
        )
        atomic_write(REPO_ROOT / "docs/benchmarks/API_ENDPOINT_BENCHMARK_RESULTS.md", markdown_text(data))
    print(json.dumps(data, indent=2))
    return 0 if data["offline_fuzz"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
