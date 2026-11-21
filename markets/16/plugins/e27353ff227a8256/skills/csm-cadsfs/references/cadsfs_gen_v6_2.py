#!/usr/bin/env python3
"""
CADSFS JSON Generator v6 — genera proyectos de sala para CADSFS.
CANA SAN MARTIN — CADSFS V1.49.84 (gen v6.1)

Cambios v6:
  - materials: [] (NUNCA incluir materiales custom — usa DB interna de 2665 entries)
  - surface_group_material_b + surface_assembly_map + wall_assemblies incluidos
  - Geometría centrada en (0,0) con Y=0 como eje de simetría
  - Extrusiones usan Wall 1..N (no Wall_0)
  - Studio monitor library completa: 30 modelos / 10 marcas
  - Presets de assemblies incluidos

Uso:
    python cadsfs_gen__6_.py --width 10 --depth 15 --height 5 --output sala.csm
    python cadsfs_gen__6_.py --width 12 --depth 20 --height 8 --floor "Alfombra" --ceiling "Yeso pintado" --walls "Hormigón" --output teatro.csm
"""
import numpy as np
import zlib
import base64
import json
import argparse
import math


# ══════════════════════════════════════════════════════════════
# CONSTANTES
# ══════════════════════════════════════════════════════════════

BANDS = [63,80,100,125,160,200,250,315,400,500,630,800,
         1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500]
# 24 bandas de 1/3 de octava (63 Hz – 12.5 kHz), idénticas a BANDS_HZ de CADSFS.
# (Antes el generador tenía 27 con 31/40/50 Hz, que CADSFS no usa.)


# ══════════════════════════════════════════════════════════════
# STUDIO MONITOR LIBRARY — 30 modelos, 10 marcas
# ══════════════════════════════════════════════════════════════
# Convención: brand_model (lowercase, underscores)
# Todas son type="point", default_polar="Model"
# Datos de: genelec.com, neumann.com, adam-audio.com, krkmusic.com,
#           focal.com, atcloudspeakers.co.uk, dynaudio.com, amphion.fi,
#           usa.yamaha.com, ikmultimedia.com, sweetwater.com, thomann.de

