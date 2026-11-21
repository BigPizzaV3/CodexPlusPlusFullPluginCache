#!/usr/bin/env python3
"""Control the lifecycle of the one existing Morningside K3s instance."""

import argparse
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


INSTANCE = "morningside-k3s-v001"
SERVICE = "k3s"
STATE_FORMAT = "{{.Name}}|{{.Status}}|{{.VMType}}|{{.Arch}}"
ANSI = re.compile(r"\x1b\[[0-9;]*m")


class ControlError(Exception):
    pass


class Morningside:
    def __init__(self, limactl):
        self.limactl = limactl
        self.env = dict(os.environ)
        self.env["LIMA_HOME"] = str(Path.home() / ".lima")
        self.env.pop("SSH", None)

    def lima(self, *args, timeout=15):
        try:
            return subprocess.run(
                [self.limactl, "--tty=false", *args],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                errors="replace",
                env=self.env,
                cwd="/",
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exc:
            raise ControlError("Lima timed out. Check status before trying again.") from exc
        except OSError as exc:
            raise ControlError("Could not run Lima. Check that it is installed and accessible.") from exc

    def vm_state(self):
        result = self.lima("list", INSTANCE, "--format", STATE_FORMAT)
        if result.returncode != 0:
            if f"No instance matching {INSTANCE} found" in result.stderr:
                raise ControlError(f"Existing Lima instance {INSTANCE} was not found.")
            raise ControlError("Could not inspect Morningside in the default Lima home.")
        fields = result.stdout.strip().split("|")
        if len(fields) != 4 or fields[0] != INSTANCE or fields[2:] != ["vz", "aarch64"]:
            raise ControlError("The instance did not match the expected Morningside VM identity.")
        if fields[1] not in ("Running", "Stopped"):
            raise ControlError("Lima did not report Morningside as Running or Stopped.")
        return fields[1].lower()

    def openrc(self, *args, timeout=15):
        return self.lima(
            "shell", "--start=false", "--preserve-env=false", "--workdir=/", INSTANCE,
            "sudo", "-n", "rc-service", *args, timeout=timeout,
        )

    def service_state(self):
        if self.openrc("--exists", SERVICE).returncode != 0:
            raise ControlError("Could not confirm the OpenRC K3s service inside Morningside.")
        response = self.openrc(SERVICE, "status")
        lines = ANSI.sub("", response.stdout).splitlines()
        if response.returncode == 0 and any(line.strip() == "* status: started" for line in lines):
            return "running"
        if response.returncode != 0 and any(line.strip() == "* status: stopped" for line in lines):
            return "stopped"
        if response.returncode != 0 and any(line.strip() == "* status: crashed" for line in lines):
            return "crashed"
        raise ControlError("Could not establish K3s service state from OpenRC.")

    def control(self, action, state):
        state["vm"] = self.vm_state()
        if state["vm"] == "stopped":
            state["k3s"] = "offline"
            if action != "start":
                return
            state.update(vm="unknown", k3s="unknown")
            if self.lima("start", "--timeout=90s", INSTANCE, timeout=100).returncode != 0:
                raise ControlError("Morningside startup did not complete. Check status before trying again.")
            state["vm"] = self.vm_state()
            if state["vm"] != "running":
                raise ControlError("Lima did not confirm that Morningside started.")

        state["k3s"] = self.service_state()
        if action == "start" and state["k3s"] != "running":
            if state["k3s"] == "crashed":
                raise ControlError("OpenRC reports K3s crashed. Inspect the service before trying again.")
            state["k3s"] = "unknown"
            if self.openrc(SERVICE, "start", timeout=60).returncode != 0:
                raise ControlError("K3s service startup did not complete. Check status before trying again.")
            state["k3s"] = self.service_state()
            if state["k3s"] != "running":
                raise ControlError("OpenRC did not confirm that K3s started.")
        if action == "stop":
            state.update(vm="unknown", k3s="unknown")
            if self.lima("stop", INSTANCE, timeout=100).returncode != 0:
                raise ControlError("Morningside shutdown did not complete. Check status before trying again.")
            state["vm"] = self.vm_state()
            if state["vm"] != "stopped":
                raise ControlError("Lima did not confirm that Morningside stopped.")
            state["k3s"] = "offline"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("status", "start", "stop"))
    args = parser.parse_args()
    result = dict(action=args.action, target=INSTANCE, vm="unknown", k3s="unknown")
    try:
        if platform.system() != "Darwin" or platform.machine() != "arm64":
            raise ControlError("Use Morningside from a native Apple silicon macOS session.")
        lima_path = os.pathsep.join([os.environ.get("PATH", os.defpath), "/opt/homebrew/bin", "/usr/local/bin"])
        limactl = shutil.which("limactl", path=lima_path)
        if limactl is None:
            raise ControlError("Lima is required. Install Lima, then check Morningside status again.")
        Morningside(str(Path(limactl).resolve())).control(args.action, result)
    except ControlError as exc:
        print(json.dumps(dict(result, ok=False, error=str(exc)), sort_keys=True))
        return 1
    print(json.dumps(dict(result, ok=True), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
