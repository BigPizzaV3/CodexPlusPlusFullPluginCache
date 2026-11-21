"""Validate the packaged remote contract and model its surface decision.

Pure policy helpers for package/acceptance checks; no executor, HTTP client or agent runtime.
Cloud agents follow the equivalent execution-surface and mcp-workflow playbooks directly.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit

CREATE_OPERATIONS = {
    "image": {"account", "capabilities", "create_image", "generation_status"},
    "video": {"account", "capabilities", "create_video", "generation_status"},
    "voice": {"account", "audio_catalog", "create_voice", "audio_status"},
    "music": {"account", "audio_catalog", "create_music", "audio_status"},
    "template": {"account", "template", "create_template_media", "generation_status"},
    "compose.render": {"account", "edit_video", "edit_status", "render_edit"},
}
VIDEO_OPERATIONS = {
    "video",
    "first_frame_video",
    "multi_reference_video",
    "reference",
    "transition",
    "extend",
    "modify",
    "edit",
    "upscale",
    "motion-control",
    "last_frame_video",
}
IMAGE_OPERATIONS = {"image", "image_reference"}
SUPPORTED_OPERATIONS = (
    IMAGE_OPERATIONS | VIDEO_OPERATIONS | {"voice", "music", "template", "compose.render"}
)


def choose_surface(
    *,
    cli_state: str,
    skill: str,
    available_tools: Iterable[str],
    catalog: dict,
    operation: str = "image",
    planning_only: bool = False,
    in_flight: str | None = None,
    import_kind: str | None = None,
) -> dict[str, str]:
    """Model the documented gate using evidence supplied by the host, never guessed."""
    if cli_state not in {"usable", "recoverable", "unavailable", "unknown"}:
        raise ValueError("invalid CLI evidence state")
    if in_flight is not None:
        if in_flight not in {"cli", "mcp"}:
            raise ValueError("invalid in-flight transport")
        return {"surface": in_flight, "action": "recover", "reason": "preserve_submission"}
    policy = next((s["mcp"] for s in catalog["skills"] if s["name"] == skill), None)
    if planning_only or (policy and policy["operation"] == "chat"):
        return {"surface": "chat", "action": "plan", "reason": "no_media_required"}
    if cli_state in {"usable", "recoverable"}:
        return {
            "surface": "cli",
            "action": "execute" if cli_state == "usable" else "repair",
            "reason": "cli_first",
        }
    if cli_state == "unknown":
        return {"surface": "undetermined", "action": "check", "reason": "need_structural_evidence"}
    if policy is None:
        return {"surface": "mcp", "action": "stop", "reason": "unsupported_skill"}
    if (
        operation in {"workspace.list", "workspace.current", "workspace.switch"}
        and policy["operation"] in catalog["workspace_scope"]["operations"]
    ):
        required = {"workspace", "account"} if operation == "workspace.switch" else {"workspace"}
        if not required.issubset(available_tools):
            return {"surface": "mcp", "action": "connect", "reason": "missing_callable_tools"}
        return {"surface": "mcp", "action": "execute", "reason": "supported_workspace_operation"}
    if policy["operation"] == "discover":
        return {"surface": "chat", "action": "discover", "reason": "supported_cloud_catalog"}
    if operation not in SUPPORTED_OPERATIONS:
        return {"surface": "mcp", "action": "stop", "reason": "unsupported_operation"}
    # These are local queue operation aliases, not a remote MCP parameter catalog.
    kind = (
        "video"
        if operation in VIDEO_OPERATIONS
        else "image"
        if operation in IMAGE_OPERATIONS
        else operation
    )
    if kind != policy["operation"]:
        return {"surface": "mcp", "action": "stop", "reason": "unsupported_skill_operation"}
    required = set(CREATE_OPERATIONS[kind])
    if import_kind is not None:
        if import_kind not in {"attachment", "url"}:
            raise ValueError("invalid reference import kind")
        required |= {
            "import_status",
            "import_asset" if import_kind == "attachment" else "import_url",
        }
    if not required.issubset(set(available_tools)):
        return {"surface": "mcp", "action": "connect", "reason": "missing_callable_tools"}
    return {"surface": "mcp", "action": "execute", "reason": "supported_cloud_outcome"}


def membership_gate(member_type: object, *, fallback_consented: bool = False) -> str:
    """Mirror backend numeric levels; never reuse the CLI's label-only heuristics."""
    if (
        isinstance(member_type, bool)
        or not isinstance(member_type, int)
        or member_type not in range(12)
    ):
        return "unknown"
    if member_type == 0:
        return "fallback" if fallback_consented else "upgrade_or_consent"
    return "server_entitlement_required"


def validate_mcp_contract(root: Path) -> list[str]:
    if (root / "packages/skills/catalog.json").is_file():
        import runpy
        import tempfile

        helper = runpy.run_path(str(root / "scripts/internal/skill_catalog.py"))
        files = helper["workflow_files"](root, "codex")
        with tempfile.TemporaryDirectory(prefix="pixverse-mcp-contract-") as temporary:
            stage = Path(temporary)
            for name in (".mcp.json", ".codex-plugin/plugin.json"):
                files[name] = (root / name).read_bytes()
            for name, content in files.items():
                path = stage / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            return validate_mcp_contract(stage)

    issues: list[str] = []
    try:
        config = json.loads((root / ".mcp.json").read_text())
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
        if manifest.get("mcpServers") != "./.mcp.json":
            issues.append("manifest must reference the single remote config")
        if set(config) != {"mcpServers"} or set(config["mcpServers"]) != {"pixverse"}:
            issues.append("exactly one PixVerse server is required")
        server = config["mcpServers"]["pixverse"]
        if set(server) != {"type", "url"} or server["type"] != "http":
            issues.append("remote config may contain only HTTP type and URL, never credentials")
        url = urlsplit(server["url"])
        if (
            url.scheme != "https"
            or not url.hostname
            or url.path != "/mcp"
            or url.username
            or url.password
            or url.query
            or url.fragment
        ):
            issues.append(
                "endpoint must be an absolute HTTPS /mcp URL without credentials or API prefix"
            )
        if server["url"] != "https://mcp.pixverse.ai/mcp":
            issues.append("release connection must use the production PixVerse endpoint")
        if (root / "skills-shared/mcp-capabilities.json").exists():
            issues.append("obsolete packaged MCP capability snapshot")
        entries = list((root / "skills").glob("*/SKILL.md"))
        if not entries:
            issues.append("missing installed Skills")
        for path in entries:
            body = path.read_text()
            skill = path.parent.name
            gate = body.find("## Execution Surface")
            if gate < 0 or gate > body.find("\n# ") + 160:
                issues.append(f"{skill}: execution gate must precede workflow instructions")
            if "../../skills-shared/execution-surface.md" not in body:
                issues.append(f"{skill}: missing execution surface contract")
            blocked = (
                "**Desktop required: do not activate this production skill in MCP mode.**" in body
            )
            supported = "### MCP Scope\n" in body
            if supported == blocked:
                issues.append(f"{skill}: expected exactly one MCP scope classification")
            if supported and "../../skills-shared/mcp-workflow.md" not in body:
                issues.append(f"{skill}: missing common MCP workflow")
    except (OSError, KeyError, TypeError, ValueError, AttributeError) as exc:
        issues.append(f"invalid MCP contract: {exc}")
    return issues