STUDIO_MONITORS = {
    # GENELEC (4)
    "genelec_8010a":  {"name": "Genelec 8010A",    "max_spl": 96,   "dims": [0.121,0.116,0.195], "wt": 1.5,  "bw_h": 100, "bw_v": 100, "f_lo": 67,    "f_hi": 25000},
    "genelec_8020d":  {"name": "Genelec 8020D",    "max_spl": 100,  "dims": [0.148,0.142,0.242], "wt": 3.2,  "bw_h": 100, "bw_v": 100, "f_lo": 56,    "f_hi": 25000},
    "genelec_8030c":  {"name": "Genelec 8030C",    "max_spl": 104,  "dims": [0.189,0.178,0.299], "wt": 5.6,  "bw_h": 100, "bw_v": 100, "f_lo": 47,    "f_hi": 25000},
    "genelec_8040b":  {"name": "Genelec 8040B",    "max_spl": 105,  "dims": [0.237,0.223,0.350], "wt": 6.7,  "bw_h": 100, "bw_v": 100, "f_lo": 45,    "f_hi": 21000},
    # NEUMANN (3)
    "neumann_kh80_dsp":  {"name": "Neumann KH 80 DSP",  "max_spl": 108.8, "dims": [0.148,0.172,0.232], "wt": 3.4, "bw_h": 120, "bw_v": 120, "f_lo": 57, "f_hi": 21000},
    "neumann_kh120_ii":  {"name": "Neumann KH 120 II",  "max_spl": 116.8, "dims": [0.182,0.227,0.287], "wt": 6.2, "bw_h": 110, "bw_v": 110, "f_lo": 44, "f_hi": 21000},
    "neumann_kh150":     {"name": "Neumann KH 150",     "max_spl": 118.7, "dims": [0.225,0.273,0.345], "wt": 9.0, "bw_h": 110, "bw_v": 110, "f_lo": 38, "f_hi": 21000},
    # ADAM AUDIO (4)
    "adam_t7v":   {"name": "ADAM Audio T7V",   "max_spl": 110,  "dims": [0.210,0.297,0.337], "wt": 5.6,  "bw_h": 100, "bw_v": 100, "f_lo": 39, "f_hi": 25000},
    "adam_a4v":   {"name": "ADAM Audio A4V",   "max_spl": 106,  "dims": [0.160,0.188,0.267], "wt": 3.5,  "bw_h": 100, "bw_v": 100, "f_lo": 52, "f_hi": 42000},
    "adam_a7v":   {"name": "ADAM Audio A7V",   "max_spl": 111,  "dims": [0.201,0.280,0.337], "wt": 8.0,  "bw_h": 100, "bw_v": 100, "f_lo": 41, "f_hi": 42000},
    "adam_a77x":  {"name": "ADAM Audio A77X",  "max_spl": 121,  "dims": [0.201,0.340,0.406], "wt": 9.6,  "bw_h": 100, "bw_v": 100, "f_lo": 38, "f_hi": 50000},
    # KRK (3)
    "krk_rokit5_g4": {"name": "KRK Rokit 5 G4", "max_spl": 104, "dims": [0.190,0.229,0.286], "wt": 4.3, "bw_h": 100, "bw_v": 100, "f_lo": 43, "f_hi": 40000},
    "krk_rokit7_g4": {"name": "KRK Rokit 7 G4", "max_spl": 107, "dims": [0.232,0.267,0.331], "wt": 5.9, "bw_h": 100, "bw_v": 100, "f_lo": 36, "f_hi": 40000},
    "krk_rokit8_g4": {"name": "KRK Rokit 8 G4", "max_spl": 109, "dims": [0.268,0.328,0.392], "wt": 7.9, "bw_h": 100, "bw_v": 100, "f_lo": 33, "f_hi": 40000},
    # FOCAL (3)
    "focal_alpha50_evo": {"name": "Focal Alpha 50 Evo", "max_spl": 104, "dims": [0.168,0.222,0.285], "wt": 5.5, "bw_h": 90, "bw_v": 90, "f_lo": 45, "f_hi": 22000},
    "focal_alpha65_evo": {"name": "Focal Alpha 65 Evo", "max_spl": 106, "dims": [0.200,0.262,0.335], "wt": 7.4, "bw_h": 90, "bw_v": 90, "f_lo": 40, "f_hi": 22000},
    "focal_shape65":     {"name": "Focal Shape 65",     "max_spl": 109, "dims": [0.204,0.297,0.332], "wt": 8.6, "bw_h": 100, "bw_v": 100, "f_lo": 40, "f_hi": 35000},
    # ATC (2)
    "atc_scm25a_pro": {"name": "ATC SCM25A Pro", "max_spl": 108, "dims": [0.266,0.325,0.442], "wt": 17.0, "bw_h": 80, "bw_v": 80, "f_lo": 47, "f_hi": 22000},
    "atc_scm45a_pro": {"name": "ATC SCM45A Pro", "max_spl": 112, "dims": [0.360,0.385,0.620], "wt": 35.0, "bw_h": 80, "bw_v": 80, "f_lo": 42, "f_hi": 20000},
    # DYNAUDIO (3)
    "dynaudio_lyd5":      {"name": "Dynaudio LYD 5",     "max_spl": 107, "dims": [0.170,0.205,0.267], "wt": 5.6,  "bw_h": 120, "bw_v": 120, "f_lo": 45, "f_hi": 21000},
    "dynaudio_lyd48":     {"name": "Dynaudio LYD 48",    "max_spl": 116, "dims": [0.235,0.300,0.398], "wt": 10.5, "bw_h": 120, "bw_v": 120, "f_lo": 37, "f_hi": 21000},
    "dynaudio_bm5_mkiii": {"name": "Dynaudio BM5 mkIII", "max_spl": 118, "dims": [0.216,0.300,0.345], "wt": 8.0,  "bw_h": 120, "bw_v": 120, "f_lo": 42, "f_hi": 24000},
    # AMPHION (2)
    "amphion_one18": {"name": "Amphion One18", "max_spl": 110, "dims": [0.236,0.290,0.373], "wt": 10.5, "bw_h": 100, "bw_v": 100, "f_lo": 38, "f_hi": 20000},
    "amphion_two18": {"name": "Amphion Two18", "max_spl": 118, "dims": [0.284,0.286,0.440], "wt": 11.5, "bw_h": 100, "bw_v": 100, "f_lo": 28, "f_hi": 20000},
    # YAMAHA HS (3)
    "yamaha_hs5": {"name": "Yamaha HS5", "max_spl": 107, "dims": [0.170,0.222,0.285], "wt": 5.3, "bw_h": 100, "bw_v": 100, "f_lo": 54, "f_hi": 30000},
    "yamaha_hs7": {"name": "Yamaha HS7", "max_spl": 108, "dims": [0.210,0.284,0.332], "wt": 8.2, "bw_h": 100, "bw_v": 100, "f_lo": 43, "f_hi": 30000},
    "yamaha_hs8": {"name": "Yamaha HS8", "max_spl": 110, "dims": [0.250,0.334,0.390], "wt": 10.2,"bw_h": 100, "bw_v": 100, "f_lo": 38, "f_hi": 30000},
    # IK MULTIMEDIA (3)
    "ik_iloud_micro":      {"name": "IK Multimedia iLoud Micro Monitor",       "max_spl": 107, "dims": [0.090,0.135,0.180], "wt": 0.92, "bw_h": 90, "bw_v": 90, "f_lo": 55, "f_hi": 20000},
    "ik_iloud_mtm":        {"name": "IK Multimedia iLoud MTM",         "max_spl": 103, "dims": [0.160,0.195,0.264], "wt": 2.5,  "bw_h": 90, "bw_v": 90, "f_lo": 50, "f_hi": 24000},
    "ik_iloud_precision5": {"name": "IK Multimedia iLoud Precision 5", "max_spl": 109, "dims": [0.188,0.252,0.291], "wt": 5.0,  "bw_h": 90, "bw_v": 90, "f_lo": 33, "f_hi": 24000},
}


