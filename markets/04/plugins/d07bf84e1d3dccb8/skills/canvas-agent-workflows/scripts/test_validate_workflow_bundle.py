#!/usr/bin/env python3
"""Unit test entry for canvas-agent-workflows bundle validation."""

from __future__ import annotations

import unittest

import validate_workflow_bundle


class ValidateWorkflowBundleTests(unittest.TestCase):
    def test_bundle_contracts(self) -> None:
        self.assertEqual(validate_workflow_bundle.main(), 0)


if __name__ == "__main__":
    unittest.main()
