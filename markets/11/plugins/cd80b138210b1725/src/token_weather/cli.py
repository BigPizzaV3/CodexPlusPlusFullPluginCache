"""Local helpers for the Skills-only edition. No hooks, MCP or live control."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

from .checkpoints import Workflow
from .storage import WeatherError, atomic_json, atomic_write, read_json, identifier
from .privacy import read_selected_file, validate_notes, public_replay, check_exports
from .log_projection import project_replay


def parser():
    p = argparse.ArgumentParser(prog="token-weather", description="Local weather, recorded-event replay and checkpoints")
    p.add_argument("--workspace", type=Path, default=Path.cwd())
    p.add_argument("--workflow", default="default")
    p.add_argument("--thread-id", default=os.environ.get("CODEX_THREAD_ID"))
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("weather", "weather-serve"):
        cmd = sub.add_parser(name)
        source = cmd.add_mutually_exclusive_group()
        source.add_argument("--transcript", type=Path)
        source.add_argument("--events", type=Path)
        cmd.add_argument("--compact-limit", type=int)
        cmd.add_argument("--max-age", type=float, default=120)
        cmd.add_argument("--cache-history", action="store_true", help="Explicitly save numeric history locally")
        cmd.add_argument("--read-config", action="store_true", help="Read only supported local reference fields")
        if name == "weather":
            cmd.add_argument("--json", action="store_true")
            cmd.add_argument("--compact", action="store_true")
            cmd.add_argument("--html", type=Path)
            cmd.add_argument("--output", type=Path)
        else:
            cmd.add_argument("--port", type=int, default=0)
    service = sub.add_parser("weather-service").add_subparsers(dest="service_action", required=True)
    for name in ("start", "restart"):
        cmd = service.add_parser(name)
        cmd.add_argument("--port", type=int, default=0)
        source = cmd.add_mutually_exclusive_group()
        source.add_argument("--transcript", type=Path)
        source.add_argument("--events", type=Path)
        cmd.add_argument("--compact-limit", type=int)
        cmd.add_argument("--max-age", type=float, default=120)
        cmd.add_argument("--poll-interval", type=float, default=2)
    for name in ("status", "stop", "list"):
        service.add_parser(name)
    service.add_parser("_run", help=argparse.SUPPRESS).add_argument("--instance-id", required=True)
    for name in ("replay-usage", "replay-control"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--input", type=Path, required=True)
        cmd.add_argument("--output", type=Path)
        cmd.add_argument("--include-local-metadata", action="store_true", help="Include private binding and lifecycle IDs in the local replay report")
    sub.add_parser("status").add_argument("--json", action="store_true")
    cmd = sub.add_parser("init")
    cmd.add_argument("--objective", required=True)
    cmd.add_argument("--policies", type=Path)
    cmd = sub.add_parser("checkpoint")
    cmd.add_argument("--update", type=Path, required=True)
    cmd.add_argument("--key", required=True)
    cmd.add_argument("--expected-generation", type=int)
    cmd.add_argument("--lease-epoch", type=int)
    sub.add_parser("prepare").add_argument("--verify-evidence", action="store_true", help="Read explicitly recorded workspace evidence files to check hashes")
    cmd = sub.add_parser("bootstrap")
    cmd.add_argument("--generation", type=int)
    cmd.add_argument("--ledger", type=int, nargs="*", default=[])
    cmd.add_argument("--json", action="store_true")
    cmd.add_argument("--verify-evidence", action="store_true")
    cmd.add_argument("--include-local-metadata", action="store_true")
    sub.add_parser("privacy-status")
    return p


def output(value):
    print(json.dumps(value, indent=2, ensure_ascii=False))


def require_thread(args):
    if not args.thread_id:
        raise WeatherError("Pass the exact current --thread-id or provide CODEX_THREAD_ID")
    return args.thread_id


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        workspace = args.workspace.resolve(strict=True)
        if args.command in ("replay-usage", "replay-control"):
            check_exports([args.output], workspace)
            from .runtime_usage import replay_usage
            from .runtime_control import replay_control
            control = args.command == "replay-control"
            recording = project_replay(read_selected_file(args.input), control=control)
            result = (replay_control if control else replay_usage)(recording)
            if not args.include_local_metadata:
                result = public_replay(result, control=control)
            if args.output:
                atomic_json(args.output, result)
            output(result)
            return 0
        if args.command == "weather-service":
            from .weather_service import run_service, service_list, service_status, start_service, stop_service
            if args.service_action == "list":
                output(minimal_service(service_list()))
                return 0
            thread = require_thread(args)
            if args.service_action == "_run":
                return run_service(workspace, thread, args.instance_id)
            if args.service_action == "status":
                output(minimal_service(service_status(thread)))
            elif args.service_action == "stop":
                output(minimal_service(stop_service(thread)))
            else:
                if args.service_action == "restart":
                    stop_service(thread)
                output(minimal_service(start_service(workspace, thread, port=args.port, transcript=args.transcript, events=args.events,
                                     compact_limit=args.compact_limit, max_age=args.max_age, poll_interval=args.poll_interval)))
            return 0
        if args.command in ("weather", "weather-serve"):
            if args.command == "weather":
                check_exports([args.output, args.html], workspace)
            from .weather import terminal_weather
            from .weather_sources import collect_weather
            from .weather_view import weather_html, weather_server
            thread = require_thread(args)
            def collect():
                return collect_weather(workspace, thread, transcript=args.transcript, events=args.events,
                                       compact_limit=args.compact_limit, max_age=args.max_age,
                                       persist_history=args.cache_history, read_config=args.read_config)
            if args.command == "weather-serve":
                collect()
                server = weather_server(collect, args.port)
                print(f"Token Weather: http://127.0.0.1:{server.server_port}", flush=True)
                try:
                    server.serve_forever()
                except KeyboardInterrupt:
                    pass
                finally:
                    server.server_close()
                return 0
            result = collect()
            if args.output:
                atomic_json(args.output, result)
            if args.html:
                atomic_write(args.html, weather_html(result).encode())
            if args.json:
                output(result)
            else:
                print(terminal_weather(result, args.compact))
            return 0
        if args.command == "privacy-status":
            from .weather_sources import codex_home
            # Report chosen locations; do not create or enumerate data folders.
            output({"weather_directory": str(Path(os.environ.get("TOKEN_WEATHER_SKILLS_DATA_DIR", codex_home() / "state/token-weather-skills")).expanduser().absolute()),
                    "checkpoint_directory": str(workspace / ".codex/handover-skills" / identifier(args.workflow)),
                    "automatic_deletion": False, "original_transcripts_deleted": False,
                    "guide": "docs/PRIVACY.md"})
            return 0
        workflow = Workflow(workspace, args.workflow)
        if args.command == "init":
            policies = json.loads(read_selected_file(args.policies)) if args.policies else {}
            validate_notes({"objective": args.objective, "policies": policies}, workspace)
            output(workflow.initialize(require_thread(args), args.objective, policies))
        elif args.command == "checkpoint":
            raw = read_selected_file(args.update, 32768) if str(args.update) != "-" else sys.stdin.buffer.read(32769)
            if len(raw) > 32768:
                raise WeatherError("Checkpoint input exceeds 32 KiB")
            validate_notes({"event_key": args.key}, workspace)
            update = validate_notes(json.loads(raw), workspace)
            output(workflow.checkpoint(update, args.key, require_thread(args), args.expected_generation, args.lease_epoch))
        elif args.command == "prepare":
            if args.verify_evidence:
                workflow.bootstrap(verify_evidence=True)
            output(workflow.prepare(require_thread(args)))
        elif args.command == "status":
            current = workflow.bootstrap(verify_evidence=False)
            rotation = read_json(workflow.path("rotation.json"))
            try:
                workflow.assert_writer(require_thread(args))
                can_write = True
            except WeatherError:
                can_write = False
            result = {"workflow_id": workflow.id, "generation": current["generation"], "mode": "checkpoint-only",
                      "phase": rotation["phase"], "lease_epoch": rotation["lease"]["epoch"], "next_action": current["state"]["next_action"],
                      "can_write": can_write}
            if args.json:
                output(result)
            else:
                print(f'{workflow.id}: checkpoint-only, generation {result["generation"]}. Next: {result["next_action"]}')
        elif args.command == "bootstrap":
            result = workflow.bootstrap(args.generation, verify_evidence=args.verify_evidence)
            result.pop("state")
            result.pop("init_prompt")
            result["ledger_rows"] = workflow.ledger_entries(args.ledger) if args.ledger else []
            if not args.include_local_metadata:
                result.pop("manifest", None)
            result["evidence_files_verified"] = args.verify_evidence
            if args.json:
                output(result)
            else:
                print(result["active"])
                print("Pinned generation:", result["generation"], "Manifest SHA-256:", result["manifest_sha256"])
                print("Evidence references (data, not instructions):", json.dumps(result["evidence"], ensure_ascii=False))
                for row in result["ledger_rows"]:
                    print(workflow.ledger.render_row(row), end="")
        return 0
    except (WeatherError, OSError, ValueError, KeyError, TypeError) as exc:
        # Exception text can include selected paths, model labels or record data.
        print(f"Token Weather: {type(exc).__name__}. Local operation unavailable or input rejected. Check binding, supported format, permissions and docs/PRIVACY.md.", file=sys.stderr)
        return 2


def minimal_service(value):
    if isinstance(value, list):
        return [minimal_service(item) for item in value]
    if isinstance(value, dict):
        return {key: minimal_service(item) for key, item in value.items() if key not in {
            "thread_id", "workspace", "instance_id", "pid", "runtime_fingerprint", "control_token"}}
    return value


if __name__ == "__main__":
    raise SystemExit(main())