# ══════════════════════════════════════════════════════════════
# ASSEMBLY PRESETS
# ══════════════════════════════════════════════════════════════

ASSEMBLY_PRESETS = {
    "asm_pared_estudio": {"layers": [
        {"material_id": "gyp_125", "thickness_mm": 12.5, "bonded_with_prev": True},
        {"material_id": "air_50",  "thickness_mm": 50,   "bonded_with_prev": False},
        {"material_id": "mineral_wool_80", "thickness_mm": 80, "bonded_with_prev": False},
        {"material_id": "gyp_125", "thickness_mm": 12.5, "bonded_with_prev": True}]},
    "asm_piso_flotante": {"layers": [
        {"material_id": "concrete_200", "thickness_mm": 200, "bonded_with_prev": True},
        {"material_id": "neoprene_25",  "thickness_mm": 25,  "bonded_with_prev": False},
        {"material_id": "concrete_100", "thickness_mm": 100, "bonded_with_prev": True}]},
    "asm_techo_desacoplado": {"layers": [
        {"material_id": "gyp_125",         "thickness_mm": 12.5, "bonded_with_prev": True},
        {"material_id": "air_200",         "thickness_mm": 200,  "bonded_with_prev": False},
        {"material_id": "mineral_wool_100","thickness_mm": 100,  "bonded_with_prev": False},
        {"material_id": "concrete_150",    "thickness_mm": 150,  "bonded_with_prev": True}]},
    "asm_pared_hormigon": {"layers": [
        {"material_id": "plaster_20",  "thickness_mm": 20,  "bonded_with_prev": True},
        {"material_id": "concrete_200","thickness_mm": 200, "bonded_with_prev": True},
        {"material_id": "plaster_20",  "thickness_mm": 20,  "bonded_with_prev": True}]},
    "asm_pared_ladrillo": {"layers": [
        {"material_id": "plaster_20", "thickness_mm": 20,  "bonded_with_prev": True},
        {"material_id": "brick_230",  "thickness_mm": 230, "bonded_with_prev": True},
        {"material_id": "plaster_20", "thickness_mm": 20,  "bonded_with_prev": True}]},
    "asm_piso_hormigon": {"layers": [
        {"material_id": "concrete_300", "thickness_mm": 300, "bonded_with_prev": True}]},
    "asm_techo_hormigon": {"layers": [
        {"material_id": "plaster_25",  "thickness_mm": 25,  "bonded_with_prev": True},
        {"material_id": "air_300",     "thickness_mm": 300, "bonded_with_prev": False},
        {"material_id": "concrete_200","thickness_mm": 200, "bonded_with_prev": True}]},
    "asm_ventana_doble": {"layers": [
        {"material_id": "glass_6",  "thickness_mm": 6,   "bonded_with_prev": True},
        {"material_id": "air_100", "thickness_mm": 100, "bonded_with_prev": False},
        {"material_id": "glass_10","thickness_mm": 10,  "bonded_with_prev": True}]},
    "asm_puerta_doble": {"layers": [
        {"material_id": "wood_45", "thickness_mm": 45, "bonded_with_prev": True},
        {"material_id": "air_50",  "thickness_mm": 50, "bonded_with_prev": False},
        {"material_id": "wood_45", "thickness_mm": 45, "bonded_with_prev": True}]},
}


