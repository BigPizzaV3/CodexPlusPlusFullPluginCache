#!/usr/bin/env python3
"""Compare declared metadata and UI against actual exported XML; fail closed."""
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from blueprint_schema import load_blueprint

TYPES = {"string": {"nvarchar", "string"}, "email": {"nvarchar", "string"},
         "url": {"nvarchar", "string"}, "multilinetext": {"ntext", "memo"},
         "money": {"money"}, "decimal": {"decimal"}, "integer": {"int", "integer"},
         "boolean": {"bit", "boolean"}, "choice": {"picklist"}, "date": {"datetime"},
         "datetime": {"datetime"}, "lookup": {"lookup"}, "double": {"float", "double"},
         "file": {"file"}, "image": {"image"}, "multiselectchoice": {"multiselectpicklist"}}


def parse(path):
    root = ET.parse(path).getroot()
    for node in root.iter():
        node.tag = node.tag.split("}")[-1]
    return root


def labels(root):
    return {n.get("description", "").casefold() for n in root.findall("./LocalizedNames/LocalizedName")}


def compare(blueprint, folder):
    missing, checks = [], []
    folder = Path(folder)
    def check(ok, kind, **details):
        (checks if ok else missing).append(dict(kind=kind, **details, status="present" if ok else "missing-or-different"))
    entity_dirs = {p.name.casefold(): p for p in (folder / "Entities").glob("*") if p.is_dir()}
    relationships = []
    for path in (folder / "Other/Relationships").glob("*.xml"):
        for rel in parse(path).findall(".//EntityRelationship"):
            relationships.append((rel.findtext("ReferencingEntityName", "").casefold(),
                                  rel.findtext("ReferencedEntityName", "").casefold(),
                                  rel.findtext("ReferencingAttributeName", "").casefold(),
                                  rel.get("Name", "").casefold()))
    field_aliases, page_aliases = {}, {}
    for table in blueprint["dataModel"]["tables"]:
        logical = table["logicalName"].casefold()
        page_aliases[logical] = logical
        if table.get("displayName"):
            page_aliases[table["displayName"].casefold()] = logical
        aliases = field_aliases[logical] = {}
        for col in table.get("columns", []):
            name = col["logicalName"].casefold()
            aliases[name] = name
            if col.get("displayName"):
                aliases[col["displayName"].casefold()] = name
        directory = entity_dirs.get(logical)
        exists = directory is not None and (directory / "Entity.xml").is_file()
        check(exists, "table", table=logical)
        if not exists:
            continue
        root = parse(directory / "Entity.xml")
        columns = {n.findtext("LogicalName", "").casefold(): n for n in root.findall(".//attribute")}
        for name, node in columns.items():
            aliases[name] = name
            for label in node.findall(".//displayname"):
                aliases[label.get("description", "").casefold()] = name
        for column in table.get("columns", []):
            name = column["logicalName"].casefold()
            node = columns.get(name)
            check(node is not None, "column", table=logical, column=name)
            if node is None:
                continue
            actual = node.findtext("Type", "").casefold()
            expected = column["type"].casefold()
            check(actual in TYPES.get(expected, {expected}), "columnType", table=logical, column=name, expected=expected, actual=actual)
            if expected in {"email", "url"}:
                check(node.findtext("Format", "").casefold() == expected, "columnFormat", table=logical, column=name, expected=expected)
            if "required" in column:
                required = node.findtext("RequiredLevel", "").casefold()
                check(required in {"none", "recommended", "required", "applicationrequired", "systemrequired"} and (required in {"required", "applicationrequired", "systemrequired"}) == column["required"], "columnRequired", table=logical, column=name)
        for rel in table.get("relationships", []):
            pair = (logical, rel["target"].casefold())
            if rel.get("type") == "oneToMany":
                pair = pair[::-1]
            matches = [r for r in relationships if r[:2] == pair]
            if rel.get("lookup"):
                matches = [r for r in matches if r[2] == rel["lookup"].casefold()]
            if rel.get("schemaName"):
                matches = [r for r in matches if r[3] == rel["schemaName"].casefold()]
            check(bool(matches) and rel.get("type", "manyToOne") in {"manyToOne", "oneToMany"}, "relationship", table=logical, target=rel["target"])
    for kind, glob, tag, fieldkey in (("forms", "FormXml/**/*.xml", "systemform", "primaryTaskFields"), ("views", "SavedQueries/*.xml", "savedquery", "columns")):
        for expected in blueprint.get(kind, []):
            table = expected["table"].casefold()
            directory = entity_dirs.get(table)
            candidates = []
            for path in directory.glob(glob) if directory else []:
                candidates.extend(parse(path).findall(".//" + tag))
            idtag = "formid" if kind == "forms" else "savedqueryid"
            matched = [n for n in candidates if (expected.get("id") and n.findtext(idtag, "").strip("{}").casefold() == expected["id"].strip("{}").casefold()) or (not expected.get("id") and expected["name"].casefold() in labels(n))]
            check(len(matched) == 1, kind, table=table, name=expected["name"])
            if len(matched) != 1:
                continue
            node = matched[0]
            actual_fields = ({n.get("datafieldname", "").casefold() for n in node.findall(".//control")} if kind == "forms" else {n.get("name", "").casefold() for n in node.findall(".//layoutxml//cell")})
            for field in expected.get(fieldkey, []):
                resolved = field_aliases.get(table, {}).get(field.casefold(), field.casefold())
                check(resolved in actual_fields, kind + "Field", table=table, name=expected["name"], field=field)
            if kind == "views" and expected.get("defaultSort"):
                parts = expected["defaultSort"].rsplit(" ", 1)
                field = field_aliases.get(table, {}).get(parts[0].casefold(), parts[0].casefold())
                orders = node.findall(".//fetchxml/fetch/entity/order")
                check(bool(orders) and orders[0].get("attribute", "").casefold() == field and orders[0].get("descending", "false") == ("true" if len(parts) == 2 and parts[1].lower() == "desc" else "false"), "viewSort", table=table, name=expected["name"])
    subareas = []
    for path in (folder / "AppModuleSiteMaps").rglob("*.xml"):
        subareas.extend(parse(path).findall(".//SubArea"))
    check(bool(subareas), "appNavigation")
    for group in blueprint.get("navigation", []):
        pages = [group["table"]] if group.get("table") else group.get("pages", [])
        for page in pages:
            if isinstance(page, dict):
                key, attr = (page.get("table"), "Entity") if page.get("table") else (page.get("url"), "Url")
            else:
                key, attr = page_aliases.get(page.casefold(), page.casefold()), "Entity"
            check(bool(key) and any(n.get(attr, "").casefold() == key.casefold() for n in subareas), "navigationPage", page=page)
    for page in blueprint.get("customPages", []):
        check(False, "customPageEvidenceRequired", page=page)
    return {"valid": not missing, "missing": missing, "checks": checks, "repairRequired": bool(missing),
            "scope": "Declared tables, columns, types, required levels, relationships, forms, views and sitemap pages. Runtime role/accessibility/UAT evidence remains separate.",
            "nextAction": "Repair differences and export again." if missing else "Declared supported metadata matches; complete runtime and release gates separately."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", type=Path)
    parser.add_argument("solution_folder", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        report = compare(load_blueprint(args.blueprint), args.solution_folder)
    except (OSError, ValueError, ET.ParseError, TypeError) as exc:
        report = {"valid": False, "missing": [], "checks": [], "errors": [str(exc)], "repairRequired": True}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
