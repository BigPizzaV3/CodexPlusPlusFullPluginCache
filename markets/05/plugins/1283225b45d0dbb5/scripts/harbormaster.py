#!/usr/bin/env python3
"""
Harbormaster ⚓  —  the anti-killall.

The everyday doom loop this kills:
    "port's busy"  →  `killall node`  →  ...wait why is EVERYTHING dead  →  who did this?

Harbormaster shows you every listening port, ties each one to the project
that owns it, frees exactly ONE port when you ask (never the whole harbor),
and logs every kill + every mysterious disappearance so a dev server can
never vanish on you again without a paper trail.

Two faces, one engine:
    • CLI       →  `ports`  (instant, surgical, lives in your terminal)
    • Dashboard →  `ports serve`  (live, auto-refreshing, click-to-kill)

Target: macOS (Apple Silicon / Intel). Also works on Linux with psutil.
Deps:   none for the macOS CLI; psutil is an optional cross-platform fallback;
        flask is only needed for the dashboard.
Data:   ~/.harbormaster/  (history.jsonl + state.json)
"""

import argparse
import getpass
import json
import os
import pwd
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ----------------------------------------------------------------------------
# Soft dependency handling — fail gracefully with install hints
# ----------------------------------------------------------------------------
try:
    import psutil
except ImportError:
    psutil = None

APP_DIR = Path.home() / ".harbormaster"
HISTORY_FILE = APP_DIR / "history.jsonl"
STATE_FILE = APP_DIR / "state.json"
RESERVATIONS_FILE = APP_DIR / "reservations.json"
DEFAULT_DASH_PORT = 7717  # "HARBOR"-ish, unlikely to collide

# Commands that are almost certainly a dev server you spun up yourself.
DEV_COMMANDS = {
    "node", "deno", "bun", "npm", "pnpm", "yarn", "next-server", "next-router-worker",
    "vite", "esbuild", "webpack", "rollup", "parcel", "turbo", "ng", "serve",
    "http-server", "live-server", "nodemon", "ts-node", "tsx",
    "python", "python3", "python3.10", "python3.11", "python3.12", "python3.13",
    "flask", "gunicorn", "uvicorn", "hypercorn", "daphne", "waitress-serve",
    "ruby", "rails", "puma", "rackup", "thin", "unicorn",
    "php", "php-fpm", "artisan",
    "java", "gradle", "mvn", "spring",
    "go", "air", "cargo", "rustc", "trunk",
    "dotnet", "caddy", "deno", "bun", "wrangler", "miniflare", "convex",
    "rails", "meteor", "expo", "metro", "storybook", "vercel", "netlify",
}

# macOS / system daemons that listen on ports but you almost never want to kill.
SYSTEM_HINTS = {
    "rapportd", "sharingd", "controlce", "controlcenter", "airplayxpchelper",
    "remoted", "launchd", "mdnsresponder", "netbiosd", "cupsd", "apache",
    "identityservicesd", "akd", "homed", "rapport", "spotlight",
    "softwareupdated", "trustd", "syspolicyd", "secd",
}


# ----------------------------------------------------------------------------
# ANSI color helpers (auto-disabled when not a TTY)
# ----------------------------------------------------------------------------
class C:
    enabled = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    @classmethod
    def paint(cls, text, *codes):
        if not cls.enabled:
            return text
        return "".join(codes) + text + cls.RESET

    @classmethod
    def c256(cls, text, n):
        if not cls.enabled:
            return text
        return f"\033[38;5;{n}m{text}{cls.RESET}"


# A pleasant, readable spread of xterm-256 colors for project badges.
_BADGE_COLORS = [39, 208, 170, 76, 214, 45, 199, 105, 220, 51, 207, 84, 222, 117, 213, 156]

# Matching hex colors for the web dashboard, keyed by the same index.
_BADGE_HEX = [
    "#36a3ff", "#ff8c1a", "#c77dff", "#5ad17a", "#ffb02e", "#34d6e6",
    "#ff4fa3", "#8c9eff", "#ffd23f", "#22d3ee", "#ff6ec7", "#7CFC9B",
    "#ffe066", "#7cc4ff", "#ff79e1", "#b9f5b1",
]


def _stable_index(name, modulo):
    h = 0
    for ch in name:
        h = (h * 131 + ord(ch)) & 0xFFFFFFFF
    return h % modulo


def badge_256(name):
    return _BADGE_COLORS[_stable_index(name, len(_BADGE_COLORS))]


def badge_hex(name):
    return _BADGE_HEX[_stable_index(name, len(_BADGE_HEX))]


# ----------------------------------------------------------------------------
# Time helpers
# ----------------------------------------------------------------------------
def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def human_age(seconds):
    if seconds is None:
        return "—"
    seconds = int(seconds)
    if seconds < 0:
        seconds = 0
    if seconds < 60:
        return f"{seconds}s"
    m, s = divmod(seconds, 60)
    if m < 60:
        return f"{m}m{s:02d}s"
    h, m = divmod(m, 60)
    if h < 24:
        return f"{h}h{m:02d}m"
    d, h = divmod(h, 24)
    return f"{d}d{h:02d}h"


def human_clock(iso_str):
    """Turn an ISO timestamp into a short local clock like '2:43pm'."""
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%-I:%M%p").lower()
    except Exception:
        return iso_str


# ----------------------------------------------------------------------------
# Project attribution — walk up from a process cwd to find what owns it
# ----------------------------------------------------------------------------
_PROJECT_MARKERS = (
    ".git", "package.json", "pyproject.toml", "Cargo.toml", "go.mod",
    "Gemfile", "composer.json", "pom.xml", "build.gradle", ".project-root",
    "requirements.txt", "deno.json", "bun.lockb",
)


def project_for(cwd):
    """Return (project_name, project_root) for a working directory, or (None, None)."""
    if not cwd:
        return None, None
    try:
        p = Path(cwd).resolve()
    except Exception:
        return None, None
    home = Path.home().resolve()
    cur = p
    # Walk up looking for a project marker, but stop at home / filesystem root.
    for _ in range(40):
        try:
            for marker in _PROJECT_MARKERS:
                if (cur / marker).exists():
                    return cur.name, str(cur)
        except (PermissionError, OSError):
            pass
        if cur == cur.parent or cur == home:
            break
        cur = cur.parent
    # No marker found — fall back to the cwd's own folder name.
    return p.name, str(p)


def _project_from_launchd_label(label):
    """Return the human service identity from a reverse-DNS launchd label."""
    if not label:
        return None
    parts = [part for part in str(label).strip().split(".") if part]
    if not parts:
        return None
    candidate = parts[-1].strip()
    return candidate or None


def project_for_process(cwd, cmdline, executable, launchd_label=None):
    """Attribute launchd and agent-owned services without trusting cwd alone."""
    project, root = project_for(cwd)
    if project and project != "/":
        return project, root

    try:
        words = shlex.split(cmdline or "")
    except ValueError:
        words = []
    for index, word in enumerate(words[:-1]):
        if word == "-m":
            module = words[index + 1].strip()
            if module:
                return module.split(".", 1)[0], None

    for word in words[1:]:
        if word.startswith("-"):
            continue
        candidate = Path(word).expanduser()
        if candidate.suffix in {".py", ".js", ".ts", ".rb"}:
            project, root = project_for(str(candidate.parent))
            if project:
                return project, root

    launchd_project = _project_from_launchd_label(launchd_label)
    if launchd_project:
        return launchd_project, None

    executable_name = Path(executable or "").name
    if executable_name:
        return executable_name, None
    return None, None


