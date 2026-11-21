"""Opaque v2 delivery layout, strict archive audit, and lossless record retention.

Identifiers are stable across builds. They reduce incidental exposure, not access.
No code or data is executed by these functions.
"""
from __future__ import annotations
import base64
import io
import json
import re
import posixpath
import zipfile
from .safety import (IterationError, canonical, code_path, read_archive, sha, legacy_label, extra_readme,
                     BLOCKED_NAMES, BLOCKED_PARTS)

AUTO = "PROGRAM/Automation/"
LEGACY_AUTO = "Program/Automation/"
README = "PROGRAM/readme.md"
LAUNCH = "run.bat"
RECORDS = {
    "index": "AB60.json", "position": "CP74.md", "rules": "LN32.md",
    "components": "SX18.md", "options": "QD47.md", "evidence": "VT83.json",
    "resume": "RK26.md", "events": "MJ59.jsonl", "retained": "UX41.md",
    "supervisor": "ZP90.py",
}
OLD = {
    "index": "A00.json", "position": "A10.md", "rules": "A20.md",
    "components": "A30.md", "options": "A40.md", "evidence": "A50.json",
    "resume": "A60.md", "events": "A70.jsonl", "retained": "A80.md",
    "supervisor": "A81.py",
}
INDEX = AUTO + RECORDS["index"]
RUNNER = AUTO + RECORDS["supervisor"]
EXTRA_RECORDS = {"lifecycle": AUTO+"RT42.py", "test_plan": AUTO+"QA27.json", "qualification": AUTO+"RC18.json"}
RETAINED_PREFIX = AUTO + "RA21/"
MAX_RECORD_BYTES = 2 * 1024 * 1024


def record(files: dict[str, bytes], role: str) -> bytes:
    return next((files[p] for prefix in (AUTO, LEGACY_AUTO)
                 for p in (prefix + RECORDS[role], prefix + OLD[role]) if p in files), b"")


def identity(files: dict[str, bytes], verify: bool = True) -> tuple[dict, str | None]:
    candidates = [p for p in (INDEX, AUTO + OLD["index"], LEGACY_AUTO + RECORDS["index"],
                               LEGACY_AUTO + OLD["index"]) if p in files]
    if len(candidates) > 1:
        raise IterationError("Two identity records found; resolve the conflicting input before importing.", "ambiguous_identity")
    if not candidates:
        return {}, None
    path = candidates[0]
    try:
        value = json.loads(files[path])
    except (ValueError, UnicodeError) as exc:
        raise IterationError("Invalid identity record.") from exc
    if not isinstance(value, dict) or value.get("format") != "iteration" or value.get("format_version") not in (1, 2):
        raise IterationError("Unsupported record format; import refused rather than guessed.")
    if (path.rsplit("/", 1)[-1] == RECORDS["index"]) != (value["format_version"] == 2):
        raise IterationError("Identity filename and format version disagree.")
    if verify:
        hashes = value.get("file_sha256", {})
        if not isinstance(hashes, dict) or set(hashes) != set(files) - {path}:
            raise IterationError("Manifest file inventory is incomplete or different from the archive.")
        for name, digest in hashes.items():
            if sha(files[name]) != digest:
                raise IterationError("Imported file checksum mismatch: " + name)
    return value, path


