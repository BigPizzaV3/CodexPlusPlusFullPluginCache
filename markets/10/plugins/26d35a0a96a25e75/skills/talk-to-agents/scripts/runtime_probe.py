#!/usr/bin/env python3
"""Non-secret, read-only capability leads; never connects or consumes messages.

Default mode runs no subprocess. --check-systemd performs only a bounded,
read-only user service-manager query. No configuration contents are read,
no files are written, and no state-changing command is available.
"""
import argparse
import json
import os
import platform
import shutil
import subprocess
from pathlib import Path

TOOLS = ("bolter-agent", "codex", "systemctl", "crontab", "launchctl", "schtasks")
KNOWN_SYSTEMD_STATES = {
    "initializing", "starting", "running", "degraded", "maintenance",
    "stopping", "offline", "unknown",
}


def directory_status(path):
    """Report properties of a directory without reading its contents or creating it."""
    if path is None:
        return {"configured": False, "exists": False, "writable": False}
    try:
        directory = Path(path)
        exists = directory.is_dir()
        return {"configured": True, "exists": exists,
                "writable": exists and os.access(directory, os.W_OK | os.X_OK)}
    except (OSError, ValueError):
        return {"configured": True, "exists": None, "writable": None}


def systemd_status(binary, runner=None):
    """Never return stderr or arbitrary command output; it may contain private data."""
    if not binary:
        return {"check": "unavailable", "manager_reachable": False}
    runner = subprocess.run if runner is None else runner
    try:
        result = runner(
            [binary, "--user", "is-system-running"],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, timeout=3, check=False,
        )
    except subprocess.TimeoutExpired:
        return {"check": "timed_out", "manager_reachable": None}
    except PermissionError:
        return {"check": "denied", "manager_reachable": None}
    except OSError:
        return {"check": "unavailable", "manager_reachable": None}
    stderr = (result.stderr or "").lower()
    if "permission denied" in stderr or "operation not permitted" in stderr:
        return {"check": "denied", "manager_reachable": None}
    state = (result.stdout or "").strip().lower()
    if state in KNOWN_SYSTEMD_STATES:
        return {"check": "checked", "manager_reachable": state not in {"offline", "unknown"},
                "reported_state": state}
    return {"check": "unconfirmed", "manager_reachable": None}


def collect(workspace=None, check_systemd=False):
    found = {tool: shutil.which(tool) for tool in TOOLS}
    system = platform.system()
    if check_systemd and system == "Linux":
        manager = systemd_status(found["systemctl"])
    elif check_systemd:
        manager = {"check": "not_applicable", "manager_reachable": None}
    else:
        manager = {"check": "not_checked", "manager_reachable": None}
    return {
        "schema_version": 1,
        "read_only": True,
        "platform": {"system": system, "machine": platform.machine()},
        "tools_on_path": {tool: bool(path) for tool, path in found.items()},
        "directories": {
            "workspace": directory_status(workspace if workspace is not None else os.getcwd()),
            "home": directory_status(os.environ.get("HOME")),
            "xdg_config_home": directory_status(os.environ.get("XDG_CONFIG_HOME")),
        },
        "systemd_user_manager": manager,
        "not_tested": [
            "Bolter identity or credentials", "active listener or unread messages",
            "native connector or subscription", "same-agent wake command",
            "unattended approval compatibility", "durable storage",
            "startup configuration", "reply delivery", "restart recovery",
        ],
        "conclusion": "Inventory only. Tool presence and directory access do not prove persistence.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", help="Directory to inspect without creating it; defaults to cwd")
    parser.add_argument("--check-systemd", action="store_true",
                        help="Run a bounded read-only Linux user-manager query; no service changes")
    args = parser.parse_args()
    print(json.dumps(collect(args.workspace, args.check_systemd), indent=2))


if __name__ == "__main__":
    main()
