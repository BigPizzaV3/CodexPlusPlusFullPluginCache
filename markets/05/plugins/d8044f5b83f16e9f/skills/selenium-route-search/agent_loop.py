"""Minimal, dependency-free agent loop for the Selenium route-search API.

Submit -> poll (honoring Retry-After) -> read ranked routes. Uses only the
Python standard library so it drops into any agent runtime.

    SELENIUM_API_URL=https://... B12_API_KEY=b12_live_... \\
        python agent_loop.py "CC(=O)Oc1ccccc1C(=O)O" --tier standard
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request

TIERS = {
    "scout": {"researcher_runs": 1, "max_route_families": 1, "target_ready_routes": 1, "timeout_minutes": 15},
    "basic": {"researcher_runs": 1, "max_route_families": 3, "target_ready_routes": 1, "timeout_minutes": 30},
    "standard": {"researcher_runs": 5, "max_route_families": 8, "target_ready_routes": 3, "timeout_minutes": 90},
    "exhaustive": {"researcher_runs": 12, "max_route_families": 24, "target_ready_routes": 6, "timeout_minutes": 360},
}
TERMINAL = {"completed", "partial", "failed", "cancelled"}


def _call(base, key, method, path, body=None, headers=None):
    url = f"{base.rstrip('/')}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {key}")
    if data:
        req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            retry_after = resp.headers.get("Retry-After")
            payload = json.loads(resp.read().decode())
            return payload, (int(retry_after) if retry_after else None)
    except urllib.error.HTTPError as exc:  # noqa: PERF203
        detail = json.loads(exc.read().decode() or "{}")
        raise SystemExit(f"API error {exc.code}: {json.dumps(detail)}") from exc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("smiles")
    ap.add_argument("--tier", choices=sorted(TIERS), default="standard")
    ap.add_argument("--name", default=None)
    ap.add_argument("--idempotency-key", default=None)
    ap.add_argument(
        "--approved-credits",
        type=int,
        default=None,
        help="Required for Scout; must exactly match the live quote.",
    )
    ap.add_argument("--max-wait-seconds", type=int, default=7200)
    args = ap.parse_args()

    base, key = os.getenv("SELENIUM_API_URL"), os.getenv("B12_API_KEY")
    if not base or not key:
        raise SystemExit("set SELENIUM_API_URL and B12_API_KEY")

    body = {
        "smiles": args.smiles,
        "name": args.name,
        "tier": args.tier,
        **TIERS[args.tier],
    }
    body = {k: v for k, v in body.items() if v is not None}

    quote, _ = _call(base, key, "POST", "/v1/route-searches/quote", body)
    print(f"quote: {quote['credits_required']} credits", file=sys.stderr)
    if args.tier == "scout":
        if args.approved_credits != int(quote["credits_required"]):
            raise SystemExit(
                "Scout requires explicit approval of the live quote; re-run with "
                f"--approved-credits {quote['credits_required']}"
            )
        body["quote_id"] = quote["quote_id"]
        body["approved_credits"] = args.approved_credits

    # Stable idempotency key: a retried submit returns the same job, never a
    # second billable one.
    idem = args.idempotency_key or f"{args.smiles}|{args.tier}"
    job, _ = _call(base, key, "POST", "/v1/route-searches", body, {"Idempotency-Key": idem})
    job_id = job["id"]
    print(f"submitted {job_id} ({job['status']}, charged {job['credits_charged']})", file=sys.stderr)

    deadline = time.monotonic() + args.max_wait_seconds
    while True:
        status, retry_after = _call(base, key, "GET", f"/v1/route-searches/{job_id}")
        p = status.get("progress") or {}
        print(f"  {status['status']}: {p.get('families_solved', 0)} solved / "
              f"{p.get('families_found', 0)} found, {p.get('elapsed_minutes', 0)}min",
              file=sys.stderr)
        if status["status"] in TERMINAL:
            break
        if time.monotonic() >= deadline:
            print("wait budget exhausted; job still running", file=sys.stderr)
            break
        time.sleep(max(30, retry_after or status.get("retry_after_seconds") or 60))

    routes, _ = _call(base, key, "GET", f"/v1/route-searches/{job_id}/routes")
    print(json.dumps(routes, indent=2))  # machine-readable result to stdout
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
