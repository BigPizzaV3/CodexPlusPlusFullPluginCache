"""One fail-closed contract for the CLI and MCP execution paths."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from blueprint_schema import load_blueprint

IDENTIFIER = r"[A-Za-z][A-Za-z0-9_]*"
ENTITY = rf"EntityDefinitions\(LogicalName='{IDENTIFIER}'\)"
ATTRIBUTE = rf"{ENTITY}/Attributes\(LogicalName='{IDENTIFIER}'\)"
RELATIONSHIP = rf"RelationshipDefinitions\(SchemaName='{IDENTIFIER}'\)"
PATHS = {
    "POST": [r"EntityDefinitions", rf"{ENTITY}/Attributes", r"RelationshipDefinitions"],
    "PATCH": [ENTITY, ATTRIBUTE, RELATIONSHIP],
}


def normalized_url(value):
    if not isinstance(value, str):
        raise ValueError("targetUrl must be an HTTPS origin")
    parsed = urlsplit(value)
    if (parsed.scheme != "https" or not parsed.hostname or not re.fullmatch(r"[A-Za-z0-9.-]+", parsed.hostname) or parsed.username or parsed.password
            or parsed.query or parsed.fragment or parsed.path not in ("", "/") or parsed.port not in (None, 443)):
        raise ValueError("targetUrl must be an HTTPS origin without credentials, path, query or custom port")
    return f"https://{parsed.hostname.lower()}"


def valid_solution(value):
    return (isinstance(value, str) and re.fullmatch(IDENTIFIER, value) is not None
            and value.lower() not in {"default", "activesolution", "active", "system"})


def operation_issues(operations):
    if not isinstance(operations, list) or not operations:
        return ["operations must be a non-empty list"]
    issues = []
    for index, op in enumerate(operations):
        prefix = f"operations[{index}]"
        if not isinstance(op, dict):
            issues.append(f"{prefix} must be an object")
            continue
        method, path = op.get("method"), op.get("path")
        if (op.get("type") != "webApiMetadata" or not isinstance(method, str)
                or not isinstance(path, str) or not any(re.fullmatch(p, path) for p in PATHS.get(method, []))):
            issues.append(f"{prefix}: unsupported metadata method/path")
        if not isinstance(op.get("payload"), dict) or not op["payload"]:
            issues.append(f"{prefix}: non-empty payload object required")
        elif method == "POST" and not re.fullmatch(IDENTIFIER, str(op["payload"].get("SchemaName", ""))):
            issues.append(f"{prefix}: POST requires SchemaName")
    return issues


def load_manifest(path):
    file = Path(path).resolve()
    raw = file.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    data = json.loads(raw.decode("utf-8-sig"))
    if not isinstance(data, dict):
        return {}, ["manifest must be an object"], digest
    issues = []
    for key in ("approvedBy", "changeId", "blueprintPath"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            issues.append(f"{key} must be a non-empty string")
    try:
        target = normalized_url(data.get("targetUrl"))
    except ValueError as exc:
        issues.append(str(exc))
        target = None
    if not valid_solution(data.get("solutionUniqueName")):
        issues.append("solutionUniqueName must identify a custom solution; Default/System/Active forbidden")
    if data.get("allowDefaultSolution", False) is not False:
        issues.append("allowDefaultSolution must be false")
    if type(data.get("writeApproved", False)) is not bool:
        issues.append("writeApproved must be boolean")
    issues.extend(operation_issues(data.get("operations")))
    if isinstance(data.get("blueprintPath"), str) and data["blueprintPath"]:
        blueprint_path = file.parent / data["blueprintPath"]
        try:
            bp = load_blueprint(blueprint_path)
            actual_hash = hashlib.sha256(blueprint_path.read_bytes()).hexdigest()
            if data.get("blueprintHash") != actual_hash:
                issues.append("blueprintHash missing or different from blueprint bytes")
            if bp.get("solution", {}).get("uniqueName") != data.get("solutionUniqueName"):
                issues.append("blueprint solution differs from manifest")
            if normalized_url(bp.get("solution", {}).get("environment")) != target:
                issues.append("blueprint environment differs from manifest")
        except (OSError, ValueError, TypeError) as exc:
            issues.append(f"blueprint invalid: {exc}")
    return data, issues, digest
