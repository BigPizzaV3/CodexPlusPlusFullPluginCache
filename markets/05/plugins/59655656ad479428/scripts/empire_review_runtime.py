#!/usr/bin/env python3
"""Lightweight single-partner review router for Codex."""

from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import html
import ipaddress
import json
import math
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.parse import unquote, urlparse
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_SCRIPTS_ROOT = PLUGIN_ROOT / "scripts"
if str(PLUGIN_SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_SCRIPTS_ROOT))

import context_policy  # noqa: E402
import empire_present  # noqa: E402
import empire_response_recovery  # noqa: E402
from empire_budget import (  # noqa: E402
    BudgetError,
    BudgetStore,
    microusd_to_usd,
    pricing_snapshot_id,
    project_identity,
    usd_to_microusd,
)
from empire_response_recovery import (  # noqa: E402
    BLOCKED_FINISH_REASONS,
    COMPLETE_FINISH_REASONS,
    DEFAULT_MAX_PROVIDER_RESPONSE_BYTES,
    MAX_RECOVERY_CONTENT_BYTES,
    MAX_RECOVERY_RECEIPT_BYTES,
    PARTIAL_FINISH_REASONS,
    RECOVERY_CHUNK_CHARS,
    RouterError,
    _atomic_private_json,
    _load_response_receipt,
    assistant_response_content,
    audit_response_recoveries,
    budget_project,
    finalize_provider_response,
    list_response_recoveries,
    mark_response_dispatched,
    normalize_provider_result,
    observed_usage_cost,
    outcome_proven_nonbillable,
    platform_cache_dir,
    platform_data_dir,
    prepare_provider_response,
    provider_reference_data,
    read_response_recovery,
    repair_response_recovery,
    response_billing_state,
    response_recovery_root,
)
from empire_response_recovery import (  # noqa: E402
    capture_provider_response as _capture_provider_response,
)
from empire_secret_policy import (  # noqa: E402
    SECRET_PATTERNS,
    SENSITIVE_NAMES,
    SENSITIVE_SUFFIXES,
    high_entropy_secret_labels,
    secret_findings,
)

__all__ = [
    "BLOCKED_FINISH_REASONS",
    "COMPLETE_FINISH_REASONS",
    "MAX_RECOVERY_CONTENT_BYTES",
    "MAX_RECOVERY_RECEIPT_BYTES",
    "PARTIAL_FINISH_REASONS",
    "_load_response_receipt",
    "assistant_response_content",
    "high_entropy_secret_labels",
    "normalize_provider_result",
    "response_recovery_root",
]


