#!/usr/bin/env python3
"""Prepare workflow MCP requests from live exports. Authentication stays with the host."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from receipts import payload, verify_workflow
from transfer import atomic_write


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    atomic_write(path, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())


def validate_export(raw: dict, workflow_id: int, organization_id: int, created: bool = False) -> dict:
    value = payload(raw)
    if value.get("workflowId") != workflow_id or value.get("orgId") != organization_id:
        raise ValueError("Export does not match the authenticated organization and destination workflow")
    if not isinstance(value.get("modelHash"), str) or not value["modelHash"].strip():
        raise ValueError("Fresh workflow export must include modelHash")
    if created and value.get("paused") is not True:
        raise ValueError("New workflow must be verified as paused before modification")
    return value


def prepare_request(export: dict, *, code: str | None = None, session: str | None = None) -> dict:
    if (code is None) == (session is None):
        raise ValueError("Provide exactly one SDK code file or completed upload session")
    arguments = {"workflow_id": export["workflowId"], "expected_model_hash": export["modelHash"]}
    if code is not None:
        if not code.strip() or not re.search(r"\bsdk\.finish\(\)\s*;?\s*$", code):
            raise ValueError("SDK code must end with sdk.finish()")
        if re.search(r"viber|telegram", code, flags=re.I):
            raise ValueError("Viber and Telegram are unavailable in Reteno")
        arguments["code"] = code
    elif not session or not session.strip():
        raise ValueError("Upload session must be non-empty")
    else:
        arguments["uploadSessionId"] = session
    return {"tool": "update_workflow", "arguments": arguments}


def _workflow_start_config_to_catalog_schema(value: dict[str, Any] | None) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("Workflow start configuration must be an object or null")
    if "type" in value and "params" in value:
        return value

    trigger = str(value.get("trigger") or "").strip()
    if not trigger:
        return None

    configuration_enabled = bool(value.get("configurationEnabled"))
    avoid_run = bool(value.get("avoidRun"))
    config_mapping = {
        "BY_EVENT": ("EVENT_BASED", "eventTypeTrigger"),
        "REGULAR": ("REGULAR", "regularTrigger"),
        "BY_CONTACT_FIELD_CHANGED": ("ON_CONTACT_FIELD_CHANGE", "contactFieldTrigger"),
        "EVENT_BASED_WITH_SEGMENT_PARAMETERS": (
            "EVENT_BASED_WITH_SEGMENT_PARAMETERS",
            "eventTypeWithSegmentParameters",
        ),
    }
    mapping = config_mapping.get(trigger)
    if mapping is None:
        raise ValueError(f"Unsupported workflow start trigger: {trigger}")
    catalog_type, branch_name = mapping
    branch = value.get(branch_name) if branch_name else None
    if not isinstance(branch, dict):
        return None

    if trigger == "BY_EVENT" and not configuration_enabled and not branch.get("eventTypeId"):
        return None

    params = dict(branch)
    if trigger == "REGULAR":
        if "startHour" in params:
            params["fromStartHour"] = params.pop("startHour")
        if "endHour" in params:
            params["toStartHour"] = params.pop("endHour")

    return {
        "type": catalog_type,
        "params": params,
        "avoidRun": avoid_run,
        "configurationEnabled": configuration_enabled,
    }

def _workflow_stop_config_to_catalog_schema(value: dict[str, Any] | None) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("Workflow stop configuration must be an object or null")
    if "enabled" in value:
        return value

    enabled = bool(value.get("isExitFromWorkflow"))
    if not enabled:
        return {"enabled": False}

    exit_type = str(value.get("exitType") or "EventTypeId").strip()
    if exit_type == "GroupId":
        return {
            "enabled": True,
            "type": "GROUP_BASED",
            "params": {"groupId": str(value.get("groupId") or "")},
        }
    if exit_type == "Order":
        return {
            "enabled": True,
            "type": "ORDER_BASED",
            "params": {
                "intervalCount": str(value.get("intervalCount") or ""),
                "intervalUnit": str(value.get("intervalUnit") or "Days"),
            },
        }

    params = {"eventTypeId": str(value.get("eventTypeId") or "")}
    interval_count = value.get("intervalCount")
    if interval_count not in (None, ""):
        params["intervalCount"] = str(interval_count)
        params["intervalUnit"] = str(value.get("intervalUnit") or "Days")
    return {
        "enabled": True,
        "type": "EVENT_BASED",
        "params": params,
    }

def clone_files(source: dict, graph: Any, output_dir: Path) -> None:
    if not isinstance(graph, list) or any(not isinstance(item, dict) for item in graph):
        raise ValueError("Exported workflow graph must be an array of objects")
    if re.search(r"viber|telegram", json.dumps(graph), flags=re.I):
        raise ValueError("Source graph contains a channel unavailable in Reteno")
    for key in ("startConfig", "stopConfig"):
        if key not in source:
            raise ValueError(f"Source export is missing {key}; do not drop an unknown configuration")
    configs = {
        "startConfig": _workflow_start_config_to_catalog_schema(source["startConfig"]),
        "stopConfig": _workflow_stop_config_to_catalog_schema(source["stopConfig"]),
    }
    write_json(output_dir / "workflow.json", graph)
    write_json(output_dir / "configs.json", configs)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--export", type=Path, required=True)
    prepare.add_argument("--workflow-id", type=int, required=True)
    prepare.add_argument("--organization-id", type=int, required=True)
    prepare.add_argument("--created", action="store_true")
    group = prepare.add_mutually_exclusive_group(required=True)
    group.add_argument("--code", type=Path)
    group.add_argument("--upload-session-id")
    prepare.add_argument("--output", type=Path, required=True)
    clone = commands.add_parser("clone-files")
    clone.add_argument("--export", type=Path, required=True)
    clone.add_argument("--workflow-id", type=int, required=True)
    clone.add_argument("--organization-id", type=int, required=True)
    clone.add_argument("--graph", type=Path, required=True)
    clone.add_argument("--output-dir", type=Path, required=True)
    verify = commands.add_parser("verify")
    verify.add_argument("--response", type=Path, required=True)
    verify.add_argument("--workflow-id", type=int, required=True)
    verify.add_argument("--created", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "verify":
            verify_workflow(read_json(args.response), args.workflow_id, args.created)
            print(json.dumps({"verified": True, "workflowId": args.workflow_id}))
            return
        exported = validate_export(read_json(args.export), args.workflow_id, args.organization_id,
                                   getattr(args, "created", False))
        if args.command == "prepare":
            request = prepare_request(exported, code=args.code.read_text() if args.code else None,
                                      session=args.upload_session_id)
            write_json(args.output, request)
        else:
            clone_files(exported, read_json(args.graph), args.output_dir)
        print(json.dumps({"prepared": True, "persisted": False, "workflowId": args.workflow_id}))
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Workflow preparation failed: {exc}\n")


if __name__ == "__main__":
    main()
