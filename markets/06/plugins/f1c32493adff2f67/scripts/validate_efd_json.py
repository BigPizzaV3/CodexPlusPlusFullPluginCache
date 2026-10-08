#!/usr/bin/env python3
"""Validate an EFD 2.1 JSON file without executing untrusted content."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PLUGIN_ROOT / "skills" / "efd-json-forge" / "references" / "efd-2.1.schema.json"
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*-[A-Za-z0-9._-]+$")


def issue(items: list[dict[str, str]], severity: str, path: str, message: str) -> None:
    items.append({"severity": severity, "path": path, "message": message})


def resolve_ref(root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported external schema reference: {ref}")
    value: Any = root
    for token in ref[2:].split("/"):
        value = value[token.replace("~1", "/").replace("~0", "~")]
    return value


def schema_validate(value: Any, rule: dict[str, Any], root: dict[str, Any], path: str, out: list[dict[str, str]]) -> None:
    if "$ref" in rule:
        schema_validate(value, resolve_ref(root, rule["$ref"]), root, path, out)
        return
    expected = rule.get("type")
    type_ok = {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }
    if expected and not type_ok.get(expected, True):
        issue(out, "error", path, f"expected {expected}")
        return
    if "const" in rule and value != rule["const"]:
        issue(out, "error", path, f"must equal {rule['const']!r}")
    if "enum" in rule and value not in rule["enum"]:
        issue(out, "error", path, f"value is not in {rule['enum']!r}")
    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0):
            issue(out, "error", path, "string is too short")
        if "maxLength" in rule and len(value) > rule["maxLength"]:
            issue(out, "error", path, "string is too long")
        if "pattern" in rule and not re.search(rule["pattern"], value):
            issue(out, "error", path, f"does not match {rule['pattern']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in rule and value < rule["minimum"]:
            issue(out, "error", path, f"must be >= {rule['minimum']}")
        if "exclusiveMinimum" in rule and value <= rule["exclusiveMinimum"]:
            issue(out, "error", path, f"must be > {rule['exclusiveMinimum']}")
        if "maximum" in rule and value > rule["maximum"]:
            issue(out, "error", path, f"must be <= {rule['maximum']}")
    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            issue(out, "error", path, "array has too few items")
        if rule.get("uniqueItems"):
            encoded = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
            if len(encoded) != len(set(encoded)):
                issue(out, "error", path, "array items must be unique")
        item_rule = rule.get("items")
        if isinstance(item_rule, dict):
            for index, item in enumerate(value):
                schema_validate(item, item_rule, root, f"{path}[{index}]", out)
    if isinstance(value, dict):
        properties = rule.get("properties", {})
        for required in rule.get("required", []):
            if required not in value:
                issue(out, "error", path, f"missing required property {required}")
        if rule.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    issue(out, "error", f"{path}.{key}", "additional property is not allowed")
        for key, child_rule in properties.items():
            if key in value:
                schema_validate(value[key], child_rule, root, f"{path}.{key}", out)


def index_ids(items: Any, path: str, diagnostics: list[dict[str, str]]) -> set[str]:
    result: set[str] = set()
    if not isinstance(items, list):
        return result
    for index, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            continue
        item_id = item["id"]
        if not ID_PATTERN.fullmatch(item_id):
            issue(diagnostics, "error", f"{path}[{index}].id", "invalid stable ID")
        if item_id in result:
            issue(diagnostics, "error", f"{path}[{index}].id", f"duplicate ID {item_id}")
        result.add(item_id)
    return result


def semantic_validate(doc: dict[str, Any], diagnostics: list[dict[str, str]]) -> None:
    units = index_ids(doc.get("organizationUnits"), "$.organizationUnits", diagnostics)
    positions = index_ids(doc.get("positions"), "$.positions", diagnostics)
    ai_workers = index_ids(doc.get("aiWorkers", []), "$.aiWorkers", diagnostics)
    systems = index_ids(doc.get("systemActors", []), "$.systemActors", diagnostics)
    externals = index_ids(doc.get("externalParties", []), "$.externalParties", diagnostics)
    process = doc.get("process") if isinstance(doc.get("process"), dict) else {}
    workspace = doc.get("workspace") if isinstance(doc.get("workspace"), dict) else {}
    project = doc.get("project") if isinstance(doc.get("project"), dict) else {}
    if project.get("workspaceId") != workspace.get("id"):
        issue(diagnostics, "error", "$.project.workspaceId", "workspace reference does not match workspace.id")
    if process.get("projectId") != project.get("id"):
        issue(diagnostics, "error", "$.process.projectId", "project reference does not match project.id")
    for index, position in enumerate(doc.get("positions", [])):
        if not isinstance(position, dict):
            continue
        for unit_index, unit_id in enumerate(position.get("unitIds", [])):
            if unit_id not in units:
                issue(diagnostics, "error", f"$.positions[{index}].unitIds[{unit_index}]", "organization unit reference does not exist")
    stages = index_ids(process.get("stages"), "$.process.stages", diagnostics)
    nodes = process.get("nodes") if isinstance(process.get("nodes"), list) else []
    node_ids = index_ids(nodes, "$.process.nodes", diagnostics)
    edges = process.get("edges") if isinstance(process.get("edges"), list) else []
    edge_ids = index_ids(edges, "$.process.edges", diagnostics)
    registries = [units, positions, ai_workers, systems, externals, stages, node_ids, edge_ids]
    combined = [item_id for registry in registries for item_id in registry]
    if len(combined) != len(set(combined)):
        issue(diagnostics, "error", "$", "stable IDs must be unique across entity registries")
    participant_sets = {"position": positions, "ai_worker": ai_workers, "system": systems, "external_party": externals}

    node_types: dict[str, str] = {}
    incoming = {node_id: 0 for node_id in node_ids}
    outgoing = {node_id: 0 for node_id in node_ids}
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            continue
        node_id = node.get("id")
        if isinstance(node_id, str):
            node_types[node_id] = str(node.get("type", ""))
        if node.get("stageId") not in stages:
            issue(diagnostics, "error", f"$.process.nodes[{index}].stageId", "stage reference does not exist")
        for unit_index, unit_id in enumerate(node.get("unitIds", [])):
            if unit_id not in units:
                issue(diagnostics, "error", f"$.process.nodes[{index}].unitIds[{unit_index}]", "organization unit reference does not exist")
        roles_seen: set[str] = set()
        for raci_index, raci in enumerate(node.get("raci", [])):
            if not isinstance(raci, dict):
                continue
            participant_type = raci.get("participantType")
            participant_id = raci.get("participantId")
            allowed = participant_sets.get(str(participant_type), set())
            if participant_id not in allowed:
                issue(diagnostics, "error", f"$.process.nodes[{index}].raci[{raci_index}].participantId", "participant reference does not exist")
            roles_seen.update(role for role in raci.get("roles", []) if isinstance(role, str))
        if node.get("type") in {"task", "system_action", "approval"}:
            if "R" not in roles_seen:
                issue(diagnostics, "warning", f"$.process.nodes[{index}].raci", "executable node has no Responsible (R)")
            if "A" not in roles_seen:
                issue(diagnostics, "warning", f"$.process.nodes[{index}].raci", "executable node has no Accountable (A)")

    decision_outcomes: dict[str, list[dict[str, Any]]] = {}
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            continue
        source = edge.get("sourceId")
        target = edge.get("targetId")
        if source not in node_ids:
            issue(diagnostics, "error", f"$.process.edges[{index}].sourceId", "source node does not exist")
        else:
            outgoing[source] += 1
        if target not in node_ids:
            issue(diagnostics, "error", f"$.process.edges[{index}].targetId", "target node does not exist")
        else:
            incoming[target] += 1
        if source in node_ids and node_types.get(source) == "decision":
            decision_outcomes.setdefault(source, []).append(edge)
    if not any(node_types.get(node_id) == "start" for node_id in node_ids):
        issue(diagnostics, "error", "$.process.nodes", "process has no start node")
    if not any(node_types.get(node_id) == "end" for node_id in node_ids):
        issue(diagnostics, "error", "$.process.nodes", "process has no end node")
    for node_id in node_ids:
        if incoming[node_id] == 0 and outgoing[node_id] == 0 and len(node_ids) > 1:
            issue(diagnostics, "warning", f"$.process.nodes[id={node_id}]", "node is isolated")
        if node_types.get(node_id) == "decision":
            branches = decision_outcomes.get(node_id, [])
            if len(branches) < 2:
                issue(diagnostics, "error", f"$.process.nodes[id={node_id}]", "decision requires at least two outgoing branches")
            for branch in branches:
                if not str(branch.get("label", "")).strip():
                    issue(diagnostics, "error", f"$.process.edges[id={branch.get('id', '?')}].label", "decision branch requires a label")

    layout = doc.get("layout") if isinstance(doc.get("layout"), dict) else {}
    if layout.get("processId") != process.get("id"):
        issue(diagnostics, "error", "$.layout.processId", "layout process reference does not match process.id")
    for index, item in enumerate(layout.get("items", [])):
        if isinstance(item, dict) and item.get("efdId") not in node_ids:
            issue(diagnostics, "error", f"$.layout.items[{index}].efdId", "layout node reference does not exist")
    for index, edge in enumerate(layout.get("edges", [])):
        if isinstance(edge, dict) and edge.get("efdId") not in edge_ids:
            issue(diagnostics, "error", f"$.layout.edges[{index}].efdId", "layout edge reference does not exist")
    mapping = doc.get("drawioMapping") if isinstance(doc.get("drawioMapping"), dict) else {}
    if mapping.get("processId") != process.get("id"):
        issue(diagnostics, "error", "$.drawioMapping.processId", "draw.io mapping process reference does not match process.id")
    valid_efd_ids = node_ids | edge_ids
    for index, cell in enumerate(mapping.get("cells", [])):
        if isinstance(cell, dict) and cell.get("efdId") not in valid_efd_ids:
            issue(diagnostics, "error", f"$.drawioMapping.cells[{index}].efdId", "draw.io cell reference does not exist")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an EW AI EFD 2.1 JSON file")
    parser.add_argument("file", type=Path)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    args = parser.parse_args()
    diagnostics: list[dict[str, str]] = []
    try:
        doc = json.loads(args.file.read_text(encoding="utf-8"))
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        result = {"valid": False, "errors": 1, "warnings": 0, "diagnostics": [{"severity": "error", "path": "$", "message": str(error)}]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    if not isinstance(doc, dict):
        issue(diagnostics, "error", "$", "root must be an object")
    else:
        schema_validate(doc, schema, schema, "$", diagnostics)
        semantic_validate(doc, diagnostics)
    errors = sum(item["severity"] == "error" for item in diagnostics)
    warnings = sum(item["severity"] == "warning" for item in diagnostics)
    print(json.dumps({"valid": errors == 0, "errors": errors, "warnings": warnings, "diagnostics": diagnostics}, ensure_ascii=False, indent=2))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
