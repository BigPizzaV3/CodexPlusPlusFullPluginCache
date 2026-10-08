from __future__ import annotations

import json
import re
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PLUGIN_ROOT / "skills"
SHARED_REFERENCES_ROOT = PLUGIN_ROOT / "shared-references"
SHARED_REFERENCE_CONSUMERS_PATH = SHARED_REFERENCES_ROOT / "consumers.json"
MARKDOWN_LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")


def _assert_explicit_reference_loading(
    skill_name: str,
    relative_paths: tuple[str, ...],
) -> None:
    skill_path = SKILLS_ROOT / skill_name / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")

    assert "read and follow every" in skill
    assert "load all of them before" in skill
    for relative_path in relative_paths:
        assert f"]({relative_path})" in skill
        assert (skill_path.parent / relative_path).is_file(), relative_path


def _shared_reference_consumers() -> dict[str, list[str]]:
    return json.loads(SHARED_REFERENCE_CONSUMERS_PATH.read_text(encoding="utf-8"))


def _relative_markdown_links(markdown: str) -> list[str]:
    relative_links: list[str] = []
    for match in MARKDOWN_LINK_PATTERN.finditer(markdown):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        target = target.partition("#")[0]
        if (
            not target
            or "://" in target
            or target.startswith("mailto:")
            or not target.endswith(".md")
        ):
            continue
        relative_links.append(target)
    return relative_links


def test_shared_reference_copies_match_canonical_sources() -> None:
    expected_copies: set[Path] = set()
    for reference_name, skill_names in _shared_reference_consumers().items():
        source = SHARED_REFERENCES_ROOT / reference_name
        assert source.is_file(), reference_name
        source_bytes = source.read_bytes()
        for skill_name in skill_names:
            copy = SKILLS_ROOT / skill_name / "references" / "_shared" / reference_name
            assert copy.is_file(), copy
            assert copy.read_bytes() == source_bytes, copy
            expected_copies.add(copy)

    assert set(SKILLS_ROOT.glob("*/references/_shared/*.md")) == expected_copies


def test_every_relative_markdown_link_stays_inside_its_skill_bundle() -> None:
    for skill_root in sorted(SKILLS_ROOT.iterdir()):
        if not (skill_root / "SKILL.md").is_file():
            continue
        for markdown_path in skill_root.rglob("*.md"):
            markdown = markdown_path.read_text(encoding="utf-8")
            for relative_path in _relative_markdown_links(markdown):
                assert not relative_path.startswith("/"), (
                    markdown_path,
                    relative_path,
                )
                assert all(part not in {"", ".", ".."} for part in relative_path.split("/")), (
                    markdown_path,
                    relative_path,
                )
                target = (markdown_path.parent / relative_path).resolve()
                assert target.is_relative_to(skill_root.resolve()), (
                    markdown_path,
                    relative_path,
                )
                assert target.is_file(), (markdown_path, relative_path)
