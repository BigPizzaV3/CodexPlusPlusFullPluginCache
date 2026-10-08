#!/usr/bin/env python3
"""Unit tests for validate_graph_state.py."""

from __future__ import annotations

import copy
import unittest

from validate_graph_state import validate_state


def node(
    node_id: str,
    *,
    status: str = "PASSED",
    depends_on: list[str] | None = None,
    access: str = "read-only",
    approval: str = "not-required",
    evidence: list[str] | None = None,
    attempt: int | None = None,
    max_attempts: int = 1,
    status_history: list[str] | None = None,
) -> dict:
    if status_history is None:
        status_history = {
            "PENDING": ["PENDING"],
            "READY": ["PENDING", "READY"],
            "RUNNING": ["PENDING", "READY", "RUNNING"],
            "PASSED": ["PENDING", "READY", "RUNNING", "PASSED"],
            "FAILED": ["PENDING", "READY", "RUNNING", "FAILED"],
            "BLOCKED": ["PENDING", "BLOCKED"],
            "NEEDS_APPROVAL": ["PENDING", "NEEDS_APPROVAL"],
            "SKIPPED": ["PENDING", "SKIPPED"],
        }[status]
    if attempt is None:
        attempt = status_history.count("RUNNING")
    return {
        "id": node_id,
        "title": node_id.replace("-", " ").title(),
        "kind": "verify",
        "role": "tool",
        "access": access,
        "status": status,
        "status_history": status_history,
        "depends_on": depends_on or [],
        "expected_output": "Verified result",
        "evidence_required": True,
        "evidence": ["test output"] if evidence is None and status == "PASSED" else (evidence or []),
        "attempt": attempt,
        "max_attempts": max_attempts,
        "approval": approval,
    }


def state(*nodes: dict, status: str = "COMPLETE") -> dict:
    return {
        "schema_version": 1,
        "run_id": "graph-test",
        "task": "Test the validator",
        "status": status,
        "nodes": list(nodes),
    }


class GraphStateValidatorTests(unittest.TestCase):
    def assert_has_error(self, payload: dict, fragment: str) -> None:
        errors = validate_state(payload)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_complete_graph(self) -> None:
        payload = state(node("scope"), node("verify", depends_on=["scope"]))
        self.assertEqual(validate_state(payload), [])

    def test_duplicate_ids(self) -> None:
        self.assert_has_error(state(node("same"), node("same")), "duplicate node id")

    def test_missing_dependency(self) -> None:
        self.assert_has_error(state(node("verify", depends_on=["missing"])), "missing dependency")

    def test_dependency_cycle(self) -> None:
        payload = state(node("a", depends_on=["b"]), node("b", depends_on=["a"]))
        self.assert_has_error(payload, "dependency cycle detected")

    def test_attempt_exceeds_limit(self) -> None:
        retry_history = ["PENDING", "READY", "RUNNING", "FAILED", "READY", "RUNNING", "PASSED"]
        payload = state(node("verify", status_history=retry_history, attempt=2, max_attempts=1))
        self.assert_has_error(payload, "attempt exceeds max_attempts")

    def test_ready_before_dependency_resolves(self) -> None:
        payload = state(
            node("scope", status="RUNNING"),
            node("verify", status="READY", depends_on=["scope"]),
            status="RUNNING",
        )
        self.assert_has_error(payload, "active before dependencies resolved")

    def test_passed_evidence_is_required(self) -> None:
        payload = state(node("verify", evidence=[]))
        self.assert_has_error(payload, "passed node requires evidence")

    def test_external_write_requires_approval(self) -> None:
        payload = state(node("publish", access="external-write", approval="required"))
        self.assert_has_error(payload, "gated access requires granted approval")

    def test_external_write_with_approval_is_valid(self) -> None:
        payload = state(node("publish", access="external-write", approval="granted"))
        self.assertEqual(validate_state(payload), [])

    def test_illegal_transition(self) -> None:
        payload = state(node("verify", status_history=["PENDING", "PASSED"], attempt=0))
        self.assert_has_error(payload, "illegal transition PENDING -> PASSED")

    def test_terminal_run_consistency(self) -> None:
        payload = state(node("verify", status="RUNNING"), status="COMPLETE")
        self.assert_has_error(payload, "COMPLETE requires every node")

    def test_input_is_not_mutated(self) -> None:
        payload = state(node("scope"))
        original = copy.deepcopy(payload)
        validate_state(payload)
        self.assertEqual(payload, original)


if __name__ == "__main__":
    unittest.main()