# ══════════════════════════════════════════════════════════════
# ENCODING
# ══════════════════════════════════════════════════════════════

def encode_float_array(arr, dtype=np.float32):
    a = np.asarray(arr, dtype=dtype)
    return base64.b64encode(zlib.compress(a.tobytes(order="C"), level=9)).decode("ascii")

def encode_int_array(arr):
    a = np.asarray(arr, dtype=np.int32)
    return base64.b64encode(zlib.compress(a.tobytes(order="C"), level=9)).decode("ascii")


# ══════════════════════════════════════════════════════════════
# GEOMETRÍA — CENTRADA EN (0,0)
# ══════════════════════════════════════════════════════════════

def create_box_centered(depth, width, height):
    """Box centrado en (0,0,0) base en Z=0. Retorna (V, F, group_order, ftg).
    depth=X, width=Y, height=Z. Convención CADSFS."""
    hd, hw = depth/2, width/2
    V = np.array([
        [-hd,-hw,0],[ hd,-hw,0],[ hd, hw,0],[-hd, hw,0],
        [-hd,-hw,height],[ hd,-hw,height],[ hd, hw,height],[-hd, hw,height]
    ], dtype=np.float64)
    F = np.array([
        [0,2,1],[0,3,2],       # Floor
        [4,5,6],[4,6,7],       # Ceiling
        [1,2,6],[1,6,5],       # Wall +X
        [0,7,3],[0,4,7],       # Wall -X
        [2,3,7],[2,7,6],       # Wall +Y
        [0,1,5],[0,5,4],       # Wall -Y
    ], dtype=np.int32)
    group_order = ["Floor","Ceiling","Wall +X","Wall -X","Wall +Y","Wall -Y"]
    ftg = np.array([0,0,1,1,2,2,3,3,4,4,5,5], dtype=np.int32)
    return V, F, group_order, ftg

