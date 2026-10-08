#!/usr/bin/env python3
"""Dependency-free, human-first Markdown presentation for Empire CLI results.

The runtime dictionaries remain the source of truth.  This module only projects
those dictionaries into a stable view for Codex's native Markdown renderer.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

VIEWS = ("json", "compact", "detailed")

_SUCCESS = {
    "approved",
    "approved_for_codex",
    "available",
    "clear",
    "completed",
    "configured",
    "continuation_plan_ready",
    "downloaded",
    "ready",
    "ready_for_codex_adversarial_review",
    "recorded",
    "reconciled",
    "rejected",
    "released",
    "released_after_reconciliation",
    "repaired",
    "response_chunk",
    "route_planned",
    "preview",
    "selected",
    "settled",
    "updated",
}
_ATTENTION = {
    "attention_required",
    "compensation_pending",
    "continuation_plan_blocked",
    "exhausted",
    "failed_empty",
    "pending_claim",
    "pending_reconciliation",
}
_WARNING = {
    "completed_degraded",
    "configured_unverified",
    "codex_only",
    "not_configured",
    "partial_recoverable",
    "quarantined",
    "unavailable",
    "unconfigured",
}

_SECTION_ORDER = (
    "review",
    "research_artifact",
    "budget",
    "routing_evidence",
    "context_preflight",
    "continuation",
    "repository_evidence",
    "response_validation",
    "chunk",
)
_COLLECTION_ORDER = (
    "findings",
    "records",
    "reservations",
    "responses",
    "events",
    "models",
    "candidates",
    "fallbacks",
)
_PRESENTATION_ONLY = {
    "contributors",
    "contributor_footnote",
    "model_syntheses",
    "response_footnote",
    "synthesis_footnote",
}


def add_view_argument(parser: argparse.ArgumentParser) -> None:
    """Add the non-breaking renderer selector to a top-level parser."""
    parser.add_argument(
        "--view",
        choices=VIEWS,
        default="json",
        help=(
            "Output contract: unchanged JSON (default), a compact Markdown card, "
            "or a detailed Markdown card"
        ),
    )


def parse_args_with_view(
    parser: argparse.ArgumentParser, argv: Sequence[str] | None = None
) -> argparse.Namespace:
    """Accept ``--view`` before or after nested subcommands.

    Argparse normally requires top-level options to precede the subcommand.
    Moving this one presentation-only option to the front keeps the CLI humane
    without changing command-specific parsing.
    """
    values = list(sys.argv[1:] if argv is None else argv)
    view_tokens: list[str] = []
    for index, token in enumerate(values):
        if token == "--view":
            if index + 1 >= len(values):
                parser.error("argument --view: expected one argument")
            view_tokens = [token, values[index + 1]]
            del values[index : index + 2]
            break
        if token.startswith("--view="):
            view_tokens = [token]
            del values[index]
            break
    return parser.parse_args([*view_tokens, *values])


def command_title(args: argparse.Namespace) -> str:
    """Create a concise title from the parsed command path."""
    parts: list[str] = []
    for attribute in (
        "command",
        "provider_command",
        "mode_command",
        "language_command",
        "budget_command",
        "compensation_command",
        "responses_command",
    ):
        value = getattr(args, attribute, None)
        if isinstance(value, str) and value:
            parts.append(value)
    return " · ".join(_humanize(part) for part in parts) or "Result"


def format_output(
    payload: Mapping[str, Any], *, view: str = "json", title: str = "Result"
) -> str:
    """Render one result while leaving the original mapping unchanged."""
    if view == "json":
        return json.dumps(payload, indent=2) + "\n"
    if view not in VIEWS:
        raise ValueError(f"Unsupported Empire view: {view}")
    return render_markdown(payload, title=title, detailed=view == "detailed")


def render_markdown(
    payload: Mapping[str, Any], *, title: str = "Result", detailed: bool = False
) -> str:
    status = str(payload.get("status") or payload.get("state") or "available")
    symbol, label = _status_treatment(status)
    lines = [f"## Empire · {_escape(title)}", "", f"{symbol} **{label}**"]
    note = _status_note(status)
    if note:
        lines.extend(("", note))

    error = payload.get("error")
    if error is not None:
        lines.extend(("", "### What happened", "", _safe_paragraph(error)))

    facts = _summary_facts(payload)
    if facts:
        lines.extend(("", "### At a glance", "", "| Signal | Value |", "| --- | --- |"))
        lines.extend(f"| {_escape(key)} | {_inline(value)} |" for key, value in facts)

    _append_review(lines, payload.get("review"), detailed=detailed)
    _append_content(lines, payload)
    _append_collections(lines, payload, detailed=detailed)

    if detailed:
        consumed = {
            "status",
            "state",
            "error",
            "content",
            "review",
            *_COLLECTION_ORDER,
            *_PRESENTATION_ONLY,
        }
        for key in _SECTION_ORDER:
            if key in consumed:
                continue
            section = payload.get(key)
            if isinstance(section, Mapping):
                _append_mapping(lines, _humanize(key), section)
                consumed.add(key)
        remainder = {
            key: value
            for key, value in payload.items()
            if key not in consumed
            and key not in _PRESENTATION_ONLY
            and not _is_summary_fact(key, value)
        }
        if remainder:
            _append_mapping(lines, "Additional details", remainder)

    action = payload.get("next_action") or _next_action(status, payload)
    if action:
        lines.extend(("", "### Next action", "", _safe_paragraph(action)))

    lines.extend(
        (
            "",
            "---",
            (
                "`Detailed Markdown view · underlying JSON contract unchanged`"
                if detailed
                else "`Compact Markdown view · use --view detailed for full metadata · "
                "underlying JSON contract unchanged`"
            ),
        )
    )
    return "\n".join(lines).rstrip() + "\n"


def _status_treatment(status: str) -> tuple[str, str]:
    normalized = status.lower()
    if normalized in _SUCCESS:
        return "✓", _humanize(status)
    if normalized in _ATTENTION:
        return "!", f"Action required · {_humanize(status)}"
    if normalized in _WARNING:
        return "△", _humanize(status)
    if any(word in normalized for word in ("error", "failed", "blocked", "corrupt")):
        return "×", _humanize(status)
    if any(word in normalized for word in ("pending", "prepared", "dispatched")):
        return "…", _humanize(status)
    return "○", _humanize(status)


def _status_note(status: str) -> str | None:
    return {
        "completed": "The external contribution is durable and ready for Codex review.",
        "completed_degraded": (
            "Useful bytes were saved, but the structured response contract did not pass."
        ),
        "partial_recoverable": (
            "Usable assistant output was saved before the incomplete provider terminal state."
        ),
        "failed_empty": (
            "No deliverable assistant bytes were recovered; billing and compensation remain visible."
        ),
        "route_planned": "Preview only. No provider dispatch or budget reservation occurred.",
        "continuation_plan_ready": (
            "The continuation boundary is verified; provider dispatch and budget reservation did not occur."
        ),
        "continuation_plan_blocked": (
            "The continuation remains non-billable until every route or identity blocker is resolved."
        ),
        "attention_required": "This state needs human reconciliation or follow-up.",
        "error": "The command stopped without reporting a successful result.",
    }.get(status.lower())


def _summary_facts(payload: Mapping[str, Any]) -> list[tuple[str, Any]]:
    routing = _mapping(payload.get("routing_evidence"))
    budget = _mapping(payload.get("budget"))
    artifact = _mapping(payload.get("research_artifact"))
    chunk = _mapping(payload.get("chunk"))
    manifest = _mapping(payload.get("manifest"))
    handoff_route = _mapping(manifest.get("route"))
    handoff_cost = _mapping(manifest.get("cost"))
    continuation_plan = _mapping(payload.get("continuation_plan"))
    authorization = _mapping(payload.get("authorization"))
    candidates: list[tuple[str, Any]] = [
        ("Role", manifest.get("role") or _external_role(payload)),
        ("Artifact format", manifest.get("format")),
        (
            "Model",
            payload.get("selected_model")
            or handoff_route.get("selected_model")
            or continuation_plan.get("selected_model"),
        ),
        (
            "Served model",
            payload.get("canonical_served_model")
            or handoff_route.get("served_model")
            or continuation_plan.get("served_model"),
        ),
        (
            "Provider",
            routing.get("served_provider")
            or routing.get("provider_name")
            or routing.get("inference_provider")
            or handoff_route.get("served_provider")
            or handoff_route.get("selected_provider")
            or continuation_plan.get("served_provider")
            or _provenance_label(payload, "served_provider")
            or _provenance_label(payload, "routing_provider")
            or payload.get("provider"),
        ),
        ("Cost lane", payload.get("cost_lane") or payload.get("cost_mode")),
        ("Expected cost", _usd(payload.get("expected_cost_usd"))),
        (
            "Observed cost",
            _usd(
                payload.get("observed_cost_usd")
                if payload.get("observed_cost_usd") is not None
                else artifact.get("observed_cost_usd")
                if artifact.get("observed_cost_usd") is not None
                else budget.get(
                    "observed_cost_usd",
                    budget.get("observed_usd", handoff_cost.get("observed_cost_usd")),
                )
            ),
        ),
        (
            "Projected maximum",
            _usd(
                routing.get("projected_maximum_usd")
                if routing.get("projected_maximum_usd") is not None
                else routing.get(
                    "projected_max_cost_usd",
                    payload.get(
                        "reserved_maximum_usd",
                        handoff_cost.get("projected_cost_usd"),
                    ),
                )
            ),
        ),
        (
            "Incremental estimate",
            _usd(authorization.get("incremental_estimated_max_usd")),
        ),
        (
            "Minimum cumulative ceiling",
            _usd(authorization.get("minimum_disclosed_cumulative_ceiling_usd")),
        ),
        (
            "Provider dispatch",
            "not performed"
            if payload.get("provider_dispatch_performed") is False
            else None,
        ),
        (
            "Budget reservation",
            "not created" if payload.get("budget_reserved") is False else None,
        ),
        ("Billing", artifact.get("billing_state") or budget.get("authorization")),
        (
            "Delivery",
            "receipted"
            if artifact.get("delivery_receipted") is True
            else "not receipted"
            if artifact.get("delivery_receipted") is False
            else artifact.get("artifact_state"),
        ),
        ("Durable bytes", artifact.get("durable_response_bytes")),
        ("Project", payload.get("project_name")),
        ("Budget limit", _usd(payload.get("project_limit_usd"))),
        ("Settled spend", _usd(payload.get("settled_spend_usd"))),
        ("Active reservations", _usd(payload.get("active_reservations_usd"))),
        ("Budget remaining", _usd(payload.get("project_budget_remaining_usd"))),
        ("Unresolved cost", _usd(payload.get("unresolved_usd"))),
        ("Pending reconciliation", payload.get("pending_reconciliation_count")),
        ("Pending reservations", payload.get("pending_count")),
        ("Records", payload.get("record_count")),
        ("Responses", payload.get("response_count")),
        ("Handoff ID", payload.get("handoff_id")),
        ("Response ID", payload.get("response_id") or artifact.get("response_id")),
        (
            "Reservation ID",
            payload.get("reservation_id")
            or budget.get("reservation_id")
            or _mapping(payload.get("reservation")).get("reservation_id"),
        ),
        (
            "Generation ID",
            routing.get("provider_generation_id")
            or artifact.get("provider_generation_id"),
        ),
        (
            "Provider request ID",
            routing.get("provider_request_id") or artifact.get("provider_request_id"),
        ),
        ("Chunk", _chunk_summary(chunk)),
    ]
    seen: set[str] = set()
    facts: list[tuple[str, Any]] = []
    for label, value in candidates:
        if value is None or value == "" or label in seen:
            continue
        seen.add(label)
        facts.append((label, value))
    return facts


def _append_review(lines: list[str], review: Any, *, detailed: bool) -> None:
    if not isinstance(review, Mapping):
        return
    summary = review.get("summary")
    findings = review.get("findings")
    if summary:
        lines.extend(("", "### Advisory brief", "", _safe_paragraph(summary)))
    if isinstance(findings, list):
        _append_item_list(lines, "Findings", findings, detailed=detailed)


def _append_content(lines: list[str], payload: Mapping[str, Any]) -> None:
    content = payload.get("content")
    if not isinstance(content, str):
        return
    lines.extend(("", "### Recovered source", "", _fenced(content, "text")))


def _append_collections(
    lines: list[str], payload: Mapping[str, Any], *, detailed: bool
) -> None:
    for key in _COLLECTION_ORDER:
        value = payload.get(key)
        if not isinstance(value, list):
            continue
        _append_item_list(lines, _humanize(key), value, detailed=detailed)


def _append_item_list(
    lines: list[str], title: str, items: list[Any], *, detailed: bool
) -> None:
    if not items:
        return
    lines.extend(("", f"### {_escape(title)} · {len(items)}", ""))
    visible = items if detailed else items[:3]
    for index, item in enumerate(visible, start=1):
        if isinstance(item, Mapping):
            name = (
                item.get("title")
                or item.get("model_id")
                or item.get("response_id")
                or item.get("reservation_id")
                or item.get("event_type")
                or item.get("state")
                or f"Item {index}"
            )
            severity = item.get("severity")
            lead = f"{_humanize(severity)} · {name}" if severity else name
            lines.append(f"- **{_inline(lead)}**")
            keys = (
                "evidence",
                "recommendation",
                "reason",
                "provider",
                "observed_usd",
                "billing_state",
                "safe_to_synthesize",
                "updated_at",
            )
            for key in keys:
                if item.get(key) is not None:
                    lines.append(f"  - {_escape(_humanize(key))}: {_inline(item[key])}")
            if detailed:
                shown = {"title", "severity", *keys}
                for key, value in item.items():
                    if key not in shown and _is_scalar(value):
                        lines.append(f"  - {_escape(_humanize(key))}: {_inline(value)}")
        else:
            lines.append(f"- {_inline(item)}")
    if not detailed and len(items) > len(visible):
        lines.append(f"- … {len(items) - len(visible)} more in detailed view")


def _append_mapping(lines: list[str], title: str, value: Mapping[str, Any]) -> None:
    scalar_rows = [(key, item) for key, item in value.items() if _is_scalar(item)]
    if scalar_rows:
        lines.extend(
            ("", f"### {_escape(title)}", "", "| Field | Value |", "| --- | --- |")
        )
        lines.extend(
            f"| {_escape(_humanize(key))} | {_inline(item)} |"
            for key, item in scalar_rows
        )
    for key, item in value.items():
        if isinstance(item, list):
            _append_item_list(lines, _humanize(key), item, detailed=True)
        elif isinstance(item, Mapping):
            _append_mapping(lines, f"{title} · {_humanize(key)}", item)


def _next_action(status: str, payload: Mapping[str, Any]) -> str | None:
    normalized = status.lower()
    if normalized == "partial_recoverable":
        return (
            "Read and synthesize every saved chunk. Ask for explicit authorization before "
            "any paid continuation."
        )
    if normalized == "completed_degraded":
        return "Review the durable artifact in bounded chunks before using its advice."
    if normalized == "failed_empty":
        return (
            "Inspect the compensation record and provider activity. Do not retry the paid "
            "request automatically."
        )
    if normalized in {"attention_required", "pending_reconciliation"}:
        return "Reconcile the provider outcome against external billing evidence."
    if normalized == "exhausted":
        return "Continue in Codex without external dispatch, or ask the user to change the budget."
    if normalized == "codex_only":
        return "Continue the task locally in Codex; no external model was dispatched."
    if normalized in {"configured_unverified", "unavailable"}:
        return (
            "Retry the redacted status check with the required system-keyring access."
        )
    if normalized in {"not_configured", "unconfigured"}:
        return "Offer setup only if the user wants to configure this capability."
    if normalized == "route_planned":
        return (
            "Review model identity, privacy posture, and maximum cost before dispatch."
        )
    if normalized == "error" and payload.get("error"):
        return "Resolve the reported condition, then rerun only when retry safety is known."
    return None


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _provenance_label(payload: Mapping[str, Any], kind: str) -> str | None:
    footnote = _mapping(payload.get("response_footnote"))
    chips = footnote.get("chips")
    if not isinstance(chips, list):
        return None
    for chip in chips:
        if isinstance(chip, Mapping) and chip.get("kind") == kind:
            label = chip.get("label")
            if isinstance(label, str) and label:
                return label
    return None


def _external_role(payload: Mapping[str, Any]) -> str | None:
    contributors = payload.get("contributors")
    if not isinstance(contributors, list):
        return None
    for contributor in contributors:
        if not isinstance(contributor, Mapping):
            continue
        if contributor.get("model_id") == "codex" or contributor.get("role") == "lead":
            continue
        role = contributor.get("role")
        if isinstance(role, str) and role:
            return role
    return None


def _is_scalar(value: Any) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def _is_summary_fact(key: str, value: Any) -> bool:
    return _is_scalar(value) and key in {
        "selected_model",
        "canonical_served_model",
        "provider",
        "cost_lane",
        "cost_mode",
        "expected_cost_usd",
        "observed_cost_usd",
        "reserved_maximum_usd",
        "project_name",
        "project_limit_usd",
        "settled_spend_usd",
        "active_reservations_usd",
        "project_budget_remaining_usd",
        "unresolved_usd",
        "pending_reconciliation_count",
        "pending_count",
        "record_count",
        "response_count",
        "handoff_id",
        "response_id",
        "reservation_id",
    }


def _chunk_summary(chunk: Mapping[str, Any]) -> str | None:
    if not chunk:
        return None
    offset = chunk.get("offset")
    returned = chunk.get("returned_chars")
    total = chunk.get("total_chars")
    if offset is None or returned is None:
        return None
    suffix = f" of {total}" if total is not None else ""
    return f"{offset}–{int(offset) + int(returned)}{suffix} chars"


def _usd(value: Any) -> str | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        amount = float(value)
    except (TypeError, ValueError):
        return str(value)
    return f"${amount:,.6f}".rstrip("0").rstrip(".")


def _humanize(value: Any) -> str:
    text = str(value).replace("_", " ").replace("-", " ").strip()
    if not text:
        return "Unknown"
    acronyms = {
        "api": "API",
        "id": "ID",
        "llm": "LLM",
        "openai": "OpenAI",
        "sha256": "SHA-256",
        "usd": "USD",
        "zdr": "ZDR",
    }
    words = [acronyms.get(word.lower(), word) for word in text.split()]
    if words[0].lower() not in acronyms:
        words[0] = words[0][:1].upper() + words[0][1:]
    return " ".join(words)


def _safe_paragraph(value: Any) -> str:
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    return "  \n".join(_escape(line) for line in text.split("\n"))


def _inline(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, float):
        value = f"{value:.8f}".rstrip("0").rstrip(".")
    return _escape(str(value).replace("\n", " "))


def _escape(value: Any) -> str:
    text = str(value)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"([\\`*_{}\[\]()#+|])", r"\\\1", text)


def _fenced(content: str, language: str = "") -> str:
    runs: Iterable[str] = re.findall(r"`+", content)
    width = max((len(run) for run in runs), default=2) + 1
    fence = "`" * max(3, width)
    return f"{fence}{language}\n{content}\n{fence}"