def split_input(files: dict[str, bytes]) -> tuple[dict[str, bytes], dict[str, bytes]]:
    """Import both older Program/ layouts and the new PROGRAM/ archive.

    Verify original manifest hashes BEFORE remapping names (performed by caller).
    Program files are never reinterpreted as documentation; their bytes are kept.
    """
    source, notes = {}, {}
    ignored = {"run.bat", "Run.bat", "LogReport.zip", RUNNER,
               LEGACY_AUTO + RECORDS["supervisor"], AUTO + OLD["supervisor"],
               LEGACY_AUTO + OLD["supervisor"], EXTRA_RECORDS["lifecycle"],
               LEGACY_AUTO + "RT42.py"}
    for name, data in files.items():
        if name in ignored:
            continue
        if (name in ("readme.md", README) or
                name.startswith(AUTO) or name.startswith(LEGACY_AUTO) or
                legacy_label(name) or extra_readme(name)):
            parts = name.split("/")
            if any(p.casefold() in BLOCKED_NAMES or p.casefold() in BLOCKED_PARTS or
                   p.casefold().endswith((".pem", ".pfx", ".p12", ".key")) for p in parts):
                raise IterationError("Excluded credential/development file in reference input.", "possible_secret")
            suffix = "." + name.rsplit(".", 1)[-1].casefold() if "." in name.rsplit("/", 1)[-1] else ""
            if not name.startswith((RETAINED_PREFIX, LEGACY_AUTO + "RA21/")) and suffix in (".py", ".pyc", ".pyd", ".exe", ".dll", ".bat", ".cmd", ".ps1", ".db", ".sqlite", ".sqlite3", ".zip"):
                raise IterationError("Ambiguous source/data under a reference label: " + name, "ambiguous_legacy_file")
            notes[name] = data
        elif name.startswith(("PROGRAM/", "Program/")):
            path = code_path(name)
            if path in source:
                raise IterationError("Duplicate application path during legacy import.", "case_collision")
            source[path] = data
        else:
            raise IterationError("Unsupported top-level file: " + name + ". The importer will not guess a new application layout.")
    if "PROGRAM/main.py" not in source or not ({"run.bat", "Run.bat"} & files.keys()):
        raise IterationError("Import needs run.bat and PROGRAM/main.py (or the previous Build_ layout).")
    return source, notes