def create_extrusion_centered(polygon_xy, height):
    """Extruye polígono centrado en (0,0). Retorna (V, F, group_order, ftg).
    Walls named Wall 1..N (1-indexed, matches create_extrude_mesh convention)."""
    N = len(polygon_xy)
    V_bottom = np.array([[p[0], p[1], 0.0] for p in polygon_xy], dtype=np.float64)
    V_top = np.array([[p[0], p[1], height] for p in polygon_xy], dtype=np.float64)
    V = np.vstack([V_bottom, V_top])
    faces = []
    groups = {}
    # Floor (fan triangulation, inverted winding for -Z normal)
    fs = len(faces)
    for i in range(N - 2):
        faces.append([0, i+2, i+1])  # reversed for inward normal
    groups["Floor"] = list(range(fs, len(faces)))
    # Ceiling (fan triangulation, normal winding)
    fs = len(faces)
    for i in range(N - 2):
        faces.append([N, N+i+1, N+i+2])
    groups["Ceiling"] = list(range(fs, len(faces)))
    # Walls (1-indexed)
    for i in range(N):
        j = (i + 1) % N
        fs = len(faces)
        faces.append([i, j, j+N])
        faces.append([i, j+N, i+N])
        groups[f"Wall {i+1}"] = [fs, fs+1]
    F = np.array(faces, dtype=np.int32)
    group_order = list(groups.keys())
    ftg = np.zeros(len(faces), dtype=np.int32)
    for gi, gname in enumerate(group_order):
        for fi in groups[gname]:
            ftg[fi] = gi
    return V, F, group_order, ftg


# ══════════════════════════════════════════════════════════════
# GENERADOR PRINCIPAL
# ══════════════════════════════════════════════════════════════

