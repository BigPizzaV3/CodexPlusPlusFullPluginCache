#!/usr/bin/env python3
"""Fail-closed validator for the phased direct-image LP workflow."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import struct
import sys
import zlib
from pathlib import Path
from typing import Callable
from urllib.parse import urljoin, urlsplit


PHASES = [
    "structure-approved",
    "fv-selection-pending",
    "fv-review",
    "fv-direction-approved",
    "page-continuity-approved",
    "sections-complete",
    "whole-page-reviewed",
    "assembly-approved",
    "assembled",
]
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")
CODE_SUFFIXES = {".html", ".htm", ".css", ".js", ".jsx", ".ts", ".tsx"}
SECTION_NAME_DENY_PATTERN = re.compile(r"(?:^|[-_.])(screen(?:shot)?|review|whole|full[-_]?page|crop)(?:[-_.]|$)", re.IGNORECASE)
WORKFLOW_SCHEMA_VERSION = "1.5"
READ_ONLY_WORKFLOW_SCHEMA_VERSIONS = {"1.1", "1.2", "1.3", "1.4"}
LEGACY_WORKFLOW_SCHEMA_VERSION = "1.1"
MIN_FINISHED_FV_HEIGHT = 600
MAX_FINISHED_FV_HEIGHT = 900
MIN_COLOR_BUCKETS = 8
MIN_LUMA_RANGE = 24
MIN_EDGE_RATIO = 0.002
MIN_CANDIDATE_PIXEL_DIFFERENCE_RATIO = 0.03
CANDIDATE_ID_PATTERN = re.compile(r"^candidate-[0-9]{2,}$")
CANDIDATE_TOKEN_PATTERN = re.compile(r"(?<![A-Za-z0-9_-])candidate-[0-9]{2,}(?![A-Za-z0-9_-])")
LiveRuntimeProbe = Callable[[dict, str, str], dict]


def _load_direct_validator():
    script = Path(__file__).with_name("validate_direct_image_manifest.py")
    spec = importlib.util.spec_from_file_location("lp_direct_image_manifest_validator", script)
    if not spec or not spec.loader:
        raise RuntimeError("cannot load direct-image manifest validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DIRECT = _load_direct_validator()


class WorkflowError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise WorkflowError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(payload: object) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def workflow_state_binding(path: Path, project_root: Path) -> dict[str, str]:
    """Return the caller-visible binding for a workflow state outside artifact_root."""

    try:
        relative = path.resolve().relative_to(project_root.resolve())
    except ValueError as exc:
        raise WorkflowError("prior pending workflow state must stay inside project root") from exc
    require(".." not in relative.parts, "prior pending workflow state path is invalid")
    return {"path": relative.as_posix(), "sha256": sha256(path.resolve())}


def selection_neutral_projection(comparison: dict) -> dict:
    """Project a comparison onto facts that must not change after presentation.

    Selection-only flags, rejection explanations, the exact later-turn context,
    and its approval binding are intentionally excluded. Candidate order, image
    and provenance bindings, inspection evidence, material axes, presentation,
    structure/budget/batch bindings, and validator scope remain committed.
    """

    candidates = []
    for candidate in comparison.get("candidates", []):
        projected = dict(candidate)
        inspection = candidate.get("inspection")
        if isinstance(inspection, dict):
            projected_inspection = {
                key: value
                for key, value in inspection.items()
                if key not in {"selected", "rejection_reason"}
            }
            projected["inspection"] = projected_inspection
        candidates.append(projected)
    return {
        "kind": comparison.get("kind"),
        "schema_version": comparison.get("schema_version"),
        "structure_sha256": comparison.get("structure_sha256"),
        "fv_content_budget": comparison.get("fv_content_budget"),
        "fv_content_budget_sha256": comparison.get("fv_content_budget_sha256"),
        "batch_context": comparison.get("batch_context"),
        "candidates": candidates,
        "material_difference_pairs": comparison.get("material_difference_pairs"),
        "candidate_presentation": comparison.get("candidate_presentation"),
        "reviewer_input_image_sha256s": comparison.get("reviewer_input_image_sha256s"),
        "validator_scope": comparison.get("validator_scope"),
    }


def load_json(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkflowError(f"cannot read {label}: {exc}") from exc
    require(isinstance(value, dict), f"{label} must be a JSON object")
    return value


def resolve_inside(root: Path, value: object, label: str, *, directory: bool = False) -> Path:
    require(isinstance(value, str) and value and value.strip() == value, f"{label} must be a relative path")
    relative = Path(value)
    require(not relative.is_absolute() and ".." not in relative.parts, f"{label} must stay inside its root")
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise WorkflowError(f"{label} escapes its root") from exc
    require(resolved.is_dir() if directory else resolved.is_file(), f"{label} does not exist: {value}")
    return resolved


def validate_binding(binding: object, artifact_root: Path, label: str) -> Path:
    require(isinstance(binding, dict) and set(binding) == {"path", "sha256"}, f"{label} binding is invalid")
    path = resolve_inside(artifact_root, binding.get("path"), f"{label}.path")
    digest = binding.get("sha256")
    require(isinstance(digest, str) and SHA256_PATTERN.fullmatch(digest), f"{label}.sha256 is invalid")
    require(digest == sha256(path), f"{label} sha256 mismatch")
    return path


def phase_at_least(phase: str, threshold: str) -> bool:
    return PHASES.index(phase) >= PHASES.index(threshold)


def validate_base_origin(value: object) -> str:
    require(isinstance(value, str) and value == value.strip(), "runtime base_origin must be a normalized origin")
    parsed = urlsplit(value)
    require(
        parsed.scheme == "http"
        and parsed.hostname in {"127.0.0.1", "localhost"}
        and parsed.username is None
        and parsed.password is None
        and parsed.path == ""
        and parsed.query == ""
        and parsed.fragment == "",
        "runtime base_origin must be loopback http with no credentials/path/query/fragment",
    )
    try:
        port = parsed.port
    except ValueError as exc:
        raise WorkflowError("runtime base_origin port is invalid") from exc
    require(port is not None and 1 <= port <= 65535, "runtime base_origin requires an explicit valid port")
    normalized = f"http://{parsed.hostname}:{port}"
    require(value == normalized, "runtime base_origin must be normalized exactly")
    return normalized


def validate_runtime_route(route: object, base_origin: str) -> str:
    require(
        isinstance(route, str)
        and route == route.strip()
        and route.startswith("/")
        and not route.startswith("//")
        and "\\" not in route,
        "runtime route must be a single-slash absolute path without backslashes",
    )
    parsed = urlsplit(route)
    require(not parsed.scheme and not parsed.netloc and not parsed.fragment, "runtime route must not change origin or contain a fragment")
    target = urlsplit(urljoin(f"{base_origin}/", route))
    target_origin = f"{target.scheme}://{target.hostname}:{target.port}"
    require(target_origin == base_origin, "runtime route resolution changed the approved origin")
    return route


def validate_ledger(
    state: dict,
    artifact_root: Path,
    *,
    allow_later_artifacts: bool = False,
) -> dict[str, str]:
    ledger = state.get("artifact_ledger")
    require(isinstance(ledger, list), "artifact_ledger must be an array")
    ledger_paths: dict[str, str] = {}
    allowed_kinds = {
        "structure", "approval-receipt", "section-image", "review-json",
        "review-image", "continuity-plan", "manifest", "runtime-code", "runtime-map", "runtime-qa",
        "candidate-image", "source-evidence", "approval-view",
    }
    for index, entry in enumerate(ledger, start=1):
        require(isinstance(entry, dict) and set(entry) == {"kind", "path", "sha256"}, f"artifact_ledger item {index} fields are invalid")
        kind = entry.get("kind")
        value = entry.get("path")
        digest = entry.get("sha256")
        require(kind in allowed_kinds, f"artifact_ledger item {index} kind is invalid")
        require(isinstance(value, str) and value not in ledger_paths, f"artifact_ledger path must be unique: {value}")
        path = resolve_inside(artifact_root, value, f"artifact_ledger item {index}.path")
        require(path.is_file() and not path.is_symlink(), f"artifact ledger may contain regular files only: {value}")
        require(isinstance(digest, str) and SHA256_PATTERN.fullmatch(digest), f"artifact_ledger item {index} sha256 is invalid")
        require(digest == sha256(path), f"artifact_ledger sha256 mismatch: {value}")
        ledger_paths[value] = kind

    inventory: set[str] = set()
    for path in artifact_root.rglob("*"):
        require(not path.is_symlink(), f"artifact_root must not contain symlinks: {path.relative_to(artifact_root)}")
        if path.is_file():
            inventory.add(path.relative_to(artifact_root).as_posix())
    if allow_later_artifacts:
        require(set(ledger_paths) <= inventory, "frozen pending ledger references a missing artifact")
    else:
        require(set(ledger_paths) == inventory, "artifact_ledger must exactly equal recursive artifact_root inventory")
    return ledger_paths


def png_rows(path: Path) -> tuple[int, int, int, list[bytes]]:
    width, height = DIRECT.validate_png(path)
    data = path.read_bytes()
    offset = len(DIRECT.PNG_SIGNATURE)
    color_type = -1
    compressed: list[bytes] = []
    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + length]
        if kind == b"IHDR":
            color_type = payload[9]
        elif kind == b"IDAT":
            compressed.append(payload)
        offset += 12 + length
    channels = 3 if color_type == 2 else 4
    raw = zlib.decompress(b"".join(compressed))
    stride = width * channels
    rows: list[bytes] = []
    prior = bytes(stride)
    cursor = 0
    for _ in range(height):
        filter_type = raw[cursor]
        encoded = raw[cursor + 1:cursor + 1 + stride]
        cursor += stride + 1
        decoded = bytearray(stride)
        for index, byte in enumerate(encoded):
            left = decoded[index - channels] if index >= channels else 0
            above = prior[index]
            upper_left = prior[index - channels] if index >= channels else 0
            if filter_type == 0:
                predictor = 0
            elif filter_type == 1:
                predictor = left
            elif filter_type == 2:
                predictor = above
            elif filter_type == 3:
                predictor = (left + above) // 2
            else:
                p = left + above - upper_left
                distances = (abs(p - left), abs(p - above), abs(p - upper_left))
                predictor = (left, above, upper_left)[distances.index(min(distances))]
            decoded[index] = (byte + predictor) & 0xFF
        prior = bytes(decoded)
        if channels == 3:
            rgba = b"".join(decoded[index:index + 3] + b"\xff" for index in range(0, stride, 3))
        else:
            rgba = bytes(decoded)
        rows.append(rgba)
    return width, height, channels, rows


def canonical_premultiplied_rows(rows: list[bytes]) -> list[bytes]:
    canonical: list[bytes] = []
    for row in rows:
        output = bytearray(len(row))
        for offset in range(0, len(row), 4):
            red, green, blue, alpha = row[offset:offset + 4]
            if alpha == 0:
                red = green = blue = 0
            elif alpha < 255:
                red = (red * alpha + 127) // 255
                green = (green * alpha + 127) // 255
                blue = (blue * alpha + 127) // 255
            output[offset:offset + 4] = bytes((red, green, blue, alpha))
        canonical.append(bytes(output))
    return canonical


def validate_new_image_descriptor(
    image: object,
    artifact_root: Path,
    label: str,
) -> tuple[Path, set[tuple[str, str]], list[bytes]]:
    fields = {"id", "order", "path", "sha256", "width", "height", "creation_method", "provenance", "browser_screenshot", "derived_from_whole_page"}
    require(isinstance(image, dict) and set(image) == fields, f"{label} fields are invalid")
    path = validate_binding({"path": image.get("path"), "sha256": image.get("sha256")}, artifact_root, label)
    width, height, _, rows = png_rows(path)
    require(width == 390
            and DIRECT.strict_int(image.get("width")) and image.get("width") == width
            and DIRECT.strict_int(image.get("height")) and image.get("height") == height,
            f"{label} dimensions are invalid")
    require(image.get("browser_screenshot") is False, f"{label} must not be a browser screenshot")
    require(image.get("derived_from_whole_page") is False, f"{label} must not derive from a whole-page review")
    method = image.get("creation_method")
    provenance = image.get("provenance")
    expected: set[tuple[str, str]] = set()
    expected_kind = {
        "image-generation": "host-session-image-generation",
        "user-provided": "user-provided-finished-artwork",
    }.get(method)
    require(expected_kind is not None, f"{label} requires full regenerated or newly user-provided finished artwork")
    provenance_fields = {"kind", "finished_design", "source_sha256", "evidence"}
    require(
        isinstance(provenance, dict)
        and set(provenance) == provenance_fields
        and provenance.get("kind") == expected_kind
        and provenance.get("finished_design") is True
        and provenance.get("source_sha256") == image.get("sha256"),
        f"{label} provenance binding is invalid",
    )
    evidence_path = validate_binding(provenance.get("evidence"), artifact_root, f"{label} source evidence")
    evidence = load_json(evidence_path, f"{label} source evidence")
    evidence_fields = {
        "kind", "schema_version", "source_kind", "source_sha256", "finished_design",
        "provided_by", "source_reference", "evidence",
    }
    require(
        set(evidence) == evidence_fields
        and evidence.get("kind") == "finished-image-source-evidence"
        and evidence.get("schema_version") == "1.0"
        and evidence.get("source_kind") == expected_kind
        and evidence.get("source_sha256") == image.get("sha256")
        and evidence.get("finished_design") is True
        and DIRECT.nonempty_string(evidence.get("evidence")),
        f"{label} source evidence content is invalid",
    )
    expected_provider = "host" if method == "image-generation" else {"user", "controller"}
    require(
        evidence.get("provided_by") == expected_provider
        if isinstance(expected_provider, str)
        else evidence.get("provided_by") in expected_provider,
        f"{label} source evidence provider is invalid",
    )
    reference = evidence.get("source_reference")
    if method == "image-generation":
        require(
            isinstance(reference, dict)
            and set(reference) == {"kind", "invocation_id", "result_asset_id"}
            and reference.get("kind") == "host-image-generation-result"
            and DIRECT.nonempty_string(reference.get("invocation_id"))
            and DIRECT.nonempty_string(reference.get("result_asset_id")),
            f"{label} source evidence requires concrete host invocation/result identifiers",
        )
    else:
        require(
            isinstance(reference, dict)
            and set(reference) == {"kind", "message_id", "attachment_id"}
            and reference.get("kind") == "user-attachment"
            and DIRECT.nonempty_string(reference.get("message_id"))
            and DIRECT.nonempty_string(reference.get("attachment_id")),
            f"{label} source evidence requires concrete user message/attachment identifiers",
        )
    expected.add((provenance["evidence"]["path"], "source-evidence"))
    canonical_rows = canonical_premultiplied_rows(rows)
    color_buckets: set[tuple[int, int, int]] = set()
    min_luma = 255
    max_luma = 0
    visible_pixels = 0
    edge_changes = 0
    edge_total = 0
    prior_lumas: list[int] | None = None
    for row in canonical_rows:
        row_lumas: list[int] = []
        prior_luma: int | None = None
        for offset in range(0, len(row), 4):
            red, green, blue, alpha = row[offset:offset + 4]
            if alpha > 2:
                visible_pixels += 1
            color_buckets.add((red >> 5, green >> 5, blue >> 5))
            luma = (54 * red + 183 * green + 19 * blue) >> 8
            row_lumas.append(luma)
            min_luma = min(min_luma, luma)
            max_luma = max(max_luma, luma)
            if prior_luma is not None:
                edge_total += 1
                edge_changes += abs(luma - prior_luma) >= 8
            prior_luma = luma
        if prior_lumas is not None:
            edge_total += len(row_lumas)
            edge_changes += sum(abs(current - above) >= 8 for current, above in zip(row_lumas, prior_lumas))
        prior_lumas = row_lumas
    require(visible_pixels > 0, f"{label} must contain visible pixels")
    require(
        len(color_buckets) >= MIN_COLOR_BUCKETS
        and max_luma - min_luma >= MIN_LUMA_RANGE
        and edge_total > 0
        and edge_changes / edge_total >= MIN_EDGE_RATIO,
        f"{label} must pass conservative non-flat color/luma/edge sanity",
    )
    return path, expected, rows


def validate_structure(
    state: dict,
    artifact_root: Path,
    workflow_schema: str,
) -> tuple[dict, dict, list[dict], list[dict], list[dict], set[tuple[str, str]]]:
    structure = state.get("structure")
    structure_fields = {"path", "sha256", "approval_receipt"}
    if workflow_schema in {"1.4", WORKFLOW_SCHEMA_VERSION}:
        structure_fields.add("approval_view")
    require(isinstance(structure, dict) and set(structure) == structure_fields, "structure fields are invalid")
    structure_path = validate_binding({"path": structure.get("path"), "sha256": structure.get("sha256")}, artifact_root, "structure")
    document = load_json(structure_path, "structure document")
    try:
        sections, boundaries, series = DIRECT.validate_structure_document(document, artifact_root)
        if workflow_schema == WORKFLOW_SCHEMA_VERSION:
            DIRECT.validate_structure_production(document, artifact_root)
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    expected = {(structure["path"], "structure")}
    if document.get("schema_version") == DIRECT.STRUCTURE_SCHEMA_VERSION:
        expected |= {
            (source["evidence"]["path"], "source-evidence")
            for source in document.get("source_ledger", [])
            if source.get("kind") in {"permission-record", "privacy-review"}
        }
    if workflow_schema in {"1.4", WORKFLOW_SCHEMA_VERSION}:
        approval_view_path = validate_binding(structure.get("approval_view"), artifact_root, "structure approval view")
        try:
            DIRECT.validate_structure_approval_view(
                approval_view_path,
                document,
                structure["path"],
                structure["sha256"],
            )
        except DIRECT.ContractError as exc:
            raise WorkflowError(str(exc)) from exc
        expected.add((structure["approval_view"]["path"], "approval-view"))
    receipt = structure.get("approval_receipt")
    receipt_path = validate_binding(receipt, artifact_root, "structure approval receipt")
    subject = DIRECT.structure_approval_subject(document, structure["path"], structure["sha256"])
    try:
        DIRECT.validate_receipt(receipt_path, "lp-structure", canonical_digest(subject), "structure approval receipt")
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    expected.add((receipt["path"], "approval-receipt"))
    return structure, document, sections, boundaries, series, expected


def validate_candidate_observations(
    inspection: object,
    handoff: dict,
    *,
    selected: bool,
    selection_pending: bool,
    label: str,
) -> None:
    fields = {
        "render_inspection", "provider_recognition", "belief_shift", "credibility", "action",
        "message_image_alignment", "hierarchy", "copy_readability", "generic_substitution",
        "content_budget_observation", "message_match", "scan_outcomes", "render_copy_fit",
        "selected", "rejection_reason",
    }
    require(isinstance(inspection, dict) and set(inspection) == fields, f"{label} inspection fields are invalid")
    render = inspection.get("render_inspection")
    require(
        isinstance(render, dict)
        and set(render) == {"status", "input_sha256", "notes"}
        and render.get("status") == "inspected-in-session"
        and isinstance(render.get("input_sha256"), str)
        and SHA256_PATTERN.fullmatch(render["input_sha256"])
        and DIRECT.nonempty_string(render.get("notes")),
        f"{label} requires an actual rendered-image inspection record",
    )

    expected_provider = handoff["provider_recognition"]
    provider = inspection.get("provider_recognition")
    require(
        isinstance(provider, dict)
        and set(provider) == {"decision", "observed_provider_name", "location", "observation"}
        and provider.get("decision") == expected_provider["decision"]
        and DIRECT.nonempty_string(provider.get("observation")),
        f"{label} provider observation is invalid",
    )
    if expected_provider["decision"] == "visible":
        require(provider.get("observed_provider_name") == expected_provider["provider_name"], f"{label} is missing exact visible provider identity")
        require(DIRECT.nonempty_string(provider.get("location")), f"{label} visible provider location is required")
    else:
        require(provider.get("observed_provider_name") is None and provider.get("location") is None, f"{label} deferred provider observation must be null")

    belief = inspection.get("belief_shift")
    require(
        isinstance(belief, dict)
        and set(belief) == {"visible_expression", "location", "observation"}
        and belief.get("visible_expression") == handoff["belief_shift"]["visible_expression"]
        and DIRECT.nonempty_string(belief.get("location"))
        and DIRECT.nonempty_string(belief.get("observation")),
        f"{label} belief-shift observation is incomplete",
    )

    credibility = inspection.get("credibility")
    expected_credibility = handoff["credibility"]["visible_expressions"]
    require(isinstance(credibility, list) and len(credibility) == len(expected_credibility), f"{label} credibility observations are incomplete")
    for index, (observed, expected) in enumerate(zip(credibility, expected_credibility), start=1):
        require(
            isinstance(observed, dict)
            and set(observed) == {"claim_id", "visible_expression", "location", "observation"}
            and observed.get("claim_id") == expected["claim_id"]
            and observed.get("visible_expression") == expected["text"]
            and DIRECT.nonempty_string(observed.get("location"))
            and DIRECT.nonempty_string(observed.get("observation")),
            f"{label} credibility observation {index} is incomplete",
        )

    action = inspection.get("action")
    require(
        isinstance(action, dict)
        and set(action) == {"visible_label", "location", "observation", "primary_action_count"}
        and action.get("visible_label") == handoff["five_second"]["next_action"]
        and isinstance(action.get("primary_action_count"), int)
        and not isinstance(action["primary_action_count"], bool)
        and action["primary_action_count"] == 1
        and DIRECT.nonempty_string(action.get("location"))
        and DIRECT.nonempty_string(action.get("observation")),
        f"{label} action observation is incomplete",
    )
    message_match = inspection.get("message_match")
    require(
        isinstance(message_match, dict)
        and set(message_match) == {"source_message", "offer", "next_action", "observation"}
        and all(message_match.get(key) == "pass" for key in ("source_message", "offer", "next_action"))
        and DIRECT.nonempty_string(message_match.get("observation")),
        f"{label} source-message/offer/action match must pass",
    )
    scan_outcomes = inspection.get("scan_outcomes")
    scan_contract = handoff["scan_contract"]
    require(isinstance(scan_outcomes, dict) and set(scan_outcomes) == set(scan_contract),
            f"{label} scan outcomes are incomplete")
    for key, contract in scan_contract.items():
        outcome = scan_outcomes.get(key)
        require(
            isinstance(outcome, dict)
            and set(outcome) == {"decision", "answer", "evidence_used", "observation"}
            and outcome.get("decision") == "pass"
            and outcome.get("answer") == contract["answer"]
            and isinstance(outcome.get("evidence_used"), list)
            and outcome["evidence_used"]
            and all(mode in contract["evidence_modes"] for mode in outcome["evidence_used"])
            and DIRECT.nonempty_string(outcome.get("observation")),
            f"{label} scan outcome {key} must pass with approved copy/visual/proof/CTA evidence",
        )
    fit = inspection.get("render_copy_fit")
    require(
        isinstance(fit, dict)
        and set(fit) == {
            "viewport_width", "headline_lines", "support_lines", "cta_lines",
            "nonuniform_glyph_scaling", "condensed_to_fit", "clipping", "overflow", "observation",
        }
        and DIRECT.strict_int(fit.get("viewport_width")) and fit.get("viewport_width") == 390
        and isinstance(fit.get("headline_lines"), int) and not isinstance(fit["headline_lines"], bool) and 1 <= fit["headline_lines"] <= 3
        and isinstance(fit.get("support_lines"), int) and not isinstance(fit["support_lines"], bool) and 0 <= fit["support_lines"] <= 4
        and isinstance(fit.get("cta_lines"), int) and not isinstance(fit["cta_lines"], bool) and fit["cta_lines"] == 1
        and all(fit.get(key) is False for key in ("nonuniform_glyph_scaling", "condensed_to_fit", "clipping", "overflow"))
        and DIRECT.nonempty_string(fit.get("observation")),
        f"{label} rendered copy fit must pass at 390px (H1 <=3, support <=4, CTA=1 line, no squeeze/clip/overflow)",
    )
    for field in ("message_image_alignment", "copy_readability"):
        value = inspection.get(field)
        require(
            isinstance(value, dict)
            and set(value) == {"decision", "observation"}
            and value.get("decision") == "pass"
            and DIRECT.nonempty_string(value.get("observation")),
            f"{label} {field} observation must pass",
        )
    hierarchy = inspection.get("hierarchy")
    require(isinstance(hierarchy, list) and len(hierarchy) >= 3, f"{label} hierarchy observations are incomplete")
    for rank, item in enumerate(hierarchy, start=1):
        require(
            isinstance(item, dict)
            and set(item) == {"rank", "element", "location", "observation"}
            and DIRECT.strict_int(item.get("rank")) and item.get("rank") == rank
            and DIRECT.nonempty_string(item.get("element"))
            and DIRECT.nonempty_string(item.get("location"))
            and DIRECT.nonempty_string(item.get("observation")),
            f"{label} hierarchy observation {rank} is weak or unobserved",
        )
    generic = inspection.get("generic_substitution")
    require(
        isinstance(generic, dict)
        and set(generic) == {"assessment", "concrete_observations"}
        and generic.get("assessment") == "distinctive"
        and isinstance(generic.get("concrete_observations"), list)
        and len(generic["concrete_observations"]) >= 2
        and all(DIRECT.nonempty_string(item) for item in generic["concrete_observations"]),
        f"{label} generic substitution is risky or lacks concrete observations",
    )
    budget = handoff["fv_content_budget"]
    visible_items = budget["visible_items"]
    budget_observation = inspection.get("content_budget_observation")
    expected_item_ids = [item["id"] for item in visible_items]
    expected_char_count = sum(DIRECT.non_whitespace_length(item["text"]) for item in visible_items)
    expected_proof_count = sum(item["semantic_role"] == "proof" for item in visible_items)
    require(
        isinstance(budget_observation, dict)
        and set(budget_observation) == {
            "profile", "visible_item_ids", "observed_char_count", "observed_item_count",
            "observed_proof_count", "no_unplanned_text", "unplanned_visible_text",
        }
        and budget_observation.get("profile") == budget["profile"]
        and budget_observation.get("visible_item_ids") == expected_item_ids
        and all(DIRECT.strict_int(budget_observation.get(key)) for key in (
            "observed_char_count", "observed_item_count", "observed_proof_count"
        ))
        and budget_observation.get("observed_char_count") == expected_char_count
        and budget_observation.get("observed_item_count") == len(visible_items)
        and budget_observation.get("observed_proof_count") == expected_proof_count
        and budget_observation.get("no_unplanned_text") is True
        and budget_observation.get("unplanned_visible_text") == [],
        f"{label} content-budget inventory/counts drift or declare unplanned visible text",
    )
    require(inspection.get("selected") is selected, f"{label} selected flag drift")
    if selected:
        require(inspection.get("rejection_reason") is None, f"{label} selected candidate cannot have a rejection reason")
    elif selection_pending:
        require(inspection.get("rejection_reason") is None, f"{label} pending candidate must remain neutrally unselected")
    else:
        require(DIRECT.nonempty_string(inspection.get("rejection_reason")), f"{label} rejected candidate requires a concrete rejection reason")


def validate_fv_candidates_and_comparison(
    state: dict,
    artifact_root: Path,
    structure: dict,
    structure_document: dict,
    structure_sections: list[dict],
    phase: str,
    workflow_schema: str,
    *,
    validate_batch_history: bool = True,
    comparison_outcome: dict | None = None,
) -> tuple[list[dict], dict | None, dict | None, set[tuple[str, str]]]:
    if workflow_schema != WORKFLOW_SCHEMA_VERSION:
        return [], None, None, set()
    candidates = state.get("fv_candidates")
    comparison_binding = state.get("fv_creative_comparison")
    if validate_batch_history:
        history = state.get("fv_batch_history")
        require(isinstance(history, list), "fv_batch_history must be an array")
    require(isinstance(candidates, list), "fv_candidates must be an array")
    if phase == "structure-approved":
        require(not candidates and comparison_binding is None, "FV candidates/comparison are forbidden before fv-review")
        if validate_batch_history:
            require(not history, "fv_batch_history must be empty before fv-review")
        return candidates, None, None, set()
    require(len(candidates) == 2, "workflow schema 1.5 requires exactly two finished FV candidates per batch before selection")
    expected: set[tuple[str, str]] = set()
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    seen_hashes: set[str] = set()
    seen_source_references: dict[tuple[str, ...], str] = {}
    source_evidence_expected: set[tuple[str, str]] = set()
    decoded_candidates: list[tuple[int, int, list[bytes], list[bytes]]] = []
    for index, candidate in enumerate(candidates, start=1):
        require(isinstance(candidate, dict) and set(candidate) == {"candidate_id", "image"}, f"FV candidate {index} fields are invalid")
        candidate_id = candidate.get("candidate_id")
        require(
            isinstance(candidate_id, str)
            and CANDIDATE_ID_PATTERN.fullmatch(candidate_id) is not None
            and candidate_id not in seen_ids,
            f"FV candidate {index} id must be a unique candidate-<digits> token",
        )
        image = candidate.get("image")
        _, image_expected, rows = validate_new_image_descriptor(image, artifact_root, f"FV candidate {index}")
        require(
            MIN_FINISHED_FV_HEIGHT <= image.get("height", 0) <= MAX_FINISHED_FV_HEIGHT,
            f"FV candidate {index} height must be between {MIN_FINISHED_FV_HEIGHT}px and {MAX_FINISHED_FV_HEIGHT}px",
        )
        require(image.get("id") == structure_sections[0].get("id")
                and DIRECT.strict_int(image.get("order")) and image.get("order") == 1,
                f"FV candidate {index} drifts from first approved section")
        require(image["path"] not in seen_paths and image["sha256"] not in seen_hashes, "FV candidates require distinct paths and hashes")
        evidence_path = resolve_inside(
            artifact_root, image["provenance"]["evidence"]["path"], f"FV candidate {index} source evidence",
        )
        evidence = load_json(evidence_path, f"FV candidate {index} source evidence")
        reference = evidence["source_reference"]
        reference_key = (
            ("host-result", reference["result_asset_id"])
            if reference["kind"] == "host-image-generation-result"
            else ("user-attachment", reference["message_id"], reference["attachment_id"])
        )
        require(
            reference_key not in seen_source_references,
            f"FV candidate {index} source result/attachment reference must be unique across distinct candidates",
        )
        seen_source_references[reference_key] = image["sha256"]
        seen_ids.add(candidate_id)
        seen_paths.add(image["path"])
        seen_hashes.add(image["sha256"])
        source_evidence_expected |= image_expected
        decoded_candidates.append((image["width"], image["height"], rows, canonical_premultiplied_rows(rows)))

    for left in range(len(decoded_candidates)):
        left_width, left_height, _, left_canonical_rows = decoded_candidates[left]
        left_pixels = b"".join(left_canonical_rows)
        for right in range(left + 1, len(decoded_candidates)):
            right_width, right_height, _, right_canonical_rows = decoded_candidates[right]
            right_pixels = b"".join(right_canonical_rows)
            require(left_width == right_width == 390, "FV candidate widths must remain 390px")
            overlap_pixels = min(left_height, right_height) * left_width
            differing = sum(
                left_pixels[offset:offset + 4] != right_pixels[offset:offset + 4]
                for offset in range(0, overlap_pixels * 4, 4)
            )
            differing += abs(left_height - right_height) * left_width
            total_pixels = max(left_height, right_height) * left_width
            require(
                total_pixels > 0 and differing / total_pixels >= MIN_CANDIDATE_PIXEL_DIFFERENCE_RATIO,
                f"FV candidates {left + 1}/{right + 1} require at least 3% canonical decoded RGBA pixel difference",
            )

    comparison_path = validate_binding(comparison_binding, artifact_root, "FV creative comparison")
    require(comparison_path.suffix.lower() == ".json", "FV creative comparison must be JSON")
    comparison = load_json(comparison_path, "FV creative comparison")
    fields = {
        "kind", "schema_version", "structure_sha256", "candidates", "material_difference_pairs",
        "candidate_presentation", "selected_candidate_id", "selection_context", "selection_approval",
        "reviewer_input_image_sha256s", "fv_content_budget", "fv_content_budget_sha256",
        "batch_context", "selection_status", "pending_comparison_sha256", "validator_scope",
    }
    require(set(comparison) == fields, "FV creative comparison fields are invalid")
    require(comparison.get("kind") == "lp-fv-creative-comparison" and comparison.get("schema_version") == "1.2", "FV creative comparison type is invalid")
    require(comparison.get("structure_sha256") == structure["sha256"], "FV creative comparison structure hash drift")
    budget = structure_document["fv_handoff"]["fv_content_budget"]
    require(comparison.get("fv_content_budget") == budget, "FV creative comparison content budget drift")
    require(comparison.get("fv_content_budget_sha256") == canonical_digest(budget), "FV creative comparison content budget digest drift")
    batch = comparison.get("batch_context")
    require(
        isinstance(batch, dict)
        and set(batch) == {"batch_number", "kind", "request_message_id", "request_text", "revision_approval"}
        and DIRECT.strict_int(batch.get("batch_number"))
        and batch.get("batch_number") in {1, 2},
        "FV candidate batch_context permits only initial batch 1 or revision batch 2",
    )
    if batch["batch_number"] == 1:
        require(batch.get("kind") == "initial" and batch.get("request_message_id") is None
                and batch.get("request_text") is None and batch.get("revision_approval") is None,
                "FV initial batch context is invalid")
    else:
        require(batch.get("kind") == "user-requested-revision"
                and DIRECT.nonempty_string(batch.get("request_message_id"))
                and DIRECT.nonempty_string(batch.get("request_text"))
                and isinstance(batch.get("revision_approval"), dict),
                "FV revision batch 2 requires an explicit user/controller request")
    presentation = comparison.get("candidate_presentation")
    presentation_fields = {"path", "sha256", "width", "height", "candidate_sha256s", "layout", "review_only"}
    require(isinstance(presentation, dict) and set(presentation) == presentation_fields, "FV candidate presentation fields are invalid")
    presentation_path = validate_binding({"path": presentation.get("path"), "sha256": presentation.get("sha256")}, artifact_root, "FV candidate presentation")
    presentation_width, presentation_height, _, presentation_rows = png_rows(presentation_path)
    require(
        DIRECT.strict_int(presentation.get("width"))
        and DIRECT.strict_int(presentation.get("height"))
        and presentation_width == presentation.get("width") == 390
        and presentation_height == presentation.get("height") == sum(candidate["image"]["height"] for candidate in candidates)
        and presentation.get("candidate_sha256s") == [candidate["image"]["sha256"] for candidate in candidates]
        and presentation.get("layout") == "exact-vertical-candidate-stack"
        and presentation.get("review_only") is True,
        "FV candidate presentation binding/dimensions are invalid",
    )
    require(
        presentation_rows == [row for _, _, raw_rows, _ in decoded_candidates for row in raw_rows],
        "FV candidate presentation must contain every candidate's exact decoded pixels in order",
    )
    reviews = comparison.get("candidates")
    require(isinstance(reviews, list) and len(reviews) == len(candidates), "FV creative comparison must bind every candidate")
    revision_requested = comparison_outcome is not None and comparison_outcome.get("kind") == "revision-requested"
    selection_pending = phase == "fv-selection-pending" and not revision_requested
    selectionless = selection_pending or revision_requested
    selected_id = comparison.get("selected_candidate_id")
    if selection_pending:
        require(
            comparison.get("selection_status") == "pending" and selected_id is None,
            "pending comparison must keep selection status/id null",
        )
    elif revision_requested:
        require(
            comparison.get("selection_status") == "revision-requested" and selected_id is None,
            "revision-requested comparison must keep selection id null and preserve its outcome",
        )
    else:
        require(comparison.get("selection_status") == "selected", "selected comparison must declare selected status")
    selected_reviews = []
    for index, (review, candidate) in enumerate(zip(reviews, candidates), start=1):
        require(isinstance(review, dict) and set(review) == {"candidate_id", "image", "inspection"}, f"FV comparison candidate {index} fields are invalid")
        require(review.get("candidate_id") == candidate["candidate_id"] and review.get("image") == candidate["image"], f"FV comparison candidate {index} binding drift")
        is_selected = not selectionless and review["candidate_id"] == selected_id
        validate_candidate_observations(
            review.get("inspection"),
            structure_document["fv_handoff"],
            selected=is_selected,
            selection_pending=selection_pending,
            label=f"FV comparison candidate {index}",
        )
        require(review["inspection"]["render_inspection"]["input_sha256"] == candidate["image"]["sha256"], f"FV comparison candidate {index} reviewer input hash drift")
        if is_selected:
            selected_reviews.append(review)
    require(len(selected_reviews) == (0 if selectionless else 1),
            "FV creative comparison selection must match its batch-history outcome")
    selection_context = comparison.get("selection_context")
    if selectionless:
        require(selection_context is None and comparison.get("selection_approval") is None,
                "selectionless comparison must not fabricate candidate selection context or approval")
    elif isinstance(selection_context, dict) and selection_context.get("kind") == "agent-delegation-context":
        require(set(selection_context) == {"kind", "selected_candidate_id", "reason"}
                and selection_context.get("selected_candidate_id") == selected_id
                and DIRECT.nonempty_string(selection_context.get("reason")),
                "agent candidate selection must identify the exact candidate and rationale")
        delegated_path = validate_binding(comparison.get("selection_approval"), artifact_root, "agent selection receipt")
        require(load_json(delegated_path, "agent selection receipt").get("kind") == "agent-delegation-record",
                "agent selection context requires a distinct delegated receipt")
    else:
        require(
            isinstance(selection_context, dict)
            and set(selection_context) == {
                "presentation_message_id", "selection_message_id", "selected_candidate_id", "decision_text",
            }
            and DIRECT.nonempty_string(selection_context.get("presentation_message_id"))
            and DIRECT.nonempty_string(selection_context.get("selection_message_id"))
            and selection_context.get("presentation_message_id") != selection_context.get("selection_message_id")
            and selection_context.get("selected_candidate_id") == selected_id
            and DIRECT.nonempty_string(selection_context.get("decision_text"))
            and CANDIDATE_TOKEN_PATTERN.findall(selection_context.get("decision_text")) == [selected_id],
            "FV candidate selection requires an explicit candidate ID in a later user/controller message",
        )
    require(
        comparison.get("reviewer_input_image_sha256s") == [candidate["image"]["sha256"] for candidate in candidates],
        "FV creative comparison reviewer input image hashes drift",
    )
    pairs = comparison.get("material_difference_pairs")
    expected_pairs = [
        [candidates[left]["candidate_id"], candidates[right]["candidate_id"]]
        for left in range(len(candidates)) for right in range(left + 1, len(candidates))
    ]
    require(isinstance(pairs, list) and len(pairs) == len(expected_pairs), "FV creative comparison material differences are incomplete")
    for index, (pair, expected_ids) in enumerate(zip(pairs, expected_pairs), start=1):
        require(isinstance(pair, dict) and set(pair) == {"candidate_ids", "axes"} and pair.get("candidate_ids") == expected_ids, f"FV material-difference pair {index} binding is invalid")
        axes = pair.get("axes")
        require(isinstance(axes, list) and axes, f"FV material-difference pair {index} requires at least one material difference")
        for axis_index, axis in enumerate(axes, start=1):
            require(isinstance(axis, dict) and set(axis) == {"axis", "observation"} and DIRECT.nonempty_string(axis.get("axis")) and DIRECT.nonempty_string(axis.get("observation")), f"FV material-difference pair {index} axis {axis_index} is incomplete")
    require(comparison.get("validator_scope") == "bound-comparison-evidence-not-aesthetic-pixel-truth", "FV creative comparison validator_scope is invalid")
    pending_digest = comparison.get("pending_comparison_sha256")
    require(
        isinstance(pending_digest, str)
        and SHA256_PATTERN.fullmatch(pending_digest) is not None
        and pending_digest == canonical_digest(selection_neutral_projection(comparison)),
        "FV pending comparison digest does not match the selection-neutral comparison",
    )

    selection_receipt = comparison.get("selection_approval")
    if not selectionless:
        transition = state.get("fv_transition")
        require(isinstance(transition, dict), "selected FV comparison requires a frozen pending-state transition")
        selection_path = validate_binding(selection_receipt, artifact_root, "FV candidate selection approval")
        selection_subject = {
            "scope": "fv-candidate-selection",
            "structure_sha256": structure["sha256"],
            "prior_pending_state": transition["prior_pending_state"],
            "pending_comparison": transition["pending_comparison"],
            "candidate_presentation": presentation,
            "candidate_sha256s": [candidate["image"]["sha256"] for candidate in candidates],
            "pending_comparison_sha256": pending_digest,
            "selected_candidate_id": selected_id,
            "selected_sha256": selected_reviews[0]["image"]["sha256"],
            "selection_context": selection_context,
        }
        try:
            DIRECT.validate_receipt(
                selection_path,
                "lp-fv-candidate-selection",
                canonical_digest(selection_subject),
                "FV candidate selection approval",
            )
        except DIRECT.ContractError as exc:
            raise WorkflowError(str(exc)) from exc
        selection_record = load_json(selection_path, "FV candidate selection approval")
        if selection_record.get("kind") == "agent-delegation-record":
            require(selection_context.get("kind") == "agent-delegation-context", "delegated selection must not fabricate human message context")
        if selection_record.get("kind") == "conversation-approval-record":
            decision_evidence = selection_record.get("decision_evidence")
            require(
                isinstance(decision_evidence, dict)
                and decision_evidence.get("kind") == "verbatim"
                and decision_evidence.get("value") == selection_context["decision_text"],
                "FV candidate selection conversation record must preserve the exact explicit later-turn decision",
            )
    if batch["batch_number"] == 2:
        transition = state.get("fv_transition")
        require(isinstance(transition, dict), "revision batch requires a frozen batch-1 pending-state transition")
        history = state.get("fv_batch_history")
        require(isinstance(history, list) and history and isinstance(history[0], dict),
                "revision batch requires retained batch-1 history")
        batch1_pending_state = (
            transition.get("prior_pending_state")
            if transition.get("batch_number") == 1 else history[0].get("pending_state")
        )
        batch1_pending_comparison = (
            transition.get("pending_comparison")
            if transition.get("batch_number") == 1 else history[0].get("pending_comparison")
        )
        require(isinstance(batch1_pending_state, dict) and isinstance(batch1_pending_comparison, dict),
                "revision batch lost its frozen batch-1 state/comparison")
        revision_path = validate_binding(batch["revision_approval"], artifact_root, "FV revision request approval")
        revision_subject = {
            "scope": "fv-candidate-revision",
            "structure_sha256": structure["sha256"],
            "prior_pending_state": batch1_pending_state,
            "pending_comparison": batch1_pending_comparison,
            "pending_comparison_sha256": history[0].get("pending_comparison_sha256"),
            "request_context": {
                "request_message_id": batch["request_message_id"],
                "request_text": batch["request_text"],
            },
        }
        try:
            DIRECT.validate_receipt(
                revision_path,
                "lp-fv-candidate-revision",
                canonical_digest(revision_subject),
                "FV revision request approval",
            )
        except DIRECT.ContractError as exc:
            raise WorkflowError(str(exc)) from exc
        expected.add((batch["revision_approval"]["path"], "approval-receipt"))
    for candidate in candidates:
        kind = "section-image" if not selectionless and candidate["candidate_id"] == selected_id else "candidate-image"
        expected.add((candidate["image"]["path"], kind))
    expected |= source_evidence_expected
    expected.add((presentation["path"], "review-image"))
    if not selectionless:
        expected.add((selection_receipt["path"], "approval-receipt"))
    expected.add((comparison_binding["path"], "review-json"))
    if validate_batch_history:
        expected |= validate_fv_batch_history(
            state,
            artifact_root,
            structure,
            structure_document,
            structure_sections,
            phase,
            workflow_schema,
            candidates,
            comparison,
        )
    return candidates, comparison, selected_reviews[0] if selected_reviews else None, expected


def validate_fv_batch_history(
    state: dict,
    artifact_root: Path,
    structure: dict,
    structure_document: dict,
    structure_sections: list[dict],
    phase: str,
    workflow_schema: str,
    current_candidates: list[dict],
    current_comparison: dict,
) -> set[tuple[str, str]]:
    history = state["fv_batch_history"]
    current_batch_number = current_comparison["batch_context"]["batch_number"]
    state_pending_digest = state.get("fv_pending_comparison_sha256")
    require(
        isinstance(state_pending_digest, str)
        and SHA256_PATTERN.fullmatch(state_pending_digest) is not None
        and state_pending_digest == current_comparison["pending_comparison_sha256"],
        "workflow current pending comparison digest drift",
    )
    require(
        len(history) == current_batch_number and 1 <= len(history) <= 2,
        "fv_batch_history must contain ordered batch 1 and optional batch 2 exactly once",
    )
    expected: set[tuple[str, str]] = set()
    comparison_paths: set[str] = set()
    candidate_paths: set[str] = set()
    candidate_hashes: set[str] = set()
    entry_fields = {
        "batch_number", "comparison", "candidates", "pending_state", "pending_comparison",
        "pending_comparison_sha256", "outcome",
    }
    for index, entry in enumerate(history, start=1):
        require(isinstance(entry, dict) and set(entry) == entry_fields, f"fv_batch_history entry {index} fields are invalid")
        require(DIRECT.strict_int(entry.get("batch_number")) and entry.get("batch_number") == index,
                f"fv_batch_history entry {index} must preserve ordered batch_number")
        comparison_binding = entry.get("comparison")
        require(isinstance(comparison_binding, dict), f"fv_batch_history entry {index} comparison binding is invalid")
        comparison_path = comparison_binding.get("path")
        require(isinstance(comparison_path, str) and comparison_path not in comparison_paths,
                f"fv_batch_history entry {index} comparison path must be unique")
        comparison_paths.add(comparison_path)
        entry_candidates = entry.get("candidates")
        require(isinstance(entry_candidates, list), f"fv_batch_history entry {index} candidates must be an array")
        outcome = entry.get("outcome")
        require(isinstance(outcome, dict) and outcome.get("kind") in {"selection-pending", "selected", "revision-requested"},
                f"fv_batch_history entry {index} outcome is invalid")
        if outcome["kind"] == "selection-pending":
            require(
                set(outcome) == {"kind"}
                and index == current_batch_number
                and phase == "fv-selection-pending",
                "only the current pending phase may declare selection-pending",
            )
        elif outcome["kind"] == "selected":
            require(set(outcome) == {"kind", "selected_candidate_id"}
                    and CANDIDATE_ID_PATTERN.fullmatch(outcome.get("selected_candidate_id", "")) is not None,
                    f"fv_batch_history entry {index} selected outcome is invalid")
        else:
            require(set(outcome) == {"kind", "request_message_id", "request_text"}
                    and index == 1 and len(history) == 2
                    and DIRECT.nonempty_string(outcome.get("request_message_id"))
                    and DIRECT.nonempty_string(outcome.get("request_text")),
                    "only retained batch 1 may have a bound revision-requested outcome")

        if index == current_batch_number:
            require(comparison_binding == state["fv_creative_comparison"],
                    "fv_batch_history current comparison binding must equal workflow current comparison")
            require(entry_candidates == current_candidates,
                    "fv_batch_history current candidates must equal workflow current candidates")
            bound_comparison = current_comparison
        else:
            prior_state = {
                "fv_candidates": entry_candidates,
                "fv_creative_comparison": comparison_binding,
            }
            _, bound_comparison, _, prior_expected = validate_fv_candidates_and_comparison(
                prior_state,
                artifact_root,
                structure,
                structure_document,
                structure_sections,
                phase,
                workflow_schema,
                validate_batch_history=False,
                comparison_outcome=outcome,
            )
            require(bound_comparison is not None, f"fv_batch_history entry {index} comparison is missing")
            expected |= {
                (path, "candidate-image" if kind == "section-image" else kind)
                for path, kind in prior_expected
            }

        require(bound_comparison["batch_context"]["batch_number"] == index,
                f"fv_batch_history entry {index} comparison batch_number drift")
        pending_state_binding = entry.get("pending_state")
        pending_comparison_binding = entry.get("pending_comparison")
        if outcome["kind"] == "selection-pending":
            require(
                pending_state_binding is None and pending_comparison_binding == comparison_binding,
                f"fv_batch_history entry {index} current pending snapshot binding is invalid",
            )
        else:
            transition = state.get("fv_transition")
            require(
                isinstance(pending_state_binding, dict)
                and isinstance(pending_comparison_binding, dict)
                and isinstance(transition, dict),
                f"fv_batch_history entry {index} must retain its frozen pending state/comparison",
            )
            if transition.get("batch_number") == index:
                require(
                    pending_state_binding == transition.get("prior_pending_state")
                    and pending_comparison_binding == transition.get("pending_comparison"),
                    f"fv_batch_history entry {index} frozen pending transition binding drift",
                )
        require(entry.get("pending_comparison_sha256") == bound_comparison["pending_comparison_sha256"],
                f"fv_batch_history entry {index} pending comparison digest drift")
        if isinstance(pending_comparison_binding, dict):
            expected.add((pending_comparison_binding.get("path"), "review-json"))
        expected_kind = "initial" if index == 1 else "user-requested-revision"
        require(bound_comparison["batch_context"]["kind"] == expected_kind,
                f"fv_batch_history entry {index} comparison kind drift")
        if outcome["kind"] == "selection-pending":
            require(
                bound_comparison["selection_status"] == "pending"
                and bound_comparison["selected_candidate_id"] is None,
                f"fv_batch_history entry {index} pending outcome drift",
            )
        elif outcome["kind"] == "selected":
            require(bound_comparison["selected_candidate_id"] == outcome["selected_candidate_id"],
                    f"fv_batch_history entry {index} selected outcome drift")
        else:
            next_batch = current_comparison["batch_context"]
            require(next_batch["batch_number"] == 2
                    and next_batch["request_message_id"] == outcome["request_message_id"]
                    and next_batch["request_text"] == outcome["request_text"],
                    "batch 2 must bind the retained batch 1 explicit revision request exactly")
        require(bound_comparison["candidates"] == [
            {"candidate_id": candidate["candidate_id"], "image": candidate["image"],
             "inspection": review["inspection"]}
            for candidate, review in zip(entry_candidates, bound_comparison["candidates"])
        ], f"fv_batch_history entry {index} candidate/comparison binding drift")

        for candidate_index, candidate in enumerate(entry_candidates, start=1):
            require(isinstance(candidate, dict) and set(candidate) == {"candidate_id", "image"},
                    f"fv_batch_history entry {index} candidate {candidate_index} fields are invalid")
            image = candidate["image"]
            path = image.get("path") if isinstance(image, dict) else None
            digest = image.get("sha256") if isinstance(image, dict) else None
            require(isinstance(path, str) and path not in candidate_paths,
                    f"fv_batch_history candidate paths must not be overwritten or reused across batches: {path}")
            require(isinstance(digest, str) and digest not in candidate_hashes,
                    f"fv_batch_history candidate hashes must not be reused across batches: {digest}")
            candidate_paths.add(path)
            candidate_hashes.add(digest)
    return expected


def validate_fv_transition(
    state_path: Path,
    project_root: Path,
    artifact_root: Path,
    state: dict,
    phase: str,
    current_comparison: dict | None,
    prior_pending_state: Path | None,
    prior_pending_state_sha256: str | None,
    *,
    caller_anchored_snapshot: bool,
) -> None:
    """Validate the separately frozen state that preceded a selection/revision transition.

    The top-level transition input is chosen by the caller. Recursive history is
    safe to follow from a caller-anchored frozen state because changing an
    embedded binding would change that already-bound state file's bytes.
    """

    transition = state.get("fv_transition")
    if current_comparison is None:
        require(transition is None and prior_pending_state is None and prior_pending_state_sha256 is None,
                "pre-FV workflow must not declare a pending-state transition")
        return
    current_batch = current_comparison["batch_context"]["batch_number"]
    initial_pending = phase == "fv-selection-pending" and current_batch == 1
    if initial_pending:
        require(transition is None, "initial FV pending state must not self-bind a prior pending state")
        require(prior_pending_state is None and prior_pending_state_sha256 is None,
                "initial FV pending state does not accept prior pending-state inputs")
        return

    transition_fields = {"batch_number", "prior_pending_state", "pending_comparison", "pending_comparison_sha256"}
    require(isinstance(transition, dict) and set(transition) == transition_fields,
            "FV transition must bind the separately frozen prior pending state")
    require(DIRECT.strict_int(transition.get("batch_number")) and transition["batch_number"] in {1, 2},
            "FV transition batch_number is invalid")
    state_binding = transition.get("prior_pending_state")
    require(isinstance(state_binding, dict) and set(state_binding) == {"path", "sha256"},
            "FV transition prior pending state binding is invalid")
    if prior_pending_state is None:
        require(caller_anchored_snapshot, "transition validation requires --prior-pending-state")
        supplied_path = resolve_inside(project_root, state_binding.get("path"), "prior pending workflow state")
        expected_prior_sha256 = state_binding.get("sha256")
    else:
        require(
            isinstance(prior_pending_state_sha256, str)
            and SHA256_PATTERN.fullmatch(prior_pending_state_sha256) is not None,
            "transition validation requires --prior-pending-state-sha256 as 64 lowercase hex characters",
        )
        supplied_path = prior_pending_state.resolve()
        expected_prior_sha256 = prior_pending_state_sha256
        require(supplied_path.is_file(), "prior pending workflow state does not exist")
        try:
            supplied_path.relative_to(project_root)
        except ValueError as exc:
            raise WorkflowError("prior pending workflow state must stay inside project root") from exc
    require(
        isinstance(expected_prior_sha256, str)
        and SHA256_PATTERN.fullmatch(expected_prior_sha256) is not None
        and sha256(supplied_path) == expected_prior_sha256,
        "prior pending workflow state does not match the caller-supplied sha256",
    )
    if prior_pending_state is not None:
        require(
            supplied_path == resolve_inside(project_root, state_binding.get("path"), "prior pending workflow state"),
            "caller-supplied prior pending state does not match the current transition binding",
        )
    require(state_binding.get("sha256") == expected_prior_sha256,
            "current transition prior pending-state sha256 differs from the caller-supplied sha256")
    require(supplied_path != state_path, "current and prior pending workflow states must be different files")
    try:
        supplied_path.relative_to(artifact_root)
    except ValueError:
        pass
    else:
        require(False, "prior pending workflow state must be outside artifact_root")
    require(workflow_state_binding(supplied_path, project_root) == state_binding,
            "prior pending workflow state sha256/path binding mismatch")

    prior = load_json(supplied_path, "prior pending workflow state")
    require(
        prior.get("schema_version") == WORKFLOW_SCHEMA_VERSION
        and prior.get("kind") == "lp-direct-image-workflow-state"
        and prior.get("phase") == "fv-selection-pending",
        "prior transition input must be a workflow 1.5 fv-selection-pending state",
    )
    validate(
        supplied_path,
        project_root,
        prior_pending_state=None,
        prior_pending_state_sha256=None,
        _caller_anchored_snapshot=True,
    )
    prior_binding = prior.get("fv_creative_comparison")
    require(prior_binding == transition.get("pending_comparison"),
            "prior pending comparison binding drift from frozen state")
    prior_comparison_path = validate_binding(prior_binding, artifact_root, "frozen prior pending comparison")
    prior_comparison = load_json(prior_comparison_path, "frozen prior pending comparison")
    require(
        prior_comparison.get("selection_status") == "pending"
        and prior_comparison.get("selected_candidate_id") is None
        and prior_comparison.get("selection_context") is None
        and prior_comparison.get("selection_approval") is None,
        "frozen prior comparison must remain selection-neutral and pending",
    )
    require(prior_comparison["batch_context"]["batch_number"] == transition["batch_number"],
            "frozen prior pending batch drift")
    require(
        transition.get("pending_comparison_sha256") == prior_comparison.get("pending_comparison_sha256")
        == canonical_digest(selection_neutral_projection(prior_comparison)),
        "frozen prior pending comparison digest drift",
    )
    prior_history = prior.get("fv_batch_history")
    current_history = state.get("fv_batch_history")
    require(isinstance(prior_history, list) and isinstance(current_history, list),
            "FV transition batch history is invalid")
    transition_index = transition["batch_number"] - 1
    require(len(prior_history) > transition_index and len(current_history) > transition_index,
            "FV transition batch history is incomplete")
    require(current_history[:transition_index] == prior_history[:transition_index],
            "earlier FV batch history changed after the caller-supplied pending snapshot")
    prior_pending_entry = prior_history[transition_index]
    current_transition_entry = current_history[transition_index]
    require(
        current_transition_entry.get("candidates") == prior_pending_entry.get("candidates")
        and current_transition_entry.get("pending_state") == state_binding
        and current_transition_entry.get("pending_comparison") == prior_binding
        and current_transition_entry.get("pending_comparison_sha256") == prior_comparison["pending_comparison_sha256"],
        "current FV history changed the frozen presented batch",
    )
    if current_batch == transition["batch_number"]:
        require(state.get("fv_creative_comparison") != prior_binding,
                "selected/revision comparison must use a distinct path from the frozen pending comparison")
        require(
            selection_neutral_projection(current_comparison) == selection_neutral_projection(prior_comparison),
            "current FV comparison changed facts from the caller-supplied pending snapshot",
        )
    else:
        require(
            current_batch == 2 and transition["batch_number"] == 1 and phase == "fv-selection-pending",
            "only the one allowed revision may advance from frozen batch 1 to pending batch 2",
        )


def validate_section_images(
    state: dict,
    artifact_root: Path,
    structure_sections: list[dict],
    phase: str,
    workflow_schema: str,
    selected_candidate: dict | None,
    candidate_paths: set[str],
) -> tuple[list[dict], set[tuple[str, str]], list[bytes]]:
    images = state.get("section_images")
    require(isinstance(images, list), "section_images must be an array")
    if phase in {"structure-approved", "fv-selection-pending"}:
        required_count = 0
    elif phase in {"fv-review", "fv-direction-approved", "page-continuity-approved"}:
        required_count = 1
    else:
        required_count = len(structure_sections)
    require(len(images) == required_count, f"phase {phase} requires exactly {required_count} section image(s)")
    expected: set[tuple[str, str]] = set()
    combined_rows: list[bytes] = []
    seen_paths: set[str] = set()
    seen_hashes: set[str] = set()
    legacy_image_fields = {"id", "order", "path", "sha256", "width", "height", "creation_method", "browser_screenshot", "derived_from_whole_page"}
    for index, image in enumerate(images, start=1):
        if workflow_schema == LEGACY_WORKFLOW_SCHEMA_VERSION:
            require(isinstance(image, dict) and set(image) == legacy_image_fields, f"section image {index} fields are invalid")
        else:
            _, image_expected, rows = validate_new_image_descriptor(image, artifact_root, f"section image {index}")
            for expected_path, expected_kind in image_expected:
                if expected_path not in candidate_paths and expected_path not in {candidate.get("path") for candidate in images if isinstance(candidate, dict)}:
                    expected.add((expected_path, expected_kind))
        require(image.get("id") == structure_sections[index - 1].get("id")
                and DIRECT.strict_int(image.get("order")) and image.get("order") == index,
                f"section image {index} drifts from approved structure")
        value = image.get("path")
        require(isinstance(value, str) and value not in seen_paths, f"section image {index} path must be unique")
        require(not SECTION_NAME_DENY_PATTERN.search(Path(value).name), f"section image {index} looks like a screenshot/review/whole-page/crop artifact")
        path = validate_binding({"path": value, "sha256": image.get("sha256")}, artifact_root, f"section image {index}")
        width, height, _, rows = png_rows(path)
        require(width == 390
                and DIRECT.strict_int(image.get("width")) and image.get("width") == width
                and DIRECT.strict_int(image.get("height")) and image.get("height") == height,
                f"section image {index} dimensions are invalid")
        if workflow_schema == LEGACY_WORKFLOW_SCHEMA_VERSION:
            require(image.get("creation_method") in {"image-generation", "raster-composition", "user-provided"}, f"section image {index} creation_method is invalid")
        require(image.get("browser_screenshot") is False, f"section image {index} must not be a browser screenshot")
        require(image.get("derived_from_whole_page") is False, f"section image {index} must not derive from a whole-page review")
        require(image["sha256"] not in seen_hashes, f"section image {index} must be independently sourced")
        seen_paths.add(value)
        seen_hashes.add(image["sha256"])
        if workflow_schema == LEGACY_WORKFLOW_SCHEMA_VERSION or index > 1:
            expected.add((value, "section-image"))
        combined_rows.extend(rows)
    if workflow_schema == WORKFLOW_SCHEMA_VERSION and images:
        require(selected_candidate is not None and images[0] == selected_candidate["image"], "final selected FV source must equal exactly one creative-comparison candidate")
    return images, expected, combined_rows


def validate_quality_gate(gate: object, structure_schema_version: str) -> None:
    require(isinstance(gate, dict), "fv_review.quality_gate must be an object")
    fields = {"viewport_width", "five_second_test", "dominant_message", "hierarchy_and_emphasis", "density", "evidence_and_trust", "cta_hierarchy", "decision", "notes"}
    require(set(gate) == fields and DIRECT.strict_int(gate.get("viewport_width"))
            and gate.get("viewport_width") == 390,
            "fv_review.quality_gate fields/viewport are invalid")
    five = gate.get("five_second_test")
    require(isinstance(five, dict) and set(five) == {"audience", "primary_promise_or_offer", "next_action"}, "five_second_test fields are invalid")
    require(all(value == "pass" for value in five.values()), "five_second_test must pass")
    require(all(gate.get(key) == "pass" for key in ("dominant_message", "hierarchy_and_emphasis", "evidence_and_trust", "cta_hierarchy", "decision")), "FV quality gate must pass")
    if structure_schema_version == DIRECT.LEGACY_STRUCTURE_SCHEMA_VERSION:
        require(gate.get("density") == "balanced", "FV density must be balanced")
    else:
        require(gate.get("density") == "pass", "new-schema FV density outcome must pass")
    require(isinstance(gate.get("notes"), str) and gate["notes"].strip(), "FV quality gate notes are required")


def validate_fv_outcome_review_1_2(
    review_json: dict,
    artifact_root: Path,
    structure: dict,
    structure_document: dict,
    source_fv: dict,
    shown_artifact: dict,
    quality_gate: dict,
) -> set[tuple[str, str]]:
    fields = {
        "kind", "schema_version", "structure_sha256", "fv_handoff", "fv_handoff_sha256",
        "source_fv", "shown_presentation", "quality_gate_sha256", "outcomes", "outcome_results",
        "generic_substitution_risk", "action_presentation", "validator_scope",
    }
    require(set(review_json) == fields, "FV outcome review fields are invalid")
    require(
        review_json.get("kind") == "lp-fv-outcome-review" and review_json.get("schema_version") == "1.2",
        "FV outcome review type is invalid",
    )
    require(review_json.get("structure_sha256") == structure["sha256"], "FV outcome review structure hash drift")
    handoff = structure_document["fv_handoff"]
    require(review_json.get("fv_handoff") == handoff, "FV outcome review fv_handoff content drift")
    require(review_json.get("fv_handoff_sha256") == canonical_digest(handoff), "FV outcome review fv_handoff digest drift")
    require(review_json.get("source_fv") == source_fv, "FV outcome review source FV binding drift")
    require(review_json.get("quality_gate_sha256") == canonical_digest(quality_gate), "FV outcome review quality gate digest drift")
    require(review_json.get("outcomes") == handoff, "FV outcome review copied outcomes drift")

    results = review_json.get("outcome_results")
    result_fields = {
        "five_second", "dominant_message", "belief_shift", "visual_job", "credibility",
        "identity_recognition", "avoid_impressions",
    }
    require(isinstance(results, dict) and set(results) == result_fields, "FV outcome_results fields are invalid")
    five_results = results.get("five_second")
    require(
        isinstance(five_results, dict)
        and set(five_results) == {"audience", "promise_or_offer", "next_action"}
        and all(value == "pass" for value in five_results.values()),
        "FV five-second outcome results must pass",
    )
    require(
        all(results.get(key) == "pass" for key in result_fields - {"five_second"}),
        "every FV handoff outcome must pass",
    )
    require(review_json.get("generic_substitution_risk") == "pass", "FV generic substitution risk must pass")
    require(
        review_json.get("validator_scope") == "declared-outcome-review-not-pixel-truth",
        "FV outcome review validator_scope is invalid",
    )

    presentation = review_json.get("shown_presentation")
    presentation_fields = {"path", "sha256", "width", "height", "review_only"}
    require(isinstance(presentation, dict) and set(presentation) == presentation_fields, "FV shown presentation fields are invalid")
    require(
        shown_artifact == {"path": presentation.get("path"), "sha256": presentation.get("sha256")},
        "fv_review shown_artifact must equal the reviewed 390px presentation",
    )
    presentation_path = validate_binding(
        {"path": presentation.get("path"), "sha256": presentation.get("sha256")},
        artifact_root,
        "FV shown presentation",
    )
    try:
        width, height = DIRECT.validate_png(presentation_path)
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    require(width == 390
            and DIRECT.strict_int(presentation.get("width")) and presentation.get("width") == width
            and DIRECT.strict_int(presentation.get("height")) and presentation.get("height") == height,
            "FV shown presentation dimensions are invalid")

    action = review_json.get("action_presentation")
    action_fields = {"status", "method", "visible_action_label", "supporting_state"}
    require(isinstance(action, dict) and set(action) == action_fields, "FV action_presentation fields are invalid")
    require(action.get("status") == "complete", "FV action presentation must be complete")
    require(action.get("method") in {"source-image", "review-only-runtime-overlay"}, "FV action presentation method is invalid")
    expected_label = handoff["five_second"]["next_action"]
    require(DIRECT.meaningful_action_label(action.get("visible_action_label")), "FV visible action label must be meaningful")
    require(action.get("visible_action_label") == expected_label, "FV visible action label must exactly equal approved next_action")
    supporting_state = action.get("supporting_state")
    require(supporting_state is None or DIRECT.nonempty_string(supporting_state), "FV action supporting_state must be null or a non-empty string")

    if action["method"] == "source-image":
        require(
            presentation.get("path") == source_fv["path"]
            and presentation.get("sha256") == source_fv["sha256"]
            and presentation.get("review_only") is False,
            "source-image action presentation must show the exact source FV",
        )
        return set()
    require(
        presentation.get("path") != source_fv["path"]
        and presentation.get("sha256") != source_fv["sha256"]
        and presentation.get("review_only") is True,
        "runtime-overlay action requires a separate review-only 390px presentation",
    )
    return {(presentation["path"], "review-image")}


def validate_fv_outcome_review_1_4(
    review_json: dict,
    artifact_root: Path,
    structure: dict,
    structure_document: dict,
    source_fv: dict,
    shown_artifact: dict,
    quality_gate: dict,
    comparison_binding: dict,
    selected_comparison: dict,
) -> set[tuple[str, str]]:
    fields = {
        "kind", "schema_version", "structure_sha256", "fv_handoff", "fv_handoff_sha256",
        "fv_content_budget", "fv_content_budget_sha256", "content_budget_observation",
        "creative_comparison", "selected_candidate_id", "selected_observations", "source_fv",
        "shown_presentation", "quality_gate_sha256", "outcomes", "outcome_results",
        "generic_substitution_risk", "action_presentation", "validator_scope",
    }
    require(set(review_json) == fields, "FV outcome review fields are invalid")
    require(review_json.get("kind") == "lp-fv-outcome-review" and review_json.get("schema_version") == "1.4", "FV outcome review type is invalid")
    require(review_json.get("structure_sha256") == structure["sha256"], "FV outcome review structure hash drift")
    handoff = structure_document["fv_handoff"]
    require(review_json.get("fv_handoff") == handoff, "FV outcome review fv_handoff content drift")
    require(review_json.get("fv_handoff_sha256") == canonical_digest(handoff), "FV outcome review fv_handoff digest drift")
    budget = handoff["fv_content_budget"]
    require(review_json.get("fv_content_budget") == budget, "FV outcome review content budget drift")
    require(review_json.get("fv_content_budget_sha256") == canonical_digest(budget), "FV outcome review content budget digest drift")
    require(review_json.get("creative_comparison") == comparison_binding, "FV outcome review creative comparison binding drift")
    require(review_json.get("selected_candidate_id") == selected_comparison["candidate_id"], "FV outcome review selected candidate drift")
    require(review_json.get("selected_observations") == selected_comparison["inspection"], "FV outcome review selected observations drift")
    require(review_json.get("content_budget_observation") == selected_comparison["inspection"]["content_budget_observation"],
            "FV outcome review selected content-budget observation drift")
    require(review_json.get("source_fv") == source_fv == selected_comparison["image"], "FV outcome review source/selected FV binding drift")
    require(review_json.get("quality_gate_sha256") == canonical_digest(quality_gate), "FV outcome review quality gate digest drift")
    require(review_json.get("outcomes") == handoff, "FV outcome review copied outcomes drift")
    result_fields = {
        "five_second", "dominant_message", "belief_shift", "visual_job", "credibility",
        "identity_recognition", "provider_recognition", "avoid_impressions",
        "fv_content_budget", "context_assessment", "scan_contract",
    }
    results = review_json.get("outcome_results")
    require(isinstance(results, dict) and set(results) == result_fields, "FV outcome_results fields are invalid")
    five = results.get("five_second")
    require(isinstance(five, dict) and set(five) == {"audience", "promise_or_offer", "next_action"} and all(value == "pass" for value in five.values()), "FV five-second outcome results must pass")
    require(all(results.get(key) == "pass" for key in result_fields - {"five_second"}), "every FV handoff outcome must pass")
    require(review_json.get("generic_substitution_risk") == "pass", "FV generic substitution risk must pass")

    presentation = review_json.get("shown_presentation")
    presentation_fields = {"path", "sha256", "width", "height", "review_only"}
    require(isinstance(presentation, dict) and set(presentation) == presentation_fields, "FV shown presentation fields are invalid")
    require(
        presentation == {
            "path": source_fv["path"], "sha256": source_fv["sha256"], "width": source_fv["width"],
            "height": source_fv["height"], "review_only": False,
        }
        and shown_artifact == {"path": source_fv["path"], "sha256": source_fv["sha256"]},
        "schema 1.4 source/shown/selected FV must agree exactly",
    )
    presentation_path = validate_binding({"path": presentation["path"], "sha256": presentation["sha256"]}, artifact_root, "FV shown presentation")
    width, height = DIRECT.validate_png(presentation_path)
    require(DIRECT.strict_int(presentation.get("width")) and DIRECT.strict_int(presentation.get("height"))
            and width == presentation["width"] == 390 and height == presentation["height"],
            "FV shown presentation dimensions are invalid")

    action = review_json.get("action_presentation")
    require(
        isinstance(action, dict)
        and set(action) == {"status", "method", "visible_action_label", "runtime_overlay_policy"}
        and action.get("status") == "complete"
        and action.get("method") == "source-image"
        and action.get("visible_action_label") == handoff["five_second"]["next_action"]
        and action.get("runtime_overlay_policy") == "transparent-hit-area-over-baked-control",
        "schema 1.4 action must be complete in the selected source image",
    )
    require(DIRECT.meaningful_action_label(action["visible_action_label"]), "FV visible action label must be meaningful")
    require(review_json.get("validator_scope") == "bound-review-evidence-not-aesthetic-pixel-truth", "FV outcome review validator_scope is invalid")
    return set()


def validate_fv_review(
    state: dict,
    artifact_root: Path,
    structure: dict,
    structure_document: dict,
    images: list[dict],
    phase: str,
    workflow_schema: str,
    comparison_binding: dict | None,
    selected_comparison: dict | None,
) -> set[tuple[str, str]]:
    review = state.get("fv_review")
    if phase in {"structure-approved", "fv-selection-pending"}:
        require(review is None, "fv_review is forbidden before fv-review")
        return set()
    require(isinstance(review, dict), "fv_review must be an object")
    require(set(review) == {"scope", "shown_artifact", "review_artifact", "quality_gate", "approval_receipt"}, "fv_review fields are invalid")
    require(review.get("scope") == "fv-only", "fv_review scope must be fv-only")
    shown = review.get("shown_artifact")
    require(isinstance(shown, dict) and set(shown) == {"path", "sha256"}, "fv_review shown_artifact binding is invalid")
    review_path = validate_binding(review.get("review_artifact"), artifact_root, "FV review artifact")
    require(review_path.suffix.lower() == ".json", "FV review artifact must be JSON, not an image or screenshot")
    structure_schema = structure_document.get("schema_version")
    validate_quality_gate(review.get("quality_gate"), structure_schema)
    expected = {(review["review_artifact"]["path"], "review-json")}
    if structure_schema == DIRECT.LEGACY_STRUCTURE_SCHEMA_VERSION:
        require(shown == {"path": images[0]["path"], "sha256": images[0]["sha256"]}, "fv_review shown_artifact must be the FV section image")
    else:
        review_json = load_json(review_path, "FV outcome review artifact")
        if structure_schema == DIRECT.STRUCTURE_SCHEMA_VERSION:
            require(workflow_schema == WORKFLOW_SCHEMA_VERSION, "schema 1.5 structure requires workflow schema 1.5")
            require(isinstance(comparison_binding, dict) and isinstance(selected_comparison, dict), "schema 1.5 FV review requires creative comparison")
            expected |= validate_fv_outcome_review_1_4(
                review_json, artifact_root, structure, structure_document, images[0], shown,
                review["quality_gate"], comparison_binding, selected_comparison,
            )
        else:
            expected |= validate_fv_outcome_review_1_2(
                review_json, artifact_root, structure, structure_document, images[0], shown, review["quality_gate"],
            )
    receipt = review.get("approval_receipt")
    if phase == "fv-review":
        require(receipt is None, "FV approval receipt is forbidden during fv-review")
    else:
        receipt_path = validate_binding(receipt, artifact_root, "FV approval receipt")
        subject = {"scope": "fv-only", "structure": structure, "fv_image": images[0], "review_artifact": review["review_artifact"], "quality_gate": review["quality_gate"]}
        if structure_schema in {"1.2", "1.3", DIRECT.STRUCTURE_SCHEMA_VERSION}:
            subject["shown_artifact"] = shown
        if structure_schema == DIRECT.STRUCTURE_SCHEMA_VERSION:
            subject["creative_comparison"] = comparison_binding
        try:
            DIRECT.validate_receipt(receipt_path, "lp-fv-direction", canonical_digest(subject), "FV approval receipt")
        except DIRECT.ContractError as exc:
            raise WorkflowError(str(exc)) from exc
        expected.add((receipt["path"], "approval-receipt"))
    return expected


def validate_page_continuity(
    state: dict,
    artifact_root: Path,
    structure: dict,
    boundaries: list[dict],
    series: list[dict],
    phase: str,
) -> tuple[dict | None, set[tuple[str, str]]]:
    continuity = state.get("page_continuity")
    if not phase_at_least(phase, "page-continuity-approved"):
        require(continuity is None, "page_continuity is forbidden before FV direction approval")
        return None, set()
    require(
        isinstance(continuity, dict)
        and set(continuity) == {"plan", "approval_receipt"},
        "page_continuity fields are invalid",
    )
    plan_path = validate_binding(continuity.get("plan"), artifact_root, "page continuity plan")
    plan = load_json(plan_path, "page continuity plan")
    try:
        DIRECT.validate_continuity_plan(plan, structure["sha256"], boundaries, series)
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    receipt_path = validate_binding(continuity.get("approval_receipt"), artifact_root, "page continuity approval receipt")
    subject = {"scope": "page-continuity", "structure": structure, "plan": continuity["plan"]}
    try:
        DIRECT.validate_receipt(receipt_path, "lp-page-continuity", canonical_digest(subject), "page continuity approval receipt")
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    return continuity, {
        (continuity["plan"]["path"], "continuity-plan"),
        (continuity["approval_receipt"]["path"], "approval-receipt"),
    }


def validate_whole_page(
    state: dict,
    artifact_root: Path,
    continuity: dict | None,
    continuity_plan: dict | None,
    structure_sections: list[dict],
    structure_document: dict,
    images: list[dict],
    combined_rows: list[bytes],
    phase: str,
) -> tuple[dict | None, set[tuple[str, str]]]:
    review = state.get("whole_page_review")
    if not phase_at_least(phase, "whole-page-reviewed"):
        require(review is None, "whole_page_review is forbidden before sections are complete")
        return None, set()
    require(continuity is not None, "whole-page review requires approved page continuity")
    require(continuity_plan is not None, "whole-page review requires a bound page continuity plan")
    fields = {"composite", "review_artifact"}
    require(isinstance(review, dict) and set(review) == fields, "whole_page_review fields are invalid")
    composite = review.get("composite")
    composite_fields = {"path", "sha256", "width", "height", "derived_from_section_sha256s", "review_only", "design_source"}
    require(isinstance(composite, dict) and set(composite) == composite_fields, "whole-page composite fields are invalid")
    path = validate_binding({"path": composite.get("path"), "sha256": composite.get("sha256")}, artifact_root, "whole-page composite")
    width, height, _, rows = png_rows(path)
    require(width == 390
            and DIRECT.strict_int(composite.get("width")) and composite.get("width") == width
            and DIRECT.strict_int(composite.get("height")) and composite.get("height") == height,
            "whole-page composite dimensions are invalid")
    require(height == sum(image["height"] for image in images), "whole-page review height must equal section heights")
    require(composite.get("derived_from_section_sha256s") == [image["sha256"] for image in images], "whole-page review source digest order is invalid")
    require(composite.get("review_only") is True and composite.get("design_source") is False, "whole-page composite must be review-only and never a design source")
    require(rows == combined_rows, "whole-page review must be the exact vertical composite of section images")
    review_path = validate_binding(review.get("review_artifact"), artifact_root, "whole-page review artifact")
    review_json = load_json(review_path, "whole-page review artifact")
    try:
        DIRECT.validate_whole_page_review(
            review_json,
            continuity["plan"]["sha256"],
            continuity_plan,
            structure_sections,
            [image["sha256"] for image in images],
            structure_document["fv_handoff"] if structure_document.get("schema_version") == DIRECT.STRUCTURE_SCHEMA_VERSION else None,
            structure_document.get("authentic_proof"),
            structure_document.get("cta_strategy"),
        )
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    return review, {(composite["path"], "review-image"), (review["review_artifact"]["path"], "review-json")}


def validate_manifest(state: dict, artifact_root: Path, continuity: dict | None, whole_page: dict | None, phase: str) -> tuple[dict | None, set[tuple[str, str]]]:
    binding = state.get("final_manifest")
    if not phase_at_least(phase, "assembly-approved"):
        require(binding is None, "final_manifest is forbidden before assembly approval")
        return None, set()
    path = validate_binding(binding, artifact_root, "final manifest")
    try:
        DIRECT.validate(path, artifact_root)
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    manifest = load_json(path, "final manifest")
    require(continuity is not None and whole_page is not None, "final manifest requires approved continuity and whole-page review")
    expected_continuity = {
        "page_continuity_plan": continuity["plan"],
        "page_continuity_approval": continuity["approval_receipt"],
        "whole_page_review": whole_page["review_artifact"],
        "whole_page_composite": {key: whole_page["composite"][key] for key in ("path", "sha256")},
    }
    require(manifest.get("continuity") == expected_continuity, "final manifest continuity binding drift")
    receipt = manifest.get("assembly_approval", {}).get("receipt")
    require(isinstance(receipt, dict), "final manifest assembly receipt is invalid")
    return manifest, {(binding["path"], "manifest"), (receipt.get("path"), "approval-receipt")}


def validate_runtime_assembly(
    state: dict,
    artifact_root: Path,
    manifest: dict | None,
    phase: str,
    runtime_probe: LiveRuntimeProbe | None,
) -> set[tuple[str, str]]:
    runtime = state.get("runtime_assembly")
    if phase != "assembled":
        require(runtime is None, "runtime_assembly is forbidden before assembled")
        return set()
    require(manifest is not None, "assembled phase requires a validated final manifest")
    fields = {"base_origin", "route", "manifest", "source_files", "runtime_mapping", "browser_qa", "approval_receipt"}
    require(isinstance(runtime, dict) and set(runtime) == fields, "runtime_assembly fields are invalid")
    base_origin = validate_base_origin(runtime.get("base_origin"))
    route = validate_runtime_route(runtime.get("route"), base_origin)
    require(runtime.get("manifest") == state.get("final_manifest"), "runtime_assembly manifest binding drift")

    source_files = runtime.get("source_files")
    require(isinstance(source_files, list) and source_files, "assembled phase requires bound runtime source files")
    source_values: list[str] = []
    source_bindings: list[dict] = []
    seen: set[str] = set()
    expected: set[tuple[str, str]] = set()
    for index, binding in enumerate(source_files, start=1):
        path = validate_binding(binding, artifact_root, f"runtime source {index}")
        value = binding["path"]
        require(value not in seen, f"runtime source {index} path must be unique")
        require(path.suffix.lower() in CODE_SUFFIXES, f"runtime source {index} must use a code extension")
        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise WorkflowError(f"runtime source {index} must be UTF-8 text") from exc
        require(source.strip(), f"runtime source {index} must not be blank")
        seen.add(value)
        source_values.append(source)
        source_bindings.append(binding)
        expected.add((value, "runtime-code"))

    image_paths = [section["image"]["path"] for section in manifest["sections"]]

    mapping_path = validate_binding(runtime.get("runtime_mapping"), artifact_root, "runtime mapping")
    mapping = load_json(mapping_path, "runtime mapping")
    mapping_fields = {"kind", "schema_version", "manifest_sha256", "base_origin", "route", "source_files", "sections"}
    require(isinstance(mapping, dict) and set(mapping) == mapping_fields, "runtime mapping fields are invalid")
    require(mapping.get("kind") == "lp-runtime-assembly-map" and mapping.get("schema_version") == "1.2", "runtime mapping type is invalid")
    require(mapping.get("manifest_sha256") == state["final_manifest"]["sha256"], "runtime mapping manifest hash drift")
    require(mapping.get("base_origin") == base_origin, "runtime mapping base_origin drift")
    require(mapping.get("route") == route and mapping.get("source_files") == source_bindings, "runtime mapping route/source binding drift")
    mapped_sections = mapping.get("sections")
    require(isinstance(mapped_sections, list) and len(mapped_sections) == len(manifest["sections"]), "runtime mapping must cover every manifest section")
    for index, (mapped, section) in enumerate(zip(mapped_sections, manifest["sections"]), start=1):
        require(
            isinstance(mapped, dict)
            and set(mapped) == {"id", "order", "image_path", "source_file_path"},
            f"runtime mapping section {index} fields are invalid",
        )
        require(
            mapped.get("id") == section["id"]
            and DIRECT.strict_int(mapped.get("order")) and mapped.get("order") == index
            and mapped.get("image_path") == section["image"]["path"],
            f"runtime mapping section {index} drifts from manifest",
        )
        require(mapped.get("source_file_path") in seen, f"runtime mapping section {index} source file is unbound")
        source_index = [binding["path"] for binding in source_bindings].index(mapped["source_file_path"])
        require(mapped["image_path"] in source_values[source_index], f"runtime mapping section {index} image path is absent from bound source")
    expected.add((runtime["runtime_mapping"]["path"], "runtime-map"))

    qa_path = validate_binding(runtime.get("browser_qa"), artifact_root, "runtime browser QA")
    qa = load_json(qa_path, "runtime browser QA")
    qa_fields = {"kind", "schema_version", "manifest_sha256", "base_origin", "route", "viewports", "validator_scope"}
    require(isinstance(qa, dict) and set(qa) == qa_fields, "runtime browser QA fields are invalid")
    require(qa.get("kind") == "lp-runtime-browser-qa" and qa.get("schema_version") == "1.2", "runtime browser QA type is invalid")
    require(qa.get("manifest_sha256") == state["final_manifest"]["sha256"], "runtime browser QA manifest hash drift")
    require(qa.get("base_origin") == base_origin, "runtime browser QA base_origin drift")
    require(qa.get("route") == route, "runtime browser QA route drift")
    require(qa.get("validator_scope") == "bound-evidence-not-live-browser-truth", "runtime browser QA validator_scope is invalid")
    viewports = qa.get("viewports")
    require(isinstance(viewports, list)
            and all(isinstance(item, dict) and DIRECT.strict_int(item.get("width")) for item in viewports)
            and [item["width"] for item in viewports] == [320, 390, 430],
            "runtime browser QA must cover 320/390/430 in order")
    viewport_fields = {
        "width", "result", "dom_image_order", "served_image_sha256s", "no_gaps", "no_overflow",
        "overlays", "accessibility", "direct_call",
    }
    image_hashes = [section["image"]["sha256"] for section in manifest["sections"]]
    for item in viewports:
        require(isinstance(item, dict) and set(item) == viewport_fields, "runtime browser QA viewport fields are invalid")
        require(item.get("result") == "pass", f"runtime browser QA viewport {item.get('width')} must pass")
        require(item.get("dom_image_order") == image_paths, f"runtime browser QA viewport {item.get('width')} DOM image order drift")
        require(item.get("served_image_sha256s") == image_hashes, f"runtime browser QA viewport {item.get('width')} served image hash drift")
        require(item.get("no_gaps") is True and item.get("no_overflow") is True, f"runtime browser QA viewport {item.get('width')} gap/overflow check failed")
        require(item.get("overlays") == "pass" and item.get("accessibility") == "pass", f"runtime browser QA viewport {item.get('width')} overlay/accessibility check failed")
        expected_call = "pass" if manifest["structure"] and any(
            overlay.get("action_role") == "secondary-direct-call"
            for section in manifest["sections"] for overlay in section["overlays"]
        ) else "not-applicable"
        require(item.get("direct_call") == expected_call,
                f"runtime browser QA viewport {item.get('width')} direct-call result drift")
    expected.add((runtime["browser_qa"]["path"], "runtime-qa"))
    receipt_path = validate_binding(runtime.get("approval_receipt"), artifact_root, "runtime assembly approval receipt")
    subject = {
        "scope": "runtime-assembly",
        "manifest": runtime["manifest"],
        "base_origin": base_origin,
        "route": route,
        "source_files": source_bindings,
        "runtime_mapping": runtime["runtime_mapping"],
        "browser_qa": runtime["browser_qa"],
    }
    try:
        DIRECT.validate_receipt(
            receipt_path,
            "lp-runtime-assembly",
            canonical_digest(subject),
            "runtime assembly approval receipt",
        )
    except DIRECT.ContractError as exc:
        raise WorkflowError(str(exc)) from exc
    expected.add((runtime["approval_receipt"]["path"], "approval-receipt"))
    require(callable(runtime_probe), "assembled phase requires an injected live runtime probe")
    try:
        live_result = runtime_probe(manifest, base_origin, route)
    except WorkflowError:
        raise
    except Exception as exc:
        raise WorkflowError(f"live runtime probe failed: {exc}") from exc
    require(isinstance(live_result, dict), "live runtime probe must return a JSON object")
    require(live_result == qa, "live runtime probe result drift from bound runtime browser QA")
    return expected


def validate(
    state_path: Path,
    project_root: Path,
    *,
    runtime_probe: LiveRuntimeProbe | None = None,
    legacy_read_only: bool = False,
    prior_pending_state: Path | None = None,
    prior_pending_state_sha256: str | None = None,
    _caller_anchored_snapshot: bool = False,
) -> None:
    project_root = project_root.resolve()
    state_path = state_path.resolve()
    require(project_root.is_dir(), "project root must be a directory")
    state = load_json(state_path, "workflow state")
    workflow_schema = state.get("schema_version")
    expected_fields = {"schema_version", "kind", "phase", "design_mode", "artifact_root", "structure", "section_images", "fv_review", "page_continuity", "whole_page_review", "final_manifest", "runtime_assembly", "artifact_ledger"}
    if workflow_schema in {"1.2", "1.3", "1.4", WORKFLOW_SCHEMA_VERSION}:
        expected_fields |= {"fv_candidates", "fv_creative_comparison"}
    if workflow_schema in {"1.3", "1.4", WORKFLOW_SCHEMA_VERSION}:
        expected_fields.add("fv_batch_history")
    if workflow_schema in {"1.4", WORKFLOW_SCHEMA_VERSION}:
        expected_fields |= {"fv_pending_comparison_sha256", "fv_transition"}
    require(set(state) == expected_fields, "workflow state fields are invalid")
    require(workflow_schema in READ_ONLY_WORKFLOW_SCHEMA_VERSIONS | {WORKFLOW_SCHEMA_VERSION} and state.get("kind") == "lp-direct-image-workflow-state", "workflow state type is invalid")
    phase = state.get("phase")
    require(phase in PHASES, "workflow phase is invalid")
    if workflow_schema in READ_ONLY_WORKFLOW_SCHEMA_VERSIONS:
        require(legacy_read_only, "legacy workflow schemas require explicit --legacy-read-only archive inspection")
        require(
            phase == "structure-approved"
            and state.get("section_images") == []
            and state.get("fv_candidates", []) == []
            and state.get("fv_creative_comparison") is None
            and state.get("fv_batch_history", []) == []
            and state.get("fv_review") is None
            and state.get("page_continuity") is None
            and state.get("whole_page_review") is None
            and state.get("final_manifest") is None
            and state.get("runtime_assembly") is None,
            "legacy read-only mode cannot authorize phase progression or assembly",
        )
    else:
        require(not legacy_read_only, "--legacy-read-only accepts legacy archives only")
        require(
            (state.get("fv_pending_comparison_sha256") is None)
            if phase == "structure-approved"
            else (
                isinstance(state.get("fv_pending_comparison_sha256"), str)
                and SHA256_PATTERN.fullmatch(state["fv_pending_comparison_sha256"]) is not None
            ),
            "workflow pending comparison digest must be null only before candidate presentation",
        )
    require(state.get("design_mode") == "direct-finished-section-images", "design_mode is invalid")
    artifact_root = resolve_inside(project_root, state.get("artifact_root"), "artifact_root", directory=True)
    try:
        state_path.relative_to(artifact_root)
    except ValueError:
        pass
    else:
        require(False, "workflow state file must be outside dedicated artifact_root")

    ledger = validate_ledger(state, artifact_root, allow_later_artifacts=_caller_anchored_snapshot)
    structure, structure_document, structure_sections, boundaries, series, expected = validate_structure(
        state, artifact_root, workflow_schema,
    )
    structure_schema = structure_document.get("schema_version")
    if workflow_schema == WORKFLOW_SCHEMA_VERSION:
        require(structure_schema == DIRECT.STRUCTURE_SCHEMA_VERSION, "current workflow schema is only for the current structure schema")
    elif workflow_schema in {"1.3", "1.4"}:
        require(structure_schema == "1.4", "archived workflow schema 1.3/1.4 requires structure schema 1.4")
    else:
        require(structure_schema in DIRECT.READ_ONLY_STRUCTURE_SCHEMA_VERSIONS, "current structure schema requires current workflow schema")
    candidates, comparison, selected_comparison, comparison_expected = validate_fv_candidates_and_comparison(
        state, artifact_root, structure, structure_document, structure_sections, phase, workflow_schema,
    )
    expected |= comparison_expected
    if workflow_schema == WORKFLOW_SCHEMA_VERSION:
        validate_fv_transition(
            state_path,
            project_root,
            artifact_root,
            state,
            phase,
            comparison,
            prior_pending_state,
            prior_pending_state_sha256,
            caller_anchored_snapshot=_caller_anchored_snapshot,
        )
    else:
        require(prior_pending_state is None and prior_pending_state_sha256 is None,
                "legacy workflows do not accept prior pending-state inputs")
    images, section_expected, combined_rows = validate_section_images(
        state, artifact_root, structure_sections, phase, workflow_schema, selected_comparison,
        {candidate["image"]["path"] for candidate in candidates},
    )
    expected |= section_expected
    expected |= validate_fv_review(
        state, artifact_root, structure, structure_document, images, phase, workflow_schema,
        state.get("fv_creative_comparison"), selected_comparison,
    )
    continuity, continuity_expected = validate_page_continuity(state, artifact_root, structure, boundaries, series, phase)
    expected |= continuity_expected
    continuity_plan = load_json(
        resolve_inside(artifact_root, continuity["plan"]["path"], "page continuity plan"),
        "page continuity plan",
    ) if continuity is not None else None
    whole_page, whole_expected = validate_whole_page(
        state, artifact_root, continuity, continuity_plan, structure_sections, structure_document,
        images, combined_rows, phase
    )
    expected |= whole_expected
    manifest, manifest_expected = validate_manifest(state, artifact_root, continuity, whole_page, phase)
    expected |= manifest_expected
    expected |= validate_runtime_assembly(state, artifact_root, manifest, phase, runtime_probe)

    expected_map = {path: kind for path, kind in expected}
    if phase != "assembled":
        require(
            not any(kind in {"runtime-code", "runtime-map", "runtime-qa"} for kind in ledger.values()),
            "runtime artifacts are forbidden before assembled",
        )
    require(ledger == expected_map, "artifact_ledger kinds must exactly match workflow-bound artifacts")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("state", type=Path)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--runtime-base-url")
    parser.add_argument("--prior-pending-state", type=Path)
    parser.add_argument("--prior-pending-state-sha256")
    parser.add_argument("--legacy-read-only", action="store_true")
    args = parser.parse_args()
    try:
        state = load_json(args.state.resolve(), "workflow state")
        if state.get("schema_version") in READ_ONLY_WORKFLOW_SCHEMA_VERSIONS:
            validate(args.state, args.project_root, legacy_read_only=args.legacy_read_only)
            print("OK: legacy structure-approved archive is readable; progression and assembly are not authorized")
            return 0
        runtime_probe: LiveRuntimeProbe | None = None
        if state.get("phase") == "assembled":
            require(
                isinstance(args.runtime_base_url, str) and bool(args.runtime_base_url.strip()),
                "assembled phase requires --runtime-base-url",
            )
            runtime = state.get("runtime_assembly")
            require(isinstance(runtime, dict), "assembled phase requires runtime_assembly")
            approved_origin = validate_base_origin(runtime.get("base_origin"))
            supplied_origin = validate_base_origin(args.runtime_base_url)
            require(supplied_origin == approved_origin, "--runtime-base-url must equal approved runtime base_origin")
            project_root = args.project_root.resolve()
            artifact_root = resolve_inside(project_root, state.get("artifact_root"), "artifact_root", directory=True)
            manifest_binding = state.get("final_manifest")
            require(isinstance(manifest_binding, dict), "assembled phase requires final_manifest")
            manifest_path = resolve_inside(artifact_root, manifest_binding.get("path"), "final_manifest.path")
            probe_script = Path(__file__).with_name("probe_runtime.mjs")

            def run_live_probe(_manifest: dict, base_origin: str, route: str) -> dict:
                command = [
                    "node", str(probe_script),
                    "--base-origin", base_origin,
                    "--route", route,
                    "--manifest", str(manifest_path),
                ]
                try:
                    completed = subprocess.run(
                        command,
                        cwd=project_root,
                        capture_output=True,
                        text=True,
                        timeout=120,
                        check=False,
                    )
                except (OSError, subprocess.TimeoutExpired) as exc:
                    raise WorkflowError(f"live runtime probe could not execute: {exc}") from exc
                if completed.returncode != 0:
                    detail = completed.stderr.strip() or completed.stdout.strip() or "unknown probe error"
                    raise WorkflowError(f"live runtime probe failed: {detail}")
                try:
                    result = json.loads(completed.stdout)
                except json.JSONDecodeError as exc:
                    raise WorkflowError("live runtime probe returned invalid JSON") from exc
                require(isinstance(result, dict), "live runtime probe must return a JSON object")
                return result

            runtime_probe = run_live_probe
        validate(
            args.state,
            args.project_root,
            runtime_probe=runtime_probe,
            legacy_read_only=args.legacy_read_only,
            prior_pending_state=args.prior_pending_state,
            prior_pending_state_sha256=args.prior_pending_state_sha256,
        )
    except WorkflowError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("OK: phased direct-image workflow state is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
