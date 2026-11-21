#!/usr/bin/env python3
"""Prepare a task-local, CPU-only transcription runtime; never accepts audio.

Default is read-only preflight. Use --allow-download explicitly to install wheels
and fetch the pinned public multilingual model. No API credentials are needed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

SCHEMA_VERSION = 1
PACKAGE = "faster-whisper"
PACKAGE_VERSION = "1.2.1"
MODEL_REPO = "Systran/faster-whisper-small"
MODEL_REVISION = "536b0662742c02347bc0e980a01041f333bce120"
MODEL_FILES = ("config.json", "model.bin", "tokenizer.json", "vocabulary.txt")
MARKER = ".dr-shigyo-transcriber-runtime.json"
MARKER_CONTENT = {"kind": "dr-shigyo-transcriber-runtime", "schema_version": SCHEMA_VERSION}
READY = "ready.json"
MAX_STEP_SECONDS = 600
MAX_STEP_ATTEMPTS = 2
REPAIRABLE = {"invalid_manifest", "missing_python", "missing_model_file", "invalid_model_file", "model_changed", "dependencies_changed", "wrong_version", "invalid_verification"}
# Pins verified against these public publisher endpoints on 2026-10-17.
SOURCES = ["https://pypi.org/pypi/faster-whisper/1.2.1/json",
           "https://huggingface.co/api/models/Systran/faster-whisper-small"]


class SetupError(Exception):
    def __init__(self, code, message, **detail):
        super().__init__(message)
        self.code, self.detail = code, detail


def within(child, parent):
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def validate_runtime(raw, cwd=None):
    work = Path(cwd or Path.cwd()).resolve()
    runtime = Path(raw).expanduser().resolve()
    if runtime == work or runtime == Path.home().resolve() or not within(runtime, work):
        raise SetupError("unsafe_runtime", "Choose a dedicated runtime subdirectory inside the current task working directory.")
    # A task may live below .codex, but installed plugin caches and skill bundles
    # are not task runtime storage. Never modify them even with --allow-download.
    if "skills" in runtime.parts or ("plugins" in runtime.parts and "cache" in runtime.parts):
        raise SetupError("unsafe_runtime", "Runtime must be outside installed skills and plugin caches.")
    if any((p / ".codex-plugin" / "plugin.json").is_file() or (p / "plugin.json").is_file()
           for p in [runtime, *runtime.parents] if within(p, work)):
        raise SetupError("unsafe_runtime", "Runtime must be outside the distributed plugin directory.")
    if runtime.exists() and not runtime.is_dir():
        raise SetupError("unsafe_runtime", "Runtime path exists and is not a directory.")
    if runtime.is_dir() and any(runtime.iterdir()):
        marker = runtime / MARKER
        try:
            actual = json.loads(marker.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise SetupError("unmanaged_directory", "Existing nonempty runtime directory is not managed by this helper; choose a new directory.")
        if actual != MARKER_CONTENT:
            raise SetupError("unmanaged_directory", "Runtime ownership marker is incompatible.")
    for relative in (READY, MARKER, "venv", "models", "models/faster-whisper-small", "cache", *["models/faster-whisper-small/" + n for n in MODEL_FILES]):
        if (runtime / relative).is_symlink() or not within((runtime / relative).resolve(), runtime):
            raise SetupError("unsafe_runtime", "Runtime storage contains a directory link outside the private runtime.")
    return runtime


def runtime_python(runtime):
    return runtime / "venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def environment(runtime, offline=False):
    env = os.environ.copy()
    # Suppress implicit authenticated Hub access, custom mirrors and accidental
    # shared caches. Nothing in this helper receives or uploads a user recording.
    for name in list(env):
        if name.startswith("PIP_") or name in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "HF_ENDPOINT", "PYTHONPATH", "PYTHONHOME"):
            env.pop(name, None)
    env.update({"HF_HOME": str(runtime / "cache" / "huggingface"),
                "HF_HUB_CACHE": str(runtime / "cache" / "huggingface" / "hub"),
                "XDG_CACHE_HOME": str(runtime / "cache"),
                "PIP_CACHE_DIR": str(runtime / "cache" / "pip"),
                "PIP_CONFIG_FILE": os.devnull,
                "PIP_DISABLE_PIP_VERSION_CHECK": "1",
                "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1", "HF_HUB_DISABLE_TELEMETRY": "1",
                "DO_NOT_TRACK": "1", "HF_HUB_ETAG_TIMEOUT": "25", "HF_HUB_DOWNLOAD_TIMEOUT": "60",
                "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1"})
    if offline:
        env["HF_HUB_OFFLINE"] = "1"
    else:
        env.pop("HF_HUB_OFFLINE", None)
    return env


def progress(step, **detail):
    print(json.dumps({"event": "audio_setup", "step": step, **detail}), file=sys.stderr, flush=True)


def transient_failure(message):
    """Retry ordinary transport failures once, never policy/auth/certificate errors."""
    value = message.lower()
    blocked = ("403", "401", "forbidden", "permission denied", "access denied", "certificate", "ssl", "blocked", "denied by", "network is unreachable")
    if any(item in value for item in blocked):
        return False
    return any(item in value for item in ("timed out", "timeout", "connection reset", "connection aborted", "temporary failure", "temporarily unavailable", "429", "502", "503", "504"))


def execute(command, runtime, step, timeout=MAX_STEP_SECONDS, offline=False):
    retries = MAX_STEP_ATTEMPTS if step in ("install_packages", "download_model") and not offline else 1
    for attempt in range(1, retries + 1):
        progress(step, attempt=attempt)
        try:
            result = subprocess.run(command, check=False, text=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, env=environment(runtime, offline), timeout=timeout)
        except subprocess.TimeoutExpired:
            # A fully timed-out setup is bounded and reported; another ten-minute
            # attempt would mask a persistent host limit.
            raise SetupError("step_timeout", "Setup step exceeded its time limit.", step=step, timeout_seconds=timeout, attempts=attempt)
        except PermissionError as exc:
            raise SetupError("permission_denied", str(exc), step=step)
        except OSError as exc:
            raise SetupError("execution_failed", str(exc), step=step)
        if not result.returncode:
            return result.stdout
        diagnostic = (result.stderr or result.stdout)[-2500:]
        if attempt < retries and transient_failure(diagnostic):
            progress(step, action="retry_transient_failure", next_attempt=attempt + 1)
            time.sleep(1)
            continue
        raise SetupError("step_failed", "Setup step failed after the allowed attempts.",
                         step=step, returncode=result.returncode, diagnostic=diagnostic, attempts=attempt)


def get_versions(runtime):
    code = "import json,importlib.metadata as m; import faster_whisper; print(json.dumps({d.metadata['Name']:d.version for d in m.distributions() if d.metadata['Name']}))"
    output = execute([str(runtime_python(runtime)), "-I", "-B", "-c", code], runtime, "verify_imports", timeout=90, offline=True)
    try:
        versions = json.loads(output)
    except ValueError:
        raise SetupError("invalid_verification", "Dependency verification did not return valid JSON.")
    if versions.get(PACKAGE) != PACKAGE_VERSION:
        raise SetupError("wrong_version", "Installed faster-whisper does not match the pinned release.")
    return dict(sorted(versions.items(), key=lambda item: item[0].lower()))


def fingerprint(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return {"bytes": path.stat().st_size, "sha256": digest.hexdigest()}


def model_fingerprints(model):
    result = {}
    for filename in MODEL_FILES:
        path = model / filename
        if not path.is_file() or path.stat().st_size == 0:
            raise SetupError("missing_model_file", "Required local model file is absent or empty.", file=filename)
        result[filename] = fingerprint(path)
    # Check the small metadata files are parseable; actual inference is tested by
    # transcribe_audio.py rather than claimed by this preparation utility.
    for filename in ("config.json", "tokenizer.json"):
        try:
            json.loads((model / filename).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise SetupError("invalid_model_file", "Model JSON is invalid.", file=filename)
    return result


def preflight(runtime):
    ready = runtime / READY
    if not ready.is_file():
        return {"status": "not_ready", "reason": "No verified ready manifest exists.", "runtime_dir": str(runtime), "download_required": True}
    try:
        saved = json.loads(ready.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise SetupError("invalid_manifest", "Ready manifest is unreadable.")
    if not isinstance(saved, dict):
        raise SetupError("invalid_manifest", "Ready manifest must be a JSON object.")
    expected = {"backend": PACKAGE, "model_repo": MODEL_REPO, "model_revision": MODEL_REVISION,
                "python": str(runtime_python(runtime)), "model_path": str(runtime / "models" / "faster-whisper-small"),
                "schema_version": SCHEMA_VERSION}
    if any(saved.get(key) != value for key, value in expected.items()):
        raise SetupError("invalid_manifest", "Ready manifest does not match the pinned task-local runtime.")
    if not runtime_python(runtime).is_file():
        raise SetupError("missing_python", "Task-local Python interpreter is missing.")
    actual = model_fingerprints(Path(saved["model_path"]))
    if actual != saved.get("model_files"):
        raise SetupError("model_changed", "Model files differ from the verified ready manifest; do not use this runtime.")
    versions = get_versions(runtime)
    if versions != saved.get("installed_versions"):
        raise SetupError("dependencies_changed", "Installed package versions differ from the ready manifest.")
    return {**saved, "status": "ready", "preflight_verified": True, "network_used": False, "repaired_this_run": False}


def prepare(runtime, repair_reason=None, before_model=None):
    runtime.mkdir(parents=True, exist_ok=True)
    marker = runtime / MARKER
    if not marker.exists():
        marker.write_text(json.dumps(MARKER_CONTENT) + "\n", encoding="utf-8")
    # Venv is private and reusable after an interrupted download/install. It does
    # not inherit system packages and does not change system/global Python.
    python = runtime_python(runtime)
    if not repair_reason and (runtime / "venv").exists():
        config = runtime / "venv" / "pyvenv.cfg"
        if not python.is_file() or not config.is_file():
            repair_reason = "incomplete_venv"
        elif "include-system-site-packages = false" not in config.read_text(encoding="utf-8").lower():
            raise SetupError("unsafe_venv", "Task-local interpreter is not an isolated virtual environment.")
        else:
            try:
                execute([str(python), "-I", "-B", "-m", "pip", "--version"], runtime, "verify_pip", timeout=30, offline=True)
            except SetupError as exc:
                if exc.code == "step_failed" and "No module named pip" in exc.detail.get("diagnostic", ""):
                    repair_reason = "incomplete_venv"
                else:
                    raise
    if repair_reason and (runtime / "venv").exists():
        # Preserve the previous managed environment for diagnosis; no recursive
        # deletion and no changes to global Python or installed plugin files.
        backup = runtime / ("venv-before-repair-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f"))
        (runtime / "venv").rename(backup)
        progress("repair_runtime", reason=repair_reason, preserved_directory=backup.name)
    if not python.exists():
        execute([sys.executable, "-I", "-B", "-m", "venv", str(runtime / "venv")], runtime, "create_venv", timeout=90)
    config = runtime / "venv" / "pyvenv.cfg"
    if not config.is_file() or "include-system-site-packages = false" not in config.read_text(encoding="utf-8").lower():
        raise SetupError("unsafe_venv", "Task-local interpreter is not an isolated virtual environment.")
    install_command = [str(python), "-I", "-B", "-m", "pip", "install", "--disable-pip-version-check", "--no-input",
                       "--index-url", "https://pypi.org/simple", "--only-binary=:all:",
                       "--retries", "0", "--timeout", "60", f"{PACKAGE}=={PACKAGE_VERSION}"]
    execute(install_command, runtime, "install_packages")
    try:
        versions = get_versions(runtime)
    except SetupError as exc:
        # An interrupted wheel may leave metadata that pip calls installed while
        # imports fail. Reinstall only this private environment once, from the
        # same official registry; never switch indexes or alter host protections.
        if exc.code != "step_failed" or exc.detail.get("step") != "verify_imports" or not any(
            item in exc.detail.get("diagnostic", "") for item in ("ModuleNotFoundError", "ImportError", "Library not loaded")):
            raise
        progress("repair_packages", reason="import_failed_after_install")
        execute(install_command + ["--force-reinstall", "--no-cache-dir"], runtime, "install_packages")
        versions = get_versions(runtime)
        repair_reason = repair_reason or "incomplete_packages"
    if before_model is not None:
        before_model(str(python))
    model = runtime / "models" / "faster-whisper-small"
    download_code = """import json,sys
