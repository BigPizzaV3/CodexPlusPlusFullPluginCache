"""Path, archive, content, and JSON validation. No project code is executed here."""
from __future__ import annotations
import base64
import hashlib
import io
import json
import re
import stat
import zipfile
from pathlib import Path, PurePosixPath

MAX_FILE = 16 * 1024 * 1024
MAX_ARCHIVE = 128 * 1024 * 1024
MAX_TOTAL = 384 * 1024 * 1024
MAX_FILES = 6000
RESERVED = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}
BLOCKED_PARTS = {".git", ".venv", "venv", "__pycache__", ".ssh", "node_modules"}
BLOCKED_NAMES = {".env", ".env.local", ".env.production", "id_rsa", "id_ed25519", "credentials.json", "secrets.json"}
SECRET = re.compile(r"(?:-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}|\bgh[pousr]_[A-Za-z0-9]{30,}|\bAKIA[A-Z0-9]{16}\b)")

class IterationError(Exception):
    def __init__(self, message: str, code: str = "invalid_request"):
        super().__init__(message)
        self.code = code

def canonical(path: str) -> str:
    if not isinstance(path, str) or not path or len(path) > 220:
        raise IterationError("File path is empty or too long.")
    if "\\" in path or path.startswith("/") or "\x00" in path:
        raise IterationError("Use a relative forward-slash path.")
    bits = path.split("/")
    for p in bits:
        if p in ("", ".", "..") or any(ord(c) < 32 for c in p) or any(c in '<>:"|?*' for c in p):
            raise IterationError(f"Unsafe Windows path: {path}")
        if p.endswith((".", " ")) or p.split(".")[0].upper() in RESERVED:
            raise IterationError(f"Reserved Windows filename: {path}")
    return str(PurePosixPath(path))

def legacy_label(path: str) -> bool:
    """Reject retired document/folder labels regardless of spacing or case."""
    pieces = path.replace("\\", "/").split("/")
    return any(any(token in re.sub(r"[^a-z0-9]", "", p.casefold())
                   for token in ("handoff", "lockedin", "brainstorm")) for p in pieces)

def extra_readme(path: str) -> bool:
    leaf = path.replace("\\", "/").rsplit("/", 1)[-1].casefold()
    return leaf.split(".", 1)[0] == "readme" and path not in ("readme.md", "PROGRAM/readme.md")


def code_path(path: str) -> str:
    path = canonical(path)
    bits = path.split("/")
    # Accept source calls from earlier Build_ releases, but normalize immediately.
    if bits[0] == "Program":
        bits[0] = "PROGRAM"
        path = "/".join(bits)
    if path == "PROGRAM/readme.md" or legacy_label(path) or extra_readme(path):
        raise IterationError("Reserved documentation name. Use the coded package records, not parallel workflow folders.", "reserved_record_name")
    if len(bits) < 2 or bits[0] != "PROGRAM" or bits[1].casefold() == "automation":
        raise IterationError("Write only within PROGRAM/. Automation records and run.bat are engine-managed.", "protected_path")
    if any(p.casefold() in BLOCKED_PARTS or p.casefold() in BLOCKED_NAMES or p.casefold().endswith((".pem", ".pfx", ".p12", ".key")) for p in bits):
        raise IterationError(f"Excluded development or credential file: {path}", "protected_path")
    return path

def within(root: Path, relative: str) -> Path:
    relative = canonical(relative)
    target = root.joinpath(*relative.split("/"))
    for parent in (target, *target.parents):
        if parent == root.parent:
            break
        if parent.is_symlink():
            raise IterationError("Symbolic links are not allowed.")
    if not target.resolve().is_relative_to(root.resolve()):
        raise IterationError("Path escapes the workspace.")
    return target

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def decode_file(item: dict) -> bytes:
    content = item.get("content")
    if not isinstance(content, str):
        raise IterationError("File content must be text or base64 text.")
    encoding = item.get("encoding", "utf-8")
    if encoding == "utf-8":
        result = content.encode("utf-8")
    elif encoding == "base64":
        try:
            result = base64.b64decode(content, validate=True)
        except Exception as exc:
            raise IterationError("Invalid base64 file.") from exc
    else:
        raise IterationError("Encoding must be utf-8 or base64.")
    if len(result) > MAX_FILE:
        raise IterationError("One file exceeds the 16 MiB alpha limit.")
    if SECRET.search(result.decode("utf-8", errors="ignore")):
        raise IterationError("A likely private credential was detected; remove it before packaging.", "possible_secret")
    return result

