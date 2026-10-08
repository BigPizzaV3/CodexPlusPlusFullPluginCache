"""Deterministic preview data; no production identifiers or contact addresses."""
from datetime import date, timedelta
from uuid import NAMESPACE_URL, uuid5


def generate_samples(blueprint, count=3):
    tables = blueprint["dataModel"]["tables"]
    ids = {t["logicalName"]: [str(uuid5(NAMESPACE_URL, f"synthetic.invalid/{t['logicalName']}/{i}")) for i in range(count)] for t in tables}
    result = {}
    for table in tables:
        name = table["logicalName"]
        records = []
        for index in range(count):
            row = {name + "id": ids[name][index]}
            for column in table.get("columns", []):
                field, kind = column["logicalName"], column["type"].lower()
                if kind in {"string", "multilinetext", "memo"}:
                    value = f"Sample {index + 1}: {field}"
                    value = value[:column.get("maxLength", 100)]
                elif kind in {"money", "decimal", "double"}:
                    value = round(10.25 * (index + 1), 2)
                elif kind in {"integer", "int", "bigint"}:
                    value = index + 1
                elif kind == "boolean":
                    value = index % 2 == 0
                elif kind in {"date", "datetime"}:
                    value = (date(2026, 1, 1) + timedelta(days=index)).isoformat()
                    if kind == "datetime":
                        value += "T12:00:00Z"
                elif kind == "email":
                    value = f"sample{index + 1}@example.invalid"
                elif kind == "url":
                    value = f"https://example.invalid/sample/{index + 1}"
                elif kind in {"choice", "multiselectchoice"}:
                    options = column.get("values", [])
                    if not options:
                        raise ValueError(f"{name}.{field}: explicit choice values required")
                    option = options[index % len(options)]
                    value = option.get("value") if isinstance(option, dict) else option
                    if value is None:
                        raise ValueError(f"{name}.{field}: choice value required")
                    if kind == "multiselectchoice":
                        value = [value]
                elif kind == "lookup":
                    target = column.get("target")
                    if target not in ids:
                        raise ValueError(f"{name}.{field}: declared lookup target required for synthetic references")
                    value = ids[target][index]
                elif kind in {"file", "image"} and not column.get("required"):
                    value = None
                else:
                    raise ValueError(f"{name}.{field}: unsupported synthetic data type {kind}")
                row[field] = value
            records.append(row)
        result[name] = records
    return result
