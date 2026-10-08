#!/usr/bin/env python3
"""Validate a Graph Mode checkpoint using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


RUN_STATUSES = {"PLANNING", "RUNNING", "COMPLETE", "BLOCKED", "NEEDS_APPROVAL", "FAILED"}
NODE_STATUSES = {
    "PENDING",
    "READY",
    "RUNNING",
    "PASSED",
    "FAILED",
    "BLOCKED",
    "NEEDS_APPROVAL",
    "SKIPPED",
}
NODE_KINDS = {
    "scope",
    "explore",
    "execute",
    "verify",
    "review",
    "synthesize",
    "approve",
    "monitor",
    "repair",
}
ROLES = {"main", "explorer", "worker", "reviewer", "tool", "human"}
ACCESS_LEVELS = {"read-only", "workspace-write", "external-write", "destructive"}
APPROVALS = {"not-required", "required", "granted", "denied"}
RESOLVED_DEPENDENCY_STATUSES = {"PASSED", "SKIPPED"}
ACTIVE_AFTER_DEPENDENCIES = {"READY", "RUNNING", "PASSED"}
LEGAL_TRANSITIONS = {
    "PENDING": {"READY", "SKIPPED", "BLOCKED", "NEEDS_APPROVAL"},
    "READY": {"RUNNING", "SKIPPED", "BLOCKED", "NEEDS_APPROVAL"},
    "RUNNING": {"PASSED", "FAILED", "BLOCKED", "NEEDS_APPROVAL"},
    "FAILED": {"READY"},
    "BLOCKED": {"READY"},
    "NEEDS_APPROVAL": {"READY", "BLOCKED", "SKIPPED"},
    "PASSED": set(),
    "SKIPPED": set(),
}


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _require_keys(container: dict[str, Any], keys: set[str], context: str) -> list[str]:
    return [f"{context}: missing required field '{key}'" for key in sorted(keys - container.keys())]


def _validate_status_history(node: dict[str, Any], context: str) -> list[str]:
    errors: list[str] = []
    history = node.get("status_history")
    if not isinstance(history, list) or not history:
        return [f"{context}: status_history must be a non-empty array"]
    if history[0] != "PENDING":
        errors.append(f"{context}: status_history must begin with PENDING")
    if history[-1] != node.get("status"):
        errors.append(f"{context}: status must equal the final status_history entry")
    for index, state in enumerate(history):
        if state not in NODE_STATUSES:
            errors.append(f"{context}: invalid status_history value at index {index}: {state!r}")
    for before, after in zip(history, history[1:]):
        if before in NODE_STATUSES and after not in LEGAL_TRANSITIONS.get(before, set()):
            errors.append(f"{context}: illegal transition {before} -> {after}")
    running_count = sum(state == "RUNNING" for state in history)
    if isinstance(node.get("attempt"), int) and node.get("attempt") != running_count:
        errors.append(
            f"{context}: attempt must equal RUNNING transitions ({running_count}), got {node.get('attempt')}"
        )
    return errors


def _find_cycle(nodes_by_id: dict[str, dict[str, Any]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node_id: str) -> list[str] | None:
        if node_id in visiting:
            start = stack.index(node_id)
            return stack[start:] + [node_id]
        if node_id in visited:
            return None
        visiting.add(node_id)
        stack.append(node_id)
        for dependency in nodes_by_id[node_id].get("depends_on", []):
            if dependency in nodes_by_id:
                cycle = visit(dependency)
                if cycle:
                    return cycle
        stack.pop()
        visiting.remove(node_id)
        visited.add(node_id)
        return None

    for node_id in nodes_by_id:
        cycle = visit(node_id)
        if cycle:
            return cycle
    return None


def validate_state(state: Any) -> list[str]:
    """Return validation errors; an empty list means the state is valid."""
    if not isinstance(state, dict):
        return ["checkpoint root must be a JSON object"]

    errors = _require_keys(state, {"schema_version", "run_id", "task", "status", "nodes"}, "run")
    if state.get("schema_version") != 1:
        errors.append("run: schema_version must be 1")
    if not _is_nonempty_string(state.get("run_id")):
        errors.append("run: run_id must be a non-empty string")
    if not _is_nonempty_string(state.get("task")):
        errors.append("run: task must be a non-empty string")
    if state.get("status") not in RUN_STATUSES:
        errors.append(f"run: invalid status {state.get('status')!r}")

    nodes = state.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        errors.append("run: nodes must be a non-empty array")
        return errors

    required_node_keys = {
        "id",
        "title",
        "kind",
        "role",
        "access",
        "status",
        "status_history",
        "depends_on",
        "expected_output",
        "evidence_required",
        "evidence",
        "attempt",
        "max_attempts",
        "approval",
    }
    nodes_by_id: dict[str, dict[str, Any]] = {}

    for index, raw_node in enumerate(nodes):
        context = f"node[{index}]"
        if not isinstance(raw_node, dict):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(_require_keys(raw_node, required_node_keys, context))
        node_id = raw_node.get("id")
        if not _is_nonempty_string(node_id):
            errors.append(f"{context}: id must be a non-empty string")
        elif node_id in nodes_by_id:
            errors.append(f"{context}: duplicate node id {node_id!r}")
        else:
            nodes_by_id[node_id] = raw_node
        if not _is_nonempty_string(raw_node.get("title")):
            errors.append(f"{context}: title must be a non-empty string")
        if raw_node.get("kind") not in NODE_KINDS:
            errors.append(f"{context}: invalid kind {raw_node.get('kind')!r}")
        if raw_node.get("role") not in ROLES:
            errors.append(f"{context}: invalid role {raw_node.get('role')!r}")
        if raw_node.get("access") not in ACCESS_LEVELS:
            errors.append(f"{context}: invalid access {raw_node.get('access')!r}")
        if raw_node.get("status") not in NODE_STATUSES:
            errors.append(f"{context}: invalid status {raw_node.get('status')!r}")
        if not _is_nonempty_string(raw_node.get("expected_output")):
            errors.append(f"{context}: expected_output must be a non-empty string")
        if not isinstance(raw_node.get("evidence_required"), bool):
            errors.append(f"{context}: evidence_required must be boolean")
        evidence = raw_node.get("evidence")
        if not isinstance(evidence, list) or any(not _is_nonempty_string(item) for item in evidence):
            errors.append(f"{context}: evidence must be an array of non-empty strings")
        if raw_node.get("status") == "PASSED" and raw_node.get("evidence_required") and not evidence:
            errors.append(f"{context}: passed node requires evidence")
        attempt = raw_node.get("attempt")
        max_attempts = raw_node.get("max_attempts")
        if not isinstance(attempt, int) or isinstance(attempt, bool) or attempt < 0:
            errors.append(f"{context}: attempt must be a non-negative integer")
        if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
            errors.append(f"{context}: max_attempts must be a positive integer")
        if isinstance(attempt, int) and isinstance(max_attempts, int) and attempt > max_attempts:
            errors.append(f"{context}: attempt exceeds max_attempts")
        if raw_node.get("approval") not in APPROVALS:
            errors.append(f"{context}: invalid approval {raw_node.get('approval')!r}")
        dependencies = raw_node.get("depends_on")
        if not isinstance(dependencies, list) or any(not _is_nonempty_string(item) for item in dependencies):
            errors.append(f"{context}: depends_on must be an array of non-empty strings")
        elif len(dependencies) != len(set(dependencies)):
            errors.append(f"{context}: depends_on contains duplicates")
        errors.extend(_validate_status_history(raw_node, context))

    for node_id, node in nodes_by_id.items():
        dependencies = node.get("depends_on")
        if not isinstance(dependencies, list):
            continue
        for dependency in dependencies:
            if dependency not in nodes_by_id:
                errors.append(f"node {node_id!r}: missing dependency {dependency!r}")
            elif dependency == node_id:
                errors.append(f"node {node_id!r}: cannot depend on itself")
        if node.get("status") in ACTIVE_AFTER_DEPENDENCIES:
            unresolved = [
                dependency
                for dependency in dependencies
                if dependency in nodes_by_id
                and nodes_by_id[dependency].get("status") not in RESOLVED_DEPENDENCY_STATUSES
            ]
            if unresolved:
                errors.append(f"node {node_id!r}: active before dependencies resolved: {unresolved}")
        if node.get("access") in {"external-write", "destructive"}:
            if node.get("status") in ACTIVE_AFTER_DEPENDENCIES and node.get("approval") != "granted":
                errors.append(f"node {node_id!r}: gated access requires granted approval before activation")
            if node.get("approval") == "denied" and node.get("status") not in {"SKIPPED", "BLOCKED"}:
                errors.append(f"node {node_id!r}: denied approval requires SKIPPED or BLOCKED status")

    cycle = _find_cycle(nodes_by_id)
    if cycle:
        errors.append(f"run: dependency cycle detected: {' -> '.join(cycle)}")

    run_status = state.get("status")
    node_statuses = [node.get("status") for node in nodes_by_id.values()]
    if run_status == "PLANNING" and any(status != "PENDING" for status in node_statuses):
        errors.append("run: PLANNING requires every node to be PENDING")
    if run_status == "COMPLETE":
        if not any(status == "PASSED" for status in node_statuses):
            errors.append("run: COMPLETE requires at least one passed node")
        if any(status not in {"PASSED", "SKIPPED"} for status in node_statuses):
            errors.append("run: COMPLETE requires every node to be PASSED or SKIPPED")
    if run_status == "BLOCKED" and "BLOCKED" not in node_statuses:
        errors.append("run: BLOCKED requires at least one blocked node")
    if run_status == "NEEDS_APPROVAL" and "NEEDS_APPROVAL" not in node_statuses:
        errors.append("run: NEEDS_APPROVAL requires at least one node awaiting approval")
    if run_status == "FAILED" and "FAILED" not in node_statuses:
        errors.append("run: FAILED requires at least one failed node")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path, help="Path to Graph Mode state JSON")
    parser.add_argument("--quiet", action="store_true", help="Print only validation errors")
    args = parser.parse_args(argv)

    try:
        with args.checkpoint.open(encoding="utf-8") as handle:
            state = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        print(f"invalid checkpoint: {error}", file=sys.stderr)
        return 1

    errors = validate_state(state)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"Graph state valid: {state['run_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
