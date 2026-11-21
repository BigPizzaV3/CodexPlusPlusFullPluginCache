#!/usr/bin/env python3
"""Build deterministic release package for OpenAI ChatGPT / Codex plugin."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import sys
import tempfile
import zipfile
from pathlib import Path

FIXED_TIME = (1980, 1, 1, 0, 0, 0)
ROOT = Path(__file__).resolve().parents[1]

def build_package(output_zip: Path) -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        stage = Path(tmpdir) / "bundle"
        stage.mkdir(parents=True, exist_ok=True)

        # Copy required plugin files
        (stage / ".codex-plugin").mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / ".codex-plugin" / "plugin.json", stage / ".codex-plugin" / "plugin.json")
        shutil.copy2(ROOT / "plugin.json", stage / "plugin.json")
        shutil.copy2(ROOT / "README.md", stage / "README.md")
        shutil.copy2(ROOT / "LICENSE", stage / "LICENSE")

        shutil.copytree(ROOT / "skills", stage / "skills")
        shutil.copytree(ROOT / "assets", stage / "assets")
        shutil.copytree(ROOT / "evals", stage / "evals")
        shutil.copytree(ROOT / "scripts", stage / "scripts")
        if (ROOT / "docs").exists():
            shutil.copytree(ROOT / "docs", stage / "docs")

        # Clean OS / temporary files
        for p in stage.rglob(".DS_Store"):
            p.unlink()
        for p in stage.rglob("__pycache__"):
            shutil.rmtree(p)
        for p in stage.rglob("*.py[cod]"):
            p.unlink()

        # Collect directories and files sorted for deterministic archive
        directories: set[str] = set()
        files: list[str] = []
        for current, dirs, names in os.walk(stage, topdown=True, followlinks=False):
            cur = Path(current)
            for name in sorted(dirs):
                rel = (cur / name).relative_to(stage).as_posix() + "/"
                directories.add(rel)
            for name in sorted(names):
                rel = (cur / name).relative_to(stage).as_posix()
                files.append(rel)
                parts = rel.split("/")[:-1]
                for i in range(1, len(parts) + 1):
                    directories.add("/".join(parts[:i]) + "/")

        output_zip.parent.mkdir(parents=True, exist_ok=True)
        tmp_zip = output_zip.with_name(output_zip.name + ".tmp")
        if tmp_zip.exists():
            tmp_zip.unlink()

        with zipfile.ZipFile(tmp_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for rel in sorted(directories):
                info = zipfile.ZipInfo(rel, FIXED_TIME)
                info.create_system = 3
                info.external_attr = (stat.S_IFDIR | 0o755) << 16
                archive.writestr(info, b"")
            for rel in sorted(files):
                file_path = stage.joinpath(*rel.split("/"))
                info = zipfile.ZipInfo(rel, FIXED_TIME)
                info.create_system = 3
                info.compress_type = zipfile.ZIP_DEFLATED
                executable = bool(file_path.stat().st_mode & stat.S_IXUSR)
                mode = 0o755 if executable else 0o644
                info.external_attr = (stat.S_IFREG | mode) << 16
                archive.writestr(info, file_path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

        tmp_zip.replace(output_zip)

    digest = hashlib.sha256(output_zip.read_bytes()).hexdigest()
    return {
        "ok": True,
        "outputPath": str(output_zip.resolve()),
        "sha256": digest,
        "bytes": output_zip.stat().st_size,
        "entries": len(directories) + len(files),
    }

def main():
    dest = ROOT / "dist" / "ask-farouk-about-creative-thinking-v1.0.0.zip"
    if len(sys.argv) > 1:
        dest = Path(sys.argv[1]).resolve()
    result = build_package(dest)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
