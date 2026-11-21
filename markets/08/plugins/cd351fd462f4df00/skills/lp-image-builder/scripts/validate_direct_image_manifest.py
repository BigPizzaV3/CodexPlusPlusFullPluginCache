#!/usr/bin/env python3
"""Read-only validator for the public direct-section-image LP contract."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import struct
import sys
import unicodedata
import zlib
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ALLOWED_OVERLAYS = {"cta", "form", "map", "accordion", "video", "link"}
BOUNDARY_MECHANISMS = {"visual", "layout", "open-loop", "contrast", "copy", "mixed"}
STRUCTURE_SCHEMA_VERSION = "1.6"
MODERN_STRUCTURE_SCHEMA_VERSIONS = {"1.5", STRUCTURE_SCHEMA_VERSION}
READ_ONLY_STRUCTURE_SCHEMA_VERSIONS = {"1.1", "1.2", "1.3", "1.4", "1.5"}
LEGACY_STRUCTURE_SCHEMA_VERSION = "1.1"
MANIFEST_SCHEMA_VERSION = "1.2"
STEP_LABEL_PATTERN = re.compile(r"\bSTEP\s*[-_#:：]?\s*\d+\b", re.IGNORECASE)
FV_ITEM_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FV_SEMANTIC_ROLES = {
    "audience", "dominant", "support", "provider", "proof", "action",
    "secondary-action", "availability",
}
FV_VISUAL_WEIGHTS = {"primary", "supporting", "micro"}
FV_CONTENT_BUDGETS = {
    "lean": {"max_chars": 90, "max_items": 5, "max_proofs": 1},
    "standard": {"max_chars": 140, "max_items": 7, "max_proofs": 2},
    "reassurance-heavy": {"max_chars": 180, "max_items": 8, "max_proofs": 3},
}
FV_MICRO_MAX_CHARS = 24
MIN_FINISHED_FV_HEIGHT = 600
MAX_FINISHED_FV_HEIGHT = 900
SOURCE_KINDS = {
    "customer-record", "customer-face-asset", "handwritten-feedback-asset",
    "business-record", "permission-record", "privacy-review",
}
PROOF_MODES = {"customer-face", "handwritten-feedback", "verified-fallback", "none"}
DIRECT_CALL_FIELDS = {
    "decision", "eligibility_rationale", "label", "phone_e164", "phone_source_id",
    "availability_copy", "availability_source_id", "section_id", "tracking_marker",
}
ROUTE_FORMATS = {"direct_capture", "article_reframe", "diagnostic"}
PERSUASION_JOBS = {
    "stop", "identify", "reframe", "educate", "diagnose", "prove",
    "demonstrate", "compare", "offer", "capture",
}
ROUTE_SOURCE_TYPES = {
    "user_input", "paid_strategy", "paid_evidence", "paid_voc",
    "paid_results", "inference",
}
ROUTE_PAID_EVIDENCE_KINDS = {
    "paid_strategy": "strategy",
    "paid_evidence": "evidence",
    "paid_voc": "voc",
    "paid_results": "results",
}
ROUTE_CONFIDENCE = {"high", "medium", "low"}
ROUTE_PROOF_MODULES = {
    "measured_result", "customer_case", "customer_voice", "third_party_evidence",
    "product_demo", "mechanism_explanation", "comparison_evidence",
    "faq_objection_handling",
}
ROUTE_CTA_KINDS = {
    "purchase", "free_trial", "document_request", "demo_request", "diagnosis",
    "consultation", "quotation", "booking", "inquiry", "next_destination",
}
ARTICLE_HANDOFF_ENGLISH_PATTERN = re.compile(
    r"^(?:"
    r"(?:view|read|learn|see|explore|discover)\s+(?:more|(?:the\s+)?(?:[a-z0-9][a-z0-9'&/-]*\s+){0,5}"
    r"(?:details?|guides?|case\s+stud(?:y|ies)|examples?|methods?|process(?:es)?|how\s+it\s+works))|"
    r"(?:learn|read|view|see|explore|discover)\s+more\s+about\s+(?:the\s+)?(?:service|product|solution|method|process)|"
    r"(?:explore|discover)\s+(?:the\s+)?(?:service|product|solution)|continue\s+reading|"
    r"start\s+with\s+(?:the\s+)?guide|contact\s+center\s+details|purchase\s+guide|"
    r"get\s+a\s+free\s+assessment\s+guide|"
    r"(?:continue|go|proceed)\s+to\s+(?:the\s+)?(?:next\s+)?"
    r"(?:content|article|page|service\s+details?|details?|guide|case\s+stud(?:y|ies)|examples?|methods?|process(?:es)?)|"
    r"next\s*:?\s*(?:content|article|page|service\s+details?|details?|guide)"
    r")$",
    re.IGNORECASE,
)
ARTICLE_HANDOFF_JAPANESE_PATTERNS = tuple(re.compile(pattern) for pattern in (
    r"^(?:続き|もっと|さらに)(?:を)?(?:読む|見る)$",
    r"^(?:詳しく見る|もっと知る|詳しく知る|もっと学ぶ|詳しく学ぶ)$",
    r"^(?:(?:.+)?(?:詳細|内容|紹介|ガイド|事例|実例|解決策|方法|進め方|仕組み|プロセス|流れ))(?:を)?(?:見る|読む|学ぶ)$",
    r"^.+(?:を|について)詳しく見る$",
    r"^(?:次の)?(?:記事|コンテンツ|ページ|サービス詳細|サービスの詳細)(?:を)?(?:見る|読む|へ進む)$",
))


class ContractError(ValueError):
    pass


_approval_spec = importlib.util.spec_from_file_location(
    "lp_structure_approval_contract", Path(__file__).with_name("structure_approval_contract.py")
)
assert _approval_spec and _approval_spec.loader
APPROVAL = importlib.util.module_from_spec(_approval_spec)
_approval_spec.loader.exec_module(APPROVAL)


def validate_approval_contract(document: dict, sources: dict, *, for_images: bool = False,
                               for_clicks: bool = False) -> dict:
    try:
        return APPROVAL.validate(document, sources, for_images=for_images, for_clicks=for_clicks)
    except APPROVAL.ApprovalContractError as exc:
        raise ContractError(str(exc)) from exc


def structure_approval_subject(document: dict, source_path: str, source_sha256: str) -> dict:
    subject = {"path": source_path, "sha256": source_sha256,
               "sections_sha256": canonical_digest(document["sections"])}
    if document.get("schema_version") == STRUCTURE_SCHEMA_VERSION:
        subject["approval_contract_sha256"] = canonical_digest(document["approval_contract"])
    return subject


def validate_structure_production(document: dict, evidence_root: Path, *, for_clicks: bool = False) -> None:
    require(document.get("schema_version") == STRUCTURE_SCHEMA_VERSION,
            "new production requires structure schema 1.6; legacy structure schemas are read-only and cannot authorize assembly")
    sources = validate_source_ledger(document, evidence_root)
    validate_approval_contract(document, sources, for_images=True, for_clicks=for_clicks)
    if for_clicks:
        require(safe_primary_href(document["cta_strategy"]["primary"]["href"]),
                "interactive assembly requires a safe source-bound CTA destination")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_project_file(project_root: Path, value: object, label: str) -> Path:
    require(isinstance(value, str) and value.strip() == value and value, f"{label} must be a relative path")
    relative = Path(value)
    require(not relative.is_absolute() and ".." not in relative.parts, f"{label} must stay inside project root")
    resolved = (project_root / relative).resolve()
    try:
        resolved.relative_to(project_root)
    except ValueError as exc:
        raise ContractError(f"{label} escapes project root") from exc
    require(resolved.is_file(), f"{label} does not exist: {value}")
    return resolved


def validate_png(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    require(data.startswith(PNG_SIGNATURE), f"not a PNG: {path}")
    offset = len(PNG_SIGNATURE)
    chunk_index = 0
    ihdr: tuple[int, int, int, int, int] | None = None
    idat_parts: list[bytes] = []
    saw_idat = False
    idat_closed = False
    saw_iend = False
    saw_plte = False
    while offset < len(data):
        require(offset + 12 <= len(data), f"truncated PNG chunk: {path}")
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        kind = data[offset + 4 : offset + 8]
        require(length <= 0x7FFFFFFF, f"PNG chunk exceeds length limit: {path}")
        require(len(kind) == 4 and all(65 <= byte <= 90 or 97 <= byte <= 122 for byte in kind), f"PNG chunk type is invalid: {path}")
        end = offset + 12 + length
        require(end <= len(data), f"truncated PNG payload: {path}")
        payload = data[offset + 8 : offset + 8 + length]
        declared_crc = struct.unpack(">I", data[offset + 8 + length : end])[0]
        actual_crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
        require(declared_crc == actual_crc, f"PNG CRC mismatch: {path}")

        require(not saw_iend, f"PNG contains chunks after IEND: {path}")
        if kind == b"IHDR":
            require(chunk_index == 0 and ihdr is None and length == 13, f"PNG must start with one 13-byte IHDR: {path}")
            width, height = struct.unpack(">II", payload[:8])
            bit_depth, color_type, compression, filter_method, interlace = payload[8:13]
            valid_depths = {0: {1, 2, 4, 8, 16}, 2: {8, 16}, 3: {1, 2, 4, 8}, 4: {8, 16}, 6: {8, 16}}
            require(width > 0 and height > 0, f"PNG dimensions must be positive: {path}")
            require(color_type in valid_depths and bit_depth in valid_depths[color_type], f"PNG bit-depth/color-type is invalid: {path}")
            require(compression == 0 and filter_method == 0 and interlace in {0, 1}, f"PNG compression/filter/interlace is invalid: {path}")
            require(bit_depth == 8 and color_type in {2, 6} and interlace == 0, f"PNG must use the public 8-bit non-interlaced RGB/RGBA subset: {path}")
            ihdr = (width, height, bit_depth, color_type, interlace)
        elif kind == b"PLTE":
            require(False, f"PNG public RGB/RGBA subset must not contain PLTE: {path}")
            require(ihdr is not None and not saw_idat and not saw_plte, f"PNG PLTE order/count is invalid: {path}")
            require(3 <= length <= 768 and length % 3 == 0, f"PNG PLTE length is invalid: {path}")
            _, _, bit_depth, color_type, _ = ihdr
            require(color_type not in {0, 4}, f"grayscale PNG must not contain PLTE: {path}")
            if color_type == 3:
                require(length // 3 <= 2**bit_depth, f"PNG PLTE exceeds indexed bit depth: {path}")
            saw_plte = True
        elif kind == b"tRNS":
            require(False, f"PNG public RGB/RGBA subset must not contain tRNS: {path}")
        elif kind == b"IDAT":
            require(ihdr is not None and not idat_closed, f"PNG IDAT order is invalid: {path}")
            saw_idat = True
            idat_parts.append(payload)
        elif kind == b"IEND":
            require(ihdr is not None and saw_idat and length == 0, f"PNG IEND is invalid: {path}")
            saw_iend = True
            require(end == len(data), f"PNG has bytes after IEND: {path}")
            offset = end
            break
        else:
            if saw_idat:
                idat_closed = True
            require(kind[0] & 0x20 != 0, f"PNG contains unsupported critical chunk {kind.decode('ascii')}: {path}")
        offset = end
        chunk_index += 1

    require(offset == len(data) and ihdr is not None and saw_idat and saw_iend, f"PNG structure is incomplete: {path}")
    width, height, bit_depth, color_type, interlace = ihdr
    require(color_type != 3 or saw_plte, f"indexed PNG must contain PLTE: {path}")
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[color_type]
    passes = ((0, 0, 1, 1),) if interlace == 0 else (
        (0, 0, 8, 8), (4, 0, 8, 8), (0, 4, 4, 8), (2, 0, 4, 4),
        (0, 2, 2, 4), (1, 0, 2, 2), (0, 1, 1, 2),
    )
    scanlines: list[tuple[int, int]] = []
    expected_size = 0
    for x_start, y_start, x_step, y_step in passes:
        pass_width = 0 if width <= x_start else (width - x_start + x_step - 1) // x_step
        pass_height = 0 if height <= y_start else (height - y_start + y_step - 1) // y_step
        if not pass_width or not pass_height:
            continue
        row_bytes = (pass_width * channels * bit_depth + 7) // 8
        scanlines.append((pass_height, row_bytes))
        expected_size += pass_height * (row_bytes + 1)
    require(expected_size <= 256 * 1024 * 1024, f"PNG decoded bytes exceed safety limit: {path}")
    try:
        decoder = zlib.decompressobj()
        decoded = decoder.decompress(b"".join(idat_parts), expected_size + 1)
        exceeded = len(decoded) > expected_size or bool(decoder.unconsumed_tail)
        if not exceeded:
            decoded += decoder.flush()
    except zlib.error as exc:
        raise ContractError(f"PNG IDAT cannot be decoded: {path}") from exc
    require(not exceeded and len(decoded) == expected_size, f"PNG decoded scanline length is invalid: {path}")
    require(decoder.eof and not decoder.unused_data, f"PNG zlib stream is incomplete or has trailing data: {path}")
    cursor = 0
    for pass_height, row_bytes in scanlines:
        for _ in range(pass_height):
            require(decoded[cursor] <= 4, f"PNG scanline filter is invalid: {path}")
            cursor += row_bytes + 1
    return width, height


def canonical_digest(payload: object) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _approval_view_value(value: object) -> str:
    """Render one JSON value readably without creating a second copy authority."""

    if value is None or value == "" or value == []:
        return "—"
    if isinstance(value, str):
        return value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def render_structure_approval_view(document: dict, source_path: str, source_sha256: str) -> str:
    """Return the deterministic human approval view for an already-valid structure JSON."""

    validate_structure_document(document)
    require(nonempty_string(source_path), "approval view source path is required")
    require(bool(re.fullmatch(r"[0-9a-f]{64}", source_sha256)), "approval view source sha256 is invalid")
    handoff = document["fv_handoff"]
    five = handoff["five_second"]
    budget = handoff["fv_content_budget"]
    lines = [
        "# LP structure approval view",
        "",
        f"- Authoritative JSON: `{source_path}`",
        f"- JSON SHA-256: `{source_sha256}`",
        "- Authority: the JSON above is the sole machine, copy, and section-order authority. Edit it first, then regenerate this view.",
        "",
        "## Decision summary",
        "",
        f"- Goal: {_approval_view_value(document.get('objective'))}",
        f"- Audience: {_approval_view_value(document.get('audience'))}",
        f"- Offer: {_approval_view_value(document.get('offer'))}",
        f"- Primary action: {_approval_view_value(document.get('primary_cta'))}",
        f"- Traffic/context: {_approval_view_value(document.get('traffic'))}",
        "",
        "## First-view plan",
        "",
        f"- Five-second audience: {_approval_view_value(five['audience'])}",
        f"- Five-second promise/offer: {_approval_view_value(five['promise_or_offer'])}",
        f"- Visible action: {_approval_view_value(five['next_action'])}",
        f"- Dominant message: {_approval_view_value(handoff['dominant_message'])}",
        f"- Visual job: {_approval_view_value(handoff['visual_job'])}",
        f"- Content budget: `{budget['profile']}` — {_approval_view_value(budget['rationale'])}",
        "- Deferred from the first view:",
    ]
    deferred = budget["deferred_items"]
    if deferred:
        for item in deferred:
            lines.append(
                f"  - `{item['id']}` → `{item['destination_section_id']}`: "
                f"{_approval_view_value(item['text'])} — {_approval_view_value(item['rationale'])}"
            )
    else:
        lines.append("  - None")

    if document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
        route = document.get("acquisition_route_brief")
        if route is not None:
            primary_route = route["primary_route"]
            build_target = next(
                item for item in primary_route["touchpoints"]
                if item["id"] == primary_route["build_target_touchpoint_id"]
            )
            override = route["user_override"]
            route_choice_lines: list[str]
            if override["applied"]:
                recommended_route = next(
                    item for item in route["alternative_routes"]
                    if item["id"] == override["recommended_route_id"]
                )
                route_choice_lines = [
                    f"- Selected user override: `{primary_route['format']}` (`{primary_route['id']}`) "
                    f"/ confidence `{primary_route['confidence']}`",
                    f"- Recommended route: `{recommended_route['format']}` "
                    f"(`{recommended_route['id']}`) / confidence `{recommended_route['confidence']}`",
                    f"- Override reason: {_approval_view_value(override['reason'])}",
                    "- Override correction plan:",
                    *[
                        f"  - {_approval_view_value(item)}"
                        for item in override["correction_plan"]
                    ],
                ]
            else:
                route_choice_lines = [
                    f"- Recommended route: `{primary_route['format']}` (`{primary_route['id']}`) "
                    f"/ confidence `{primary_route['confidence']}`",
                ]
            lines.extend([
                "",
                "## Route Check",
                "",
                f"- Readiness/mode: `{route['readiness']['status']}` / `{route['mode']}`",
                f"- Current state: {_approval_view_value(route['strategy']['current_state']['value'])} "
                f"(`{route['strategy']['current_state']['source']}`, confidence "
                f"`{route['strategy']['current_state']['confidence']}`)",
                "- Required shifts:",
            ])
            for shift in route["strategy"]["required_shifts"]:
                lines.append(
                    f"  - {_approval_view_value(shift['value'])} "
                    f"(`{shift['source']}`, confidence `{shift['confidence']}`)"
                )
            lines.extend([
                f"- Primary barrier: {_approval_view_value(route['strategy']['primary_barrier']['value'])} "
                f"(`{route['strategy']['primary_barrier']['source']}`, confidence "
                f"`{route['strategy']['primary_barrier']['confidence']}`)",
                f"- Economics: `{route['economics']['status']}` — {_approval_view_value(route['economics']['conclusion'])}",
                *route_choice_lines,
                f"- Build target: `{build_target['id']}` — {_approval_view_value(build_target['message_role'])}",
                "- Route rationale:",
            ])
            for rationale in primary_route["rationale"]:
                lines.append(f"  - {_approval_view_value(rationale)}")
            lines.append("- Touchpoint responsibilities:")
            for touchpoint in primary_route["touchpoints"]:
                jobs = ", ".join(f"`{job}`" for job in touchpoint["persuasion_jobs"])
                exit_binding = ""
                if touchpoint.get("exit_action_kind") == "next_destination":
                    exit_binding = f" -> `{touchpoint['exit_target_touchpoint_id']}`"
                lines.append(
                    f"  - `{touchpoint['id']}` ({touchpoint['surface_kind']}): "
                    f"{_approval_view_value(touchpoint['message_role'])}; jobs {jobs}; "
                    f"exit action: {_approval_view_value(touchpoint['exit_action'])}{exit_binding}"
                )
            lines.append("- Alternatives:")
            for alternative in route["alternative_routes"]:
                lines.append(
                    f"  - `{alternative['format']}` / confidence `{alternative['confidence']}` — "
                    f"{_approval_view_value(alternative['rationale'][0])}"
                )
            lines.append("- Not recommended now:")
            for rejected in route["rejected_routes"]:
                lines.append(
                    f"  - `{rejected['format']}` — "
                    f"{'; '.join(_approval_view_value(reason) for reason in rejected['reasons'])}"
                )
            conversion_action = route["conversion_action"]
            lines.extend([
                f"- Final conversion action: `{conversion_action['kind']}` / "
                f"{_approval_view_value(conversion_action['label'])} at "
                f"`{conversion_action['final_touchpoint_id']}`",
                "- Assumptions:",
            ])
            for assumption in route["assumptions"]:
                lines.append(
                    f"  - `{assumption['id']}` / impact `{assumption['impact']}` / confidence "
                    f"`{assumption['confidence']}`: {_approval_view_value(assumption['statement'])}; "
                    f"validate with {_approval_view_value(assumption['validation_method'])}"
                )
            measurement = route["measurement_plan"]
            lines.extend([
                f"- Measurement outcome: {_approval_view_value(measurement['primary_outcome'])}",
                "- Leading indicators: " + "; ".join(
                    _approval_view_value(item) for item in measurement["leading_indicators"]
                ),
                "- Decision rules: " + "; ".join(
                    _approval_view_value(item) for item in measurement["decision_rules"]
                ),
            ])
        proof = document["authentic_proof"]
        direct_call = document["cta_strategy"]["direct_call"]
        lines.extend([
            "",
            "## Authentic proof decision",
            "",
            f"- Selected mode: `{proof['selected_mode']}` — {_approval_view_value(proof['selection_rationale'])}",
            "- Proof items:",
        ])
        if proof["items"]:
            for item in proof["items"]:
                lines.append(
                    f"  - `{item['proof_id']}` / `{item['mode']}` / claim `{item['claim_id']}` / "
                    f"sections {_approval_view_value(item['use_sections'])}: {_approval_view_value(item['display_copy'])}; "
                    f"content sources {_approval_view_value(item['content_source_ids'])}, asset source "
                    f"`{_approval_view_value(item['asset_source_id'])}`; permission "
                    f"{_approval_view_value(item['usage_permission'])}; privacy {_approval_view_value(item['privacy'])}"
                )
        else:
            lines.append("  - None available; no customer or testimonial representation is authorized.")
        lines.extend([
            "",
            "## CTA decision",
            "",
            f"- Primary action: {_approval_view_value(document['cta_strategy']['primary'])}",
            f"- Direct call: `{direct_call['decision']}` — {_approval_view_value(direct_call['eligibility_rationale'])}",
        ])
        if direct_call["decision"] == "enabled":
            lines.extend([
                f"- Direct-call visible label: {_approval_view_value(direct_call['label'])}",
                f"- Direct-call phone/source: `{direct_call['phone_e164']}` / `{direct_call['phone_source_id']}`",
                f"- Direct-call availability: {_approval_view_value(direct_call['availability_copy'])}",
                f"- Direct-call availability source: `{direct_call['availability_source_id']}`",
                f"- Direct-call section/tracking: `{direct_call['section_id']}` / `{direct_call['tracking_marker']}`",
            ])

        lines.extend(["", "## Section bridges"])
        if document["adjacent_boundary_plan"]:
            for boundary in document["adjacent_boundary_plan"]:
                bridge = boundary["bridge_plan"]
                lines.extend([
                    "",
                    f"### Bridge {boundary['order']}: `{boundary['from_section_id']}` → `{boundary['to_section_id']}`",
                    "",
                    f"- Semantic: {_approval_view_value(bridge['semantic'])}",
                    f"- Copy: {_approval_view_value(bridge['copy'])}",
                    f"- Visual: {_approval_view_value(bridge['visual'])}",
                    f"- Layout: {_approval_view_value(bridge['layout'])}",
                    f"- Arrow: {_approval_view_value(bridge['arrow'])}",
                ])
        else:
            lines.extend(["", "- No adjacent boundary (single-section page)."])

    lines.extend(["", "## Sections"])
    for section in document["sections"]:
        copy = section["copy"]
        lines.extend([
            "",
            f"### {section['order']}. `{section['id']}`",
            "",
            f"- Reader question / role: {_approval_view_value(section.get('role'))}",
            f"- Answer: {_approval_view_value(copy.get('body'))}",
            f"- Headline: {_approval_view_value(copy.get('headline'))}",
            f"- Proof/source: {_approval_view_value(section.get('evidence'))}",
            f"- CTA: {_approval_view_value(copy.get('cta'))}",
            f"- Authoritative copy object: `{json.dumps(copy, ensure_ascii=False, sort_keys=True, separators=(',', ':'))}`",
        ])

    if document.get("schema_version") == STRUCTURE_SCHEMA_VERSION:
        lines.extend(["", "## Unresolved questions", ""])
        for question in document.get("evidence_and_unknowns", []):
            lines.append(f"- Question: {_approval_view_value(question['question'])}; sources {_approval_view_value(question['source_ids'])}")
        if not document.get("evidence_and_unknowns"):
            lines.append("- No additional questions recorded; field-level unknowns remain listed below.")
        lines.extend(APPROVAL.approval_lines(document))
        return "\n".join(lines)

    lines.extend([
        "",
        "## Unknowns and locks",
        "",
        f"- Evidence / unknowns: {_approval_view_value(document.get('evidence_and_unknowns'))}",
        f"- Locked items: {_approval_view_value(document.get('locked_items'))}",
        "",
        "## Approval",
        "",
        "Reply with OK / このまま進めて to approve only the authoritative JSON identified above, or list the exact changes needed. JSON changes require regenerating this view.",
        "",
    ])
    return "\n".join(lines)


def validate_structure_approval_view(
    view_path: Path,
    document: dict,
    source_path: str,
    source_sha256: str,
) -> None:
    try:
        observed = view_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ContractError(f"cannot read structure approval view: {exc}") from exc
    expected = render_structure_approval_view(document, source_path, source_sha256)
    require(observed == expected, "structure approval view content/hash binding drift")


def load_json(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read {label}: {exc}") from exc
    require(isinstance(value, dict), f"{label} must be a JSON object")
    return value


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def strict_int(value: object) -> bool:
    """Return true only for JSON integers, never JSON booleans."""

    return isinstance(value, int) and not isinstance(value, bool)


def meaningful_action_label(value: object) -> bool:
    """Require a visible Unicode label, not whitespace/control/format-only text."""

    return (
        isinstance(value, str)
        and value == value.strip()
        and any(character.isalnum() for character in value)
        and not any(unicodedata.category(character) in {"Cc", "Cf"} for character in value)
    )


def normalized_route_semantics(value: str) -> str:
    """Normalize diagnostic semantics so punctuation/case/spacing cannot fake a branch."""

    normalized = unicodedata.normalize("NFKC", value).casefold()
    return "".join(character for character in normalized if character.isalnum())


def safe_article_handoff_action_label(value: str) -> bool:
    """Allow only whole labels whose meaning is an informational next-destination handoff."""

    normalized = unicodedata.normalize("NFKC", value).casefold().strip()
    normalized = re.sub(r"\s+", " ", normalized).rstrip(".!?！。？")
    compact = normalized.replace(" ", "")
    return bool(ARTICLE_HANDOFF_ENGLISH_PATTERN.fullmatch(normalized)) or any(
        pattern.fullmatch(compact) for pattern in ARTICLE_HANDOFF_JAPANESE_PATTERNS
    )


def safe_primary_href(value: object) -> bool:
    if not isinstance(value, str) or not value or value != value.strip():
        return False
    if "\\" in value or any(unicodedata.category(character) in {"Cc", "Cf"} for character in value):
        return False
    if value.startswith("/"):
        return not value.startswith("//") and not urlsplit(value).scheme and not urlsplit(value).netloc
    parsed = urlsplit(value)
    return (
        parsed.scheme == "https" and bool(parsed.hostname)
        and parsed.username is None and parsed.password is None
        and not parsed.fragment
    )


def future_rfc3339_or_none(value: object) -> bool:
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.astimezone(timezone.utc) > datetime.now(timezone.utc)


def regions_overlap(left: dict, right: dict) -> bool:
    return (
        max(left["x"], right["x"]) < min(left["x"] + left["width"], right["x"] + right["width"])
        and max(left["y"], right["y"]) < min(left["y"] + left["height"], right["y"] + right["height"])
    )


def section_authority_copy(section: dict) -> str:
    copy = section.get("copy")
    require(isinstance(copy, dict), "first section copy is invalid")
    values = [copy.get(key) for key in ("headline", "body", "cta")]
    return "\n".join(value for value in values if isinstance(value, str))


def non_whitespace_length(value: str) -> int:
    return sum(not character.isspace() for character in value)


def first_section_copy_leaves(copy: object, prefix: str = "") -> list[tuple[str, str]]:
    """Return every string leaf in stable JSON order; null leaves are intentionally invisible."""

    if isinstance(copy, str):
        return [(prefix, copy)]
    if copy is None:
        return []
    if isinstance(copy, dict):
        leaves: list[tuple[str, str]] = []
        for key, value in copy.items():
            require(nonempty_string(key), "first-section copy keys must be non-empty strings")
            child = f"{prefix}.{key}" if prefix else key
            leaves.extend(first_section_copy_leaves(value, child))
        return leaves
    if isinstance(copy, list):
        leaves = []
        for index, value in enumerate(copy):
            child = f"{prefix}.{index}" if prefix else str(index)
            leaves.extend(first_section_copy_leaves(value, child))
        return leaves
    require(False, f"first-section copy leaf {prefix or '<root>'} must be string or null")
    return []


def verified_claims(document: dict) -> dict[str, dict]:
    ledger = document.get("claim_source_ledger")
    require(isinstance(ledger, list), "proof content requires claim_source_ledger")
    claims: dict[str, dict] = {}
    for index, claim in enumerate(ledger, start=1):
        require(isinstance(claim, dict), f"claim_source_ledger item {index} must be an object")
        claim_id = claim.get("claim_id")
        require(nonempty_string(claim_id) and claim_id not in claims, f"claim_source_ledger item {index} claim_id must be unique")
        claims[claim_id] = claim
    return claims


def validate_source_ledger(document: dict, evidence_root: Path | None = None) -> dict[str, dict]:
    if evidence_root is not None:
        evidence_root = evidence_root.resolve()
    ledger = document.get("source_ledger")
    require(isinstance(ledger, list) and ledger, "schema 1.5 source_ledger must be non-empty")
    sources: dict[str, dict] = {}
    fields = {"source_id", "kind", "reference", "provided_by", "verified"}
    for index, source in enumerate(ledger, start=1):
        require(isinstance(source, dict), f"source_ledger item {index} must be an object")
        kind = source.get("kind")
        expected_fields = set(fields)
        if kind in {"permission-record", "privacy-review"}:
            expected_fields |= {"evidence", "authored_by_model"}
        elif kind == "business-record" and ({"verified_value_kind", "verified_value"} & set(source)):
            expected_fields |= {"verified_value_kind", "verified_value"}
        if kind == "business-record" and "field_values" in source:
            require(document.get("schema_version") == STRUCTURE_SCHEMA_VERSION,
                    "field-bound approval sources require structure schema 1.6")
            expected_fields.add("field_values")
        require(set(source) == expected_fields,
                f"source_ledger item {index} fields are invalid")
        source_id = source.get("source_id")
        require(nonempty_string(source_id) and source_id not in sources,
                f"source_ledger item {index} source_id must be unique")
        require(kind in SOURCE_KINDS,
                f"source_ledger item {index} kind is invalid")
        require(nonempty_string(source.get("reference")),
                f"source_ledger item {index} reference is required")
        require(source.get("provided_by") in {"user", "controller", "public-record"},
                f"source_ledger item {index} provided_by is invalid")
        require(source.get("verified") is True,
                f"source_ledger item {index} must be explicitly verified")
        normalized = dict(source)
        if "field_values" in source:
            try:
                APPROVAL.validate_source_fields(source)
            except APPROVAL.ApprovalContractError as exc:
                raise ContractError(str(exc)) from exc
        if kind in {"permission-record", "privacy-review"}:
            require(source.get("provided_by") in {"user", "controller"}
                    and source.get("authored_by_model") is False,
                    f"source_ledger item {index} external evidence cannot be model-authored or self-attested")
            binding = source.get("evidence")
            require(isinstance(binding, dict) and set(binding) == {"path", "sha256"}
                    and nonempty_string(binding.get("path"))
                    and isinstance(binding.get("sha256"), str)
                    and re.fullmatch(r"[0-9a-f]{64}", binding["sha256"]),
                    f"source_ledger item {index} external evidence binding is invalid")
            if evidence_root is not None:
                evidence_path = resolve_project_file(evidence_root, binding["path"], f"source_ledger item {index} evidence.path")
                require(binding["sha256"] == sha256(evidence_path),
                        f"source_ledger item {index} external evidence sha256 mismatch")
                payload = load_json(evidence_path, f"source_ledger item {index} external evidence")
                common = {"kind", "schema_version", "evidence_kind", "provided_by", "authored_by_model",
                          "asset_source_id", "use_sections"}
                extra = {"scope", "expires_at"} if kind == "permission-record" else {"constraints"}
                require(isinstance(payload, dict) and set(payload) == common | extra
                        and payload.get("kind") == "lp-external-source-evidence"
                        and payload.get("schema_version") == "1.0"
                        and payload.get("evidence_kind") == kind
                        and payload.get("provided_by") == source.get("provided_by")
                        and payload.get("authored_by_model") is False,
                        f"source_ledger item {index} external evidence payload is invalid")
                normalized["_evidence_payload"] = payload
        elif kind == "business-record" and "verified_value_kind" in source:
            require(source.get("verified_value_kind") in {"phone_e164", "availability_copy"}
                    and nonempty_string(source.get("verified_value")),
                    f"source_ledger item {index} verified business value is invalid")
        sources[source_id] = normalized
    return sources


def validate_authentic_proof(document: dict, section_ids: list[str], sources: dict[str, dict]) -> dict:
    strategy = document.get("authentic_proof")
    fields = {"preferred_order", "availability", "selected_mode", "selection_rationale", "items"}
    require(isinstance(strategy, dict) and set(strategy) == fields,
            "authentic_proof fields are invalid")
    require(strategy.get("preferred_order") == [
        "customer-face", "handwritten-feedback", "verified-fallback"
    ], "authentic_proof preferred_order must preserve the truthful proof ladder")
    availability = strategy.get("availability")
    ladder = ["customer-face", "handwritten-feedback", "verified-fallback"]
    require(isinstance(availability, dict) and list(availability) == ladder,
            "authentic_proof availability must assess the proof ladder in order")
    first_available: str | None = None
    for mode in ladder:
        assessment = availability.get(mode)
        require(isinstance(assessment, dict)
                and set(assessment) == {"status", "rationale"}
                and assessment.get("status") in {"available", "unavailable"}
                and nonempty_string(assessment.get("rationale")),
                f"authentic_proof availability {mode} is invalid")
        if first_available is None and assessment["status"] == "available":
            first_available = mode
    selected_mode = strategy.get("selected_mode")
    expected_mode = first_available or "none"
    require(selected_mode == expected_mode,
            "authentic_proof must select the first truthfully available proof mode")
    require(nonempty_string(strategy.get("selection_rationale")),
            "authentic_proof selection_rationale is required")
    items = strategy.get("items")
    require(isinstance(items, list), "authentic_proof items must be an array")
    require(bool(items) == (selected_mode != "none"),
            "authentic_proof items must match the selected proof mode")
    item_fields = {
        "proof_id", "mode", "claim_id", "content_source_ids", "asset_source_id",
        "usage_permission", "privacy", "use_sections", "display_copy",
    }
    claims = verified_claims(document) if items else {}
    seen_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        require(isinstance(item, dict) and set(item) == item_fields,
                f"authentic_proof item {index} fields are invalid")
        proof_id = item.get("proof_id")
        require(isinstance(proof_id, str) and FV_ITEM_ID_PATTERN.fullmatch(proof_id)
                and proof_id not in seen_ids,
                f"authentic_proof item {index} proof_id must be a unique stable token")
        seen_ids.add(proof_id)
        require(item.get("mode") == selected_mode,
                f"authentic_proof item {index} mode must equal selected_mode")
        claim_id = item.get("claim_id")
        require(claim_id in claims and claims[claim_id].get("status") in {"verified", "確認済み"},
                f"authentic_proof item {index} must bind a verified claim")
        content_sources = item.get("content_source_ids")
        require(isinstance(content_sources, list) and content_sources
                and all(source_id in sources for source_id in content_sources)
                and len(content_sources) == len(set(content_sources)),
                f"authentic_proof item {index} content sources are invalid")
        require(set(content_sources) <= set(claims[claim_id].get("source_ids", [])),
                f"authentic_proof item {index} content sources must be claim sources")
        use_sections = item.get("use_sections")
        require(isinstance(use_sections, list) and use_sections
                and all(section_id in section_ids for section_id in use_sections)
                and len(use_sections) == len(set(use_sections)),
                f"authentic_proof item {index} use_sections are invalid")
        require(set(use_sections) <= set(claims[claim_id].get("use_sections", [])),
                f"authentic_proof item {index} sections must be claim-authorized")
        display_copy = item.get("display_copy")
        require(nonempty_string(display_copy) and display_copy in claims[claim_id].get("claim", ""),
                f"authentic_proof item {index} display_copy must be exact verified claim text")
        asset_source_id = item.get("asset_source_id")
        permission = item.get("usage_permission")
        privacy = item.get("privacy")
        require(isinstance(permission, dict)
                and set(permission) == {"status", "evidence_source_id", "asset_source_id", "use_sections", "scope", "expires_at"},
                f"authentic_proof item {index} usage_permission fields are invalid")
        require(isinstance(privacy, dict)
                and set(privacy) == {"status", "evidence_source_id", "asset_source_id", "use_sections", "constraints"},
                f"authentic_proof item {index} privacy fields are invalid")
        if selected_mode in {"customer-face", "handwritten-feedback"}:
            expected_asset_kind = (
                "customer-face-asset" if selected_mode == "customer-face"
                else "handwritten-feedback-asset"
            )
            require(asset_source_id in sources and sources[asset_source_id]["kind"] == expected_asset_kind,
                    f"authentic_proof item {index} asset source is invalid")
            require(permission.get("status") == "explicitly-granted"
                    and permission.get("evidence_source_id") in sources
                    and sources[permission["evidence_source_id"]]["kind"] == "permission-record"
                    and permission.get("asset_source_id") == asset_source_id
                    and permission.get("use_sections") == use_sections
                    and nonempty_string(permission.get("scope"))
                    and future_rfc3339_or_none(permission.get("expires_at")),
                    f"authentic_proof item {index} requires explicit scoped usage permission")
            permission_payload = sources[permission["evidence_source_id"]].get("_evidence_payload")
            if permission_payload is not None:
                require(permission_payload.get("asset_source_id") == asset_source_id
                        and permission_payload.get("use_sections") == use_sections
                        and permission_payload.get("scope") == permission.get("scope")
                        and permission_payload.get("expires_at") == permission.get("expires_at"),
                        f"authentic_proof item {index} permission drifts from external evidence")
            require(privacy.get("status") == "cleared"
                    and privacy.get("evidence_source_id") in sources
                    and sources[privacy["evidence_source_id"]]["kind"] == "privacy-review"
                    and privacy.get("asset_source_id") == asset_source_id
                    and privacy.get("use_sections") == use_sections
                    and isinstance(privacy.get("constraints"), list)
                    and all(nonempty_string(value) for value in privacy["constraints"]),
                    f"authentic_proof item {index} requires an explicit privacy clearance")
            privacy_payload = sources[privacy["evidence_source_id"]].get("_evidence_payload")
            if privacy_payload is not None:
                require(privacy_payload.get("asset_source_id") == asset_source_id
                        and privacy_payload.get("use_sections") == use_sections
                        and privacy_payload.get("constraints") == privacy.get("constraints"),
                        f"authentic_proof item {index} privacy clearance drifts from external evidence")
        else:
            require(asset_source_id is None,
                    f"authentic_proof item {index} verified fallback cannot imply a customer asset")
            require(all(sources[source_id]["kind"] == "business-record" for source_id in content_sources),
                    f"authentic_proof item {index} verified fallback requires non-customer business-record sources")
            require(permission == {"status": "not-applicable", "evidence_source_id": None,
                                   "asset_source_id": None, "use_sections": use_sections,
                                   "scope": None, "expires_at": None},
                    f"authentic_proof item {index} fallback permission must be not-applicable")
            require(privacy == {"status": "not-applicable", "evidence_source_id": None,
                                "asset_source_id": None, "use_sections": use_sections,
                                "constraints": []},
                    f"authentic_proof item {index} fallback privacy must be not-applicable")
    return strategy


def validate_cta_strategy(document: dict, section_ids: list[str], sources: dict[str, dict]) -> dict:
    strategy = document.get("cta_strategy")
    require(isinstance(strategy, dict) and set(strategy) == {"primary", "direct_call"},
            "cta_strategy fields are invalid")
    primary = strategy.get("primary")
    require(isinstance(primary, dict)
            and set(primary) == {"label", "destination_kind", "section_ids", "href"}
            and primary.get("label") == document.get("primary_cta")
            and primary.get("destination_kind") in {"form", "booking", "checkout", "link"}
            and isinstance(primary.get("section_ids"), list) and primary["section_ids"]
            and all(section_id in section_ids for section_id in primary["section_ids"])
            and len(primary["section_ids"]) == len(set(primary["section_ids"])),
            "cta_strategy primary action is invalid")
    require((document.get("schema_version") == STRUCTURE_SCHEMA_VERSION and primary.get("href") is None)
            or safe_primary_href(primary.get("href")),
            "cta_strategy primary href must be a safe relative path or explicit https URL")
    for section_id in primary["section_ids"]:
        section = document["sections"][section_ids.index(section_id)]
        require(section.get("copy", {}).get("cta") == primary["label"],
                f"cta_strategy primary label must be exact in section {section_id}")
    direct = strategy.get("direct_call")
    require(isinstance(direct, dict) and set(direct) == DIRECT_CALL_FIELDS,
            "cta_strategy direct_call fields are invalid")
    require(direct.get("decision") in {"enabled", "not-eligible", "not-selected"}
            and nonempty_string(direct.get("eligibility_rationale")),
            "cta_strategy direct_call decision/rationale is invalid")
    optional_fields = DIRECT_CALL_FIELDS - {"decision", "eligibility_rationale"}
    if direct["decision"] != "enabled":
        require(all(direct.get(key) is None for key in optional_fields),
                "disabled direct_call fields must be null")
        return strategy
    require(meaningful_action_label(direct.get("label"))
            and direct["label"] != primary["label"],
            "enabled direct_call requires a distinct exact secondary label")
    require(isinstance(direct.get("phone_e164"), str)
            and re.fullmatch(r"\+[1-9][0-9]{7,14}", direct["phone_e164"]),
            "enabled direct_call phone_e164 is invalid")
    require(direct.get("phone_source_id") in sources
            and sources[direct["phone_source_id"]]["kind"] == "business-record"
            and sources[direct["phone_source_id"]].get("verified_value_kind") == "phone_e164"
            and sources[direct["phone_source_id"]].get("verified_value") == direct["phone_e164"],
            "enabled direct_call phone number must bind a verified business source")
    require(nonempty_string(direct.get("availability_copy"))
            and direct.get("availability_source_id") in sources
            and sources[direct["availability_source_id"]]["kind"] == "business-record"
            and sources[direct["availability_source_id"]].get("verified_value_kind") == "availability_copy"
            and sources[direct["availability_source_id"]].get("verified_value") == direct["availability_copy"],
            "enabled direct_call availability copy must bind a verified business source")
    require(direct.get("section_id") in section_ids,
            "enabled direct_call section_id is invalid")
    require(isinstance(direct.get("tracking_marker"), str)
            and FV_ITEM_ID_PATTERN.fullmatch(direct["tracking_marker"]),
            "enabled direct_call tracking_marker must be a stable token")
    section = document["sections"][section_ids.index(direct["section_id"])]
    copy_leaves = [value for _, value in first_section_copy_leaves(section.get("copy"))]
    require(any(direct["label"] in value for value in copy_leaves)
            and any(direct["availability_copy"] in value for value in copy_leaves),
            "enabled direct_call label and availability copy must be baked into its section authority copy")
    return strategy


def validate_bridge_plan(plan: object, transition_copy: object, index: int) -> None:
    fields = {"semantic", "copy", "visual", "layout", "arrow"}
    require(isinstance(plan, dict) and set(plan) == fields,
            f"boundary {index} bridge_plan fields are invalid")
    semantic = plan.get("semantic")
    require(isinstance(semantic, dict)
            and set(semantic) == {"open_question", "next_answer"}
            and all(nonempty_string(semantic.get(key)) for key in semantic),
            f"boundary {index} semantic bridge is invalid")
    copy = plan.get("copy")
    require(isinstance(copy, dict)
            and set(copy) == {"strategy", "exact_text"}
            and copy.get("strategy") in {"none", "continuation", "open-loop", "contrast"},
            f"boundary {index} copy bridge is invalid")
    if copy["strategy"] == "none":
        require(copy.get("exact_text") is None and transition_copy is None,
                f"boundary {index} copyless bridge must keep exact text null")
    else:
        require(nonempty_string(copy.get("exact_text"))
                and copy["exact_text"] == transition_copy,
                f"boundary {index} copy bridge must bind exact transition_copy")
    visual = plan.get("visual")
    layout = plan.get("layout")
    require(isinstance(visual, dict)
            and set(visual) == {"continuity_device", "handoff"}
            and all(nonempty_string(visual.get(key)) for key in visual),
            f"boundary {index} visual bridge is invalid")
    require(isinstance(layout, dict)
            and set(layout) == {"section_end", "next_section_start", "spacing_rhythm"}
            and all(nonempty_string(layout.get(key)) for key in layout),
            f"boundary {index} layout bridge is invalid")
    arrow = plan.get("arrow")
    require(isinstance(arrow, dict)
            and set(arrow) == {"use", "supports"}
            and arrow.get("use") in {"none", "supportive"},
            f"boundary {index} arrow bridge is invalid")
    if arrow["use"] == "none":
        require(arrow.get("supports") is None,
                f"boundary {index} unused arrow supports must be null")
    else:
        require(nonempty_string(arrow.get("supports")),
                f"boundary {index} supportive arrow must name the real bridge it supports")


def validate_route_string_list(value: object, label: str, *, allow_empty: bool = False) -> list[str]:
    require(isinstance(value, list)
            and (allow_empty or bool(value))
            and all(nonempty_string(item) for item in value)
            and len(value) == len(set(value)),
            f"{label} must be a {'possibly empty ' if allow_empty else ''}unique string array")
    return value


def validate_route_sourced_value(value: object, label: str) -> dict:
    fields = {"value", "source", "confidence", "evidence_refs"}
    require(isinstance(value, dict) and set(value) == fields,
            f"{label} fields are invalid")
    require(nonempty_string(value.get("value")), f"{label} value is required")
    require(value.get("source") in ROUTE_SOURCE_TYPES, f"{label} source is invalid")
    require(value.get("confidence") in ROUTE_CONFIDENCE, f"{label} confidence is invalid")
    validate_route_string_list(value.get("evidence_refs"), f"{label} evidence_refs", allow_empty=True)
    return value


def validate_route_option(
    option: object,
    label: str,
    *,
    allowed_evidence_refs: set[str],
    enforce_selected_article_contract: bool = False,
) -> tuple[dict, dict]:
    fields = {
        "id", "format", "confidence", "fit_signals", "risk_signals", "rationale",
        "diagnostic_logic", "build_target_touchpoint_id", "touchpoints",
    }
    require(isinstance(option, dict) and set(option) == fields, f"{label} fields are invalid")
    require(nonempty_string(option.get("id")), f"{label} id is required")
    require(option.get("format") in ROUTE_FORMATS, f"{label} format is invalid")
    require(option.get("confidence") in ROUTE_CONFIDENCE, f"{label} confidence is invalid")
    for key in ("fit_signals", "risk_signals", "rationale"):
        validate_route_string_list(option.get(key), f"{label} {key}")
    if option["format"] == "diagnostic":
        diagnostic = option.get("diagnostic_logic")
        require(isinstance(diagnostic, dict)
                and set(diagnostic) == {"conditions", "outcomes"},
                f"{label} diagnostic route requires structured evidence-grounded decision logic")
        outcomes = diagnostic.get("outcomes")
        require(isinstance(outcomes, list) and len(outcomes) >= 2,
                f"{label} diagnostic logic requires at least two outcomes")
        outcome_ids: set[str] = set()
        results: set[str] = set()
        next_actions: set[str] = set()
        for outcome_index, outcome in enumerate(outcomes, start=1):
            require(isinstance(outcome, dict)
                    and set(outcome) == {"id", "result", "next_action"},
                    f"{label} diagnostic outcome {outcome_index} fields are invalid")
            outcome_id = outcome.get("id")
            require(nonempty_string(outcome_id) and outcome_id not in outcome_ids
                    and nonempty_string(outcome.get("result"))
                    and meaningful_action_label(outcome.get("next_action")),
                    f"{label} diagnostic outcome {outcome_index} is invalid")
            outcome_ids.add(outcome_id)
            results.add(normalized_route_semantics(outcome["result"]))
            next_actions.add(normalized_route_semantics(outcome["next_action"]))
        require(len(results) >= 2 and len(next_actions) >= 2,
                f"{label} diagnostic outcomes must produce materially different results and next actions")
        conditions = diagnostic.get("conditions")
        require(isinstance(conditions, list) and len(conditions) >= 2,
                f"{label} diagnostic logic requires at least two conditions")
        condition_ids: set[str] = set()
        normalized_conditions: set[str] = set()
        resolved_outcomes: set[str] = set()
        for condition_index, condition in enumerate(conditions, start=1):
            require(isinstance(condition, dict)
                    and set(condition) == {"id", "when", "evidence_refs", "outcome_id"},
                    f"{label} diagnostic condition {condition_index} fields are invalid")
            condition_id = condition.get("id")
            refs = validate_route_string_list(
                condition.get("evidence_refs"),
                f"{label} diagnostic condition {condition_index} evidence_refs",
            )
            require(nonempty_string(condition_id) and condition_id not in condition_ids
                    and nonempty_string(condition.get("when"))
                    and condition.get("outcome_id") in outcome_ids
                    and set(refs) <= allowed_evidence_refs,
                    f"{label} diagnostic condition {condition_index} authority is invalid")
            normalized_condition = normalized_route_semantics(condition["when"])
            require(normalized_condition and normalized_condition not in normalized_conditions,
                    f"{label} diagnostic conditions must be materially different")
            condition_ids.add(condition_id)
            normalized_conditions.add(normalized_condition)
            resolved_outcomes.add(condition["outcome_id"])
        require(resolved_outcomes == outcome_ids,
                f"{label} diagnostic conditions must resolve every outcome")
    else:
        require(option.get("diagnostic_logic") is None,
                f"{label} non-diagnostic route must keep diagnostic_logic null")

    touchpoints = option.get("touchpoints")
    require(isinstance(touchpoints, list) and touchpoints, f"{label} touchpoints must be non-empty")
    touchpoint_fields = {
        "id", "order", "surface_kind", "channel", "message_format", "destination_format",
        "persuasion_jobs", "current_state", "required_shift", "message_role", "exit_action",
    }
    exit_binding_fields = {"exit_action_kind", "exit_target_touchpoint_id"}
    ids: list[str] = []
    prior_shift: str | None = None
    assigned_jobs: set[str] = set()
    for index, touchpoint in enumerate(touchpoints, start=1):
        actual_fields = set(touchpoint) if isinstance(touchpoint, dict) else set()
        require(isinstance(touchpoint, dict)
                and (actual_fields == touchpoint_fields
                     or actual_fields == touchpoint_fields | exit_binding_fields),
                f"{label} touchpoint {index} fields are invalid")
        touchpoint_id = touchpoint.get("id")
        require(nonempty_string(touchpoint_id) and touchpoint_id not in ids,
                f"{label} touchpoint {index} id must be unique")
        ids.append(touchpoint_id)
        require(strict_int(touchpoint.get("order")) and touchpoint["order"] == index,
                f"{label} touchpoint {index} order is invalid")
        require(touchpoint.get("surface_kind") in {"creative", "destination", "sales"},
                f"{label} touchpoint {index} surface_kind is invalid")
        require(nonempty_string(touchpoint.get("channel"))
                and nonempty_string(touchpoint.get("message_format")),
                f"{label} touchpoint {index} channel/message_format is required")
        destination_format = touchpoint.get("destination_format")
        require(destination_format is None or destination_format in ROUTE_FORMATS,
                f"{label} touchpoint {index} destination_format is invalid")
        jobs = validate_route_string_list(
            touchpoint.get("persuasion_jobs"), f"{label} touchpoint {index} persuasion_jobs"
        )
        require(set(jobs) <= PERSUASION_JOBS,
                f"{label} touchpoint {index} persuasion_jobs are invalid")
        require(not (assigned_jobs & set(jobs)),
                f"{label} persuasion jobs cannot be duplicated across touchpoints")
        assigned_jobs.update(jobs)
        for key in ("current_state", "required_shift", "message_role", "exit_action"):
            require(nonempty_string(touchpoint.get(key)), f"{label} touchpoint {index} {key} is required")
        if prior_shift is not None:
            require(touchpoint["current_state"] == prior_shift,
                    f"{label} touchpoint {index} current_state must continue the prior required_shift")
        prior_shift = touchpoint["required_shift"]

    require("capture" in touchpoints[-1]["persuasion_jobs"],
            f"{label} final touchpoint must perform capture")
    target_id = option.get("build_target_touchpoint_id")
    require(target_id in ids, f"{label} build target does not resolve")
    target = touchpoints[ids.index(target_id)]
    require(target["surface_kind"] == "destination"
            and target["destination_format"] == option["format"],
            f"{label} build target must be the selected destination format")
    if option["format"] == "article_reframe" and enforce_selected_article_contract:
        article_jobs = set(target["persuasion_jobs"])
        require({"reframe", "educate"} <= article_jobs
                and article_jobs <= {"identify", "reframe", "educate"},
                f"{label} article_reframe build target must perform reframe and educate only; identify is optional and prove/offer/capture are forbidden")
        article_index = ids.index(target_id)
        final = touchpoints[-1]
        require(article_index < len(touchpoints) - 1
                and final["surface_kind"] == "destination"
                and final["destination_format"] == "direct_capture"
                and {"prove", "offer", "capture"} <= set(final["persuasion_jobs"]),
                f"{label} article_reframe requires a later final direct_capture service destination performing prove, offer, and capture")
        require(target.get("exit_action_kind") == "next_destination"
                and target.get("exit_target_touchpoint_id") == final["id"]
                and target["exit_action"] != final["exit_action"]
                and safe_article_handoff_action_label(target["exit_action"]),
                f"{label} article_reframe exit_action must be a safe informational next-destination CTA structurally bound to the final service destination")
        require(all(
            not (exit_binding_fields & set(touchpoint))
            for touchpoint in touchpoints if touchpoint is not target
        ), f"{label} article_reframe exit binding fields belong only on the article build target")
    elif option["format"] != "article_reframe":
        require(all(not (exit_binding_fields & set(touchpoint)) for touchpoint in touchpoints),
                f"{label} exit binding fields are reserved for an article_reframe build target")
    return option, target


def validate_acquisition_route_brief(document: dict) -> dict | None:
    brief = document.get("acquisition_route_brief")
    if brief is None:
        # Existing schema 1.5 artifacts remain readable/buildable. The current
        # lp-structure authoring Skill requires this extension for new output.
        return None
    fields = {
        "kind", "schema_version", "route_rule_version", "mode", "request_type",
        "project_context", "readiness", "strategy", "economics", "required_persuasion_jobs",
        "primary_route", "alternative_routes", "rejected_routes", "proof_plan",
        "conversion_action", "assumptions", "measurement_plan", "user_override",
    }
    require(isinstance(brief, dict) and set(brief) == fields,
            "acquisition_route_brief fields are invalid")
    require(brief.get("kind") == "acquisition-route-brief"
            and brief.get("schema_version") == "1.0"
            and brief.get("route_rule_version") == "acquisition-route-v1",
            "acquisition_route_brief identity/version is invalid")
    require(brief.get("mode") in {"free_light", "paid_quality"},
            "acquisition_route_brief mode is invalid")
    require(brief.get("request_type") in {"new_route", "lp_create", "route_audit", "improve_existing_route"},
            "acquisition_route_brief request_type is invalid")

    project_context = brief.get("project_context")
    if brief["mode"] == "free_light":
        require(project_context is None, "free_light route brief cannot include project context")
    else:
        require(isinstance(project_context, dict)
                and set(project_context) == {"project_id", "context_fingerprint"}
                and all(nonempty_string(project_context.get(key)) for key in project_context),
                "paid_quality route brief requires exact project/context binding")

    readiness = brief.get("readiness")
    require(isinstance(readiness, dict)
            and set(readiness) == {"status", "missing_critical", "missing_optional", "conflicts"},
            "acquisition_route_brief readiness fields are invalid")
    allowed_readiness = {"ready", "draft", "partial"} if document.get("schema_version") == STRUCTURE_SCHEMA_VERSION else {"ready"}
    require(readiness.get("status") in allowed_readiness,
            "a legacy structure document requires a ready acquisition route brief; new documents allow draft/partial")
    missing = validate_route_string_list(readiness.get("missing_critical"), "route missing_critical", allow_empty=True)
    require(readiness["status"] != "ready" or not missing,
            "ready acquisition route cannot have missing critical inputs")
    validate_route_string_list(readiness.get("missing_optional"), "route missing_optional", allow_empty=True)
    validate_route_string_list(readiness.get("conflicts"), "route conflicts", allow_empty=True)

    strategy = brief.get("strategy")
    strategy_fields = {
        "who", "current_state", "required_shifts", "what", "offer",
        "conversion_goal", "primary_barrier", "core_message",
    }
    require(isinstance(strategy, dict) and set(strategy) == strategy_fields,
            "acquisition_route_brief strategy fields are invalid")
    for key in strategy_fields - {"required_shifts"}:
        validate_route_sourced_value(strategy.get(key), f"route strategy {key}")
    shifts = strategy.get("required_shifts")
    require(isinstance(shifts, list) and shifts, "route strategy required_shifts must be non-empty")
    for index, shift in enumerate(shifts, start=1):
        validate_route_sourced_value(shift, f"route strategy required_shift {index}")
    if brief["mode"] == "free_light":
        paid_sources = {"paid_strategy", "paid_evidence", "paid_voc", "paid_results"}
        sourced_values = [strategy[key] for key in strategy_fields - {"required_shifts"}] + shifts
        require(not any(value["source"] in paid_sources for value in sourced_values),
                "free_light route brief cannot claim paid project sources")

    source_ids = {
        item["source_id"] for item in document.get("source_ledger", [])
        if isinstance(item, dict) and nonempty_string(item.get("source_id"))
    }
    paid_refs: set[str] = set()
    if brief["mode"] == "paid_quality":
        context_fingerprint = project_context["context_fingerprint"]
        require(bool(re.fullmatch(r"[0-9a-f]{64}", context_fingerprint)),
                "paid_quality route context_fingerprint is invalid")
        paid_refs = {
            f"context:{context_fingerprint}:{kind}"
            for kind in ROUTE_PAID_EVIDENCE_KINDS.values()
        }
    allowed_evidence_refs = source_ids | paid_refs
    sourced_values = [strategy[key] for key in strategy_fields - {"required_shifts"}] + shifts
    for value in sourced_values:
        refs = set(value["evidence_refs"])
        if value["source"] == "user_input":
            require(bool(refs) and refs <= source_ids,
                    "route user_input evidence_refs must resolve to source_ledger")
        elif value["source"] in ROUTE_PAID_EVIDENCE_KINDS:
            expected_ref = (
                f"context:{project_context['context_fingerprint']}:"
                f"{ROUTE_PAID_EVIDENCE_KINDS[value['source']]}"
                if project_context is not None else None
            )
            require(refs == {expected_ref},
                    "route paid evidence_refs must bind the exact project context fingerprint and authority")
        else:
            require(refs <= allowed_evidence_refs,
                    "route inference evidence_refs must resolve to an allowed authority")

    economics = brief.get("economics")
    require(isinstance(economics, dict)
            and set(economics) == {"status", "known_inputs", "missing_inputs", "conclusion"}
            and economics.get("status") in {"confirmed", "partial", "unconfirmed"}
            and nonempty_string(economics.get("conclusion")),
            "acquisition_route_brief economics fields are invalid")
    validate_route_string_list(economics.get("known_inputs"), "route economics known_inputs", allow_empty=True)
    validate_route_string_list(economics.get("missing_inputs"), "route economics missing_inputs", allow_empty=True)
    require(not (set(economics["known_inputs"]) & set(economics["missing_inputs"])),
            "route economics inputs cannot be both known and missing")
    require(economics["status"] != "confirmed" or not economics["missing_inputs"],
            "confirmed route economics cannot retain missing inputs")

    required_jobs = validate_route_string_list(
        brief.get("required_persuasion_jobs"), "required_persuasion_jobs"
    )
    require(set(required_jobs) <= PERSUASION_JOBS,
            "required_persuasion_jobs contains an invalid job")
    primary, build_target = validate_route_option(
        brief.get("primary_route"), "primary_route",
        allowed_evidence_refs=allowed_evidence_refs,
        enforce_selected_article_contract=True,
    )
    require(primary["format"] != "diagnostic",
            "diagnostic is not an available build target until every outcome is bound to a visible result and next action")
    require(primary["touchpoints"][0]["current_state"] == strategy["current_state"]["value"],
            "primary route must start from the sourced current state")
    sourced_shifts = {shift["value"] for shift in shifts}
    require(all(touchpoint["required_shift"] in sourced_shifts for touchpoint in primary["touchpoints"]),
            "primary route required shifts must resolve to sourced required_shifts")
    assigned_jobs = {
        job for touchpoint in primary["touchpoints"] for job in touchpoint["persuasion_jobs"]
    }
    require(set(required_jobs) == assigned_jobs,
            "primary route persuasion jobs must exactly match the required jobs")
    require("capture" in assigned_jobs, "primary route must carry the visitor to a capture action")

    alternatives = brief.get("alternative_routes")
    require(isinstance(alternatives, list) and alternatives,
            "acquisition_route_brief requires at least one alternative route")
    route_ids = {primary["id"]}
    considered_formats = {primary["format"]}
    for index, option in enumerate(alternatives, start=1):
        validated, _ = validate_route_option(
            option, f"alternative_route {index}",
            allowed_evidence_refs=allowed_evidence_refs,
        )
        require(validated["id"] not in route_ids, f"alternative_route {index} id is duplicated")
        route_ids.add(validated["id"])
        considered_formats.add(validated["format"])

    rejected = brief.get("rejected_routes")
    require(isinstance(rejected, list) and rejected,
            "acquisition_route_brief requires at least one rejected route")
    rejected_formats: set[str] = set()
    for index, item in enumerate(rejected, start=1):
        require(isinstance(item, dict) and set(item) == {"format", "reasons"}
                and item.get("format") in ROUTE_FORMATS
                and item["format"] not in considered_formats | rejected_formats,
                f"rejected_route {index} is invalid or duplicated")
        validate_route_string_list(item.get("reasons"), f"rejected_route {index} reasons")
        rejected_formats.add(item["format"])
    require(considered_formats | rejected_formats == ROUTE_FORMATS,
            "route brief must explicitly consider direct, article, and diagnostic formats")

    conversion = brief.get("conversion_action")
    require(isinstance(conversion, dict)
            and set(conversion) == {"kind", "label", "final_touchpoint_id"}
            and conversion.get("kind") in ROUTE_CTA_KINDS
            and meaningful_action_label(conversion.get("label"))
            and conversion.get("final_touchpoint_id") == primary["touchpoints"][-1]["id"]
            and conversion["label"] == primary["touchpoints"][-1]["exit_action"],
            "route conversion action must bind the final touchpoint")
    if primary["format"] == "article_reframe":
        require(conversion["kind"] != "next_destination"
                and conversion["final_touchpoint_id"] != build_target["id"]
                and conversion["label"] != build_target["exit_action"],
                "article_reframe conversion action must bind the later final service destination while the article exit_action remains the next-destination CTA")

    proof = brief.get("proof_plan")
    proof_fields = {
        "available_evidence", "evidence_gaps", "allowed_claim_ids",
        "disallowed_claims", "recommended_modules",
    }
    require(isinstance(proof, dict) and set(proof) == proof_fields,
            "acquisition_route_brief proof_plan fields are invalid")
    for key in proof_fields:
        validate_route_string_list(
            proof.get(key), f"route proof_plan {key}",
            allow_empty=key in {"available_evidence", "evidence_gaps", "allowed_claim_ids", "disallowed_claims"},
        )
    require(set(proof["recommended_modules"]) <= ROUTE_PROOF_MODULES,
            "route proof_plan recommended_modules are invalid")
    claim_ids = {claim.get("claim_id") for claim in document.get("claim_source_ledger", []) if isinstance(claim, dict)}
    require(set(proof["allowed_claim_ids"]) <= claim_ids,
            "route proof_plan allowed_claim_ids do not resolve")

    assumptions = brief.get("assumptions")
    require(isinstance(assumptions, list), "route assumptions must be an array")
    assumption_ids: set[str] = set()
    for index, assumption in enumerate(assumptions, start=1):
        require(isinstance(assumption, dict)
                and set(assumption) == {"id", "statement", "confidence", "impact", "validation_method"},
                f"route assumption {index} fields are invalid")
        require(nonempty_string(assumption.get("id")) and assumption["id"] not in assumption_ids,
                f"route assumption {index} id must be unique")
        assumption_ids.add(assumption["id"])
        require(nonempty_string(assumption.get("statement"))
                and assumption.get("confidence") in ROUTE_CONFIDENCE
                and assumption.get("impact") in {"high", "medium", "low"}
                and (assumption.get("validation_method") is None
                     or nonempty_string(assumption.get("validation_method"))),
                f"route assumption {index} is invalid")

    measurement = brief.get("measurement_plan")
    measurement_fields = {
        "primary_outcome", "leading_indicators", "evaluation_window",
        "decision_rules", "segments", "warnings",
    }
    require(isinstance(measurement, dict) and set(measurement) == measurement_fields,
            "acquisition_route_brief measurement_plan fields are invalid")
    require(measurement.get("primary_outcome") == strategy["conversion_goal"]["value"],
            "route measurement primary outcome must bind conversion_goal")
    for key in ("leading_indicators", "decision_rules", "segments", "warnings"):
        validate_route_string_list(measurement.get(key), f"route measurement {key}", allow_empty=key in {"segments", "warnings"})
    require(measurement.get("evaluation_window") is None
            or nonempty_string(measurement.get("evaluation_window")),
            "route measurement evaluation_window is invalid")

    override = brief.get("user_override")
    override_fields = {"applied", "selected_route_id", "recommended_route_id", "reason", "correction_plan"}
    require(isinstance(override, dict) and set(override) == override_fields
            and isinstance(override.get("applied"), bool),
            "acquisition_route_brief user_override fields are invalid")
    if override["applied"]:
        require(override.get("selected_route_id") == primary["id"]
                and override.get("recommended_route_id") in route_ids
                and override["recommended_route_id"] != override["selected_route_id"]
                and nonempty_string(override.get("reason")),
                "applied route override must preserve selected and recommended route identities")
        recommended_route = next(
            option for option in alternatives
            if option["id"] == override["recommended_route_id"]
        )
        require(recommended_route["format"] != "diagnostic",
                "diagnostic cannot be a recommended route until every outcome is bound to a visible result and next action")
        validate_route_string_list(override.get("correction_plan"), "route override correction_plan")
    else:
        require(override.get("selected_route_id") is None
                and override.get("recommended_route_id") is None
                and override.get("reason") is None
                and override.get("correction_plan") == [],
                "unused route override fields must be null/empty")

    require(document.get("audience") == strategy["who"]["value"],
            "route WHO must bind the structure audience")
    require(document.get("offer") == strategy["offer"]["value"],
            "route offer must bind the structure offer")
    require(document.get("objective") == strategy["conversion_goal"]["value"],
            "route conversion goal must bind the structure objective")
    require(document.get("primary_cta") == build_target["exit_action"],
            "structure primary CTA must bind the selected build touchpoint exit action")
    handoff = document.get("fv_handoff", {})
    five_second = handoff.get("five_second", {}) if isinstance(handoff, dict) else {}
    scan_contract = handoff.get("scan_contract", {}) if isinstance(handoff, dict) else {}
    context_assessment = handoff.get("context_assessment", {}) if isinstance(handoff, dict) else {}
    require(five_second.get("audience") == strategy["who"]["value"]
            and scan_contract.get("relevance", {}).get("answer") == strategy["who"]["value"],
            "route WHO must bind the visible FV audience and relevance answer")
    require(scan_contract.get("what_it_is", {}).get("answer") == strategy["what"]["value"],
            "route WHAT must bind the visible FV what_it_is answer")
    require(five_second.get("promise_or_offer") == strategy["offer"]["value"]
            and scan_contract.get("core_benefit", {}).get("answer") == strategy["offer"]["value"]
            and context_assessment.get("source_offer") == strategy["offer"]["value"],
            "route offer must bind the visible FV offer")
    require(handoff.get("dominant_message") == strategy["core_message"]["value"],
            "route core message must bind the FV dominant_message")
    belief = handoff.get("belief_shift", {}) if isinstance(handoff, dict) else {}
    require(belief.get("from") == build_target["current_state"]
            and belief.get("to") == build_target["required_shift"],
            "FV belief shift must bind the selected build touchpoint")
    section_jobs: set[str] = set()
    for index, section in enumerate(document.get("sections", []), start=1):
        jobs = validate_route_string_list(
            section.get("persuasion_jobs"), f"structure section {index} persuasion_jobs"
        )
        require(set(jobs) <= PERSUASION_JOBS,
                f"structure section {index} persuasion_jobs are invalid")
        section_jobs.update(jobs)
    require(set(build_target["persuasion_jobs"]) == section_jobs,
            "structure sections must exactly cover the selected destination persuasion jobs")
    return brief


def validate_fv_content_budget(document: dict, handoff: dict, first_section_id: str) -> dict:
    budget = handoff.get("fv_content_budget")
    fields = {"profile", "rationale", "visible_items", "deferred_items", "guardrail_assessment"}
    require(isinstance(budget, dict) and set(budget) == fields, "fv_content_budget fields are invalid")
    profile = budget.get("profile")
    require(profile in FV_CONTENT_BUDGETS, "fv_content_budget profile must be lean, standard, or reassurance-heavy")
    require(nonempty_string(budget.get("rationale")), "fv_content_budget rationale is required")
    limits = FV_CONTENT_BUDGETS[profile]

    visible = budget.get("visible_items")
    require(isinstance(visible, list) and visible, "fv_content_budget visible_items must be non-empty")
    visible_fields = {"id", "semantic_role", "copy_key", "text", "visual_weight", "claim_id"}
    seen_ids: set[str] = set()
    roles: dict[str, list[dict]] = {role: [] for role in FV_SEMANTIC_ROLES}
    for index, item in enumerate(visible, start=1):
        require(isinstance(item, dict) and set(item) == visible_fields, f"fv_content_budget visible item {index} fields are invalid")
        item_id = item.get("id")
        role = item.get("semantic_role")
        require(isinstance(item_id, str) and FV_ITEM_ID_PATTERN.fullmatch(item_id) and item_id not in seen_ids,
                f"fv_content_budget visible item {index} id must be a unique stable token")
        require(role in FV_SEMANTIC_ROLES, f"fv_content_budget visible item {index} semantic_role is invalid")
        require(nonempty_string(item.get("copy_key")), f"fv_content_budget visible item {index} copy_key is required")
        require(nonempty_string(item.get("text")), f"fv_content_budget visible item {index} text is required")
        require(item.get("visual_weight") in FV_VISUAL_WEIGHTS, f"fv_content_budget visible item {index} visual_weight is invalid")
        if item["visual_weight"] == "micro":
            require(non_whitespace_length(item["text"]) <= FV_MICRO_MAX_CHARS,
                    f"fv_content_budget visible item {index} micro text exceeds {FV_MICRO_MAX_CHARS} characters")
        claim_id = item.get("claim_id")
        require(claim_id is None or nonempty_string(claim_id), f"fv_content_budget visible item {index} claim_id is invalid")
        require((role == "proof") == (claim_id is not None),
                f"fv_content_budget visible item {index} proof role and claim_id must be paired")
        seen_ids.add(item_id)
        roles[role].append(item)

    visible_chars = sum(non_whitespace_length(item["text"]) for item in visible)
    guardrail = budget.get("guardrail_assessment")
    actual_counts = {
        "char_count": visible_chars,
        "item_count": len(visible),
        "proof_count": len(roles["proof"]),
    }
    within_profile = (
        visible_chars <= limits["max_chars"]
        and len(visible) <= limits["max_items"]
        and len(roles["proof"]) <= limits["max_proofs"]
    )
    require(
        isinstance(guardrail, dict)
        and set(guardrail) == {"char_count", "item_count", "proof_count", "status", "rationale"}
        and all(strict_int(guardrail.get(key)) for key in actual_counts)
        and all(guardrail.get(key) == value for key, value in actual_counts.items())
        and guardrail.get("status") == ("within-profile" if within_profile else "context-exception")
        and nonempty_string(guardrail.get("rationale")),
        "fv_content_budget guardrail assessment must report exact counts and context-sensitive status",
    )
    for role in ("support", "audience", "provider"):
        require(len(roles[role]) <= 1, f"fv_content_budget allows at most one visible {role} item")
    for role in ("secondary-action", "availability"):
        require(len(roles[role]) <= 1, f"fv_content_budget allows at most one visible {role} item")
    require(len(roles["dominant"]) == 1, "fv_content_budget requires exactly one dominant item")
    require(len(roles["action"]) == 1, "fv_content_budget requires exactly one action item")
    require(roles["dominant"][0]["visual_weight"] == "primary", "fv_content_budget dominant item must carry primary visual weight")
    require(sum(item["visual_weight"] == "primary" for item in visible) == 1,
            "fv_content_budget requires one primary item so the dominant message remains singular")

    copy = document["sections"][0].get("copy")
    leaves = [(key, value) for key, value in first_section_copy_leaves(copy) if value]
    leaf_keys = [key for key, _ in leaves]
    observed_key_order: list[str] = []
    for item in visible:
        key = item["copy_key"]
        require(key in leaf_keys, f"fv_content_budget visible item copy_key does not resolve: {key}")
        if not observed_key_order or observed_key_order[-1] != key:
            require(key not in observed_key_order, f"fv_content_budget visible items for copy key {key} must be contiguous")
            observed_key_order.append(key)
    require(observed_key_order == leaf_keys,
            "fv_content_budget visible item copy keys must cover every non-empty first-section copy leaf in order")
    for key, exact_copy in leaves:
        covered = "".join(item["text"] for item in visible if item["copy_key"] == key)
        require(covered == exact_copy,
                f"fv_content_budget visible items must completely cover first-section copy leaf {key} in order")

    require(roles["dominant"][0]["text"] == handoff["dominant_message"],
            "fv_content_budget dominant item must exactly equal dominant_message")
    require(roles["action"][0]["text"] == handoff["five_second"]["next_action"],
            "fv_content_budget action item must exactly equal next_action")
    belief_expression = handoff["belief_shift"]["visible_expression"]
    require(any(belief_expression in item["text"] for item in roles["dominant"] + roles["support"]),
            "fv_content_budget must bind the exact belief visible_expression inside a dominant or support item")

    claims = verified_claims(document) if roles["proof"] or handoff["credibility"]["decision"] == "visible" else {}
    for index, item in enumerate(roles["proof"], start=1):
        claim_id = item["claim_id"]
        require(claim_id in claims, f"fv_content_budget proof item {index} claim_id does not resolve")
        claim = claims[claim_id]
        require(claim.get("status") in {"verified", "確認済み"}, f"fv_content_budget proof item {index} claim is not verified")
        require(nonempty_string(claim.get("claim")) and item["text"] in claim["claim"],
                f"fv_content_budget proof item {index} text must be an exact claim-supported phrase")
        require(isinstance(claim.get("use_sections"), list) and first_section_id in claim["use_sections"],
                f"fv_content_budget proof item {index} claim must authorize the first section")

    deferred = budget.get("deferred_items")
    require(isinstance(deferred, list), "fv_content_budget deferred_items must be an array")
    deferred_fields = {"id", "semantic_role", "text", "claim_id", "destination_section_id", "rationale"}
    section_ids = [section.get("id") for section in document["sections"]]
    deferred_roles: dict[str, list[dict]] = {role: [] for role in FV_SEMANTIC_ROLES}
    deferred_claims: dict[str, dict] | None = None
    for index, item in enumerate(deferred, start=1):
        require(isinstance(item, dict) and set(item) == deferred_fields, f"fv_content_budget deferred item {index} fields are invalid")
        item_id = item.get("id")
        role = item.get("semantic_role")
        require(isinstance(item_id, str) and FV_ITEM_ID_PATTERN.fullmatch(item_id) and item_id not in seen_ids,
                f"fv_content_budget deferred item {index} id must be a unique stable token")
        require(role in FV_SEMANTIC_ROLES, f"fv_content_budget deferred item {index} semantic_role is invalid")
        require(nonempty_string(item.get("text")) and nonempty_string(item.get("rationale")),
                f"fv_content_budget deferred item {index} text/rationale is required")
        destination = item.get("destination_section_id")
        require(destination in section_ids[1:],
                f"fv_content_budget deferred item {index} destination must be a real later section")
        destination_section = document["sections"][section_ids.index(destination)]
        destination_leaves = first_section_copy_leaves(destination_section.get("copy"))
        require(any(item["text"] in leaf for _, leaf in destination_leaves),
                f"fv_content_budget deferred item {index} text must appear exactly in one destination section copy leaf")
        claim_id = item.get("claim_id")
        require(claim_id is None or nonempty_string(claim_id), f"fv_content_budget deferred item {index} claim_id is invalid")
        require((role == "proof") == (claim_id is not None),
                f"fv_content_budget deferred item {index} proof role and claim_id must be paired")
        if role == "proof":
            deferred_claims = deferred_claims or verified_claims(document)
            require(claim_id in deferred_claims, f"fv_content_budget deferred proof item {index} claim_id does not resolve")
            claim = deferred_claims[claim_id]
            require(claim.get("status") in {"verified", "確認済み"}, f"fv_content_budget deferred proof item {index} claim is not verified")
            require(nonempty_string(claim.get("claim")) and item["text"] in claim["claim"],
                    f"fv_content_budget deferred proof item {index} text must be an exact claim-supported phrase")
            require(isinstance(claim.get("use_sections"), list) and destination in claim["use_sections"],
                    f"fv_content_budget deferred proof item {index} claim must authorize its destination section")
        seen_ids.add(item_id)
        deferred_roles[role].append(item)

    identity = handoff["identity_recognition"]
    if identity["decision"] == "visible":
        require(len(roles["audience"]) == 1 and roles["audience"][0]["text"] == identity["recognition_target"],
                "visible identity recognition must bind one exact audience item")
    else:
        require(not roles["audience"] and deferred_roles["audience"],
                "deferred identity recognition must bind a later audience item and no visible audience item")
    provider = handoff["provider_recognition"]
    if provider["decision"] == "visible":
        require(len(roles["provider"]) == 1 and provider["provider_name"] in roles["provider"][0]["text"],
                "visible provider recognition must bind one provider item containing the exact provider_name")
    else:
        require(not roles["provider"] and deferred_roles["provider"],
                "deferred provider recognition must bind a later provider item and no visible provider item")
    credibility = handoff["credibility"]
    if credibility["decision"] == "visible":
        expected = [{"claim_id": item["claim_id"], "text": item["text"]} for item in roles["proof"]]
        require(expected == credibility["visible_expressions"],
                "visible credibility expressions must bind the ordered proof items exactly")
    elif has_no_available_proof(document):
        require(not roles["proof"] and not deferred_roles["proof"],
                "unavailable credibility must not invent visible or deferred proof")
    else:
        require(not roles["proof"] and deferred_roles["proof"],
                "deferred credibility must bind a later proof item and no visible proof item")
    if document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
        direct = document["cta_strategy"]["direct_call"]
        if direct["decision"] == "enabled" and direct["section_id"] == first_section_id:
            require(len(roles["secondary-action"]) == 1
                    and roles["secondary-action"][0]["text"] == direct["label"],
                    "FV direct_call label must bind one exact secondary-action item")
            require(len(roles["availability"]) == 1
                    and roles["availability"][0]["text"] == direct["availability_copy"],
                    "FV direct_call availability must bind one exact availability item")
        else:
            require(not roles["secondary-action"] and not roles["availability"],
                    "FV cannot show an unapproved direct-call secondary action")
    return budget


def has_no_available_proof(document: dict) -> bool:
    proof = document.get("authentic_proof", {})
    availability = proof.get("availability", {})
    return (
        document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS
        and proof.get("selected_mode") == "none"
        and proof.get("items") == []
        and set(availability) == {"customer-face", "handwritten-feedback", "verified-fallback"}
        and all(isinstance(item, dict) and item.get("status") == "unavailable"
                for item in availability.values())
    )


def validate_fv_handoff(document: dict, first_section_id: str) -> dict | None:
    schema_version = document.get("schema_version")
    if schema_version in {"1.1", "1.2"}:
        if schema_version == "1.2":
            return validate_fv_handoff_1_2(document, first_section_id)
        return None

    require("fv_handoff" in document, f"schema {schema_version} structure requires fv_handoff")
    handoff = document.get("fv_handoff")
    fields = {
        "five_second", "dominant_message", "belief_shift", "visual_job", "credibility",
        "identity_recognition", "provider_recognition", "avoid_impressions",
    }
    if schema_version in {"1.4"} | MODERN_STRUCTURE_SCHEMA_VERSIONS:
        fields |= {"fv_content_budget", "context_assessment", "scan_contract"}
    require(isinstance(handoff, dict) and set(handoff) == fields, "fv_handoff fields are invalid")

    five = handoff.get("five_second")
    require(
        isinstance(five, dict)
        and set(five) == {"audience", "promise_or_offer", "next_action"},
        "fv_handoff.five_second fields are invalid",
    )
    require(nonempty_string(five.get("audience")), "fv_handoff audience is required")
    require(nonempty_string(five.get("promise_or_offer")), "fv_handoff promise_or_offer is required")
    require(meaningful_action_label(five.get("next_action")), "fv_handoff next_action must be a meaningful visible action label")
    require(nonempty_string(handoff.get("dominant_message")), "fv_handoff dominant_message is required")
    if schema_version in {"1.4"} | MODERN_STRUCTURE_SCHEMA_VERSIONS:
        context = handoff.get("context_assessment")
        context_fields = {
            "traffic_source_message", "source_message_match", "source_offer", "source_action",
            "awareness", "category_familiarity", "offer_complexity", "decision_risk",
            "proof_strength", "visual_explanatory_power", "action_readiness", "regulatory_class",
        }
        require(
            isinstance(context, dict)
            and set(context) == context_fields
            and all(nonempty_string(context.get(key)) for key in context_fields - {"source_message_match"})
            and (context.get("source_message_match") == "matched" or (
                context.get("source_message_match") == "unconfirmed"
                and schema_version == STRUCTURE_SCHEMA_VERSION
                and document.get("approval_contract", {}).get("request", {}).get("hypothesis_design") is True
            )),
            "fv_handoff context_assessment fields are invalid or source message is mismatched",
        )
        require(context["source_offer"] == five["promise_or_offer"],
                "fv_handoff source offer must exactly match promise_or_offer")
        require(context["source_action"] == five["next_action"],
                "fv_handoff source action must exactly match next_action")
        scan = handoff.get("scan_contract")
        scan_keys = {"relevance", "what_it_is", "core_benefit", "trust_basis", "next_action"}
        require(isinstance(scan, dict) and set(scan) == scan_keys, "fv_handoff scan_contract fields are invalid")
        allowed_modes = {"copy", "visual", "proof", "cta"}
        for key in scan_keys:
            outcome = scan.get(key)
            require(
                isinstance(outcome, dict)
                and set(outcome) == {"answer", "evidence_modes", "rationale"}
                and nonempty_string(outcome.get("answer"))
                and isinstance(outcome.get("evidence_modes"), list)
                and outcome["evidence_modes"]
                and all(mode in allowed_modes for mode in outcome["evidence_modes"])
                and len(outcome["evidence_modes"]) == len(set(outcome["evidence_modes"]))
                and nonempty_string(outcome.get("rationale")),
                f"fv_handoff scan_contract {key} is invalid",
            )
        require(scan["next_action"]["answer"] == five["next_action"] and "cta" in scan["next_action"]["evidence_modes"],
                "fv_handoff scan next_action must bind the exact CTA")
        require(scan["core_benefit"]["answer"] == five["promise_or_offer"],
                "fv_handoff scan core_benefit must bind the exact offer")
        if has_no_available_proof(document):
            require(handoff.get("credibility", {}).get("decision") == "deferred"
                    and scan["trust_basis"]["evidence_modes"] == ["copy"],
                    "unavailable trust basis must disclose missing proof in copy, not imply proof or visual evidence")
            disclosure = scan["trust_basis"]["answer"]
            require(disclosure in section_authority_copy(document["sections"][0])
                    and any(disclosure in item.get("text", "") for item in handoff.get("fv_content_budget", {}).get("visible_items", [])),
                    "unavailable trust basis disclosure must appear in visible FV copy")
        else:
            require("proof" in scan["trust_basis"]["evidence_modes"] or "visual" in scan["trust_basis"]["evidence_modes"],
                    "fv_handoff scan trust_basis must identify proof or visual evidence")
    authority_copy = section_authority_copy(document["sections"][0])
    belief = handoff.get("belief_shift")
    require(
        isinstance(belief, dict)
        and set(belief) == {"from", "to", "visible_expression"}
        and nonempty_string(belief.get("from"))
        and nonempty_string(belief.get("to"))
        and nonempty_string(belief.get("visible_expression")),
        "fv_handoff belief_shift is invalid",
    )
    require(
        belief["visible_expression"] in authority_copy,
        "fv_handoff belief_shift visible_expression must appear exactly in first-section authority copy",
    )
    require(nonempty_string(handoff.get("visual_job")), "fv_handoff visual_job outcome is required")

    credibility = handoff.get("credibility")
    require(
        isinstance(credibility, dict)
        and set(credibility) == {"decision", "evidence_refs", "visible_expressions", "rationale"}
        and credibility.get("decision") in {"visible", "deferred"}
        and isinstance(credibility.get("evidence_refs"), list)
        and isinstance(credibility.get("visible_expressions"), list)
        and nonempty_string(credibility.get("rationale")),
        "fv_handoff credibility is invalid",
    )
    refs = credibility["evidence_refs"]
    expressions = credibility["visible_expressions"]
    require(
        all(nonempty_string(ref) for ref in refs) and len(refs) == len(set(refs)),
        "fv_handoff credibility evidence_refs must be unique claim ids",
    )
    if credibility["decision"] == "visible":
        require(refs, "visible FV credibility requires evidence_refs")
        require(
            len(expressions) == len(refs),
            "visible FV credibility requires one visible expression per evidence_ref",
        )
        ledger = document.get("claim_source_ledger")
        require(isinstance(ledger, list), "visible FV credibility requires claim_source_ledger")
        claims: dict[str, dict] = {}
        for index, claim in enumerate(ledger, start=1):
            require(isinstance(claim, dict), f"claim_source_ledger item {index} must be an object")
            claim_id = claim.get("claim_id")
            require(nonempty_string(claim_id) and claim_id not in claims, f"claim_source_ledger item {index} claim_id must be unique")
            claims[claim_id] = claim
        for ref in refs:
            require(ref in claims, f"FV credibility evidence_ref does not resolve: {ref}")
            claim = claims[ref]
            require(nonempty_string(claim.get("claim")), f"FV credibility claim {ref} requires concrete claim text")
            source_ids = claim.get("source_ids")
            require(
                isinstance(source_ids, list)
                and source_ids
                and all(nonempty_string(source_id) for source_id in source_ids)
                and len(source_ids) == len(set(source_ids)),
                f"FV credibility claim {ref} requires non-empty unique source_ids",
            )
            require(claim.get("status") in {"verified", "確認済み"}, f"FV credibility claim {ref} status is not verified")
            use_sections = claim.get("use_sections")
            require(
                isinstance(use_sections, list) and first_section_id in use_sections,
                f"FV credibility claim {ref} must include first section in use_sections",
            )
        expression_fields = {"claim_id", "text"}
        expression_ids: list[str] = []
        for index, expression in enumerate(expressions, start=1):
            require(
                isinstance(expression, dict) and set(expression) == expression_fields,
                f"FV credibility visible expression {index} fields are invalid",
            )
            claim_id = expression.get("claim_id")
            text = expression.get("text")
            require(claim_id in refs and claim_id not in expression_ids, f"FV credibility visible expression {index} claim binding is invalid")
            require(nonempty_string(text), f"FV credibility visible expression {index} text is required")
            require(text in authority_copy, f"FV credibility visible expression {index} must appear exactly in first-section authority copy")
            require(text in claims[claim_id]["claim"], f"FV credibility visible expression {index} must appear exactly in its source-ledger claim")
            expression_ids.append(claim_id)
        require(expression_ids == refs, "FV credibility visible expressions must follow evidence_refs exactly")
    else:
        require(not refs, "deferred FV credibility requires empty evidence_refs")
        require(not expressions, "deferred FV credibility requires empty visible_expressions")

    identity = handoff.get("identity_recognition")
    require(
        isinstance(identity, dict)
        and set(identity) == {"decision", "recognition_target", "rationale"}
        and identity.get("decision") in {"visible", "deferred"}
        and nonempty_string(identity.get("rationale")),
        "fv_handoff identity_recognition is invalid",
    )
    if identity["decision"] == "visible":
        require(nonempty_string(identity.get("recognition_target")), "visible identity recognition requires recognition_target")
    else:
        require(identity.get("recognition_target") is None, "deferred identity recognition requires null recognition_target")

    provider = handoff.get("provider_recognition")
    require(
        isinstance(provider, dict)
        and set(provider) == {"decision", "provider_name", "rationale"}
        and provider.get("decision") in {"visible", "deferred"}
        and nonempty_string(provider.get("rationale")),
        "fv_handoff provider_recognition is invalid",
    )
    if provider["decision"] == "visible":
        require(nonempty_string(provider.get("provider_name")), "visible provider recognition requires exact provider_name")
        require(provider["provider_name"] in authority_copy, "visible provider_name must appear exactly in first-section authority copy")
    else:
        require(provider.get("provider_name") is None, "deferred provider recognition requires null provider_name")

    require(
        document["sections"][0]["copy"].get("cta") == five["next_action"],
        f"schema {schema_version} first-section CTA copy must exactly equal fv_handoff next_action",
    )

    avoid = handoff.get("avoid_impressions")
    require(
        isinstance(avoid, list)
        and avoid
        and all(nonempty_string(item) for item in avoid)
        and len(avoid) == len(set(avoid)),
        "fv_handoff avoid_impressions must be a non-empty unique list",
    )
    if schema_version in {"1.4"} | MODERN_STRUCTURE_SCHEMA_VERSIONS:
        validate_fv_content_budget(document, handoff, first_section_id)
    return handoff


def validate_fv_handoff_1_2(document: dict, first_section_id: str) -> dict:
    """Preserve schema 1.2 as a read-only compatibility contract."""

    handoff = document.get("fv_handoff")
    fields = {
        "five_second", "dominant_message", "belief_shift", "visual_job", "credibility",
        "identity_recognition", "avoid_impressions",
    }
    require(isinstance(handoff, dict) and set(handoff) == fields, "fv_handoff fields are invalid")
    five = handoff.get("five_second")
    require(isinstance(five, dict) and set(five) == {"audience", "promise_or_offer", "next_action"}, "fv_handoff.five_second fields are invalid")
    require(nonempty_string(five.get("audience")) and nonempty_string(five.get("promise_or_offer")), "fv_handoff five_second outcomes are required")
    require(meaningful_action_label(five.get("next_action")), "fv_handoff next_action must be a meaningful visible action label")
    require(nonempty_string(handoff.get("dominant_message")) and nonempty_string(handoff.get("visual_job")), "fv_handoff dominant_message/visual_job is required")
    belief = handoff.get("belief_shift")
    require(isinstance(belief, dict) and set(belief) == {"from", "to"} and all(nonempty_string(belief.get(key)) for key in ("from", "to")), "fv_handoff belief_shift is invalid")
    credibility = handoff.get("credibility")
    require(isinstance(credibility, dict) and set(credibility) == {"decision", "evidence_refs", "rationale"} and credibility.get("decision") in {"visible", "deferred"} and isinstance(credibility.get("evidence_refs"), list) and nonempty_string(credibility.get("rationale")), "fv_handoff credibility is invalid")
    refs = credibility["evidence_refs"]
    require(all(nonempty_string(ref) for ref in refs) and len(refs) == len(set(refs)), "fv_handoff credibility evidence_refs must be unique claim ids")
    if credibility["decision"] == "visible":
        require(refs, "visible FV credibility requires evidence_refs")
        ledger = document.get("claim_source_ledger")
        require(isinstance(ledger, list), "visible FV credibility requires claim_source_ledger")
        claims = {claim.get("claim_id"): claim for claim in ledger if isinstance(claim, dict) and nonempty_string(claim.get("claim_id"))}
        require(len(claims) == len(ledger), "claim_source_ledger claim_id must be unique")
        for ref in refs:
            require(ref in claims, f"FV credibility evidence_ref does not resolve: {ref}")
            claim = claims[ref]
            require(nonempty_string(claim.get("claim")), f"FV credibility claim {ref} requires concrete claim text")
            source_ids = claim.get("source_ids")
            require(isinstance(source_ids, list) and source_ids and all(nonempty_string(value) for value in source_ids) and len(source_ids) == len(set(source_ids)), f"FV credibility claim {ref} requires non-empty unique source_ids")
            require(claim.get("status") in {"verified", "確認済み"}, f"FV credibility claim {ref} status is not verified")
            require(isinstance(claim.get("use_sections"), list) and first_section_id in claim["use_sections"], f"FV credibility claim {ref} must include first section in use_sections")
    else:
        require(not refs, "deferred FV credibility requires empty evidence_refs")
    identity = handoff.get("identity_recognition")
    require(isinstance(identity, dict) and set(identity) == {"decision", "recognition_target", "rationale"} and identity.get("decision") in {"visible", "deferred"} and nonempty_string(identity.get("rationale")), "fv_handoff identity_recognition is invalid")
    require(nonempty_string(identity.get("recognition_target")) if identity["decision"] == "visible" else identity.get("recognition_target") is None, "fv_handoff identity_recognition target is invalid")
    avoid = handoff.get("avoid_impressions")
    require(isinstance(avoid, list) and avoid and all(nonempty_string(value) for value in avoid) and len(avoid) == len(set(avoid)), "fv_handoff avoid_impressions must be a non-empty unique list")
    return handoff


def validate_structure_document(document: dict, evidence_root: Path | None = None) -> tuple[list[dict], list[dict], list[dict]]:
    require(
        document.get("kind") == "lp-structure-document"
        and document.get("schema_version") in READ_ONLY_STRUCTURE_SCHEMA_VERSIONS | {STRUCTURE_SCHEMA_VERSION},
        "structure document type/schema is invalid",
    )
    require(document.get("schema_version") == STRUCTURE_SCHEMA_VERSION or "approval_contract" not in document,
            "approval_contract cannot be downgraded to a legacy structure schema")
    sections = document.get("sections")
    require(isinstance(sections, list) and sections, "structure document sections must be non-empty")
    section_ids: list[str] = []
    for index, section in enumerate(sections, start=1):
        require(isinstance(section, dict), f"structure section {index} must be an object")
        section_id = section.get("id")
        require(nonempty_string(section_id) and section_id not in section_ids, f"structure section {index} id must be unique")
        require(strict_int(section.get("order")) and section.get("order") == index,
                f"structure section {section_id} order must be {index}")
        copy = section.get("copy")
        require(
            isinstance(copy, dict)
            and isinstance(copy.get("headline"), str)
            and isinstance(copy.get("body"), str),
            f"structure section {section_id} copy is invalid",
        )
        section_ids.append(section_id)

    validate_fv_handoff(document, section_ids[0])

    if document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
        sources = validate_source_ledger(document, evidence_root)
        validate_authentic_proof(document, section_ids, sources)
        validate_cta_strategy(document, section_ids, sources)
        validate_acquisition_route_brief(document)
        if document.get("schema_version") == STRUCTURE_SCHEMA_VERSION:
            validate_approval_contract(document, sources)

    boundaries = document.get("adjacent_boundary_plan")
    require(isinstance(boundaries, list), "adjacent_boundary_plan must be an array")
    require(len(boundaries) == max(0, len(sections) - 1), "adjacent_boundary_plan must contain exactly N-1 boundaries")
    boundary_fields = {
        "order", "from_section_id", "to_section_id", "why_next", "mechanism", "transition_copy"
    }
    if document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
        boundary_fields.add("bridge_plan")
    for index, boundary in enumerate(boundaries, start=1):
        require(isinstance(boundary, dict) and set(boundary) == boundary_fields, f"boundary {index} fields are invalid")
        require(strict_int(boundary.get("order")) and boundary.get("order") == index,
                f"boundary {index} order is invalid")
        require(
            boundary.get("from_section_id") == section_ids[index - 1]
            and boundary.get("to_section_id") == section_ids[index],
            f"boundary {index} must bind the adjacent approved sections in order",
        )
        require(nonempty_string(boundary.get("why_next")), f"boundary {index} why_next is required")
        mechanism = boundary.get("mechanism")
        require(mechanism in BOUNDARY_MECHANISMS, f"boundary {index} mechanism is invalid; decorative arrows alone are not a mechanism")
        transition_copy = boundary.get("transition_copy")
        if mechanism == "copy":
            require(nonempty_string(transition_copy), f"boundary {index} copy mechanism requires transition_copy")
        elif mechanism != "mixed":
            require(transition_copy is None, f"boundary {index} non-copy mechanism must keep transition_copy null")
        else:
            require(transition_copy is None or nonempty_string(transition_copy), f"boundary {index} transition_copy is invalid")
        if document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
            validate_bridge_plan(boundary.get("bridge_plan"), transition_copy, index)

    require("repeated_series" in document, "repeated_series must be explicitly present")
    series = document.get("repeated_series")
    require(isinstance(series, list), "repeated_series must be an array")
    series_ids: set[str] = set()
    series_fields = {"id", "members", "recognizable_cues"}
    member_fields = {"section_id", "component_id"}
    for series_index, item in enumerate(series, start=1):
        require(isinstance(item, dict) and set(item) == series_fields, f"repeated_series item {series_index} fields are invalid")
        series_id = item.get("id")
        require(nonempty_string(series_id) and series_id not in series_ids, f"repeated_series item {series_index} id must be unique")
        series_ids.add(series_id)
        members = item.get("members")
        require(isinstance(members, list) and len(members) >= 2, f"series {series_id} requires at least two members")
        member_positions: list[int] = []
        seen_members: set[tuple[str, str | None]] = set()
        for member_index, member in enumerate(members, start=1):
            require(isinstance(member, dict) and set(member) == member_fields, f"series {series_id} member {member_index} fields are invalid")
            section_id = member.get("section_id")
            component_id = member.get("component_id")
            require(section_id in section_ids, f"series {series_id} member {member_index} section_id is invalid")
            require(component_id is None or nonempty_string(component_id), f"series {series_id} member {member_index} component_id is invalid")
            key = (section_id, component_id)
            require(key not in seen_members, f"series {series_id} member {member_index} is duplicated")
            seen_members.add(key)
            member_positions.append(section_ids.index(section_id))
        require(member_positions == sorted(member_positions), f"series {series_id} members must follow section order")
        occupied = sorted(set(member_positions))
        require(occupied == list(range(occupied[0], occupied[-1] + 1)), f"series {series_id} must span contiguous sections/components")
        cues = item.get("recognizable_cues")
        require(
            isinstance(cues, list)
            and cues
            and all(nonempty_string(cue) for cue in cues)
            and len(cues) == len(set(cues)),
            f"series {series_id} recognizable_cues must be non-empty and unique",
        )

    assessment = document.get("series_assessment")
    assessment_fields = {"status", "rationale", "candidate_inventory"}
    require(isinstance(assessment, dict) and set(assessment) == assessment_fields, "series_assessment fields are invalid")
    status = assessment.get("status")
    require(status in {"present", "none"}, "series_assessment status must be present or none")
    require(nonempty_string(assessment.get("rationale")), "series_assessment rationale is required")
    inventory = assessment.get("candidate_inventory")
    require(isinstance(inventory, list) and inventory, "series_assessment candidate_inventory must be non-empty")
    inventory_fields = {"section_id", "component_id", "label", "series_candidate"}
    inventory_keys: set[tuple[str, str | None]] = set()
    represented_sections: set[str] = set()
    candidate_keys: set[tuple[str, str | None]] = set()
    for index, item in enumerate(inventory, start=1):
        require(isinstance(item, dict) and set(item) == inventory_fields, f"series candidate inventory item {index} fields are invalid")
        section_id = item.get("section_id")
        component_id = item.get("component_id")
        require(section_id in section_ids, f"series candidate inventory item {index} section_id is invalid")
        require(component_id is None or nonempty_string(component_id), f"series candidate inventory item {index} component_id is invalid")
        require(nonempty_string(item.get("label")), f"series candidate inventory item {index} label is required")
        require(isinstance(item.get("series_candidate"), bool), f"series candidate inventory item {index} series_candidate is invalid")
        key = (section_id, component_id)
        require(key not in inventory_keys, f"series candidate inventory item {index} is duplicated")
        inventory_keys.add(key)
        represented_sections.add(section_id)
        if item["series_candidate"]:
            candidate_keys.add(key)
    require(represented_sections == set(section_ids), "series candidate inventory must assess every section")

    if status == "present":
        require(series, "series_assessment present requires repeated_series")
        require(len(candidate_keys) >= 2, "series_assessment present requires at least two candidate members")
        assigned_keys = {
            (member["section_id"], member["component_id"])
            for item in series
            for member in item["members"]
        }
        require(
            candidate_keys == assigned_keys,
            "series candidate inventory true keys must exactly equal repeated_series member keys",
        )
        for item in series:
            for member in item["members"]:
                require(
                    (member["section_id"], member["component_id"]) in candidate_keys,
                    f"series {item['id']} member is missing from audited candidate inventory",
                )
    else:
        require(not series, "series_assessment none requires repeated_series to be empty")
        require(not candidate_keys, "series_assessment none cannot mark series candidates")
        step_labels = {match.group(0).upper().replace(" ", "") for match in STEP_LABEL_PATTERN.finditer(
            json.dumps(sections, ensure_ascii=False) + json.dumps(inventory, ensure_ascii=False)
        )}
        require(
            len(step_labels) < 2,
            "series_assessment none conflicts with obvious numbered STEP labels; declare and review the series",
        )
    return sections, boundaries, series


def validate_continuity_plan(plan: dict, structure_sha256: str, boundaries: list[dict], series: list[dict]) -> None:
    fields = {
        "kind", "schema_version", "structure_sha256", "shared_visual_system", "band_rhythm",
        "boundaries", "repeated_series",
    }
    require(set(plan) == fields, "page continuity plan fields are invalid")
    require(plan.get("kind") == "lp-page-continuity-plan" and plan.get("schema_version") == "1.1", "page continuity plan type is invalid")
    require(plan.get("structure_sha256") == structure_sha256, "page continuity plan structure binding drift")
    visual = plan.get("shared_visual_system")
    visual_fields = {"color_logic", "typography_logic", "imagery_logic", "shape_and_material_logic"}
    require(
        isinstance(visual, dict)
        and set(visual) == visual_fields
        and all(nonempty_string(visual.get(key)) for key in visual_fields),
        "shared_visual_system is incomplete",
    )
    rhythm = plan.get("band_rhythm")
    require(
        isinstance(rhythm, dict)
        and set(rhythm) == {"pattern", "spacing_logic"}
        and all(nonempty_string(rhythm.get(key)) for key in ("pattern", "spacing_logic")),
        "band_rhythm is incomplete",
    )
    planned_boundaries = plan.get("boundaries")
    require(isinstance(planned_boundaries, list) and len(planned_boundaries) == len(boundaries), "page continuity plan boundaries are incomplete")
    plan_boundary_fields = set(boundaries[0]) | {"execution_cue", "decorative_arrow_only"} if boundaries else set()
    for index, (planned, approved) in enumerate(zip(planned_boundaries, boundaries), start=1):
        require(isinstance(planned, dict) and set(planned) == plan_boundary_fields, f"page continuity boundary {index} fields are invalid")
        require({key: planned[key] for key in approved} == approved, f"page continuity boundary {index} drifts from structure")
        require(nonempty_string(planned.get("execution_cue")), f"page continuity boundary {index} execution_cue is required")
        require(planned.get("decorative_arrow_only") is False, f"page continuity boundary {index} cannot rely on decorative arrows alone")

    planned_series = plan.get("repeated_series")
    require(isinstance(planned_series, list) and len(planned_series) == len(series), "page continuity repeated_series is incomplete")
    for index, (planned, approved) in enumerate(zip(planned_series, series), start=1):
        fields = set(approved) | {"cue_invariants"}
        require(isinstance(planned, dict) and set(planned) == fields, f"page continuity series {index} fields are invalid")
        require({key: planned[key] for key in approved} == approved, f"page continuity series {index} drifts from structure")
        invariants = planned.get("cue_invariants")
        require(isinstance(invariants, list) and len(invariants) == len(approved["recognizable_cues"]), f"page continuity series {approved['id']} invariants are incomplete")
        for cue, invariant in zip(approved["recognizable_cues"], invariants):
            require(
                isinstance(invariant, dict)
                and set(invariant) == {"cue", "rule"}
                and invariant.get("cue") == cue
                and nonempty_string(invariant.get("rule")),
                f"page continuity series {approved['id']} cue invariant is invalid",
            )


def validate_whole_page_review(
    review: dict,
    plan_sha256: str,
    plan: dict,
    sections: list[dict],
    section_sha256s: list[str],
    fv_handoff: dict | None = None,
    authentic_proof: dict | None = None,
    cta_strategy: dict | None = None,
) -> None:
    boundaries = plan["boundaries"]
    series = plan["repeated_series"]
    fields = {
        "kind", "schema_version", "page_continuity_plan_sha256", "section_sha256s",
        "boundary_reviews", "text_fit_reviews", "series_reviews", "overall_decision", "validator_scope",
    }
    if fv_handoff is not None:
        fields |= {"fv_render_outcome", "authentic_proof_review", "direct_call_review"}
    require(set(review) == fields, "whole-page review fields are invalid")
    require(review.get("kind") == "lp-whole-page-continuity-review" and review.get("schema_version") == "1.1", "whole-page review type is invalid")
    require(review.get("page_continuity_plan_sha256") == plan_sha256, "whole-page review plan hash drift")
    require(review.get("section_sha256s") == section_sha256s, "whole-page review section hash/order drift")
    require(review.get("overall_decision") == "pass", "whole-page review must pass")
    require(review.get("validator_scope") == "declared-review-completeness-not-pixel-truth", "whole-page review validator_scope is invalid")

    if fv_handoff is not None:
        require(authentic_proof is not None and cta_strategy is not None,
                "whole-page schema 1.1 requires proof and CTA contracts")
        proof_strategy = authentic_proof
        proof_review = review.get("authentic_proof_review")
        require(isinstance(proof_review, dict)
                and set(proof_review) == {"selected_mode", "item_reviews", "decision", "observation"}
                and proof_review.get("selected_mode") == proof_strategy["selected_mode"]
                and proof_review.get("decision") == "pass"
                and nonempty_string(proof_review.get("observation")),
                "whole-page authentic proof review is invalid")
        proof_items = proof_strategy["items"]
        item_reviews = proof_review.get("item_reviews")
        require(isinstance(item_reviews, list) and len(item_reviews) == len(proof_items),
                "whole-page authentic proof review must cover every approved proof item")
        for index, (observed, approved) in enumerate(zip(item_reviews, proof_items), start=1):
            expected = {
                "proof_id": approved["proof_id"], "mode": approved["mode"],
                "claim_id": approved["claim_id"], "content_source_ids": approved["content_source_ids"],
                "asset_source_id": approved["asset_source_id"],
                "permission_status": approved["usage_permission"]["status"],
                "privacy_status": approved["privacy"]["status"],
                "use_sections": approved["use_sections"], "display_copy": approved["display_copy"],
            }
            require(isinstance(observed, dict)
                    and set(observed) == set(expected) | {"decision", "observation"}
                    and all(observed.get(key) == value for key, value in expected.items())
                    and observed.get("decision") == "pass"
                    and nonempty_string(observed.get("observation")),
                    f"whole-page authentic proof item review {index} drifts from the approved source/permission contract")

        direct = cta_strategy["direct_call"]
        call_review = review.get("direct_call_review")
        require(isinstance(call_review, dict)
                and set(call_review) == {
                    "decision", "section_id", "image_sha256", "visible_label", "availability_copy",
                    "primary_action_count", "secondary_call_count", "result", "observation",
                }
                and call_review.get("decision") == direct["decision"]
                and call_review.get("primary_action_count") == 1
                and nonempty_string(call_review.get("observation")),
                "whole-page direct-call review is invalid")
        if direct["decision"] == "enabled":
            section_index = [section["id"] for section in sections].index(direct["section_id"])
            require(call_review.get("section_id") == direct["section_id"]
                    and call_review.get("image_sha256") == section_sha256s[section_index]
                    and call_review.get("visible_label") == direct["label"]
                    and call_review.get("availability_copy") == direct["availability_copy"]
                    and call_review.get("secondary_call_count") == 1
                    and call_review.get("result") == "pass",
                    "whole-page direct-call review must bind the baked exact label, availability, and section image")
        else:
            require(call_review.get("section_id") is None
                    and call_review.get("image_sha256") is None
                    and call_review.get("visible_label") is None
                    and call_review.get("availability_copy") is None
                    and call_review.get("secondary_call_count") == 0
                    and call_review.get("result") == "not-applicable",
                    "disabled direct-call review must remain not-applicable")

        outcome = review.get("fv_render_outcome")
        outcome_fields = {
            "section_id", "image_sha256", "viewport_width", "headline_lines", "support_lines", "cta_lines",
            "primary_action_count", "nonuniform_glyph_scaling", "condensed_to_fit", "clipping", "overflow",
            "message_match", "scan_outcomes", "observation",
        }
        require(isinstance(outcome, dict) and set(outcome) == outcome_fields,
                "whole-page FV render outcome fields are invalid")
        require(outcome.get("section_id") == sections[0].get("id")
                and outcome.get("image_sha256") == section_sha256s[0]
                and strict_int(outcome.get("viewport_width"))
                and outcome.get("viewport_width") == 390,
                "whole-page FV render outcome image/viewport binding drift")
        require(isinstance(outcome.get("headline_lines"), int) and not isinstance(outcome["headline_lines"], bool)
                and 1 <= outcome["headline_lines"] <= 3
                and isinstance(outcome.get("support_lines"), int) and not isinstance(outcome["support_lines"], bool)
                and 0 <= outcome["support_lines"] <= 4
                and isinstance(outcome.get("cta_lines"), int) and not isinstance(outcome["cta_lines"], bool)
                and outcome["cta_lines"] == 1,
                "whole-page FV render line counts must satisfy H1 <=3, support <=4, CTA=1")
        require(isinstance(outcome.get("primary_action_count"), int)
                and not isinstance(outcome["primary_action_count"], bool)
                and outcome["primary_action_count"] == 1,
                "whole-page FV render must contain exactly one primary CTA")
        require(all(outcome.get(key) is False for key in ("nonuniform_glyph_scaling", "condensed_to_fit", "clipping", "overflow"))
                and nonempty_string(outcome.get("observation")),
                "whole-page FV render must not squeeze, condense, clip, or overflow")
        message_match = outcome.get("message_match")
        require(isinstance(message_match, dict)
                and set(message_match) == {"source_message", "offer", "next_action", "observation"}
                and all(message_match.get(key) == "pass" for key in ("source_message", "offer", "next_action"))
                and nonempty_string(message_match.get("observation")),
                "whole-page FV source-message/offer/action match must pass")
        scan_contract = fv_handoff["scan_contract"]
        scan_outcomes = outcome.get("scan_outcomes")
        require(isinstance(scan_outcomes, dict) and set(scan_outcomes) == set(scan_contract),
                "whole-page FV scan outcomes are incomplete")
        for key, contract in scan_contract.items():
            observed = scan_outcomes.get(key)
            require(isinstance(observed, dict)
                    and set(observed) == {"decision", "answer", "evidence_used", "observation"}
                    and observed.get("decision") == "pass"
                    and observed.get("answer") == contract["answer"]
                    and isinstance(observed.get("evidence_used"), list) and observed["evidence_used"]
                    and all(mode in contract["evidence_modes"] for mode in observed["evidence_used"])
                    and nonempty_string(observed.get("observation")),
                    f"whole-page FV scan outcome {key} must pass with approved evidence")

    reviews = review.get("boundary_reviews")
    require(isinstance(reviews, list) and len(reviews) == len(boundaries), "whole-page review must cover every N-1 boundary")
    review_fields = {
        "order", "from_section_id", "to_section_id", "mechanism", "transition_copy",
        "bridge_plan", "semantic_seam", "visual_seam", "execution_cue", "notes",
    }
    for index, (item, boundary) in enumerate(zip(reviews, boundaries), start=1):
        require(isinstance(item, dict) and set(item) == review_fields, f"boundary review {index} fields are invalid")
        require(strict_int(item.get("order")), f"boundary review {index} order must be an integer")
        for key in ("order", "from_section_id", "to_section_id", "mechanism", "transition_copy"):
            require(item.get(key) == boundary.get(key), f"boundary review {index} drifts from continuity contract")
        require(item.get("bridge_plan") == boundary.get("bridge_plan"),
                f"boundary review {index} exact bridge_plan drift")
        require(item.get("semantic_seam") == "pass" and item.get("visual_seam") == "pass", f"boundary review {index} seam must pass")
        require(item.get("execution_cue") == boundary.get("execution_cue"), f"boundary review {index} execution_cue drift")
        require(nonempty_string(item.get("notes")), f"boundary review {index} evidence is incomplete")

    text_reviews = review.get("text_fit_reviews")
    require(isinstance(text_reviews, list) and len(text_reviews) == len(sections), "whole-page review must cover text fit for every section")
    text_fields = {
        "section_id", "order", "authority_copy_composition", "nonuniform_glyph_scaling",
        "condensed_to_fit", "clipping", "overflow", "body_font_px", "supporting_text_present",
        "supporting_font_px", "line_height_ratio", "decision", "notes",
    }
    for index, (item, section) in enumerate(zip(text_reviews, sections), start=1):
        require(isinstance(item, dict) and set(item) == text_fields, f"text-fit review {index} fields are invalid")
        require(item.get("section_id") == section.get("id")
                and strict_int(item.get("order")) and item.get("order") == index,
                f"text-fit review {index} section binding is invalid")
        require(item.get("authority_copy_composition") in {"deterministic-raster", "verified-user-provided", "visually-verified-finished-image"}, f"text-fit review {index} authority copy composition is invalid")
        for key in ("nonuniform_glyph_scaling", "condensed_to_fit", "clipping", "overflow"):
            require(item.get(key) is False, f"text-fit review {index} rejects {key}")
        body = item.get("body_font_px")
        require(isinstance(body, (int, float)) and not isinstance(body, bool) and body >= 16, f"text-fit review {index} body font is below 16px")
        supporting_present = item.get("supporting_text_present")
        require(isinstance(supporting_present, bool), f"text-fit review {index} supporting_text_present is invalid")
        supporting = item.get("supporting_font_px")
        if supporting_present:
            require(isinstance(supporting, (int, float)) and not isinstance(supporting, bool) and supporting >= 14, f"text-fit review {index} supporting font is below 14px")
        else:
            require(supporting is None, f"text-fit review {index} supporting_font_px must be null when absent")
        line_height = item.get("line_height_ratio")
        require(isinstance(line_height, (int, float)) and not isinstance(line_height, bool) and line_height >= 1.4, f"text-fit review {index} line-height is below 1.4")
        require(item.get("decision") == "pass" and nonempty_string(item.get("notes")), f"text-fit review {index} must pass with notes")

    series_reviews = review.get("series_reviews")
    require(isinstance(series_reviews, list) and len(series_reviews) == len(series), "whole-page review must cover every repeated series")
    for index, (item, approved) in enumerate(zip(series_reviews, series), start=1):
        fields = {"series_id", "recognizable_cues", "cue_invariants", "member_reviews", "identity_continuity", "notes"}
        require(isinstance(item, dict) and set(item) == fields, f"series review {index} fields are invalid")
        require(item.get("series_id") == approved["id"] and item.get("recognizable_cues") == approved["recognizable_cues"], f"series review {index} identity/cues drift")
        require(item.get("cue_invariants") == approved["cue_invariants"], f"series review {index} cue invariant drift")
        members = item.get("member_reviews")
        require(isinstance(members, list) and len(members) == len(approved["members"]), f"series review {index} members are incomplete")
        for member_index, (member, expected_member) in enumerate(zip(members, approved["members"]), start=1):
            require(
                isinstance(member, dict)
                and set(member) == {"section_id", "component_id", "cues_present", "cue_invariants_present", "identity"}
                and member.get("section_id") == expected_member["section_id"]
                and member.get("component_id") == expected_member["component_id"],
                f"series review {index} member {member_index} binding is invalid",
            )
            require(member.get("cues_present") == approved["recognizable_cues"], f"series review {index} member {member_index} recognizable cue drift")
            require(member.get("cue_invariants_present") == approved["cue_invariants"], f"series review {index} member {member_index} cue invariant drift")
            require(member.get("identity") == "pass", f"series review {index} member {member_index} identity drift")
        require(item.get("identity_continuity") == "pass" and nonempty_string(item.get("notes")), f"series review {index} identity continuity must pass")


DELEGATED_LP_SCOPES = {
    "lp-structure": "structure",
    "lp-fv-candidate-selection": "design", "lp-fv-direction": "design",
    "lp-page-continuity": "design", "lp-direct-image-assembly": "implementation",
    "lp-runtime-assembly": "implementation",
}


def validate_agent_delegation(receipt: dict, scope: str, subject_sha256: str, label: str) -> None:
    """Validate scoped AI expression, never substitute human source/fact approval."""
    require(scope in DELEGATED_LP_SCOPES, f"{label} cannot delegate this approval scope")
    fields = {"kind", "schema_version", "scope", "decision", "subject_sha256", "agent_id", "reason", "decided_at", "run_id", "scope_revision", "scope_hash", "step_id", "run_snapshot"}
    require(set(receipt) == fields and receipt.get("schema_version") == "1.0", f"{label} delegation fields invalid")
    require(receipt.get("kind") == "agent-delegation-record" and receipt.get("decision") == "selected" and receipt.get("scope") == scope, f"{label} delegation type/scope invalid")
    require(receipt.get("subject_sha256") == subject_sha256, f"{label} delegation subject changed")
    require(nonempty_string(receipt.get("agent_id")) and nonempty_string(receipt.get("reason")), f"{label} delegation actor/reason required")
    try:
        decided = datetime.fromisoformat(receipt.get("decided_at", "").replace("Z", "+00:00"))
        run = receipt["run_snapshot"]["run"]
        expires = datetime.fromisoformat(run["leaseExpiresAt"].replace("Z", "+00:00"))
        approved = datetime.fromisoformat(run["approval"]["reportedAt"].replace("Z", "+00:00"))
        require(decided.tzinfo is not None and approved <= decided <= expires and decided.timestamp() <= datetime.now(timezone.utc).timestamp() + 60, f"{label} decision must fall within its recorded approved lease")
    except (ValueError, KeyError, TypeError):
        require(False, f"{label} delegation snapshot/time invalid")
    require(run.get("status") == "running", f"{label} running mandate required")
    require("leaseToken" not in run, f"{label} secret execution token cannot enter shared receipts")
    for field, key in (("run_id", "id"), ("scope_revision", "scopeRevision"), ("scope_hash", "scopeHash")):
        require(receipt.get(field) == run.get(key), f"{label} delegation {field} stale")
    mandate = run.get("scope")
    require(isinstance(mandate, dict) and canonical_digest(mandate) == run.get("scopeHash"), f"{label} mandate digest invalid")
    approval = run.get("approval", {})
    require(approval.get("kind") == "executor_reported_conversation" and approval.get("scopeRevision") == run["scopeRevision"] and approval.get("scopeHash") == run["scopeHash"] and nonempty_string(approval.get("statement")), f"{label} scoped conversation approval required")
    require(DELEGATED_LP_SCOPES[scope] in mandate.get("delegation", []), f"{label} area not delegated")
    expected_skill = "lp-structure" if scope == "lp-structure" else "lp-image-builder"
    require(any(step.get("id") == receipt.get("step_id") and step.get("skill") == expected_skill for step in mandate.get("steps", [])), f"{label} step is outside LP mandate")
    human_subjects = ("product", "price", "terms", "truth", "material_rights") if scope == "lp-structure" else ("truth", "material_rights")
    for subject in human_subjects:
        require(any(item.get("subject") == subject and nonempty_string(item.get("statement")) for item in mandate.get("humanDecisions", [])), f"{label} human {subject} decision required")


def validate_receipt(path: Path, scope: str, subject_sha256: str, label: str) -> None:
    """Accept external receipt bytes or a truthful model-recorded conversation decision."""

    receipt = load_json(path, label)
    timestamp_pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
    if receipt.get("kind") == "agent-delegation-record":
        validate_agent_delegation(receipt, scope, subject_sha256, label)
    elif receipt.get("kind") == "external-approval-receipt":
        require(set(receipt) == {"kind", "schema_version", "scope", "decision", "provided_by", "authored_by_model", "approved_at", "subject_sha256"}, f"{label} fields are invalid")
        require(receipt.get("schema_version") == "1.0", f"{label} type is invalid")
        require(receipt.get("scope") == scope and receipt.get("decision") == "approved", f"{label} scope/decision is invalid")
        require(receipt.get("provided_by") in {"user", "controller"}, f"{label} must come from user or controller")
        require(receipt.get("authored_by_model") is False, f"{label} must not be model-authored")
        approved_at = receipt.get("approved_at")
        require(isinstance(approved_at, str) and re.fullmatch(timestamp_pattern, approved_at), f"{label} approved_at must be RFC3339")
    elif receipt.get("kind") == "conversation-approval-record":
        expected_fields = {
            "kind",
            "schema_version",
            "scope",
            "decision",
            "decision_provided_by",
            "recorded_by",
            "recorded_at",
            "subject_sha256",
            "decision_evidence",
        }
        require(set(receipt) == expected_fields and receipt.get("schema_version") == "1.0", f"{label} fields/type are invalid")
        require(receipt.get("scope") == scope and receipt.get("decision") == "approved", f"{label} scope/decision is invalid")
        require(receipt.get("decision_provided_by") in {"user", "controller"}, f"{label} decision must come from user or controller")
        require(receipt.get("recorded_by") == "model", f"{label} conversation record must truthfully identify the model recorder")
        recorded_at = receipt.get("recorded_at")
        require(isinstance(recorded_at, str) and re.fullmatch(timestamp_pattern, recorded_at), f"{label} recorded_at must be RFC3339")
        evidence = receipt.get("decision_evidence")
        require(isinstance(evidence, dict), f"{label} decision_evidence must be an object")
        if evidence.get("kind") == "verbatim":
            require(set(evidence) == {"kind", "value"}, f"{label} verbatim decision_evidence fields are invalid")
            require(isinstance(evidence.get("value"), str) and evidence["value"].strip(), f"{label} verbatim decision evidence is required")
        elif evidence.get("kind") == "message-sha256":
            require(set(evidence) == {"kind", "sha256", "source"}, f"{label} message digest evidence fields are invalid")
            require(isinstance(evidence.get("sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", evidence["sha256"]), f"{label} message evidence sha256 is invalid")
            require(evidence.get("source") == "immediately-preceding-user-or-controller-message", f"{label} message evidence source is invalid")
        else:
            require(False, f"{label} decision_evidence kind is invalid")
    else:
        require(False, f"{label} type is invalid")
    require(receipt.get("subject_sha256") == subject_sha256, f"{label} subject digest mismatch")


def validate(manifest_path: Path, project_root: Path) -> None:
    project_root = project_root.resolve()
    require(project_root.is_dir(), "project root must be a directory")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read manifest: {exc}") from exc

    require(
        set(manifest) == {"schema_version", "kind", "status", "structure", "continuity", "sections", "assembly_approval", "assembly"},
        "manifest fields are invalid",
    )
    require(manifest.get("schema_version") == MANIFEST_SCHEMA_VERSION, f"schema_version must be {MANIFEST_SCHEMA_VERSION}")
    require(manifest.get("kind") == "lp-direct-image-assembly", "kind must be lp-direct-image-assembly")
    require(manifest.get("status") == "approved-for-assembly", "manifest must be approved-for-assembly")

    structure = manifest.get("structure")
    require(isinstance(structure, dict), "structure must be an object")
    require(set(structure) == {"path", "sha256", "approval_view", "approval_receipt"}, "structure fields are invalid")
    structure_path = resolve_project_file(project_root, structure.get("path"), "structure.path")
    require(structure.get("sha256") == sha256(structure_path), "structure sha256 mismatch")
    structure_document = load_json(structure_path, "structure document")
    structure_sections, structure_boundaries, structure_series = validate_structure_document(structure_document, project_root)
    validate_structure_production(structure_document, project_root, for_clicks=True)
    approval_view_binding = structure.get("approval_view")
    require(
        isinstance(approval_view_binding, dict) and set(approval_view_binding) == {"path", "sha256"},
        "structure approval_view binding is invalid",
    )
    approval_view_path = resolve_project_file(project_root, approval_view_binding.get("path"), "structure.approval_view.path")
    require(approval_view_binding.get("sha256") == sha256(approval_view_path), "structure approval view sha256 mismatch")
    validate_structure_approval_view(approval_view_path, structure_document, structure["path"], structure["sha256"])
    structure_receipt_binding = structure.get("approval_receipt")
    require(isinstance(structure_receipt_binding, dict) and set(structure_receipt_binding) == {"path", "sha256"}, "structure approval_receipt binding is invalid")
    structure_receipt_path = resolve_project_file(project_root, structure_receipt_binding.get("path"), "structure.approval_receipt.path")
    require(structure_receipt_binding.get("sha256") == sha256(structure_receipt_path), "structure approval receipt sha256 mismatch")
    structure_subject = structure_approval_subject(structure_document, structure["path"], structure["sha256"])
    validate_receipt(structure_receipt_path, "lp-structure", canonical_digest(structure_subject), "structure approval receipt")

    sections = manifest.get("sections")
    require(isinstance(sections, list) and sections, "sections must be a non-empty array")
    require(len(sections) == len(structure_sections), "manifest section count must match approved structure")
    ids: set[str] = set()
    paths: set[str] = set()
    direct_call_overlays = 0
    direct_call = structure_document["cta_strategy"]["direct_call"]
    primary_strategy = structure_document["cta_strategy"]["primary"]
    primary_overlay_counts = {section_id: 0 for section_id in primary_strategy["section_ids"]}
    for index, section in enumerate(sections, start=1):
        require(isinstance(section, dict), f"section {index} must be an object")
        section_id = section.get("id")
        require(isinstance(section_id, str) and section_id and section_id not in ids, f"section {index} id must be unique")
        ids.add(section_id)
        require(strict_int(section.get("order")) and section.get("order") == index,
                f"section {section_id} order must be {index}")
        structure_section = structure_sections[index - 1]
        require(isinstance(structure_section, dict), f"approved structure section {index} must be an object")
        require(structure_section.get("id") == section_id
                and strict_int(structure_section.get("order")) and structure_section.get("order") == index,
                f"section {section_id} id/order drift from approved structure")
        copy = structure_section.get("copy")
        require(isinstance(copy, dict) and isinstance(copy.get("headline"), str) and isinstance(copy.get("body"), str), f"approved structure section {section_id} copy is invalid")
        require(section.get("loading") == ("eager" if index == 1 else "lazy"), f"section {section_id} loading is invalid")
        require(isinstance(section.get("alt"), str) and section["alt"].strip(), f"section {section_id} alt is required")
        require(
            isinstance(section.get("accessible_summary"), str) and section["accessible_summary"].strip(),
            f"section {section_id} accessible_summary is required",
        )

        image = section.get("image")
        require(isinstance(image, dict), f"section {section_id} image must be an object")
        image_value = image.get("path")
        require(isinstance(image_value, str) and image_value not in paths, f"section {section_id} image path must be unique")
        paths.add(image_value)
        image_path = resolve_project_file(project_root, image_value, f"section {section_id} image.path")
        width, height = validate_png(image_path)
        require(width == 390 and strict_int(image.get("width")) and image.get("width") == 390,
                f"section {section_id} width must be exactly 390")
        require(strict_int(image.get("height")) and image.get("height") == height,
                f"section {section_id} height mismatch")
        if index == 1:
            require(
                MIN_FINISHED_FV_HEIGHT <= height <= MAX_FINISHED_FV_HEIGHT,
                f"section {section_id} FV height must be between {MIN_FINISHED_FV_HEIGHT}px and {MAX_FINISHED_FV_HEIGHT}px",
            )
        require(image.get("sha256") == sha256(image_path), f"section {section_id} sha256 mismatch")

        overlays = section.get("overlays")
        require(isinstance(overlays, list), f"section {section_id} overlays must be an array")
        cta_regions: list[tuple[str, dict]] = []
        for overlay_index, overlay in enumerate(overlays, start=1):
            label = f"section {section_id} overlay {overlay_index}"
            require(isinstance(overlay, dict), f"{label} must be an object")
            require(overlay.get("kind") in ALLOWED_OVERLAYS, f"{label} kind is not allowed")
            if structure_document.get("schema_version") in MODERN_STRUCTURE_SCHEMA_VERSIONS:
                if overlay.get("kind") == "cta":
                    require(set(overlay) == {
                        "kind", "reserved_region", "image_region_policy", "accessible_label",
                        "action_role", "href", "tracking_marker", "availability_copy",
                    }, f"{label} CTA fields are invalid")
                    require(
                        overlay.get("image_region_policy") == "transparent_hit_area_over_baked_control",
                        f"{label} must be a transparent hit area over the baked visible CTA control",
                    )
                    if overlay.get("action_role") == "primary":
                        require(section_id in structure_document["cta_strategy"]["primary"]["section_ids"],
                                f"{label} primary CTA is not approved for this section")
                        require(overlay.get("accessible_label") == structure_document["cta_strategy"]["primary"]["label"],
                                f"{label} primary accessible label must equal the approved primary CTA label")
                        require(overlay.get("href") == primary_strategy["href"],
                                f"{label} primary href must equal the approved safe destination")
                        require(overlay.get("tracking_marker") is None
                                and overlay.get("availability_copy") is None,
                                f"{label} primary CTA cannot carry direct-call metadata")
                        primary_overlay_counts[section_id] += 1
                    elif overlay.get("action_role") == "secondary-direct-call":
                        require(direct_call["decision"] == "enabled"
                                and section_id == direct_call["section_id"],
                                f"{label} direct-call CTA is not enabled for this section")
                        require(overlay.get("accessible_label") == direct_call["label"]
                                and overlay.get("href") == f"tel:{direct_call['phone_e164']}"
                                and overlay.get("tracking_marker") == direct_call["tracking_marker"]
                                and overlay.get("availability_copy") == direct_call["availability_copy"],
                                f"{label} direct-call CTA drifts from the approved phone/label/availability/tracking contract")
                        direct_call_overlays += 1
                    else:
                        require(False, f"{label} action_role is invalid")
                else:
                    require(set(overlay) == {
                        "kind", "reserved_region", "image_region_policy", "accessible_label"
                    }, f"{label} fields are invalid")
                    require(overlay.get("image_region_policy") == "interactive_only", f"{label} must remain interactive-only")
            else:
                require(overlay.get("image_region_policy") == "blank_or_neutral", f"{label} must reserve a blank_or_neutral region")
            require(isinstance(overlay.get("accessible_label"), str) and overlay["accessible_label"].strip(), f"{label} label is required")
            region = overlay.get("reserved_region")
            require(isinstance(region, dict) and set(region) == {"x", "y", "width", "height"}, f"{label} region is invalid")
            values = [region[key] for key in ("x", "y", "width", "height")]
            require(all(isinstance(value, int) and not isinstance(value, bool) for value in values), f"{label} region must use integers")
            x, y, region_width, region_height = values
            require(x >= 0 and y >= 0 and region_width > 0 and region_height > 0, f"{label} region must be positive")
            require(x + region_width <= 390 and y + region_height <= height, f"{label} region exceeds image bounds")
            if overlay.get("action_role") == "secondary-direct-call":
                require(region_width * 320 / 390 >= 44 and region_height * 320 / 390 >= 44,
                        f"{label} must remain at least 44x44 CSS pixels at the 320px viewport")
            if overlay.get("kind") == "cta":
                cta_regions.append((overlay["action_role"], region))
        for left_index, (left_role, left_region) in enumerate(cta_regions):
            for right_role, right_region in cta_regions[left_index + 1:]:
                require(not regions_overlap(left_region, right_region),
                        f"section {section_id} CTA overlays materially overlap: {left_role}/{right_role}")

    require(direct_call_overlays == (1 if direct_call["decision"] == "enabled" else 0),
            "manifest must contain exactly one direct-call overlay when enabled and none otherwise")
    require(all(count == 1 for count in primary_overlay_counts.values()),
            "manifest requires exactly one interactive primary CTA overlay in every approved primary section")

    continuity = manifest.get("continuity")
    require(
        isinstance(continuity, dict)
        and set(continuity) == {
            "page_continuity_plan", "page_continuity_approval", "whole_page_review", "whole_page_composite"
        },
        "continuity bindings are invalid",
    )

    def bound_file(field: str) -> tuple[dict, Path]:
        binding = continuity.get(field)
        require(isinstance(binding, dict) and set(binding) == {"path", "sha256"}, f"continuity.{field} binding is invalid")
        path = resolve_project_file(project_root, binding.get("path"), f"continuity.{field}.path")
        require(binding.get("sha256") == sha256(path), f"continuity.{field} sha256 mismatch")
        return binding, path

    plan_binding, plan_path = bound_file("page_continuity_plan")
    plan = load_json(plan_path, "page continuity plan")
    validate_continuity_plan(plan, structure["sha256"], structure_boundaries, structure_series)
    _, continuity_receipt_path = bound_file("page_continuity_approval")
    continuity_subject = {"scope": "page-continuity", "structure": structure, "plan": plan_binding}
    validate_receipt(
        continuity_receipt_path,
        "lp-page-continuity",
        canonical_digest(continuity_subject),
        "page continuity approval receipt",
    )
    review_binding, review_path = bound_file("whole_page_review")
    review = load_json(review_path, "whole-page review")
    validate_whole_page_review(
        review,
        plan_binding["sha256"],
        plan,
        structure_sections,
        [section["image"]["sha256"] for section in sections],
        structure_document["fv_handoff"],
        structure_document["authentic_proof"],
        structure_document["cta_strategy"],
    )
    _, composite_path = bound_file("whole_page_composite")
    composite_width, composite_height = validate_png(composite_path)
    require(composite_width == 390, "whole_page_composite width must be 390")
    require(composite_height == sum(section["image"]["height"] for section in sections), "whole_page_composite height must equal section heights")

    assembly = manifest.get("assembly")
    require(isinstance(assembly, dict), "assembly must be an object")
    require(assembly.get("mode") == "direct-section-images", "assembly mode is invalid")
    require(assembly.get("stack") == "block-no-gap", "assembly stack is invalid")
    require(assembly.get("exact_source_bytes") is True, "exact_source_bytes must be true")
    require(assembly.get("static_copy_runtime") == "image_only", "static_copy_runtime must be image_only")
    viewports = assembly.get("responsive_viewports")
    require(isinstance(viewports, list)
            and all(strict_int(value) for value in viewports)
            and viewports == [320, 390, 430],
            "responsive_viewports must be [320,390,430]")

    approval = manifest.get("assembly_approval")
    require(isinstance(approval, dict) and set(approval) == {"receipt"}, "assembly_approval must contain one receipt binding")
    approval_binding = approval.get("receipt")
    require(isinstance(approval_binding, dict) and set(approval_binding) == {"path", "sha256"}, "assembly approval receipt binding is invalid")
    approval_path = resolve_project_file(project_root, approval_binding.get("path"), "assembly_approval.receipt.path")
    require(approval_binding.get("sha256") == sha256(approval_path), "assembly approval receipt sha256 mismatch")
    assembly_subject = {"structure": structure, "continuity": continuity, "sections": sections, "assembly": assembly}
    validate_receipt(approval_path, "lp-direct-image-assembly", canonical_digest(assembly_subject), "assembly approval receipt")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--legacy-read-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.legacy_read_only:
            document = load_json(args.manifest.resolve(), "legacy structure archive")
            validate_structure_document(document)
            require(
                document.get("schema_version") in READ_ONLY_STRUCTURE_SCHEMA_VERSIONS,
                "--legacy-read-only accepts structure schema 1.1/1.2 archives only",
            )
        else:
            validate(args.manifest.resolve(), args.project_root)
    except ContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.legacy_read_only:
        print("OK: legacy structure archive is readable; progression and assembly are not authorized")
    else:
        print("OK: approved direct-image LP manifest is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
