#!/usr/bin/env python3
"""Validate the canvas-agent-workflows skill bundle contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
OPERATE_ROOT = SKILL_ROOT.parent / "operate-topview-canvas"
REPO_DOCS = SKILL_ROOT.parents[3] / "docs"

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "evals/evals.json",
    "references/workflow-routing.md",
    "references/orchestration-runtime.md",
    "references/duration-and-task-assembly.md",
    "references/reference-resolution.md",
    "references/generation-stage-machine.md",
    "references/recipes/asset-product.md",
    "references/recipes/scene-surrogate.md",
    "references/recipes/image-video-generation.md",
    "references/recipes/audio-continuity.md",
    "references/recipes/ffmpeg-media.md",
    "references/recipes/timeline.md",
    "references/workflows/direct-generation.md",
    "references/workflows/ecommerce-product-video.md",
    "references/workflows/short-film.md",
    "references/workflows/social-media-video.md",
    "references/workflows/video-element-editing.md",
    "references/workflows/video-replication.md",
    "references/workflows/web-research.md",
]

RICH_WORKFLOWS = [
    "references/workflows/video-replication.md",
    "references/workflows/video-element-editing.md",
    "references/workflows/ecommerce-product-video.md",
    "references/workflows/short-film.md",
    "references/workflows/social-media-video.md",
]

GENERATION_WORKFLOWS = RICH_WORKFLOWS + [
    "references/workflows/direct-generation.md",
]

# Hard ban: any hit in skill content files fails (no "never use X" exemption).
HARD_BANNED_PATTERNS = [
    (re.compile(r"(?i)goal\s*mode"), "goal mode wording"),
    (re.compile(r"(?i)step\s*mode"), "step mode wording"),
    (re.compile(r"await_generation_tasks"), "await_generation_tasks"),
    (re.compile(r"plan_output_kinds"), "plan_output_kinds"),
    (re.compile(r"skill_view"), "skill_view"),
    (re.compile(r"canvas_project_memory"), "canvas_project_memory"),
    (re.compile(r"tool_continue"), "tool_continue"),
    (re.compile(r"\b(SceneCard|VideoCard|ImageCard|StyleCard)s?\b"), "Web card type noun"),
    (re.compile(r"import_web_media"), "import_web_media"),
]

# Legacy Canvas submit/config names may appear only inside explicit bans.
LEGACY_PATTERNS_ALLOW_NEGATION = [
    (re.compile(r"topview_get_generation_config"), "legacy topview_get_generation_config"),
    (re.compile(r"\btoolType\b"), "legacy toolType submit shape"),
    (re.compile(r"\bsourceNodeIds\b"), "legacy sourceNodeIds submit shape"),
    # topview_generate_voice is deliberately absent: Canvas exposes no TTS
    # capability, so cross-shot narration must route to the standalone tool.
    (re.compile(r"topview_generate_(image|video|audio|music)\b"), "generic topview_generate_*"),
]

CONTINUE_POSITIVE = re.compile(
    r"(reply|respond|ask(?:\s+the)?\s+user(?:\s+to)?|wait\s+for\s+(?:the\s+)?user)"
    r".{0,40}\b(OK|continue|继续)\b"
    r"|"
    r"\b(?:please|must|should)\s+(?:reply|respond).{0,20}\b(OK|continue|继续)\b"
    r"|"
    r"\buser\s+(?:must|should)\s+(?:reply|say)\s+(?:OK|continue|继续)\b",
    re.IGNORECASE,
)

THREE_SCENE_DEFAULT = re.compile(
    r"(default|always|must).{0,40}(three|3)\s+(scenes?|scene\s*cards?|video\s*tasks?)",
    re.IGNORECASE,
)

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)

USER_PATH_MARKERS = (
    b"/" + b"Users" + b"/",
    b"/" + b"home" + b"/",
)

NEGATION_MARKERS = (
    "never",
    "do not",
    "don't",
    "forbidden",
    "must not",
    "not use",
    "not call",
    "ban",
    "without asking",
    "no user",
    "not ask",
    "reject",
    "replace",
    "instead of",
)


class ValidationError(Exception):
    pass


def read(rel: str) -> str:
    path = SKILL_ROOT / rel
    if not path.is_file():
        raise ValidationError(f"Missing required file: {rel}")
    return path.read_text(encoding="utf-8")


def iter_skill_content() -> list[tuple[str, str]]:
    """Markdown, YAML, and JSON under the skill (not validator scripts)."""
    items: list[tuple[str, str]] = []
    for path in sorted(SKILL_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".yaml", ".yml", ".json"}:
            continue
        rel = str(path.relative_to(SKILL_ROOT))
        items.append((rel, path.read_text(encoding="utf-8")))
    return items


REMOVED_STUBS = (
    "references/model-capability-planning.md",
    "references/local-media-bridge.md",
)


def validate_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (SKILL_ROOT / rel).is_file():
            raise ValidationError(f"Missing required file: {rel}")
    if (SKILL_ROOT / "references/goal-runtime.md").exists():
        raise ValidationError("references/goal-runtime.md must be removed; use orchestration-runtime.md")
    for rel in REMOVED_STUBS:
        if (SKILL_ROOT / rel).exists():
            raise ValidationError(
                f"{rel} must be removed; use $operate-topview-canvas canonical references"
            )


def validate_skill_frontmatter() -> None:
    text = read("SKILL.md")
    if not text.startswith("---\n"):
        raise ValidationError("SKILL.md must start with YAML frontmatter")
    if "name: canvas-agent-workflows" not in text.split("---", 2)[1]:
        raise ValidationError("SKILL.md name must be canvas-agent-workflows")
    if "[TODO:" in text:
        raise ValidationError("SKILL.md still contains TODO markers")
    for needle in (
        "references/workflow-routing.md",
        "references/generation-stage-machine.md",
        "references/orchestration-runtime.md",
        "references/duration-and-task-assembly.md",
        "references/reference-resolution.md",
        "generation-planning.md",
        "local-media-bridge.md",
        "$operate-topview-canvas",
        "Plan Ledger",
    ):
        if needle not in text:
            raise ValidationError(f"SKILL.md must mention {needle}")
    if "Mandatory before planning" not in text:
        raise ValidationError("SKILL.md must keep a reduced mandatory progressive-read section")
    if "Conditional" not in text:
        raise ValidationError("SKILL.md must mark generation-planning / reference / local-bridge as conditional")
    for needle in (
        "Canvas-first creative gate",
        "whiteboard",
        "world_3d",
        "director_stage",
        "open_topview_canvas",
    ):
        if needle not in text:
            raise ValidationError(f"SKILL.md must keep Canvas-first creative guidance: {needle}")

    evals = json.loads(read("evals/evals.json"))
    case_ids = {case.get("id") for case in evals.get("cases", [])}
    for case_id in (
        "Canvas-first-image-default",
        "Canvas-first-video-default",
        "Canvas-first-interactive-surfaces",
    ):
        if case_id not in case_ids:
            raise ValidationError(f"evals must keep Canvas-first regression case: {case_id}")


def _read_operate(rel: str) -> str:
    path = OPERATE_ROOT / rel
    if not path.is_file():
        raise ValidationError(f"Missing operate canonical file: {path}")
    return path.read_text(encoding="utf-8")


def validate_capability_first() -> None:
    skill = read("SKILL.md")
    if "generation-planning.md" not in skill or "$operate-topview-canvas" not in skill:
        raise ValidationError(
            "SKILL.md must direct agents to $operate-topview-canvas generation-planning.md"
        )
    planning = _read_operate("references/generation-planning.md")
    if "get_topview_canvas_generation_capabilities" not in planning:
        raise ValidationError("operate generation-planning must call get_topview_canvas_generation_capabilities")
    if "before" not in planning.lower() and "Only then" not in planning:
        raise ValidationError("operate generation-planning must require lookup before task counts")
    if "three Scenes" not in planning and "three video tasks" not in planning:
        raise ValidationError("operate generation-planning must forbid default three-scene planning")
    for needle in ("defaultSelectionPolicy", "marked `preferred`", "capability's `defaults`", "must never hardcode"):
        if needle not in planning:
            raise ValidationError(f"operate generation-planning must keep server-owned defaults rule: {needle}")
    for needle in ("Universal duration", "rebalance", "1–3s", "1-3s"):
        if needle in planning:
            break
    else:
        raise ValidationError("operate generation-planning must include universal duration assembly")
    gates = read("references/duration-and-task-assembly.md")
    if "generation-planning.md" not in gates or "operate-topview-canvas" not in gates:
        raise ValidationError("duration-and-task-assembly must point to operate generation-planning.md")
    if "Workflow-specific single-task gates" not in gates:
        raise ValidationError("duration-and-task-assembly must keep workflow-specific single-task gates")


def validate_reference_links() -> None:
    for rel in RICH_WORKFLOWS:
        text = read(rel)
        if "reference-resolution.md" not in text:
            raise ValidationError(f"{rel} must point to reference-resolution.md")
    for rel in GENERATION_WORKFLOWS:
        text = read(rel)
        if "duration-and-task-assembly.md" not in text:
            raise ValidationError(f"{rel} must point to duration-and-task-assembly.md")


def validate_scene_contract() -> None:
    text = read("references/recipes/scene-surrogate.md")
    if "reference_node_ids" not in text:
        raise ValidationError("scene surrogate must mention reference_node_ids")
    if "typed" not in text.lower() or "inputs" not in text.lower():
        raise ValidationError("scene surrogate must distinguish semantic refs from typed inputs")
    if "node-groups.md" not in text or "operate-topview-canvas" not in text:
        raise ValidationError("scene surrogate must point to operate node-groups.md for Group structure")
    groups = _read_operate("references/node-groups.md")
    if "create_topview_canvas_group_node" not in groups:
        raise ValidationError("operate node-groups must document create_topview_canvas_group_node")
    if "generic" not in groups.lower() and "not a Scene-specific" not in groups:
        raise ValidationError("operate node-groups must describe generic Group composition, not Scene-only")


def validate_local_bridge() -> None:
    skill = read("SKILL.md")
    if "local-media-bridge.md" not in skill or "$operate-topview-canvas" not in skill:
        raise ValidationError(
            "SKILL.md must direct agents to $operate-topview-canvas local-media-bridge.md"
        )
    ffmpeg = read("references/recipes/ffmpeg-media.md")
    if "local-media-bridge.md" not in ffmpeg or "operate-topview-canvas" not in ffmpeg:
        raise ValidationError("ffmpeg-media recipe must point to operate local-media-bridge.md")
    text = _read_operate("references/local-media-bridge.md")
    for needle in (
        "prepare_topview_canvas_media_upload",
        "HTTP PUT",
        "create_topview_canvas_media_node",
        "canvas_node",
    ):
        if needle not in text:
            raise ValidationError(f"operate local media bridge must mention {needle}")
    for forbidden in ("ta_upload_credential", "ta_upload_check_file"):
        if forbidden in text:
            raise ValidationError(f"operate local media bridge must not use {forbidden} for Canvas")
    if "local filesystem paths" not in text.lower() and "Local filesystem paths" not in text:
        raise ValidationError("operate local media bridge must ban local paths as submit sources")


def validate_paid_generation_approval_mode() -> None:
    operate = _read_operate("SKILL.md")
    if "Paid generation approval mode" not in operate:
        raise ValidationError("operate SKILL.md must document Paid generation approval mode")
    for needle in ("confirm_each_submit", "autonomous", "paid generation approval mode gate"):
        if needle not in operate:
            raise ValidationError(f"operate SKILL.md must mention {needle}")
    api = _read_operate("references/canvas-mcp-api.md")
    if "confirm_each_submit" not in api or "autonomous" not in api:
        raise ValidationError("canvas-mcp-api must document paid generation approval modes")
    if "付费生成审批模式" not in api and "paid generation approval mode" not in api.lower():
        raise ValidationError("canvas-mcp-api must name the paid generation approval mode gate")
    orchestration = read("references/orchestration-runtime.md")
    if "confirm_each_submit" not in orchestration:
        raise ValidationError(
            "orchestration runtime must honor confirm_each_submit paid-parameter approval"
        )
    if "paid generation approval mode" not in orchestration.lower():
        raise ValidationError(
            "orchestration runtime must defer to paid generation approval mode"
        )
    if "bypass `confirm_each_submit`" not in orchestration and "bypass confirm_each_submit" not in orchestration:
        raise ValidationError(
            "orchestration runtime must forbid bypassing confirm_each_submit parameter approval"
        )
    skill = read("SKILL.md")
    if "paid generation approval mode" not in skill.lower():
        raise ValidationError(
            "canvas-agent-workflows SKILL.md must defer paid generation approval mode "
            "to $operate-topview-canvas"
        )


def validate_orchestration_runtime() -> None:
    text = read("references/orchestration-runtime.md")
    if "refresh_topview_canvas_generation_task" not in text:
        raise ValidationError("orchestration runtime must poll refresh_topview_canvas_generation_task")
    if "continue" not in text.lower():
        raise ValidationError("orchestration runtime must explicitly reject user continue barriers")
    if not re.search(r"(?i)observational", text) and "仅观测" not in text:
        if not re.search(r"(?i)do \*\*not\*\* send `?expectedRevision`?|Do \*\*not\*\* send `?expectedRevision`?", text):
            raise ValidationError(
                "orchestration runtime must treat revision as observational / forbid expectedRevision"
            )
    for match in re.finditer(r"(?i)revision chaining", text):
        start = max(0, match.start() - 48)
        snippet = text[start : match.end() + 24].lower()
        if not any(m in snippet for m in ("not ", "no ", "不要", "勿", "禁止")):
            raise ValidationError("orchestration runtime must not prefer revision chaining")
    if re.search(r"(?i)re-read .*get_topview_canvas_state.*before dependent", text):
        raise ValidationError(
            "orchestration runtime must not require get_state before every dependent stage"
        )
    if "before dependent stages" in text:
        raise ValidationError(
            "orchestration runtime must not require state re-read before dependent stages"
        )
    if "Parallelism is limited to read-only" in text:
        raise ValidationError(
            "orchestration runtime must not limit parallelism to read-only only "
            "(safe parallel independent tools are preferred)"
        )
    if "Safe Parallel Policy" not in text:
        raise ValidationError("orchestration runtime must document Safe Parallel Policy")
    if not re.search(r"(?i)wait-all", text):
        raise ValidationError("orchestration runtime must require wait-all for parallel waves")
    if re.search(r"(?i)Serial write vs parallel refresh", text):
        raise ValidationError("orchestration runtime must not use obsolete serial-vs-parallel-refresh framing")
    if re.search(r"(?i)refresh polls on that canvas stay serial|submit / \*\*refresh\*\* serial", text):
        raise ValidationError(
            "orchestration runtime must not demand blanket same-canvas refresh serial"
        )


def validate_stage_machine_and_references() -> None:
    stage = read("references/generation-stage-machine.md")
    for needle in (
        "Plan Ledger",
        "capabilityVersion",
        "mentionToken",
        "inputRoles",
        "Safe Parallel Policy",
    ):
        if needle not in stage:
            raise ValidationError(f"generation-stage-machine must mention {needle}")
    if "lastRevision" in stage:
        raise ValidationError("generation-stage-machine must not keep a lastRevision write cursor")
    if not re.search(r"(?i)do \*\*not\*\* send `?expectedRevision`?|Do \*\*not\*\* send `?expectedRevision`?", stage):
        raise ValidationError("generation-stage-machine must forbid sending expectedRevision")
    if not re.search(r"(?i)wait-all", stage):
        raise ValidationError("generation-stage-machine must require wait-all for parallel waves")
    if "parallelSameCanvasWrites=false" not in stage and "same-target" not in stage.lower():
        raise ValidationError(
            "generation-stage-machine must keep same-target / dependency-unsafe writes serial"
        )
    if re.search(r"(?i)\bbatch\s+(submit|mutation|write|create)\b", stage):
        raise ValidationError("generation-stage-machine must not recommend batch writes")
    if re.search(r"(?i)Serial write vs parallel refresh|Serial create / submit / refresh", stage):
        raise ValidationError(
            "generation-stage-machine must not demand blanket serial create/submit/refresh"
        )
    if re.search(r"(?i)shared latest successful revision", stage):
        raise ValidationError(
            "generation-stage-machine must not teach a shared latest revision across parallel polls"
        )
    if not re.search(r"(?i)distinct.{0,40}commandId|commandId.{0,40}distinct", stage):
        raise ValidationError("generation-stage-machine must require distinct commandId per paid intent")
    if "consistencyStatus=projected" not in stage and "projected" not in stage:
        raise ValidationError("generation-stage-machine must document projection barrier")

    refs = read("references/reference-resolution.md")
    if "canvas_node" not in refs or "nodeId" not in refs:
        raise ValidationError("reference-resolution must prefer canvas_node.nodeId")
    if "does **not** read or submit `assetId`" not in refs:
        raise ValidationError("reference-resolution must ban Agent-facing assetId")
    if '"kind": "canvas_asset"' in refs or "canvas_asset` + `assetId`" in refs:
        raise ValidationError("reference-resolution examples must not use canvas_asset/assetId")
    if "sceneNodeId" not in refs:
        raise ValidationError("reference-resolution must keep sceneNodeId storyboard contract")

    planning = _read_operate("references/generation-planning.md")
    if "inputRoles" not in planning:
        raise ValidationError("operate generation-planning must document summary inputRoles")
    if "hard-require `parametersSchema`" not in planning and "do **not** hard-require" not in planning:
        raise ValidationError(
            "operate generation-planning must not hard-require parametersSchema every time"
        )

    api = _read_operate("references/canvas-mcp-api.md")
    if "inputRoles" not in api:
        raise ValidationError("canvas-mcp-api must document summary inputRoles")
    if "wire-level deprecated" not in api or "canvas_asset" not in api:
        raise ValidationError(
            "canvas-mcp-api must keep canvas_asset as wire-level deprecated compatibility"
        )
    if "Agent 禁止使用" not in api:
        raise ValidationError("canvas-mcp-api must forbid Agent use of canvas_asset")
    if "Safe Parallel Policy" not in api:
        raise ValidationError("canvas-mcp-api must document Safe Parallel Policy")
    if "串行 create/submit/refresh" in api:
        raise ValidationError(
            "canvas-mcp-api must not demand blanket serial create/submit/refresh"
        )
    if "nodes.basic" not in api or "nodes.geometry" not in api:
        raise ValidationError("canvas-mcp-api must document state projection field set")
    if "真实投影" not in api and "project" not in api.lower() and "裁剪" not in api:
        raise ValidationError("canvas-mcp-api must clarify state filters project/crop the response")
    if "仅观测" not in api and "observational" not in api.lower():
        raise ValidationError("canvas-mcp-api must clarify response revision is observational")
    # Negatively forbid positive fields=["revision"] teaching
    for match in re.finditer(r'fields=\["revision"\]', api):
        start = max(0, match.start() - 48)
        snippet = api[start : match.end() + 32]
        normalized = re.sub(r"\*+", "", snippet.lower())
        if not any(
            m in snippet or m in normalized
            for m in ("不要", "勿", "禁止", "无", "not ", "do not", "**not**")
        ):
            raise ValidationError(
                'canvas-mcp-api must not teach fields=["revision"] positively'
            )
    # Negatively forbid positive fields=["environment"] teaching
    for match in re.finditer(r'fields=\["environment"\]', api):
        start = max(0, match.start() - 48)
        snippet = api[start : match.end() + 32]
        normalized = re.sub(r"\*+", "", snippet.lower())
        if not any(
            m in snippet or m in normalized
            for m in ("不要", "勿", "禁止", "无", "not ", "do not", "**not**")
        ):
            raise ValidationError(
                'canvas-mcp-api must not teach fields=["environment"] positively'
            )
    # Allowed projection enum must not still list environment after webUrl
    if re.search(r"`webUrl`[、,]\s*`environment`", api):
        raise ValidationError(
            "canvas-mcp-api must not list environment in the allowed state fields enum"
        )
    if "sinceRevision" not in api:
        raise ValidationError("canvas-mcp-api must explicitly reject sinceRevision claims")
    if "layout" not in api:
        raise ValidationError("canvas-mcp-api must document submit layout")
    if 'include=["state"]' not in api:
        raise ValidationError("canvas-mcp-api must document slim refresh / diagnostic include")

    short_film = read("references/workflows/short-film.md")
    if "sceneNodeId" not in short_film:
        raise ValidationError("short-film workflow must use sceneNodeId storyboard path")
    if "Asset nodes → persisted scenes → storyboard" not in short_film:
        raise ValidationError("short-film workflow must describe Asset → scene → storyboard → video DAG")
    if "Safe Parallel Policy" not in short_film and "safe-parallel" not in short_film.lower():
        raise ValidationError("short-film workflow must allow safe parallel same-layer work")


def _has_negation(snippet: str) -> bool:
    return any(marker in snippet for marker in NEGATION_MARKERS)


def validate_forbidden_and_continue() -> None:
    for rel, text in iter_skill_content():
        for pattern, label in HARD_BANNED_PATTERNS:
            match = pattern.search(text)
            if match:
                raise ValidationError(
                    f"{rel} contains banned web/product noun ({label}): {match.group(0)!r}"
                )
        for pattern, label in LEGACY_PATTERNS_ALLOW_NEGATION:
            for match in pattern.finditer(text):
                start = max(0, match.start() - 160)
                snippet = text[start : match.end() + 80].lower()
                if _has_negation(snippet):
                    continue
                raise ValidationError(
                    f"{rel} contains forbidden pattern ({label}): {match.group(0)}"
                )
        for match in CONTINUE_POSITIVE.finditer(text):
            start = max(0, match.start() - 64)
            snippet = text[start : match.end() + 32].lower()
            if _has_negation(snippet):
                continue
            raise ValidationError(
                f"{rel} contains a positive user continue/OK barrier: {match.group(0)!r}"
            )
        for match in THREE_SCENE_DEFAULT.finditer(text):
            start = max(0, match.start() - 64)
            snippet = text[start : match.end() + 32].lower()
            if any(
                marker in snippet
                for marker in ("never", "do not", "don't", "forbid", "no global", "not")
            ):
                continue
            raise ValidationError(
                f"{rel} appears to default to three scenes/tasks: {match.group(0)!r}"
            )


def validate_element_editing_reference_video() -> None:
    text = read("references/workflows/video-element-editing.md")
    if "reference_video" not in text:
        raise ValidationError("element editing must require reference_video")
    if "do not" not in text.lower() or "degrade" not in text.lower():
        raise ValidationError("element editing must forbid silent degradation without reference_video")


def validate_replication_policy() -> None:
    text = read("references/workflows/video-replication.md")
    if "do not" not in text.lower() or "reference_video" not in text:
        raise ValidationError("replication must state original reference_video policy")
    if "one" not in text.lower() or "15" not in text:
        raise ValidationError("replication must document 15s single-task expectation")


def validate_evals() -> None:
    payload = json.loads(read("evals/evals.json"))
    if not isinstance(payload, dict) or payload.get("schemaVersion") != 1:
        raise ValidationError("evals.json schemaVersion must be 1")
    cases = payload.get("cases")
    if not isinstance(cases, list) or len(cases) < 10:
        raise ValidationError("evals.json must include at least 10 cases")
    ids: set[str] = set()
    required_ids = {
        "Replication-15s",
        "Replication-16s",
        "Social-15s",
        "Ecommerce-single",
        "Short-continuous",
        "Element-edit-22s",
        "Voice-continuity",
        "Capability-max-10",
        "Missing-rich-route",
        "Non-durable-input",
        "Timeline-export",
    }
    for case in cases:
        if not isinstance(case, dict):
            raise ValidationError("each eval case must be an object")
        case_id = str(case.get("id", ""))
        if not case_id:
            raise ValidationError("eval case missing id")
        if case_id in ids:
            raise ValidationError(f"duplicate eval id: {case_id}")
        ids.add(case_id)
        if not str(case.get("prompt", "")).strip():
            raise ValidationError(f"{case_id} missing prompt")
        asserts = case.get("assertions")
        if not isinstance(asserts, list) or not asserts:
            raise ValidationError(f"{case_id} missing assertions")
    missing = sorted(required_ids - ids)
    if missing:
        raise ValidationError(f"evals.json missing required ids: {', '.join(missing)}")


def validate_no_secrets_or_user_paths() -> None:
    for path in SKILL_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix in {".pyc", ".pyo"} or "__pycache__" in path.parts:
            continue
        data = path.read_bytes()
        if any(marker in data for marker in USER_PATH_MARKERS):
            raise ValidationError(f"user-specific path found in {path.relative_to(SKILL_ROOT)}")
        text = data.decode("utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                raise ValidationError(f"possible secret material in {path.relative_to(SKILL_ROOT)}")


def validate_traceability_doc() -> None:
    path = REPO_DOCS / "CANVAS_WORKFLOW_MIGRATION_TRACEABILITY.md"
    if not path.is_file():
        raise ValidationError("missing docs/CANVAS_WORKFLOW_MIGRATION_TRACEABILITY.md")
    text = path.read_text(encoding="utf-8")
    for needle in ("workflow-video-replication", "canvas-agent-workflows", "feature/init"):
        if needle not in text:
            raise ValidationError(f"traceability doc missing {needle}")


def main() -> int:
    checks = [
        validate_required_files,
        validate_skill_frontmatter,
        validate_capability_first,
        validate_reference_links,
        validate_scene_contract,
        validate_local_bridge,
        validate_orchestration_runtime,
        validate_paid_generation_approval_mode,
        validate_stage_machine_and_references,
        validate_forbidden_and_continue,
        validate_element_editing_reference_video,
        validate_replication_policy,
        validate_evals,
        validate_no_secrets_or_user_paths,
        validate_traceability_doc,
    ]
    try:
        for check in checks:
            check()
    except ValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"OK: canvas-agent-workflows bundle validated ({len(REQUIRED_FILES)} required files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
