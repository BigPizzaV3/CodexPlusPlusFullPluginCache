"""Node runtime discovery under restricted MCP server environments."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from test_mcp_server import load_server


class NodeRuntimeTests(unittest.TestCase):
    def test_packaged_worker_can_spawn_its_node_wrapper_without_node_on_path(self) -> None:
        server = load_server()
        node_runtime = server._node_runtime()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run_directory = root / "run"
            run_directory.mkdir()
            host_bin = root / "host-bin"
            host_bin.mkdir()
            fake_codex = host_bin / "codex"
            fake_codex.write_text(
                "\n".join(
                    [
                        f"#!{sys.executable}",
                        "import json, os, sys",
                        "if sys.argv[1:] == ['--version']:",
                        "    print('codex fixture')",
                        "    raise SystemExit(0)",
                        "sys.stdin.read()",
                        "print(json.dumps({'type': 'thread.started', 'thread_id': 'runtime-thread'}))",
                        "environment = {name: os.environ[name] for name in ('PATH', 'GIT_EXEC_PATH')}",
                        "print(json.dumps({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': json.dumps(environment)}}))",
                        "print(json.dumps({'type': 'turn.completed', 'usage': {'input_tokens': 1, 'output_tokens': 1}}))",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            fake_codex.chmod(0o700)
            environment = {
                "PATH": str(host_bin),
                "CODEX_MCP_NODE_PATH": node_runtime,
                "CODEX_CLI_PATH": str(fake_codex),
                "GIT_EXEC_PATH": str(root / "host-git-helpers"),
            }
            with mock.patch.dict(os.environ, environment, clear=True):
                result = server._run_worker(
                    {"model": "gpt-5.6-sol", "prompt": "Check the worker runtime."},
                    run_directory=run_directory,
                    working_directory=root,
                    read_only=True,
                    log_label="runtime-test",
                    timeout=10,
                )
                self.assertEqual(os.environ["PATH"], str(host_bin))

            self.assertEqual(result["thread_id"], "runtime-thread")
            child_environment = json.loads(result["finalResponse"])
            self.assertEqual(
                child_environment["PATH"],
                os.pathsep.join([str(host_bin), str(Path(node_runtime).parent)]),
            )
            self.assertEqual(child_environment["GIT_EXEC_PATH"], environment["GIT_EXEC_PATH"])

    def test_uses_codex_runtime_hints_without_path(self) -> None:
        server = load_server()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cases = (
                (
                    {"CODEX_BROWSER_USE_NODE_PATH": str(root / "browser-node")},
                    root / "browser-node",
                ),
                (
                    {"CODEX_ELECTRON_RESOURCES_PATH": str(root / "resources")},
                    root / "resources" / "cua_node" / "bin" / "node",
                ),
                (
                    {"CODEX_CLI_PATH": str(root / "cli" / "codex")},
                    root / "cli" / "cua_node" / "bin" / "node",
                ),
            )
            for environment, node in cases:
                with self.subTest(environment=environment):
                    node.parent.mkdir(parents=True, exist_ok=True)
                    node.write_text("#!/bin/sh\nprintf 'v22.0.0\\n'\n", encoding="utf-8")
                    node.chmod(0o700)
                    with mock.patch.dict(os.environ, {"PATH": "", **environment}, clear=True):
                        self.assertEqual(server._node_runtime(), str(node))

    def test_uses_bundled_runtime_without_path(self) -> None:
        server = load_server()
        with tempfile.TemporaryDirectory() as temporary:
            cache_root = Path(temporary)
            node = cache_root / "codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
            node.parent.mkdir(parents=True)
            node.write_text("#!/bin/sh\nprintf 'v22.0.0\\n'\n", encoding="utf-8")
            node.chmod(0o700)
            with mock.patch.dict(
                os.environ, {"XDG_CACHE_HOME": str(cache_root), "PATH": ""}, clear=True
            ):
                self.assertEqual(server._node_runtime(), str(node))

    def test_uses_homebrew_without_path(self) -> None:
        server = load_server()
        node = Path("/opt/homebrew/bin/node")
        with (
            mock.patch.dict(os.environ, {"PATH": ""}, clear=True),
            mock.patch.object(
                server.Path, "is_file", autospec=True, side_effect=lambda path: path == node
            ),
            mock.patch.object(server.os, "access", return_value=True),
            mock.patch.object(
                server.subprocess, "run", return_value=mock.Mock(returncode=0, stdout="v22.0.0\n")
            ),
        ):
            self.assertEqual(server._node_runtime(), str(node))

    def test_skips_unsupported_fallback_runtime(self) -> None:
        server = load_server()
        with tempfile.TemporaryDirectory() as temporary:
            cache_root = Path(temporary)
            node = cache_root / "codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
            node.parent.mkdir(parents=True)
            node.write_text("#!/bin/sh\nprintf 'v16.20.0\\n'\n", encoding="utf-8")
            node.chmod(0o700)
            with (
                mock.patch.dict(
                    os.environ, {"XDG_CACHE_HOME": str(cache_root), "PATH": ""}, clear=True
                ),
                mock.patch.object(
                    server.Path, "is_file", autospec=True, side_effect=lambda path: path == node
                ),
                mock.patch.object(server.shutil, "which", return_value="/existing/node"),
            ):
                self.assertEqual(server._node_runtime(), "/existing/node")