def generate_project(width, depth, height, materials_config=None,
                     materials_b_config=None, assembly_config=None,
                     source_pos=None, receiver_pos=None,
                     speakers=None, polygon_xy=None,
                     audience_areas=None, project_name="",
                     surround_mode=False, surround_format="2.0"):
    """Genera un proyecto CADSFS completo.

    Args:
        width: ancho (Y) en metros
        depth: profundidad (X) en metros
        height: altura (Z) en metros
        materials_config: dict {group_name: material_name} para cara A
        materials_b_config: dict {group_name: material_name} para cara B
        assembly_config: dict {group_name: assembly_id}
        polygon_xy: lista de [x,y] para extrusión (centrada en 0,0)
        speakers: lista de speaker_systems
        audience_areas: lista de audience zones
        project_name: nombre del proyecto
        surround_mode: True para surround
        surround_format: "2.0", "5.1", "7.1", etc.
    """
    # Geometría
    if polygon_xy:
        V, F, group_order, ftg = create_extrusion_centered(polygon_xy, height)
        source_obj = {
            "kind": "extrude",
            "polygon_xy": [[float(p[0]),float(p[1])] for p in polygon_xy],
            "height": float(height),
            "size_xyz": None, "mesh_file": None, "mesh_scale": 1.0
        }
    else:
        V, F, group_order, ftg = create_box_centered(float(depth), float(width), float(height))
        source_obj = {
            "kind": "box",
            "size_xyz": [float(depth), float(width), float(height)],
            "polygon_xy": None, "height": None,
            "mesh_file": None, "mesh_scale": 1.0
        }

    # Materiales por defecto (nombres REALES de la DB interna)
    mat_map = {}
    for g in group_order:
        if g == "Floor":
            mat_map[g] = "Alfombra"
        elif g == "Ceiling":
            mat_map[g] = "Yeso pintado"
        else:
            mat_map[g] = "Hormigón"
    if materials_config:
        mat_map.update(materials_config)

    # Materiales cara B
    mat_b_map = {}
    for g in group_order:
        if g == "Floor" or g == "Ceiling":
            mat_b_map[g] = "Hormigón"
        elif g.startswith("Wall"):
            mat_b_map[g] = "Ladrillo"
    if materials_b_config:
        mat_b_map.update(materials_b_config)

    # Assemblies
    asm_map = {}
    used_assemblies = {}
    for g in group_order:
        if g == "Floor":
            asm_map[g] = "asm_piso_hormigon"
        elif g == "Ceiling":
            asm_map[g] = "asm_techo_hormigon"
        elif g.startswith("Wall"):
            asm_map[g] = "asm_pared_hormigon"
    if assembly_config:
        asm_map.update(assembly_config)
    # Collect used assemblies
    for asm_id in asm_map.values():
        if asm_id in ASSEMBLY_PRESETS:
            used_assemblies[asm_id] = ASSEMBLY_PRESETS[asm_id]

    # Posiciones auto (centradas)
    if source_pos is None:
        source_pos = [-depth * 0.35, 0.0, 1.5]
    if receiver_pos is None:
        receiver_pos = [depth * 0.15, 0.0, 1.2]

    # Asegurar Unassigned y Default en group_order
    if "Unassigned" not in group_order:
        group_order.append("Unassigned")
    if "Default" not in group_order:
        group_order.append("Default")

    obj = {
        "obj_id": 1, "name": "Recinto", "parent_id": None,
        "is_enclosure": True, "two_sided": False, "side_a_exterior": False,
        "source": source_obj,
        "base_vertices_world": {"data": encode_float_array(V, np.float32), "shape": list(V.shape)},
        "faces_local": {"data": encode_int_array(F), "shape": list(F.shape)},
        "group_order": group_order,
        "face_to_group_idx": {"data": encode_int_array(ftg), "length": int(ftg.size)},
        "group_material": {g: mat_map.get(g, "Default") for g in group_order},
        "pivot_world": [0.0, 0.0, 0.0],
        "rotation_deg": [0.0, 0.0, 0.0],
        "translation_m": [0.0, 0.0, 0.0],
        "scale": [1, 1, 1],
        "color_override": None,
        "visible": True,
    }

    sgm = {f"1|{g}": mat_map.get(g, "Default") for g in group_order}
    sgm_b = {f"1|{g}": mat_b_map[g] for g in group_order if g in mat_b_map}
    sam = {f"1|{g}": asm_map[g] for g in group_order if g in asm_map}

    return {
        "app": "CADSFS", "version": "1.49.84", "bands_hz": list(BANDS),
        "c_m_s": 343.0,
        "materials": [],  # NUNCA incluir materiales custom
        "selected_material_name": "Default",
        "objects": [obj],
        "surface_group_material": sgm,
        "surface_group_material_b": sgm_b,
        "surface_assembly_map": sam,
        "surface_thickness_dir": {f"1|{g}": "inward" for g in group_order if g in asm_map},
        "wall_assemblies": used_assemblies,
        "source_pos": [float(x) for x in source_pos],
        "receiver_pos": [float(x) for x in receiver_pos],
        "source_spl_db": 94.0, "source_polar_pattern": "Omni",
        "receiver_radius_m": 0.10,
        "speaker_systems": speakers or [],
        "active_enclosure_id": 1,
        "outdoor_mode": False,
        "surround_mode": surround_mode,
        "surround_format": surround_format,
        "project_name": project_name,
        "project_designer": "",
        "project_venue_type": "",
        "audience_areas": audience_areas or [],
        "audience_areas_enabled": True,
        "ground_conditions": {"type": "rigid", "flow_resistivity": 20000},
        "show_wall_sections": True,
    }


# ══════════════════════════════════════════════════════════════
# HELPERS PARA PARLANTES
# ══════════════════════════════════════════════════════════════