def retain(notes: dict[str, bytes], manifest: dict | None = None) -> dict:
    """Preserve exact bytes under coded filenames with an inspectable provenance map."""
    manifest = manifest or {}
    prior = manifest.get("preserved_file_origins", {})
    if not isinstance(prior, dict):
        raise IterationError("Invalid retained-file index.")
    out = {}
    for name, data in sorted(notes.items()):
        if name in (AUTO + RECORDS["retained"], AUTO + OLD["retained"]) and prior:
            # Prior provenance is recreated below; its actual documents remain in RA21.
            continue
        previous = prior.get(name, {})
        if not isinstance(previous, dict):
            raise IterationError("Invalid retained-file origin entry.")
        original = previous.get("original_path", name)
        if not isinstance(original, str):
            raise IterationError("Invalid retained-file origin.")
        # Avoid silently recoding an unverified path. No filesystem extraction is done.
        canonical(original)
        digest = sha(data)
        seed = int(sha((original + "\0" + digest).encode()), 16)
        extension = PathSuffix(name)
        for attempt in range(67600):
            n = (seed + attempt) % 67600
            code = chr(65 + n // 2600) + chr(65 + (n // 100) % 26) + str(n % 100).zfill(2)
            path = RETAINED_PREFIX + code + extension
            item = {"original_path": original, "sha256": digest, "content_base64": base64.b64encode(data).decode("ascii")}
            if path not in out or out[path] == item:
                out[path] = item
                break
        else:
            raise IterationError("Retained record namespace exhausted.")
    if sum(len(base64.b64decode(v["content_base64"])) for v in out.values()) > MAX_RECORD_BYTES:
        raise IterationError("Retained records exceed the 2 MiB limit; nothing was silently truncated.")
    return out


def PathSuffix(name: str) -> str:
    suffix = "." + name.rsplit("/", 1)[-1].rsplit(".", 1)[-1].lower() if "." in name.rsplit("/", 1)[-1] else ".bin"
    # Executable/archive originals become inert binary records, not runnable helpers.
    return suffix if suffix in (".md", ".txt", ".json", ".jsonl", ".csv", ".png", ".jpg", ".rst") else ".bin"


def unpack_retained(items: dict) -> dict[str, bytes]:
    out = {}
    for path, item in items.items():
        if not re.fullmatch(re.escape(RETAINED_PREFIX) + r"[A-Z]{2}[0-9]{2}\.[a-z0-9]+", path):
            raise IterationError("Unsafe retained-record path.")
        try:
            data = base64.b64decode(item["content_base64"], validate=True)
        except (KeyError, TypeError, ValueError) as exc:
            raise IterationError("Invalid retained-record encoding.") from exc
        if sha(data) != item.get("sha256"):
            raise IterationError("Retained-record checksum mismatch.")
        out[path] = data
    if sum(map(len, out.values())) > MAX_RECORD_BYTES:
        raise IterationError("Retained records exceed the size limit.")
    return out


def check_delivery(files: dict[str, bytes], verify: bool = True) -> dict:
    if set(p.split("/")[0] for p in files) != {LAUNCH, "PROGRAM"}:
        raise IterationError("Delivery root must contain ONLY run.bat and PROGRAM/.", "layout_failed")
    required = {INDEX, RUNNER, README, "PROGRAM/main.py",
                *[AUTO + RECORDS[r] for r in ("position", "rules", "components", "options", "evidence", "resume", "events")]}
    if not required <= set(files):
        raise IterationError("Missing required program, README, or coded records.", "layout_failed")
    for path, data in files.items():
        canonical(path)
        if legacy_label(path) or extra_readme(path):
            raise IterationError("Delivery contains a disallowed workflow label or duplicate readme: " + path, "layout_failed")
        if path.startswith(AUTO):
            rel = path[len(AUTO):]
            if not re.fullmatch(r"(?:RA21/)?[A-Z]{2}[0-9]{2}\.[a-z0-9]+", rel):
                raise IterationError("Noncoded Automation path: " + path, "layout_failed")
        elif path.startswith("PROGRAM/") and path != README:
            if code_path(path) != path:
                raise IterationError("Noncanonical program path: " + path, "layout_failed")
        if legacy_label(path) or path.endswith("LogReport.zip"):
            raise IterationError("Do not ship pre-generated diagnostic archives.", "layout_failed")
    m, index_path = identity(files, verify=verify)
    if index_path != INDEX or m.get("format_version") != 2:
        raise IterationError("Delivery must use the current coded record format.", "layout_failed")
    indexes = m.get("record_index")
    expected_index = {r: AUTO + n for r, n in RECORDS.items() if AUTO + n in files}
    expected_index.update({role: path for role, path in EXTRA_RECORDS.items() if path in files})
    if indexes != expected_index:
        raise IterationError("Record lexicon does not match the delivered files.", "layout_failed")
    text = files[README].decode("utf-8")
    if legacy_label(text):
        raise IterationError("README exposes a retired workflow label.", "layout_failed")
    targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    normalized_targets = set()
    for target in targets:
        if target.startswith(("http://", "https://")):
            continue
        resolved = posixpath.normpath(posixpath.join("PROGRAM", target.removeprefix("./")))
        if resolved.startswith("../") or resolved.startswith("/"):
            raise IterationError("README link escapes its archive: " + target, "layout_failed")
        if target.endswith("/"):
            ok = any(x.startswith(resolved.rstrip("/") + "/") for x in files)
        else:
            ok = resolved in files
        if not ok:
            raise IterationError("README has a broken local link: " + target, "layout_failed")
        normalized_targets.add(resolved)
    if not all(AUTO + RECORDS[r] in normalized_targets for r in ("index", "position", "rules", "components", "options", "evidence", "resume", "events")):
        raise IterationError("README is missing coded references.", "layout_failed")
    return {"status": "passed", "files": len(files), "layout_version": 3,
            "root": ["run.bat", "PROGRAM/"], "readme": README,
            "legacy_labels": 0, "readme_count": 1, "integrity": "matched" if verify else "not_checked", "runtime_tested": False}


def audit_archive(raw: bytes) -> dict:
    files = read_archive(raw)
    # Empty ZIP folders must not evade a file-only audit.
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for entry in z.infolist():
            if legacy_label(entry.filename):
                raise IterationError("Disallowed folder label in delivered ZIP.", "layout_failed")
            if entry.is_dir():
                folder = canonical(entry.filename.rstrip("/"))
                if folder != "PROGRAM" and not folder.startswith("PROGRAM/"):
                    raise IterationError("Unexpected root directory.", "layout_failed")
                if folder.startswith(AUTO) and not re.fullmatch(r"(?:[A-Z]{2}[0-9]{2})(?:/[A-Z]{2}[0-9]{2})*", folder[len(AUTO):]):
                    raise IterationError("Noncoded empty Automation folder.", "layout_failed")
    return check_delivery(files)
