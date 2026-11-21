"""Local delivery evidence primitives; deliberately bundled with each owning skill."""

from __future__ import annotations
import hashlib
import json
from pathlib import Path

VERSION = "7454.1"
STATES = ("outline", "working-draft", "review-draft", "submission-candidate")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mounted_skill_script_directories(start):
    """Every ``skills/<skill>/scripts`` directory visible from ``start`` or one
    of its ancestors, without assuming where the host mounts skills."""
    seen = []
    for ancestor in [start, *start.parents]:
        for pattern in ("skills/*/scripts", "*/skills/*/scripts", "*/*/skills/*/scripts"):
            try:
                found = sorted(ancestor.glob(pattern))
            except OSError:
                continue
            for candidate in found:
                if candidate.is_dir() and candidate not in seen:
                    seen.append(candidate)
    return seen


def skill_directory():
    """The mounted skill directory this validator belongs to, so a receipt names
    the skill whose checks it records instead of leaving that to inference.

    In place, the skill directory is the ancestor holding SKILL.md above this
    scripts directory. When the documented whole-directory relocation copied
    scripts/ into a task workspace, that ancestor is gone, so the copy is
    matched byte-for-byte against the scripts of each mounted skill that is
    visible from the workspace; an ambiguous or modified copy yields None
    rather than a guess."""
    try:
        here = Path(__file__).resolve()
    except OSError:
        return None
    for ancestor in here.parents[1:]:
        if (ancestor / "SKILL.md").is_file() and (ancestor / "scripts" / here.name).is_file():
            return ancestor.name or None
    try:
        local = {p.name: p.read_bytes() for p in here.parent.glob("*.py")}
    except OSError:
        return None
    matches = []
    for candidate in mounted_skill_script_directories(here.parent):
        try:
            names = {p.name for p in candidate.glob("*.py")}
            if names == set(local) and all(
                (candidate / name).read_bytes() == body for name, body in local.items()
            ):
                matches.append(candidate.parent.name)
        except OSError:
            continue
    return matches[0] if len(matches) == 1 else None


def contract_digest(contract):
    return (
        hashlib.sha256(
            json.dumps(contract, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        if contract is not None
        else None
    )


def load_contract(path, allowed):
    contract = json.loads(Path(path).read_text())
    if (
        not isinstance(contract, dict)
        or type(contract.get("schema_version")) is not int
        or contract.get("schema_version") != 1
    ):
        raise ValueError("Contract must be an object with schema_version 1")
    unknown = (
        set(contract)
        - set(allowed)
        - {
            "schema_version",
            "state",
            "mandatory_inputs",
            "required_text",
            "render",
            "notes",
            "visual_review",
        }
    )
    if unknown:
        raise ValueError("Unknown contract fields: " + ", ".join(sorted(unknown)))
    if contract.get("state", "submission-candidate") not in STATES:
        raise ValueError("Unknown delivery state")
    for field in ("mandatory_inputs", "required_text"):
        if field in contract and (
            not isinstance(contract[field], list)
            or not all(isinstance(v, str) for v in contract[field])
        ):
            raise ValueError(field + " must be a list of strings")
    if "visual_review" in contract and (
        not isinstance(contract["visual_review"], str)
        or not contract["visual_review"].strip()
    ):
        raise ValueError("visual_review must describe the completed inspection")
    if "render" in contract and not isinstance(contract["render"], dict):
        raise ValueError("render must be an object")
    rendering = contract.get("render", {})
    if set(rendering) - {"required", "keep_together", "repeated_headers"}:
        raise ValueError("Unknown render contract fields")
    if "required" in rendering and not isinstance(rendering["required"], bool):
        raise ValueError("render.required must be boolean")
    for group in rendering.get("keep_together", []):
        if (
            not isinstance(group, dict)
            or set(group) != {"lead", "follow"}
            or not all(isinstance(v, str) and v for v in group.values())
        ):
            raise ValueError("keep_together requires nonempty lead/follow strings")
    for table in rendering.get("repeated_headers", []):
        if (
            not isinstance(table, dict)
            or set(table) != {"header", "row_markers"}
            or not isinstance(table["header"], str)
            or not isinstance(table["row_markers"], list)
            or not all(isinstance(v, str) and v for v in table["row_markers"])
        ):
            raise ValueError("repeated_headers requires header and row_markers")
    return contract


def bind_render(artifact, outputs, directory):
    manifest = {
        "artifact_sha256": digest(artifact),
        "outputs": {Path(p).name: digest(p) for p in outputs},
    }
    Path(directory, "render-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n"
    )
    return manifest


def verify_render(artifact, directory):
    directory = Path(directory)
    manifest = json.loads((directory / "render-manifest.json").read_text())
    if manifest.get("artifact_sha256") != digest(artifact):
        raise ValueError(
            "Render manifest artifact hash mismatch; render exact final binary again"
        )
    outputs = manifest.get("outputs")
    if (
        not isinstance(outputs, dict)
        or not outputs
        or not any(n.endswith(".pdf") for n in outputs)
        or not any(n.endswith(".png") for n in outputs)
    ):
        raise ValueError("Render manifest requires PDF and PNG outputs")
    for name, sha in outputs.items():
        if Path(name).name != name or digest(directory / name) != sha:
            raise ValueError("Rendered output hash mismatch: " + name)
    return outputs


def finish(
    result,
    artifact,
    contract=None,
    checks=(),
    unresolved=(),
    rendered_dir=None,
    final_validation=True,
):
    unresolved = list(unresolved)
    executed = list(checks)
    rendered = {}
    if rendered_dir:
        try:
            rendered = verify_render(artifact, rendered_dir)
            executed.append("rendered-output-integrity")
        except (OSError, ValueError, TypeError, KeyError) as exc:
            result["errors"].append(str(exc))
    else:
        unresolved.append("rendered-layout-review")
    if contract is None:
        unresolved.append("task-contract-not-supplied")
    elif contract.get("mandatory_inputs"):
        unresolved.extend("missing-input:" + v for v in contract["mandatory_inputs"])
        if (
            final_validation
            and contract.get("state", "submission-candidate") == "submission-candidate"
        ):
            result["errors"].append(
                "Submission candidate has unresolved mandatory inputs"
            )
    if (
        final_validation
        and contract is not None
        and contract.get("render", {}).get("required", False)
        and not rendered_dir
    ):
        result["errors"].append("Required rendering was not executed")
    if contract is not None and rendered and not contract.get("visual_review"):
        unresolved.append("visual-review-not-recorded")
    elif contract is not None and rendered:
        executed.append("recorded-visual-review")
    result.update(
        validation_stage="final" if final_validation else "behavioral-probe",
        status="failed" if result["errors"] else "passed",
        artifact_sha256=digest(artifact),
        validator_version=VERSION,
        skill_directories=[d for d in [skill_directory()] if d],
        contract_digest=contract_digest(contract),
        executed_checks=sorted(set(executed)),
        unresolved_checks=sorted(set(unresolved)),
        rendered_output_hashes=rendered,
        readiness=(
            "failed"
            if result["errors"]
            else ("unresolved" if unresolved else "verified")
        ),
        state=contract.get("state", "submission-candidate") if contract else None,
    )
    return result


def verify_receipt(artifact, receipt, contract):
    expected = (digest(artifact), VERSION, contract_digest(contract))
    actual = tuple(
        receipt.get(k)
        for k in ("artifact_sha256", "validator_version", "contract_digest")
    )
    if actual != expected:
        raise ValueError(
            "Stale QA receipt: artifact, validator version, or contract digest changed"
        )
    return True