def capture_provider_response(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Capture provider bytes while preserving the public fault-injection seam."""
    original_writer = empire_response_recovery._atomic_private_json
    empire_response_recovery._atomic_private_json = _atomic_private_json
    try:
        return _capture_provider_response(*args, **kwargs)
    finally:
        empire_response_recovery._atomic_private_json = original_writer


OPENROUTER_MODELS = "https://openrouter.ai/api/v1/models"
OPENROUTER_USER_MODELS = "https://openrouter.ai/api/v1/models/user"
OPENROUTER_CHAT = "https://openrouter.ai/api/v1/chat/completions"
OPENAI_MODELS = "https://api.openai.com/v1/models"
OPENAI_RESPONSES = "https://api.openai.com/v1/responses"
OPENAI_CHAT = "https://api.openai.com/v1/chat/completions"
OPENAI_BATCHES = "https://api.openai.com/v1/batches"
ANTHROPIC_MODELS = "https://api.anthropic.com/v1/models"
ANTHROPIC_MESSAGES = "https://api.anthropic.com/v1/messages"
ANTHROPIC_COUNT_TOKENS = "https://api.anthropic.com/v1/messages/count_tokens"
ANTHROPIC_MESSAGE_BATCHES = "https://api.anthropic.com/v1/messages/batches"
GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"
GEMINI_MODELS = GEMINI_BASE + "/models"
GEMINI_INTERACTIONS = GEMINI_BASE + "/interactions"
GEMINI_GENERATE_CONTENT = GEMINI_BASE + "/models/{model}:generateContent"
GEMINI_STREAM_GENERATE_CONTENT = GEMINI_BASE + "/models/{model}:streamGenerateContent"
GEMINI_COUNT_TOKENS = GEMINI_BASE + "/models/{model}:countTokens"
XAI_BASE = "https://api.x.ai/v1"
XAI_MODELS = XAI_BASE + "/models"
XAI_RESPONSES = XAI_BASE + "/responses"
XAI_CHAT = XAI_BASE + "/chat/completions"
DEEPSEEK_BASE = "https://api.deepseek.com"
DEEPSEEK_MODELS = DEEPSEEK_BASE + "/models"
DEEPSEEK_CHAT = DEEPSEEK_BASE + "/chat/completions"
DEEPSEEK_BETA_BASE = DEEPSEEK_BASE + "/beta"
DEEPSEEK_ANTHROPIC_BASE = DEEPSEEK_BASE + "/anthropic"
HIGGSFIELD_BASE = "https://platform.higgsfield.ai"
HIGGSFIELD_STATUS = HIGGSFIELD_BASE + "/requests/{request_id}/status"
HIGGSFIELD_CANCEL = HIGGSFIELD_BASE + "/requests/{request_id}/cancel"
AA_MODELS = "https://artificialanalysis.ai/api/v2/language/models"
AA_MODELS_FREE = "https://artificialanalysis.ai/api/v2/language/models/free"
AA_MAX_PAGES = 25
MAX_FILES = 8
DEFAULT_MAX_BYTES = 80_000
MAX_EXTERNAL_TASK_CHARS = 4_000
MAX_PARTNER_SUMMARY_CHARS = 6_000
MAX_PARTNER_FINDINGS = 50
MAX_PARTNER_FIELD_CHARS = 2_000
SKILL_ROOT = PLUGIN_ROOT / "skills" / "empire-review"
PLUGIN_ASSET_ROOT = PLUGIN_ROOT / "assets"
ICON_ROOT = PLUGIN_ASSET_ROOT / "llm-icons"
ICON_ASSET_ROOT = ICON_ROOT.parent
ICON_MANIFEST = ICON_ROOT / "model-icon-manifest.json"
PROVIDER_REGISTRY_PATH = SKILL_ROOT / "assets" / "provider-registry.json"
LANGUAGE_QUALIFICATION_PACK = (
    SKILL_ROOT / "assets" / "multilingual-qualification-pack.json"
)
KEYCHAIN_SERVICE = "empire-codex-router"
SECURITY_COMMAND = "/usr/bin/security"
WINDOWS_CREDENTIAL_SCRIPT = PLUGIN_SCRIPTS_ROOT / "windows_credential_store.ps1"
MODEL_ENDPOINT_PATH = platform_cache_dir() / "proposed-models.json"
AA_CACHE_PATH = platform_cache_dir() / "artificial-analysis-models.json"
ROUTE_HEALTH_PATH = platform_cache_dir() / "route-health.json"
PROVIDER_CATALOG_DIR = platform_cache_dir() / "provider-catalogs"
MODEL_ENDPOINT_TTL_MINUTES = 20
MODEL_ENDPOINT_MAX_STALE_HOURS = 24
AA_CACHE_TTL_HOURS = 6
ROUTE_HEALTH_TTL_MINUTES = 45
MODEL_ENDPOINT_SCHEMA_VERSION = "1.9.0"
SETTINGS_SCHEMA_VERSION = 2
ROUTING_MODES = ("direct_only", "prefer_direct", "openrouter_only", "custom")
FALLBACK_MODES = ("disabled", "same_model_only", "same_family_only", "any_eligible")
DEFAULT_SETTINGS_PATH = platform_data_dir() / "settings.json"
DEFAULT_LANGUAGE_QUALIFICATION_RESULTS_PATH = (
    platform_data_dir() / "language-qualifications.json"
)
MAX_CACHE_CLOCK_SKEW = timedelta(minutes=5)

COST_MODES = ("auto", "free", "value", "frontier")
COST_LANES = {
    "auto": "adaptive",
    "free": "absolute_zero",
    "value": "value_paid",
    "frontier": "frontier_quality",
}
SELECTION_STRENGTHS = ("hard_lock", "prefer", "try_first")
VALUE_MAX_INPUT_PER_MTOK_USD = 2.0
VALUE_MAX_OUTPUT_PER_MTOK_USD = 8.0
VALUE_MAX_REQUEST_USD = 0.25
PRICING_COMPONENTS = (
    "prompt",
    "completion",
    "request",
    "image",
    "audio",
    "video",
    "web_search",
    "internal_reasoning",
    "input_cache_read",
    "input_cache_write",
)

WEIGHTS = {
    "quality": {
        "coding": 0.40,
        "intelligence": 0.23,
        "context": 0.08,
        "price": 0.04,
        "speed": 0.05,
        "capability": 0.10,
        "availability": 0.10,
    },
    "balanced": {
        "coding": 0.30,
        "intelligence": 0.18,
        "context": 0.05,
        "price": 0.17,
        "speed": 0.10,
        "capability": 0.10,
        "availability": 0.10,
    },
    "fast": {
        "coding": 0.22,
        "intelligence": 0.08,
        "context": 0,
        "price": 0.18,
        "speed": 0.30,
        "capability": 0.10,
        "availability": 0.12,
    },
    "cheap": {
        "coding": 0.18,
        "intelligence": 0.08,
        "context": 0,
        "price": 0.40,
        "speed": 0.12,
        "capability": 0.10,
        "availability": 0.12,
    },
}


class AmbiguousProviderOutcome(RouterError):
    """Transport ended after dispatch without proving whether billing occurred."""

    def __init__(
        self,
        message: str,
        *,
        provider_generation_id: str | None = None,
        provider_request_id: str | None = None,
    ) -> None:
        self.provider_generation_id = provider_generation_id
        self.provider_request_id = provider_request_id
        super().__init__(message)


class ProviderRequestError(RouterError):
    def __init__(
        self,
        status_code: int,
        url: str,
        message: str,
        metadata: dict[str, Any] | None = None,
        *,
        provider_generation_id: str | None = None,
        provider_request_id: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.url = url
        self.provider_message = message
        self.metadata = metadata or {}
        self.provider_generation_id = provider_generation_id
        self.provider_request_id = provider_request_id
        category = provider_failure_category(status_code, message)
        super().__init__(f"HTTP {status_code} from {url} [{category}]: {message[:400]}")


class RejectRedirects(HTTPRedirectHandler):
    """Prevent bearer credentials from following provider-controlled redirects."""

    def redirect_request(self, *_: Any, **__: Any) -> None:
        raise RouterError("Provider redirect refused")


def provider_failure_category(status_code: int, message: str = "") -> str:
    lowered = message.lower()
    if status_code == 404 and (
        "no endpoint" in lowered or "no allowed provider" in lowered
    ):
        return "no_compatible_endpoint"
    if status_code == 402:
        return "insufficient_credit"
    if status_code == 429:
        return "rate_limited"
    if status_code in {502, 503, 504, 529}:
        return "provider_unavailable"
    if status_code in {400, 404, 422}:
        return "request_incompatible"
    return "provider_rejected"


def tls_context() -> ssl.SSLContext:
    paths = ssl.get_default_verify_paths()
    if paths.cafile and Path(paths.cafile).is_file():
        return ssl.create_default_context()
    for candidate in (
        os.environ.get("SSL_CERT_FILE"),
        "/etc/ssl/cert.pem",
        "/private/etc/ssl/cert.pem",
    ):
        if candidate and Path(candidate).is_file():
            return ssl.create_default_context(cafile=candidate)
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except (ImportError, OSError):
        return ssl.create_default_context()


def credential_backend() -> tuple[str, str]:
    if sys.platform == "darwin" and Path(SECURITY_COMMAND).is_file():
        return "macos_keychain", SECURITY_COMMAND
    if sys.platform == "win32":
        command = shutil.which("pwsh") or shutil.which("powershell")
        if command and WINDOWS_CREDENTIAL_SCRIPT.is_file():
            return "windows_credential_manager", command
    if sys.platform.startswith("linux"):
        command = shutil.which("secret-tool")
        if command:
            return "linux_secret_service", command
    raise RouterError(
        "No secure system credential store is available. Install Secret Service "
        "and secret-tool on Linux, or use provider environment variables for CI."
    )


def _credential_failure_state(backend: str, returncode: int, stderr: str) -> str:
    """Distinguish a missing item from an inaccessible credential store."""
    lowered = stderr.lower()
    inaccessible_markers = (
        "interaction is not allowed",
        "user interaction is not allowed",
        "authorization denied",
        "access denied",
        "not permitted",
        "operation not permitted",
        "keychain is locked",
        "one or more parameters passed",
        "failed to connect",
        "service is not available",
        "secret service",
    )
    if any(marker in lowered for marker in inaccessible_markers):
        return "inaccessible"
    if backend == "macos_keychain" and "could not be found" in lowered:
        return "missing"
    if backend == "windows_credential_manager" and returncode == 1 and not stderr:
        return "missing"
    if backend == "linux_secret_service" and returncode == 1 and not stderr:
        return "missing"
    return "inaccessible"


def credential_probe(account: str) -> dict[str, Any]:
    """Return credential state without collapsing access failures into absence."""
    try:
        backend, command = credential_backend()
    except RouterError:
        return {
            "value": None,
            "state": "inaccessible",
            "source": "system_keyring_unavailable",
            "backend": None,
        }
    if backend == "macos_keychain":
        arguments = [
            command,
            "find-generic-password",
            "-s",
            KEYCHAIN_SERVICE,
            "-a",
            account,
            "-w",
        ]
    elif backend == "linux_secret_service":
        arguments = [
            command,
            "lookup",
            "service",
            KEYCHAIN_SERVICE,
            "account",
            account,
        ]
    else:
        arguments = [
            command,
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(WINDOWS_CREDENTIAL_SCRIPT),
            "get",
            KEYCHAIN_SERVICE,
            account,
        ]
    try:
        proc = subprocess.run(
            arguments,
            text=True,
            capture_output=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {
            "value": None,
            "state": "inaccessible",
            "source": "system_keyring_inaccessible",
            "backend": backend,
        }
    if proc.returncode != 0:
        state = _credential_failure_state(backend, proc.returncode, proc.stderr.strip())
        return {
            "value": None,
            "state": state,
            "source": "missing" if state == "missing" else "system_keyring_inaccessible",
            "backend": backend,
        }
    value = proc.stdout.rstrip("\r\n")
    return {
        "value": value or None,
        "state": "present" if value else "missing",
        "source": "system_keyring" if value else "missing",
        "backend": backend,
    }


def credential_get(account: str) -> str | None:
    return credential_probe(account)["value"]


def credential_store(account: str, secret: str) -> str:
    backend, command = credential_backend()
    if not secret:
        raise RouterError(f"Credential cannot be empty: {account}")
    if backend == "macos_keychain":
        password_hex = secret.encode("utf-8").hex()
        arguments = [command, "-i"]
        credential_input = (
            f'add-generic-password -U -s "{KEYCHAIN_SERVICE}" '
            f'-a "{account}" -X {password_hex}\n'
        )
    elif backend == "linux_secret_service":
        arguments = [
            command,
            "store",
            "--label=Empire LLM Codex",
            "service",
            KEYCHAIN_SERVICE,
            "account",
            account,
        ]
        credential_input = secret
    else:
        arguments = [
            command,
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(WINDOWS_CREDENTIAL_SCRIPT),
            "store",
            KEYCHAIN_SERVICE,
            account,
        ]
        credential_input = secret
    proc = subprocess.run(
        arguments,
        input=credential_input,
        text=True,
        capture_output=True,
        timeout=20,
    )
    if proc.returncode != 0:
        raise RouterError(f"Could not store {account} credential in the system keyring")
    return backend


def store_and_verify_credential(account: str, secret: str) -> dict[str, Any]:
    """Persist a secret, then verify it without ever returning the secret."""
    backend = credential_store(account, secret)
    probe = credential_probe(account)
    if probe["state"] == "missing":
        raise RouterError(
            "The system keyring reported a successful save, but readback could not "
            f"find the {account} credential. It was not accepted as configured."
        )
    result = credential_status(probe["value"], probe["source"])
    result["backend"] = backend
    result["verified"] = probe["state"] == "present"
    return result


def credential_delete(account: str) -> bool:
    backend, command = credential_backend()
    if backend == "macos_keychain":
        arguments = [
            command,
            "delete-generic-password",
            "-s",
            KEYCHAIN_SERVICE,
            "-a",
            account,
        ]
    elif backend == "linux_secret_service":
        arguments = [
            command,
            "clear",
            "service",
            KEYCHAIN_SERVICE,
            "account",
            account,
        ]
    else:
        arguments = [
            command,
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(WINDOWS_CREDENTIAL_SCRIPT),
            "delete",
            KEYCHAIN_SERVICE,
            account,
        ]
    proc = subprocess.run(
        arguments,
        text=True,
        capture_output=True,
        timeout=20,
    )
    return proc.returncode == 0


def resolve_credential(
    env_names: tuple[str, ...], account: str
) -> tuple[str | None, str]:
    for name in env_names:
        value = os.environ.get(name)
        if value:
            return value, "environment"
    probe = credential_probe(account)
    return probe["value"], probe["source"]


def credential_status(value: str | None, source: str) -> dict[str, Any]:
    if value:
        return {"present": True, "source": source, "action": "none"}
    if source == "system_keyring_inaccessible":
        return {
            "present": None,
            "source": source,
            "action": "retry_with_keyring_access",
        }
    if source == "system_keyring_unavailable":
        return {
            "present": None,
            "source": source,
            "action": "install_secure_keyring",
        }
    return {"present": False, "source": "missing", "action": "setup"}


def credential_required_message(label: str, source: str, setup_hint: str) -> str:
    if source == "system_keyring_inaccessible":
        return (
            f"{label} credential could not be checked because the system keyring is "
            "inaccessible in this sandbox. Retry the redacted credential check with "
            "Keychain/keyring access; do not enter the credential again."
        )
    if source == "system_keyring_unavailable":
        return (
            f"{label} credential could not be checked because no supported secure "
            "system keyring is available. Install the platform keyring dependency or "
            "use an environment variable only in CI/headless operation."
        )
    return f"{label} credential is missing; {setup_hint}"


def settings_path() -> Path:
    configured = os.environ.get("EMPIRE_SETTINGS_PATH")
    return (
        Path(configured).expanduser().resolve() if configured else DEFAULT_SETTINGS_PATH
    )


def load_settings() -> dict[str, Any]:
    path = settings_path()
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default_settings()
    except (OSError, json.JSONDecodeError) as exc:
        raise RouterError(f"Empire settings are unreadable: {exc}") from exc
    if not isinstance(value, dict):
        raise RouterError("Empire settings use an unsupported schema")
    return migrate_settings(value)


def default_settings() -> dict[str, Any]:
    """Preserve the existing OpenRouter default while making eligibility explicit."""
    return {
        "schema_version": SETTINGS_SCHEMA_VERSION,
        "inference_provider": "openrouter",
        "providers": {
            "instances": {
                "openrouter": {
                    "provider_id": "openrouter",
                    "kind": "aggregator",
                    "enabled": True,
                    "credential_ref": "openrouter",
                }
            }
        },
        "routing_policy": {
            "mode": "openrouter_only",
            "enabled_providers": ["openrouter"],
            "priority": ["openrouter"],
            "allowed_families": ["*"],
            "fallback": {"openrouter": "disabled"},
        },
    }


def direct_instance_id(name: str) -> str:
    return provider_slug(name) + "-direct"


def _direct_instance(name: str, config: dict[str, Any]) -> dict[str, Any]:
    slug = provider_slug(name)
    return {
        "provider_id": slug,
        "kind": "direct",
        "enabled": True,
        "credential_ref": provider_account(slug),
        "endpoint": config.get("endpoint"),
        "model_id": config.get("model_id"),
        "catalog_model_id": config.get("catalog_model_id") or config.get("model_id"),
        "input_cost_per_mtok": config.get("input_cost_per_mtok"),
        "output_cost_per_mtok": config.get("output_cost_per_mtok"),
        "context_tokens": config.get("context_tokens"),
        "protocol": config.get("protocol", "openai_chat_completions"),
    }


def validate_routing_policy(value: Any, instances: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RouterError("Empire routing policy must be an object")
    mode = value.get("mode")
    if mode not in ROUTING_MODES:
        raise RouterError("Empire routing policy uses an unsupported mode")
    enabled = value.get("enabled_providers")
    priority = value.get("priority")
    families = value.get("allowed_families")
    fallback = value.get("fallback")
    if not isinstance(enabled, list) or not all(isinstance(item, str) for item in enabled):
        raise RouterError("Enabled providers must be a list of provider instance IDs")
    if not isinstance(priority, list) or not all(isinstance(item, str) for item in priority):
        raise RouterError("Provider priority must be a list of provider instance IDs")
    if len(enabled) != len(set(enabled)) or len(priority) != len(set(priority)):
        raise RouterError("Provider eligibility and priority cannot contain duplicates")
    unknown = (set(enabled) | set(priority)) - set(instances)
    if unknown:
        raise RouterError("Routing policy references unknown provider instances")
    if any(item not in enabled for item in priority):
        raise RouterError("Every prioritized provider must also be enabled")
    if not isinstance(families, list) or not families or not all(
        isinstance(item, str) and item.strip() for item in families
    ):
        raise RouterError("Allowed families must be a non-empty string list")
    if not isinstance(fallback, dict) or fallback.get("openrouter") not in FALLBACK_MODES:
        raise RouterError("OpenRouter fallback uses an unsupported mode")
    if mode == "direct_only" and "openrouter" in enabled:
        raise RouterError("direct_only policy cannot enable OpenRouter")
    if mode == "openrouter_only" and enabled != ["openrouter"]:
        raise RouterError("openrouter_only policy must enable only OpenRouter")
    if fallback.get("openrouter") != "disabled" and "openrouter" not in enabled:
        raise RouterError("OpenRouter fallback requires OpenRouter to be explicitly enabled")
    return value


def migrate_settings(value: dict[str, Any]) -> dict[str, Any]:
    """Normalize settings to schema v2 without writing during a read."""
    version = value.get("schema_version")
    if version == SETTINGS_SCHEMA_VERSION:
        providers = value.get("providers")
        current_instances = (
            providers.get("instances") if isinstance(providers, dict) else None
        )
        if not isinstance(current_instances, dict) or not all(
            isinstance(key, str) and isinstance(item, dict)
            for key, item in current_instances.items()
        ):
            raise RouterError("Empire provider instances are invalid")
        validate_routing_policy(value.get("routing_policy"), current_instances)
        return value
    if version != 1:
        raise RouterError("Empire settings use an unsupported schema")

    migrated = dict(value)
    migrated["schema_version"] = SETTINGS_SCHEMA_VERSION
    instances: dict[str, dict[str, Any]] = {
        "openrouter": {
            "provider_id": "openrouter",
            "kind": "aggregator",
            "enabled": value.get("inference_provider", "openrouter") == "openrouter",
            "credential_ref": "openrouter",
        }
    }
    direct = value.get("direct_provider")
    direct_id: str | None = None
    if isinstance(direct, dict):
        name = provider_slug(str(direct.get("name", "")))
        direct_id = direct_instance_id(name)
        instances[direct_id] = _direct_instance(name, direct)
    selected = value.get("inference_provider", "openrouter")
    if selected == "direct" and direct_id:
        instances["openrouter"]["enabled"] = False
        policy: dict[str, Any] = {
            "mode": "direct_only",
            "enabled_providers": [direct_id],
            "priority": [direct_id],
            "allowed_families": [instances[direct_id]["provider_id"]],
            "fallback": {"openrouter": "disabled"},
        }
    else:
        policy = default_settings()["routing_policy"]
    migrated["providers"] = {"instances": instances}
    migrated["routing_policy"] = policy
    migrated.pop("direct_provider", None)
    validate_routing_policy(policy, instances)
    return migrated


def configured_direct_provider(
    settings: dict[str, Any],
) -> tuple[str | None, dict[str, Any] | None]:
    """Read both schema v1 test fixtures and normalized schema v2 settings."""
    legacy = settings.get("direct_provider")
    if isinstance(legacy, dict):
        name = provider_slug(str(legacy.get("name", "")))
        return direct_instance_id(name), legacy
    providers = settings.get("providers")
    instances = providers.get("instances") if isinstance(providers, dict) else None
    if not isinstance(instances, dict):
        return None, None
    priority = settings.get("routing_policy", {}).get("priority", [])
    ordered = [*priority, *(key for key in instances if key not in priority)]
    for instance_id in ordered:
        item = instances.get(instance_id)
        if isinstance(item, dict) and item.get("kind") == "direct":
            config = dict(item)
            config["name"] = item.get("provider_id")
            return instance_id, config
    return None, None


def _private_directory(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(path.parent, 0o700)
    except OSError:
        pass


def _atomic_private_text(path: Path, content: str) -> None:
    """Atomically replace private state without a predictable symlinkable temp path."""
    _private_directory(path)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def save_settings(value: dict[str, Any]) -> None:
    path = settings_path()
    _atomic_private_text(path, json.dumps(value, indent=2) + "\n")


def provider_slug(value: str) -> str:
    slug = value.strip().lower()
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", slug):
        raise RouterError(
            "Provider name must be 1-64 lowercase letters, numbers, or hyphens"
        )
    return slug


def catalog_provider_slug(value: str) -> str:
    """Normalize external catalog labels without weakening user-input checks."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    slug = slug[:64].rstrip("-")
    return slug or "unknown"


def provider_account(name: str) -> str:
    return "provider:" + provider_slug(name)


def _nonpublic_hostname(hostname: str) -> bool:
    lowered = hostname.rstrip(".").lower()
    if (
        lowered in {"localhost", "localhost.localdomain"}
        or lowered.endswith(".localhost")
        or lowered.endswith(".local")
    ):
        return True
    try:
        address = ipaddress.ip_address(lowered)
    except ValueError:
        return False
    return not address.is_global


def _unsafe_url_shape(value: str, parsed: Any) -> bool:
    decoded_segments = unquote(parsed.path).split("/")
    return (
        len(value) > 2_048
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
        or not parsed.hostname.isascii()
        or any(segment in {".", ".."} for segment in decoded_segments)
    )


def validate_provider_endpoint(value: str) -> str:
    cleaned = value.strip()
    parsed = urlparse(cleaned)
    if (
        parsed.scheme != "https"
        or not parsed.netloc
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or _nonpublic_hostname(parsed.hostname)
        or _unsafe_url_shape(cleaned, parsed)
    ):
        raise RouterError(
            "Direct-provider endpoint must be remote HTTPS with no credentials, query, or fragment"
        )
    return cleaned


def load_provider_registry(path: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load only reviewed provider endpoints and reject unsafe registry entries."""
    source = path or PROVIDER_REGISTRY_PATH
    try:
        value = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RouterError(f"Provider registry is unreadable: {exc}") from exc
    if not isinstance(value, dict) or value.get("schema_version") != "1.0.0":
        raise RouterError("Provider registry uses an unsupported schema")
    entries = value.get("providers")
    if not isinstance(entries, list):
        raise RouterError("Provider registry entries are invalid")
    registry: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise RouterError("Provider registry contains a non-object entry")
        provider_id = provider_slug(str(entry.get("provider_id", "")))
        family = provider_slug(str(entry.get("family", "")))
        if provider_id in registry:
            raise RouterError("Provider registry contains duplicate provider IDs")
        hosts = entry.get("allowed_hosts")
        base_url = validate_provider_endpoint(str(entry.get("base_url", "")))
        parsed = urlparse(base_url)
        if (
            not isinstance(hosts, list)
            or not hosts
            or not all(isinstance(host, str) for host in hosts)
            or parsed.hostname not in hosts
        ):
            raise RouterError("Provider base URL is outside its allowed host list")
        discovery = entry.get("discovery")
        endpoints = entry.get("inference_endpoints")
        if not isinstance(discovery, dict) or discovery.get("mode") not in {
            "api",
            "curated",
            "manual",
        }:
            raise RouterError("Provider discovery contract is invalid")
        discovery_path = discovery.get("path")
        if discovery.get("mode") == "api" and (
            not isinstance(discovery_path, str) or not discovery_path.startswith("/")
        ):
            raise RouterError("API discovery requires a relative path")
        if not isinstance(endpoints, list) or not endpoints:
            raise RouterError("Provider inference endpoints are missing")
        for endpoint in endpoints:
            path_value = endpoint.get("path") if isinstance(endpoint, dict) else None
            if not isinstance(path_value, str) or not path_value.startswith("/"):
                raise RouterError("Provider inference endpoint path is invalid")
        pattern = entry.get("model_id_pattern")
        if not isinstance(pattern, str):
            raise RouterError("Provider model namespace pattern is missing")
        try:
            re.compile(pattern)
        except re.error as exc:
            raise RouterError("Provider model namespace pattern is invalid") from exc
        normalized = dict(entry)
        normalized["provider_id"] = provider_id
        normalized["family"] = family
        normalized["base_url"] = base_url.rstrip("/")
        registry[provider_id] = normalized
    return registry


def registered_provider(value: str) -> dict[str, Any]:
    requested = provider_slug(value)
    registry = load_provider_registry()
    if requested in registry:
        return registry[requested]
    matches = [entry for entry in registry.values() if entry["family"] == requested]
    if len(matches) == 1:
        return matches[0]
    raise RouterError(f"Unknown or ambiguous registered provider: {requested}")


def add_registered_provider(value: str) -> dict[str, Any]:
    credential_backend()
    provider = registered_provider(value)
    instance_id = provider["provider_id"]
    family = provider["family"]
    api_key = getpass.getpass(f"{family} API key: ").strip()
    if not api_key:
        raise RouterError("Direct-provider API key is required")
    account = provider_account(family)
    stored = store_and_verify_credential(account, api_key)
    settings = load_settings()
    instances = settings["providers"]["instances"]
    instances[instance_id] = {
        "provider_id": family,
        "registry_id": instance_id,
        "kind": "direct",
        "enabled": True,
        "credential_ref": account,
    }
    if "openrouter" in instances:
        instances["openrouter"]["enabled"] = False
    settings["inference_provider"] = "direct"
    settings["routing_policy"] = {
        "mode": "direct_only",
        "enabled_providers": [instance_id],
        "priority": [instance_id],
        "allowed_families": [family],
        "fallback": {"openrouter": "disabled"},
    }
    save_settings(settings)
    return {
        "status": "configured" if stored["verified"] else "configured_unverified",
        "provider_instance_id": instance_id,
        "provider_family": family,
        "routing_mode": "direct_only",
        "openrouter_fallback": "disabled",
        "credential_present": stored["present"],
        "credential_source": stored["source"],
        "next_command": f"provider discover {instance_id}",
    }


def provider_catalog_path(instance_id: str) -> Path:
    return PROVIDER_CATALOG_DIR / f"{provider_slug(instance_id)}.json"


def _write_private_json(path: Path, value: dict[str, Any]) -> None:
    _atomic_private_text(path, json.dumps(value, indent=2) + "\n")


def _provider_instance(settings: dict[str, Any], value: str) -> tuple[str, dict[str, Any]]:
    requested = provider_slug(value)
    instances = settings["providers"]["instances"]
    if requested in instances and instances[requested].get("kind") == "direct":
        return requested, instances[requested]
    matches = [
        (instance_id, instance)
        for instance_id, instance in instances.items()
        if instance.get("kind") == "direct"
        and instance.get("provider_id") == requested
    ]
    if len(matches) == 1:
        return matches[0]
    raise RouterError(f"Direct provider is not configured: {requested}")


def discover_registered_provider(value: str) -> dict[str, Any]:
    """Refresh one provider catalog without invoking a model or storing secrets."""
    settings = load_settings()
    instance_id, instance = _provider_instance(settings, value)
    registry_id = provider_slug(str(instance.get("registry_id") or instance_id))
    provider = registered_provider(registry_id)
    discovery = provider["discovery"]
    if discovery.get("mode") != "api":
        raise RouterError("This provider does not support authenticated API discovery")
    env_names = provider.get("credential_env")
    env_tuple = tuple(env_names) if isinstance(env_names, list) else ()
    credential_ref = str(instance.get("credential_ref", ""))
    api_key, source = resolve_credential(env_tuple, credential_ref)
    if not api_key:
        raise RouterError(
            credential_required_message(
                "Direct-provider", source, "add the provider again"
            )
        )
    discovery_url = provider["base_url"] + discovery["path"]
    parsed = urlparse(discovery_url)
    if parsed.hostname not in provider["allowed_hosts"]:
        raise RouterError("Discovery URL is outside the provider allowlist")
    response = request_json(discovery_url, api_key=api_key)
    raw_models = response.get("data", response.get("models"))
    if not isinstance(raw_models, list):
        raise RouterError("Provider discovery returned an invalid model list")
    pattern = re.compile(provider["model_id_pattern"])
    endpoint = next(
        (
            item
            for item in provider["inference_endpoints"]
            if item.get("preferred") is True
        ),
        provider["inference_endpoints"][0],
    )
    models: list[dict[str, Any]] = []
    seen: set[str] = set()
    excluded = 0
    for raw in raw_models:
        model_id = str(raw.get("id", "")).strip() if isinstance(raw, dict) else ""
        if not model_id or len(model_id) > 200 or not pattern.fullmatch(model_id):
            excluded += 1
            continue
        route_id = f"{instance_id}:{model_id}"
        if route_id in seen:
            excluded += 1
            continue
        seen.add(route_id)
        models.append(
            {
                "route_id": route_id,
                "model_id": model_id,
                "family": provider["family"],
                "endpoint_ref": f"{registry_id}.{endpoint['id']}",
                "availability": "available",
                "capabilities": {},
                "pricing": {},
                "pricing_status": "unknown",
            }
        )
    if not models:
        raise RouterError("Provider discovery returned no valid provider-scoped models")
    models.sort(key=lambda item: item["model_id"])
    path = provider_catalog_path(instance_id)
    previous_ids: set[str] = set()
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
        previous_ids = {
            str(item.get("route_id"))
            for item in previous.get("models", [])
            if isinstance(item, dict)
        }
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        pass
    now = datetime.now(timezone.utc).replace(microsecond=0)
    ttl = int(discovery.get("ttl_minutes", MODEL_ENDPOINT_TTL_MINUTES))
    catalog = {
        "schema_version": "1.0.0",
        "provider_instance_id": instance_id,
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "expires_at": (now + timedelta(minutes=ttl))
        .isoformat()
        .replace("+00:00", "Z"),
        "catalog_source": "authenticated_provider_api",
        "models": models,
    }
    _write_private_json(path, catalog)
    current_ids = {item["route_id"] for item in models}
    return {
        "status": "refreshed",
        "provider_instance_id": instance_id,
        "credential_source": source,
        "catalog_path": str(path),
        "model_count": len(models),
        "excluded_count": excluded,
        "added": sorted(current_ids - previous_ids),
        "removed": sorted(previous_ids - current_ids),
        "expires_at": catalog["expires_at"],
    }


def list_provider_instances() -> dict[str, Any]:
    settings = load_settings()
    instances = settings["providers"]["instances"]
    redacted = []
    for instance_id, instance in sorted(instances.items()):
        credential_ref = str(instance.get("credential_ref", ""))
        _, source = resolve_credential((), credential_ref)
        redacted.append(
            {
                "instance_id": instance_id,
                "provider_id": instance.get("provider_id"),
                "kind": instance.get("kind"),
                "enabled": instance_id
                in settings["routing_policy"]["enabled_providers"],
                "priority": settings["routing_policy"]["priority"].index(instance_id)
                if instance_id in settings["routing_policy"]["priority"]
                else None,
                "credential_present": (
                    credential_status(None, source)["present"]
                    if source != "system_keyring"
                    else True
                ),
                "credential_source": source,
            }
        )
    return {"routing_policy": settings["routing_policy"], "providers": redacted}


def direct_provider_status(settings: dict[str, Any] | None = None) -> dict[str, Any]:
    settings = settings or load_settings()
    instance_id, config = configured_direct_provider(settings)
    if not isinstance(config, dict) or instance_id is None:
        return {"configured": False, "credential_present": False, "source": "missing"}
    name = provider_slug(str(config.get("name", "")))
    key, source = resolve_credential(
        ("EMPIRE_PROVIDER_API_KEY",), provider_account(name)
    )
    return {
        "configured": True,
        "selected": instance_id
        in settings.get("routing_policy", {}).get("priority", [])[:1]
        or settings.get("inference_provider") == "direct",
        "instance_id": instance_id,
        "name": name,
        "endpoint": config.get("endpoint"),
        "model_id": config.get("model_id"),
        "catalog_model_id": config.get("catalog_model_id"),
        "credential_present": credential_status(key, source)["present"],
        "source": source,
    }


def setup_direct_provider(
    name: str,
    endpoint: str,
    model_id: str,
    catalog_model_id: str | None,
    input_cost_per_mtok: str,
    output_cost_per_mtok: str,
    context_tokens: int,
) -> dict[str, Any]:
    credential_backend()
    slug = provider_slug(name)
    endpoint = validate_provider_endpoint(endpoint)
    if not model_id.strip() or len(model_id) > 200:
        raise RouterError(
            "Direct-provider model ID is required and must be at most 200 characters"
        )
    if catalog_model_id is not None and len(catalog_model_id) > 200:
        raise RouterError("Catalog model ID must be at most 200 characters")
    if context_tokens <= 0:
        raise RouterError("Context tokens must be greater than zero")
    input_microusd_per_mtok = usd_to_microusd(input_cost_per_mtok)
    output_microusd_per_mtok = usd_to_microusd(output_cost_per_mtok)
    api_key = getpass.getpass(f"{slug} API key: ").strip()
    if not api_key:
        raise RouterError("Direct-provider API key is required")
    stored = store_and_verify_credential(provider_account(slug), api_key)
    settings = load_settings()
    instance_id = direct_instance_id(slug)
    config = {
        "endpoint": endpoint,
        "model_id": model_id.strip(),
        "catalog_model_id": (catalog_model_id or model_id).strip(),
        "input_cost_per_mtok": microusd_to_usd(input_microusd_per_mtok),
        "output_cost_per_mtok": microusd_to_usd(output_microusd_per_mtok),
        "context_tokens": context_tokens,
        "protocol": "openai_chat_completions",
    }
    instances = settings.setdefault("providers", {}).setdefault("instances", {})
    instances[instance_id] = _direct_instance(slug, config)
    if "openrouter" in instances:
        instances["openrouter"]["enabled"] = False
    settings["inference_provider"] = "direct"
    settings["routing_policy"] = {
        "mode": "direct_only",
        "enabled_providers": [instance_id],
        "priority": [instance_id],
        "allowed_families": [slug],
        "fallback": {"openrouter": "disabled"},
    }
    save_settings(settings)
    return {
        "status": "configured" if stored["verified"] else "configured_unverified",
        "inference_provider": "direct",
        "direct_provider": direct_provider_status(settings),
    }


def select_inference_provider(value: str) -> dict[str, Any]:
    if value not in {"openrouter", "direct"}:
        raise RouterError("Inference provider must be openrouter or direct")
    settings = load_settings()
    direct_id, direct = configured_direct_provider(settings)
    if value == "direct" and (direct_id is None or direct is None):
        raise RouterError("No direct provider is configured; run `provider setup`")
    instances = settings["providers"]["instances"]
    if value == "direct":
        if direct_id is None or direct is None:
            raise RouterError("Direct-provider configuration disappeared during selection")
        for instance in instances.values():
            instance["enabled"] = False
        instances[direct_id]["enabled"] = True
        settings["routing_policy"] = {
            "mode": "direct_only",
            "enabled_providers": [direct_id],
            "priority": [direct_id],
            "allowed_families": [provider_slug(str(direct.get("name", "")))],
            "fallback": {"openrouter": "disabled"},
        }
    else:
        instances.setdefault(
            "openrouter",
            {
                "provider_id": "openrouter",
                "kind": "aggregator",
                "credential_ref": "openrouter",
            },
        )["enabled"] = True
        settings["routing_policy"] = default_settings()["routing_policy"]
    settings["inference_provider"] = value
    save_settings(settings)
    return {"status": "selected", "inference_provider": value}


def default_selection_strength(cost_mode: str) -> str:
    return "prefer" if cost_mode == "auto" else "hard_lock"


def validate_language(value: str | None) -> str | None:
    if value is None or not value.strip():
        return None
    language = value.strip()
    if not re.fullmatch(r"[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8}){0,3}", language):
        raise RouterError("Language must be a BCP 47-style tag such as es-PR or ja-JP")
    parts = language.split("-")
    normalized = [parts[0].lower()]
    for part in parts[1:]:
        normalized.append(part.upper() if len(part) == 2 and part.isalpha() else part)
    return "-".join(normalized)


def cost_mode_status() -> dict[str, Any]:
    settings = load_settings()
    value = settings.get("cost_mode", "auto")
    if value not in COST_MODES:
        value = "auto"
    strength = settings.get("selection_strength", default_selection_strength(value))
    if strength not in SELECTION_STRENGTHS:
        strength = default_selection_strength(value)
    return {
        "status": "configured",
        "cost_mode": value,
        "internal_policy": COST_LANES[value],
        "selection_strength": strength,
        "maximum_total_cost_usd": 0
        if value == "free" and strength == "hard_lock"
        else None,
        "cross_tier_fallback": strength != "hard_lock",
        "target_language": validate_language(settings.get("target_language")),
        "scope": "user_default",
        "available_modes": list(COST_MODES),
        "available_selection_strengths": list(SELECTION_STRENGTHS),
        "openai_excluded": True,
    }


def set_cost_mode(value: str, selection_strength: str | None = None) -> dict[str, Any]:
    if value not in COST_MODES:
        raise RouterError(f"Cost mode must be one of: {', '.join(COST_MODES)}")
    strength = selection_strength or default_selection_strength(value)
    if strength not in SELECTION_STRENGTHS:
        raise RouterError(
            "Selection strength must be one of: " + ", ".join(SELECTION_STRENGTHS)
        )
    settings = load_settings()
    settings["cost_mode"] = value
    settings["selection_strength"] = strength
    save_settings(settings)
    return cost_mode_status()


def reset_cost_mode() -> dict[str, Any]:
    settings = load_settings()
    settings["cost_mode"] = "auto"
    settings["selection_strength"] = "prefer"
    settings.pop("target_language", None)
    save_settings(settings)
    return cost_mode_status()


def language_status() -> dict[str, Any]:
    language = validate_language(load_settings().get("target_language"))
    return {
        "status": "configured" if language else "unconfigured",
        "target_language": language,
        "scope": "user_default",
    }


def set_language(value: str) -> dict[str, Any]:
    settings = load_settings()
    settings["target_language"] = validate_language(value)
    save_settings(settings)
    return language_status()


def reset_language() -> dict[str, Any]:
    settings = load_settings()
    settings.pop("target_language", None)
    save_settings(settings)
    return language_status()


def language_qualification_results_path() -> Path:
    configured = os.environ.get("EMPIRE_LANGUAGE_QUALIFICATION_RESULTS_PATH")
    return (
        Path(configured).expanduser()
        if configured
        else DEFAULT_LANGUAGE_QUALIFICATION_RESULTS_PATH
    )


def load_language_qualification_pack() -> dict[str, Any]:
    try:
        pack = json.loads(LANGUAGE_QUALIFICATION_PACK.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RouterError(f"Language qualification pack is unavailable: {exc}") from exc
    if pack.get("schema_version") != "1.0.0":
        raise RouterError("Unsupported language qualification pack schema")
    locales = pack.get("locales")
    dimensions = pack.get("dimensions")
    cases = pack.get("cases")
    policy = pack.get("verification_policy")
    if not isinstance(locales, list) or not locales:
        raise RouterError("Language qualification pack has no locales")
    if not isinstance(dimensions, list) or not dimensions:
        raise RouterError("Language qualification pack has no dimensions")
    if not isinstance(cases, list) or not cases:
        raise RouterError("Language qualification pack has no test cases")
    if not isinstance(policy, dict):
        raise RouterError("Language qualification pack has no verification policy")
    locale_tags = {
        validate_language(str(item.get("tag")))
        for item in locales
        if isinstance(item, dict)
    }
    if None in locale_tags or not locale_tags:
        raise RouterError("Language qualification pack contains an invalid locale")
    case_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("locale"):
            raise RouterError(
                "Language qualification pack contains an invalid test case"
            )
        if case["id"] in case_ids:
            raise RouterError(
                "Language qualification pack contains duplicate test case IDs"
            )
        case_ids.add(case["id"])
        if validate_language(str(case["locale"])) not in locale_tags:
            raise RouterError(
                "Language qualification case references an unknown locale"
            )
        if not isinstance(case.get("deterministic_checks"), list):
            raise RouterError("Language qualification case lacks deterministic checks")
    return pack


def language_qualification_status() -> dict[str, Any]:
    pack = load_language_qualification_pack()
    locale_tags = [validate_language(str(item["tag"])) for item in pack["locales"]]
    results_path = language_qualification_results_path()
    evaluations: list[dict[str, Any]] = []
    if results_path.exists():
        try:
            result_data = json.loads(results_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RouterError(
                f"Language qualification results are invalid: {exc}"
            ) from exc
        if (
            result_data.get("schema_version") != "1.0.0"
            or result_data.get("pack_id") != pack.get("pack_id")
            or result_data.get("pack_version") != pack.get("pack_version")
            or not isinstance(result_data.get("evaluations"), list)
        ):
            raise RouterError(
                "Language qualification results do not match the active pack"
            )
        evaluations = result_data["evaluations"]

    threshold = float(pack["verification_policy"]["minimum_total_score"])
    verified: list[dict[str, Any]] = []
    for item in evaluations:
        if not isinstance(item, dict):
            continue
        model_id = str(item.get("model_id", "")).strip()
        locale = validate_language(str(item.get("locale", "")))
        dimension_scores = item.get("dimension_scores")
        complete_dimensions = isinstance(dimension_scores, dict) and all(
            dimension in dimension_scores for dimension in pack["dimensions"]
        )
        if (
            model_id
            and not model_id.lower().startswith("openai/")
            and locale in locale_tags
            and item.get("deterministic_pass") is True
            and item.get("human_reviewed") is True
            and complete_dimensions
            and float(item.get("total_score", -1)) >= threshold
            and item.get("evaluated_at")
        ):
            verified.append(
                {
                    "model_id": model_id,
                    "locale": locale,
                    "total_score": float(item["total_score"]),
                    "evaluated_at": item["evaluated_at"],
                }
            )
    verified_locales = sorted({item["locale"] for item in verified})
    return {
        "status": "qualified_models_available" if verified else "framework_ready",
        "pack_id": pack["pack_id"],
        "pack_version": pack["pack_version"],
        "case_count": len(pack["cases"]),
        "locales": locale_tags,
        "verified_locales": verified_locales,
        "unverified_locales": [
            tag for tag in locale_tags if tag not in verified_locales
        ],
        "verified_models": verified,
        "verification_policy": {
            "minimum_total_score": threshold,
            "deterministic_pass_required": True,
            "human_review_required": True,
            "openai_excluded": True,
        },
        "results_present": results_path.exists(),
        "note": "No model or locale is marked verified without complete deterministic and human-reviewed evidence.",
    }


def remove_direct_provider(assume_yes: bool = False) -> dict[str, Any]:
    settings = load_settings()
    instance_id, config = configured_direct_provider(settings)
    if not isinstance(config, dict) or instance_id is None:
        return {"status": "not_configured"}
    if not assume_yes:
        answer = (
            input("Delete the direct-provider credential and settings? [y/N] ")
            .strip()
            .lower()
        )
        if answer not in {"y", "yes"}:
            return {"status": "cancelled"}
    name = provider_slug(str(config.get("name", "")))
    deleted = credential_delete(provider_account(name))
    settings["providers"]["instances"].pop(instance_id, None)
    openrouter = settings["providers"]["instances"].setdefault(
        "openrouter",
        {
            "provider_id": "openrouter",
            "kind": "aggregator",
            "credential_ref": "openrouter",
        },
    )
    openrouter["enabled"] = True
    settings["inference_provider"] = "openrouter"
    settings["routing_policy"] = default_settings()["routing_policy"]
    save_settings(settings)
    return {"status": "deleted", "credential_deleted": deleted}


def doctor() -> dict[str, Any]:
    openrouter, openrouter_source = resolve_credential(
        ("OPENROUTER_API_KEY",), "openrouter"
    )
    aa, aa_source = resolve_credential(
        ("ARTIFICIAL_ANALYSIS_API_KEY", "AA_API_KEY"), "artificial-analysis"
    )
    settings = load_settings()
    return {
        "inference_provider": settings.get("inference_provider", "openrouter"),
        "openrouter": credential_status(openrouter, openrouter_source),
        "artificial_analysis": credential_status(aa, aa_source),
        "direct_provider": direct_provider_status(settings),
    }


def setup_credentials() -> dict[str, Any]:
    backend, _ = credential_backend()
    openrouter = getpass.getpass("OpenRouter API key: ").strip()
    artificial_analysis = getpass.getpass(
        "Artificial Analysis API key (optional, press Enter to skip): "
    ).strip()
    if not openrouter:
        raise RouterError("OpenRouter API key is required")
    openrouter_status = store_and_verify_credential("openrouter", openrouter)
    if artificial_analysis:
        aa_status = store_and_verify_credential(
            "artificial-analysis", artificial_analysis
        )
    else:
        aa_probe = credential_probe("artificial-analysis")
        aa_status = credential_status(aa_probe["value"], aa_probe["source"])
    openrouter_public = {
        key: value
        for key, value in openrouter_status.items()
        if key not in {"backend", "verified"}
    }
    aa_public = {
        key: value
        for key, value in aa_status.items()
        if key not in {"backend", "verified"}
    }
    return {
        "status": (
            "configured"
            if openrouter_status["verified"]
            else "configured_unverified"
        ),
        "service": KEYCHAIN_SERVICE,
        "credential_backend": backend,
        "openrouter": openrouter_public,
        "artificial_analysis": aa_public,
    }


def logout_credentials(assume_yes: bool = False) -> dict[str, Any]:
    credential_backend()
    if not assume_yes:
        answer = (
            input("Delete Empire Review credentials from the system keyring? [y/N] ")
            .strip()
            .lower()
        )
        if answer not in {"y", "yes"}:
            return {"status": "cancelled"}
    settings = load_settings()
    direct_id, direct = configured_direct_provider(settings)
    direct_deleted = False
    if isinstance(direct, dict) and direct_id is not None:
        direct_deleted = credential_delete(
            provider_account(str(direct.get("name", "")))
        )
        settings["providers"]["instances"].pop(direct_id, None)
        settings["providers"]["instances"].setdefault(
            "openrouter",
            {
                "provider_id": "openrouter",
                "kind": "aggregator",
                "credential_ref": "openrouter",
            },
        )["enabled"] = True
        settings["inference_provider"] = "openrouter"
        settings["routing_policy"] = default_settings()["routing_policy"]
        save_settings(settings)
    return {
        "status": "deleted",
        "openrouter": {"deleted": credential_delete("openrouter")},
        "artificial_analysis": {"deleted": credential_delete("artificial-analysis")},
        "direct_provider": {"deleted": direct_deleted},
    }


def validate_outbound_https_url(value: str) -> str:
    cleaned = value.strip()
    parsed = urlparse(cleaned)
    if (
        parsed.scheme != "https"
        or not parsed.netloc
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.fragment
        or _nonpublic_hostname(parsed.hostname)
        or _unsafe_url_shape(cleaned, parsed)
    ):
        raise RouterError("Outbound provider URL must use remote HTTPS without credentials")
    return cleaned


def secure_urlopen(request: Request, timeout: int):
    opener = build_opener(RejectRedirects(), HTTPSHandler(context=tls_context()))
    return opener.open(request, timeout=timeout)


def _set_response_read_timeout(response: Any, remaining_seconds: float) -> bool:
    """Best-effort socket deadline tightening for urllib response implementations."""
    candidates = [
        getattr(getattr(response, "fp", None), "raw", None),
        getattr(response, "fp", None),
    ]
    for candidate in candidates:
        sock = getattr(candidate, "_sock", None)
        if sock is not None and hasattr(sock, "settimeout"):
            sock.settimeout(max(0.001, remaining_seconds))
            return True
    return False


def _provider_references_from_headers(headers: Any) -> dict[str, str | None]:
    """Copy only billing-correlation identifiers from provider response headers."""

    def header(*names: str) -> str | None:
        for name in names:
            try:
                value = headers.get(name)
            except AttributeError:
                value = None
            if isinstance(value, str) and value.strip():
                return value.strip()[:200]
        return None

    return {
        "provider_generation_id": header(
            "X-Generation-Id", "X-OpenRouter-Generation-Id"
        ),
        "provider_request_id": header("X-Request-Id", "X-OpenRouter-Request-Id"),
    }


def request_json(
    url: str,
    *,
    api_key: str | None = None,
    headers: dict[str, str] | None = None,
    body: dict[str, Any] | None = None,
    timeout: int = 30,
    max_response_bytes: int = DEFAULT_MAX_PROVIDER_RESPONSE_BYTES,
) -> dict[str, Any]:
    url = validate_outbound_https_url(url)
    if timeout <= 0:
        raise RouterError("Provider total deadline must be positive")
    started = time.monotonic()
    deadline = started + timeout
    merged = {"Accept": "application/json", "User-Agent": "empire-review/0.1"}
    if headers:
        merged.update(headers)
    if api_key:
        merged["Authorization"] = f"Bearer {api_key}"
    payload = None
    if body is not None:
        payload = json.dumps(body).encode()
        merged["Content-Type"] = "application/json"
    req = Request(
        url, data=payload, headers=merged, method="POST" if payload else "GET"
    )
    if max_response_bytes <= 0:
        raise RouterError("Provider response byte ceiling must be positive")
    provider_references: dict[str, str | None] = {
        "provider_generation_id": None,
        "provider_request_id": None,
    }
    try:
        with secure_urlopen(req, timeout) as response:
            provider_references = _provider_references_from_headers(response.headers)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise AmbiguousProviderOutcome(
                    "Provider total deadline expired before response capture",
                    **provider_references,
                )
            socket_deadline_applied = _set_response_read_timeout(response, remaining)
            content_length = response.headers.get("Content-Length")
            if content_length is not None:
                try:
                    declared_size = int(content_length)
                except ValueError as exc:
                    raise AmbiguousProviderOutcome(
                        "Provider returned an invalid Content-Length after dispatch",
                        **provider_references,
                    ) from exc
                if declared_size > max_response_bytes:
                    raise AmbiguousProviderOutcome(
                        "Provider response exceeded the configured byte ceiling",
                        **provider_references,
                    )
            try:
                encoded = response.read(max_response_bytes + 1)
                if len(encoded) > max_response_bytes:
                    raise AmbiguousProviderOutcome(
                        "Provider response exceeded the configured byte ceiling",
                        **provider_references,
                    )
                decoded = json.loads(encoded)
                if not isinstance(decoded, dict):
                    raise AmbiguousProviderOutcome(
                        "Provider returned a non-object response after dispatch",
                        **provider_references,
                    )
                elapsed = time.monotonic() - started
                decoded["_empire_transport"] = {
                    **provider_references,
                    "rate_limit": {
                        key: value[:200]
                        for key, header_name in (
                            ("limit", "X-RateLimit-Limit"),
                            ("remaining", "X-RateLimit-Remaining"),
                            ("reset", "X-RateLimit-Reset"),
                            ("retry_after", "Retry-After"),
                        )
                        if isinstance((value := response.headers.get(header_name)), str)
                        and value.strip()
                    }
                    or None,
                    "total_deadline_seconds": timeout,
                    "elapsed_seconds": round(elapsed, 6),
                    "deadline_exceeded": elapsed > timeout,
                    "socket_deadline_applied": socket_deadline_applied,
                }
                return decoded
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise AmbiguousProviderOutcome(
                    f"Provider returned an unreadable response after dispatch: {url}",
                    **provider_references,
                ) from exc
    except HTTPError as exc:
        provider_references = _provider_references_from_headers(exc.headers)
        try:
            detail = exc.read(1000).decode(errors="replace")
        except Exception as read_exc:
            raise ProviderRequestError(
                exc.code,
                url,
                "request rejected",
                None,
                **provider_references,
            ) from read_exc
        parsed_error: dict[str, Any] = {}
        try:
            candidate = json.loads(detail)
            parsed_error = candidate if isinstance(candidate, dict) else {}
            message = parsed_error.get("error", {}).get("message") or "request rejected"
        except (json.JSONDecodeError, AttributeError):
            message = "request rejected"
        if parsed_error:
            parsed_error["_empire_transport"] = provider_references
            provider_references = provider_reference_data(parsed_error)
        metadata = parsed_error.get("openrouter_metadata")
        raise ProviderRequestError(
            exc.code,
            url,
            str(message),
            metadata if isinstance(metadata, dict) else None,
            **provider_references,
        ) from exc
    except AmbiguousProviderOutcome:
        raise
    except Exception as exc:
        raise AmbiguousProviderOutcome(
            f"Provider outcome is ambiguous after dispatch: {url}",
            **provider_references,
        ) from exc


def fixture(path: Path, name: str) -> dict[str, Any]:
    with (path / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], text=True, capture_output=True, timeout=20
    )
    if proc.returncode:
        raise RouterError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def git_optional(repo: Path, *args: str) -> str | None:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], text=True, capture_output=True, timeout=20
    )
    return proc.stdout.strip() if proc.returncode == 0 else None


def inside(repo: Path, value: str) -> Path:
    candidate = (repo / value).resolve()
    try:
        candidate.relative_to(repo)
    except ValueError as exc:
        raise RouterError(f"Path escapes repository: {value}") from exc
    if not candidate.is_file():
        raise RouterError(f"Not a readable file: {value}")
    return candidate


def is_sensitive_path(path: Path) -> bool:
    lower_name = path.name.lower()
    return (
        lower_name in SENSITIVE_NAMES
        or lower_name.startswith(".env.")
        or path.suffix.lower() in SENSITIVE_SUFFIXES
    )


def redact_evidence(value: str) -> tuple[str, int]:
    redactions = 0
    for pattern in SECRET_PATTERNS:
        value, count = pattern.subn(
            lambda match: (match.group(1) if match.lastindex else "")
            + "[REDACTED_SECRET]",
            value,
        )
        redactions += count
    return value, redactions


def validate_external_text(label: str, value: str, *, max_chars: int) -> str:
    normalized = value.strip()
    if not normalized:
        raise RouterError(f"{label} must not be empty")
    if len(normalized) > max_chars:
        raise RouterError(f"{label} exceeds the {max_chars}-character limit")
    findings = secret_findings(normalized)
    if findings:
        raise RouterError(
            f"{label} rejected by secret policy: " + ", ".join(findings)
        )
    return normalized


def changed_paths(root: Path) -> list[Path]:
    names: list[str] = []
    for args in (
        ("diff", "--cached", "--name-only", "-z", "--"),
        ("diff", "--name-only", "-z", "--"),
    ):
        names.extend(item for item in git(root, *args).split("\0") if item)
    paths: list[Path] = []
    seen: set[Path] = set()
    for name in names:
        path = (root / name).resolve(strict=False)
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise RouterError(f"Changed path escapes repository: {name}") from exc
        if path not in seen:
            seen.add(path)
            paths.append(path)
    return paths


def validate_evidence_paths(paths: list[Path], root: Path) -> None:
    rejected = [
        str(path.relative_to(root)) for path in paths if is_sensitive_path(path)
    ]
    if rejected:
        raise RouterError(
            "Sensitive changed paths cannot be routed: " + ", ".join(sorted(rejected))
        )


def collect_evidence(
    repo_value: str,
    files: list[str],
    max_bytes: int,
    evidence_mode: str = "diff",
) -> tuple[str, dict[str, Any]]:
    repo = Path(repo_value).expanduser().resolve()
    if not repo.is_dir():
        raise RouterError(f"Repository is not a directory: {repo}")
    root = Path(git(repo, "rev-parse", "--show-toplevel").strip()).resolve()
    try:
        repo.relative_to(root)
    except ValueError as exc:
        raise RouterError("Requested directory is outside its Git worktree") from exc
    if len(files) > MAX_FILES:
        raise RouterError(f"At most {MAX_FILES} files may be selected")
    if max_bytes <= 0:
        raise RouterError("--max-bytes must be greater than zero")
    if evidence_mode not in {"diff", "files-only"}:
        raise RouterError(f"Unsupported evidence mode: {evidence_mode}")
    if evidence_mode == "files-only" and not files:
        raise RouterError("--evidence-mode files-only requires at least one --file")

    parts = []
    if evidence_mode == "diff":
        changed = changed_paths(root)
        validate_evidence_paths(changed, root)
        staged = git(root, "diff", "--cached", "--no-ext-diff", "--unified=3", "--")
        unstaged = git(root, "diff", "--no-ext-diff", "--unified=3", "--")
        if staged:
            parts.append("## Staged diff\n" + staged)
        if unstaged:
            parts.append("## Unstaged diff\n" + unstaged)
    read_files: list[str] = []
    explicit_paths: list[Path] = []
    for value in files:
        path = inside(root, value)
        explicit_paths.append(path)
    validate_evidence_paths(explicit_paths, root)
    for path in explicit_paths:
        rel = str(path.relative_to(root))
        if evidence_mode == "files-only" and path.stat().st_size > max_bytes:
            raise RouterError(f"Selected file exceeds --max-bytes: {rel}")
        content = path.read_text(encoding="utf-8", errors="replace")
        candidate = parts + [f"## File: {rel}\n" + content]
        if evidence_mode == "files-only" and len("\n".join(candidate).encode()) > max_bytes:
            raise RouterError("Selected files exceed the aggregate --max-bytes limit")
        parts = candidate
        read_files.append(rel)
    evidence = "\n".join(parts)
    findings = secret_findings(evidence)
    if findings:
        raise RouterError(
            "Outbound evidence rejected by secret policy: " + ", ".join(findings)
        )
    redactions = 0
    encoded = evidence.encode()
    truncated = len(encoded) > max_bytes
    if truncated:
        evidence = encoded[:max_bytes].decode(errors="ignore") + "\n[TRUNCATED]"
    head = git_optional(root, "rev-parse", "HEAD")
    status = git(root, "status", "--porcelain")
    untracked = [line[3:] for line in status.splitlines() if line.startswith("?? ")]
    dirty = bool(status)
    return evidence, {
        "source": "bounded_files_only"
        if evidence_mode == "files-only"
        else "local_git_diff_and_bounded_files",
        "evidence_mode": evidence_mode,
        "evidence_manifest": [
            {"path": relative, "source": "explicit_file"} for relative in read_files
        ],
        "diff_included": evidence_mode == "diff" and bool(staged or unstaged),
        "repository_root": str(root),
        "commit": head,
        "unborn_repository": head is None,
        "dirty": dirty,
        "files_reviewed": read_files,
        "bytes": min(len(encoded), max_bytes),
        "truncated": truncated,
        "secret_redactions": redactions,
        "untracked_file_count": len(untracked),
        "warning": "Untracked files are not included unless selected with --file"
        if untracked
        else None,
        "repository_state_verified": True,
    }


def number(obj: dict[str, Any], *keys: str) -> float | None:
    for key in keys:
        value: Any = obj
        for part in key.split("."):
            if not isinstance(value, dict):
                value = None
                break
            value = value.get(part)
        try:
            if value is not None:
                return float(value)
        except (TypeError, ValueError):
            pass
    return None


def token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def model_identity(model_id: str, display_name: str) -> dict[str, Any]:
    publisher, separator, api_model_id = model_id.partition("/")
    if not separator:
        publisher = "unknown"
        api_model_id = model_id
    publisher = catalog_provider_slug(publisher)
    identity_text = f"{api_model_id} {display_name}".lower()
    family_aliases = (
        ("claude", "claude"),
        ("gemini", "gemini"),
        ("deepseek", "deepseek"),
        ("qwen", "qwen"),
        ("grok", "grok"),
        ("llama", "llama"),
        ("mistral", "mistral"),
        ("command", "command"),
        ("gpt", "gpt"),
        ("o1", "o-series"),
        ("o3", "o-series"),
        ("o4", "o-series"),
    )
    family = next(
        (
            canonical
            for keyword, canonical in family_aliases
            if keyword in identity_text
        ),
        publisher,
    )
    claude_match = re.search(
        r"^claude-(?P<edition>[a-z][a-z0-9]*)-(?P<major>\d+)"
        r"(?:-(?P<minor>\d+))?(?:-(?P<snapshot>\d{8}))?$",
        api_model_id,
    )
    version_match = re.search(r"(?<!\d)(\d+(?:\.\d+){0,2})(?!\d)", api_model_id)
    model_version = version_match.group(1) if version_match else None
    model_snapshot = None
    edition = "standard"
    if claude_match:
        edition = claude_match.group("edition")
        model_version = claude_match.group("major")
        if claude_match.group("minor"):
            model_version += f".{claude_match.group('minor')}"
        model_snapshot = claude_match.group("snapshot")
    elif version_match:
        suffix = api_model_id[version_match.end() :].strip("-_. ")
        if suffix:
            edition = suffix.split("-", 1)[0]
    elif family != publisher:
        family_position = api_model_id.lower().find(family)
        if family_position >= 0:
            suffix = api_model_id[family_position + len(family) :].strip("-_. ")
            if suffix:
                edition = suffix.split("-", 1)[0]
    is_tts = family == "gemini" and "tts" in api_model_id.lower()
    if is_tts:
        edition = (
            api_model_id[version_match.end() :].strip("-_. ")
            if version_match
            else "tts"
        )
    return {
        "model_name": display_name,
        "display_name": display_name,
        "publisher": publisher,
        "model_family": family,
        "model_version": model_version,
        "model_edition": edition,
        "model_snapshot": model_snapshot,
        "model_kind": "text_to_speech" if is_tts else "language_model",
        "modalities": ["text", "audio"] if is_tts else ["text"],
        "api_model_id": api_model_id,
    }


def model_endpoints(model_id: str) -> list[dict[str, Any]]:
    publisher, separator, api_model_id = model_id.partition("/")
    publisher = catalog_provider_slug(publisher) if separator else "unknown"
    api_model_id = api_model_id if separator else model_id
    endpoints = [
        {
            "provider": "openrouter",
            "api": "chat_completions",
            "url": OPENROUTER_CHAT,
            "model_id": model_id,
            "preferred": publisher
            not in {"openai", "anthropic", "google", "x-ai", "deepseek"},
        }
    ]
    if publisher == "openai":
        endpoints.extend(
            [
                {
                    "provider": "openai",
                    "api": "responses",
                    "url": OPENAI_RESPONSES,
                    "model_id": api_model_id,
                    "preferred": True,
                },
                {
                    "provider": "openai",
                    "api": "chat_completions",
                    "url": OPENAI_CHAT,
                    "model_id": api_model_id,
                    "preferred": False,
                },
                {
                    "provider": "openai",
                    "api": "batch",
                    "url": OPENAI_BATCHES,
                    "model_id": api_model_id,
                    "preferred": False,
                },
            ]
        )
    elif publisher == "anthropic":
        endpoints.extend(
            [
                {
                    "provider": "anthropic",
                    "api": "messages",
                    "url": ANTHROPIC_MESSAGES,
                    "model_id": api_model_id,
                    "preferred": True,
                },
                {
                    "provider": "anthropic",
                    "api": "count_tokens",
                    "url": ANTHROPIC_COUNT_TOKENS,
                    "model_id": api_model_id,
                    "preferred": False,
                },
                {
                    "provider": "anthropic",
                    "api": "message_batch",
                    "url": ANTHROPIC_MESSAGE_BATCHES,
                    "model_id": api_model_id,
                    "preferred": False,
                },
            ]
        )
    elif publisher == "google":
        endpoints.extend(
            [
                {
                    "provider": "google_gemini",
                    "api": "interactions",
                    "url": GEMINI_INTERACTIONS,
                    "model_id": api_model_id,
                    "preferred": True,
                },
                {
                    "provider": "google_gemini",
                    "api": "generate_content",
                    "url": GEMINI_GENERATE_CONTENT.format(model=api_model_id),
                    "model_id": api_model_id,
                    "preferred": False,
                },
                {
                    "provider": "google_gemini",
                    "api": "stream_generate_content",
                    "url": GEMINI_STREAM_GENERATE_CONTENT.format(model=api_model_id),
                    "model_id": api_model_id,
                    "preferred": False,
                },
                {
                    "provider": "google_gemini",
                    "api": "count_tokens",
                    "url": GEMINI_COUNT_TOKENS.format(model=api_model_id),
                    "model_id": api_model_id,
                    "preferred": False,
                },
            ]
        )
    elif publisher == "x-ai":
        endpoints.extend(
            [
                {
                    "provider": "xai",
                    "api": "responses",
                    "url": XAI_RESPONSES,
                    "model_id": api_model_id,
                    "preferred": True,
                },
                {
                    "provider": "xai",
                    "api": "chat_completions",
                    "url": XAI_CHAT,
                    "model_id": api_model_id,
                    "preferred": False,
                },
            ]
        )
    elif publisher == "deepseek":
        endpoints.append(
            {
                "provider": "deepseek",
                "api": "chat_completions",
                "url": DEEPSEEK_CHAT,
                "model_id": api_model_id,
                "preferred": True,
            }
        )
    return endpoints


@lru_cache(maxsize=1)
def load_icon_manifest() -> dict[str, Any]:
    try:
        with ICON_MANIFEST.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise RouterError(f"Model icon manifest is unavailable: {exc}") from exc


def resolve_model_icon(model_id: str, display_name: str) -> dict[str, Any]:
    manifest = load_icon_manifest()
    icons = {item["id"]: item for item in manifest.get("icons", [])}
    aliases = manifest.get("aliases", {})
    text = f"{model_id} {display_name}".lower()
    # OpenRouter prefixes floating aliases with `~`; it is not part of the
    # publisher identity and must not force a generic OpenRouter icon.
    provider = model_id.removeprefix("~").split("/", 1)[0].lower()
    families = (
        ("claude", "claude", {"anthropic"}),
        ("gemini", "gemini", {"google"}),
        ("gemma", "gemma", {"google"}),
        ("lyria", "lyria", {"google"}),
        ("nova-", "nova", {"amazon"}),
        ("mercury", "inception", {"inception"}),
        ("venice", "venice", {"cognitivecomputations"}),
        ("lfm", "liquid", {"liquid"}),
        ("longcat", "longcat", {"meituan"}),
        ("deepseek", "deepseek", {"deepseek"}),
        ("qwen", "qwen", {"qwen"}),
        ("grok", "grok", {"x-ai"}),
        ("kimi", "moonshot", {"moonshotai"}),
        ("mimo", "xiaomi-mimo", {"xiaomi"}),
        ("mistral", "mistral", {"mistralai"}),
        ("llama", "meta", {"meta", "meta-llama"}),
    )
    family_icon_id = next(
        (
            target
            for keyword, target, publishers in families
            if keyword in text and provider in publishers
        ),
        None,
    )
    provider_aliases = {
        "anthropic": "anthropic",
        "google": "gemini",
        "meta-llama": "meta",
        "mistralai": "mistral",
        "moonshotai": "moonshot",
        "x-ai": "grok",
        "z-ai": "zai",
        "arcee-ai": "arcee",
        "nousresearch": "nousresearch",
    }
    provider_icon_id = provider_aliases.get(provider, aliases.get(provider, provider))
    requested_icon_id = family_icon_id or provider_icon_id
    fallback_used = requested_icon_id not in icons
    icon_id = (
        manifest.get("default_icon_id", "openrouter")
        if fallback_used
        else requested_icon_id
    )
    item = icons[icon_id]
    asset_path = (ICON_ASSET_ROOT / item["path"]).resolve()
    footnote_path = (ICON_ROOT / "footnotes" / f"{icon_id}.png").resolve()
    label = item.get("label") or display_name
    return {
        "icon_id": icon_id,
        "icon_label": label,
        "icon_path": str(asset_path),
        "icon_markdown": f"![{label}](<{asset_path}>)",
        "icon_footnote_path": str(footnote_path),
        "icon_footnote_markdown": f"![{label}](<{footnote_path}>)",
        "icon_status": item.get("status", "unknown"),
        "icon_match": (
            "fallback" if fallback_used else "model_family" if family_icon_id else "provider"
        ),
        "icon_fallback_used": fallback_used,
        "missing_icon_id": requested_icon_id if fallback_used else None,
    }


def synthesis_anchor(model_label: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", model_label.lower()).strip("-")
    return f"empire-synthesis-{slug or 'model'}"


def routed_model_role(selected: dict[str, Any]) -> dict[str, Any]:
    modalities = set(selected.get("modalities") or ["text"])
    modality_supported = "text" in modalities
    route_score = selected.get("route_score")
    benchmark_ranked = bool(
        selected.get("benchmark_matched")
        and selected.get("coding") is not None
        and isinstance(route_score, (int, float))
        and not isinstance(route_score, bool)
    )
    role = "worker" if modality_supported and benchmark_ranked else "partner"
    if role == "worker":
        reason = "ranked coding benchmark matched the code-text modality"
    elif not modality_supported:
        reason = "task modality support is not established"
    else:
        reason = "matching benchmark evidence is unavailable"
    return {
        "role": role,
        "task_modality": "code_text",
        "modality_supported": modality_supported,
        "benchmark_ranked": benchmark_ranked,
        "benchmark_route_score": route_score if benchmark_ranked else None,
        "role_reason": reason,
    }


def contributor_badges(
    selected: dict[str, Any],
    *,
    synthesis_available: bool = False,
    external_status: str = "contributed",
) -> list[dict[str, Any]]:
    lead = resolve_model_icon("openai/codex", "Codex")
    partner = resolve_model_icon(selected["id"], selected["name"])
    routed_role = routed_model_role(selected)
    anchor_id = synthesis_anchor(selected["name"])
    return [
        {
            "role": "lead",
            "model_id": "codex",
            "label": "Codex",
            "badge": "lead",
            "status": "lead",
            "synthesis_available": False,
            "synthesis_anchor": None,
            **lead,
        },
        {
            "model_id": selected["id"],
            "label": selected["name"],
            "badge": routed_role["role"],
            "status": external_status,
            "synthesis_available": synthesis_available,
            "synthesis_anchor": anchor_id if synthesis_available else None,
            **partner,
            **routed_role,
        },
    ]


def _markdown_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", r"\[").replace("]", r"\]")


def _chip_text_width(value: str, pixels_per_character: float) -> int:
    units = sum(2 if ord(character) > 0x7F else 1 for character in value)
    return max(1, round(units * pixels_per_character))


def _rendered_chip_path(entry: dict[str, Any], detail: str | None) -> Path | None:
    """Build one transparent image so Codex never aligns icon and text separately."""
    icon_value = entry.get("icon_footnote_path")
    if not isinstance(icon_value, str) or not icon_value:
        return None
    icon_path = Path(icon_value)
    try:
        icon_data = icon_path.read_bytes()
    except OSError:
        return None
    label = str(entry["label"])
    visible_text = label if detail is None else f"{label} · {detail}"
    text_width = _chip_text_width(visible_text, 8.2)
    width = min(560, max(96, 34 + text_width))
    digest = hashlib.sha256(
        b"composite-v3\0"
        + icon_data
        + b"\0"
        + label.encode()
        + b"\0"
        + (detail or "").encode()
    ).hexdigest()[:24]
    override = os.environ.get("EMPIRE_CHIP_CACHE_DIR")
    directory = (
        Path(override).expanduser()
        if override
        else platform_cache_dir() / "rendered-chips"
    )
    output = directory / f"chip-{digest}.svg"
    if output.is_file():
        return output.resolve()
    icon_uri = "data:image/png;base64," + base64.b64encode(icon_data).decode("ascii")
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" '
        f'viewBox="0 0 {width} 28" role="img" aria-label="{html.escape(visible_text)}">'
        f'<image href="{icon_uri}" x="2" y="4" width="20" height="20"/>'
        f'<text x="30" y="14" dominant-baseline="middle" fill="#f4f4f5" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" '
        f'font-size="14"><tspan font-weight="650">{html.escape(label)}</tspan>'
        + (
            f'<tspan fill="#b5b5bd" font-weight="400"> · {html.escape(detail)}</tspan>'
            if detail is not None
            else ""
        )
        + '</text></svg>'
    )
    try:
        directory.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(directory, 0o700)
        except OSError:
            pass
        temporary = output.with_suffix(".tmp")
        temporary.write_text(svg, encoding="utf-8")
        try:
            os.chmod(temporary, 0o600)
        except OSError:
            pass
        os.replace(temporary, output)
    except OSError:
        return None
    return output.resolve()


def _markdown_icon_chip(entry: dict[str, Any], detail: str | None) -> str:
    label = _markdown_label(str(entry["label"]))
    rendered_path = _rendered_chip_path(entry, detail)
    if rendered_path:
        alt = label if detail is None else f"{label} · {_markdown_label(detail)}"
        image = f"![{alt}](<{rendered_path}>)"
    else:
        # A standalone icon recreates Codex's image/text baseline mismatch.
        # Degrade to readable text when the atomic SVG cannot be cached.
        image = ""
    href = entry.get("href")
    content = image or (
        label if detail is None else f"{label} · {_markdown_label(detail)}"
    )
    if isinstance(href, str) and href:
        content = f"[{content}]({href})"
    return content


def contributor_footnote(contributors: list[dict[str, Any]]) -> dict[str, Any]:
    markdown_parts = []
    text_parts = []
    glyphs = {"lead": "◆", "worker": "◇", "partner": "○"}
    chips = []
    for entry in contributors:
        label = str(entry["label"])
        role = str(entry["role"])
        anchor = entry.get("synthesis_anchor")
        glyph = glyphs.get(role, "·")
        chip = dict(entry)
        footnote_path = entry.get("icon_footnote_path")
        if isinstance(footnote_path, str) and footnote_path:
            chip["icon_footnote_markdown"] = f"![{label}](<{footnote_path}>)"
        status = str(entry.get("status") or "")
        detail = role if status in {"", "lead", "contributed"} else f"{status} {role}"
        if entry.get("synthesis_available") and isinstance(anchor, str):
            chip["href"] = f"#{anchor}"
        markdown_parts.append(_markdown_icon_chip(chip, detail))
        text_parts.append(f"{glyph} {label} · {detail}")
        chips.append(
            {
                "kind": "model",
                "label": label,
                "detail": detail,
                "model_id": entry.get("model_id"),
                "icon_id": entry.get("icon_id"),
                "icon_svg_path": entry.get("icon_path"),
                "icon_footnote_path": entry.get("icon_footnote_path"),
                "icon_match": entry.get("icon_match"),
                "icon_fallback_used": entry.get("icon_fallback_used", False),
                "missing_icon_id": entry.get("missing_icon_id"),
                "href": chip.get("href"),
            }
        )
    return {
        "markdown": "  ".join(markdown_parts),
        "text_fallback": "  ·  ".join(text_parts),
        "placement": "response_footer",
        "renderer": "codex_markdown_composite_chips",
        "layout": "inline_composite_footnote_chips",
        "icon_assets": "transparent_svg_chip_with_embedded_14px_png_icon_and_vector_text",
        "alignment": "single_image_internal_alignment",
        "chips": chips,
        "raw_html_disabled": "Codex displays raw HTML as escaped text",
        "image_fallback": "Use text_fallback if the Codex surface does not render local Markdown images.",
    }


def _base_model_label(value: str) -> str:
    """Remove provider branding while preserving the model's readable base name."""
    label = re.sub(r"^[^:]+:\s*", "", value.strip())
    return re.sub(
        r"^(?:Google|NVIDIA|Anthropic|Meta|Moonshot(?:\s+AI)?|Mistral(?:\s+AI)?|xAI)\s+",
        "",
        label,
        flags=re.IGNORECASE,
    ).strip()


def synthesis_model_footnote(contributors: list[dict[str, Any]]) -> dict[str, Any]:
    """Render external model identity as atomic, base-name-only Codex chips."""
    markdown_parts: list[str] = []
    text_parts: list[str] = []
    chips: list[dict[str, Any]] = []
    for entry in contributors:
        if entry.get("role") == "lead":
            continue
        label = _base_model_label(str(entry["label"]))
        chip = {**entry, "label": label}
        markdown_parts.append(_markdown_icon_chip(chip, None))
        text_parts.append(label)
        chips.append(
            {
                "kind": "model",
                "label": label,
                "model_id": entry.get("model_id"),
                "icon_id": entry.get("icon_id"),
                "icon_svg_path": entry.get("icon_path"),
                "icon_footnote_path": entry.get("icon_footnote_path"),
                "icon_match": entry.get("icon_match"),
                "icon_fallback_used": entry.get("icon_fallback_used", False),
                "missing_icon_id": entry.get("missing_icon_id"),
            }
        )
    return {
        "markdown": "  ".join(markdown_parts),
        "text_fallback": " · ".join(text_parts),
        "placement": "synthesis_or_conclusion_end",
        "renderer": "codex_markdown_composite_chips",
        "layout": "inline_composite_footnote_chips",
        "alignment": "single_image_internal_alignment",
        "label_policy": "base_model_name_only",
        "chips": chips,
    }


def _named_icon(icon_id: str, label: str) -> dict[str, Any]:
    manifest = load_icon_manifest()
    icons = {item["id"]: item for item in manifest.get("icons", [])}
    item = icons.get(icon_id) or icons[manifest.get("default_icon_id", "openrouter")]
    resolved_id = str(item["id"])
    svg_path = (ICON_ASSET_ROOT / item["path"]).resolve()
    footnote_path = (ICON_ROOT / "footnotes" / f"{resolved_id}.png").resolve()
    if not footnote_path.is_file():
        footnote_path = (ICON_ROOT / "footnotes" / "openrouter.png").resolve()
    return {
        "label": label,
        "icon_id": resolved_id,
        "icon_path": str(svg_path),
        "icon_footnote_path": str(footnote_path),
        "icon_footnote_markdown": f"![{label}](<{footnote_path}>)",
    }


def completion_web_sources(payload: dict[str, Any]) -> list[dict[str, str]]:
    """Extract only provider-returned web citations; never invent source URLs."""
    try:
        choice = payload["choices"][0]
        message = choice.get("message") or {}
    except (KeyError, IndexError, TypeError):
        return []
    values: list[Any] = []
    for container in (message, choice, payload):
        if not isinstance(container, dict):
            continue
        for key in ("annotations", "citations"):
            found = container.get(key)
            if isinstance(found, list):
                values.extend(found)
    sources: list[dict[str, str]] = []
    seen: set[str] = set()
    for value in values:
        title = ""
        url = ""
        if isinstance(value, str):
            url = value
        elif isinstance(value, dict):
            citation = value.get("url_citation")
            if isinstance(citation, dict):
                url = str(citation.get("url") or "")
                title = str(citation.get("title") or "")
            else:
                url = str(value.get("url") or value.get("href") or "")
                title = str(value.get("title") or value.get("name") or "")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc or url in seen:
            continue
        seen.add(url)
        sources.append(
            {
                "url": url,
                "label": title.strip() or parsed.netloc.removeprefix("www."),
            }
        )
        if len(sources) == 8:
            break
    return sources


def response_provenance_footnote(
    contributors: list[dict[str, Any]],
    *,
    selected: dict[str, Any] | None,
    route_provider: str | None,
    served_provider: str | None = None,
    artificial_analysis_used: bool = False,
    artificial_analysis: dict[str, Any] | None = None,
    web_sources: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    contributor_footer = contributor_footnote(contributors)
    markdown_parts = [contributor_footer["markdown"]]
    text_parts = [contributor_footer["text_fallback"]]
    chips = list(contributor_footer["chips"])

    if route_provider == "openrouter":
        route_icon = _named_icon("openrouter", "OpenRouter")
        route_label = "OpenRouter"
    elif route_provider == "direct" and selected:
        route_label = str(selected.get("provider") or "Direct provider")
        route_icon = resolve_model_icon(f"{route_label}/provider", route_label)
    else:
        route_icon = None
        route_label = ""
    if route_icon:
        route_chip = {**route_icon, "label": route_label}
        markdown_parts.append(_markdown_icon_chip(route_chip, "route"))
        text_parts.append(f"{route_label} · route")
        chips.append(
            {
                "kind": "routing_provider",
                "label": route_label,
                "detail": "route",
                "icon_id": route_icon.get("icon_id"),
                "icon_svg_path": route_icon.get("icon_path"),
                "icon_footnote_path": route_icon.get("icon_footnote_path"),
                "href": None,
            }
        )

    if served_provider and served_provider.casefold() != route_label.casefold():
        served_icon = resolve_model_icon(f"{served_provider}/provider", served_provider)
        served_chip = {**served_icon, "label": served_provider}
        markdown_parts.append(_markdown_icon_chip(served_chip, "served"))
        text_parts.append(f"{served_provider} · served")
        chips.append(
            {
                "kind": "served_provider",
                "label": served_provider,
                "detail": "served",
                "icon_id": served_icon.get("icon_id"),
                "icon_svg_path": served_icon.get("icon_path"),
                "icon_footnote_path": served_icon.get("icon_footnote_path"),
                "icon_match": served_icon.get("icon_match"),
                "icon_fallback_used": served_icon.get("icon_fallback_used", False),
                "missing_icon_id": served_icon.get("missing_icon_id"),
                "href": None,
            }
        )

    if artificial_analysis_used:
        aa_icon = _named_icon("artificial-analysis", "Artificial Analysis")
        markdown_parts.append(_markdown_icon_chip(aa_icon, "benchmark evidence"))
        text_parts.append("Artificial Analysis · benchmark evidence")
        chips.append(
            {
                "kind": "benchmark_source",
                "label": "Artificial Analysis",
                "detail": "benchmark evidence",
                "icon_id": aa_icon.get("icon_id"),
                "icon_svg_path": aa_icon.get("icon_path"),
                "icon_footnote_path": aa_icon.get("icon_footnote_path"),
                "snapshot": artificial_analysis or {},
                "href": None,
            }
        )

    for source in web_sources or []:
        label = _markdown_label(source["label"])
        url = source["url"]
        markdown_parts.append(f"[{label}]({url}) · web source")
        text_parts.append(f"{source['label']} · web source")
        chips.append(
            {
                "kind": "web_source",
                "label": source["label"],
                "detail": "web source",
                "url": url,
                "native_codex_citation_preferred": True,
                "href": url,
            }
        )

    return {
        "markdown": "  ".join(part for part in markdown_parts if part),
        "text_fallback": "  ·  ".join(part for part in text_parts if part),
        "placement": "response_footer",
        "renderer": "codex_markdown_composite_chips",
        "layout": "inline_composite_footnote_chips",
        "chips": chips,
        "svg_source_of_truth": True,
        "codex_image_derivative_px": 14,
        "web_citation_policy": "Use native Codex citation chips for Codex web-tool sources; only provider-returned URLs appear here.",
        "raw_html_disabled": True,
    }


def model_syntheses(
    contributors: list[dict[str, Any]],
    research_artifact: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    return [
        {
            "synthesis_id": entry["synthesis_anchor"],
            "anchor_id": entry["synthesis_anchor"],
            "model_id": entry["model_id"],
            "label": entry["label"],
            "heading": f"Empire synthesis: {entry['label']}",
            "role": entry["role"],
            "kind": "scout_review",
            "source": "review",
            "available": True,
            "research_artifact": research_artifact,
            "footnote": synthesis_model_footnote([entry]),
        }
        for entry in contributors
        if entry.get("synthesis_available") and entry.get("synthesis_anchor")
    ]


def exact_model_index(
    payload: dict[str, Any], identity_field: str
) -> dict[str, dict[str, Any]]:
    """Preserve exact identities and exclude every occurrence of a collision."""
    out: dict[str, dict[str, Any]] = {}
    collisions: set[str] = set()
    rows = payload.get("data", [])
    if not isinstance(rows, list):
        return out
    for row in rows:
        if not isinstance(row, dict):
            continue
        key = row.get(identity_field)
        if not isinstance(key, str) or not key or key != key.strip():
            continue
        if key in out:
            collisions.add(key)
            continue
        out[key] = row
    for key in collisions:
        out.pop(key, None)
    return out


def aa_index(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return exact_model_index(payload, "openrouter_api_id")


def match_aa(model: dict[str, Any], index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    model_id = model.get("id")
    return index.get(model_id, {}) if isinstance(model_id, str) else {}


def first_number(
    primary: dict[str, Any],
    primary_keys: tuple[str, ...],
    fallback: dict[str, Any],
    fallback_keys: tuple[str, ...],
) -> float | None:
    value = number(primary, *primary_keys)
    return value if value is not None else number(fallback, *fallback_keys)


def normalized_languages(model: dict[str, Any], benchmark: dict[str, Any]) -> list[str]:
    values = model.get("supported_languages") or model.get("languages")
    if not values:
        values = benchmark.get("supported_languages") or benchmark.get("languages")
    if not isinstance(values, list):
        return []
    languages: list[str] = []
    for value in values:
        try:
            language = validate_language(str(value))
        except RouterError:
            continue
        if language and language not in languages:
            languages.append(language)
    return languages


def language_eligibility(model: dict[str, Any], target_language: str | None) -> str:
    if not target_language:
        return "not_requested"
    supported = model.get("supported_languages") or []
    if not supported:
        return "unverified"
    requested = target_language.lower()
    base = requested.split("-", 1)[0]
    normalized = {str(item).lower() for item in supported}
    return (
        "verified" if requested in normalized or base in normalized else "unsupported"
    )


def language_routing_mode(model: dict[str, Any], target_language: str | None) -> str:
    if not target_language:
        return "not_requested"
    if model.get("language_eligibility") == "verified":
        return "verified_language_eligibility"
    return "unverified_output_instruction_only"


def normalize_catalog(
    openrouter: dict[str, Any], aa: dict[str, Any], allow_openai: bool
) -> list[dict[str, Any]]:
    # Codex is already the OpenAI lead. Keep OpenAI out of every external
    # partner lineup even if an older caller still passes allow_openai=True.
    del allow_openai
    index = aa_index(aa)
    rows = []
    for model in exact_model_index(openrouter, "id").values():
        model_id = str(model.get("id", ""))
        if not model_id or model_id.lower().startswith("openai/"):
            continue
        pricing = model.get("pricing") or {}
        prompt = number(pricing, "prompt")
        completion = number(pricing, "completion")
        pricing_components = {
            component: number(pricing, component) for component in PRICING_COMPONENTS
        }
        if (
            prompt is None
            or completion is None
            or not math.isfinite(prompt)
            or not math.isfinite(completion)
            or prompt < 0
            or completion < 0
        ):
            continue
        architecture = model.get("architecture")
        if not isinstance(architecture, dict):
            continue
        modalities = architecture.get("input_modalities")
        output_modalities = architecture.get("output_modalities")
        if not isinstance(modalities, list) or not isinstance(output_modalities, list):
            continue
        if not all(
            isinstance(values, list) and "text" in values
            and all(isinstance(value, str) for value in values)
            for values in (modalities, output_modalities)
        ):
            continue
        bench = match_aa(model, index)
        evaluations = bench.get("evaluations") or {}
        params = set(model.get("supported_parameters") or [])
        supports_json = "response_format" in params or "structured_outputs" in params
        supports_output_limit = bool(
            {"max_tokens", "max_completion_tokens"}.intersection(params)
        )
        if not supports_json or not supports_output_limit:
            continue
        display_name = str(model.get("name") or model_id)
        identity = model_identity(model_id, display_name)
        endpoints = model_endpoints(model_id)
        # A normal Empire Review call is text-only and uses no paid search,
        # image, audio, or media tools. Prompt, completion, and fixed request
        # pricing must all be explicitly present and exactly zero before the
        # route can enter the Absolute Zero lane.
        explicit_free_route = model_id.lower().endswith(":free") or (
            model_id.lower() == "openrouter/free"
        )
        request_price = pricing_components.get("request")
        request_cost_verified_zero = request_price == 0 or (
            request_price is None and explicit_free_route
        )
        absolute_zero_text = (
            prompt == 0 and completion == 0 and request_cost_verified_zero
        )
        absolute_zero_basis = (
            "all_text_pricing_components_zero"
            if request_price == 0 and absolute_zero_text
            else "explicit_free_route_with_zero_token_prices"
            if absolute_zero_text
            else None
        )
        rows.append(
            {
                "id": model_id,
                "name": display_name,
                **identity,
                "endpoint_providers": sorted(
                    {endpoint["provider"] for endpoint in endpoints}
                ),
                "endpoints": endpoints,
                "modalities": list(modalities or ["text"]),
                "output_modalities": list(output_modalities),
                "supported_languages": normalized_languages(model, bench),
                "prompt_price": prompt,
                "completion_price": completion,
                "request_price": pricing_components.get("request"),
                "pricing_components": pricing_components,
                "absolute_zero_text": absolute_zero_text,
                "absolute_zero_basis": absolute_zero_basis,
                "free_route_kind": "generic_router"
                if model_id.lower() == "openrouter/free"
                else "explicit_model"
                if explicit_free_route
                else None,
                "blended_price": prompt + completion,
                "context": number(
                    model, "context_length", "top_provider.context_length"
                )
                or 0,
                "coding": first_number(
                    evaluations,
                    ("artificial_analysis_coding_index", "coding_index"),
                    bench,
                    ("coding_index",),
                ),
                "intelligence": first_number(
                    evaluations,
                    ("artificial_analysis_intelligence_index", "intelligence_index"),
                    bench,
                    ("intelligence_index",),
                ),
                "speed": first_number(
                    evaluations,
                    ("output_speed", "tokens_per_second"),
                    bench,
                    (
                        "performance.median_output_tokens_per_second",
                        "median_output_tokens_per_second",
                        "output_speed",
                        "tokens_per_second",
                    ),
                ),
                "capability": (1.0 + float("tools" in params)) / 2,
                "supports_json": True,
                "supports_response_format": "response_format" in params,
                "supports_strict_json": "structured_outputs" in params,
                "supports_output_limit": supports_output_limit,
                "supported_parameters": sorted(params),
                "benchmark_matched": bool(bench),
                "benchmark_model": bench.get("slug") or bench.get("name")
                if bench
                else None,
            }
        )
    return rows


def scaled(values: list[float | None], reverse: bool = False) -> list[float]:
    present = [v for v in values if v is not None and math.isfinite(v)]
    if not present:
        return [0.25] * len(values)
    low, high = min(present), max(present)
    result = []
    for value in values:
        if value is None or not math.isfinite(value):
            score = 0.25
        elif high == low:
            score = 1.0
        else:
            score = (value - low) / (high - low)
        valid = value is not None and math.isfinite(value)
        result.append(1 - score if reverse and valid else score)
    return result


def retryable_free_route_error(error: Exception) -> bool:
    message = str(error)
    return any(
        f"HTTP {status}" in message
        for status in (400, 404, 408, 429, 500, 502, 503, 504)
    )


def route_health_path() -> Path:
    configured = os.environ.get("EMPIRE_ROUTE_HEALTH_PATH")
    return Path(configured).expanduser().resolve() if configured else ROUTE_HEALTH_PATH


def load_route_health() -> dict[str, Any]:
    path = route_health_path()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema_version": 1, "routes": {}}
    if payload.get("schema_version") != 1 or not isinstance(
        payload.get("routes"), dict
    ):
        return {"schema_version": 1, "routes": {}}
    return payload


def record_route_health(
    model_id: str,
    *,
    success: bool,
    status_code: int | None = None,
    category: str | None = None,
) -> None:
    payload = load_route_health()
    routes = payload.setdefault("routes", {})
    previous = routes.get(model_id) if isinstance(routes.get(model_id), dict) else {}
    routes[model_id] = {
        "last_attempt_at": datetime.now(timezone.utc).isoformat(),
        "last_result": "success" if success else "failure",
        "status_code": status_code,
        "category": None if success else category or "provider_rejected",
        "consecutive_failures": 0
        if success
        else int(previous.get("consecutive_failures") or 0) + 1,
    }
    try:
        write_private_json(route_health_path(), payload)
    except OSError:
        # Health memory improves ranking but must never become a transport
        # correctness dependency.
        return


def route_availability_from_health(
    health: dict[str, Any], model_id: str, now: datetime | None = None
) -> float:
    route = health.get("routes", {}).get(model_id)
    if not isinstance(route, dict):
        return 0.5
    try:
        attempted = datetime.fromisoformat(str(route.get("last_attempt_at")))
    except (TypeError, ValueError):
        return 0.5
    if attempted.tzinfo is None:
        attempted = attempted.replace(tzinfo=timezone.utc)
    current = now or datetime.now(timezone.utc)
    if current - attempted > timedelta(minutes=ROUTE_HEALTH_TTL_MINUTES):
        return 0.5
    if route.get("last_result") == "success":
        return 1.0
    category = route.get("category")
    if category in {"no_compatible_endpoint", "request_incompatible"}:
        return 0.0
    return 0.25


def route_availability(model_id: str, now: datetime | None = None) -> float:
    return route_availability_from_health(load_route_health(), model_id, now)


def availability_label(score: float) -> str:
    if score >= 1:
        return "recent_success"
    if score <= 0:
        return "recent_incompatible"
    if score < 0.5:
        return "recent_transient_failure"
    return "unverified_since_catalog_refresh"


def projected_cost_microusd(
    model: dict[str, Any],
    evidence: str,
    max_output_tokens: int,
    planned_units: dict[str, int] | None = None,
) -> int:
    estimated_input_tokens = max(1, math.ceil(len(evidence.encode()) / 4) + 750)
    amount = Decimal(estimated_input_tokens) * Decimal(
        str(model["prompt_price"])
    ) + Decimal(max_output_tokens) * Decimal(str(model["completion_price"]))
    request_price = model.get("request_price")
    if request_price is not None:
        amount += Decimal(str(request_price))
    components = model.get("pricing_components") or {}
    for component, units in (planned_units or {}).items():
        if units < 0:
            raise RouterError("Planned billable units must be non-negative")
        if units == 0:
            continue
        price = components.get(component)
        if price is None:
            raise RouterError(
                f"Cannot authorize {component}: current catalog pricing is unavailable"
            )
        amount += Decimal(units) * Decimal(str(price))
    return usd_to_microusd(amount)


def projected_cost(
    model: dict[str, Any],
    evidence: str,
    max_output_tokens: int,
    planned_units: dict[str, int] | None = None,
) -> float:
    return (
        microusd_to_usd(
            projected_cost_microusd(
                model, evidence, max_output_tokens, planned_units=planned_units
            )
        )
        or 0.0
    )


def context_preflight_receipt(
    args: argparse.Namespace,
    request_text: str,
    selected: dict[str, Any],
    *,
    route_provider: str,
) -> dict[str, Any]:
    """Build a non-enforcing context receipt without retaining request text."""
    try:
        return context_policy.build_preflight_receipt(
            workflow="review",
            request_text=request_text,
            requested_output_tokens=args.max_output_tokens,
            provider_output_limit=None,
            output_limit_supported=bool(
                route_provider == "direct" or selected.get("supports_output_limit")
            ),
            context_limit_tokens=getattr(args, "codex_context_limit_tokens", None),
            current_usage_tokens=getattr(args, "codex_context_used_tokens", None),
            requested_class=getattr(args, "response_class", "automatic"),
        )
    except context_policy.ContextPolicyError as exc:
        raise RouterError(f"Invalid context preflight: {exc}") from exc


def is_absolute_zero_route(model: dict[str, Any]) -> bool:
    return bool(model.get("absolute_zero_text")) and (
        model.get("projected_max_cost_microusd") == 0
    )


def is_value_route(model: dict[str, Any]) -> bool:
    return (
        not is_absolute_zero_route(model)
        and model["prompt_price"] * 1_000_000 <= VALUE_MAX_INPUT_PER_MTOK_USD
        and model["completion_price"] * 1_000_000 <= VALUE_MAX_OUTPUT_PER_MTOK_USD
        and (model.get("projected_max_cost_usd") or 0) <= VALUE_MAX_REQUEST_USD
    )


def task_quality(model: dict[str, Any]) -> float | None:
    values = [
        float(value)
        for value in (model.get("coding"), model.get("intelligence"))
        if isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ]
    return sum(values) / len(values) if values else None


def infer_task_risk(task: str) -> str:
    lowered = task.lower()
    high_markers = (
        "adversarial",
        "security",
        "vulnerability",
        "architecture",
        "correctness",
        "regression",
        "production",
        "critical",
        "audit",
    )
    low_markers = ("summarize", "summary", "format", "rewrite", "typo", "smoke")
    if any(marker in lowered for marker in high_markers):
        return "high"
    if any(marker in lowered for marker in low_markers):
        return "low"
    return "medium"


def task_requests_live_catalog(task: str) -> bool:
    lowered = task.lower()
    return any(
        marker in lowered
        for marker in (
            "latest model",
            "latest available",
            "newest model",
            "newly released",
            "currently available",
            "current model lineup",
            "refresh the catalog",
            "refresh models",
        )
    )


def quality_percentile_floor(
    candidates: list[dict[str, Any]], percentile: float
) -> float | None:
    values = sorted(
        quality for model in candidates if (quality := task_quality(model)) is not None
    )
    if not values:
        return None
    index = min(len(values) - 1, max(0, math.ceil(percentile * len(values)) - 1))
    return values[index]


def pareto_value_pool(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    eligible = [model for model in candidates if is_value_route(model)]
    quality_floor = quality_percentile_floor(candidates, 0.50)
    if quality_floor is not None:
        eligible = [
            model
            for model in eligible
            if task_quality(model) is not None
            and (task_quality(model) or 0) >= quality_floor
        ]
    frontier: list[dict[str, Any]] = []
    for model in eligible:
        model_quality = task_quality(model) or 0
        model_cost = model.get("projected_max_cost_usd") or 0
        dominated = any(
            other is not model
            and (task_quality(other) or 0) >= model_quality
            and (other.get("projected_max_cost_usd") or 0) <= model_cost
            and (
                (task_quality(other) or 0) > model_quality
                or (other.get("projected_max_cost_usd") or 0) < model_cost
            )
            for other in eligible
        )
        if not dominated:
            frontier.append(model)
    return frontier


def frontier_quality_pool(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    paid = [model for model in candidates if not is_absolute_zero_route(model)]
    floor = quality_percentile_floor(paid, 0.80)
    if floor is None:
        return paid
    return [
        model
        for model in paid
        if task_quality(model) is not None and (task_quality(model) or 0) >= floor
    ]


def apply_cost_mode(
    candidates: list[dict[str, Any]],
    cost_mode: str,
    selection_strength: str = "hard_lock",
    task_risk: str = "medium",
) -> tuple[list[dict[str, Any]], str]:
    if cost_mode not in COST_MODES:
        raise RouterError(f"Unknown cost mode: {cost_mode}")
    if selection_strength not in SELECTION_STRENGTHS:
        raise RouterError(f"Unknown selection strength: {selection_strength}")
    free = [model for model in candidates if is_absolute_zero_route(model)]
    value = pareto_value_pool(candidates)
    frontier = frontier_quality_pool(candidates)
    if selection_strength != "hard_lock" and cost_mode != "auto":
        preferred = {
            "free": (free, "absolute_zero"),
            "value": (value, "value_paid"),
            "frontier": (frontier, "frontier_quality"),
        }[cost_mode]
        if preferred[0]:
            return preferred
        if free:
            return free, "absolute_zero"
        if value:
            return value, "value_paid"
        return frontier, "frontier_quality"
    if cost_mode == "free":
        return free, "absolute_zero"
    if cost_mode == "value":
        return value, "value_paid"
    if cost_mode == "frontier":
        return frontier, "frontier_quality"
    if task_risk not in {"low", "medium", "high"}:
        raise RouterError(f"Unknown task risk: {task_risk}")
    auto_quality_floor = quality_percentile_floor(
        candidates, {"low": 0.50, "medium": 0.65, "high": 0.80}[task_risk]
    )
    known_quality = [
        quality for model in candidates if (quality := task_quality(model)) is not None
    ]
    best_quality = max(known_quality) if known_quality else None
    required_best_ratio = {"low": 0.50, "medium": 0.70, "high": 0.85}[task_risk]
    qualified_free = [
        model
        for model in free
        if auto_quality_floor is None
        or (
            task_quality(model) is not None
            and (task_quality(model) or 0) >= auto_quality_floor
            and (
                best_quality is None
                or (task_quality(model) or 0) >= best_quality * required_best_ratio
            )
        )
    ]
    if qualified_free:
        return qualified_free, "absolute_zero"
    if task_risk == "high" and frontier:
        return frontier, "frontier_quality"
    if value:
        return value, "value_paid"
    return frontier, "frontier_quality"


def openrouter_provider_policy(
    cost_lane: str, *, require_zdr: bool = False
) -> dict[str, Any]:
    policy: dict[str, Any] = {
        "require_parameters": True,
        "data_collection": "deny",
        "sort": "price"
        if cost_lane in {"absolute_zero", "value_paid"}
        else "throughput",
    }
    if require_zdr:
        policy["zdr"] = True
    if cost_lane == "absolute_zero":
        # OpenRouter max_price values are USD per million tokens, per request,
        # or per image. A zero ceiling makes the upstream router reject any
        # provider endpoint that would make the bounded text call billable.
        policy["max_price"] = {
            "prompt": 0,
            "completion": 0,
            "request": 0,
            "image": 0,
        }
    elif cost_lane == "value_paid":
        policy["max_price"] = {
            "prompt": VALUE_MAX_INPUT_PER_MTOK_USD,
            "completion": VALUE_MAX_OUTPUT_PER_MTOK_USD,
            "request": VALUE_MAX_REQUEST_USD,
        }
    return policy


def completion_request_body(
    model: dict[str, Any],
    prompt: dict[str, Any],
    max_output_tokens: int,
    *,
    route_provider: str,
    reasoning_effort: str | None = None,
) -> dict[str, Any]:
    """Build a request using only parameters the selected route advertises."""
    body: dict[str, Any] = {
        "model": model.get("api_model_id", model["id"]),
        "messages": [{"role": "user", "content": json.dumps(prompt)}],
    }
    supported = set(model.get("supported_parameters") or [])
    # Direct-provider settings explicitly declare the OpenAI chat-completions
    # protocol, so its compatibility does not depend on OpenRouter metadata.
    permissive_direct = route_provider == "direct"
    if permissive_direct or "temperature" in supported:
        body["temperature"] = 0.1
    if permissive_direct or "max_tokens" in supported:
        body["max_tokens"] = max_output_tokens
    elif "max_completion_tokens" in supported:
        body["max_completion_tokens"] = max_output_tokens
    else:
        raise RouterError(
            f"Selected model does not advertise an output-token limit parameter: {model['id']}"
        )
    if permissive_direct or "response_format" in supported:
        body["response_format"] = {"type": "json_object"}
    else:
        raise RouterError(
            f"Selected model does not advertise JSON response formatting: {model['id']}"
        )
    if reasoning_effort and "reasoning_effort" in supported:
        body["reasoning_effort"] = reasoning_effort
    return body


def review_prompt(
    task: str, target_language: str | None, evidence: str
) -> dict[str, Any]:
    return {
        "task": task,
        "role": "You are one advisory reviewer. Codex is the lead and will verify your findings.",
        "target_language": target_language,
        "requirements": {
            "return_json_only": True,
            "schema": {
                "summary": "string",
                "confidence": "low|medium|high",
                "findings": [
                    {
                        "severity": "critical|high|medium|low",
                        "title": "string",
                        "evidence": "string",
                        "recommendation": "string",
                    }
                ],
            },
            "rules": [
                "Use only supplied evidence",
                "Do not claim repository access",
                "Prefer concrete correctness, security, and regression findings",
            ],
        },
        "repository_evidence": evidence
        or "[No staged/unstaged diff or selected files]",
    }


def lead_only_contributors() -> list[dict[str, Any]]:
    lead = resolve_model_icon("openai/codex", "Codex")
    return [
        {
            "role": "lead",
            "model_id": "codex",
            "label": "Codex",
            "badge": "lead",
            "status": "lead",
            "synthesis_available": False,
            "synthesis_anchor": None,
            **lead,
        }
    ]


def endpoint_model(model: dict[str, Any]) -> dict[str, Any]:
    free_route_kind = model.get("free_route_kind")
    return {
        "id": model["id"],
        "name": model["name"],
        "model_name": model.get("model_name", model["name"]),
        "display_name": model.get("display_name", model["name"]),
        "publisher": model.get("publisher"),
        "model_family": model.get("model_family"),
        "model_version": model.get("model_version"),
        "model_edition": model.get("model_edition", "standard"),
        "model_snapshot": model.get("model_snapshot"),
        "api_model_id": model.get("api_model_id", model["id"]),
        "endpoint_providers": model.get("endpoint_providers", []),
        "endpoints": model.get("endpoints", []),
        "context_tokens": model["context"],
        "input_cost_per_mtok": round(model["prompt_price"] * 1_000_000, 6),
        "output_cost_per_mtok": round(model["completion_price"] * 1_000_000, 6),
        "fixed_request_cost_usd": model.get("request_price"),
        "pricing_components": model.get("pricing_components", {}),
        "absolute_zero_text": bool(model.get("absolute_zero_text")),
        "absolute_zero_basis": model.get("absolute_zero_basis"),
        "free_route_kind": free_route_kind,
        "free_route_warnings": [
            "Zero token cost does not imply unlimited request capacity.",
            "Free endpoints may have lower rate limits, higher latency, or temporary unavailability.",
            *(
                ["The generic free router does not guarantee the exact served model."]
                if free_route_kind == "generic_router"
                else []
            ),
        ]
        if free_route_kind
        else [],
        "output_modalities": model.get("output_modalities", ["text"]),
        "supported_languages": model.get("supported_languages", []),
        "coding_score": model["coding"],
        "intelligence_score": model["intelligence"],
        "speed_tokens_per_second": model["speed"],
        "structured_output": model["supports_json"],
        "benchmark_matched": model["benchmark_matched"],
        "benchmark_model": model["benchmark_model"],
        "route_score": model.get("route_score"),
    }


def build_model_endpoint(
    catalog: dict[str, Any],
    aa: dict[str, Any],
    aa_source: str,
    aa_available: bool,
    catalog_endpoint: str = OPENROUTER_USER_MODELS,
    previous_endpoint: dict[str, Any] | None = None,
) -> dict[str, Any]:
    generated = datetime.now(timezone.utc)
    catalog_models = normalize_catalog(catalog, aa, allow_openai=False)
    candidates = [dict(model) for model in catalog_models]
    proposed: dict[str, list[dict[str, Any]]] = {}
    reference_evidence = "x" * 20_000
    lane_candidates = [dict(model) for model in candidates]
    for model in lane_candidates:
        model["projected_max_cost_microusd"] = projected_cost_microusd(
            model, reference_evidence, 8000
        )
        model["projected_max_cost_usd"] = microusd_to_usd(
            model["projected_max_cost_microusd"]
        )
    for mode in WEIGHTS:
        pool = [dict(model) for model in lane_candidates]
        _, ranked = choose(pool, mode)
        proposed[mode] = [endpoint_model(model) for model in ranked[:5]]
    free_pool, _ = apply_cost_mode(lane_candidates, "free")
    if free_pool:
        _, free_ranked = choose(free_pool, "balanced")
        proposed["free_fallback"] = [
            endpoint_model(model) for model in free_ranked[:10]
        ]
    else:
        free_ranked = []
        proposed["free_fallback"] = []
    value_pool, _ = apply_cost_mode(lane_candidates, "value")
    frontier_pool, _ = apply_cost_mode(lane_candidates, "frontier")
    _, value_ranked = choose(value_pool, "balanced") if value_pool else (None, [])
    _, frontier_ranked = (
        choose(frontier_pool, "quality") if frontier_pool else (None, [])
    )
    automatic_pool, automatic_lane = apply_cost_mode(lane_candidates, "auto")
    automatic_mode = "quality" if automatic_lane == "frontier_quality" else "balanced"
    _, automatic_ranked = (
        choose(automatic_pool, automatic_mode) if automatic_pool else (None, [])
    )
    cost_lanes = {
        "absolute_zero": [endpoint_model(model) for model in free_ranked[:10]],
        "value_paid": [endpoint_model(model) for model in value_ranked[:10]],
        "frontier_quality": [endpoint_model(model) for model in frontier_ranked[:10]],
        "adaptive": [endpoint_model(model) for model in automatic_ranked[:10]],
    }
    previous_ids = {
        str(model.get("id"))
        for model in (previous_endpoint or {}).get("catalog_models", [])
        if isinstance(model, dict) and model.get("id")
    }
    current_ids = {str(model["id"]) for model in catalog_models}
    raw_models = catalog.get("data", [])
    raw_model_count = len(raw_models) if isinstance(raw_models, list) else 0
    return {
        "schema_version": MODEL_ENDPOINT_SCHEMA_VERSION,
        "endpoint": "empire-review://models/proposed",
        "generated_at": generated.isoformat(),
        "expires_at": (
            generated + timedelta(minutes=MODEL_ENDPOINT_TTL_MINUTES)
        ).isoformat(),
        "discovery": {
            "trigger": "empire_invocation",
            "catalog_authority": "authenticated_openrouter_user_catalog",
            "cron_required": False,
            "soft_freshness_minutes": MODEL_ENDPOINT_TTL_MINUTES,
            "maximum_stale_fallback_hours": MODEL_ENDPOINT_MAX_STALE_HOURS,
            "raw_model_count": raw_model_count,
            "eligible_model_count": len(catalog_models),
            "excluded_model_count": max(0, raw_model_count - len(catalog_models)),
            "availability_basis": [
                "authenticated_user_catalog_membership",
                "text_output_and_request_parameter_compatibility",
                "local_recent_route_health",
                "provider_dispatch_validation",
            ],
            "delta": {
                "baseline_available": bool(previous_endpoint),
                "added": sorted(current_ids - previous_ids)
                if previous_endpoint
                else [],
                "removed": sorted(previous_ids - current_ids)
                if previous_endpoint
                else [],
                "retained_count": len(current_ids & previous_ids)
                if previous_endpoint
                else 0,
            },
        },
        "policy": {
            "codex_is_lead": True,
            "openai_excluded": True,
            "openai_excluded_from_partner_selection": True,
            "openai_catalog_included": False,
            "remote_api_routes_only": True,
            "default_cost_ceiling_usd": None,
            "catalog_freshness_minutes": MODEL_ENDPOINT_TTL_MINUTES,
            "cost_modes": list(COST_MODES),
            "selection_strengths": list(SELECTION_STRENGTHS),
            "absolute_zero_required_components": [
                "prompt",
                "completion",
                "request",
            ],
            "absolute_zero_missing_request_rule": (
                "allowed_only_for_explicit_:free_or_openrouter/free_routes"
            ),
            "value_policy": {
                "maximum_input_per_million_usd": VALUE_MAX_INPUT_PER_MTOK_USD,
                "maximum_output_per_million_usd": VALUE_MAX_OUTPUT_PER_MTOK_USD,
                "maximum_estimated_request_usd": VALUE_MAX_REQUEST_USD,
                "minimum_task_quality_percentile": 50,
                "pareto_frontier_required": True,
            },
            "frontier_policy": {
                "minimum_task_quality_percentile": 80,
                "price_is_not_a_quality_proxy": True,
            },
            "language_evidence_policy": "unknown_is_unverified_not_invented",
        },
        "supported_filters": [
            "publisher",
            "model_family",
            "model_version",
            "model_edition",
            "model_snapshot",
            "model_kind",
            "modalities",
            "endpoint_providers",
            "endpoints.api",
        ],
        "provider_endpoints": {
            "openrouter": {
                "models": OPENROUTER_USER_MODELS,
                "chat_completions": OPENROUTER_CHAT,
            },
            "anthropic": {
                "models": ANTHROPIC_MODELS,
                "messages": ANTHROPIC_MESSAGES,
                "count_tokens": ANTHROPIC_COUNT_TOKENS,
                "message_batch": ANTHROPIC_MESSAGE_BATCHES,
            },
            "google_gemini": {
                "provider_kind": "multimodal_model_api",
                "base_url": GEMINI_BASE,
                "models": GEMINI_MODELS,
                "interactions": GEMINI_INTERACTIONS,
                "generate_content": GEMINI_GENERATE_CONTENT,
                "stream_generate_content": GEMINI_STREAM_GENERATE_CONTENT,
                "count_tokens": GEMINI_COUNT_TOKENS,
            },
            "xai": {
                "provider_kind": "multimodal_model_api",
                "base_url": XAI_BASE,
                "models": XAI_MODELS,
                "responses": XAI_RESPONSES,
                "chat_completions": XAI_CHAT,
            },
            "deepseek": {
                "provider_kind": "language_model_api",
                "base_url": DEEPSEEK_BASE,
                "models": DEEPSEEK_MODELS,
                "chat_completions": DEEPSEEK_CHAT,
                "beta_base_url": DEEPSEEK_BETA_BASE,
                "anthropic_compatible_base_url": DEEPSEEK_ANTHROPIC_BASE,
            },
            "higgsfield": {
                "provider_kind": "generative_media_gateway",
                "base_url": HIGGSFIELD_BASE,
                "generation": HIGGSFIELD_BASE + "/{endpoint_path}",
                "request_status": HIGGSFIELD_STATUS,
                "request_cancel": HIGGSFIELD_CANCEL,
                "catalog_discovery": {
                    "kind": "cli",
                    "command": "higgsfield model list",
                },
            },
        },
        "higgsfield_endpoints": [
            {
                "id": "higgsfield/flux-pro/kontext/max/text-to-image",
                "model_name": "FLUX Pro Kontext Max",
                "model_kind": "image_generation",
                "endpoint_url": HIGGSFIELD_BASE + "/flux-pro/kontext/max/text-to-image",
                "status": "documented_sdk_example",
            },
            {
                "id": "higgsfield/v1/image2video/dop",
                "model_name": "Higgsfield DoP",
                "model_kind": "video_generation",
                "endpoint_url": HIGGSFIELD_BASE + "/v1/image2video/dop",
                "status": "documented_sdk_example",
            },
        ],
        "sources": {
            "openrouter": {
                "endpoint": catalog_endpoint,
                "status": "available",
                "model_count": len(catalog.get("data", [])),
            },
            "artificial_analysis": benchmark_snapshot(aa, aa_source, aa_available),
        },
        "proposed_models": proposed,
        "cost_lanes": cost_lanes,
        "eligible_models": candidates,
        "catalog_models": catalog_models,
    }


def write_private_json(path: Path, payload: dict[str, Any]) -> None:
    _atomic_private_text(path, json.dumps(payload, indent=2) + "\n")


def write_model_endpoint(endpoint: dict[str, Any]) -> None:
    write_private_json(MODEL_ENDPOINT_PATH, endpoint)


def acquire_model_refresh_lock(timeout_seconds: float = 10.0) -> tuple[int, Path]:
    lock_path = MODEL_ENDPOINT_PATH.with_suffix(".refresh.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + max(0.1, timeout_seconds)
    while True:
        try:
            descriptor = os.open(
                lock_path,
                os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                0o600,
            )
            os.write(descriptor, str(os.getpid()).encode("ascii"))
            return descriptor, lock_path
        except FileExistsError:
            try:
                age = time.time() - lock_path.stat().st_mtime
                if age > 120:
                    lock_path.unlink()
                    continue
            except FileNotFoundError:
                continue
            if time.monotonic() >= deadline:
                raise RouterError(
                    "Timed out waiting for the model-catalog refresh lock"
                )
            time.sleep(0.05)


def release_model_refresh_lock(descriptor: int, lock_path: Path) -> None:
    try:
        os.close(descriptor)
    finally:
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass


def load_aa_cache(fresh_only: bool = True) -> dict[str, Any] | None:
    try:
        cached = json.loads(AA_CACHE_PATH.read_text(encoding="utf-8"))
        fetched_at = datetime.fromisoformat(cached["fetched_at"])
        payload = cached["payload"]
        if fetched_at.tzinfo is None or not isinstance(payload, dict):
            return None
        if fetched_at > datetime.now(timezone.utc) + MAX_CACHE_CLOCK_SKEW:
            return None
        if fresh_only and (
            datetime.now(timezone.utc) - fetched_at
            > timedelta(hours=AA_CACHE_TTL_HOURS)
        ):
            return None
        return payload
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return None


def fetch_artificial_analysis_models(
    api_key: str,
    *,
    access: str = "auto",
    requester: Any = None,
    max_pages: int = AA_MAX_PAGES,
) -> dict[str, Any]:
    """Fetch one current, paginated Artificial Analysis language-model snapshot.

    ``auto`` attempts the Pro/Commercial endpoint first and falls back to the
    documented Free endpoint only when the credential is valid but lacks the
    required subscription tier. No credential or raw response body is added to
    the returned source receipt.
    """
    if access not in {"auto", "free", "pro"}:
        raise RouterError("Artificial Analysis access must be auto, free, or pro")
    if not isinstance(api_key, str) or not api_key.strip():
        raise RouterError("Artificial Analysis credential is unavailable")
    if max_pages < 1 or max_pages > AA_MAX_PAGES:
        raise RouterError(
            f"Artificial Analysis page ceiling must be between 1 and {AA_MAX_PAGES}"
        )
    request = requester or request_json
    endpoints = (
        (AA_MODELS_FREE,)
        if access == "free"
        else (AA_MODELS,)
        if access == "pro"
        else (AA_MODELS, AA_MODELS_FREE)
    )
    last_forbidden: ProviderRequestError | None = None
    for endpoint_index, endpoint in enumerate(endpoints):
        rows: list[dict[str, Any]] = []
        page = 1
        tier: str | None = None
        index_version: int | float | None = None
        rate_limit: dict[str, str] | None = None
        try:
            while True:
                separator = "&" if "?" in endpoint else "?"
                payload = request(
                    f"{endpoint}{separator}page={page}",
                    headers={"x-api-key": api_key},
                    timeout=10,
                )
                if not isinstance(payload, dict) or not isinstance(
                    payload.get("data"), list
                ):
                    raise RouterError(
                        "Artificial Analysis returned an invalid language-model page"
                    )
                page_rows = payload["data"]
                if not all(isinstance(row, dict) for row in page_rows):
                    raise RouterError(
                        "Artificial Analysis returned an invalid model record"
                    )
                page_tier = payload.get("tier")
                if page_tier is not None and not isinstance(page_tier, str):
                    raise RouterError("Artificial Analysis returned an invalid tier")
                if tier is not None and page_tier is not None and page_tier != tier:
                    raise RouterError(
                        "Artificial Analysis changed subscription tier during pagination"
                    )
                tier = page_tier or tier
                page_version = payload.get("intelligence_index_version")
                if page_version is not None and (
                    isinstance(page_version, bool)
                    or not isinstance(page_version, (int, float))
                ):
                    raise RouterError(
                        "Artificial Analysis returned an invalid index version"
                    )
                if (
                    index_version is not None
                    and page_version is not None
                    and page_version != index_version
                ):
                    raise RouterError(
                        "Artificial Analysis changed index version during pagination"
                    )
                if page_version is not None:
                    index_version = page_version
                transport = payload.get("_empire_transport")
                if isinstance(transport, dict) and isinstance(
                    transport.get("rate_limit"), dict
                ):
                    rate_limit = {
                        str(key): str(value)[:200]
                        for key, value in transport["rate_limit"].items()
                        if isinstance(key, str) and isinstance(value, str)
                    }
                rows.extend(page_rows)
                pagination = payload.get("pagination")
                if pagination is None:
                    has_more = False
                elif not isinstance(pagination, dict):
                    raise RouterError(
                        "Artificial Analysis returned invalid pagination metadata"
                    )
                else:
                    page_has_more = pagination.get("has_more")
                    if not isinstance(page_has_more, bool):
                        raise RouterError(
                            "Artificial Analysis pagination omitted has_more"
                        )
                    has_more = page_has_more
                if not has_more:
                    break
                if page >= max_pages:
                    raise RouterError(
                        "Artificial Analysis pagination exceeded the configured ceiling"
                    )
                page += 1
        except ProviderRequestError as exc:
            if access == "auto" and endpoint_index == 0 and exc.status_code == 403:
                last_forbidden = exc
                continue
            raise
        return {
            "tier": tier or ("free" if endpoint == AA_MODELS_FREE else "unknown"),
            "intelligence_index_version": index_version,
            "pagination": {
                "page": page,
                "page_size": len(rows),
                "total_pages": page,
                "has_more": False,
            },
            "data": rows,
            "_empire_source": {
                "endpoint": endpoint,
                "access_requested": access,
                "fallback_from_pro": last_forbidden is not None,
                "pages_fetched": page,
                "model_count": len(rows),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "rate_limit": rate_limit,
            },
        }
    raise last_forbidden or RouterError("Artificial Analysis is unavailable")


def resolve_aa_evidence(
    *, force_refresh: bool = False, access: str = "auto", allow_stale: bool = True
) -> tuple[dict[str, Any], str, bool]:
    cached = None if force_refresh else load_aa_cache()
    if cached is not None:
        return cached, "local_cache", True
    aa_key, aa_source = resolve_credential(
        ("ARTIFICIAL_ANALYSIS_API_KEY", "AA_API_KEY"), "artificial-analysis"
    )
    if aa_key:
        try:
            payload = fetch_artificial_analysis_models(aa_key, access=access)
            write_private_json(
                AA_CACHE_PATH,
                {
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                    "payload": payload,
                },
            )
            return payload, aa_source, True
        except RouterError as exc:
            stale = load_aa_cache(fresh_only=False) if allow_stale else None
            if stale is not None:
                stale = dict(stale)
                stale["warning"] = f"Using stale benchmark cache: {exc}"
                return stale, "stale_local_cache", True
            return {"data": [], "warning": str(exc)}, aa_source, False
    stale = load_aa_cache(fresh_only=False) if allow_stale else None
    if stale is not None:
        return stale, "stale_local_cache", True
    return (
        {
            "data": [],
            "warning": credential_required_message(
                "Artificial Analysis",
                aa_source,
                "run the Empire settings setup if benchmark enrichment is needed",
            ),
        },
        aa_source,
        False,
    )


def valid_model_endpoint(endpoint: Any) -> bool:
    if not isinstance(endpoint, dict):
        return False
    if endpoint.get("schema_version") != MODEL_ENDPOINT_SCHEMA_VERSION:
        return False
    if endpoint.get("endpoint") != "empire-review://models/proposed":
        return False
    sources = endpoint.get("sources")
    proposed = endpoint.get("proposed_models")
    cost_lanes = endpoint.get("cost_lanes")
    discovery = endpoint.get("discovery")
    eligible = endpoint.get("eligible_models")
    catalog = endpoint.get("catalog_models")
    if (
        not isinstance(sources, dict)
        or not isinstance(proposed, dict)
        or not isinstance(cost_lanes, dict)
        or not isinstance(discovery, dict)
    ):
        return False
    if (
        discovery.get("catalog_authority") != "authenticated_openrouter_user_catalog"
        or discovery.get("cron_required") is not False
        or not isinstance(discovery.get("delta"), dict)
    ):
        return False
    if not isinstance(eligible, list) or not isinstance(catalog, list):
        return False
    if not all(
        isinstance(proposed.get(mode), list) for mode in (*WEIGHTS, "free_fallback")
    ):
        return False
    if not all(
        isinstance(cost_lanes.get(mode), list)
        for mode in ("absolute_zero", "value_paid", "frontier_quality", "adaptive")
    ):
        return False
    catalog_by_id: dict[str, dict[str, Any]] = {}
    required_model_fields = {
        "id",
        "publisher",
        "prompt_price",
        "completion_price",
        "request_price",
        "pricing_components",
        "absolute_zero_text",
        "absolute_zero_basis",
        "free_route_kind",
        "context",
        "modalities",
        "output_modalities",
        "supports_response_format",
        "supports_strict_json",
        "supports_output_limit",
        "supported_parameters",
        "endpoint_providers",
        "endpoints",
    }
    for model in catalog:
        if not isinstance(model, dict) or not required_model_fields.issubset(model):
            return False
        model_id = model.get("id")
        if not isinstance(model_id, str) or not model_id or model_id in catalog_by_id:
            return False
        for field in ("prompt_price", "completion_price"):
            price = model.get(field)
            if not isinstance(price, (int, float)) or isinstance(price, bool):
                return False
            if not math.isfinite(price) or price < 0:
                return False
        context = model.get("context")
        if (
            not isinstance(context, (int, float))
            or isinstance(context, bool)
            or context < 0
        ):
            return False
        if not isinstance(model.get("publisher"), str):
            return False
        request_price = model.get("request_price")
        if request_price is not None and (
            not isinstance(request_price, (int, float))
            or isinstance(request_price, bool)
            or not math.isfinite(request_price)
            or request_price < 0
        ):
            return False
        if not isinstance(model.get("pricing_components"), dict):
            return False
        if not isinstance(model.get("absolute_zero_text"), bool):
            return False
        if model["absolute_zero_text"] and not isinstance(
            model.get("absolute_zero_basis"), str
        ):
            return False
        if "text" not in model.get("output_modalities", []):
            return False
        if model_id.lower().startswith("openai/"):
            return False
        if not all(
            isinstance(model.get(field), list)
            for field in (
                "modalities",
                "output_modalities",
                "supported_parameters",
                "endpoint_providers",
                "endpoints",
            )
        ):
            return False
        if not all(
            isinstance(model.get(field), bool)
            for field in (
                "supports_response_format",
                "supports_strict_json",
                "supports_output_limit",
            )
        ):
            return False
        catalog_by_id[model_id] = model
    eligible_ids: set[str] = set()
    for model in eligible:
        if not isinstance(model, dict):
            return False
        model_id = model.get("id")
        if not isinstance(model_id, str) or model_id in eligible_ids:
            return False
        canonical = catalog_by_id.get(model_id)
        if canonical is None or model != canonical:
            return False
        eligible_ids.add(model_id)
    proposed_ids: set[str] = set()
    for mode in (*WEIGHTS, "free_fallback"):
        for model in proposed[mode]:
            if not isinstance(model, dict) or not isinstance(model.get("id"), str):
                return False
            if model["id"] not in catalog_by_id:
                return False
            proposed_key = f"{mode}:{model['id']}"
            if proposed_key in proposed_ids:
                return False
            proposed_ids.add(proposed_key)
    for lane in ("absolute_zero", "value_paid", "frontier_quality", "adaptive"):
        for model in cost_lanes[lane]:
            if not isinstance(model, dict) or not isinstance(model.get("id"), str):
                return False
            if model["id"] not in catalog_by_id:
                return False
            if lane == "absolute_zero" and not model.get("absolute_zero_text"):
                return False
    try:
        generated = datetime.fromisoformat(endpoint["generated_at"])
        expires = datetime.fromisoformat(endpoint["expires_at"])
    except (KeyError, TypeError, ValueError):
        return False
    if generated.tzinfo is None or expires.tzinfo is None:
        return False
    now = datetime.now(timezone.utc)
    if generated > now + MAX_CACHE_CLOCK_SKEW:
        return False
    if expires <= generated:
        return False
    if expires - generated > timedelta(minutes=MODEL_ENDPOINT_TTL_MINUTES):
        return False
    return True


def refresh_model_endpoint(*, reuse_fresh: bool = False) -> dict[str, Any]:
    openrouter_key, openrouter_source = resolve_credential(
        ("OPENROUTER_API_KEY",), "openrouter"
    )
    if not openrouter_key:
        raise RouterError(
            credential_required_message(
                "OpenRouter", openrouter_source, "run `empire_router.py setup`"
            )
        )
    descriptor, lock_path = acquire_model_refresh_lock()
    try:
        if reuse_fresh:
            existing = load_model_endpoint()
            if existing is not None:
                return existing
        previous_endpoint = load_model_endpoint(fresh_only=False)
        catalog = request_json(OPENROUTER_USER_MODELS, api_key=openrouter_key)
        aa, aa_source, aa_available = resolve_aa_evidence()
        endpoint = build_model_endpoint(
            catalog,
            aa,
            aa_source,
            aa_available,
            catalog_endpoint=OPENROUTER_USER_MODELS,
            previous_endpoint=previous_endpoint,
        )
        write_model_endpoint(endpoint)
        return endpoint
    finally:
        release_model_refresh_lock(descriptor, lock_path)


def load_model_endpoint(fresh_only: bool = True) -> dict[str, Any] | None:
    try:
        endpoint = json.loads(MODEL_ENDPOINT_PATH.read_text(encoding="utf-8"))
        if not valid_model_endpoint(endpoint):
            return None
        expires = datetime.fromisoformat(endpoint["expires_at"])
        if fresh_only and expires <= datetime.now(timezone.utc):
            return None
        return endpoint
    except (OSError, KeyError, ValueError, json.JSONDecodeError):
        return None


def model_endpoint_age(endpoint: dict[str, Any]) -> timedelta:
    generated = datetime.fromisoformat(endpoint["generated_at"])
    return datetime.now(timezone.utc) - generated


def resolve_model_endpoint(
    *, require_benchmarks: bool = False
) -> tuple[dict[str, Any], str]:
    fresh = load_model_endpoint()
    if fresh is not None and (
        not require_benchmarks
        or fresh["sources"]["artificial_analysis"]["status"] == "available"
    ):
        return fresh, "fresh_cached"
    stale = load_model_endpoint(fresh_only=False)
    try:
        refreshed = refresh_model_endpoint(reuse_fresh=True)
        if (
            require_benchmarks
            and refreshed["sources"]["artificial_analysis"]["status"] != "available"
        ):
            raise RouterError("Artificial Analysis benchmark evidence is unavailable")
        return refreshed, "live"
    except RouterError:
        if (
            stale is not None
            and model_endpoint_age(stale)
            <= timedelta(hours=MODEL_ENDPOINT_MAX_STALE_HOURS)
            and (
                not require_benchmarks
                or stale["sources"]["artificial_analysis"]["status"] == "available"
            )
        ):
            return stale, "stale_fallback"
        raise


def model_endpoint_view(
    endpoint: dict[str, Any],
    mode: str | None,
    cost_mode: str | None = None,
    target_language: str | None = None,
    task_profile: str | None = None,
) -> dict[str, Any]:
    lane_names = {
        "free": "absolute_zero",
        "value": "value_paid",
        "frontier": "frontier_quality",
        "auto": "adaptive",
    }
    language = validate_language(target_language)
    models = (
        endpoint["cost_lanes"].get(lane_names[cost_mode], [])
        if cost_mode
        else endpoint["proposed_models"].get(mode, [])
        if mode
        else endpoint["cost_lanes"]
    )
    if language and isinstance(models, list):
        models = [
            {
                **model,
                "language_eligibility": language_eligibility(model, language),
            }
            for model in models
            if language_eligibility(model, language) != "unsupported"
        ]
    task_tokens = {
        "coding": (6000, 3000),
        "review": (8000, 2500),
        "ui": (5000, 4000),
        "security": (10000, 3000),
        "architecture": (12000, 3500),
        "translation": (4000, 4500),
    }
    if task_profile and isinstance(models, list):
        input_tokens, output_tokens = task_tokens[task_profile]
        enriched = []
        for model in models:
            expected = (
                Decimal(input_tokens)
                * Decimal(str(model["input_cost_per_mtok"]))
                / Decimal(1_000_000)
                + Decimal(output_tokens)
                * Decimal(str(model["output_cost_per_mtok"]))
                / Decimal(1_000_000)
                + Decimal(str(model.get("fixed_request_cost_usd") or 0))
            )
            enriched.append(
                {
                    **model,
                    "estimated_task_cost_usd": microusd_to_usd(
                        usd_to_microusd(expected)
                    ),
                    "estimated_task_input_tokens": input_tokens,
                    "estimated_task_output_tokens": output_tokens,
                }
            )
        models = enriched
    if isinstance(models, list):
        health = load_route_health()
        observed_at = datetime.now(timezone.utc)
        models = [
            {
                **model,
                "recent_route_availability": (
                    score := route_availability_from_health(
                        health, str(model.get("id", "")), observed_at
                    )
                ),
                "availability_status": availability_label(score),
            }
            for model in models
        ]
    generated_at = datetime.fromisoformat(endpoint["generated_at"])
    expires_at = datetime.fromisoformat(endpoint["expires_at"])
    now = datetime.now(timezone.utc)
    return {
        "endpoint": endpoint["endpoint"],
        "generated_at": endpoint["generated_at"],
        "expires_at": endpoint["expires_at"],
        "sources": endpoint["sources"],
        "discovery": endpoint["discovery"],
        "catalog_freshness": {
            "status": "fresh" if expires_at > now else "stale",
            "age_seconds": max(0, round((now - generated_at).total_seconds())),
            "refresh_due": expires_at <= now,
        },
        "target_language": language,
        "task_profile": task_profile,
        "language_evidence_warning": (
            "Models without current language evidence remain marked unverified."
            if language
            else None
        ),
        "models": models,
    }


def choose(
    candidates: list[dict[str, Any]], mode: str
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if not candidates:
        raise RouterError("No eligible non-OpenAI text models were found")
    dimensions = {
        "coding": scaled([m["coding"] for m in candidates]),
        "intelligence": scaled([m["intelligence"] for m in candidates]),
        "context": scaled([m["context"] for m in candidates]),
        "price": scaled([m["blended_price"] for m in candidates], reverse=True),
        "speed": scaled([m["speed"] for m in candidates]),
        "capability": [m["capability"] for m in candidates],
        "availability": [float(m.get("availability", 0.5)) for m in candidates],
    }
    weights = WEIGHTS[mode]
    for i, model in enumerate(candidates):
        model["dimension_scores"] = {
            key: round(values[i], 4) for key, values in dimensions.items()
        }
        model["route_score"] = round(
            sum(weights[key] * values[i] for key, values in dimensions.items()), 6
        )
    ranked = sorted(
        candidates,
        key=lambda item: (-item["route_score"], item["blended_price"], item["id"]),
    )
    return ranked[0], ranked


def _table_separator_cells(line: str) -> list[str] | None:
    candidate = line.replace(r"\|", "|").strip().strip("|")
    cells = [cell.strip() for cell in candidate.split("|")]
    if len(cells) < 2 or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
        return None
    return cells


def _looks_like_table_row(line: str, minimum_columns: int) -> bool:
    candidate = line.replace(r"\|", "|").strip()
    if not candidate or candidate.startswith(("```", "~~~")):
        return False
    cells = candidate.strip("|").split("|")
    return len(cells) >= minimum_columns


def _normalize_table_row(line: str, separator: bool = False) -> str:
    candidate = line.replace(r"\|", "|").strip().strip("|")
    cells = [cell.strip() for cell in candidate.split("|")]
    if separator:
        cells = [
            (":" if cell.startswith(":") else "")
            + "---"
            + (":" if cell.endswith(":") else "")
            for cell in cells
        ]
    return "| " + " | ".join(cells) + " |"


def normalize_markdown_tables(text: str) -> str:
    """Repair escaped Markdown table delimiters without touching prose or code."""
    lines = text.splitlines()
    in_fence = False
    fence_marker = ""
    eligible: list[bool] = []
    for line in lines:
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in {"```", "~~~"}:
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            eligible.append(False)
            continue
        eligible.append(not in_fence)

    table_rows: dict[int, bool] = {}
    for index, line in enumerate(lines):
        if not eligible[index]:
            continue
        separator_cells = _table_separator_cells(line)
        if separator_cells is None or index == 0:
            continue
        column_count = len(separator_cells)
        if not eligible[index - 1] or not _looks_like_table_row(
            lines[index - 1], column_count
        ):
            continue
        table_rows[index - 1] = False
        table_rows[index] = True
        cursor = index + 1
        while (
            cursor < len(lines)
            and eligible[cursor]
            and _looks_like_table_row(lines[cursor], column_count)
        ):
            table_rows[cursor] = False
            cursor += 1

    for index, separator in table_rows.items():
        lines[index] = _normalize_table_row(lines[index], separator=separator)
    return "\n".join(lines)


def normalize_partner_markdown(value: Any) -> Any:
    if isinstance(value, str):
        return normalize_markdown_tables(value)
    if isinstance(value, list):
        return [normalize_partner_markdown(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_partner_markdown(item) for key, item in value.items()}
    return value


def _json_with_pipe_escape_repair(text: str) -> Any:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        repaired = re.sub(r"(?<!\\)\\\|", r"\\\\|", text)
        if repaired == text:
            raise
        return json.loads(repaired)


def parse_partner(
    payload: dict[str, Any], *, allow_plaintext_fallback: bool = False
) -> dict[str, Any]:
    try:
        content = payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RouterError(
            "OpenRouter response did not contain assistant content"
        ) from exc
    if isinstance(content, list):
        content = "".join(
            str(item.get("text", "")) for item in content if isinstance(item, dict)
        )
    if isinstance(content, dict):
        result = content
    else:
        text = str(content or "").strip()
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
        text = re.sub(r"\s*```\s*$", "", text)
        try:
            result = _json_with_pipe_escape_repair(text)
        except json.JSONDecodeError:
            start = text.find("{")
            if start < 0:
                if not text:
                    raise RouterError("Partner model returned an empty response")
                if not allow_plaintext_fallback:
                    raise RouterError(
                        "Partner response failed the structured review contract"
                    )
                result = {
                    "summary": text[:6000],
                    "findings": [],
                    "confidence": "unknown",
                    "structured_response": False,
                    "warning": "Partner returned plain text; Codex must verify it",
                }
            else:
                try:
                    candidate = text[start:]
                    try:
                        result, _ = json.JSONDecoder().raw_decode(candidate)
                    except json.JSONDecodeError:
                        repaired = re.sub(r"(?<!\\)\\\|", r"\\\\|", candidate)
                        result, _ = json.JSONDecoder().raw_decode(repaired)
                except json.JSONDecodeError:
                    if not allow_plaintext_fallback:
                        raise RouterError(
                            "Partner response failed the structured review contract"
                        )
                    result = {
                        "summary": text[:6000],
                        "findings": [],
                        "confidence": "unknown",
                        "structured_response": False,
                        "warning": "Partner returned malformed JSON; Codex must verify it",
                    }
    if not isinstance(result, dict):
        raise RouterError("Partner model response must be a JSON object")
    result.setdefault("findings", [])
    result.setdefault("summary", "")
    result.setdefault("confidence", "unknown")
    result.setdefault("structured_response", True)
    result = normalize_partner_markdown(result)
    normalized_findings: list[dict[str, str]] = []
    if result.get("structured_response") is not False:
        if not isinstance(result.get("summary"), str):
            raise RouterError("Partner summary must be a string")
        confidence = result.get("confidence")
        if confidence not in {"low", "medium", "high", "unknown"}:
            raise RouterError(
                "Partner confidence must be low, medium, high, or unknown"
            )
        findings = result.get("findings")
        if not isinstance(findings, list):
            raise RouterError("Partner findings must be a list")
        if len(findings) > MAX_PARTNER_FINDINGS:
            raise RouterError(
                f"Partner response exceeds the {MAX_PARTNER_FINDINGS}-finding limit"
            )
        required = ("severity", "title", "evidence", "recommendation")
        for finding in findings:
            if not isinstance(finding, dict) or not all(
                isinstance(finding.get(field), str) for field in required
            ):
                raise RouterError("Each partner finding must match the review schema")
            if finding["severity"] not in {"critical", "high", "medium", "low"}:
                raise RouterError("Partner finding severity is invalid")
            projected = {field: finding[field].strip() for field in required}
            if any(not projected[field] for field in required):
                raise RouterError("Partner finding fields must not be empty")
            if any(
                len(projected[field]) > MAX_PARTNER_FIELD_CHARS
                for field in ("title", "evidence", "recommendation")
            ):
                raise RouterError("Partner finding field exceeds the safety limit")
            normalized_findings.append(projected)
    summary = str(result.get("summary", "")).strip()
    if len(summary) > MAX_PARTNER_SUMMARY_CHARS:
        raise RouterError("Partner summary exceeds the safety limit")
    normalized = {
        "summary": summary,
        "confidence": result.get("confidence", "unknown"),
        "findings": normalized_findings,
        "structured_response": result.get("structured_response") is not False,
    }
    if normalized["structured_response"] is False:
        normalized["warning"] = str(
            result.get("warning") or "Partner returned unstructured output; Codex must verify it"
        )[:500]
    findings = secret_findings(json.dumps(normalized, ensure_ascii=False))
    if findings:
        raise RouterError(
            "Partner response rejected by secret policy: " + ", ".join(findings)
        )
    return normalized


def benchmark_snapshot(
    payload: dict[str, Any], source: str, available: bool
) -> dict[str, Any]:
    if not available:
        return {"status": "unavailable", "source": None, "credential_source": source}
    snapshot: dict[str, Any] = {}
    allowed = (
        "updated_at",
        "last_updated",
        "as_of",
        "generated_at",
        "snapshot_date",
        "version",
    )
    for key in allowed:
        value = payload.get(key)
        if isinstance(value, (str, int, float, bool)):
            snapshot[key] = value
    meta = payload.get("meta")
    if isinstance(meta, dict):
        for key in allowed:
            value = meta.get(key)
            if isinstance(value, (str, int, float, bool)):
                snapshot[key] = value
    source_receipt = payload.get("_empire_source")
    endpoint = (
        source_receipt.get("endpoint")
        if isinstance(source_receipt, dict)
        else None
    )
    return {
        "status": "available",
        "source": "offline_fixture"
        if source == "offline_fixture"
        else endpoint or AA_MODELS,
        "credential_source": source,
        "model_count": len(payload.get("data", [])),
        "tier": payload.get("tier"),
        "intelligence_index_version": payload.get("intelligence_index_version"),
        "snapshot": snapshot or None,
    }


def budget_status(repo_value: str) -> dict[str, Any]:
    project_id, project_name, _ = budget_project(repo_value)
    with BudgetStore() as store:
        return store.status(project_id, project_name)


def budget_set(repo_value: str, limit_usd: str) -> dict[str, Any]:
    project_id, project_name, _ = budget_project(repo_value)
    limit_microusd = usd_to_microusd(limit_usd)
    with BudgetStore() as store:
        return store.set_limit(project_id, project_name, limit_microusd)


def budget_history(repo_value: str, limit: int = 50) -> dict[str, Any]:
    project_id, project_name, _ = budget_project(repo_value)
    with BudgetStore() as store:
        return store.history(project_id, project_name, limit)


def budget_pending(repo_value: str, limit: int = 50) -> dict[str, Any]:
    project_id, _, _ = budget_project(repo_value)
    with BudgetStore() as store:
        return store.pending(project_id, limit)


def budget_reconcile(
    reservation_id: str, observed_cost_usd: str
) -> dict[str, Any]:
    observed_microusd = usd_to_microusd(observed_cost_usd)
    with BudgetStore() as store:
        store.settle(reservation_id, observed_microusd)
        return {
            "status": "reconciled",
            "reservation": store.reservation(reservation_id),
            "evidence_requirement": "provider billing or usage evidence",
        }


def budget_release_pending(
    reservation_id: str, reason: str, confirmed: bool
) -> dict[str, Any]:
    if not confirmed:
        raise RouterError(
            "Releasing a pending reservation requires --yes and external evidence "
            "that no billable request exists"
        )
    with BudgetStore() as store:
        reservation = store.reconcile_release(reservation_id, reason)
    return {
        "status": "released_after_reconciliation",
        "reservation": reservation,
        "evidence_requirement": "provider confirmed no billable request",
    }


def compensation_list(
    repo_value: str, state: str | None = None, limit: int = 100
) -> dict[str, Any]:
    project_id, _, _ = budget_project(repo_value)
    with BudgetStore() as store:
        return store.compensations(project_id, state=state, limit=limit)


def compensation_report(
    state: str | None = None, limit: int = 500
) -> dict[str, Any]:
    """Return one content-free claim report across all local Empire projects."""
    with BudgetStore() as store:
        report = store.compensations(None, state=state, limit=limit)
    report["scope"] = "all_projects"
    report["contains_provider_content"] = False
    report["next_action"] = (
        "Match each provider_generation_id with provider activity, then record "
        "the submitted case using `compensation update --state pending_claim`."
    )
    return report


def compensation_open(
    repo_value: str,
    reservation_id: str,
    response_id: str | None,
    reason: str,
) -> dict[str, Any]:
    project_id, _, _ = budget_project(repo_value)
    with BudgetStore() as store:
        reservation = store.reservation(reservation_id)
        if reservation["project_id"] != project_id:
            raise RouterError("Reservation does not belong to the selected project")
        record = store.open_compensation(
            reservation_id,
            response_id=response_id,
            reason=reason,
        )
    return {"status": "recorded", "compensation": record}


def compensation_update(
    repo_value: str,
    reservation_id: str,
    state: str,
    evidence_reference: str,
    confirmed: bool,
) -> dict[str, Any]:
    if state in {"credited", "refunded", "denied"} and not confirmed:
        raise RouterError(
            "A terminal compensation state requires --yes and provider evidence"
        )
    project_id, _, _ = budget_project(repo_value)
    with BudgetStore() as store:
        current = store.compensation_record(reservation_id)
        if current["project_id"] != project_id:
            raise RouterError(
                "Compensation record does not belong to the selected project"
            )
        record = store.update_compensation(
            reservation_id,
            state,
            evidence_reference,
        )
    return {"status": "updated", "compensation": record}


def max_authorized_microusd(args: argparse.Namespace) -> int | None:
    value = getattr(args, "max_authorized_cost", None)
    if value is None and hasattr(args, "max_estimated_cost"):
        value = getattr(args, "max_estimated_cost")
    if value is None:
        return None
    return usd_to_microusd(value)


def direct_provider_candidate(
    config: dict[str, Any], endpoint: dict[str, Any] | None
) -> dict[str, Any]:
    name = provider_slug(str(config.get("name", "")))
    model_id = str(config.get("model_id", "")).strip()
    catalog_model_id = str(config.get("catalog_model_id") or model_id).strip()
    input_cost = number(config, "input_cost_per_mtok")
    output_cost = number(config, "output_cost_per_mtok")
    context = number(config, "context_tokens")
    if (
        not model_id
        or input_cost is None
        or output_cost is None
        or not math.isfinite(input_cost)
        or not math.isfinite(output_cost)
        or input_cost < 0
        or output_cost < 0
        or context is None
        or context <= 0
    ):
        raise RouterError("Direct-provider settings are incomplete or invalid")
    matched: dict[str, Any] = {}
    if endpoint:
        for item in endpoint.get("catalog_models", endpoint.get("eligible_models", [])):
            if str(item.get("id", "")).lower() == catalog_model_id.lower():
                matched = dict(item)
                break
    prompt_price = input_cost / 1_000_000
    completion_price = output_cost / 1_000_000
    absolute_zero_text = prompt_price == 0 and completion_price == 0
    canonical_model_id = f"{name}/{model_id}"
    display_name = matched.get("name") or f"{name}: {model_id}"
    direct_endpoint = validate_provider_endpoint(str(config.get("endpoint", "")))
    identity = model_identity(canonical_model_id, display_name)
    return {
        "id": canonical_model_id,
        "api_model_id": model_id,
        "catalog_model_id": catalog_model_id,
        "name": display_name,
        **identity,
        "prompt_price": prompt_price,
        "completion_price": completion_price,
        "request_price": 0.0,
        "pricing_components": {
            "prompt": prompt_price,
            "completion": completion_price,
            "request": 0.0,
        },
        "absolute_zero_text": absolute_zero_text,
        "absolute_zero_basis": "all_text_pricing_components_zero"
        if absolute_zero_text
        else None,
        "free_route_kind": "explicit_model" if absolute_zero_text else None,
        "blended_price": prompt_price + completion_price,
        "context": context,
        "coding": matched.get("coding"),
        "intelligence": matched.get("intelligence"),
        "speed": matched.get("speed"),
        "capability": matched.get("capability", 1.0),
        "supports_json": True,
        "supports_response_format": bool(matched.get("supports_response_format", True)),
        "supports_strict_json": bool(matched.get("supports_strict_json", True)),
        "supports_output_limit": bool(matched.get("supports_output_limit", True)),
        "supported_parameters": matched.get("supported_parameters") or [],
        "benchmark_matched": bool(matched.get("benchmark_matched")),
        "benchmark_model": matched.get("benchmark_model"),
        "modalities": matched.get("modalities") or ["text"],
        "output_modalities": matched.get("output_modalities") or ["text"],
        "supported_languages": matched.get("supported_languages") or [],
        "provider": name,
        "endpoint": direct_endpoint,
        "endpoint_providers": [name],
        "endpoints": [
            {
                "provider": name,
                "api": "chat_completions",
                "url": direct_endpoint,
                "model_id": model_id,
                "preferred": True,
            }
        ],
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    evidence, repo_meta = collect_evidence(
        args.repo,
        args.file,
        args.max_bytes,
        getattr(args, "evidence_mode", "diff"),
    )
    args.task = validate_external_text(
        "Review task", args.task, max_chars=MAX_EXTERNAL_TASK_CHARS
    )
    fixture_dir = Path(args.fixtures).resolve() if args.fixtures else None
    requested_provider = getattr(args, "provider", "auto")
    route_provider = "openrouter"
    direct_key: str | None = None
    direct_source = "missing"
    settings: dict[str, Any] = {}
    endpoint_generated_at: str | None = None
    catalog_status = "offline_fixture" if fixture_dir else "unavailable"
    catalog_refresh_reason = "offline_fixture" if fixture_dir else "unavailable"
    if fixture_dir:
        openrouter_key = None
        openrouter_source = "offline_fixture"
        catalog = fixture(fixture_dir, "openrouter-models.json")
        aa = fixture(fixture_dir, "artificial-analysis-models.json")
        aa_source = "offline_fixture"
        aa_available = True
        endpoint_generated_at = "offline_fixture"
    else:
        openrouter_key, openrouter_source = resolve_credential(
            ("OPENROUTER_API_KEY",), "openrouter"
        )
        settings = load_settings()
        route_provider = (
            settings.get("inference_provider", "openrouter")
            if requested_provider == "auto"
            else requested_provider
        )
        if route_provider not in {"openrouter", "direct"}:
            raise RouterError("Review provider must be auto, openrouter, or direct")
        if route_provider == "openrouter" and not openrouter_key:
            raise RouterError(
                credential_required_message(
                    "OpenRouter",
                    openrouter_source,
                    "run `empire_router.py setup`",
                )
            )
        _, direct_config = configured_direct_provider(settings)
        if route_provider == "direct":
            if not isinstance(direct_config, dict):
                raise RouterError(
                    "No direct provider is configured; run `provider setup`"
                )
            direct_name = provider_slug(str(direct_config.get("name", "")))
            if direct_name == "openai":
                raise RouterError("OpenAI routing is excluded while Codex is the lead")
            direct_key, direct_source = resolve_credential(
                ("EMPIRE_PROVIDER_API_KEY",), provider_account(direct_name)
            )
            if not direct_key:
                raise RouterError(
                    credential_required_message(
                        "Direct-provider",
                        direct_source,
                        "run `provider setup`",
                    )
                )
        explicit_live_catalog = bool(getattr(args, "require_live_catalog", False))
        intent_live_catalog = task_requests_live_catalog(args.task)
        if route_provider == "openrouter" and (
            explicit_live_catalog or intent_live_catalog
        ):
            endpoint = refresh_model_endpoint()
            catalog_status = "live_required"
            catalog_refresh_reason = (
                "explicit_require_live_catalog"
                if explicit_live_catalog
                else "latest_model_intent"
            )
        else:
            endpoint, catalog_status = resolve_model_endpoint(
                require_benchmarks=args.require_benchmarks
            )
            catalog_refresh_reason = (
                "fresh_cache_reused"
                if catalog_status == "fresh_cached"
                else "cache_missing_or_expired"
                if catalog_status == "live"
                else "live_refresh_failed_stale_fallback"
                if catalog_status == "stale_fallback"
                else catalog_status
            )
        benchmark_info = endpoint["sources"]["artificial_analysis"]
        aa_available = benchmark_info["status"] == "available"
        if args.require_benchmarks and not aa_available:
            raise RouterError(
                "Artificial Analysis benchmark evidence is unavailable; run `refresh-models`"
            )
        aa_source = benchmark_info.get("credential_source", "missing")
        aa = {
            "warning": None
            if aa_available
            else "Artificial Analysis benchmark evidence is unavailable"
        }
        if route_provider == "direct":
            if not isinstance(direct_config, dict):
                raise RouterError("Direct-provider configuration disappeared during routing")
            catalog_candidates = [direct_provider_candidate(direct_config, endpoint)]
            if (
                args.require_benchmarks
                and not catalog_candidates[0]["benchmark_matched"]
            ):
                raise RouterError(
                    "The configured direct-provider model has no Artificial Analysis match"
                )
        else:
            endpoint_models = endpoint["eligible_models"]
            catalog_candidates = [dict(model) for model in endpoint_models]
            catalog_candidates = [
                model
                for model in catalog_candidates
                if model.get("supports_response_format")
            ]
        generated_at = endpoint.get("generated_at")
        endpoint_generated_at = generated_at if isinstance(generated_at, str) else None
    if fixture_dir:
        catalog_candidates = normalize_catalog(catalog, aa, allow_openai=False)
    benchmark_receipt = (
        benchmark_snapshot(aa, aa_source, aa_available)
        if fixture_dir
        else benchmark_info
    )
    explicit_cost_mode = getattr(args, "cost_mode", None)
    cost_mode = explicit_cost_mode or settings.get("cost_mode", "auto")
    if cost_mode not in COST_MODES:
        raise RouterError("Configured cost mode is invalid; use mode set auto")
    requested_strength = getattr(args, "selection_strength", None)
    selection_strength = requested_strength or (
        default_selection_strength(cost_mode)
        if explicit_cost_mode
        else settings.get("selection_strength", default_selection_strength(cost_mode))
    )
    if selection_strength not in SELECTION_STRENGTHS:
        raise RouterError("Configured selection strength is invalid; use mode reset")
    target_language = validate_language(
        getattr(args, "language", None) or settings.get("target_language")
    )
    prompt = review_prompt(args.task, target_language, evidence)
    priced_request_text = json.dumps(prompt, separators=(",", ":"), ensure_ascii=False)
    task_risk = infer_task_risk(args.task)
    policy_scope = (
        "request"
        if any(
            value is not None
            for value in (
                explicit_cost_mode,
                requested_strength,
                getattr(args, "language", None),
            )
        )
        else "user_default"
    )
    cost_policy = {
        "cost_mode": COST_LANES[cost_mode],
        "user_mode": cost_mode,
        "scope": policy_scope,
        "selection_strength": selection_strength,
        "maximum_total_cost_usd": 0
        if cost_mode == "free" and selection_strength == "hard_lock"
        else None,
        "cross_tier_fallback": selection_strength != "hard_lock",
        "target_language": target_language,
        "task_risk": task_risk,
        "source": "explicit_user_instruction"
        if policy_scope == "request"
        else "saved_user_default",
    }
    requested_model = getattr(args, "model", None)
    if requested_model:
        if requested_model.lower().startswith("openai/"):
            raise RouterError("OpenAI models are excluded because Codex is the lead")
        requested_candidates = [
            model for model in catalog_candidates if model["id"] == requested_model
        ]
        if (
            not requested_candidates
            and not fixture_dir
            and route_provider == "openrouter"
        ):
            try:
                endpoint = refresh_model_endpoint()
            except RouterError as exc:
                raise RouterError(
                    "Requested model was absent from the cached catalog and the "
                    f"live availability refresh failed: {exc}"
                ) from exc
            benchmark_info = endpoint["sources"]["artificial_analysis"]
            aa_available = benchmark_info["status"] == "available"
            benchmark_receipt = benchmark_info
            endpoint_generated_at = endpoint.get("generated_at")
            catalog_status = "live_exact_model_refresh"
            catalog_refresh_reason = "exact_model_cache_miss"
            requested_candidates = [
                dict(model)
                for model in endpoint["eligible_models"]
                if model.get("supports_response_format")
                and model["id"] == requested_model
            ]
        catalog_candidates = requested_candidates
        if not catalog_candidates:
            raise RouterError(
                f"Requested model is not eligible or available: {requested_model}"
            )
    for candidate in catalog_candidates:
        candidate["availability"] = (
            0.5
            if route_provider == "direct" or fixture_dir
            else route_availability(candidate["id"])
        )
    if not requested_model:
        routes_without_recent_hard_failure = [
            candidate
            for candidate in catalog_candidates
            if candidate["availability"] > 0
        ]
        if routes_without_recent_hard_failure:
            catalog_candidates = routes_without_recent_hard_failure
    authorized_ceiling_microusd = max_authorized_microusd(args)
    language_ineligible: list[str] = []
    language_unverified: list[str] = []
    language_eligible: list[dict[str, Any]] = []
    for candidate in catalog_candidates:
        language_status = language_eligibility(candidate, target_language)
        candidate["language_eligibility"] = language_status
        if language_status == "unsupported":
            language_ineligible.append(candidate["id"])
            continue
        if language_status == "unverified":
            language_unverified.append(candidate["id"])
        language_eligible.append(candidate)
    catalog_candidates = language_eligible
    for candidate in catalog_candidates:
        candidate["projected_max_cost_microusd"] = projected_cost_microusd(
            candidate, priced_request_text, args.max_output_tokens
        )
        candidate["projected_max_cost_usd"] = microusd_to_usd(
            candidate["projected_max_cost_microusd"]
        )
        candidate["expected_cost_usd"] = projected_cost(
            candidate, priced_request_text, max(1, args.max_output_tokens // 4)
        )
    budget_eligible = (
        list(catalog_candidates)
        if authorized_ceiling_microusd is None
        else [
            candidate
            for candidate in catalog_candidates
            if candidate["projected_max_cost_microusd"] <= authorized_ceiling_microusd
        ]
    )
    candidates, resolved_cost_lane = apply_cost_mode(
        budget_eligible, cost_mode, selection_strength, task_risk
    )
    if not candidates:
        if cost_mode == "free":
            contributors = lead_only_contributors()
            response_footnote = response_provenance_footnote(
                contributors,
                selected=None,
                route_provider=None,
            )
            return {
                "status": "codex_only",
                "reason": "no_qualified_absolute_zero_model",
                "selected_model": None,
                "contributors": contributors,
                "contributor_footnote": contributor_footnote(contributors),
                "response_footnote": response_footnote,
                "model_syntheses": [],
                "routing_mode": args.mode,
                "cost_mode": "free",
                "cost_lane": "absolute_zero",
                "cost_policy": cost_policy,
                "paid_fallback_attempted": False,
                "repository_evidence": repo_meta,
                "message": "No qualified Absolute Zero route is available; Codex should continue alone.",
            }
        if authorized_ceiling_microusd is not None:
            raise RouterError(
                f"No eligible {cost_mode} route fits the "
                f"${microusd_to_usd(authorized_ceiling_microusd):.2f} authorized cost ceiling"
            )
        raise RouterError(f"No eligible {cost_mode} route is currently available")
    ranking_mode = "quality" if resolved_cost_lane == "frontier_quality" else args.mode
    selected, ranked = choose(candidates, ranking_mode)
    route_reason = (
        f"User-selected direct provider: {selected['provider']}"
        if route_provider == "direct"
        else f"Highest {ranking_mode} score inside the {resolved_cost_lane} lane"
    )
    if requested_model:
        route_reason = f"User-pinned exact model inside the {resolved_cost_lane} lane"
    credit_fallback = False
    route_fallback = False
    fallback_reason: str | None = None
    context_preflight = context_preflight_receipt(
        args,
        priced_request_text,
        selected,
        route_provider=route_provider,
    )

    if getattr(args, "preview_only", False):
        preview_contributors = contributor_badges(
            selected,
            synthesis_available=False,
            external_status="planned",
        )
        preview_footnote = response_provenance_footnote(
            preview_contributors,
            selected=selected,
            route_provider=route_provider,
            artificial_analysis_used=bool(
                aa_available and selected.get("benchmark_matched")
            ),
            artificial_analysis=benchmark_receipt,
        )
        preview = {
            "status": "route_planned",
            "dispatch_performed": False,
            "selected_model": selected["id"],
            "contributors": preview_contributors,
            "contributor_footnote": contributor_footnote(preview_contributors),
            "response_footnote": preview_footnote,
            "cost_mode": cost_mode,
            "cost_lane": resolved_cost_lane,
            "cost_policy": cost_policy,
            "target_language": target_language,
            "task_risk": task_risk,
            "language_evidence": "unavailable"
            if target_language and selected.get("language_eligibility") == "unverified"
            else selected.get("language_eligibility", "not_requested"),
            "language_routing_mode": language_routing_mode(selected, target_language),
            "route_reason": route_reason,
            "expected_cost_usd": selected["expected_cost_usd"],
            "reserved_maximum_usd": selected["projected_max_cost_usd"],
            "input_price_per_million_usd": round(
                selected["prompt_price"] * 1_000_000, 6
            ),
            "output_price_per_million_usd": round(
                selected["completion_price"] * 1_000_000, 6
            ),
            "task_score": task_quality(selected),
            "language_score": None,
            "authorized_cost_ceiling_usd": microusd_to_usd(authorized_ceiling_microusd),
            "catalog_status": catalog_status,
            "catalog_refresh_reason": catalog_refresh_reason,
            "catalog_discovered_at": endpoint_generated_at,
            "openai_excluded": True,
            "candidate_count": len(ranked),
            "language_ineligible_count": len(language_ineligible),
            "language_unverified_count": len(language_unverified),
            "fallbacks": [],
            "recent_route_availability": selected.get("availability", 0.5),
            "context_preflight": context_preflight,
            "route_health_warning": (
                "The exact pinned route recently failed but was retained because the user requested it."
                if requested_model and selected.get("availability", 0.5) < 0.5
                else None
            ),
            "message": "Route preview only; no external model was called and no budget was reserved.",
        }
        if getattr(args, "explain_route", False):
            preview["selection_explanation"] = {
                "ranking_mode": ranking_mode,
                "selected_score": selected.get("route_score"),
                "selected_dimensions": selected.get("dimension_scores"),
                "provider_policy": openrouter_provider_policy(
                    resolved_cost_lane,
                    require_zdr=getattr(args, "require_zdr", False),
                )
                if route_provider == "openrouter"
                else {"provider": "direct"},
                "alternatives": [
                    {
                        "model": model["id"],
                        "score": model.get("route_score"),
                        "expected_cost_usd": model.get("expected_cost_usd"),
                        "reserved_maximum_usd": model.get("projected_max_cost_usd"),
                    }
                    for model in ranked[1:4]
                ],
            }
        return preview

    project_id, project_name = project_identity(
        repo_meta.get("repository_root") or args.repo
    )
    recovery_root = (
        Path(tempfile.gettempdir()) / "empire-codex-router-fixture-responses"
        if fixture_dir and not os.environ.get("EMPIRE_RESPONSE_DIR")
        else None
    )
    response_capture = prepare_provider_response(
        kind="review",
        root=recovery_root,
    )
    selected_price_snapshot_id = pricing_snapshot_id(selected, endpoint_generated_at)
    with BudgetStore() as budget_store:
        reservation_id, budget_before = budget_store.reserve(
            project_id=project_id,
            project_name=project_name,
            provider=route_provider
            if route_provider == "openrouter"
            else selected["provider"],
            model_id=selected["id"],
            authorized_microusd=selected["projected_max_cost_microusd"],
            price_snapshot_id=selected_price_snapshot_id,
            ttl_seconds=max(300, args.timeout * 2),
        )
    if reservation_id is None:
        denied_receipt = dict(response_capture["receipt"])
        denied_receipt.update(
            {
                "state": "not_dispatched_budget_denied",
                "generation_state": "not_dispatched",
                "billing_state": "released",
                "finalized_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        _atomic_private_json(response_capture["receipt_path"], denied_receipt)
        lead = contributor_badges(selected)[0]
        response_footnote = response_provenance_footnote(
            [lead],
            selected=None,
            route_provider=None,
        )
        return {
            "status": "codex_only",
            "reason": "project_budget_exhausted",
            "selected_model": None,
            "contributors": [lead],
            "contributor_footnote": contributor_footnote([lead]),
            "response_footnote": response_footnote,
            "model_syntheses": [],
            "routing_mode": args.mode,
            "cost_mode": cost_mode,
            "cost_lane": resolved_cost_lane,
            "budget": {
                **budget_before,
                "authorization": "denied",
                "requested_authorization_usd": selected["projected_max_cost_usd"],
                "budget_assurance": "enforced_locally",
            },
            "repository_evidence": repo_meta,
            "context_preflight": context_preflight,
            "message": "External review skipped; Codex should continue alone.",
        }

    dispatch_started = False
    provider_outcome_proven_nonbillable = False
    provider_generation_id: str | None = None
    provider_request_id: str | None = None
    provider_error_status: int | None = None
    provider_error_category: str | None = None
    started = time.monotonic()
    try:
        if fixture_dir:
            completion = fixture(fixture_dir, "openrouter-completion.json")
        else:

            def complete(model: dict[str, Any]) -> dict[str, Any]:
                nonlocal dispatch_started, provider_outcome_proven_nonbillable
                nonlocal provider_generation_id, provider_request_id
                nonlocal provider_error_status, provider_error_category
                endpoint_url = (
                    model["endpoint"] if route_provider == "direct" else OPENROUTER_CHAT
                )
                completion_key = (
                    direct_key if route_provider == "direct" else openrouter_key
                )
                body = completion_request_body(
                    model,
                    prompt,
                    args.max_output_tokens,
                    route_provider=route_provider,
                    reasoning_effort=getattr(args, "reasoning_effort", None)
                    or ("medium" if args.mode == "quality" else "low"),
                )
                if route_provider == "openrouter":
                    body["provider"] = openrouter_provider_policy(
                        resolved_cost_lane,
                        require_zdr=getattr(args, "require_zdr", False),
                    )
                with BudgetStore() as budget_store:
                    budget_store.mark_dispatched(reservation_id)
                mark_response_dispatched(response_capture, reservation_id)
                dispatch_started = True
                try:
                    response = request_json(
                        endpoint_url,
                        api_key=completion_key,
                        headers={"X-OpenRouter-Metadata": "enabled"}
                        if route_provider == "openrouter"
                        else None,
                        body=body,
                        timeout=args.timeout,
                    )
                except ProviderRequestError as exc:
                    provider_generation_id = exc.provider_generation_id
                    provider_request_id = exc.provider_request_id
                    provider_error_status = exc.status_code
                    provider_error_category = provider_failure_category(
                        exc.status_code, exc.provider_message
                    )
                    provider_outcome_proven_nonbillable = outcome_proven_nonbillable(
                        route_provider, exc.status_code
                    )
                    if route_provider == "openrouter":
                        record_route_health(
                            model["id"],
                            success=False,
                            status_code=exc.status_code,
                            category=provider_failure_category(
                                exc.status_code, exc.provider_message
                            ),
                        )
                    raise
                # Return directly into durable capture. No health or billing
                # write may discard successfully received assistant bytes.
                return response

            try:
                completion = complete(selected)
            except RouterError as exc:
                if isinstance(exc, AmbiguousProviderOutcome):
                    raise
                if route_provider == "direct":
                    raise
                selected_is_free = is_absolute_zero_route(selected)
                credit_rejection = "HTTP 402" in str(exc)
                free = [
                    model
                    for model in catalog_candidates
                    if is_absolute_zero_route(model) and model["id"] != selected["id"]
                ]
                fallback_allowed = selected_is_free or cost_mode == "auto"
                if (
                    not free
                    or not (
                        credit_rejection
                        or (selected_is_free and retryable_free_route_error(exc))
                    )
                    or requested_model
                    or not fallback_allowed
                ):
                    raise
                _, ranked = choose(free, args.mode)
                failures: list[str] = []
                for fallback in ranked[:5]:
                    try:
                        completion = complete(fallback)
                        selected = fallback
                        credit_fallback = credit_rejection
                        route_fallback = True
                        fallback_reason = (
                            "credit_rejection"
                            if credit_rejection
                            else "free_endpoint_unavailable"
                        )
                        route_reason = "OpenRouter fallback to an eligible free model"
                        resolved_cost_lane = "absolute_zero"
                        break
                    except RouterError as fallback_error:
                        failures.append(
                            f"{fallback['id']}: {str(fallback_error).split(':', 1)[0]}"
                        )
                else:
                    raise RouterError(
                        "Free fallback routes failed: " + "; ".join(failures)
                    ) from exc
        # Keep correlation identifiers in memory even if the capture write
        # fails; only persistence/health bookkeeping must wait for capture.
        provider_references = provider_reference_data(
            completion, route_provider=route_provider
        )
        provider_generation_id = provider_references["provider_generation_id"]
        provider_request_id = provider_references["provider_request_id"]
        response_capture = capture_provider_response(
            completion,
            kind="review",
            prepared=response_capture,
            route_provider=route_provider,
        )
        if not fixture_dir and route_provider == "openrouter":
            record_route_health(selected["id"], success=True)
        latency_ms = round((time.monotonic() - started) * 1000)
        observed_value, cost_source = observed_usage_cost(
            completion,
            selected,
            route_provider=route_provider,
        )
        selected_price_snapshot_id = pricing_snapshot_id(
            selected, endpoint_generated_at
        )
        billing_pending = observed_value is None
        observed_microusd = observed_value or 0
        with BudgetStore() as budget_store:
            budget_store.record_provider_references(
                reservation_id,
                provider_generation_id=provider_generation_id,
                provider_request_id=provider_request_id,
            )
            if billing_pending:
                budget_store.mark_pending(
                    reservation_id,
                    cost_source,
                    provider_request_id=provider_request_id,
                    provider_generation_id=provider_generation_id,
                )
                budget_after = budget_store.status(project_id, project_name)
            else:
                budget_after = budget_store.settle(
                    reservation_id,
                    observed_microusd,
                    model_id=selected["id"],
                    price_snapshot_id=selected_price_snapshot_id,
                )
        # Assistant bytes are durable before settlement and validation. A
        # malformed or token-limited response therefore remains available for
        # bounded Codex synthesis without starting another provider call.
        validation_error: str | None = None
        partner: dict[str, Any] | None
        try:
            partner = parse_partner(
                completion,
                allow_plaintext_fallback=getattr(
                    args, "allow_plaintext_fallback", False
                ),
            )
        except RouterError as exc:
            validation_error = str(exc)
            captured_text = response_capture["content"].strip()
            safe_to_synthesize = response_capture["receipt"]["safe_to_synthesize"]
            partner = (
                {
                    "summary": captured_text[:MAX_PARTNER_SUMMARY_CHARS],
                    "findings": [],
                    "confidence": "unknown",
                    "structured_response": False,
                    "warning": (
                        "Partner output did not pass the structured contract. "
                        "Codex must review the durable research artifact in bounded chunks."
                    ),
                }
                if captured_text and safe_to_synthesize
                else None
            )
    except AmbiguousProviderOutcome as exc:
        provider_generation_id = (
            exc.provider_generation_id or provider_generation_id
        )
        provider_request_id = exc.provider_request_id or provider_request_id
        with BudgetStore() as budget_store:
            budget_store.mark_pending(
                reservation_id,
                "transport_ended_without_proven_provider_outcome",
                provider_request_id=provider_request_id,
                provider_generation_id=provider_generation_id,
            )
        failed_receipt = dict(response_capture["receipt"])
        failed_receipt.update(
            {
                "state": "failed_ambiguous_provider_outcome",
                "generation_state": "ambiguous",
                "billing_state": "pending_reconciliation",
                "provider_generation_id": provider_generation_id,
                "provider_request_id": provider_request_id,
                "finalized_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        _atomic_private_json(response_capture["receipt_path"], failed_receipt)
        raise RouterError(
            "The provider outcome is ambiguous. The authorized amount remains "
            f"reserved for reconciliation under {reservation_id}. "
            "Run `budget pending` before retrying."
        ) from exc
    except Exception:
        with BudgetStore() as budget_store:
            if dispatch_started and not provider_outcome_proven_nonbillable:
                budget_store.mark_pending(
                    reservation_id,
                    "post_dispatch_processing_or_provider_outcome_ambiguous",
                    provider_request_id=provider_request_id,
                    provider_generation_id=provider_generation_id,
                )
                failed_billing_state = "pending_reconciliation"
            else:
                try:
                    budget_store.record_provider_references(
                        reservation_id,
                        provider_generation_id=provider_generation_id,
                        provider_request_id=provider_request_id,
                    )
                except BudgetError:
                    budget_store.mark_pending(
                        reservation_id,
                        "provider_reference_conflict_requires_reconciliation",
                        provider_request_id=provider_request_id,
                        provider_generation_id=provider_generation_id,
                    )
                    failed_billing_state = "pending_reconciliation"
                else:
                    budget_store.release(reservation_id)
                    failed_billing_state = "released"
        failed_receipt = dict(response_capture["receipt"])
        failed_receipt.update(
            {
                "state": "failed_provider_request"
                if provider_error_status is not None
                else "failed_post_dispatch"
                if dispatch_started
                else "failed_pre_dispatch",
                "generation_state": response_capture["receipt"].get("generation_state", "failed")
                if response_capture.get("content") else "failed",
                "billing_state": failed_billing_state,
                "provider_error_status": provider_error_status,
                "provider_error_category": provider_error_category,
                "provider_generation_id": provider_generation_id,
                "provider_request_id": provider_request_id,
                "finalized_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        _atomic_private_json(response_capture["receipt_path"], failed_receipt)
        raise

    observed_cost_usd = microusd_to_usd(observed_microusd) or 0.0
    billing_state = response_billing_state(
        observed_microusd,
        selected["projected_max_cost_microusd"],
        pending=billing_pending,
    )
    cost_policy_violation = bool(
        cost_mode == "free"
        and selection_strength == "hard_lock"
        and (observed_microusd != 0 or billing_pending)
    )
    generation_state = response_capture["receipt"].get("generation_state")
    sensitive_response = bool(
        response_capture["receipt"].get("sensitive_content_labels")
    )
    schema_valid = bool(
        partner
        and validation_error is None
        and partner.get("structured_response") is not False
    )
    if generation_state == "blocked":
        result_status = "blocked_provider_safety"
    elif sensitive_response:
        result_status = "blocked_sensitive"
    elif not response_capture["content"]:
        result_status = "failed_empty"
    elif generation_state in {"partial", "ambiguous"}:
        result_status = "partial_recoverable"
    elif validation_error or (partner and partner.get("structured_response") is False):
        result_status = "completed_degraded"
    else:
        result_status = "completed"
    research_artifact = finalize_provider_response(
        response_capture,
        state=result_status,
        schema_valid=schema_valid,
        observed_cost_usd=observed_cost_usd,
        billing_state=billing_state,
    )
    synthesis_available = bool(
        partner and (str(partner.get("summary", "")).strip() or partner.get("findings"))
    )
    contributors = contributor_badges(selected, synthesis_available=synthesis_available)
    served_provider = (
        completion.get("provider")
        if isinstance(completion.get("provider"), str)
        else None
    )
    web_sources = completion_web_sources(completion)
    artificial_analysis_used = bool(aa_available and selected.get("benchmark_matched"))
    response_footnote = response_provenance_footnote(
        contributors,
        selected=selected,
        route_provider=route_provider,
        served_provider=served_provider,
        artificial_analysis_used=artificial_analysis_used,
        artificial_analysis=benchmark_receipt,
        web_sources=web_sources,
    )
    return {
        "status": result_status,
        "selected_model": selected["id"],
        "canonical_served_model": completion.get("model")
        if isinstance(completion.get("model"), str)
        else None,
        "contributors": contributors,
        "contributor_footnote": contributor_footnote(contributors),
        "synthesis_footnote": synthesis_model_footnote(contributors),
        "response_footnote": response_footnote,
        "model_syntheses": model_syntheses(
            contributors,
            research_artifact
            if result_status in {"partial_recoverable", "completed_degraded"}
            else None,
        ),
        "research_artifact": research_artifact,
        "continuation": {
            "eligible": result_status == "partial_recoverable",
            "authorization": "ask",
            "automatic_continuation_started": False,
            "instruction": (
                "Synthesize every available chunk before requesting authorization "
                "for a same-model continuation of only the missing work."
            ),
        },
        "web_research": {
            "used": bool(web_sources),
            "sources": web_sources,
            "citation_renderer": "native_codex_preferred",
        },
        "routing_mode": args.mode,
        "cost_mode": cost_mode,
        "cost_lane": resolved_cost_lane,
        "cost_policy": cost_policy,
        "target_language": target_language,
        "language_routing_mode": language_routing_mode(selected, target_language),
        "task_risk": task_risk,
        "route_reason": route_reason,
        "fallbacks": [fallback_reason] if fallback_reason else [],
        "routing_evidence": {
            "inference_provider": route_provider,
            "provider_name": selected.get("provider", "openrouter"),
            "served_provider": served_provider,
            "provider_generation_id": provider_generation_id,
            "provider_request_id": provider_request_id,
            "catalog_source": "openrouter_user_catalog"
            if catalog_status.startswith("live")
            else catalog_status,
            "catalog_status": catalog_status,
            "catalog_refresh_reason": catalog_refresh_reason,
            "catalog_discovered_at": endpoint_generated_at,
            "openrouter_credential_source": openrouter_source,
            "direct_provider_credential_source": direct_source
            if route_provider == "direct"
            else None,
            "benchmark_evidence": "available" if aa_available else "unavailable",
            "benchmark_used_in_selection": artificial_analysis_used,
            "artificial_analysis": benchmark_info
            if not fixture_dir
            else benchmark_snapshot(aa, aa_source, aa_available),
            "benchmark_warning": aa.get("warning"),
            "candidate_count": len(ranked),
            "catalog_candidate_count": len(catalog_candidates),
            "projected_max_cost_usd": selected["projected_max_cost_usd"],
            "projected_maximum_usd": selected["projected_max_cost_usd"],
            "expected_cost_usd": selected["expected_cost_usd"],
            "reserved_maximum_usd": selected["projected_max_cost_usd"],
            "local_authorization_usd": selected["projected_max_cost_usd"],
            "provider_enforced_total_ceiling_usd": None,
            "input_price_per_million_usd": round(
                selected["prompt_price"] * 1_000_000, 6
            ),
            "output_price_per_million_usd": round(
                selected["completion_price"] * 1_000_000, 6
            ),
            "task_score": task_quality(selected),
            "language_score": None,
            "authorized_cost_ceiling_usd": microusd_to_usd(authorized_ceiling_microusd),
            "cost_ceiling_usd": microusd_to_usd(authorized_ceiling_microusd),
            "price_snapshot_id": selected_price_snapshot_id,
            "credit_fallback": credit_fallback,
            "route_fallback": route_fallback,
            "fallback_reason": fallback_reason,
            "score": selected["route_score"],
            "dimensions": selected["dimension_scores"],
            "benchmark_matched": selected["benchmark_matched"],
            "benchmark_model": selected["benchmark_model"],
            "openai_excluded": True,
            "selection_mode": "user_pinned" if requested_model else "automatic",
            "recent_route_availability": selected.get("availability", 0.5),
            "absolute_zero_verified": is_absolute_zero_route(selected),
            "selection_strength": selection_strength,
            "privacy_policy": "zero_data_retention"
            if getattr(args, "require_zdr", False)
            else "no_data_collection",
            "target_language": target_language,
            "language_routing_mode": language_routing_mode(selected, target_language),
            "task_risk": task_risk,
            "language_eligibility": selected.get(
                "language_eligibility", "not_requested"
            ),
            "language_unverified_count": len(language_unverified),
            "cost_policy_violation": cost_policy_violation,
        },
        "budget": {
            **budget_after,
            "reservation_id": reservation_id,
            "provider": selected.get("provider", "openrouter"),
            "authorization": billing_state
            if billing_pending or billing_state == "settled_overrun"
            else "settled",
            "authorized_maximum_usd": selected["projected_max_cost_usd"],
            "local_authorization_usd": selected["projected_max_cost_usd"],
            "provider_enforced_total_ceiling_usd": None,
            "provider_generation_id": provider_generation_id,
            "provider_request_id": provider_request_id,
            "observed_cost_usd": observed_cost_usd,
            "cost_source": cost_source,
            "budget_assurance": "enforced_locally",
            "upstream_overrun_possible": True,
        },
        "latency_ms": latency_ms,
        "observed_cost_usd": observed_cost_usd,
        "estimated_cost_usd": None if billing_pending else observed_cost_usd,
        "context_preflight": context_preflight,
        "repository_evidence": repo_meta,
        "response_validation": {
            "transport_success": True,
            "schema_success": schema_valid,
            "repair_success": False,
            "degraded_plaintext": result_status
            in {"completed_degraded", "partial_recoverable"},
            "validation_failure": not schema_valid,
            "error": validation_error,
            "durable_before_validation": True,
        },
        "review": partner,
    }


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    empire_present.add_view_argument(root)
    sub = root.add_subparsers(dest="command", required=True)

    def configure_route_command(command: argparse.ArgumentParser) -> None:
        command.add_argument("--task", required=True)
        command.add_argument("--repo", default=".")
        command.add_argument("--file", action="append", default=[])
        command.add_argument(
            "--evidence-mode",
            choices=("diff", "files-only"),
            default="diff",
            help="Use the Git diff plus selected files, or isolate evidence to explicit files",
        )
        command.add_argument("--mode", choices=sorted(WEIGHTS), default="balanced")
        command.add_argument(
            "--cost-mode",
            choices=COST_MODES,
            help="Economic lane for this request (default: saved mode, then auto)",
        )
        command.add_argument(
            "--selection-strength",
            choices=SELECTION_STRENGTHS,
            help="Hard-lock the lane, prefer it, or try it first",
        )
        command.add_argument(
            "--language", help="Target language or locale, such as es-PR or ja-JP"
        )
        command.add_argument("--model", help="Pin one exact non-OpenAI model ID")
        command.add_argument(
            "--provider",
            choices=("auto", "openrouter", "direct"),
            default="auto",
            help="Inference provider (default: selected setting, then OpenRouter)",
        )
        command.add_argument(
            "--require-benchmarks",
            action="store_true",
            help="Fail unless Artificial Analysis evidence is available",
        )
        command.add_argument(
            "--require-live-catalog",
            action="store_true",
            help="Refresh the authenticated OpenRouter catalog before routing",
        )
        command.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
        command.add_argument("--timeout", type=int, default=90)
        command.add_argument("--max-output-tokens", type=int, default=8000)
        command.add_argument(
            "--response-class",
            choices=("automatic", "micro", "compact", "standard", "artifact"),
            default="automatic",
            help="Measurement-only recommended external response class",
        )
        command.add_argument(
            "--codex-context-limit-tokens",
            type=int,
            help="Caller-reported active Codex context limit for preflight only",
        )
        command.add_argument(
            "--codex-context-used-tokens",
            type=int,
            help="Caller-reported active Codex context usage for preflight only",
        )
        command.add_argument(
            "--reasoning-effort",
            choices=("low", "medium", "high"),
            help="Override the routing profile's reasoning effort when supported",
        )
        command.add_argument(
            "--max-authorized-cost",
            "--max-estimated-cost",
            dest="max_authorized_cost",
            default=None,
            help="Explicit maximum USD authorization for this external review",
        )
        command.add_argument(
            "--require-zdr",
            action="store_true",
            help="Require a Zero Data Retention endpoint (may make pinned models unavailable)",
        )
        command.add_argument("--fixtures", help=argparse.SUPPRESS)

    review = sub.add_parser("review", help="Route one bounded review")
    configure_route_command(review)
    review.add_argument(
        "--allow-plaintext-fallback",
        action="store_true",
        help="Explicitly allow a completed_degraded plaintext review",
    )
    route = sub.add_parser(
        "route", help="Preview the selected route without dispatch or reservation"
    )
    configure_route_command(route)
    route.set_defaults(preview_only=True, allow_plaintext_fallback=False)
    explain = sub.add_parser(
        "explain", help="Explain a planned route without dispatch or reservation"
    )
    configure_route_command(explain)
    explain.set_defaults(
        preview_only=True, explain_route=True, allow_plaintext_fallback=False
    )
    sub.add_parser("refresh-models", help="Refresh the proposed-model endpoint cache")
    models = sub.add_parser(
        "models", help="Print proposed models from the local endpoint"
    )
    models.add_argument("--mode", choices=[*WEIGHTS.keys(), "free_fallback"])
    models.add_argument("--cost-mode", choices=COST_MODES)
    models.add_argument("--language")
    models.add_argument(
        "--task",
        choices=("coding", "review", "ui", "security", "architecture", "translation"),
    )
    models.add_argument("--refresh", action="store_true")
    mode = sub.add_parser("mode", help="Inspect or set the saved economic lane")
    mode_sub = mode.add_subparsers(dest="mode_command", required=True)
    mode_sub.add_parser("status", help="Show the saved economic lane")
    mode_set = mode_sub.add_parser("set", help="Set the saved economic lane")
    mode_set.add_argument("value", choices=COST_MODES)
    mode_set.add_argument("--selection-strength", choices=SELECTION_STRENGTHS)
    mode_sub.add_parser("reset", help="Restore automatic cost routing")
    language = sub.add_parser("language", help="Inspect or set the target language")
    language_sub = language.add_subparsers(dest="language_command", required=True)
    language_sub.add_parser("status", help="Show the saved target language")
    language_set = language_sub.add_parser("set", help="Set the target language")
    language_set.add_argument("value")
    language_sub.add_parser("reset", help="Remove the saved target language")
    language_sub.add_parser(
        "qualifications", help="Show multilingual qualification evidence status"
    )
    sub.add_parser("setup", help="Securely store credentials in the system keyring")
    sub.add_parser("doctor", help="Report credential presence and source")
    logout = sub.add_parser(
        "logout", help="Delete stored system-keyring credentials after confirmation"
    )
    logout.add_argument("--yes", action="store_true", help=argparse.SUPPRESS)
    provider = sub.add_parser(
        "provider", help="Configure or select an inference provider"
    )
    provider_sub = provider.add_subparsers(dest="provider_command", required=True)
    provider_add = provider_sub.add_parser(
        "add", help="Add a trusted direct provider with direct-only routing"
    )
    provider_add.add_argument("value", help="Registered provider ID or family")
    provider_discover = provider_sub.add_parser(
        "discover", help="Refresh one configured provider's authenticated model catalog"
    )
    provider_discover.add_argument("value", help="Configured provider instance or family")
    provider_sub.add_parser("list", help="List redacted provider instances and routing policy")
    provider_setup = provider_sub.add_parser(
        "setup", help="Securely configure an OpenAI-compatible HTTPS provider"
    )
    provider_setup.add_argument("--name", required=True)
    provider_setup.add_argument("--endpoint", required=True)
    provider_setup.add_argument("--model", required=True)
    provider_setup.add_argument("--catalog-model")
    provider_setup.add_argument("--input-cost-per-mtok", required=True)
    provider_setup.add_argument("--output-cost-per-mtok", required=True)
    provider_setup.add_argument("--context-tokens", type=int, required=True)
    provider_sub.add_parser("status", help="Show redacted direct-provider status")
    provider_select = provider_sub.add_parser(
        "select", help="Select OpenRouter or the configured direct provider"
    )
    provider_select.add_argument("value", choices=("openrouter", "direct"))
    provider_remove = provider_sub.add_parser(
        "remove", help="Delete the direct-provider credential and settings"
    )
    provider_remove.add_argument("--yes", action="store_true", help=argparse.SUPPRESS)
    budget = sub.add_parser(
        "budget", help="Configure or inspect the local project budget"
    )
    budget_sub = budget.add_subparsers(dest="budget_command", required=True)
    budget_status_parser = budget_sub.add_parser(
        "status", help="Show local project budget status"
    )
    budget_status_parser.add_argument("--repo", default=".")
    budget_set_parser = budget_sub.add_parser(
        "set", help="Set the total local project budget"
    )
    budget_set_parser.add_argument("--repo", default=".")
    budget_set_parser.add_argument("--limit-usd", required=True)
    budget_history_parser = budget_sub.add_parser(
        "history", help="Show local settled-cost and budget-limit history"
    )
    budget_history_parser.add_argument("--repo", default=".")
    budget_history_parser.add_argument("--limit", type=int, default=50)
    budget_pending_parser = budget_sub.add_parser(
        "pending", help="Show reservations awaiting provider reconciliation"
    )
    budget_pending_parser.add_argument("--repo", default=".")
    budget_pending_parser.add_argument("--limit", type=int, default=50)
    budget_reconcile_parser = budget_sub.add_parser(
        "reconcile", help="Settle a pending reservation from provider billing evidence"
    )
    budget_reconcile_parser.add_argument("--reservation", required=True)
    budget_reconcile_parser.add_argument("--observed-cost-usd", required=True)
    budget_release_parser = budget_sub.add_parser(
        "release-pending",
        help="Release a pending reservation after the provider proves no billable call",
    )
    budget_release_parser.add_argument("--reservation", required=True)
    budget_release_parser.add_argument("--reason", required=True)
    budget_release_parser.add_argument("--yes", action="store_true")
    compensation = sub.add_parser(
        "compensation", help="Track paid calls that produced no durable delivery"
    )
    compensation_sub = compensation.add_subparsers(
        dest="compensation_command", required=True
    )
    compensation_list_parser = compensation_sub.add_parser(
        "list", help="List compensation records without provider-response content"
    )
    compensation_list_parser.add_argument("--repo", default=".")
    compensation_list_parser.add_argument(
        "--state",
        choices=["needed", "pending_claim", "credited", "refunded", "denied"],
    )
    compensation_list_parser.add_argument("--limit", type=int, default=100)
    compensation_report_parser = compensation_sub.add_parser(
        "report",
        help="Show one content-free compensation report across all local projects",
    )
    compensation_report_parser.add_argument(
        "--state",
        choices=["needed", "pending_claim", "credited", "refunded", "denied"],
    )
    compensation_report_parser.add_argument("--limit", type=int, default=500)
    compensation_open_parser = compensation_sub.add_parser(
        "open", help="Backfill a compensation record for a settled empty delivery"
    )
    compensation_open_parser.add_argument("--repo", default=".")
    compensation_open_parser.add_argument("--reservation", required=True)
    compensation_open_parser.add_argument("--response-id")
    compensation_open_parser.add_argument(
        "--reason", default="settled_without_durable_delivery"
    )
    compensation_update_parser = compensation_sub.add_parser(
        "update", help="Record claim, credit, refund, or denial evidence"
    )
    compensation_update_parser.add_argument("--repo", default=".")
    compensation_update_parser.add_argument("--reservation", required=True)
    compensation_update_parser.add_argument(
        "--state",
        required=True,
        choices=["pending_claim", "credited", "refunded", "denied"],
    )
    compensation_update_parser.add_argument("--evidence-reference", required=True)
    compensation_update_parser.add_argument("--yes", action="store_true")
    responses = sub.add_parser(
        "responses", help="List or read durable provider-response recoveries"
    )
    responses_sub = responses.add_subparsers(dest="responses_command", required=True)
    responses_sub.add_parser("list", help="List response receipts without content")
    responses_read = responses_sub.add_parser(
        "read", help="Read one validated response in bounded chunks"
    )
    responses_read.add_argument("response_id")
    responses_read.add_argument("--offset", type=int, default=0)
    responses_read.add_argument(
        "--max-chars", type=int, default=RECOVERY_CHUNK_CHARS
    )
    responses_repair = responses_sub.add_parser(
        "repair", help="Repair one interrupted local response commit"
    )
    responses_repair.add_argument("response_id")
    responses_audit = responses_sub.add_parser(
        "audit", help="Audit response journals against the project budget ledger"
    )
    responses_audit.add_argument("--repo", default=".")
    return root


def main() -> int:
    args = empire_present.parse_args_with_view(parser())
    try:
        if args.command == "setup":
            result = setup_credentials()
        elif args.command == "doctor":
            result = doctor()
        elif args.command == "logout":
            result = logout_credentials(args.yes)
        elif args.command == "provider":
            if args.provider_command == "add":
                result = add_registered_provider(args.value)
            elif args.provider_command == "discover":
                result = discover_registered_provider(args.value)
            elif args.provider_command == "list":
                result = list_provider_instances()
            elif args.provider_command == "setup":
                result = setup_direct_provider(
                    args.name,
                    args.endpoint,
                    args.model,
                    args.catalog_model,
                    args.input_cost_per_mtok,
                    args.output_cost_per_mtok,
                    args.context_tokens,
                )
            elif args.provider_command == "status":
                result = direct_provider_status()
            elif args.provider_command == "select":
                result = select_inference_provider(args.value)
            else:
                result = remove_direct_provider(args.yes)
        elif args.command == "refresh-models":
            result = model_endpoint_view(refresh_model_endpoint(), None)
            result["catalog_status"] = "live"
        elif args.command == "models":
            if args.refresh:
                endpoint, catalog_status = refresh_model_endpoint(), "live"
            else:
                endpoint, catalog_status = resolve_model_endpoint()
            result = model_endpoint_view(
                endpoint, args.mode, args.cost_mode, args.language, args.task
            )
            result["catalog_status"] = catalog_status
        elif args.command == "mode":
            if args.mode_command == "set":
                result = set_cost_mode(args.value, args.selection_strength)
            elif args.mode_command == "reset":
                result = reset_cost_mode()
            else:
                result = cost_mode_status()
        elif args.command == "language":
            if args.language_command == "set":
                result = set_language(args.value)
            elif args.language_command == "reset":
                result = reset_language()
            elif args.language_command == "qualifications":
                result = language_qualification_status()
            else:
                result = language_status()
        elif args.command == "budget":
            if args.budget_command == "set":
                result = budget_set(args.repo, args.limit_usd)
            elif args.budget_command == "history":
                result = budget_history(args.repo, args.limit)
            elif args.budget_command == "pending":
                result = budget_pending(args.repo, args.limit)
            elif args.budget_command == "reconcile":
                result = budget_reconcile(
                    args.reservation, args.observed_cost_usd
                )
            elif args.budget_command == "release-pending":
                result = budget_release_pending(
                    args.reservation, args.reason, args.yes
                )
            else:
                result = budget_status(args.repo)
        elif args.command == "compensation":
            if args.compensation_command == "report":
                result = compensation_report(args.state, args.limit)
            elif args.compensation_command == "open":
                result = compensation_open(
                    args.repo,
                    args.reservation,
                    args.response_id,
                    args.reason,
                )
            elif args.compensation_command == "update":
                result = compensation_update(
                    args.repo,
                    args.reservation,
                    args.state,
                    args.evidence_reference,
                    args.yes,
                )
            else:
                result = compensation_list(args.repo, args.state, args.limit)
        elif args.command == "responses":
            if args.responses_command == "read":
                result = read_response_recovery(
                    args.response_id,
                    offset=args.offset,
                    max_chars=args.max_chars,
                )
            elif args.responses_command == "repair":
                result = repair_response_recovery(args.response_id)
            elif args.responses_command == "audit":
                result = audit_response_recoveries(args.repo)
            else:
                result = list_response_recoveries()
        else:
            result = run(args)
        print(
            empire_present.format_output(
                result,
                view=args.view,
                title=empire_present.command_title(args),
            ),
            end="",
        )
        return 0
    except (BudgetError, RouterError, OSError, subprocess.TimeoutExpired) as exc:
        print(
            empire_present.format_output(
                {"status": "error", "error": str(exc)},
                view=args.view,
                title=empire_present.command_title(args),
            ),
            end="",
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
