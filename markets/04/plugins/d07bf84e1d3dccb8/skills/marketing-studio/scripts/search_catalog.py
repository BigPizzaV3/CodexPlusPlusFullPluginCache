#!/usr/bin/env python3
"""Return the smallest set of Marketing Studio playbooks for a request."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = SKILL_ROOT / "references" / "catalog.json"
ALIASES = {
    "find": "search discovery",
    "look for": "search discovery",
    "discover": "search discovery",
    "亚马逊": "amazon",
    "虾皮": "shopee",
    "抖音小店": "tiktok shop",
    "达人": "creator influencer",
    "红人": "creator influencer",
    "创作者": "creator influencer",
    "寻找": "search discovery",
    "选品": "product selection",
    "带货": "affiliate ecommerce",
    "素材": "creative material content",
    "脚本": "script content",
    "复盘": "review operations kpi",
    "关键词": "keyword search",
}


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if payload.get("schemaVersion") != 1 or not isinstance(payload.get("skills"), list):
        raise ValueError(f"Unsupported catalog schema in {path}")
    return payload


def expand_query(query: str) -> str:
    expanded = query.casefold()
    additions = [
        value
        for key, value in ALIASES.items()
        if key.casefold() in expanded
    ]
    return " ".join([expanded, *additions])


def tokens(value: str) -> set[str]:
    result: set[str] = set()
    for token in re.findall(r"[a-z0-9]+", value.casefold()):
        if len(token) <= 1:
            continue
        result.add(token)
        if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
            result.add(token[:-1])
    return result


def score_skill(skill: dict[str, Any], query: str) -> int:
    expanded = expand_query(query)
    query_tokens = tokens(expanded)
    code = str(skill["code"]).casefold()
    name = str(skill["name"]).casefold()
    fields = " ".join(
        [
            code,
            name,
            str(skill["platform"]),
            str(skill["category"]),
            *[str(item) for item in skill.get("keywords", [])],
        ]
    ).casefold()
    field_tokens = tokens(fields)
    score = len(query_tokens & field_tokens) * 3
    if code in expanded:
        score += 30
    if name in expanded:
        score += 20
    if str(skill["platform"]).casefold() in expanded:
        score += 8
    if str(skill["category"]).casefold() in expanded:
        score += 4
    return score


def search(
    query: str,
    *,
    platform: str | None = None,
    category: str | None = None,
    limit: int = 3,
    catalog_path: Path = CATALOG_PATH,
) -> list[dict[str, Any]]:
    skills = load_catalog(catalog_path)["skills"]
    candidates = [
        skill
        for skill in skills
        if (platform is None or skill["platform"] == platform)
        and (category is None or skill["category"] == category)
    ]
    ranked = [
        {**skill, "score": score_skill(skill, query)}
        for skill in candidates
    ]
    ranked = [skill for skill in ranked if skill["score"] > 0]
    ranked.sort(key=lambda item: (-item["score"], item["code"]))
    return ranked[:limit]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find the most relevant bundled Marketing Studio playbooks."
    )
    parser.add_argument("query", help="User request or search phrase")
    parser.add_argument("--platform", help="Exact catalog platform filter")
    parser.add_argument("--category", help="Exact catalog category filter")
    parser.add_argument("--limit", type=int, default=3, choices=range(1, 6))
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    matches = search(
        args.query,
        platform=args.platform,
        category=args.category,
        limit=args.limit,
    )
    if args.as_json:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
        return 0
    if not matches:
        print("No matching bundled playbook. Inspect references/catalog.md.")
        return 1
    for index, match in enumerate(matches, start=1):
        requirements = ", ".join(match["requires"]) or "none"
        print(f"{index}. {match['name']} ({match['code']})")
        print(f"   reference: {match['reference']}")
        print(f"   requirements: {requirements}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
