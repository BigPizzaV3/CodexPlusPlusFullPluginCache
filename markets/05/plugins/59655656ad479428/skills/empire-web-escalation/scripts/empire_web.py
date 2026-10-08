#!/usr/bin/env python3
"""Report the native-only web policy; legacy provider commands are disabled.

This compatibility entrypoint has no networking, credential, file-upload,
subprocess, or remote-browser implementation. Codex performs public research
through its own available web tools under their normal access controls.
"""

from __future__ import annotations

import argparse
import json


def policy() -> dict[str, object]:
    return {
        "status": "native_browser_only",
        "external_provider_dispatch": False,
        "credential_access": False,
        "file_uploads": False,
        "remote_browser_actions": False,
        "access_denied_behavior": "stop_and_report",
        "instruction": "Use Codex native web tools for public sources. Stop at access restrictions.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["policy"], nargs="?", default="policy")
    parser.parse_args(argv)
    print(json.dumps(policy(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