def read_archive(data: bytes) -> dict[str, bytes]:
    if len(data) > MAX_ARCHIVE:
        raise IterationError("ZIP exceeds the 128 MiB alpha import limit.")
    files: dict[str, bytes] = {}
    seen: set[str] = set()
    nodes: dict[str, str] = {}
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            if len(z.infolist()) > MAX_FILES:
                raise IterationError("Archive contains too many entries.")
            total = 0
            for info in z.infolist():
                raw = info.filename[:-1] if info.is_dir() else info.filename
                name = canonical(raw)
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode) or info.flag_bits & 1:
                    raise IterationError("Links and encrypted archives are not supported.")
                folded = name.casefold()
                if folded in seen:
                    raise IterationError("Duplicate or case-colliding ZIP path.")
                seen.add(folded)
                parts = name.split("/")
                for i in range(1, len(parts)+1):
                    prefix = "/".join(parts[:i])
                    key = prefix.casefold()
                    if key in nodes and nodes[key] != prefix:
                        raise IterationError("Case-colliding Windows directory names.")
                    nodes[key] = prefix
                if info.is_dir():
                    continue
                if info.file_size > MAX_FILE:
                    raise IterationError("A file exceeds the 16 MiB alpha limit.")
                total += info.file_size
                if total > MAX_TOTAL:
                    raise IterationError("Uncompressed archive is too large.")
                if info.file_size > 1024 * 1024 and info.file_size / max(1, info.compress_size) > 300:
                    raise IterationError("Suspicious archive compression ratio.")
                files[name] = z.read(info)
            for path in files:
                parts = path.split("/")
                if any("/".join(parts[:i]) in files for i in range(1, len(parts))):
                    raise IterationError("File/directory collision in archive.")
    except (zipfile.BadZipFile, RuntimeError, OSError) as exc:
        raise IterationError("Invalid or unreadable ZIP archive.") from exc
    if not files:
        raise IterationError("Archive has no files.")
    return files

def validate_schema(value, schema: dict, path: str = "arguments") -> None:
    """Subset used by our tool schemas; schemas deliberately avoid refs/combinators."""
    t = schema.get("type")
    types = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool, "number": (int, float)}
    if t in types and (not isinstance(value, types[t]) or (t in ("integer", "number") and isinstance(value, bool))):
        raise IterationError(f"{path}: expected {t}.")
    if "enum" in schema and value not in schema["enum"]:
        raise IterationError(f"{path}: value is not supported.")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        missing = set(schema.get("required", [])) - set(value)
        if missing:
            raise IterationError(f"{path}: missing {', '.join(sorted(missing))}.")
        if schema.get("additionalProperties") is False and set(value) - set(props):
            raise IterationError(f"{path}: unknown argument(s): {', '.join(sorted(set(value)-set(props)))}.")
        for k, v in value.items():
            if k in props:
                validate_schema(v, props[k], f"{path}.{k}")
    if isinstance(value, list):
        if len(value) > schema.get("maxItems", MAX_FILES):
            raise IterationError(f"{path}: too many items.")
        for i, item in enumerate(value):
            validate_schema(item, schema.get("items", {}), f"{path}[{i}]")
    if isinstance(value, str):
        if len(value) > schema.get("maxLength", 24 * 1024 * 1024) or len(value) < schema.get("minLength", 0):
            raise IterationError(f"{path}: text length is outside allowed bounds.")
    if t in ("integer", "number") and (value < schema.get("minimum", -1e30) or value > schema.get("maximum", 1e30)):
        raise IterationError(f"{path}: number is out of range.")