# ----------------------------------------------------------------------------
# Core enumeration: who is listening on what?
# ----------------------------------------------------------------------------
def _lsof_listeners():
    """
    Use lsof to enumerate listening TCP sockets. Works WITHOUT sudo for the
    current user's processes (i.e. your dev servers), which is the whole point.
    Returns a dict keyed by (port, pid) -> {port, pid, addrs:set}.
    """
    cmd = ["lsof", "-nP", "-iTCP", "-sTCP:LISTEN", "-FpcnL"]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    # lsof exits non-zero (1) when it has partial permission issues but still
    # prints usable rows, so we parse stdout regardless of return code.
    rows = {}
    cur_pid = None
    for line in out.stdout.splitlines():
        if not line:
            continue
        tag, val = line[0], line[1:]
        if tag == "p":
            try:
                cur_pid = int(val)
            except ValueError:
                cur_pid = None
        elif tag == "n" and cur_pid is not None:
            port = _port_from_name(val)
            if port is None:
                continue
            key = (port, cur_pid)
            rows.setdefault(key, {"port": port, "pid": cur_pid, "addrs": set()})
            rows[key]["addrs"].add(val)
    return rows


def _port_from_name(name):
    """Extract the listening port from an lsof name like '*:3000' or '[::1]:8080'."""
    if not name or "->" in name:  # '->' means an established conn, not a listener
        return None
    local = name.split("->")[0].strip()
    # Strip IPv6 brackets, then take the trailing :PORT
    m = re.search(r":(\d+)$", local)
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def _psutil_listeners():
    """
    Fallback enumerator using psutil per-process (works without root on macOS
    for your OWN processes). Slower than lsof but dependency-light.
    """
    rows = {}
    if psutil is None:
        return rows
    for proc in psutil.process_iter(["pid"]):
        try:
            conns = proc.net_connections(kind="inet")
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue
        except Exception:
            continue
        for conn in conns:
            if conn.status != psutil.CONN_LISTEN:
                continue
            if not conn.laddr:
                continue
            port = conn.laddr.port
            pid = proc.info["pid"]
            key = (port, pid)
            rows.setdefault(key, {"port": port, "pid": pid, "addrs": set()})
            rows[key]["addrs"].add(f"{conn.laddr.ip}:{port}")
    return rows


