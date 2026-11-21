"""Validate ID-only workflow checkpoints and inventory required readbacks; no I/O mutations."""
import json
import sys
from uuid import UUID

STAGES = ("attachment", "import", "po", "payment", "application", "reconciliation", "remittance", "send")
UUID_FIELDS = {"payee_id", "project_company_id", "bid_id", "document_id", "file_id", "prior_document_id", "payable_id", "commitment_id", "payment_id", "transaction_id"}
UUID_ARRAYS = {"detail_ids", "application_ids"}
OPAQUE_FIELDS = {"thread_id", "draft_id", "message_id", "summary_artifact_id"}
REQUIRED = {
    "attachment": ("document_id", "file_id"),
    "import": ("document_id", "file_id", "detail_ids"),
    "po": ("commitment_id",), "payment": ("payment_id",),
    "application": ("payment_id", "payable_id"),
    "reconciliation": ("payment_id", "transaction_id"),
    "remittance": ("summary_artifact_id", "draft_id", "thread_id"),
    "send": ("message_id", "thread_id"),
}


def uuid(value):
    if not isinstance(value, str):
        raise ValueError("Expected UUID string")
    parsed = UUID(value)
    if str(parsed) != value.lower():
        raise ValueError("Expected canonical UUID")


def opaque(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 500:
        raise ValueError("Expected nonempty bounded ID or blocker code")


def inventory(checkpoint):
    if not isinstance(checkpoint, dict) or set(checkpoint) != {"version", "project_id", "records", "stages"}:
        raise ValueError("Use only version, project_id, records and stages; never store financial data or approval")
    if type(checkpoint["version"]) is not int or checkpoint["version"] != 1:
        raise ValueError("Unsupported checkpoint version")
    uuid(checkpoint["project_id"])
    records, stages = checkpoint["records"], checkpoint["stages"]
    if not isinstance(records, dict) or not isinstance(stages, dict):
        raise ValueError("records and stages must be objects")
    for key, value in records.items():
        if key in UUID_FIELDS:
            uuid(value)
        elif key in UUID_ARRAYS:
            if not isinstance(value, list) or len(value) != len(set(value)):
                raise ValueError("Expected distinct UUID array")
            for item in value:
                uuid(item)
        elif key in OPAQUE_FIELDS:
            opaque(value)
        else:
            raise ValueError("Unsupported record field: " + key)
    for name, stage in stages.items():
        if name not in STAGES or not isinstance(stage, dict) or set(stage) - {"status", "request_id", "receipt_id", "reason", "idempotency_key", "preview_id"}:
            raise ValueError("Unsupported stage or field")
        if stage.get("status") not in {"pending", "applied", "blocked", "uncertain", "not_requested"}:
            raise ValueError("Unsupported stage status")
        for field in ("receipt_id", "reason", "idempotency_key", "preview_id"):
            if field in stage:
                opaque(stage[field])
        if "request_id" in stage:
            uuid(stage["request_id"])
        if stage["status"] == "uncertain" and name not in {"attachment", "remittance", "send"} and "request_id" not in stage:
            raise ValueError("Uncertain financial action requires original request_id")
        if stage["status"] == "applied" and any(not records.get(key) for key in REQUIRED[name]):
            raise ValueError("Applied " + name + " lacks required readback IDs")
    ordered = [name for name in STAGES if name in stages]
    return {
        "project_id": checkpoint["project_id"],
        "readback_records": records,
        "resolve_uncertain_first": [name for name in ordered if stages[name]["status"] == "uncertain"],
        "recheck_applied": [name for name in ordered if stages[name]["status"] == "applied"],
        "remaining": [name for name in ordered if stages[name]["status"] in {"pending", "blocked"}],
        "state_verified": False,
        "send_authorized": False,
    }


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: resume.py checkpoint.json")
        with open(sys.argv[1], encoding="utf-8") as source:
            result = inventory(json.load(source))
        print(json.dumps(result, indent=2))
    except (ValueError, TypeError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
