#!/usr/bin/env python3
"""Load the immutable identity contract for one packaged Meetings runtime."""

from __future__ import annotations

import json
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import TypeGuard

from helpers import (
    DuplicateJSONKeyError,
    is_json,
    is_json_array,
    unique_json_object,
)

_CONFIG_PATH = Path(__file__).with_name("runtime-config.json")
_MAXIMUM_CONFIG_BYTES = 16 * 1024
_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._() -]{0,127}\Z")
_BUNDLE_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9.-]{0,127}\Z")
_TEAM_IDENTIFIER = re.compile(r"[A-Z0-9]{10}\Z")
_TOOL_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
MEETINGS_DISTRIBUTION_MARKETPLACES = {
    "internal": "openai-internal-testing",
    "external": "openai-curated-remote",
}
TRUSTED_MEETINGS_PLUGIN_PUBLISHERS = frozenset(MEETINGS_DISTRIBUTION_MARKETPLACES.values())
LOCAL_DEVELOPMENT_MARKETPLACE = "chatgpt-meetings"
LOCAL_DEVELOPMENT_PLUGIN = "chatgpt-meetings-dev"
_REQUIRED_KEYS = {
    "schemaVersion",
    "flavor",
    "distribution",
    "pluginName",
    "marketplaceName",
    "developmentUpdatePolicy",
    "serverName",
    "defaultMcpProfile",
    "appName",
    "bundleIdentifier",
    "appSupportDirectory",
    "controlTarget",
    "teamIdentifier",
    "toolNames",
    "frameworkSymlinks",
    "officialCachePublishers",
}


class RuntimeConfigError(RuntimeError):
    """Raised when the packaged immutable runtime identity is malformed."""


def _safe_relative_path(value: object) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise RuntimeConfigError("Meetings runtime config path is malformed")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise RuntimeConfigError("Meetings runtime config path is malformed")
    return value


@dataclass(frozen=True)
class RuntimeConfig:
    flavor: str
    distribution: str
    plugin_name: str
    marketplace_name: str
    development_update_policy: str
    server_name: str
    default_mcp_profile: str
    app_name: str
    bundle_identifier: str
    app_support_directory: str
    control_target: str
    team_identifier: str
    tool_names: tuple[str, ...]
    framework_symlinks: tuple[tuple[str, str], ...]
    official_cache_publishers: tuple[str, ...]


def _is_string_list(value: object) -> TypeGuard[list[str]]:
    return is_json_array(value) and all(isinstance(item, str) for item in value)


