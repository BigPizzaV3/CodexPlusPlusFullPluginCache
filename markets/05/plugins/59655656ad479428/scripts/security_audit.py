#!/usr/bin/env python3
"""Deterministic security audit for Empire source trees and release archives."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Iterable

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
MAX_ARCHIVE_ENTRIES = 5_000
MAX_ARCHIVE_COMPRESSED = 100 * 1024 * 1024
MAX_ARCHIVE_UNCOMPRESSED = 512 * 1024 * 1024
MAX_MEMBER_SIZE = 100 * 1024 * 1024
TEXT_SUFFIXES = {".json", ".md", ".ps1", ".py", ".sh", ".txt", ".yaml", ".yml"}
FORBIDDEN_PARTS = {".env", ".git", ".empire", "__pycache__"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".pem", ".p12", ".pfx", ".key"}
SECRET_PATTERNS = {
    "openrouter_key": re.compile(rb"\bsk-or-v1-[A-Za-z0-9_-]{20,}\b"),
    "openai_key": re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    "github_token": re.compile(rb"\b(?:github_pat_|ghp_)[A-Za-z0-9_]{20,}\b"),
    "aws_access_key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    "private_key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "database_credential_url": re.compile(
        rb"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s'\"]+"
    ),
    "assigned_secret": re.compile(
        rb"(?im)^\s*(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|secret)\s*[:=]\s*['\"][^'\"\r\n]{8,}['\"]"
    ),
}
SYNTHETIC_SECRET_PATHS = (
    re.compile(r"(^|/)test_[^/]*\.py$"),
    re.compile(r"(^|/)fixtures/"),
    re.compile(r"(^|/)submission-test-cases\.json$"),
)
SVG_DANGERS = (
    b"<script",
    b"<foreignobject",
    b"javascript:",
    b"onload=",
    b"onclick=",
    b"href=\"http://",
    b"href='http://",
    b"href=\"https://",
    b"href='https://",
)
PERSISTENCE_DANGERS = (
    b"crontab ",
    b"launchctl bootstrap",
    b"runatload",
    b"schtasks ",
    b"systemctl enable",
)


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str
    benchmark: str


def _synthetic_path(name: str) -> bool:
    return any(pattern.search(name) for pattern in SYNTHETIC_SECRET_PATHS)


def _path_safe(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and "\\" not in name


def _secret_hits(files: Iterable[tuple[str, bytes]]) -> tuple[list[str], int]:
    production: list[str] = []
    synthetic = 0
    for name, data in files:
        labels = [label for label, pattern in SECRET_PATTERNS.items() if pattern.search(data)]
        if not labels:
            continue
        if _synthetic_path(name):
            synthetic += len(labels)
        else:
            production.append(f"{name}: {','.join(sorted(labels))}")
    return production, synthetic


def _ast_findings(files: Iterable[tuple[str, bytes]]) -> list[str]:
    findings: list[str] = []
    forbidden_imports = {"pickle", "dill", "marshal"}
    for name, data in files:
        if not name.endswith(".py") or _synthetic_path(name):
            continue
        try:
            tree = ast.parse(data.decode("utf-8"), filename=name)
        except (SyntaxError, UnicodeDecodeError) as exc:
            findings.append(f"{name}: unreadable Python AST ({exc})")
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                modules = [alias.name for alias in node.names] if isinstance(node, ast.Import) else [node.module or ""]
                if any(module.split(".", 1)[0] in forbidden_imports for module in modules):
                    findings.append(f"{name}:{node.lineno}: unsafe serialization import")
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
                findings.append(f"{name}:{node.lineno}: dynamic code execution")
            if (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "os"
                and node.func.attr == "system"
            ):
                findings.append(f"{name}:{node.lineno}: os.system invocation")
            if any(
                keyword.arg == "shell"
                and isinstance(keyword.value, ast.Constant)
                and keyword.value.value is True
                for keyword in node.keywords
            ):
                findings.append(f"{name}:{node.lineno}: subprocess shell=True")
    return findings


def _svg_findings(files: Iterable[tuple[str, bytes]]) -> list[str]:
    findings: list[str] = []
    for name, data in files:
        if not name.endswith(".svg"):
            continue
        lowered = data.lower().replace(b" ", b"")
        hits = [value.decode("ascii") for value in SVG_DANGERS if value in lowered]
        if hits:
            findings.append(f"{name}: {','.join(hits)}")
    return findings


def _persistence_findings(files: Iterable[tuple[str, bytes]]) -> list[str]:
    findings: list[str] = []
    for name, data in files:
        if _synthetic_path(name) or name.endswith("/security_audit.py"):
            continue
        if Path(name).suffix.lower() not in {".sh", ".ps1", ".py"}:
            continue
        lowered = data.lower()
        hits = [value.decode("ascii") for value in PERSISTENCE_DANGERS if value in lowered]
        if hits:
            findings.append(f"{name}: {','.join(hits)}")
    return findings


def _skill_findings(files: dict[str, bytes]) -> list[str]:
    findings: list[str] = []
    identities: set[str] = set()
    manifest = json.loads(files[".codex-plugin/plugin.json"].decode("utf-8"))
    plugin_name = str(manifest.get("name", ""))
    for name, data in files.items():
        if not re.fullmatch(r"skills/[^/]+/SKILL\.md", name):
            continue
        text = data.decode("utf-8")
        match = re.match(r"^---\n(.*?)\n---\n(.+)$", text, re.S)
        if not match:
            findings.append(f"{name}: malformed or empty frontmatter/body")
            continue
        frontmatter, body = match.groups()
        skill_name_match = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)", frontmatter)
        description_match = re.search(r"(?m)^description:\s*['\"]?([^'\"\n]+)", frontmatter)
        skill_name = skill_name_match.group(1).strip() if skill_name_match else ""
        description = description_match.group(1).strip() if description_match else ""
        identity = f"{plugin_name}:{skill_name}"
        if not skill_name or not description or not body.strip():
            findings.append(f"{name}: required skill metadata missing")
        if len(description) > 1_024 or len(identity) > 64:
            findings.append(f"{name}: skill metadata exceeds portal limits")
        if identity in identities:
            findings.append(f"{name}: duplicate skill identity")
        identities.add(identity)
    if len(identities) != 9:
        findings.append(f"expected 9 skills, found {len(identities)}")
    return findings


def _checks(files: dict[str, bytes], *, archive: Path | None) -> list[Check]:
    names = sorted(files)
    path_findings = [name for name in names if not _path_safe(name)]
    forbidden = [
        name
        for name in names
        if any(part in FORBIDDEN_PARTS for part in PurePosixPath(name).parts)
        or PurePosixPath(name).suffix.lower() in FORBIDDEN_SUFFIXES
        or name.startswith(("/Users/", "/home/"))
        or re.match(r"^[A-Za-z]:/Users/", name)
    ]
    production_secrets, synthetic_secret_count = _secret_hits(files.items())
    ast_findings = _ast_findings(files.items())
    svg_findings = _svg_findings(files.items())
    persistence_findings = _persistence_findings(files.items())
    skill_findings = _skill_findings(files)
    archive_limit_findings: list[str] = []
    if archive is not None:
        compressed = archive.stat().st_size
        uncompressed = sum(len(value) for value in files.values())
        if compressed > MAX_ARCHIVE_COMPRESSED:
            archive_limit_findings.append("compressed archive exceeds 100 MB")
        if uncompressed > MAX_ARCHIVE_UNCOMPRESSED:
            archive_limit_findings.append("archive expands beyond 512 MiB")
        if len(files) > MAX_ARCHIVE_ENTRIES:
            archive_limit_findings.append("archive has more than 5,000 entries")
        if any(len(value) > MAX_MEMBER_SIZE for value in files.values()):
            archive_limit_findings.append("archive member exceeds 100 MiB")
    return [
        Check("archive_paths", not path_findings, f"unsafe={len(path_findings)}", "OpenAI plugin archive checks"),
        Check("archive_limits", not archive_limit_findings, "; ".join(archive_limit_findings) or "within portal limits", "OpenAI plugin archive checks"),
        Check("private_artifacts", not forbidden, f"forbidden={len(forbidden)}", "NIST SSDF PS.3 / OWASP LLM03"),
        Check("production_secrets", not production_secrets, f"production_hits={len(production_secrets)}; synthetic_test_hits={synthetic_secret_count}", "OWASP LLM02:2025"),
        Check("dangerous_python", not ast_findings, f"findings={len(ast_findings)}", "NIST SSDF PW.5"),
        Check("active_svg_content", not svg_findings, f"findings={len(svg_findings)}", "OWASP LLM03:2025"),
        Check("persistence_installers", not persistence_findings, f"findings={len(persistence_findings)}", "OpenAI skill security scan"),
        Check("skill_contracts", not skill_findings, f"findings={len(skill_findings)}", "OpenAI skill submission checks"),
    ]


def _directory_files(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }


def _archive_files(path: Path) -> dict[str, bytes]:
    if path.stat().st_size > MAX_ARCHIVE_COMPRESSED:
        return {}
    with zipfile.ZipFile(path) as archive:
        result: dict[str, bytes] = {}
        for info in archive.infolist():
            if info.is_dir():
                continue
            if info.filename in result:
                raise ValueError(f"duplicate archive member: {info.filename}")
            if info.file_size > MAX_MEMBER_SIZE:
                raise ValueError(f"oversized archive member: {info.filename}")
            result[info.filename] = archive.read(info)
        return result


def audit(*, plugin_root: Path, archive: Path | None = None) -> dict[str, object]:
    files = _archive_files(archive) if archive else _directory_files(plugin_root)
    required = {".codex-plugin/plugin.json"}
    if not required.issubset(files):
        raise ValueError("plugin manifest is missing")
    checks = _checks(files, archive=archive)
    passed = all(check.passed for check in checks)
    digest = hashlib.sha256()
    for name in sorted(files):
        digest.update(name.encode("utf-8") + b"\0" + files[name] + b"\0")
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target": str(archive or plugin_root),
        "content_digest_sha256": digest.hexdigest(),
        "file_count": len(files),
        "passed": passed,
        "benchmarks": [
            "OpenAI plugin submission security scan requirements",
            "OWASP Top 10 for LLM Applications 2025 (mapped controls only)",
            "NIST SP 800-218 SSDF 1.1 (mapped practices only)",
        ],
        "checks": [asdict(check) for check in checks],
        "claim_boundary": "Automated checks reduce known risks; they are not certification, penetration testing, or proof of zero vulnerabilities.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", type=Path, default=PLUGIN_ROOT)
    parser.add_argument("--archive", type=Path)
    args = parser.parse_args()
    result = audit(
        plugin_root=args.plugin_root.resolve(),
        archive=args.archive.resolve() if args.archive else None,
    )
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
