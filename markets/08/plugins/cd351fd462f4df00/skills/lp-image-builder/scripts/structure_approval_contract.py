"""Scoped LP decisions; validates declared bindings, not conversation authenticity."""

from __future__ import annotations


FIELD_IDS = {"who", "what", "offer", "conversion_goal", "core_message", "primary_cta", "cta_href"}
STATUSES = {"existing_approved", "provided_unapproved", "proposed", "existing_original_unavailable"}
ORIGINS = {"user_input", "paid_strategy", "paid_evidence", "paid_voc", "paid_results", "inference"}


class ApprovalContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ApprovalContractError(message)


def field_values(document: dict) -> dict:
    handoff = document.get("fv_handoff", {})
    return {
        "who": document.get("audience"),
        "what": handoff.get("scan_contract", {}).get("what_it_is", {}).get("answer"),
        "offer": document.get("offer"),
        "conversion_goal": document.get("objective"),
        "core_message": handoff.get("dominant_message"),
        "primary_cta": document.get("primary_cta"),
        "cta_href": document.get("cta_strategy", {}).get("primary", {}).get("href"),
    }


def validate_source_fields(source: dict) -> None:
    fields = source.get("field_values")
    require(source.get("kind") == "business-record" and isinstance(fields, list) and fields,
            "approval source field_values require a non-empty business record")
    seen = set()
    for item in fields:
        require(isinstance(item, dict) and set(item) == {"field", "value", "status"},
                "approval source field/value/status fields are invalid")
        field = item.get("field")
        require(field in FIELD_IDS and field not in seen, "approval source field must be known and unique")
        seen.add(field)
        status = item.get("status")
        require(status in STATUSES - {"proposed"}, "approval source status is invalid")
        require((status == "existing_original_unavailable" and item["value"] is None)
                or (status != "existing_original_unavailable"
                    and isinstance(item["value"], str) and item["value"].strip()),
                "approval source original value must match its availability")
        if status in {"existing_approved", "existing_original_unavailable"}:
            require(source.get("provided_by") in {"user", "controller"},
                    "existing approval must be supplied by user/controller")


