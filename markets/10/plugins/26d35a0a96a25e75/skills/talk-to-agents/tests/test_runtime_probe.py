"""Offline tests. No credentials, network calls, CLI login, or listeners."""
import importlib.util
import json
import subprocess
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "runtime_probe.py"
SPEC = importlib.util.spec_from_file_location("runtime_probe", MODULE)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


class ProbeTests(unittest.TestCase):
    def test_default_runs_no_commands(self):
        with patch.object(probe.subprocess, "run") as run:
            result = probe.collect()
        run.assert_not_called()
        self.assertEqual(result["systemd_user_manager"]["check"], "not_checked")
        self.assertIn("restart recovery", result["not_tested"])

    def test_default_hides_paths_and_environment_values(self):
        secret = "private-value-that-must-not-print"
        with patch.dict(probe.os.environ, {"HOME": "/" + secret, "XDG_CONFIG_HOME": "/" + secret,
                                           "API_TOKEN": secret}), \
             patch.object(probe.shutil, "which", return_value="/" + secret):
            result = probe.collect(workspace="/" + secret)
        self.assertNotIn(secret, json.dumps(result))
        self.assertTrue(all(result["tools_on_path"].values()))

    def test_absent_directory_not_created(self):
        with patch.object(probe.Path, "is_dir", return_value=False), \
             patch.object(probe.os, "access") as access:
            result = probe.directory_status("/nonexistent/place")
        access.assert_not_called()
        self.assertEqual(result, {"configured": True, "exists": False, "writable": False})

    def test_unset_directory(self):
        self.assertEqual(probe.directory_status(None),
                         {"configured": False, "exists": False, "writable": False})

    def test_unwritable_directory(self):
        with patch.object(probe.Path, "is_dir", return_value=True), \
             patch.object(probe.os, "access", return_value=False):
            self.assertFalse(probe.directory_status("/existing")["writable"])

    def test_directory_denial_not_claimed_missing(self):
        with patch.object(probe.Path, "is_dir", side_effect=PermissionError):
            self.assertIsNone(probe.directory_status("/restricted")["exists"])

    def test_missing_systemctl_does_not_run(self):
        run = Mock()
        self.assertEqual(probe.systemd_status(None, run)["check"], "unavailable")
        run.assert_not_called()

    def test_systemd_running_is_read_only_and_bounded(self):
        run = Mock(return_value=SimpleNamespace(stdout="running\n", stderr="", returncode=0))
        result = probe.systemd_status("/usr/bin/systemctl", run)
        self.assertTrue(result["manager_reachable"])
        args, kwargs = run.call_args
        self.assertEqual(args[0], ["/usr/bin/systemctl", "--user", "is-system-running"])
        self.assertEqual(kwargs["timeout"], 3)
        self.assertEqual(kwargs["stdin"], subprocess.DEVNULL)
        self.assertNotIn("shell", kwargs)

    def test_degraded_manager_still_reachable_not_persistence_proof(self):
        run = Mock(return_value=SimpleNamespace(stdout="degraded\n", stderr="", returncode=1))
        self.assertTrue(probe.systemd_status("systemctl", run)["manager_reachable"])

    def test_offline_manager(self):
        run = Mock(return_value=SimpleNamespace(stdout="offline\n", stderr="", returncode=1))
        self.assertFalse(probe.systemd_status("systemctl", run)["manager_reachable"])

    def test_timed_out_probe(self):
        run = Mock(side_effect=subprocess.TimeoutExpired("systemctl", 3))
        self.assertEqual(probe.systemd_status("systemctl", run)["check"], "timed_out")

    def test_denied_probe(self):
        run = Mock(side_effect=PermissionError)
        self.assertEqual(probe.systemd_status("systemctl", run)["check"], "denied")

    def test_denied_output_not_echoed(self):
        run = Mock(return_value=SimpleNamespace(stdout="", stderr="Operation not permitted: secret", returncode=1))
        result = probe.systemd_status("systemctl", run)
        self.assertEqual(result["check"], "denied")
        self.assertNotIn("secret", json.dumps(result))

    def test_denial_takes_precedence_over_unknown_state(self):
        run = Mock(return_value=SimpleNamespace(stdout="unknown\n", stderr="Operation not permitted", returncode=1))
        result = probe.systemd_status("systemctl", run)
        self.assertEqual(result["check"], "denied")
        self.assertIsNone(result["manager_reachable"])

    def test_unknown_output_never_echoed(self):
        run = Mock(return_value=SimpleNamespace(stdout="private data", stderr="secret", returncode=1))
        result = probe.systemd_status("systemctl", run)
        self.assertEqual(result["check"], "unconfirmed")
        self.assertNotIn("secret", json.dumps(result))
        self.assertNotIn("private data", json.dumps(result))

    def test_non_linux_no_service_command(self):
        with patch.object(probe.platform, "system", return_value="Darwin"), \
             patch.object(probe.subprocess, "run") as run:
            result = probe.collect(check_systemd=True)
        run.assert_not_called()
        self.assertEqual(result["systemd_user_manager"]["check"], "not_applicable")


if __name__ == "__main__":
    unittest.main()