def load_runtime_config(config_path: Path) -> RuntimeConfig:
    """Read a packaged identity without changing this process's runtime configuration."""

    try:
        metadata = config_path.lstat()
    except OSError as exc:
        raise RuntimeConfigError("Meetings runtime config is unavailable") from exc
    if (
        config_path.is_symlink()
        or not stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > _MAXIMUM_CONFIG_BYTES
        or (hasattr(os, "getuid") and metadata.st_uid != os.getuid())
        or (os.name != "nt" and metadata.st_mode & 0o022)
    ):
        raise RuntimeConfigError("Meetings runtime config is unsafe")
    try:
        value: object = json.loads(
            config_path.read_bytes().decode("utf-8"),
            object_pairs_hook=unique_json_object,
            parse_constant=int,
        )
    except DuplicateJSONKeyError as exc:
        raise RuntimeConfigError("Meetings runtime config has duplicate keys") from exc
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as exc:
        raise RuntimeConfigError("Meetings runtime config is malformed") from exc
    if not is_json(value) or not _REQUIRED_KEYS.issubset(value):
        raise RuntimeConfigError("Meetings runtime config schema does not match")

    component_fields = (
        "flavor",
        "serverName",
        "defaultMcpProfile",
        "appName",
        "appSupportDirectory",
        "controlTarget",
    )
    components: dict[str, str] = {}
    for field in component_fields:
        component = value.get(field)
        if not isinstance(component, str) or _COMPONENT.fullmatch(component) is None:
            raise RuntimeConfigError("Meetings runtime config identity is malformed")
        components[field] = component
    bundle_identifier = value.get("bundleIdentifier")
    team_identifier = value.get("teamIdentifier")
    if (
        type(value.get("schemaVersion")) is not int
        or value.get("schemaVersion") != 1
        or not isinstance(bundle_identifier, str)
        or not isinstance(team_identifier, str)
        or _BUNDLE_IDENTIFIER.fullmatch(bundle_identifier) is None
        or _TEAM_IDENTIFIER.fullmatch(team_identifier) is None
        or not components["appName"].endswith(".app")
    ):
        raise RuntimeConfigError("Meetings runtime config identity is malformed")

    distribution = value.get("distribution")
    plugin_name = value.get("pluginName")
    marketplace_name = value.get("marketplaceName")
    development_update_policy = value.get("developmentUpdatePolicy")
    if (
        not isinstance(distribution, str)
        or distribution not in MEETINGS_DISTRIBUTION_MARKETPLACES
        or not isinstance(plugin_name, str)
        or plugin_name != "chatgpt-meetings"
        or not isinstance(marketplace_name, str)
        or marketplace_name != MEETINGS_DISTRIBUTION_MARKETPLACES[distribution]
        or components["flavor"] not in {"production", "development"}
        or not isinstance(development_update_policy, str)
        or development_update_policy not in {"disabled", "local-to-internal"}
        or (
            development_update_policy == "local-to-internal"
            and (components["flavor"] != "development" or distribution != "internal")
        )
        or (components["flavor"] == "development" and distribution != "internal")
    ):
        raise RuntimeConfigError("Meetings runtime distribution identity is malformed")
    tools = value.get("toolNames")
    if (
        not _is_string_list(tools)
        or not 1 <= len(tools) <= 32
        or len(set(tools)) != len(tools)
        or any(_TOOL_NAME.fullmatch(item) is None for item in tools)
    ):
        raise RuntimeConfigError("Meetings runtime tool contract is malformed")

    links = value.get("frameworkSymlinks")
    normalized_links: list[tuple[str, str]] = []
    if not is_json_array(links):
        raise RuntimeConfigError("Meetings framework symlink contract is malformed")
    if len(links) > 16:
        raise RuntimeConfigError("Meetings framework symlink contract is malformed")
    for item in links:
        if not is_json(item) or set(item) != {"path", "target"}:
            raise RuntimeConfigError("Meetings framework symlink contract is malformed")
        path = _safe_relative_path(item["path"])
        target = _safe_relative_path(item["target"])
        if not path.startswith("Contents/Frameworks/Sentry.framework/"):
            raise RuntimeConfigError("Meetings framework symlink path is not allowlisted")
        normalized_links.append((path, target))
    if len({path for path, _ in normalized_links}) != len(normalized_links):
        raise RuntimeConfigError("Meetings framework symlink contract is malformed")

    publishers = value.get("officialCachePublishers")
    if (
        not _is_string_list(publishers)
        or len(set(publishers)) != len(publishers)
        or set(publishers)
        != (TRUSTED_MEETINGS_PLUGIN_PUBLISHERS if components["flavor"] == "production" else set())
    ):
        raise RuntimeConfigError("Meetings official cache contract is malformed")

    return RuntimeConfig(
        flavor=components["flavor"],
        distribution=distribution,
        plugin_name=plugin_name,
        marketplace_name=marketplace_name,
        development_update_policy=development_update_policy,
        server_name=components["serverName"],
        default_mcp_profile=components["defaultMcpProfile"],
        app_name=components["appName"],
        bundle_identifier=bundle_identifier,
        app_support_directory=components["appSupportDirectory"],
        control_target=components["controlTarget"],
        team_identifier=team_identifier,
        tool_names=tuple(tools),
        framework_symlinks=tuple(normalized_links),
        official_cache_publishers=tuple(publishers),
    )


def _load() -> RuntimeConfig:
    return load_runtime_config(_CONFIG_PATH)


RUNTIME_CONFIG = _load()