from huggingface_hub import hf_hub_download
repo,revision,local,cache,files,repair=json.loads(sys.argv[1])
for filename in files:
    hf_hub_download(repo_id=repo,revision=revision,filename=filename,local_dir=local,cache_dir=cache,token=False,force_download=repair)
print(json.dumps({'downloaded':files}))
"""
    execute([str(python), "-I", "-B", "-c", download_code,
             json.dumps([MODEL_REPO, MODEL_REVISION, str(model), str(runtime / "cache" / "huggingface" / "hub"), MODEL_FILES, bool(repair_reason)])],
            runtime, "download_model")
    manifest = {"schema_version": SCHEMA_VERSION, "status": "ready", "backend": PACKAGE,
                "python": str(python), "model_path": str(model), "model_repo": MODEL_REPO,
                "model_revision": MODEL_REVISION, "installed_versions": versions,
                "model_files": model_fingerprints(model), "runtime_dir": str(runtime),
                "created_at": datetime.now(timezone.utc).isoformat(), "source_urls": SOURCES,
                "readiness_scope": "Imports and pinned local model files verified; speech accuracy and ChatGPT Web execution are not yet verified.",
                "audio_transmitted": False, "repair_reason": repair_reason}
    temporary = runtime / (READY + ".tmp")
    temporary.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(runtime / READY)
    return {**manifest, "network_used": True, "repaired_this_run": bool(repair_reason)}


def ensure_ready(runtime, allow_download=False, before_model=None):
    """Read-only reuse or one repair of a positively identified private runtime."""
    if sys.version_info < (3, 9):
        raise SetupError("python_too_old", "Python 3.9 or later is required; no system upgrade will be performed.")
    runtime = validate_runtime(runtime)
    repair = None
    try:
        current = preflight(runtime)
    except SetupError as exc:
        # Import failure in the managed venv is repairable; policy/access errors
        # and unknown errors are not permission to replace anything.
        import_failure = exc.code == "step_failed" and exc.detail.get("step") == "verify_imports" and any(
            x in exc.detail.get("diagnostic", "") for x in ("ModuleNotFoundError", "ImportError", "Library not loaded"))
        if exc.code not in REPAIRABLE and not import_failure:
            raise
        if not allow_download:
            raise
        repair = exc.code
        current = {"status": "not_ready"}
    if current["status"] == "ready":
        if before_model is not None:
            before_model(current["python"])
        return current
    if not allow_download:
        return {**current, "network_used": False, "next_step": "Automatic setup requires permitted package/model downloads; offline mode did not attempt them."}
    return prepare(runtime, repair_reason=repair, before_model=before_model)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime-dir", required=True, help="Dedicated runtime subdirectory inside the current task working directory")
    parser.add_argument("--allow-download", action="store_true", help="Explicitly allow PyPI wheel installation and public pinned model download")
    args = parser.parse_args(argv)
    try:
        result = ensure_ready(args.runtime_dir, allow_download=args.allow_download)
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 0 if result["status"] == "ready" else 3
    except (SetupError, OSError, ValueError) as exc:
        print(json.dumps({"status": "failed", "error_code": getattr(exc, "code", "filesystem_error"),
                          "error": str(exc), "audio_transmitted": False, **getattr(exc, "detail", {})}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
