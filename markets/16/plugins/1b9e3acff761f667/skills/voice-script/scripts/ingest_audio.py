#!/usr/bin/env python3
"""One-command audio intake: validate, prepare private runtime, decode, transcribe.

Downloads trusted public dependencies/models automatically when absent. --offline
forbids these downloads. No audio is transmitted to an external service. Run from
the task working area, with runtime and outputs outside the distributed plugin.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys

VERSION = "1.1.4"
sys.dont_write_bytecode = True  # Never write caches into an installed skill bundle.
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("shigyo_audio_prepare", HERE / "prepare_transcriber.py")
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


class IntakeError(Exception):
    def __init__(self, code, message, **detail):
        super().__init__(message)
        self.code, self.detail = code, detail


class NoSpeech(Exception):
    def __init__(self, report):
        self.report = report


def private_output(raw):
    path = Path(raw).expanduser().resolve()
    for ancestor in (path, *path.parents):
        if (ancestor / ".codex-plugin").is_dir() or (ancestor / ".claude-plugin").is_dir() or (ancestor / "plugin.json").is_file():
            raise IntakeError("plugin_output_forbidden", "Store audio/transcripts outside the plugin distribution.")
    if path.exists():
        raise IntakeError("output_exists", "Use a new output directory; previous transcripts are never overwritten.")
    return path


def validate_input(args):
    path = Path(args.input).expanduser().resolve()
    if not path.is_file():
        raise IntakeError("missing_input", "The attached file is not accessible at the supplied path.")
    if args.max_bytes <= 0 or path.stat().st_size > args.max_bytes:
        raise IntakeError("size_limit", "Audio exceeds the supplied byte limit.")
    if path.stat().st_size == 0:
        raise IntakeError("empty_input", "The attached file is empty.")
    if not math.isfinite(args.max_seconds) or not 0 < args.max_seconds <= 86400:
        raise IntakeError("invalid_limit", "--max-seconds must be greater than zero and at most 86400.")
    if not 1 <= args.threads <= 8:
        raise IntakeError("invalid_threads", "--threads must be from 1 through 8.")
    if not 1 <= args.timeout_seconds <= 86400:
        raise IntakeError("invalid_timeout", "--timeout-seconds must be from 1 through 86400.")
    with path.open("rb") as handle:
        handle.read(32)  # Confirm readability before any installation or download.
    return path


def run_json(command, runtime, timeout, step):
    setup.progress(step)
    try:
        completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=timeout, env=setup.environment(runtime, offline=True))
    except subprocess.TimeoutExpired:
        raise IntakeError("execution_timeout", "Audio processing exceeded its time limit; no complete transcript is claimed.", step=step)
    except OSError as exc:
        raise IntakeError("execution_failed", str(exc), step=step)
    try:
        report = json.loads(completed.stdout)
    except ValueError:
        raise IntakeError("invalid_worker_result", "The audio worker did not return a readable result.", step=step,
                          returncode=completed.returncode, diagnostic=completed.stderr[-2000:])
    if not isinstance(report, dict):
        raise IntakeError("invalid_worker_result", "The audio worker result was not an object.", step=step)
    if completed.returncode not in (0, 3) or report.get("status") == "failed":
        raise IntakeError(report.get("error_code", "worker_failed"), report.get("error", "Audio worker failed."),
                          step=step, worker_report=report)
    return report


def verify_transcript(output, result):
    report_path, raw_path = output / "transcript.json", output / "transcript.raw.txt"
    if not report_path.is_file() or not raw_path.is_file():
        raise IntakeError("missing_output", "The worker finished without the required transcript files.")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    raw = raw_path.read_text(encoding="utf-8")
    if not isinstance(report, dict):
        raise IntakeError("inconsistent_output", "Saved transcript report must be an object.")
    if report.get("status") != result.get("status"):
        raise IntakeError("inconsistent_output", "Worker and saved transcript statuses differ.")
    if report.get("status") in ("transcribed_unverified", "needs_review") and not raw.strip():
        raise IntakeError("empty_transcript", "No usable speech was saved; do not proceed from an empty result.")
    if report.get("status") in ("transcribed_unverified", "needs_review"):
        duration, processed = report.get("duration_seconds"), report.get("processed_audio_seconds")
        if report.get("processing_complete") is not True or any(not isinstance(v, (int, float)) or not math.isfinite(v) or v <= 0 for v in (duration, processed)) or abs(duration - processed) > 0.1:
            raise IntakeError("incomplete_processing", "The transcript does not cover a completed engine run over the full recording.")
    if "raw_text" in report and report["raw_text"] != raw:
        raise IntakeError("inconsistent_output", "Saved raw transcript differs from the worker report.")
    return {"transcript_path": str(raw_path), "transcript_report_path": str(report_path),
            "transcript_characters": len(raw), "output_verified": True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--out-dir", required=True, help="A new directory for this recording")
    parser.add_argument("--runtime-dir", required=True, help="Task-local managed runtime; reusable for later recordings")
    parser.add_argument("--offline", action="store_true", help="Use only an already-prepared runtime; no installation/download")
    parser.add_argument("--language", default="ja")
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--max-seconds", type=float, default=7200)
    parser.add_argument("--max-bytes", type=int, default=1024 * 1024 * 1024)
    parser.add_argument("--timeout-seconds", type=int, default=3600)
    args = parser.parse_args(argv)
    result = {"schema_version": VERSION, "status": "not_started", "audio_transmitted": False,
              "stages": [], "offline": args.offline, "runtime_ready": False, "setup_network_attempted": False,
              "speech_completeness_verified": False}
    output = None
    report_dir_allowed = False
    original_progress = setup.progress
    def observed_progress(step, **detail):
        if step in ("install_packages", "download_model"):
            result["setup_network_attempted"] = True
        original_progress(step, **detail)
    setup.progress = observed_progress
    try:
        path = validate_input(args)
        output = private_output(args.out_dir)
        runtime = setup.validate_runtime(args.runtime_dir)
        if setup.within(path, runtime) or setup.within(output, runtime) or setup.within(runtime, output):
            raise IntakeError("overlapping_storage", "Keep source audio, runtime, and transcript output directories separate.")
        report_dir_allowed = True
        result["stages"].append({"step": "validate_input", "status": "passed", "bytes": path.stat().st_size})
        result["input_file"] = path.name

        def probe(python):
            report = run_json([python, "-I", "-B", str(HERE / "transcribe_audio.py"), "--input", str(path),
                               "--probe", "--max-seconds", str(args.max_seconds), "--max-bytes", str(args.max_bytes)],
                              runtime, min(args.timeout_seconds, 600), "decode_audio")
            result["stages"].append({"step": "decode_audio", "status": report.get("status"),
                                     "duration_seconds": report.get("duration_seconds")})
            if report.get("status") == "no_transcript":
                raise NoSpeech(report)
            if report.get("status") != "audio_ready":
                raise IntakeError("invalid_probe_result", "Audio decode probe did not confirm a usable recording.")

        result["stages"].append({"step": "prepare_runtime", "status": "running"})
        ready = setup.ensure_ready(runtime, allow_download=not args.offline, before_model=probe)
        if ready.get("status") != "ready":
            raise IntakeError("runtime_not_ready", "Offline mode requires an already prepared local runtime; no downloads were attempted.")
        result.update({"runtime_ready": True, "setup_network_used": ready.get("network_used", False),
                       "runtime_repaired": bool(ready.get("repaired_this_run")), "runtime_directory": str(runtime)})
        for stage in result["stages"]:
            if stage["step"] == "prepare_runtime": stage["status"] = "ready"
        report = run_json([ready["python"], "-I", "-B", str(HERE / "transcribe_audio.py"),
                           "--input", str(path), "--out-dir", str(output), "--backend", "faster-whisper",
                           "--model-path", ready["model_path"], "--language", args.language,
                           "--threads", str(args.threads), "--max-seconds", str(args.max_seconds),
                           "--max-bytes", str(args.max_bytes)], runtime, args.timeout_seconds, "transcribe_audio")
        if report.get("status") not in ("transcribed_unverified", "needs_review", "no_transcript"):
            raise IntakeError("invalid_worker_status", "Worker did not return a recognized transcription status.")
        result.update({"status": report["status"], "transcription": report, **verify_transcript(output, report)})
        result["stages"].append({"step": "transcribe_audio", "status": report["status"]})
    except NoSpeech as exc:
        result.update({"status": "no_transcript", "reason": "effectively_silent_audio", "probe": exc.report})
        result["stages"].append({"step": "transcribe_audio", "status": "not_run_silent_audio"})
    except (IntakeError, setup.SetupError, OSError, ValueError) as exc:
        result.update({"status": "failed", "error_code": getattr(exc, "code", "filesystem_error"),
                       "error": str(exc), **getattr(exc, "detail", {})})
        result["stages"].append({"step": result.get("step", "audio_intake"), "status": "failed"})
    finally:
        setup.progress = original_progress
        for stage in result["stages"]:
            if stage.get("status") == "running":
                stage["status"] = "not_completed"
                stage["reason"] = result.get("error_code", result.get("reason", result["status"]))
    # Pipeline metadata contains no transcript text. Keep it next to the private
    # outputs (including exact failure stages), never inside the plugin bundle.
    if output is not None and report_dir_allowed:
        try:
            output.mkdir(parents=True, exist_ok=True)
            (output / "audio-intake.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
            result["intake_report_path"] = str(output / "audio-intake.json")
        except OSError as exc:
            result["report_write_error"] = str(exc)
    print(json.dumps(result, ensure_ascii=False, allow_nan=False))
    return 0 if result["status"] == "transcribed_unverified" else 3 if result["status"] in ("needs_review", "no_transcript") else 2


if __name__ == "__main__":
    sys.exit(main())
