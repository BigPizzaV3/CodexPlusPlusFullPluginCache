#!/usr/bin/env python3
"""Check the local runtime; never inspect host credentials or make MCP calls."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys


def main():
    checks = {"python311": sys.version_info >= (3, 11),
              "dnspython": importlib.util.find_spec("dns") is not None}
    try:
        from transfer import verified_tls_context
        checks["trustedTlsCertificates"] = bool(verified_tls_context().get_ca_certs())
    except (ImportError, OSError, ValueError):
        checks["trustedTlsCertificates"] = False
    try:
        version = subprocess.check_output(["node", "--version"], text=True).strip()
        numbers = tuple(map(int, re.findall(r"\d+", version)[:3]))
        checks["node20181"] = numbers >= (20, 18, 1)
    except (OSError, subprocess.CalledProcessError):
        checks["node20181"] = False
    root = Path(__file__).resolve().parents[1]
    checks["emailSdk"] = (root / "packages/convo-email-agent/index.js").is_file()
    checks["segmentSdk"] = (root / "packages/segment-designer-sdk/dist/index.js").is_file()
    print(json.dumps({"ready": all(checks.values()), "checks": checks,
                      "optionalPlaywright": importlib.util.find_spec("playwright") is not None}))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
