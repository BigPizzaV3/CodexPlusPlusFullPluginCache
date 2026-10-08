#!/usr/bin/env python3
"""Deterministic 1-10 publishing feedback loop for Empire LLM Codex."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = PLUGIN_ROOT.parent.parent


def model_icon_root(plugin_root: Path = PLUGIN_ROOT) -> Path:
    return plugin_root / "assets/llm-icons"


def default_input(relative_path: str, packaged_fallback: str) -> Path:
    candidates = (
        Path.cwd() / relative_path,
        REPO_ROOT / relative_path,
        PLUGIN_ROOT / packaged_fallback,
    )
    return next((path for path in candidates if path.is_file()), candidates[0])


DEFAULT_EVIDENCE = default_input(
    "readiness/live-evidence.json", "assets/readiness-evidence.example.json"
)
DEFAULT_PUBLISHING = default_input(
    "readiness/publishing-inputs.json", "assets/publishing-inputs.example.json"
)
DEFAULT_TEST_CASES = default_input(
    "readiness/submission-test-cases.json", "assets/submission-test-cases.json"
)


@dataclass(frozen=True)
class Gate:
    gate_id: str
    label: str
    weight: float
    passed: bool
    detail: str
    next_action: str
    completion: str
    priority: str = "P1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.gate_id,
            "label": self.label,
            "weight": self.weight,
            "earned": self.weight if self.passed else 0.0,
            "passed": self.passed,
            "detail": self.detail,
            "priority": self.priority,
            "next_action": None if self.passed else self.next_action,
            "completion": self.completion,
        }


def load_json(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def frontmatter_name(path: Path) -> str | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return None


def run_offline_tests() -> tuple[bool, str]:
    test_files = [
        PLUGIN_ROOT / "skills/empire-handoff/scripts/test_empire_handoff.py",
        PLUGIN_ROOT / "skills/empire-review/scripts/test_context_policy.py",
        PLUGIN_ROOT / "skills/empire-review/scripts/test_empire_router.py",
        PLUGIN_ROOT / "skills/empire-web-escalation/scripts/test_empire_web.py",
        PLUGIN_ROOT / "scripts/test_empire_benchmarks.py",
        PLUGIN_ROOT / "scripts/test_empire_media.py",
        PLUGIN_ROOT / "scripts/test_empire_present.py",
        PLUGIN_ROOT / "scripts/test_skill_contracts.py",
        PLUGIN_ROOT / "scripts/test_comparative_utility.py",
        PLUGIN_ROOT / "scripts/test_endpoint_benchmark.py",
        PLUGIN_ROOT / "scripts/test_security_audit.py",
        PLUGIN_ROOT / "scripts/test_marketplace_readiness.py",
    ]
    missing = [path.name for path in test_files if not path.is_file()]
    if missing:
        return False, f"offline test files missing: {', '.join(missing)}"
    test_count = 0
    for test_file in test_files:
        proc = subprocess.run(
            [sys.executable, str(test_file)],
            cwd=str(test_file.parent),
            text=True,
            capture_output=True,
            timeout=120,
            env={
                **dict(__import__("os").environ),
                "PYTHONDONTWRITEBYTECODE": "1",
            },
        )
        if proc.returncode != 0:
            return False, f"{test_file.name} failed with exit {proc.returncode}"
        match = re.search(r"Ran (\d+) tests", proc.stdout + proc.stderr)
        if match:
            test_count += int(match.group(1))
    detail = f"{len(test_files)} offline suites passed"
    if test_count:
        detail += f" ({test_count} tests)"
    return True, detail


def evidence_passed(
    evidence: dict[str, Any], key: str, required_fields: tuple[str, ...]
) -> bool:
    item = evidence.get(key)
    return (
        isinstance(item, dict)
        and item.get("passed") is True
        and all(item.get(field) not in (None, "") for field in required_fields)
    )


def is_https(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("https://")


def as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def validate_submission_tests(data: dict[str, Any]) -> tuple[bool, str]:
    positive = as_list(data.get("positive"))
    negative = as_list(data.get("negative"))
    positive_fields = {
        "id",
        "prompt",
        "expected_behavior",
        "expected_result_shape",
        "fixture",
    }
    negative_fields = {"id", "prompt", "expected_behavior", "why_blocked"}
    valid_positive = sum(
        isinstance(item, dict) and all(item.get(field) for field in positive_fields)
        for item in positive
    )
    valid_negative = sum(
        isinstance(item, dict) and all(item.get(field) for field in negative_fields)
        for item in negative
    )
    passed = (
        len(positive) == valid_positive == 5 and len(negative) == valid_negative == 3
    )
    return (
        passed,
        f"{valid_positive}/5 positive and {valid_negative}/3 negative cases valid",
    )


def validate_icon_manifest(
    manifest: dict[str, Any], icon_root: Path | None = None
) -> tuple[bool, str]:
    icons = as_list(manifest.get("icons"))
    resolved_icon_root = (icon_root or model_icon_root()).resolve()
    assets_root = resolved_icon_root.parent
    footnote_root_value = as_dict(manifest.get("ui_contract")).get(
        "response_footnote_asset_root"
    )
    icon_ids: list[str] = []
    invalid_records = 0

    for item in icons:
        if not isinstance(item, dict):
            invalid_records += 1
            continue
        icon_id = item.get("id")
        relative_path = item.get("path")
        expected_hash = item.get("sha256")
        if not all(
            isinstance(value, str) and value
            for value in (icon_id, relative_path, expected_hash)
        ):
            invalid_records += 1
            continue
        icon_ids.append(icon_id)
        asset_path = (assets_root / relative_path).resolve()
        try:
            asset_path.relative_to(assets_root)
        except ValueError:
            invalid_records += 1
            continue
        try:
            asset_hash = hashlib.sha256(asset_path.read_bytes()).hexdigest()
        except OSError:
            asset_hash = None
        if (
            not asset_path.is_file()
            or not re.fullmatch(r"[a-f0-9]{64}", expected_hash)
            or asset_hash != expected_hash
        ):
            invalid_records += 1

    icon_id_set = set(icon_ids)
    aliases = as_dict(manifest.get("aliases"))
    schema = load_json(resolved_icon_root / "model-icon-manifest.schema.json")
    schema_properties = as_dict(schema.get("properties"))
    schema_ui = as_dict(schema_properties.get("ui_contract"))
    schema_ui_properties = as_dict(schema_ui.get("properties"))
    ui_contract = as_dict(manifest.get("ui_contract"))
    schema_valid = (
        as_dict(schema_properties.get("schema_version")).get("const")
        == manifest.get("schema_version")
        and set(ui_contract) <= set(schema_ui_properties)
        and set(as_list(schema_ui.get("required"))) <= set(ui_contract)
    )
    required_ids = {"empire-llm", "openrouter", "anthropic", "qwen", "grok"}
    aliases_valid = all(
        isinstance(alias, str)
        and alias
        and isinstance(target, str)
        and target in icon_id_set
        for alias, target in aliases.items()
    )
    footnote_root = (
        (assets_root / footnote_root_value).resolve()
        if isinstance(footnote_root_value, str)
        else None
    )
    try:
        footnote_root_valid = (
            footnote_root is not None
            and footnote_root.relative_to(assets_root) is not None
        )
    except ValueError:
        footnote_root_valid = False
    footnotes_valid = footnote_root_valid and all(
        (footnote_root / f"{icon_id}.png").is_file() for icon_id in icon_id_set
    )
    passed = all(
        (
            bool(icons),
            invalid_records == 0,
            len(icon_ids) == len(icon_id_set),
            required_ids <= icon_id_set,
            manifest.get("default_icon_id") in icon_id_set,
            aliases_valid,
            footnotes_valid,
            schema_valid,
        )
    )
    detail = (
        f"{len(icon_id_set)} local icon identities; schema, assets, hashes, aliases, and footnotes valid"
        if passed
        else "icon manifest has invalid schema, records, assets, hashes, aliases, or footnotes"
    )
    return passed, detail


def validate_real_diff_record(
    record: dict[str, Any], expected_test_id: str
) -> tuple[bool, str]:
    hash_pattern = re.compile(r"^sha256:[a-f0-9]{64}$")
    cost_bases = {
        "provider_reported",
        "provider_usage_calculation",
        "configured_estimate",
        "unavailable",
    }

    def valid_cost(value: Any, basis: Any) -> bool:
        if basis == "unavailable":
            return value is None
        return (
            basis in cost_bases
            and isinstance(value, (int, float))
            and not isinstance(value, bool)
            and value >= 0
        )

    finding_count = record.get("finding_count")
    grounded = record.get("grounded_findings")
    verified = record.get("verified_findings")
    finding_count_valid = (
        isinstance(finding_count, int)
        and not isinstance(finding_count, bool)
        and finding_count >= 1
    )
    grounded_valid = (
        isinstance(grounded, int)
        and not isinstance(grounded, bool)
        and finding_count_valid
        and grounded == finding_count
    )
    verified_valid = (
        isinstance(verified, int)
        and not isinstance(verified, bool)
        and finding_count_valid
        and isinstance(finding_count, int)
        and 1 <= verified <= finding_count
    )
    identities = (
        record.get("requested_model") is None
        or isinstance(record.get("requested_model"), str)
    ) and all(
        isinstance(record.get(key), str) and bool(record.get(key))
        for key in ("selected_model", "served_model", "served_provider")
    )
    checks = (
        record.get("schema_version") == 1,
        record.get("test_id") == expected_test_id,
        isinstance(record.get("executed_at"), str),
        all(
            isinstance(record.get(key), str)
            and bool(hash_pattern.fullmatch(record[key]))
            for key in (
                "repository_ref_hash",
                "commit_ref_hash",
                "evidence_manifest_hash",
                "reservation_ref_hash",
            )
        ),
        record.get("evidence_boundary_verified") is True,
        record.get("raw_evidence_persisted") is False,
        record.get("raw_provider_response_persisted") is False,
        record.get("untracked_file_count") == 0,
        identities,
        isinstance(record.get("fallback_applied"), bool),
        finding_count_valid,
        grounded_valid,
        verified_valid,
        record.get("fabricated_references") == 0,
        record.get("useful_finding") is True,
        record.get("redaction_scan_passed") is True,
        record.get("secret_redactions") == 0,
        valid_cost(
            record.get("projected_cost_usd"), record.get("projected_cost_basis")
        ),
        valid_cost(record.get("observed_cost_usd"), record.get("cost_basis")),
        record.get("budget_settled") is True,
        record.get("passed") is True,
    )
    passed = all(checks)
    return (
        passed,
        "validated privacy-preserving acceptance record"
        if passed
        else "acceptance record is missing or violates pass conditions",
    )


def real_diff_acceptance_status(
    release: dict[str, Any], repository_root: Path
) -> tuple[bool, str]:
    test_id = release.get("real_diff_test_id")
    artifact = release.get("real_diff_artifact")
    attested = release.get("real_diff_acceptance_passed") is True
    if not attested or not isinstance(test_id, str) or not isinstance(artifact, str):
        return False, "real-diff attestation or artifact reference missing"
    root = repository_root.resolve()
    path = (root / artifact).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        return False, "real-diff artifact escapes the repository"
    passed, detail = validate_real_diff_record(load_json(path), test_id)
    return passed, f"{detail}: {artifact}" if passed else detail


def validate_runtime_accounting_record(record: dict[str, Any]) -> tuple[bool, str]:
    required_cases = {
        "dispatch_before_transport",
        "ambiguous_timeout_retained",
        "process_crash_recovered",
        "conservative_expiry",
        "duplicate_settlement_idempotent",
        "late_response_adjusted",
        "provider_rejection_released",
        "billable_malformed_response_settled",
        "schema_migration_preserves_history",
    }
    cases = as_list(record.get("cases"))
    passed_cases = {
        item.get("id")
        for item in cases
        if isinstance(item, dict)
        and item.get("passed") is True
        and isinstance(item.get("test"), str)
        and item.get("test")
    }
    checks = (
        record.get("schema_version") == 1,
        isinstance(record.get("executed_at"), str),
        record.get("process_level") is True,
        record.get("raw_provider_payloads_persisted") is False,
        record.get("credentials_persisted") is False,
        isinstance(record.get("router_test_count"), int)
        and record.get("router_test_count", 0) >= 98,
        required_cases <= passed_cases,
        record.get("passed") is True,
    )
    passed = all(checks)
    return (
        passed,
        "validated process-level runtime accounting record"
        if passed
        else "runtime accounting evidence is missing or violates pass conditions",
    )


def validate_comparative_utility_record(record: dict[str, Any]) -> tuple[bool, str]:
    routes = as_dict(record.get("routes"))
    baseline = as_dict(routes.get("codex_alone"))
    empire = as_dict(routes.get("codex_plus_empire"))
    checks = as_dict(record.get("checks"))
    task_count = record.get("task_count")
    conditions = (
        record.get("schema_version") == 1,
        record.get("evaluation_id") == "EMPIRE_COMPARATIVE_UTILITY_01",
        isinstance(record.get("executed_at"), str),
        record.get("blind") is True,
        record.get("independent_adjudicator") is True,
        isinstance(task_count, int)
        and not isinstance(task_count, bool)
        and task_count >= 5,
        baseline.get("task_count") == task_count,
        empire.get("task_count") == task_count,
        bool(checks) and all(value is True for value in checks.values()),
        record.get("raw_prompts_persisted") is False,
        record.get("raw_responses_persisted") is False,
        record.get("passed") is True,
    )
    passed = all(conditions)
    return (
        passed,
        "validated blinded comparative utility record"
        if passed
        else "comparative utility evidence is missing or violates pass conditions",
    )


def referenced_record_status(
    hardening: dict[str, Any],
    *,
    attestation_key: str,
    artifact_key: str,
    repository_root: Path,
    validator: Any,
) -> tuple[bool, str]:
    if hardening.get(attestation_key) is not True:
        return False, f"{attestation_key} is not attested"
    artifact = hardening.get(artifact_key)
    if not isinstance(artifact, str) or not artifact:
        return False, f"{artifact_key} is missing"
    root = repository_root.resolve()
    path = (root / artifact).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        return False, f"{artifact_key} escapes the repository"
    passed, detail = validator(load_json(path))
    return passed, f"{detail}: {artifact}" if passed else detail


def git_release_status() -> tuple[bool, str]:
    try:
        head = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            timeout=10,
        )
        remote = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False, "Git release state unavailable"
    passed = (
        head.returncode == 0 and remote.returncode == 0 and bool(remote.stdout.strip())
    )
    return (
        passed,
        "initial commit and origin remote present"
        if passed
        else "initial commit or origin remote missing",
    )


def evaluate(
    evidence: dict[str, Any],
    publishing: dict[str, Any],
    test_cases: dict[str, Any],
    run_tests: bool,
    publishing_root: Path | None = None,
) -> dict[str, Any]:
    manifest = load_json(PLUGIN_ROOT / ".codex-plugin/plugin.json")
    interface = as_dict(manifest.get("interface"))
    author = as_dict(manifest.get("author"))
    required_manifest = (
        manifest.get("name") == "empire-llm-codex",
        isinstance(manifest.get("version"), str),
        bool(manifest.get("description")),
        bool(author.get("name")),
        all(
            interface.get(key)
            for key in (
                "displayName",
                "shortDescription",
                "longDescription",
                "developerName",
                "category",
            )
        ),
    )
    asset_paths = [interface.get("composerIcon"), interface.get("logo")]
    assets_exist = all(
        isinstance(value, str) and (PLUGIN_ROOT / value).is_file()
        for value in asset_paths
    )

    skill_files = sorted((PLUGIN_ROOT / "skills").glob("*/SKILL.md"))
    skill_names = {frontmatter_name(path) for path in skill_files}
    required_skill_names = {
        "empire-benchmarks",
        "empire-cost-policy",
        "empire-handoff",
        "empire-image",
        "empire-readiness",
        "empire-review",
        "empire-settings",
        "empire-video",
        "empire-web-escalation",
    }
    skills_ok = skill_names == required_skill_names

    router_path = PLUGIN_ROOT / "skills/empire-review/scripts/empire_router.py"
    router_text = (
        router_path.read_text(encoding="utf-8") if router_path.is_file() else ""
    )
    shared_runtime_paths = (
        PLUGIN_ROOT / "scripts/empire_review_runtime.py",
        PLUGIN_ROOT / "scripts/empire_budget.py",
        PLUGIN_ROOT / "scripts/empire_response_recovery.py",
        PLUGIN_ROOT / "scripts/empire_secret_policy.py",
        PLUGIN_ROOT / "scripts/context_policy.py",
    )
    runtime_text = (
        router_text
        + "\n"
        + "\n".join(
            path.read_text(encoding="utf-8")
            for path in shared_runtime_paths
            if path.is_file()
        )
    )
    settings_path = PLUGIN_ROOT / "skills/empire-settings/SKILL.md"
    settings_text = (
        settings_path.read_text(encoding="utf-8") if settings_path.is_file() else ""
    )
    settings_ok = (
        all(
            marker in runtime_text
            for marker in (
                "getpass.getpass",
                "KEYCHAIN_SERVICE",
                "credential_store",
                "windows_credential_manager",
                "linux_secret_service",
                "def doctor",
                "def logout_credentials",
                "setup_direct_provider",
                "EMPIRE_SETTINGS_PATH",
            )
        )
        and "Never ask the user to paste an API key" in settings_text
    )
    direct_provider_implemented = all(
        marker in runtime_text
        for marker in (
            "openai_chat_completions",
            "validate_provider_endpoint",
            "provider_account",
            "user_configured_direct_price_calculation",
        )
    )

    if run_tests:
        tests_ok, tests_detail = run_offline_tests()
    else:
        tests_ok, tests_detail = False, "not run; pass --run-tests"

    provenance_ok = all(
        marker in runtime_text
        for marker in (
            "contributors",
            "benchmark_evidence",
            "observed_cost_usd",
            "latency_ms",
            "selected_model",
        )
    )

    icon_root = model_icon_root()
    icons_ok, icons_detail = validate_icon_manifest(
        load_json(icon_root / "model-icon-manifest.json"), icon_root
    )

    marketplace = load_json(REPO_ROOT / ".agents/plugins/marketplace.json")
    catalog_file_ok = marketplace.get("name") == "empire-local" and any(
        isinstance(item, dict) and item.get("name") == "empire-llm-codex"
        for item in marketplace.get("plugins", [])
    )
    catalog_cli_ok = False
    if shutil.which("codex"):
        try:
            plugin_list = subprocess.run(
                ["codex", "plugin", "list"],
                text=True,
                capture_output=True,
                timeout=20,
            )
            catalog_cli_ok = (
                plugin_list.returncode == 0
                and "empire-llm-codex@empire-local" in plugin_list.stdout
            )
        except (OSError, subprocess.TimeoutExpired):
            pass
    catalog_ok = catalog_file_ok or catalog_cli_ok

    live_ok = evidence_passed(
        evidence, "live_openrouter_review", ("observed_at", "model_id", "route_id")
    )
    aa_ok = evidence_passed(
        evidence,
        "artificial_analysis_provenance",
        ("observed_at", "source", "model_count", "matched_model"),
    )
    budget_ok = evidence_passed(
        evidence,
        "budget_settlement",
        ("observed_at", "reservation_id", "cost_source"),
    )
    direct_provider_ok = direct_provider_implemented and tests_ok

    publisher = as_dict(publishing.get("publisher"))
    publisher_ok = (
        publisher.get("apps_management_write") is True
        and publisher.get("verified_identity") is True
        and bool(publisher.get("approved_name"))
        and all(author.get(key) for key in ("name", "email", "url"))
    )

    public_urls = as_dict(publishing.get("public_urls"))
    legal_ok = (
        all(
            is_https(interface.get(key))
            for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL")
        )
        and is_https(public_urls.get("supportURL"))
        and is_https(manifest.get("homepage"))
        and is_https(manifest.get("repository"))
        and bool(manifest.get("license"))
    )

    artwork_ok = (
        all(
            isinstance(interface.get(key), str)
            and interface[key].lower().endswith(".png")
            and (PLUGIN_ROOT / interface[key]).is_file()
            for key in ("composerIcon", "logo")
        )
        and "screenshots" not in interface
    )

    test_packet_ok, test_packet_detail = validate_submission_tests(test_cases)
    availability = as_dict(publishing.get("availability"))
    release = as_dict(publishing.get("release"))
    hardening = as_dict(publishing.get("hardening"))
    app_store_approval_recorded = (
        release.get("openai_app_store_status") == "approved"
        and isinstance(release.get("openai_app_store_approved_at"), str)
        and bool(release.get("openai_app_store_approved_at"))
        and isinstance(release.get("openai_app_store_approval_basis"), str)
        and bool(release.get("openai_app_store_approval_basis"))
    )
    local_hardening_ok = all(
        hardening.get(key) is True
        for key in (
            "architecture_reconciled",
            "evidence_confidentiality_passed",
            "cache_integrity_passed",
            "structured_review_passed",
        )
    )
    runtime_accounting_ok, runtime_accounting_detail = referenced_record_status(
        hardening,
        attestation_key="runtime_failure_accounting_passed",
        artifact_key="runtime_failure_accounting_artifact",
        repository_root=publishing_root or REPO_ROOT,
        validator=validate_runtime_accounting_record,
    )
    comparative_utility_ok, comparative_utility_detail = referenced_record_status(
        hardening,
        attestation_key="comparative_utility_passed",
        artifact_key="comparative_utility_artifact",
        repository_root=publishing_root or REPO_ROOT,
        validator=validate_comparative_utility_record,
    )
    countries = availability.get("countries_or_regions")
    submission_packet_ok = (
        test_packet_ok
        and isinstance(countries, list)
        and bool(countries)
        and release.get("release_notes_approved") is True
    )

    version = manifest.get("version")
    stable_version = isinstance(version, str) and "+codex." not in version
    git_ok, git_detail = git_release_status()
    release_ok = stable_version and git_ok
    real_diff_ok, real_diff_detail = real_diff_acceptance_status(
        release, publishing_root or REPO_ROOT
    )

    gates = [
        Gate(
            "manifest",
            "Plugin manifest and core assets",
            0.75,
            all(required_manifest) and assets_exist,
            "formal manifest and referenced assets present"
            if all(required_manifest) and assets_exist
            else "manifest fields or referenced assets are missing",
            "Fix the required plugin manifest fields and referenced assets.",
            "Manifest validates and every referenced core asset exists.",
            "P0",
        ),
        Gate(
            "skills",
            "Bundled skill contracts",
            0.75,
            skills_ok,
            f"found: {', '.join(sorted(name for name in skill_names if name))}",
            "Restore and validate the exact nine-skill public inventory.",
            "All nine skill folders pass contract validation with no extras.",
            "P0",
        ),
        Gate(
            "settings",
            "Secure user-managed credentials",
            0.75,
            settings_ok,
            "hidden prompts, system keyring, doctor, and logout present"
            if settings_ok
            else "secure settings contract incomplete",
            "Restore secure credential setup and redacted diagnostics.",
            "No credential value enters chat, files, logs, fixtures, or output.",
            "P0",
        ),
        Gate(
            "direct_provider",
            "User-selected direct provider",
            0.25,
            direct_provider_ok,
            "adapter passed offline tests"
            if direct_provider_ok
            else "adapter markers or tests missing",
            "Run --run-tests and fix the direct-provider adapter contract.",
            "Direct-provider adapter passes offline security and cost tests.",
        ),
        Gate(
            "offline_tests",
            "Offline regression suite",
            0.75,
            tests_ok,
            tests_detail,
            "Run the loop with --run-tests and fix every failure.",
            "Bundled offline test suite exits successfully.",
            "P0",
        ),
        Gate(
            "local_hardening",
            "Local architecture and trust-boundary hardening",
            0.0,
            local_hardening_ok,
            "architecture, evidence, cache, and structured-result gates attested"
            if local_hardening_ok
            else "one or more local hardening attestations missing",
            "Complete and attest architecture reconciliation, evidence confidentiality, cache integrity, and structured-result validation.",
            "All four local hardening gates pass deterministic validation.",
            "P0",
        ),
        Gate(
            "runtime_accounting",
            "Runtime failure accounting",
            0.0,
            runtime_accounting_ok,
            runtime_accounting_detail,
            "Implement and verify timeout, cancellation, and late-response reservation settlement across process boundaries.",
            "A process-level integration suite proves reservations always settle or expire safely.",
            "P0",
        ),
        Gate(
            "comparative_utility",
            "Comparative utility evidence",
            0.0,
            comparative_utility_ok,
            comparative_utility_detail,
            "Run blinded comparative reviews against a baseline and record whether routed reviews add measurable value.",
            "A reproducible blinded evaluation shows grounded utility beyond the baseline.",
            "P1",
        ),
        Gate(
            "provenance",
            "Route and cost provenance",
            0.75,
            provenance_ok,
            "model, benchmark, cost, latency, and contributors reported"
            if provenance_ok
            else "provenance fields missing",
            "Restore structured model, benchmark, cost, latency, and contributor provenance.",
            "Every routed result exposes the required provenance without secrets.",
        ),
        Gate(
            "icons",
            "Brand and model icon resolver",
            0.25,
            icons_ok,
            icons_detail,
            "Repair the icon manifest and fallback.",
            "Required brand/model IDs resolve to packaged assets.",
        ),
        Gate(
            "catalog",
            "Private marketplace installation",
            0.25,
            catalog_ok,
            "empire-local catalog entry discovered"
            if catalog_ok
            else "catalog entry missing",
            "Restore and validate the local marketplace entry.",
            "Plugin installs from empire-local and appears in Codex.",
        ),
        Gate(
            "live_review",
            "Genuine OpenRouter route",
            0.75,
            live_ok,
            "redacted live-route evidence supplied"
            if live_ok
            else "passing live-route evidence missing",
            "Run one bounded live route and record only redacted evidence.",
            "A real non-OpenAI model returns a structured bounded review.",
        ),
        Gate(
            "benchmark",
            "Artificial Analysis evidence",
            0.50,
            aa_ok,
            "redacted benchmark provenance supplied"
            if aa_ok
            else "benchmark evidence missing",
            "Run with required benchmarks and record snapshot metadata only.",
            "Selected route names the AA source, model count, and matched model.",
        ),
        Gate(
            "budget",
            "Budget reservation and settlement",
            0.25,
            budget_ok,
            "redacted settlement evidence supplied"
            if budget_ok
            else "settlement evidence missing",
            "Verify reservation settlement and record redacted evidence.",
            "Observed cost settles against the reserved project budget.",
        ),
        Gate(
            "publisher",
            "Verified publisher and portal access",
            0.75,
            publisher_ok,
            "verified identity, Apps Management write, and author contact present"
            if publisher_ok
            else "publisher attestation or author contact incomplete",
            "Verify the publisher, confirm Apps Management write access, and add approved author email/URL.",
            "Publishing organization recognizes the verified identity and submitter permissions.",
            "P0",
        ),
        Gate(
            "legal",
            "Public website, support, privacy, terms, and license",
            0.75,
            legal_ok,
            "all public HTTPS and license fields present"
            if legal_ok
            else "one or more public/legal fields missing",
            "Publish and approve website, support, privacy, terms, repository, and license values.",
            "Every public URL resolves over HTTPS and matches the publisher identity.",
            "P0",
        ),
        Gate(
            "artwork",
            "Marketplace icons for skills-only submission",
            0.50,
            artwork_ok,
            "square PNG composer icon and logo packaged; screenshots correctly omitted"
            if artwork_ok
            else "square PNG icon/logo missing or skills-only screenshot metadata present",
            "Package square PNG composer and directory icons and omit interface.screenshots for skills-only submission.",
            "Production PNG icon/logo are packaged and skills-only screenshot metadata is absent.",
        ),
        Gate(
            "submission_packet",
            "Submission tests, availability, and release notes",
            0.75,
            submission_packet_ok,
            f"{test_packet_detail}; availability/release notes {'ready' if submission_packet_ok else 'pending'}",
            "Approve release notes and countries/regions; keep exactly five positive and three negative test cases.",
            "Portal packet contains 5 positive tests, 3 negative tests, regions, and approved release notes.",
            "P0",
        ),
        Gate(
            "stable_release",
            "Stable version and source-control release",
            0.50,
            release_ok,
            f"version={version!s}; {git_detail}",
            "Create the initial commit and origin remote, then cut a stable version without +codex cache metadata.",
            "Stable manifest version, initial commit, and origin remote are present.",
        ),
        Gate(
            "real_diff",
            "Controlled real-diff acceptance review",
            0.75,
            real_diff_ok,
            real_diff_detail,
            "Run one useful review on a controlled non-sensitive real diff and record its redacted test ID.",
            "Codex verifies at least one useful routed finding on a controlled real diff.",
            "P0",
        ),
    ]

    earned = round(sum(gate.weight for gate in gates if gate.passed), 2)
    failed = [gate for gate in gates if not gate.passed]
    weighted_score = round(max(1.0, earned), 1)
    # Zero-weight hard gates must remain visible in the score. A perfect 10.0
    # is reserved for a release with no failed mandatory gate.
    score = min(weighted_score, 9.9) if failed else weighted_score
    if not local_hardening_ok or not runtime_accounting_ok:
        stage = "private_beta_hardening"
    elif not comparative_utility_ok:
        stage = "comparative_evaluation"
    elif any(gate.gate_id == "publisher" for gate in failed):
        stage = "publisher_review"
    elif not failed and score == 10.0 and app_store_approval_recorded:
        stage = "codex_app_store_approved"
    elif not failed and score == 10.0:
        stage = "codex_app_store_ready"
    elif score >= 8.0:
        stage = "submission_preparation"
    elif score >= 6.0:
        stage = "private_beta"
    else:
        stage = "development"

    todo = [
        {
            "rank": index,
            "gate_id": gate.gate_id,
            "priority": gate.priority,
            "task": gate.next_action,
            "done_when": gate.completion,
            "weight": gate.weight,
        }
        for index, gate in enumerate(failed, start=1)
    ]
    return {
        "schema_version": 2,
        "plugin": "empire-llm-codex",
        "score": score,
        "weighted_score_before_gate_cap": weighted_score,
        "earned_before_floor": earned,
        "minimum": 1.0,
        "maximum": 10.0,
        "stage": stage,
        "codex_app_store_ready": not failed and score == 10.0,
        "app_store_approval_recorded": app_store_approval_recorded,
        "private_beta_ready": score >= 6.0
        and all(required_manifest)
        and skills_ok
        and settings_ok,
        "next_action": failed[0].next_action
        if failed
        else (
            "Track directory availability and keep the approved package evidence current."
            if app_store_approval_recorded
            else "Submit the final package for review."
        ),
        "todo": todo,
        "gates": [gate.as_dict() for gate in gates],
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# Empire Codex App Store readiness: {report['score']:.1f}/10",
        "",
        f"- Stage: `{report['stage']}`",
        f"- Codex App Store ready: `{'yes' if report['codex_app_store_ready'] else 'no'}`",
        f"- App Store approval recorded: `{'yes' if report.get('app_store_approval_recorded') else 'no'}`",
        f"- Private beta ready: `{'yes' if report['private_beta_ready'] else 'no'}`",
        "",
        "## Feedback loop",
        "",
        "Run the readiness command after completing each unchecked item. The evidence-based packaging score is bounded from 1.0 to 10.0.",
        "The numeric score measures weighted packaging evidence; every gate, including zero-weight hardening and utility gates, must pass before release.",
        "",
        "| Gate | Earned | Result | Evidence |",
        "|---|---:|:---:|---|",
    ]
    for gate in report["gates"]:
        result = "pass" if gate["passed"] else "fail"
        lines.append(
            f"| {gate['label']} | {gate['earned']:.2f}/{gate['weight']:.2f} | {result} | {gate['detail']} |"
        )
    lines.extend(["", "## Prioritized to-do list", ""])
    if report["todo"]:
        for item in report["todo"]:
            uplift = f" (+{item['weight']:.2f})" if item["weight"] > 0 else ""
            lines.append(
                f"- [ ] **{item['priority']} · {item['gate_id']}{uplift}** — {item['task']}"
            )
            lines.append(f"  - Done when: {item['done_when']}")
    else:
        completed_action = (
            "Approval is recorded; track directory availability and release evidence."
            if report.get("app_store_approval_recorded")
            else "Every publishing gate passes. Submit the package for review."
        )
        lines.append(f"- [x] {completed_action}")
    lines.extend(
        [
            "",
            "## Next iteration",
            "",
            f"1. {report['next_action']}",
            "2. Update only the relevant redacted readiness input or package artifact.",
            "3. Rerun the command and confirm the score increased for verified evidence only.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    parser.add_argument("--publishing", type=Path, default=DEFAULT_PUBLISHING)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument(
        "--run-tests", action="store_true", help="Run bundled offline tests"
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument(
        "--write-todo", type=Path, help="Write the Markdown feedback loop to this path"
    )
    parser.add_argument(
        "--require-ready",
        action="store_true",
        help="Exit nonzero unless all publishing gates pass",
    )
    args = parser.parse_args()

    report = evaluate(
        load_json(args.evidence),
        load_json(args.publishing),
        load_json(args.test_cases),
        args.run_tests,
        args.publishing.resolve().parent.parent,
    )
    markdown = render_markdown(report)
    if args.write_todo:
        args.write_todo.parent.mkdir(parents=True, exist_ok=True)
        args.write_todo.write_text(markdown + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2) if args.format == "json" else markdown)
    return 0 if not args.require_ready or report["codex_app_store_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
