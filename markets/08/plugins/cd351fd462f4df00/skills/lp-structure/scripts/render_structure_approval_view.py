#!/usr/bin/env python3
"""Validate authoritative LP structure JSON and render/check its approval view."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import sys
from pathlib import Path


def _load_builder_validator():
    script = (
        Path(__file__).resolve().parents[2]
        / "lp-image-builder"
        / "scripts"
        / "validate_direct_image_manifest.py"
    )
    spec = importlib.util.spec_from_file_location("lp_builder_contract", script)
    if not spec or not spec.loader:
        raise RuntimeError("cannot load lp-image-builder structure validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER = _load_builder_validator()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("structure", type=Path)
    parser.add_argument("approval_view", type=Path)
    parser.add_argument("--source-path", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    structure_path = args.structure.resolve()
    view_path = args.approval_view.resolve()
    try:
        document = BUILDER.load_json(structure_path, "structure document")
        # Draft/partial views are valid outputs too. Rendering verifies declared
        # evidence and scope; it never records a user's approval.
        BUILDER.validate_structure_document(document, structure_path.parent)
        structure_sha = hashlib.sha256(structure_path.read_bytes()).hexdigest()
        expected = BUILDER.render_structure_approval_view(document, args.source_path, structure_sha)
        if args.check:
            BUILDER.validate_structure_approval_view(view_path, document, args.source_path, structure_sha)
            print("OK: structure bindings and scoped review view are valid; no approval granted")
            return 0
        view_path.parent.mkdir(parents=True, exist_ok=True)
        view_path.write_text(expected, encoding="utf-8")
    except (BUILDER.ContractError, OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"OK: wrote scoped review view; no approval granted: {view_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
