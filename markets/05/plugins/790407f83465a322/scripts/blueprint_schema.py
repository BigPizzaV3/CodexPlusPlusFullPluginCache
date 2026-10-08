"""Shared structural validation. No implicit conversion of invalid blueprints."""
import json
import re
from pathlib import Path

NAME = re.compile(r"[a-z][a-z0-9_]*", re.I)


def validate_blueprint(data):
    issues = []
    if not isinstance(data, dict):
        return ["blueprint must be an object"]
    if not isinstance(data.get("solution", {}), dict):
        return ["solution must be an object"]
    model = data.get("dataModel")
    tables = model.get("tables") if isinstance(model, dict) else None
    if not isinstance(tables, list) or not tables:
        return ["dataModel.tables must be a non-empty list"]
    seen = set()
    for table in tables:
        if not isinstance(table, dict):
            issues.append("each table must be an object")
            continue
        name = table.get("logicalName", "")
        if not isinstance(name, str) or not NAME.fullmatch(name):
            issues.append("table.logicalName must be a valid identifier")
        elif name.lower() in seen:
            issues.append(f"duplicate table: {name}")
        else:
            seen.add(name.lower())
        columns = table.get("columns", [])
        if not isinstance(columns, list):
            issues.append(f"{name}.columns must be a list")
            continue
        column_names = set()
        for column in columns:
            logical = column.get("logicalName", "") if isinstance(column, dict) else ""
            if not isinstance(logical, str) or not NAME.fullmatch(logical):
                issues.append(f"{name}: column.logicalName required")
            elif logical.lower() in column_names:
                issues.append(f"{name}: duplicate column {logical}")
            else:
                column_names.add(logical.lower())
            if not isinstance(column, dict) or not isinstance(column.get("type"), str) or not column["type"]:
                issues.append(f"{name}.{logical}: column.type required")
            elif "required" in column and type(column["required"]) is not bool:
                issues.append(f"{name}.{logical}: required must be boolean")
        rels = table.get("relationships", [])
        if not isinstance(rels, list) or any(not isinstance(r, dict) or not isinstance(r.get("target"), str) or not NAME.fullmatch(r["target"]) for r in rels):
            issues.append(f"{name}.relationships must contain objects with target identifiers")
    for key in ("forms", "views", "navigation"):
        values = data.get(key, [])
        if not isinstance(values, list) or any(not isinstance(v, dict) for v in values):
            issues.append(f"{key} must be a list of objects")
            continue
        for value in values:
            if key != "navigation":
                if not isinstance(value.get("name"), str) or not value["name"] or not isinstance(value.get("table"), str) or value["table"].lower() not in seen:
                    issues.append(f"{key}: name and a declared table required")
                fields = value.get("primaryTaskFields" if key == "forms" else "columns", [])
                if not isinstance(fields, list) or any(not isinstance(f, str) for f in fields):
                    issues.append(f"{key}: fields must be strings")
            elif not value.get("table") and not value.get("pages"):
                issues.append("navigation: table or non-empty pages required")
            elif value.get("table") and not isinstance(value["table"], str):
                issues.append("navigation.table must be a string")
            elif "pages" in value and (not isinstance(value["pages"], list) or any(not isinstance(p, (str, dict)) for p in value["pages"])):
                issues.append("navigation.pages must contain names or target objects")
    for section, keys in {"security": ["leastPrivilegeReviewed", "roleTaskMatrix", "fieldSecurityReviewed"],
                          "testing": ["keyboardTest", "responsiveTest", "roleSmokeTests"],
                          "performance": ["representativeDataTest"], "change": ["impactReviewed", "existingApp"],
                          "alm": ["devUnmanaged", "downstreamManaged", "repositoryExport"]}.items():
        value = data.get(section, {})
        if not isinstance(value, dict):
            issues.append(f"{section} must be an object")
        else:
            for key in keys:
                if key in value and type(value[key]) is not bool:
                    issues.append(f"{section}.{key} must be boolean")
    return issues


def load_blueprint(path):
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    issues = validate_blueprint(data)
    if issues:
        raise ValueError("Invalid blueprint: " + "; ".join(issues))
    return data
