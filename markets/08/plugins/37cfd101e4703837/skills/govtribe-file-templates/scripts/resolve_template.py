#!/usr/bin/env python3
"""Resolve exact template bytes and required host capabilities without modifying assets."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROLES = ("master", "example", "preview")
FORMATS = {"docx": "host-document", "xlsx": "host-spreadsheet", "pptx": "host-presentation"}
LEGACY_FORMATS = {"docx": "doc", "xlsx": "spreadsheet", "pptx": "slides"}


def contained_path(root, relative):
    if not isinstance(relative, str) or "\\" in relative:
        raise ValueError("Invalid catalog path")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or any(p in ("", ".", "..") for p in relative.split("/")):
        raise ValueError(f"Unsafe catalog path: {relative}")
    path = (root / relative).resolve(strict=True)
    if not path.is_file() or root.resolve() not in path.parents:
        raise ValueError(f"Catalog path escapes skill or is not a file: {relative}")
    return path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def valid_sha256(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def load_catalog(root=ROOT, expected_catalog_sha256=None):
    data = contained_path(root, "assets/catalog.json").read_bytes()
    sha256 = digest(data)
    if expected_catalog_sha256 is not None and sha256 != expected_catalog_sha256:
        raise ValueError("Selected catalog revision is unavailable (catalog checksum mismatch)")
    catalog = json.loads(data)
    if not isinstance(catalog, dict) or catalog.get("schema_version") not in (1, 2) or not isinstance(catalog.get("templates"), list):
        raise ValueError("Unsupported template catalog schema")
    if not isinstance(catalog.get("library_revision"), str) or not catalog["library_revision"]:
        raise ValueError("Invalid catalog identity")
    neutral = catalog["schema_version"] == 2
    if neutral:
        if catalog.get("adaptation_capability") != "host-editing" or "adaptation_skill" in catalog:
            raise ValueError("Invalid catalog adaptation capability")
    elif not isinstance(catalog.get("adaptation_skill"), str) or not catalog["adaptation_skill"]:
        raise ValueError("Invalid runtime catalog adaptation routing")
    if "source_catalog_sha256" in catalog and not valid_sha256(catalog["source_catalog_sha256"]):
        raise ValueError("Invalid source catalog provenance")
    seen = set()
    for template in catalog["templates"]:
        if not isinstance(template, dict):
            raise ValueError("Invalid template entry")
        template_id = template.get("id", "")
        if not isinstance(template_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", template_id) or template_id in seen:
            raise ValueError(f"Invalid or duplicate template ID: {template_id}")
        seen.add(template_id)
        field = "format_capability" if neutral else "format_skill"
        mapping = FORMATS if neutral else LEGACY_FORMATS
        if template.get("format") not in mapping or template.get(field) != mapping[template["format"]]:
            raise ValueError(f"Invalid format capability or routing: {template_id}")
        if neutral and "format_skill" in template:
            raise ValueError(f"Runtime format routing in shared catalog: {template_id}")
        for required in ("display_name", "domain_skill", "completion_reference"):
            if not isinstance(template.get(required), str) or not template[required]:
                raise ValueError(f"Missing {required}: {template_id}")
        if template["completion_reference"] != f"references/{template_id}.md":
            raise ValueError(f"Invalid completion reference: {template_id}")
        for role in ROLES:
            asset = template.get(role, {})
            if not isinstance(asset, dict) or not isinstance(asset.get("path"), str):
                raise ValueError(f"Missing {role}: {template_id}")
            if not asset["path"].startswith(f"assets/{template_id}/"):
                raise ValueError(f"Unexpected {role} directory: {template_id}")
            if not valid_sha256(asset.get("sha256")) or type(asset.get("bytes")) is not int or asset["bytes"] <= 0:
                raise ValueError(f"Invalid {role} integrity metadata: {template_id}")
            if "source_sha256" in asset or "source_bytes" in asset:
                if not valid_sha256(asset.get("source_sha256")) or type(asset.get("source_bytes")) is not int or asset["source_bytes"] <= 0:
                    raise ValueError(f"Invalid {role} source provenance: {template_id}")
            suffix = PurePosixPath(asset["path"]).suffix
            if suffix != (".png" if role == "preview" else "." + template["format"]):
                raise ValueError(f"Invalid {role} extension: {template_id}")
        if template["master"]["path"] == template["example"]["path"]:
            raise ValueError(f"Master and example must be distinct: {template_id}")
    return catalog, sha256


def resolve(template_id, root=ROOT, expected_catalog_sha256=None, expected_master_sha256=None):
    catalog, catalog_sha256 = load_catalog(root, expected_catalog_sha256)
    template = next((t for t in catalog["templates"] if t["id"] == template_id), None)
    if template is None:
        raise ValueError(f"Unknown template ID: {template_id}")
    if expected_master_sha256 is not None and template["master"]["sha256"] != expected_master_sha256:
        raise ValueError("Selected master revision is unavailable (master checksum mismatch)")
    result = dict(template, library_revision=catalog["library_revision"], catalog_sha256=catalog_sha256)
    route = "adaptation_capability" if catalog["schema_version"] == 2 else "adaptation_skill"
    result[route] = catalog[route]
    if "source_catalog_sha256" in catalog:
        result["source_catalog_sha256"] = catalog["source_catalog_sha256"]
    result["completion_reference_path"] = str(contained_path(root, template["completion_reference"]))
    for role in ROLES:
        asset = template[role]
        path = contained_path(root, asset["path"])
        data = path.read_bytes()
        if len(data) != asset["bytes"] or digest(data) != asset["sha256"]:
            raise ValueError(f"Asset checksum mismatch: {asset['path']}")
        result[role] = dict(asset, absolute_path=str(path))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template_id", nargs="?")
    parser.add_argument("--verify-all", action="store_true")
    parser.add_argument("--expected-catalog-sha256")
    parser.add_argument("--expected-master-sha256")
    args = parser.parse_args()
    if bool(args.template_id) == args.verify_all or (args.verify_all and args.expected_master_sha256):
        parser.error("Select one template ID or --verify-all; expected master applies to one template")
    try:
        if args.verify_all:
            catalog, _ = load_catalog(expected_catalog_sha256=args.expected_catalog_sha256)
            result = [resolve(t["id"], expected_catalog_sha256=args.expected_catalog_sha256) for t in catalog["templates"]]
        else:
            result = resolve(args.template_id, expected_catalog_sha256=args.expected_catalog_sha256,
                             expected_master_sha256=args.expected_master_sha256)
        print(json.dumps({"ok": True, "result": result}, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
