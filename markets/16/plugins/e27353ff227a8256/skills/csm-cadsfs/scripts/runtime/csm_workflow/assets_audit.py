"""Auditoría de sólo lectura para el propietario; NO es el generador ni CADSFS.

Comprueba el contenedor y sus referencias. No transforma proyectos ni certifica
su apertura, rendimiento acústico, conservación al editar o ausencia de secretos.
La lectura OOXML es acotada, sin macros, fórmulas, enlaces ni acceso a red.
"""
from __future__ import annotations

import argparse
import array
import base64
import binascii
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile
import zlib
from typing import Any

MAX_FILE_BYTES = 32 * 1024 * 1024
MAX_ARRAY_BYTES = 16 * 1024 * 1024
MAX_PROJECT_ARRAY_BYTES = 128 * 1024 * 1024
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


class AuditError(ValueError):
    """Error legible y acotado: no incluye contenido de los archivos."""


def read_bytes(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise AuditError("archivo_no_regular")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise AuditError("archivo_demasiado_grande")
    with path.open("rb") as handle:
        raw = handle.read(MAX_FILE_BYTES + 1)
    if len(raw) > MAX_FILE_BYTES:
        raise AuditError("archivo_demasiado_grande")
    return raw


def strict_json(raw: bytes) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise AuditError("clave_duplicada")
            result[key] = value
        return result

    def bad_constant(value: str) -> None:
        raise AuditError("numero_no_finito")

    if len(raw) > MAX_FILE_BYTES:
        raise AuditError("archivo_demasiado_grande")
    try:
        result = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=pairs,
                            parse_constant=bad_constant)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise AuditError("json_ilegible") from exc
    if not isinstance(result, dict):
        raise AuditError("raiz_no_objeto")
    pending = [result]
    while pending:
        item = pending.pop()
        if isinstance(item, float) and not math.isfinite(item):
            raise AuditError("numero_no_finito")
        if isinstance(item, dict):
            pending.extend(item.values())
        elif isinstance(item, list):
            pending.extend(item)
    return result


def decode_array(blob: Any, expected: str, columns: int | None = None) -> tuple[array.array, bool]:
    """Interpreta únicamente float32/int32 little-endian; devuelve si faltaba dtype.

    Un dtype omitido se infiere SÓLO para inspección de un campo conocido y queda
    señalado. No afirma que el lector CADSFS adopte la misma interpretación.
    """
    if not isinstance(blob, dict):
        raise AuditError("array_ausente")
    inferred = "dtype" not in blob
    if blob.get("dtype", expected) != expected or expected not in ("float32", "int32"):
        raise AuditError("dtype_no_admitido")
    if columns is None:
        length = blob.get("length")
        if type(length) is not int or length < 0:
            raise AuditError("longitud_invalida")
        count = length
    else:
        shape = blob.get("shape")
        if (not isinstance(shape, list) or len(shape) != 2
                or any(type(i) is not int or i < 0 for i in shape) or shape[1] != columns):
            raise AuditError("forma_invalida")
        count = shape[0] * columns
    expected_bytes = count * 4
    if expected_bytes > MAX_ARRAY_BYTES:
        raise AuditError("array_demasiado_grande")
    encoded = blob.get("data")
    if not isinstance(encoded, str) or len(encoded) > MAX_FILE_BYTES:
        raise AuditError("datos_array_invalidos")
    try:
        packed = base64.b64decode(encoded, validate=True)
        decomp = zlib.decompressobj()
        decoded = decomp.decompress(packed, expected_bytes + 1)
        if (len(decoded) != expected_bytes or not decomp.eof
                or decomp.unused_data or decomp.unconsumed_tail):
            raise AuditError("longitud_o_stream_invalido")
    except (binascii.Error, zlib.error, ValueError) as exc:
        if isinstance(exc, AuditError):
            raise
        raise AuditError("codificacion_array_invalida") from exc
    values = array.array("f" if expected == "float32" else "i")
    if values.itemsize != 4:
        raise AuditError("plataforma_no_admitida")
    values.frombytes(decoded)
    if sys.byteorder != "little":
        values.byteswap()
    if expected == "float32" and not all(math.isfinite(x) for x in values):
        raise AuditError("vertice_no_finito")
    return values, inferred


