#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SHARED_REFERENCES_ROOT = PLUGIN_ROOT / "shared-references"
SKILLS_ROOT = PLUGIN_ROOT / "skills"
CONSUMERS_PATH = SHARED_REFERENCES_ROOT / "consumers.json"
GENERATED_REFERENCE_DIRECTORY = Path("references") / "_shared"


def _load_consumers() -> dict[str, list[str]]:
    raw_consumers = json.loads(CONSUMERS_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw_consumers, dict):
        raise ValueError(f"{CONSUMERS_PATH} must contain an object")

    consumers: dict[str, list[str]] = {}
    for reference_name, skill_names in raw_consumers.items():
        if not isinstance(reference_name, str) or (
            PurePosixPath(reference_name).name != reference_name
        ):
            raise ValueError(f"Invalid shared reference name: {reference_name!r}")
        if not isinstance(skill_names, list) or not skill_names:
            raise ValueError(f"{reference_name} must have at least one consuming skill")
        if any(
            not isinstance(skill_name, str) or PurePosixPath(skill_name).name != skill_name
            for skill_name in skill_names
        ):
            raise ValueError(f"{reference_name} has an invalid skill name")
        if len(skill_names) != len(set(skill_names)):
            raise ValueError(f"{reference_name} lists a consuming skill more than once")
        consumers[reference_name] = skill_names
    return consumers


def _expected_copies(consumers: dict[str, list[str]]) -> dict[Path, bytes]:
    expected: dict[Path, bytes] = {}
    for reference_name, skill_names in consumers.items():
        source = SHARED_REFERENCES_ROOT / reference_name
        if not source.is_file():
            raise ValueError(f"Missing canonical shared reference: {source}")
        source_bytes = source.read_bytes()
        for skill_name in skill_names:
            skill_root = SKILLS_ROOT / skill_name
            if not (skill_root / "SKILL.md").is_file():
                raise ValueError(f"Missing consuming skill: {skill_root}")
            destination = skill_root / GENERATED_REFERENCE_DIRECTORY / reference_name
            expected[destination] = source_bytes
    return expected


def _find_existing_copies() -> set[Path]:
    return set(SKILLS_ROOT.glob("*/references/_shared/*.md"))


def _check(expected: dict[Path, bytes]) -> list[str]:
    failures: list[str] = []
    for destination, expected_bytes in expected.items():
        if not destination.is_file():
            failures.append(f"missing generated copy: {destination}")
        elif destination.read_bytes() != expected_bytes:
            failures.append(f"out-of-date generated copy: {destination}")
    for stale_path in sorted(_find_existing_copies() - set(expected)):
        failures.append(f"stale generated copy: {stale_path}")
    return failures


def _materialize(expected: dict[Path, bytes]) -> None:
    for destination, source_bytes in expected.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists() or destination.read_bytes() != source_bytes:
            destination.write_bytes(source_bytes)
    for stale_path in _find_existing_copies() - set(expected):
        stale_path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Materialize Ads Manager shared references into consuming skill bundles."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when generated skill-local copies are missing, stale, or unexpected.",
    )
    args = parser.parse_args()

    expected = _expected_copies(_load_consumers())
    if args.check:
        failures = _check(expected)
        if failures:
            print("\n".join(failures))
            return 1
        return 0

    _materialize(expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