def make_speaker_element(name, pos, model_id=None, channel=None,
                         yaw_deg=0.0, pitch_deg=0.0):
    """Crea un elemento de parlante.

    Si model_id está en STUDIO_MONITORS, auto-completa dims y max_spl.
    Si model_id es None, usa "point_90" como fallback.
    """
    if model_id and model_id in STUDIO_MONITORS:
        info = STUDIO_MONITORS[model_id]
        dims = info["dims"]
        wt = info["wt"]
    else:
        dims = [0.35, 0.35, 0.55]
        wt = 15.0
    if model_id is None:
        model_id = "point_90"

    el = {
        "name": str(name),
        "model_id": str(model_id),
        "pos": [float(pos[0]), float(pos[1]), float(pos[2])],
        "yaw_deg": float(yaw_deg),
        "pitch_deg": float(pitch_deg),
        "enabled": True,
    }
    if channel is not None:
        el["channel"] = str(channel)
    return el


def aim_at(spk_pos, target_pos):
    """Calcula yaw y pitch para apuntar desde spk_pos hacia target_pos.
    Returns (yaw_deg, pitch_deg)."""
    dx = target_pos[0] - spk_pos[0]
    dy = target_pos[1] - spk_pos[1]
    dz = target_pos[2] - spk_pos[2]
    yaw = math.degrees(math.atan2(dy, dx))
    horiz = math.sqrt(dx*dx + dy*dy)
    pitch = -math.degrees(math.atan2(-dz, horiz))
    return round(yaw, 1), round(pitch, 1)


def make_speaker_system(name, elements, mount="surround", surround_format=None):
    """Crea un sistema de parlantes."""
    sys = {
        "name": str(name),
        "enabled": True,
        "mount": mount,
        "elements": elements,
    }
    if surround_format:
        sys["surround_format"] = surround_format
    return sys


def make_audience_zone(name, x_min, y_min, x_max, y_max, z_m=1.2):
    """Crea una zona de audiencia rectangular."""
    return {
        "name": str(name),
        "polygon_xy": [[x_min,y_min],[x_max,y_min],[x_max,y_max],[x_min,y_max]],
        "z_m": float(z_m),
    }


# ══════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CADSFS JSON Generator v6 — CANA SAN MARTIN")
    parser.add_argument("--width", type=float, default=10.0, help="Ancho (Y) en metros")
    parser.add_argument("--depth", type=float, default=15.0, help="Profundidad (X) en metros")
    parser.add_argument("--height", type=float, default=5.0, help="Altura (Z) en metros")
    parser.add_argument("--floor", type=str, default="Alfombra", help="Material del piso")
    parser.add_argument("--ceiling", type=str, default="Yeso pintado", help="Material del techo")
    parser.add_argument("--walls", type=str, default="Hormigón", help="Material de las paredes")
    parser.add_argument("--output", type=str, default="sala.csm", help="Archivo de salida")
    parser.add_argument("--name", type=str, default="", help="Nombre del proyecto")
    args = parser.parse_args()

    mat_cfg = {"Floor": args.floor, "Ceiling": args.ceiling}
    for w in ["Wall +X", "Wall -X", "Wall +Y", "Wall -Y"]:
        mat_cfg[w] = args.walls

    data = generate_project(args.width, args.depth, args.height,
                           materials_config=mat_cfg, project_name=args.name)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    n_verts = data["objects"][0]["base_vertices_world"]["shape"][0]
    n_faces = data["objects"][0]["faces_local"]["shape"][0]
    n_groups = len(data["objects"][0]["group_order"])
    print(f"✓ Proyecto generado: {args.output}")
    print(f"  Sala: {args.depth}×{args.width}×{args.height} m (centrada en 0,0)")
    print(f"  Vértices: {n_verts}, Triángulos: {n_faces}, Superficies: {n_groups}")
    print(f"  Materiales: DB interna (materials: [])")
    print(f"  Fuente: {data['source_pos']}, Receptor: {data['receiver_pos']}")
    print(f"  Monitores disponibles: {len(STUDIO_MONITORS)} modelos")