def _lsof_process_metadata(pid):
    """Return owner UID and executable path using native macOS tooling."""
    executable = shutil.which("lsof") or "/usr/sbin/lsof"
    try:
        result = subprocess.run(
            [executable, "-nP", "-p", str(pid), "-Fnfu"],
            capture_output=True,
            text=True,
            timeout=3,
            check=False,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return None, ""
    if result.returncode not in (0, 1):
        return None, ""
    owner_uid = None
    current_file = ""
    process_executable = ""
    for line in result.stdout.splitlines():
        if not line:
            continue
        prefix, value = line[:1], line[1:]
        if prefix == "u" and owner_uid is None:
            try:
                owner_uid = int(value)
            except ValueError:
                pass
        elif prefix == "f":
            current_file = value
        elif prefix == "n" and current_file == "txt" and not process_executable:
            if value.startswith("/"):
                process_executable = value
    return owner_uid, process_executable


def _ps_command(pid):
    """Read one process command without requiring psutil."""
    try:
        result = subprocess.run(
            ["/bin/ps", "-p", str(pid), "-o", "command="],
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return ()
    if result.returncode != 0 or not result.stdout.strip():
        return ()
    try:
        return tuple(shlex.split(result.stdout.strip()))
    except ValueError:
        return ()


def _launchd_service_label(pid, owner_uid=None):
    """Resolve a current-user launchd service label without requiring root."""
    uid = os.getuid() if owner_uid is None else owner_uid
    if uid != os.getuid():
        return None
    try:
        result = subprocess.run(
            ["/bin/launchctl", "print", f"gui/{uid}"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (FileNotFoundError, OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    target = str(pid)
    for line in result.stdout.splitlines():
        match = re.match(r"^\s*(\d+)\s+[-\d]+\s+(\S+)\s*$", line)
        if match and match.group(1) == target:
            return match.group(2)
    return None


def classify(name, cwd):
    """Return 'dev' or 'system' — used to sort + style + guard kills."""
    n = (name or "").lower()
    base = n.split("/")[-1]
    if base in SYSTEM_HINTS:
        return "system"
    if base in DEV_COMMANDS or any(base.startswith(d) for d in ("python", "node", "ruby", "java")):
        return "dev"
    home = str(Path.home())
    if cwd and cwd.startswith(home) and "/Library/" not in cwd:
        return "dev"
    return "system"


def enrich(pid):
    """Pull rich detail for a PID with native macOS and optional psutil evidence."""
    info = {
        "name": None, "cmdline": None, "cwd": None,
        "username": None, "owner_uid": None, "executable": None,
        "launchd_label": None,
        "create_time": None, "age": None, "exists": True,
    }
    owner_uid, executable = _lsof_process_metadata(pid)
    command = _ps_command(pid)
    info["owner_uid"] = owner_uid
    info["executable"] = executable or None
    info["launchd_label"] = _launchd_service_label(pid, owner_uid)
    if command:
        info["cmdline"] = " ".join(command)
        info["name"] = Path(command[0]).name
    elif executable:
        info["name"] = Path(executable).name

    if owner_uid is not None:
        try:
            info["username"] = pwd.getpwuid(owner_uid).pw_name
        except (KeyError, OSError):
            pass

    if psutil is not None:
        try:
            p = psutil.Process(pid)
            with p.oneshot():
                info["name"] = info["name"] or p.name()
                if not info["cmdline"]:
                    try:
                        info["cmdline"] = " ".join(p.cmdline())
                    except (psutil.AccessDenied, Exception):
                        info["cmdline"] = info["name"]
                try:
                    info["cwd"] = p.cwd()
                except (psutil.AccessDenied, Exception):
                    info["cwd"] = None
                if not info["username"]:
                    try:
                        info["username"] = p.username()
                    except Exception:
                        info["username"] = None
                if info["owner_uid"] is None:
                    try:
                        info["owner_uid"] = int(p.uids().real)
                    except Exception:
                        pass
                if not info["executable"]:
                    try:
                        info["executable"] = p.exe()
                    except Exception:
                        pass
                try:
                    ct = p.create_time()
                    info["create_time"] = ct
                    info["age"] = time.time() - ct
                except Exception:
                    pass
        except psutil.NoSuchProcess:
            info["exists"] = False
        except Exception:
            pass
    return info


def list_listeners():
    """
    Return a sorted list of listener dicts, one per (port, pid), each enriched
    with project attribution and a dev/system classification.
    """
    try:
        raw = _lsof_listeners()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        raw = _psutil_listeners()
    if not raw:
        # lsof present but empty (or errored) — try the psutil path too.
        raw = raw or _psutil_listeners()

    listeners = []
    self_pid = os.getpid()
    reservations = read_reservations()
    for (port, pid), base in raw.items():
        meta = enrich(pid)
        proj_name, proj_root = project_for_process(
            meta.get("cwd"), meta.get("cmdline"), meta.get("executable"),
            meta.get("launchd_label")
        )
        kind = classify(meta.get("name"), meta.get("cwd"))
        cmd_short = (meta.get("name") or "?")
        proj_display = proj_name or "—"
        res = reservations.get(str(port))
        reserved_project = res.get("project") if res else None
        listeners.append({
            "port": port,
            "pid": pid,
            "command": cmd_short,
            "cmdline": meta.get("cmdline") or cmd_short,
            "cwd": meta.get("cwd"),
            "project": proj_display,
            "project_root": proj_root,
            "launchd_label": meta.get("launchd_label"),
            "username": meta.get("username"),
            "owner_uid": meta.get("owner_uid"),
            "age": meta.get("age"),
            "age_h": human_age(meta.get("age")),
            "addrs": sorted(base["addrs"]),
            "kind": kind,
            "is_self": pid == self_pid,
            "reserved_project": reserved_project,
            "reserved_note": (res.get("note") if res else None) or None,
            "collision": _is_collision(reserved_project, proj_display),
        })
    # Sort: dev servers first, then by project, then by port.
    listeners.sort(key=lambda l: (l["kind"] != "dev", (l["project"] or "").lower(), l["port"]))
    return listeners


def find_on_port(port):
    return [l for l in list_listeners() if l["port"] == port]


# ----------------------------------------------------------------------------
# History / flight recorder
# ----------------------------------------------------------------------------
def _ensure_app_dir():
    APP_DIR.mkdir(parents=True, exist_ok=True)


def log_event(event):
    """Append an event dict to history.jsonl (best-effort)."""
    _ensure_app_dir()
    event = {"ts": now_iso(), **event}
    try:
        with open(HISTORY_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        pass
    return event


def read_history(limit=200):
    if not HISTORY_FILE.exists():
        return []
    try:
        lines = HISTORY_FILE.read_text().splitlines()
    except Exception:
        return []
    events = []
    for line in lines[-limit:]:
        try:
            events.append(json.loads(line))
        except Exception:
            continue
    events.reverse()  # newest first
    return events


def _recent_kill_for(pid, within=45):
    """Did WE kill this pid recently? Used to distinguish kills from crashes."""
    if not HISTORY_FILE.exists():
        return False
    try:
        lines = HISTORY_FILE.read_text().splitlines()[-80:]
    except Exception:
        return False
    cutoff = time.time() - within
    for line in lines:
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("action") == "kill" and e.get("pid") == pid:
            try:
                ts = datetime.fromisoformat(e["ts"]).timestamp()
                if ts >= cutoff:
                    return True
            except Exception:
                return True
    return False


def snapshot_and_diff(current, log_appears=True):
    """
    Compare the current listeners against the last snapshot. Anything that
    DISAPPEARED without a recent kill from us gets logged as 'vanished'
    (a crash or an outside-killall) — this is the flight recorder that means
    a server never dies mysteriously again. Returns list of new events.
    """
    _ensure_app_dir()
    prev = {}
    if STATE_FILE.exists():
        try:
            prev = json.loads(STATE_FILE.read_text())
        except Exception:
            prev = {}

    cur_map = {f"{l['port']}:{l['pid']}": l for l in current}
    new_events = []

    # Appeared
    if log_appears:
        for key, l in cur_map.items():
            if key not in prev:
                new_events.append(log_event({
                    "action": "appeared", "port": l["port"], "pid": l["pid"],
                    "command": l["command"], "project": l["project"], "cwd": l["cwd"],
                }))

    # Vanished
    for key, l in prev.items():
        if key not in cur_map:
            pid = l.get("pid")
            if _recent_kill_for(pid):
                continue  # already accounted for as an intentional kill
            new_events.append(log_event({
                "action": "vanished", "port": l.get("port"), "pid": pid,
                "command": l.get("command"), "project": l.get("project"),
                "cwd": l.get("cwd"),
                "note": "disappeared on its own — crash or killed by something else",
            }))

    # Save new snapshot (slim)
    slim = {k: {"port": v["port"], "pid": v["pid"], "command": v["command"],
                "project": v["project"], "cwd": v["cwd"]} for k, v in cur_map.items()}
    try:
        STATE_FILE.write_text(json.dumps(slim))
    except Exception:
        pass
    return new_events


# ----------------------------------------------------------------------------
# Reservations — "this port belongs to that project; warn me on collisions"
# ----------------------------------------------------------------------------
def read_reservations():
    """Return the reservation map {port_str: {"project":..., "note":...}}."""
    if not RESERVATIONS_FILE.exists():
        return {}
    try:
        data = json.loads(RESERVATIONS_FILE.read_text())
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def write_reservations(data):
    _ensure_app_dir()
    try:
        RESERVATIONS_FILE.write_text(json.dumps(data, indent=2, sort_keys=True))
        return True
    except Exception:
        return False


def reservation_for(port):
    """Return the reservation dict for a port, or None."""
    return read_reservations().get(str(port))


def reserve_port(port, project, note=""):
    """Record that `port` is expected to belong to `project`. Returns the entry."""
    data = read_reservations()
    entry = {"project": project, "note": note or ""}
    data[str(port)] = entry
    write_reservations(data)
    return entry


def unreserve_port(port):
    """Drop a reservation. Returns the removed entry, or None if there was none."""
    data = read_reservations()
    removed = data.pop(str(port), None)
    if removed is not None:
        write_reservations(data)
    return removed


def _normalized_identity(value):
    if not value:
        return ""
    return re.sub(r"[^a-z0-9]+", "_", str(value).strip().lower()).strip("_")


def _is_collision(reserved_project, actual_project):
    """A collision is a reserved port held by a DIFFERENT project than expected."""
    if not reserved_project or not actual_project:
        return False
    return _normalized_identity(reserved_project) != _normalized_identity(actual_project)


# ----------------------------------------------------------------------------
# The surgical kill — exactly one thing, never the harbor
# ----------------------------------------------------------------------------
def current_user():
    return getpass.getuser() or os.environ.get("USER", "")


def kill_pid(pid, force=False, timeout=2.5):
    """
    Safely terminate ONE pid: SIGTERM, wait, then SIGKILL if needed.
    Refuses to touch processes you don't own, and refuses to kill itself.
    Returns (ok, message).
    """
    if pid == os.getpid():
        return False, "refusing to kill Harbormaster itself"

    owner = None
    owner_uid = None
    name = None
    if psutil is not None:
        try:
            p = psutil.Process(pid)
            owner = p.username()
            name = p.name()
        except psutil.NoSuchProcess:
            return False, "process already gone"
        except Exception:
            pass

    if owner_uid is None:
        owner_uid, _ = _lsof_process_metadata(pid)
    if owner is None and owner_uid is not None:
        try:
            owner = pwd.getpwuid(owner_uid).pw_name
        except (KeyError, OSError):
            pass

    me = current_user()
    if owner_uid is not None and owner_uid != os.getuid() and not force:
        return False, f"owned by uid {owner_uid}, not you — use --force to override"
    if owner and me and owner != me and not force:
        return False, f"owned by '{owner}', not you ('{me}') — use --force to override"
    if owner_uid is None and owner is None and not force:
        return False, "could not verify process ownership — refusing without --force"

    # SIGTERM first (graceful)
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return True, "already gone"
    except PermissionError:
        return False, "permission denied (try with sudo, or --force)"

    deadline = time.time() + timeout
    while time.time() < deadline:
        if not _pid_alive(pid):
            return True, "stopped (SIGTERM)"
        time.sleep(0.15)

    # Still alive → SIGKILL
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        return True, "stopped (SIGTERM)"
    except PermissionError:
        return False, "permission denied on SIGKILL"

    time.sleep(0.3)
    if _pid_alive(pid):
        return False, "still alive after SIGKILL (?)"
    return True, "stopped (SIGKILL)"


def _pid_alive(pid):
    if psutil is not None:
        try:
            p = psutil.Process(pid)
            return p.is_running() and p.status() != psutil.STATUS_ZOMBIE
        except psutil.NoSuchProcess:
            return False
        except Exception:
            pass
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def free_port(port, assume_yes=False, force=False, via="cli"):
    """
    Free a single port: find who holds it, show what will die, confirm, kill,
    and log it. Returns (ok, list_of_results).
    """
    holders = find_on_port(port)
    if not holders:
        return False, [{"msg": f"nothing is listening on port {port} — already free ✓"}]
    if len(holders) != 1:
        return False, [{
            "msg": (
                f"port {port} has {len(holders)} process holders — refusing a broad stop; "
                "inspect each PID separately"
            )
        }]

    results = []
    for h in holders:
        if h["is_self"]:
            results.append({"port": port, "pid": h["pid"],
                            "ok": False, "msg": "that's Harbormaster's own dashboard — left alone"})
            continue

        if h["kind"] == "system" and not force:
            if via == "cli":
                print(C.paint(f"  ⚠ '{h['command']}' looks like a system process. "
                              f"Re-run with --force if you really mean it.", C.YELLOW))
            results.append({"port": port, "pid": h["pid"], "ok": False,
                            "msg": "system process, not killed"})
            continue

        if not assume_yes and via == "cli":
            _print_kill_preview(h)
            ans = input(C.paint("  Free this port? [y/N] ", C.BOLD)).strip().lower()
            if ans not in ("y", "yes"):
                results.append({"port": port, "pid": h["pid"], "ok": False, "msg": "skipped"})
                continue

        ok, msg = kill_pid(h["pid"], force=force)
        if ok:
            log_event({"action": "kill", "via": via, "port": port, "pid": h["pid"],
                       "command": h["command"], "project": h["project"], "cwd": h["cwd"],
                       "result": msg})
        results.append({"port": port, "pid": h["pid"], "ok": ok, "msg": msg,
                        "project": h["project"], "command": h["command"]})
    return any(r.get("ok") for r in results), results


def _print_kill_preview(h):
    badge = C.c256(f" {h['project']} ", badge_256(h["project"]))
    print()
    print(f"  {C.paint('About to free', C.BOLD)} {C.paint(':' + str(h['port']), C.CYAN, C.BOLD)}")
    print(f"    project   {badge}")
    print(f"    command   {h['command']}   {C.paint('(pid ' + str(h['pid']) + ')', C.DIM)}")
    if h.get("cmdline") and h["cmdline"] != h["command"]:
        cl = h["cmdline"]
        print(f"    full      {C.paint(cl[:100] + ('…' if len(cl) > 100 else ''), C.DIM)}")
    if h.get("cwd"):
        print(f"    cwd       {C.paint(h['cwd'], C.DIM)}")
    print(f"    uptime    {h['age_h']}")
    if h.get("collision"):
        print(f"    {C.paint('⚠ collision', C.YELLOW, C.BOLD)} "
              f"{C.paint('reserved for ' + str(h.get('reserved_project')), C.YELLOW)}")


# ----------------------------------------------------------------------------
# CLI rendering
# ----------------------------------------------------------------------------
BANNER = r"""
  ⚓ Harbormaster — the anti-killall
"""


def cmd_list(args):
    listeners = list_listeners()
    snapshot_and_diff(listeners, log_appears=True)  # keep the flight recorder warm

    if args.project:
        q = args.project.lower()
        listeners = [l for l in listeners if q in (l["project"] or "").lower()
                     or (l["project_root"] and q in l["project_root"].lower())]

    if args.dev:
        listeners = [l for l in listeners if l["kind"] == "dev"]

    if not listeners:
        print(C.paint("  No listening ports found.", C.DIM))
        return

    print(C.paint(BANNER, C.CYAN, C.BOLD))
    # Header
    print("  " + C.paint(
        f"{'PORT':<7}{'PROJECT':<22}{'COMMAND':<16}{'PID':<8}{'UPTIME':<9}{'WHERE'}",
        C.DIM))
    print("  " + C.paint("─" * 86, C.DIM))

    last_project = None
    for l in listeners:
        # group separators by project for dev servers
        proj = l["project"]
        badge = C.c256(f"{proj[:20]:<20}", badge_256(proj))
        port_str = C.paint(f"{l['port']:<7}", C.CYAN, C.BOLD) if l["kind"] == "dev" \
            else C.paint(f"{l['port']:<7}", C.DIM)
        cmd = l["command"][:15]
        where = l["cwd"] or (l["addrs"][0] if l["addrs"] else "")
        home = str(Path.home())
        if where and where.startswith(home):
            where = "~" + where[len(home):]
        row = f"  {port_str}{badge}  {cmd:<14}  {str(l['pid']):<6}  {l['age_h']:<8} "
        tag = ""
        if l["is_self"]:
            tag = C.paint("  ⚓ harbormaster", C.GREEN)
        elif l["kind"] == "system":
            tag = C.paint("  · system", C.DIM)
        if l.get("collision"):
            tag += C.paint(f"  ⚠ collision (expected {l['reserved_project']})", C.YELLOW, C.BOLD)
        line = row + C.paint(where, C.DIM) + tag
        print(line if l["kind"] == "dev" else C.paint(line, C.DIM) if False else line)

    print()
    n_dev = sum(1 for l in listeners if l["kind"] == "dev")
    n_proj = len(set(l["project"] for l in listeners if l["kind"] == "dev"))
    n_collide = sum(1 for l in listeners if l.get("collision"))
    summary = f"{len(listeners)} ports · {n_dev} dev servers · {n_proj} projects"
    if n_collide:
        print("  " + C.paint(summary, C.DIM)
              + C.paint(f" · {n_collide} collision{'s' if n_collide != 1 else ''} ⚠", C.YELLOW, C.BOLD))
        print("  " + C.paint("free one with:  ports free <port>   ·   "
                             "review reservations:  ports reservations", C.DIM))
    else:
        print("  " + C.paint(summary + "   free one with:  ports free <port>", C.DIM))


def cmd_who(args):
    holders = find_on_port(args.port)
    if getattr(args, "json", False):
        # Machine-readable for walkthrough gates, agents, scripts.
        def holder_payload(h):
            item = {
                "pid": h["pid"],
                "command": h["command"],
                "project": h.get("project"),
                "kind": h.get("kind"),
                "addrs": h.get("addrs") or [],
                "age_h": h.get("age_h"),
                "is_self": bool(h.get("is_self")),
                "collision": bool(h.get("collision")),
                "reserved_project": h.get("reserved_project"),
            }
            if not getattr(args, "safe", False):
                item.update({
                    "cmdline": h.get("cmdline"),
                    "cwd": h.get("cwd"),
                    "project_root": h.get("project_root"),
                    "launchd_label": h.get("launchd_label"),
                })
            return item

        payload = {
            "port": args.port,
            "free": len(holders) == 0,
            "holders": [holder_payload(h) for h in holders],
        }
        print(json.dumps(payload, indent=2))
        return

    if not holders:
        print(C.paint(f"  Nothing is listening on port {args.port}. It's free ✓", C.GREEN))
        return
    for h in holders:
        badge = C.c256(f" {h['project']} ", badge_256(h["project"]))
        print()
        print(f"  {C.paint(':' + str(h['port']), C.CYAN, C.BOLD)}  {badge}"
              f"  {'⚓ harbormaster' if h['is_self'] else ''}")
        print(f"    pid       {h['pid']}")
        print(f"    command   {h['command']}")
        print(f"    full cmd  {C.paint(h['cmdline'], C.DIM)}")
        print(f"    cwd       {h.get('cwd') or '—'}")
        print(f"    project   {h['project']}   {C.paint(h.get('project_root') or '', C.DIM)}")
        print(f"    uptime    {h['age_h']}")
        print(f"    addrs     {C.paint(', '.join(h['addrs']), C.DIM)}")
        print(f"    type      {h['kind']}")
    print()
    print(C.paint(f"  Free it with:  ports free {args.port}", C.DIM))


def cmd_free(args):
    ok, results = free_port(args.port, assume_yes=args.yes, force=args.force, via="cli")
    for r in results:
        if "msg" in r and "pid" not in r:
            print(C.paint(f"  {r['msg']}", C.GREEN if "free" in r["msg"] else C.YELLOW))
            continue
        icon = C.paint("✓", C.GREEN) if r.get("ok") else C.paint("·", C.YELLOW)
        proj = r.get("project", "")
        print(f"  {icon} :{r['port']}  {proj}  →  {r['msg']}")
    if ok:
        print()
        print(C.paint(f"  Port {args.port} is free. Logged to history "
                      f"(see: ports history).", C.DIM))


def cmd_project(args):
    args.dev = False
    args.project = args.name
    cmd_list(args)


def cmd_reserve(args):
    project = args.project
    note = args.note or ""
    # If no project given, infer it from whoever currently holds the port.
    if not project:
        holders = [h for h in find_on_port(args.port) if not h["is_self"]]
        if holders:
            project = holders[0]["project"]
            print(C.paint(f"  Inferred project from the current holder of :{args.port}.", C.DIM))
        else:
            print(C.paint(f"  Nothing is on :{args.port} right now — name the project to reserve it for:", C.YELLOW))
            print(C.paint(f"    ports reserve {args.port} <project>", C.DIM))
            return
    reserve_port(args.port, project, note)
    badge = C.c256(f" {project} ", badge_256(project))
    print()
    print(f"  {C.paint('Reserved', C.GREEN, C.BOLD)} {C.paint(':' + str(args.port), C.CYAN, C.BOLD)} "
          f"for {badge}")
    if note:
        print(f"    note   {C.paint(note, C.DIM)}")
    # Immediately flag if the live holder doesn't match what we just reserved.
    holders = [h for h in find_on_port(args.port) if not h["is_self"]]
    for h in holders:
        if _is_collision(project, h["project"]):
            print(C.paint(f"  ⚠ heads up: :{args.port} is currently held by '{h['project']}', "
                          f"not '{project}'.", C.YELLOW))
    print()


def cmd_unreserve(args):
    removed = unreserve_port(args.port)
    if removed is None:
        print(C.paint(f"  No reservation on :{args.port} — nothing to release.", C.DIM))
        return
    print(C.paint(f"  Released reservation on :{args.port} "
                  f"(was '{removed.get('project')}').", C.GREEN))


def cmd_reservations(args):
    data = read_reservations()
    if not data:
        print(C.paint("\n  No port reservations yet.", C.DIM))
        print(C.paint("  Claim one with:  ports reserve <port> <project>\n", C.DIM))
        return
    live = {l["port"]: l for l in list_listeners() if not l["is_self"]}
    print(C.paint("\n  ⚓ Harbormaster — port reservations\n", C.CYAN, C.BOLD))
    print("  " + C.paint(f"{'PORT':<7}{'RESERVED FOR':<22}{'STATUS'}", C.DIM))
    print("  " + C.paint("─" * 66, C.DIM))
    for port_str in sorted(data, key=lambda x: int(x) if x.isdigit() else 0):
        entry = data[port_str]
        proj = entry.get("project") or "—"
        note = entry.get("note") or ""
        badge = C.c256(f"{proj[:20]:<20}", badge_256(proj))
        try:
            port_int = int(port_str)
        except ValueError:
            port_int = None
        holder = live.get(port_int)
        if holder is None:
            status = C.paint("free (idle)", C.DIM)
        elif _is_collision(proj, holder["project"]):
            status = C.paint(f"⚠ collision — held by {holder['project']}", C.YELLOW, C.BOLD)
        else:
            status = C.paint("✓ in use by the right project", C.GREEN)
        port_disp = C.paint(f"{port_str:<7}", C.CYAN, C.BOLD)
        print(f"  {port_disp}{badge}  {status}")
        if note:
            print(f"  {'':<7}{C.paint(note, C.DIM)}")
    print()


def cmd_history(args):
    # When filtering to one port, pull a deeper slice so the timeline isn't empty
    # just because the port's events fell outside the default window.
    pull = max(args.limit * 8, 400) if getattr(args, "port", None) is not None else args.limit
    events = read_history(limit=pull)
    port_filter = getattr(args, "port", None)
    if port_filter is not None:
        events = [e for e in events if e.get("port") == port_filter][: args.limit]
    else:
        events = events[: args.limit]

    if not events:
        if port_filter is not None:
            print(C.paint(f"  No history for :{port_filter} yet.", C.DIM))
        else:
            print(C.paint("  No history yet. Kills and crashes will show up here.", C.DIM))
        return

    title = (
        f"flight recorder · :{port_filter}"
        if port_filter is not None
        else "flight recorder"
    )
    print(C.paint(f"\n  ⚓ Harbormaster — {title}\n", C.CYAN, C.BOLD))
    icons = {
        "kill": (C.RED, "✕ killed  "),
        "vanished": (C.YELLOW, "⚠ vanished"),
        "appeared": (C.GREEN, "+ appeared"),
    }
    for e in events:
        color, label = icons.get(e.get("action"), (C.DIM, e.get("action", "?")))
        clock = human_clock(e.get("ts", ""))
        proj = e.get("project") or "—"
        port = e.get("port")
        cmd = e.get("command") or ""
        via = e.get("via")
        extra = ""
        if e.get("action") == "vanished":
            extra = C.paint("  (crash or outside kill — not you)", C.DIM)
        elif via:
            extra = C.paint(f"  via {via}", C.DIM)
        print(f"  {C.paint(clock, C.DIM):<22}{C.paint(label, color)}  "
              f":{port}  {proj}  {C.paint(cmd, C.DIM)}{extra}")
    print()
    if port_filter is not None:
        print(C.paint(f"  Tip: ports who {port_filter}  ·  ports free {port_filter}", C.DIM))
        print()


def cmd_watch(args):
    """Live terminal view — reprint the harbor every interval (Ctrl-C to stop)."""
    interval = max(0.5, float(getattr(args, "interval", 1.0) or 1.0))
    print(C.paint(BANNER, C.CYAN, C.BOLD))
    print(C.paint(f"  watching every {interval:g}s · Ctrl-C to stop\n", C.DIM))
    try:
        while True:
            # Clear screen + home cursor (works in modern terminals; plain reprint if not).
            sys.stdout.write("\033[H\033[2J")
            ns = argparse.Namespace(
                dev=bool(getattr(args, "dev", False)),
                project=getattr(args, "project", None),
            )
            cmd_list(ns)
            print(C.paint(f"  ↻ refresh {interval:g}s · Ctrl-C to stop", C.DIM))
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n  ⚓ watch stopped.")


def cmd_killall(args):
    """Easter egg: the reflex this whole tool exists to retire."""
    print(C.paint("\n  ⚓ Nope. 😄\n", C.YELLOW, C.BOLD))
    print("  `killall` is literally the reflex Harbormaster exists to retire.")
    print("  It's how you nuke the dev servers you actually cared about.\n")
    listeners = [l for l in list_listeners() if l["kind"] == "dev"]
    if listeners:
        print(C.paint("  Here's what you'd have wiped out:", C.DIM))
        for l in listeners:
            badge = C.c256(f" {l['project']} ", badge_256(l["project"]))
            print(f"    :{C.paint(str(l['port']), C.CYAN)}  {badge}  {l['command']}")
        print()
        print("  Free just the ONE you meant instead:")
        print(C.paint(f"    ports free <port>", C.BOLD))
    else:
        print(C.paint("  (Nothing dev-ish is even running right now.)", C.DIM))
    print()


def cmd_doctor(args):
    print(C.paint("\n  ⚓ Harbormaster — doctor\n", C.CYAN, C.BOLD))
    ok = True

    # psutil
    if psutil is not None:
        print(f"  {C.paint('✓', C.GREEN)} psutil installed ({psutil.__version__})")
    else:
        print(f"  {C.paint('·', C.YELLOW)} psutil not installed (optional on macOS)")

    # flask
    try:
        import flask  # noqa
        print(f"  {C.paint('✓', C.GREEN)} flask installed (dashboard ready)")
    except ImportError:
        print(f"  {C.paint('·', C.YELLOW)} flask missing  →  pip3 install flask  (only needed for `ports serve`)")

    # lsof
    try:
        subprocess.run(["lsof", "-v"], capture_output=True, timeout=5, check=False)
        print(f"  {C.paint('✓', C.GREEN)} lsof available (fast enumeration)")
    except Exception:
        if psutil is None:
            ok = False
            print(f"  {C.paint('✕', C.RED)} lsof and psutil unavailable — install psutil")
        else:
            print(f"  {C.paint('·', C.YELLOW)} lsof not found — using psutil enumeration")

    # data dir
    _ensure_app_dir()
    print(f"  {C.paint('✓', C.GREEN)} data dir {APP_DIR}")

    # can we see ports?
    n = len(list_listeners())
    print(f"  {C.paint('✓', C.GREEN)} currently see {n} listening port(s)")

    print()
    print(C.paint("  All set." if ok else "  Install the missing bits above, then re-run `ports doctor`.",
                  C.GREEN if ok else C.YELLOW))
    print()


def cmd_serve(args):
    try:
        from flask import Flask, jsonify, request
    except ImportError:
        print(C.paint("  The dashboard needs Flask:", C.YELLOW))
        print("    pip3 install flask")
        sys.exit(1)

    app = build_dashboard_app(Flask, jsonify, request)
    host = args.host
    port = args.port
    url = f"http://{('localhost' if host in ('0.0.0.0', '127.0.0.1') else host)}:{port}"
    print(C.paint(BANNER, C.CYAN, C.BOLD))
    print(f"  Dashboard live at  {C.paint(url, C.CYAN, C.BOLD)}")
    print(C.paint("  Auto-refreshing every 2s · click a port to free it · Ctrl-C to stop\n", C.DIM))
    if not args.no_browser:
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception:
            pass
    # Quiet werkzeug logs
    import logging
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    app.run(host=host, port=port, debug=False, threaded=True)


# ----------------------------------------------------------------------------
# Dashboard (Flask) — defined as a builder so Flask import stays optional
# ----------------------------------------------------------------------------
def build_dashboard_app(Flask, jsonify, request):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return DASHBOARD_HTML

    @app.route("/api/ports")
    def api_ports():
        listeners = list_listeners()
        snapshot_and_diff(listeners, log_appears=True)
        for l in listeners:
            l["color"] = badge_hex(l["project"])
            home = str(Path.home())
            cwd = l.get("cwd") or ""
            l["cwd_short"] = ("~" + cwd[len(home):]) if cwd.startswith(home) else cwd
        return jsonify({"ports": listeners, "ts": now_iso(),
                        "stats": _stats(listeners)})

    @app.route("/api/kill", methods=["POST"])
    def api_kill():
        data = request.get_json(force=True, silent=True) or {}
        port = data.get("port")
        force = bool(data.get("force"))
        if port is None:
            return jsonify({"ok": False, "error": "no port given"}), 400
        ok, results = free_port(int(port), assume_yes=True, force=force, via="dashboard")
        return jsonify({"ok": ok, "results": results})

    @app.route("/api/history")
    def api_history():
        return jsonify({"events": read_history(limit=120)})

    return app


def _stats(listeners):
    killed_today = 0
    today = datetime.now().date().isoformat()
    for e in read_history(limit=400):
        if e.get("action") == "kill" and e.get("ts", "").startswith(today):
            killed_today += 1
    return {
        "ports": len(listeners),
        "dev": sum(1 for l in listeners if l["kind"] == "dev"),
        "projects": len(set(l["project"] for l in listeners if l["kind"] == "dev")),
        "killed_today": killed_today,
        "collisions": sum(1 for l in listeners if l.get("collision")),
    }


# The dashboard is a single static page; all data arrives via /api/* fetches,
# so there is zero server-side templating (and no brace-escaping headaches).
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>⚓ Harbormaster</title>
<style>
  :root{
    --bg:#0a0e14; --panel:#111722; --panel2:#0d131c; --line:#1d2735;
    --text:#e6edf3; --dim:#8b9bb0; --cyan:#34d6e6; --green:#5ad17a;
    --amber:#ffb02e; --red:#ff5470; --accent:#34d6e6;
  }
  *{box-sizing:border-box}
  body{margin:0;background:radial-gradient(1200px 600px at 70% -10%,#13202e 0%,var(--bg) 55%);
    color:var(--text);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    min-height:100vh;-webkit-font-smoothing:antialiased}
  header{display:flex;align-items:center;gap:18px;padding:20px 26px;border-bottom:1px solid var(--line);
    position:sticky;top:0;background:rgba(10,14,20,.82);backdrop-filter:blur(10px);z-index:10}
  .brand{font-size:18px;font-weight:700;letter-spacing:.3px;white-space:nowrap}
  .brand small{color:var(--dim);font-weight:500;font-size:12px;margin-left:8px}
  .stats{display:flex;gap:22px;margin-left:8px;flex-wrap:wrap}
  .stat{display:flex;flex-direction:column;line-height:1.1}
  .stat b{font-size:20px;font-variant-numeric:tabular-nums}
  .stat span{font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--dim);margin-top:3px}
  .spacer{flex:1}
  .live{display:flex;align-items:center;gap:7px;color:var(--dim);font-size:12px}
  .dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 0 0 rgba(90,209,122,.6);animation:pulse 2s infinite}
  @keyframes pulse{0%{box-shadow:0 0 0 0 rgba(90,209,122,.5)}70%{box-shadow:0 0 0 7px rgba(90,209,122,0)}100%{box-shadow:0 0 0 0 rgba(90,209,122,0)}}
  .btn{border:1px solid var(--line);background:var(--panel);color:var(--text);padding:8px 14px;border-radius:9px;
    cursor:pointer;font-size:13px;transition:.15s}
  .btn:hover{border-color:var(--cyan);color:var(--cyan)}
  .wrap{padding:22px 26px 80px;max-width:1180px;margin:0 auto}
  .proj{margin-bottom:26px}
  .proj-head{display:flex;align-items:center;gap:10px;margin:0 2px 10px}
  .proj-badge{width:10px;height:10px;border-radius:3px}
  .proj-name{font-weight:650;letter-spacing:.2px}
  .proj-path{color:var(--dim);font-size:12px}
  .proj-count{color:var(--dim);font-size:12px;margin-left:auto}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
  .card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-radius:13px;padding:15px 16px;position:relative;overflow:hidden;transition:.18s}
  .card:hover{border-color:#2b3a4e;transform:translateY(-1px)}
  .card .rail{position:absolute;left:0;top:0;bottom:0;width:3px}
  .card.system{opacity:.62}
  .port{font-size:26px;font-weight:750;letter-spacing:.5px;font-variant-numeric:tabular-nums;
    display:flex;align-items:baseline;gap:7px}
  .port .colon{color:var(--dim);font-weight:500}
  .cmd{margin-top:2px;color:var(--text)}
  .meta{margin-top:9px;color:var(--dim);font-size:12px;display:flex;flex-wrap:wrap;gap:4px 12px}
  .meta b{color:#aeb9c7;font-weight:600}
  .row2{display:flex;align-items:center;justify-content:space-between;margin-top:13px;gap:10px}
  .tag{font-size:10px;text-transform:uppercase;letter-spacing:.7px;padding:3px 8px;border-radius:20px;border:1px solid var(--line);color:var(--dim)}
  .tag.dev{color:var(--green);border-color:rgba(90,209,122,.35)}
  .tag.self{color:var(--cyan);border-color:rgba(52,214,230,.4)}
  .card.collision{border-color:rgba(255,176,46,.55)}
  .collide{margin-top:9px;font-size:12px;color:var(--amber);background:rgba(255,176,46,.08);
    border:1px solid rgba(255,176,46,.3);border-radius:8px;padding:6px 9px;display:flex;gap:6px;align-items:flex-start}
  .acts{display:flex;gap:8px;align-items:center}
  .kill{border:1px solid rgba(255,84,112,.35);background:rgba(255,84,112,.08);color:var(--red);
    padding:7px 13px;border-radius:9px;cursor:pointer;font-size:12px;font-weight:600;transition:.15s}
  .kill:hover{background:var(--red);color:#fff;border-color:var(--red)}
  .kill:disabled{opacity:.4;cursor:not-allowed}
  .open{border:1px solid rgba(52,214,230,.35);background:rgba(52,214,230,.08);color:var(--cyan);
    padding:7px 12px;border-radius:9px;cursor:pointer;font-size:12px;font-weight:600;transition:.15s}
  .open:hover{background:var(--cyan);color:#04222a;border-color:var(--cyan)}
  .port.clickable{cursor:pointer}
  .port.clickable:hover .num{text-decoration:underline;text-underline-offset:3px}
  .empty{text-align:center;color:var(--dim);padding:70px 0}
  .empty .big{font-size:44px;margin-bottom:10px}
  /* History drawer */
  .fab{position:fixed;right:22px;bottom:22px;z-index:20}
  .drawer{position:fixed;top:0;right:-460px;width:440px;max-width:92vw;height:100vh;background:var(--panel2);
    border-left:1px solid var(--line);box-shadow:-20px 0 60px rgba(0,0,0,.5);transition:right .25s ease;z-index:30;
    display:flex;flex-direction:column}
  .drawer.open{right:0}
  .drawer h3{margin:0;padding:18px 20px;border-bottom:1px solid var(--line);font-size:14px;display:flex;align-items:center;gap:8px}
  .drawer .close{margin-left:auto;cursor:pointer;color:var(--dim);font-size:18px;background:none;border:none}
  .events{overflow:auto;padding:10px 14px}
  .ev{display:flex;gap:11px;padding:9px 6px;border-bottom:1px solid rgba(29,39,53,.6);font-size:12.5px}
  .ev .ico{width:18px;flex:none;text-align:center}
  .ev .body{flex:1}
  .ev .when{color:var(--dim);font-size:11px}
  .ev.kill .ico{color:var(--red)} .ev.vanished .ico{color:var(--amber)} .ev.appeared .ico{color:var(--green)}
  .ev .note{color:var(--amber);font-size:11px}
  /* Modal */
  .scrim{position:fixed;inset:0;background:rgba(4,7,11,.66);backdrop-filter:blur(2px);z-index:40;display:none;align-items:center;justify-content:center}
  .scrim.open{display:flex}
  .modal{background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:24px;width:420px;max-width:92vw}
  .modal h2{margin:0 0 4px;font-size:17px}
  .modal .sub{color:var(--dim);font-size:13px;margin-bottom:16px}
  .modal .det{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:13px 15px;font-size:13px;margin-bottom:18px}
  .modal .det div{display:flex;justify-content:space-between;gap:14px;padding:3px 0}
  .modal .det span{color:var(--dim)}
  .modal .actions{display:flex;gap:10px;justify-content:flex-end}
  .toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:var(--panel);
    border:1px solid var(--line);border-radius:11px;padding:12px 18px;z-index:60;opacity:0;transition:.25s;pointer-events:none}
  .toast.show{opacity:1;transform:translate(-50%,-6px)}
  .toast.ok{border-color:rgba(90,209,122,.5)} .toast.err{border-color:rgba(255,84,112,.5)}
  code{background:#0c1219;padding:2px 6px;border-radius:5px;color:var(--cyan);font-size:12px}
</style>
</head>
<body>
<header>
  <div class="brand">⚓ Harbormaster <small>the anti-killall</small></div>
  <div class="stats" id="stats"></div>
  <div class="spacer"></div>
  <div class="live"><span class="dot"></span> live · refreshing</div>
  <button class="btn" onclick="toggleDrawer()">🛟 History</button>
</header>

<div class="wrap" id="wrap">
  <div class="empty"><div class="big">⚓</div>scanning the harbor…</div>
</div>

<button class="btn fab" onclick="toggleDrawer()">🛟 Flight recorder</button>

<div class="drawer" id="drawer">
  <h3>🛟 Flight recorder
    <button class="close" onclick="toggleDrawer()">✕</button>
  </h3>
  <div class="events" id="events"></div>
</div>

<div class="scrim" id="scrim">
  <div class="modal">
    <h2>Free this port?</h2>
    <div class="sub">Harbormaster will stop <b>exactly this one</b> process. Nothing else in the harbor is touched.</div>
    <div class="det" id="modalDet"></div>
    <div class="actions">
      <button class="btn" onclick="closeModal()">Cancel</button>
      <button class="kill" id="confirmKill" onclick="confirmKill()">Free port</button>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
let PENDING = null;
let lastPorts = [];

function h(s){return (s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

async function refresh(){
  try{
    const r = await fetch('/api/ports'); const d = await r.json();
    lastPorts = d.ports; render(d);
  }catch(e){ /* keep last view */ }
}

function render(d){
  // stats
  const s = d.stats;
  document.getElementById('stats').innerHTML = `
    <div class="stat"><b>${s.ports}</b><span>ports</span></div>
    <div class="stat"><b style="color:var(--green)">${s.dev}</b><span>dev servers</span></div>
    <div class="stat"><b>${s.projects}</b><span>projects</span></div>
    <div class="stat"><b style="color:var(--red)">${s.killed_today}</b><span>freed today</span></div>
    ${s.collisions?`<div class="stat"><b style="color:var(--amber)">${s.collisions}</b><span>collisions</span></div>`:''}`;

  const wrap = document.getElementById('wrap');
  if(!d.ports.length){
    wrap.innerHTML = '<div class="empty"><div class="big">🌊</div>Calm harbor — nothing is listening right now.</div>';
    return;
  }
  // group by project
  const groups = {};
  for(const p of d.ports){ (groups[p.project] ||= []).push(p); }
  // dev projects first
  const order = Object.keys(groups).sort((a,b)=>{
    const ad = groups[a].some(x=>x.kind==='dev')?0:1, bd = groups[b].some(x=>x.kind==='dev')?0:1;
    return ad-bd || a.localeCompare(b);
  });
  let html='';
  for(const proj of order){
    const items = groups[proj].sort((a,b)=>a.port-b.port);
    const color = items[0].color;
    const root = items[0].project_root || '';
    html += `<div class="proj">
      <div class="proj-head">
        <span class="proj-badge" style="background:${color}"></span>
        <span class="proj-name">${h(proj)}</span>
        <span class="proj-path">${h(root)}</span>
        <span class="proj-count">${items.length} port${items.length>1?'s':''}</span>
      </div><div class="grid">`;
    for(const p of items){ html += card(p); }
    html += `</div></div>`;
  }
  wrap.innerHTML = html;
}

function card(p){
  const tag = p.is_self ? '<span class="tag self">⚓ harbormaster</span>'
            : p.kind==='dev' ? '<span class="tag dev">dev server</span>'
            : '<span class="tag">system</span>';
  const killBtn = p.is_self
    ? '<button class="kill" disabled title="that is me!">protected</button>'
    : `<button class="kill" onclick='askKill(${p.port})'>Free :${p.port}</button>`;
  const openBtn = `<button class="open" onclick='openPort(${p.port})' title="Open http://localhost:${p.port}">↗ Open</button>`;
  const collide = p.collision
    ? `<div class="collide"><span>⚠</span><span>collision — reserved for <b>${h(p.reserved_project)}</b>, held by <b>${h(p.project)}</b></span></div>`
    : '';
  return `<div class="card ${p.kind}${p.collision?' collision':''}">
    <div class="rail" style="background:${p.color}"></div>
    <div class="port clickable" onclick='openPort(${p.port})' title="Open http://localhost:${p.port}"><span class="colon">:</span><span class="num">${p.port}</span></div>
    <div class="cmd">${h(p.command)}</div>
    <div class="meta">
      <span><b>pid</b> ${p.pid}</span>
      <span><b>up</b> ${h(p.age_h)}</span>
      ${p.cwd_short?`<span><b>cwd</b> ${h(p.cwd_short)}</span>`:''}
    </div>
    ${collide}
    <div class="row2">${tag}<div class="acts">${openBtn}${killBtn}</div></div>
  </div>`;
}

function openPort(port){
  const url = 'http://localhost:'+port;
  const w = window.open(url, '_blank');
  if(w){ toast('Opening '+url+' …','ok'); }
  else { toast('Popup blocked — allow popups to open :'+port,'err'); }
}

function askKill(port){
  const p = lastPorts.find(x=>x.port===port); if(!p) return;
  PENDING = port;
  document.getElementById('modalDet').innerHTML = `
    <div><span>port</span><b>:${p.port}</b></div>
    <div><span>project</span><b>${h(p.project)}</b></div>
    <div><span>command</span><b>${h(p.command)}</b></div>
    <div><span>pid</span><b>${p.pid}</b></div>
    <div><span>uptime</span><b>${h(p.age_h)}</b></div>
    ${p.cwd_short?`<div><span>cwd</span><b>${h(p.cwd_short)}</b></div>`:''}`;
  document.getElementById('scrim').classList.add('open');
}
function closeModal(){ document.getElementById('scrim').classList.remove('open'); PENDING=null; }

async function confirmKill(){
  if(PENDING==null) return;
  const port = PENDING; const btn=document.getElementById('confirmKill');
  btn.disabled=true; btn.textContent='Freeing…';
  try{
    const r = await fetch('/api/kill',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({port})});
    const d = await r.json();
    const msg = (d.results&&d.results[0]&&d.results[0].msg) || (d.ok?'freed':'could not free');
    toast(d.ok?`Port :${port} freed — ${msg}`:`:${port} — ${msg}`, d.ok?'ok':'err');
  }catch(e){ toast('request failed','err'); }
  btn.disabled=false; btn.textContent='Free port';
  closeModal(); refresh(); loadHistory();
}

function toast(msg,kind){
  const t=document.getElementById('toast'); t.textContent=msg; t.className='toast show '+(kind||'');
  setTimeout(()=>{t.className='toast '+(kind||'');},3200);
}

function toggleDrawer(){
  const d=document.getElementById('drawer'); d.classList.toggle('open');
  if(d.classList.contains('open')) loadHistory();
}
async function loadHistory(){
  try{
    const r=await fetch('/api/history'); const d=await r.json();
    const icons={kill:'✕',vanished:'⚠',appeared:'+'};
    document.getElementById('events').innerHTML = d.events.map(e=>{
      const when=new Date(e.ts).toLocaleTimeString([], {hour:'numeric',minute:'2-digit'});
      const label={kill:'killed',vanished:'vanished',appeared:'appeared'}[e.action]||e.action;
      return `<div class="ev ${e.action}">
        <div class="ico">${icons[e.action]||'·'}</div>
        <div class="body">
          <div><b>:${e.port}</b> ${h(e.project||'')} <span style="color:var(--dim)">${h(e.command||'')}</span></div>
          <div class="when">${label} · ${when}${e.via?(' · via '+e.via):''}</div>
          ${e.action==='vanished'?'<div class="note">disappeared on its own — not you</div>':''}
        </div></div>`;
    }).join('') || '<div style="color:var(--dim);padding:20px">No events yet.</div>';
  }catch(e){}
}

document.addEventListener('keydown',e=>{ if(e.key==='Escape'){closeModal();} });
refresh(); setInterval(refresh, 2000);
</script>
</body>
</html>
"""


# ----------------------------------------------------------------------------
# Argument parsing
# ----------------------------------------------------------------------------
def build_parser():
    p = argparse.ArgumentParser(
        prog="ports",
        description="⚓ Harbormaster — see every listening port, kill exactly one, never the harbor.",
    )
    sub = p.add_subparsers(dest="command")

    lp = sub.add_parser("list", aliases=["ls"], help="list all listening ports (default)")
    lp.add_argument("--dev", action="store_true", help="only show dev servers")
    lp.add_argument("--project", help="filter to a project name/path")
    lp.set_defaults(func=cmd_list)

    wp = sub.add_parser("who", help="who is holding a port?")
    wp.add_argument("port", type=int)
    wp.add_argument("--json", action="store_true", help="machine-readable JSON (for scripts/agents)")
    wp.add_argument("--safe", action="store_true", help="omit command lines and filesystem paths from JSON")
    wp.set_defaults(func=cmd_who)

    fp = sub.add_parser("free", aliases=["kill"], help="free ONE port (surgical, never killall)")
    fp.add_argument("port", type=int)
    fp.add_argument("-y", "--yes", action="store_true", help="skip the confirm prompt")
    fp.add_argument("--force", action="store_true", help="override owner/system guards")
    fp.set_defaults(func=cmd_free)

    pp = sub.add_parser("project", help="show all ports owned by a project")
    pp.add_argument("name")
    pp.set_defaults(func=cmd_project)

    rp = sub.add_parser("reserve", help="claim a port for a project (flags future collisions)")
    rp.add_argument("port", type=int)
    rp.add_argument("project", nargs="?", help="project name (default: the current holder's project)")
    rp.add_argument("--note", help="optional note shown alongside the reservation")
    rp.set_defaults(func=cmd_reserve)

    up = sub.add_parser("unreserve", aliases=["release"], help="release a port reservation")
    up.add_argument("port", type=int)
    up.set_defaults(func=cmd_unreserve)

    rsp = sub.add_parser("reservations", aliases=["reserved"], help="list reservations + collision status")
    rsp.set_defaults(func=cmd_reservations)

    hp = sub.add_parser("history", aliases=["log"], help="flight recorder: kills + mysterious deaths")
    hp.add_argument("port", nargs="?", type=int, default=None,
                    help="optional: only show events for this port")
    hp.add_argument("--limit", type=int, default=40)
    hp.set_defaults(func=cmd_history)

    wtp = sub.add_parser("watch", help="live terminal view of the harbor (Ctrl-C to stop)")
    wtp.add_argument("--interval", type=float, default=1.0, help="refresh seconds (default 1)")
    wtp.add_argument("--dev", action="store_true", help="only show dev servers")
    wtp.add_argument("--project", help="filter to a project name/path")
    wtp.set_defaults(func=cmd_watch)

    sp = sub.add_parser("serve", aliases=["dashboard", "ui"], help="launch the live web dashboard")
    sp.add_argument("--port", type=int, default=DEFAULT_DASH_PORT)
    sp.add_argument("--host", default="127.0.0.1")
    sp.add_argument("--no-browser", action="store_true", help="don't auto-open the browser")
    sp.set_defaults(func=cmd_serve)

    dp = sub.add_parser("doctor", help="check your setup")
    dp.set_defaults(func=cmd_doctor)

    kp = sub.add_parser("killall", help=argparse.SUPPRESS)  # easter egg
    kp.set_defaults(func=cmd_killall)

    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()

    args = parser.parse_args(argv)

    # default command = list
    if not getattr(args, "command", None):
        ns = argparse.Namespace(dev=False, project=None)
        cmd_list(ns)
        return

    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  ⚓ stopped.")