def material_catalog(path: Path) -> dict[str, Any]:
    """Cuenta registros y lee nombres de la hoja recibida; no recalcula el XLSX.

    Lector OOXML mínimo sólo para esta biblioteca: no admite archivos cifrados,
    declaraciones DTD/entidades ni fórmulas en los identificadores consultados.
    """
    read_bytes(path)  # Comprobación de archivo/tamaño antes de abrir el contenedor.
    try:
        with zipfile.ZipFile(path) as archive:
            if sum(i.file_size for i in archive.infolist()) > 64 * 1024 * 1024:
                raise AuditError("xlsx_descomprimido_demasiado_grande")
            def xml(name: str) -> ET.Element:
                raw = archive.read(name)
                if b"<!DOCTYPE" in raw.upper() or b"<!ENTITY" in raw.upper():
                    raise AuditError("xml_no_admitido")
                return ET.fromstring(raw)
            shared: list[str] = []
            if "xl/sharedStrings.xml" in archive.namelist():
                shared = ["".join(t.text or "" for t in i.findall(".//s:t", NS))
                          for i in xml("xl/sharedStrings.xml")]
            sheets = [n for n in archive.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")]
            if len(sheets) != 1:
                raise AuditError("biblioteca_requiere_una_hoja")
            rows = xml(sheets[0]).findall("s:sheetData/s:row", NS)
            def row_values(row: ET.Element) -> dict[str, str]:
                result = {}
                for cell in row:
                    col = "".join(c for c in cell.get("r", "") if c.isalpha())
                    if col not in ("A", "B", "G"):
                        continue
                    if cell.find("s:f", NS) is not None:
                        raise AuditError("formula_en_identificador")
                    value = cell.find("s:v", NS)
                    text = value.text if value is not None else ""
                    kind = cell.get("t")
                    if kind == "s":
                        text = shared[int(text)]
                    elif kind == "inlineStr":
                        text = "".join(t.text or "" for t in cell.findall(".//s:t", NS))
                    result[col] = text or ""
                return result
            if not rows or row_values(rows[0]).get("A") != "ID" or row_values(rows[0]).get("B") != "Nombre":
                raise AuditError("cabecera_biblioteca_no_reconocida")
            records = [row_values(r) for r in rows[1:]]
            records = [r for r in records if r.get("A")]
            ids = [r["A"] for r in records]
            names = {r[c] for r in records for c in ("B", "G") if r.get(c)}
            return {"records": len(records), "unique_ids": len(set(ids)),
                    "duplicate_ids": sorted(k for k, v in Counter(ids).items() if v > 1),
                    "names": names, "reading_mode": "read_only_ooxml_no_recalculation"}
    except (zipfile.BadZipFile, KeyError, ET.ParseError, IndexError, ValueError) as exc:
        if isinstance(exc, AuditError):
            raise
        raise AuditError("biblioteca_xlsx_ilegible") from exc


def speaker_catalog(path: Path) -> dict[str, Any]:
    data = strict_json(read_bytes(path))
    records = data.get("speakers")
    if not isinstance(records, list) or any(not isinstance(s, dict) or not isinstance(s.get("id"), str) for s in records):
        raise AuditError("biblioteca_altavoces_invalida")
    ids = [s["id"] for s in records]
    return {"records": len(records), "unique_ids": len(set(ids)), "ids": set(ids),
            "duplicate_ids": sorted(k for k, v in Counter(ids).items() if v > 1),
            "verification_flags_are_source_claims": True}


def audit_project(path: Path, material_names: set[str] | None = None,
                  speaker_ids: set[str] | None = None) -> dict[str, Any]:
    findings: dict[tuple[str, str], list[str]] = {}
    def flag(level: str, code: str, location: str) -> None:
        findings.setdefault((level, code), []).append(location)

    raw = read_bytes(path)
    report: dict[str, Any] = {"file": path.name, "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(), "modified": False,
        "opened_in_cadsfs": False, "generator_executed": False,
        "scope": "estructura_y_referencias; NO_validacion_integral"}
    try:
        doc = strict_json(raw)
    except AuditError as exc:
        return {**report, "structural_ok": False, "findings": [{"level": "error", "code": str(exc), "count": 1}]}
    if doc.get("app") != "CADSFS":
        flag("warning", "app_no_identificada_como_CADSFS", "raiz")
    objects = doc.get("objects", [])
    if not isinstance(objects, list):
        objects = []
        flag("error", "objetos_no_son_lista", "raiz")
    stats = {"objects": len(objects), "vertices": 0, "triangles": 0, "enclosures": 0}
    ids = []
    enclosures = []
    array_budget = 0
    for position, obj in enumerate(objects):
        loc = f"objeto_indice_{position}"
        if not isinstance(obj, dict):
            flag("error", "objeto_no_diccionario", loc)
            continue
        ident = obj.get("obj_id")
        if type(ident) is not int:
            flag("error", "id_objeto_invalido", loc)
        else:
            ids.append(ident)
            loc = f"objeto_{ident}"
        if obj.get("is_enclosure") is True:
            enclosures.append(ident)
            stats["enclosures"] += 1
        try:
            verts, vi = decode_array(obj.get("base_vertices_world"), "float32", 3)
            faces, fi = decode_array(obj.get("faces_local"), "int32", 3)
            groups, gi = decode_array(obj.get("face_to_group_idx"), "int32")
            array_budget += (len(verts) + len(faces) + len(groups)) * 4
            if array_budget > MAX_PROJECT_ARRAY_BYTES:
                raise AuditError("presupuesto_arrays_excedido")
            if vi or fi or gi:
                flag("warning", "dtype_omitido_interpretado_solo_para_auditoria", loc)
            nv, nf = len(verts)//3, len(faces)//3
            stats["vertices"] += nv
            stats["triangles"] += nf
            if nv < 3 or nf < 1:
                flag("error", "malla_vacia_o_incompleta", loc)
            if any(i < 0 or i >= nv for i in faces):
                flag("error", "indice_vertice_fuera_de_rango", loc)
            if len(groups) != nf:
                flag("error", "grupos_no_coinciden_con_triangulos", loc)
            order = obj.get("group_order")
            if (not isinstance(order, list) or not all(isinstance(g, str) for g in order)
                    or any(i < 0 or i >= len(order) for i in groups)):
                flag("error", "indice_o_tabla_de_grupos_invalido", loc)
            if obj.get("is_enclosure") is True:
                edges: Counter[tuple[int, int]] = Counter()
                for i in range(0, len(faces), 3):
                    a, b, c = faces[i:i+3]
                    for x, y in ((a,b),(b,c),(c,a)):
                        edges[min(x,y), max(x,y)] += 1
                if any(n != 2 for n in edges.values()):
                    flag("warning", "envolvente_no_cerrada_por_conteo_de_aristas", loc)
        except AuditError as exc:
            flag("error", str(exc), loc)
            if str(exc) == "presupuesto_arrays_excedido":
                break
    for ident, count in Counter(ids).items():
        if count > 1:
            flag("error", "id_objeto_duplicado", str(ident))
    if not doc.get("outdoor_mode", False):
        if not enclosures or doc.get("active_enclosure_id") not in enclosures:
            flag("error", "envolvente_activa_no_resuelta", "raiz")
    materials = doc.get("materials")
    stats["embedded_material_records"] = len(materials) if isinstance(materials, list) else None
    if materials:
        flag("warning", "biblioteca_embebida_no_copiar_a_salida_nueva", "raiz")
    mapping = doc.get("surface_group_material", {})
    if not isinstance(mapping, dict):
        mapping = {}
        flag("error", "asignaciones_material_no_diccionario", "raiz")
    material_values = list(mapping.values())
    if any(not isinstance(x, str) for x in material_values):
        flag("error", "nombre_material_no_texto", "raiz")
    stats["default_surface_values"] = sum(x == "Default" for x in material_values)
    if stats["default_surface_values"]:
        flag("warning", "default_en_mapa_de_superficies_revisar_grupos_usados", "raiz")
    unknown_materials = (sorted({x for x in material_values if isinstance(x, str) and x != "Default"} - material_names)
                         if material_names is not None else [])
    report["unresolved_exact_material_names"] = unknown_materials
    if unknown_materials:
        flag("warning", "nombres_sin_coincidencia_exacta_no_prueba_de_incompatibilidad", "raiz")
    systems = doc.get("speaker_systems", [])
    if not isinstance(systems, list):
        systems = []
        flag("error", "sistemas_no_son_lista", "raiz")
    used_speakers = set()
    count_elements = 0
    for i, system in enumerate(systems):
        elements = system.get("elements", []) if isinstance(system, dict) else None
        if not isinstance(elements, list):
            flag("error", "sistema_o_elementos_invalidos", f"sistema_{i}")
            continue
        count_elements += len(elements)
        for elem in elements:
            if not isinstance(elem, dict):
                flag("error", "elemento_no_diccionario", f"sistema_{i}")
            elif isinstance(elem.get("model_id"), str):
                used_speakers.add(elem["model_id"])
            else:
                flag("warning", "modelo_altavoz_no_declarado", f"sistema_{i}")
    unknown_speakers = sorted(used_speakers - speaker_ids) if speaker_ids is not None else []
    if unknown_speakers:
        flag("warning", "modelo_sin_coincidencia_exacta", "raiz")
    report["unresolved_speaker_ids"] = unknown_speakers
    for key in ("audience_areas", "audience_zones", "beam_arrays"):
        value = doc.get(key, [])
        stats[key] = len(value) if isinstance(value, list) else None
        if not isinstance(value, list):
            flag("warning", "coleccion_no_lista", key)
    stats.update({"speaker_systems": len(systems), "speaker_elements": count_elements,
                  "outdoor": bool(doc.get("outdoor_mode", False)),
                  "material_assignments": len(mapping)})
    for key in ("source_pos", "receiver_pos"):
        value = doc.get(key)
        if (not isinstance(value, list) or len(value) != 3
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in value)):
            flag("error", "posicion_puntual_invalida", key)
    if doc.get("source_pos") == doc.get("receiver_pos"):
        flag("warning", "fuente_receptor_coincidentes", "raiz")
    report["stats"] = stats
    report["findings"] = [{"level": level, "code": code, "count": len(locs), "locations": locs[:8]}
                          for (level, code), locs in sorted(findings.items())]
    report["structural_ok"] = not any(i["level"] == "error" for i in report["findings"])
    report["catalog_compatibility_confirmed"] = False
    report["full_acoustic_validation_performed"] = False
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Auditoría local de CSM; no genera ni modifica archivos.")
    parser.add_argument("--assets-dir", type=Path, required=True)
    parser.add_argument("--report-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        material = material_catalog(args.assets_dir / "biblioteca_materiales_acustica_2665_i18n_translated.xlsx")
        speaker = speaker_catalog(args.assets_dir / "speaker_library_release_v6_unified_v22_completo.json")
        reports = [audit_project(p, material["names"], speaker["ids"]) for p in sorted(args.assets_dir.glob("*.csm"))]
        result = {"version": "0.3.0", "read_only": True,
                  "materials": {k: v for k, v in material.items() if k != "names"},
                  "speakers": {k: v for k, v in speaker.items() if k != "ids"},
                  "projects": reports, "cad_validation_run": False,
                  "generator_executed": False, "public_link": None}
        args.report_dir.mkdir(parents=True, exist_ok=True)
        output = args.report_dir / "audit_real_assets.json"
        if output.exists():
            parser.error("El informe ya existe; elegí otra carpeta para no sobrescribir.")
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Se inspeccionaron {len(reports)} CSM sin modificarlos; informe del propietario: {output}")
        return 0 if reports and all(r["structural_ok"] for r in reports) else 2
    except (AuditError, OSError) as exc:
        print(f"Auditoría no completada: {exc.__class__.__name__}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