def validate(document: dict, sources: dict, *, for_images: bool = False, for_clicks: bool = False) -> dict:
    contract = document.get("approval_contract")
    require(isinstance(contract, dict) and set(contract) == {"kind", "schema_version", "fields", "request"}
            and contract.get("kind") == "lp-structure-approval-contract"
            and contract.get("schema_version") == "1.0", "structure approval_contract is required")
    require(not document.get("locked_items"), "new structures derive locks from approval_contract, not locked_items")
    unknowns = document.get("evidence_and_unknowns", [])
    require(isinstance(unknowns, list), "unresolved questions must be an array")
    for question in unknowns:
        require(isinstance(question, dict) and set(question) == {"question", "source_ids"}
                and isinstance(question["question"], str) and question["question"].strip(),
                "unresolved questions accept only question/source_ids; approval authority belongs to approval_contract")
        refs = question["source_ids"]
        require(isinstance(refs, list) and all(isinstance(ref, str) and ref in sources for ref in refs)
                and len(refs) == len(set(refs)), "unresolved question source_ids must resolve uniquely")
    values = field_values(document)
    require(all(isinstance(value, str) and value.strip() for key, value in values.items() if key != "cta_href"),
            "approval contract requires concrete proposed structure values")
    fields = contract.get("fields")
    require(isinstance(fields, list) and len(fields) == len(FIELD_IDS), "approval fields must cover all decision fields")
    by_id = {}
    route = document.get("acquisition_route_brief", {})
    for item in fields:
        require(isinstance(item, dict) and set(item) == {"field", "origin", "status", "source_ids"},
                "approval field fields are invalid")
        field, origin, status = item.get("field"), item.get("origin"), item.get("status")
        require(field in FIELD_IDS and field not in by_id, "approval field must be known and unique")
        by_id[field] = item
        require(origin in ORIGINS and status in STATUSES, "approval field origin/status is invalid")
        require(origin in {"user_input", "inference"} or route.get("mode") == "paid_quality",
                "paid approval origins require the bound paid route context")
        refs = item.get("source_ids")
        require(isinstance(refs, list) and all(isinstance(ref, str) and ref in sources for ref in refs)
                and len(refs) == len(set(refs)), "approval source_ids must resolve uniquely")
        if field in route.get("strategy", {}):
            require(origin == route["strategy"][field]["source"], "approval origin must preserve route source")
        if status in {"existing_approved", "provided_unapproved"}:
            require(origin != "inference", "inference cannot become existing approval or supplied original")
        else:
            require(origin == "inference", "proposed or unavailable originals must retain inference origin")
        if status != "proposed":
            expected = {"field": field, "value": None if status == "existing_original_unavailable" else values[field],
                        "status": status}
            require(refs and all(expected in sources[ref].get("field_values", []) for ref in refs),
                    f"approval {field} must bind the exact source field, original value and status")
        if status == "existing_original_unavailable":
            readiness = route.get("readiness", {})
            require(readiness.get("status") != "ready" and field in readiness.get("missing_critical", []),
                    f"unavailable existing {field} must remain a critical unknown, not ready")
        if field == "cta_href":
            if values[field] is None:
                require(status == "proposed" and not refs, "unset CTA destination cannot be approved or source-bound")
            else:
                require(status in {"existing_approved", "provided_unapproved"},
                        "concrete CTA destination requires a supplied original, not an invented path")

    request = contract.get("request")
    require(isinstance(request, dict)
            and set(request) == {"mode", "field_ids", "section_ids", "hypothesis_design"},
            "approval request fields are invalid")
    require(request.get("mode") in {"review_only", "partial_structure", "full_structure"}
            and type(request.get("hypothesis_design")) is bool, "approval request mode is invalid")
    available_fields = FIELD_IDS - ({"cta_href"} if values["cta_href"] is None else set())
    available_sections = {section["id"] for section in document["sections"]}
    for key, available in (("field_ids", available_fields), ("section_ids", available_sections)):
        chosen = request.get(key)
        require(isinstance(chosen, list) and all(isinstance(value, str) and value in available for value in chosen)
                and len(chosen) == len(set(chosen)), f"approval request {key} must name exact available items")
    if request["mode"] == "review_only":
        require(not request["field_ids"] and not request["section_ids"], "review-only draft cannot request approval")
    else:
        require(request["field_ids"] or request["section_ids"], "approval request must identify its scope")
    complete = set(request["field_ids"]) == available_fields and set(request["section_ids"]) == available_sections
    require((request["mode"] == "full_structure") == complete, "full/partial approval request must match its exact scope")
    hypothetical = any(by_id[field]["status"] in {"proposed", "existing_original_unavailable"}
                       for field in request["field_ids"])
    require(not hypothetical or request["hypothesis_design"], "hypotheses require an explicit hypothesis-design request")
    if for_images or for_clicks:
        require(request["mode"] == "full_structure", "partial/review-only approval cannot authorize whole-structure production")
    if for_clicks:
        require(values["cta_href"] is not None, "interactive assembly requires a source-bound CTA destination")
    return contract


def approval_lines(document: dict) -> list[str]:
    contract = document["approval_contract"]
    values = field_values(document)
    lines = ["", "## Source and approval scope", "",
             "Original source and existing approval remain distinct from this proposed design."]
    for field in contract["fields"]:
        value = values[field["field"]]
        rendered = str(value).replace("\n", " ") if value is not None else "unset; no clickable destination"
        lines.append(f"- {field['field']}: {rendered} — origin `{field['origin']}`, authority `{field['status']}`; sources {', '.join(field['source_ids']) or 'none'}")
    request = contract["request"]
    lines += ["", "## Approval", "", f"- Requested scope: `{request['mode']}`",
              f"- Fields: {', '.join(request['field_ids']) or 'none'}",
              f"- Sections: {', '.join(request['section_ids']) or 'none'}",
              f"- Hypothesis design: `{str(request['hypothesis_design']).lower()}`",
              "This request grants no upstream strategy overwrite, source verification, spending, publication or external submission."]
    if request["mode"] == "review_only":
        lines.append("Review draft only. No production approval is requested; retain the unresolved originals and continue the scoped draft work.")
    elif request["mode"] == "partial_structure":
        lines.append("A reply approves only the listed fields/sections. It cannot authorize whole-structure image production; use scope lp-structure-partial when recording that decision.")
    else:
        lines.append("Reply with OK / このまま進めて to approve this exact JSON's full design scope (including explicitly listed hypotheses), or list changes. Hypotheses remain inferences and unavailable upstream originals remain unknown. Record the separate user/controller decision before image production. JSON changes require regenerating this view.")
    return lines + [""]
