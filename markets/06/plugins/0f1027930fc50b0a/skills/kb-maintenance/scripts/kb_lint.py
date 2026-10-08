#!/usr/bin/env python3
"""Read-only KB checks with explicit project conventions and coverage."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
    from markdown_it import MarkdownIt
    DEPENDENCY_ERROR = None
except ImportError as error:
    DEPENDENCY_ERROR = str(error)

DEFAULTS = {
    "work_dirs": ["00_System/Work/Active"],
    "decision_dirs": ["00_System/Decisions/Records"],
    "archive_dirs": ["99_Archive"],
    "archive_names": ["Archive"],
    "hot_names": ["AGENTS.md", "CLAUDE.md", "PROJECT_STATE.md", "_Context.md"],
    "context_names": ["_Context.md"],
    "exclude_dirs": [".git", ".obsidian", ".agents", ".claude", ".codex", ".venv",
                     "node_modules", "Library", "Temp", "Logs"],
    "required_metadata": ["type", "project", "status"],
    "valid_statuses": ["draft", "review", "active", "temporary", "deprecated", "superseded", "archived"],
    "inactive_statuses": ["deprecated", "superseded", "archived"],
    "canonical_key_fields": ["domain", "feature"],
    "decision_id_fields": ["decision_id", "id"],
    "decision_id_pattern": r"DEC-\d{4}-\d{3}",
    "link_types": ["wikilinks", "markdown"],
}
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def issue(kind, path, message, severity="warning"):
    return {"severity": severity, "kind": kind, "path": path, "message": message}


def under(rel, directories):
    return any(rel == directory or rel.startswith(directory + "/") for directory in directories)


def load_profile(root, config):
    path = Path(config).resolve() if config else root / ".kb-lint.json"
    overrides = {}
    if config or path.exists():
        overrides = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(overrides, dict) or overrides.keys() - DEFAULTS.keys():
            raise ValueError("profile must be an object containing only documented keys")
    for key, value in overrides.items():
        if key == "decision_id_pattern":
            if not isinstance(value, str) or not value:
                raise ValueError("decision_id_pattern must be a nonempty regular expression")
            pattern = re.compile(value)
            if pattern.match(""):
                raise ValueError("decision_id_pattern must not match an empty identifier")
        elif not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
            raise ValueError(f"{key} must be a list of nonempty strings")
    profile = {**DEFAULTS, **overrides}
    for key in ("work_dirs", "decision_dirs", "archive_dirs", "exclude_dirs"):
        for value in profile[key]:
            p = Path(value)
            if p.is_absolute() or ".." in p.parts or value in (".", "") or "\\" in value:
                raise ValueError(f"{key} must contain vault-relative paths without '..'")
        profile[key] = [Path(value).as_posix() for value in profile[key]]
    if set(profile["link_types"]) - {"wikilinks", "markdown"}:
        raise ValueError("link_types supports only wikilinks and markdown")
    if not profile["canonical_key_fields"] or not profile["decision_id_fields"]:
        raise ValueError("canonical_key_fields and decision_id_fields must not be empty")
    if set(profile["inactive_statuses"]) - set(profile["valid_statuses"]):
        raise ValueError("inactive_statuses must be included in valid_statuses")
    return profile, str(path) if config or path.exists() else "built-in source-KB defaults"


def parse_document(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    metadata = yaml.safe_load(match[1])
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict) or any(not isinstance(key, str) for key in metadata):
        raise ValueError("frontmatter must be a YAML mapping with string keys")
    return metadata, text[match.end():]


def scalar(metadata, key):
    value = metadata.get(key)
    if value is None:
        return ""
    if isinstance(value, (dict, list, set)):
        raise ValueError(f"`{key}` must be a scalar")
    return str(value).strip()


def markdown_content(body):
    tokens = MarkdownIt("commonmark").parse(body)
    links, wiki, heading = [], [], ""
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and token.tag == "h1" and not heading:
            heading = tokens[index + 1].content
        if token.type != "inline":
            continue
        for child in token.children or []:
            if child.type == "link_open":
                links.append(child.attrGet("href"))
            elif child.type == "image":
                links.append(child.attrGet("src"))
            elif child.type == "text":
                wiki.extend(WIKILINK_RE.findall(child.content))
    return links, wiki, heading


def resolve_wikilink(root, source, target, by_stem, by_rel):
    target = target.strip().replace("\\", "/")
    if Path(target).suffix and not target.lower().endswith(".md"):
        for base in (source.parent, root):
            candidate = (base / target.lstrip("/")).resolve()
            if candidate.is_relative_to(root) and candidate.is_file():
                return [candidate]
    if target.lower().endswith(".md"):
        target = target[:-3]
    if "/" not in target:
        return by_stem.get(target.casefold(), [])
    bases = [source.parent] if target.startswith(("./", "../")) else [root, source.parent]
    for base in bases:
        candidate = (base / target.lstrip("/")).resolve()
        if candidate.is_relative_to(root):
            hits = by_rel.get(candidate.relative_to(root).as_posix().casefold(), [])
            if hits:
                return hits
    return []


def emit(root, issues, files_scanned, coverage, as_json):
    counts = Counter(item["severity"] for item in issues)
    result = {"root": str(root), "files_scanned": files_scanned,
              "issue_count": len(issues), "counts": dict(counts), "issues": issues,
              "coverage": coverage,
              "unresolved_link_check": coverage.get("unresolved_links", "not_run")}
    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"KB lint: {files_scanned} Markdown files, {len(issues)} issues")
        print("Coverage: " + json.dumps(coverage, sort_keys=True))
        for item in issues:
            print(f"[{item['severity'].upper()}] {item['kind']}: {item['path']} - {item['message']}")
    return 1 if counts.get("error", 0) else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", help="Target vault directory (required)")
    parser.add_argument("--config", help="JSON project profile; defaults to <root>/.kb-lint.json")
    parser.add_argument("--stale-work-days", type=int, default=30)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--skip-unresolved-links", action="store_true",
                        help="Skip missing link targets for partial audits; report reduced coverage")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        if not root.is_dir():
            raise ValueError("vault root must be an existing directory")
        if args.stale_work_days < 0:
            raise ValueError("--stale-work-days must be nonnegative")
        if DEPENDENCY_ERROR:
            requirements = Path(__file__).resolve().parents[1] / "requirements.txt"
            raise ValueError(f"{DEPENDENCY_ERROR}; install runtime dependencies from {requirements}")
        profile, profile_source = load_profile(root, args.config)
    except (OSError, ValueError, re.error) as error:
        emit(root, [issue("input", str(root), str(error), "error")], 0,
             {"status": "invalid"}, args.json)
        return 2

    issues, files = [], []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part in profile["exclude_dirs"] for part in relative.parts[:-1]) or under(relative.as_posix(), profile["exclude_dirs"]):
            continue
        if not path.resolve().is_relative_to(root):
            issues.append(issue("outside-root", relative.as_posix(), "symlink target is outside vault", "error"))
        elif path.is_file():
            files.append(path)

    by_stem, by_rel = defaultdict(list), defaultdict(list)
    for path in files:
        by_stem[path.stem.casefold()].append(path)
        by_rel[path.relative_to(root).with_suffix("").as_posix().casefold()].append(path)

    def archived(path):
        rel = path.relative_to(root)
        return under(rel.as_posix(), profile["archive_dirs"]) or any(part in profile["archive_names"] for part in rel.parts[:-1])

    canonical, decisions = defaultdict(list), defaultdict(list)
    matched = {key: {directory: 0 for directory in profile[key]} for key in ("work_dirs", "decision_dirs")}
    scanned = 0
    for path in files:
        rel = path.relative_to(root).as_posix()
        for directories in matched.values():
            for directory in directories:
                if under(rel, [directory]):
                    directories[directory] += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            issues.append(issue("read", rel, str(error), "error"))
            continue
        scanned += 1
        try:
            metadata, body = parse_document(text)
            status = scalar(metadata, "status").lower()
            for field in set(profile["canonical_key_fields"] + profile["decision_id_fields"] +
                             ["canonical", "last_updated", "last_reviewed", "review_after"]):
                scalar(metadata, field)
        except (yaml.YAMLError, ValueError) as error:
            issues.append(issue("frontmatter", rel, str(error), "error"))
            metadata, body, status = {}, FRONTMATTER_RE.sub("", text, count=1), ""

        if not archived(path):
            for key in profile["required_metadata"]:
                if metadata.get(key) is None or metadata.get(key) == "":
                    issues.append(issue("metadata", rel, f"missing `{key}`"))
            if status and status not in profile["valid_statuses"]:
                issues.append(issue("status", rel, f"invalid lifecycle status `{status}`"))
            if status == "superseded" and not (metadata.get("superseded_by") or metadata.get("replacement")):
                issues.append(issue("superseded-link", rel, "superseded artifact lacks replacement metadata"))
            if scalar(metadata, "canonical").lower() == "true" and status not in profile["inactive_statuses"]:
                key = tuple(scalar(metadata, field).casefold() for field in profile["canonical_key_fields"])
                if any(key):
                    canonical[key].append(rel)
            if metadata.get("review_after"):
                try:
                    date = dt.date.fromisoformat(scalar(metadata, "review_after"))
                    if date < dt.date.today():
                        issues.append(issue("review-after", rel, f"review_after expired on {date}"))
                except ValueError:
                    issues.append(issue("review-after", rel, "invalid review_after date"))

        links, wiki, heading = markdown_content(body)
        if "wikilinks" in profile["link_types"]:
            for target in wiki:
                hits = resolve_wikilink(root, path, target, by_stem, by_rel)
                if not hits and not args.skip_unresolved_links:
                    issues.append(issue("broken-link", rel, f"unresolved wikilink [[{target}]]"))
                elif len(hits) > 1:
                    issues.append(issue("ambiguous-link", rel, f"[[{target}]] resolves to {len(hits)} files"))
                if path.name in profile["hot_names"] and any(archived(hit) for hit in hits):
                    issues.append(issue("hot-to-archive", rel, f"Hot surface links archived [[{target}]]"))
        if "markdown" in profile["link_types"]:
            for target in links:
                try:
                    url = urlsplit(target)
                except ValueError:
                    issues.append(issue("link-syntax", rel, f"invalid URL syntax: {target}"))
                    continue
                if url.scheme or url.netloc or not url.path:
                    continue
                local = unquote(url.path)
                base = root if local.startswith("/") else path.parent
                hit = (base / local.lstrip("/")).resolve()
                if not hit.is_relative_to(root):
                    issues.append(issue("outside-root-link", rel, f"local link leaves vault: {target}"))
                elif not hit.exists() and not args.skip_unresolved_links:
                    issues.append(issue("broken-link", rel, f"unresolved Markdown target: {target}"))
                elif hit.exists() and path.name in profile["hot_names"] and archived(hit):
                    issues.append(issue("hot-to-archive", rel, f"Hot surface links archived {target}"))

        if under(rel, profile["decision_dirs"]):
            pattern = re.compile(profile["decision_id_pattern"])
            identifiers = {scalar(metadata, field) for field in profile["decision_id_fields"] if scalar(metadata, field)}
            if not identifiers:
                # Only a defining heading/filename counts; body references never define records.
                identifiers = {match.group() for value in (heading, path.stem)
                               if (match := pattern.match(value.lstrip("[")))}
            if len(identifiers) == 1 and pattern.fullmatch(next(iter(identifiers))):
                decisions[next(iter(identifiers))].append(rel)
            else:
                issues.append(issue("decision-id", rel, "missing, invalid or conflicting record identifier"))

        if under(rel, profile["work_dirs"]) and status not in profile["inactive_statuses"]:
            stamp = scalar(metadata, "last_updated") or scalar(metadata, "last_reviewed")
            try:
                age = (dt.date.today() - dt.date.fromisoformat(stamp)).days
                if age > args.stale_work_days:
                    issues.append(issue("stale-work", rel, f"active Work artifact is {age} days old"))
            except ValueError:
                issues.append(issue("stale-work", rel, "missing or invalid last_updated/last_reviewed date"))

    for key, paths in canonical.items():
        if len(paths) > 1:
            issues.append(issue("canonical-duplicate", " | ".join(paths), f"multiple current canonical owners for {key}", "error"))
    for identifier, paths in decisions.items():
        if len(paths) > 1:
            issues.append(issue("decision-id", " | ".join(paths), f"duplicate record definition `{identifier}`", "error"))
    for path in files:
        if path.name in profile["context_names"] and not any(other.parent == path.parent and other.name not in profile["context_names"] for other in files):
            issues.append(issue("orphan-context", path.relative_to(root).as_posix(), "context has no sibling Markdown owner"))
    if not scanned:
        issues.append(issue("empty-scope", str(root), "no readable Markdown files; no KB health assessment possible"))
    coverage = {"status": "scanned" if scanned else "empty", "profile": profile_source,
                "conventions": profile, "matched_files": matched,
                "unresolved_links": "skipped" if args.skip_unresolved_links else "enabled",
                "not_checked": ["remote URLs", "heading fragments", "raw HTML links",
                                "undefined Markdown reference labels", "semantic correctness"]}
    return emit(root, issues, scanned, coverage, args.json)


if __name__ == "__main__":
    sys.exit(main())
