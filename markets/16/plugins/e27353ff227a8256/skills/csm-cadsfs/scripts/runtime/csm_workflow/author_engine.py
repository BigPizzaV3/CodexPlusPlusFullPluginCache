"""Adaptador local del generador aportado por el propietario.

No usa MCP, red, credenciales ni API. Ejecuta exclusivamente el módulo cuyo SHA256
está fijado abajo, no código enviado por un cliente. Perfil 'cookbook45-tested':
recinto extruido simple (sin huecos), materiales explícitos y sistemas ya resueltos.
La interpretación de texto/imágenes/web y la revisión semántica no están aquí.
"""
from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any
import numpy as np
from .assets_audit import strict_json, decode_array
from .core import ProjectRequest, ValidationReport
from .native_geometry import GeometryError, number, prepare_polygon, extrusion, check_extrusion, point_inside

AUTHOR_SHA256='15e9a1cd288e2d9d411101c65f42cd61ae9bc32c0b1ceb7419341ae8a56bf3fb'
ARGUMENTS={'width','depth','height','materials_config','materials_b_config','assembly_config',
           'source_pos','receiver_pos','speakers','polygon_xy','audience_areas','project_name',
           'surround_mode','surround_format'}


class IntegrationError(ValueError):
    """Diagnóstico de desarrollo; no copiar sus detalles al chat del cliente."""


def stable_bytes(value: Any) -> bytes:
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')


def load_author(path: Path):
    path=Path(path)
    if path.is_symlink() or not path.is_file() or path.stat().st_size>1000000:
        raise IntegrationError('Generador de confianza no disponible.')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=AUTHOR_SHA256:
        raise IntegrationError('El generador no coincide con la versión revisada.')
    # Ejecuta EXACTAMENTE los bytes verificados, sin una segunda lectura TOCTOU.
    spec=importlib.util.spec_from_loader('cadsfs_author_verified',loader=None)
    module=importlib.util.module_from_spec(spec)
    exec(compile(raw,str(path),'exec'),module.__dict__)
    return module


def _vector(raw) -> list[float]:
    if not isinstance(raw,(list,tuple)) or len(raw)!=3:
        raise IntegrationError('Posición tridimensional inválida.')
    return [number(v) for v in raw]


def _inside(point,poly,height):
    return 0<float(point[2])<height and point_inside(list(point[:2]),poly,boundary=False)


def _group_map(raw,groups,*,catalog=None):
    if not isinstance(raw,dict) or set(raw)!=set(groups):
        raise IntegrationError('Se requiere asignación explícita a cada superficie activa.')
    if any(not isinstance(v,str) or not v or v=='Default' for v in raw.values()):
        raise IntegrationError('Material o referencia sin resolver.')
    if catalog is not None and any(v not in catalog for v in raw.values()):
        raise IntegrationError('Nombre sin coincidencia exacta en la biblioteca recibida.')


@dataclass(frozen=True)
class BuildResult:
    content: bytes
    checks: dict[str,Any]
    changes: tuple[str,...]


class NativeBuilder:
    """El propietario configura el generador y los catálogos; el plan es sólo datos.

    Las correcciones de geometría/apuntado son explícitas y versionadas en este
    adaptador. El módulo original nunca se modifica ni se parchea en memoria.
    """
    def __init__(self, generator_path: Path, material_names: set[str], speaker_ids: set[str]):
        self.author=load_author(generator_path)
        self.material_names=frozenset(material_names)
        self.speaker_ids=frozenset(speaker_ids)
        if not self.material_names or not self.speaker_ids:
            raise IntegrationError('Se requieren las dos bibliotecas identificadas.')

    def build(self, plan: dict[str,Any]) -> BuildResult:
        if not isinstance(plan,dict) or set(plan)-{'arguments','speaker_targets'} or 'arguments' not in plan:
            raise IntegrationError('Plan de integración no reconocido.')
        args=deepcopy(plan['arguments'])
        if not isinstance(args,dict) or set(args)-ARGUMENTS or not {'width','depth','height'}<=args.keys():
            raise IntegrationError('Argumentos fuera de la interfaz real del generador.')
        stable_bytes(args)  # No NaN, infinitos ni tipos ejecutables.
        w,d,h=(number(args[k],positive=True) for k in ('width','depth','height'))
        if min(w,d,h)<1e-4:
            raise IntegrationError('Recinto inferior a la resolución admitida.')
        poly=args.get('polygon_xy')
        if poly is None:
            poly=[[-d/2,-w/2],[d/2,-w/2],[d/2,w/2],[-d/2,w/2]]
        poly=prepare_polygon(poly)
        bounds=np.asarray(poly)
        if not (np.allclose(bounds.max(0)-bounds.min(0),[d,w],rtol=1e-8,atol=1e-8) and
                np.allclose(bounds.max(0)+bounds.min(0),[0,0],atol=1e-8)):
            raise IntegrationError('El perímetro debe respetar cotas y centrado; no se cambia automáticamente.')
        args['polygon_xy']=poly
        groups=['Floor','Ceiling']+[f'Wall {i+1}' for i in range(len(poly))]
        _group_map(args.get('materials_config'),groups,catalog=self.material_names)
        _group_map(args.get('materials_b_config'),groups,catalog=self.material_names)
        if 'assembly_config' in args:
            _group_map(args['assembly_config'],groups,catalog=set(self.author.ASSEMBLY_PRESETS))
        source=_vector(args.get('source_pos') if args.get('source_pos') is not None else [-d*.35,0,1.5])
        receiver=_vector(args.get('receiver_pos') if args.get('receiver_pos') is not None else [d*.15,0,1.2])
        if not _inside(source,poly,h) or not _inside(receiver,poly,h) or np.linalg.norm(np.asarray(source)-receiver)<1e-8:
            raise IntegrationError('Fuente/receptor fuera del recinto o coincidentes: indicar posiciones válidas.')
        args['source_pos']=source; args['receiver_pos']=receiver
        if not isinstance(args.get('project_name',''),str) or len(args.get('project_name',''))>120:
            raise IntegrationError('Nombre de proyecto inválido.')
        if 'surround_mode' in args and type(args['surround_mode']) is not bool:
            raise IntegrationError('Modo surround inválido.')
        speakers=args.get('speakers') or []
        if not isinstance(speakers,list) or len(speakers)>128:
            raise IntegrationError('Sistemas de altavoces inválidos.')
        for system in speakers:
            if not isinstance(system,dict) or not isinstance(system.get('elements'),list):
                raise IntegrationError('Sistema sin elementos.')
            for el in system['elements']:
                if not isinstance(el,dict) or el.get('model_id') not in self.speaker_ids:
                    raise IntegrationError('Modelo de altavoz no presente en la biblioteca recibida.')
                el['pos']=_vector(el.get('pos'))
                if not _inside(el['pos'],poly,h):
                    raise IntegrationError('Altavoz fuera del recinto; este perfil sólo admite sistemas interiores.')
                for angle in ('yaw_deg','pitch_deg'):
                    if angle in el: number(el[angle])
        changes=['Recinto rectangular convertido en extrusión sin cambiar cotas.' if len(poly)==4 else
                 'Perímetro preservado; tapas trianguladas sin abanico indiscriminado.',
                 'Metadatos de malla y pivote normalizados; grupo no asignado conservado.',
                 'Mapas de materiales limitados a superficies activas; sin Default físico.']
        targets=plan.get('speaker_targets',[])
        if not isinstance(targets,list) or len(targets)>4096:
            raise IntegrationError('Objetivos de apuntado inválidos.')
        seen=set()
        for target in targets:
            if not isinstance(target,dict) or set(target)!={'system','element','target'}:
                raise IntegrationError('Objetivo de apuntado mal formado.')
            si,ei=target['system'],target['element']
            if type(si) is not int or type(ei) is not int or si<0 or ei<0 or si>=len(speakers) or ei>=len(speakers[si]['elements']) or (si,ei) in seen:
                raise IntegrationError('Índice de apuntado inválido o repetido.')
            seen.add((si,ei)); el=speakers[si]['elements'][ei]; aim=_vector(target['target'])
            if not _inside(aim,poly,h) or np.linalg.norm(np.asarray(aim)-el['pos'])<1e-8:
                raise IntegrationError('Objetivo de apuntado fuera del recinto o coincidente.')
            yaw,pitch_original=self.author.aim_at(el['pos'],aim)
            el['yaw_deg']=yaw; el['pitch_deg']=-pitch_original
        if targets:
            changes.append('Signo de pitch corregido sólo en apuntados calculados desde objetivos explícitos.')
        args['speakers']=speakers
        for zone in args.get('audience_areas') or []:
            if not isinstance(zone,dict): raise IntegrationError('Área de evaluación inválida.')
            zonepoly=prepare_polygon(zone.get('polygon_xy'))
            if not all(point_inside(p,poly) for p in zonepoly) or not 0<=number(zone.get('z_m'))<h:
                raise IntegrationError('Área de evaluación fuera del recinto.')
        project=self.author.generate_project(**args)
        obj=project['objects'][0]
        v,f,ftg=extrusion(poly,h)
        obj['base_vertices_world']={'dtype':'float32','shape':list(v.shape),'data':self.author.encode_float_array(v)}
        obj['faces_local']={'dtype':'int32','shape':list(f.shape),'data':self.author.encode_int_array(f)}
        obj['face_to_group_idx']={'dtype':'int32','length':len(ftg),'data':self.author.encode_int_array(ftg)}
        obj['group_order']=groups+['Unassigned']
        obj['group_material']={**args['materials_config'],'Unassigned':'Default'}
        obj['pivot_world']=[float(np.mean(v[:,0])),float(np.mean(v[:,1])),h/2]
        obj['source'].update({'path':None,'scale_to_m':1.,'centered':True,'plane':None})
        active={f'1|{g}' for g in groups}
        for key in ('surface_group_material','surface_group_material_b','surface_assembly_map','surface_thickness_dir'):
            project[key]={k:value for k,value in project[key].items() if k in active}
        content=stable_bytes(project)
        checks=self.inspect(content,plan)
        if not checks['ok']:
            raise IntegrationError('El resultado no supera la comprobación del perfil.')
        return BuildResult(content,checks,tuple(changes))

    def inspect(self, content: bytes, plan: dict[str,Any]) -> dict[str,Any]:
        """Valida sólo el perfil generado, no CSM arbitrarios ni simulación acústica."""
        try:
            data=strict_json(content); args=plan['arguments']; w,d,h=(float(args[k]) for k in ('width','depth','height'))
            poly=args.get('polygon_xy') or [[-d/2,-w/2],[d/2,-w/2],[d/2,w/2],[-d/2,w/2]]
            if data.get('app')!='CADSFS' or len(data.get('objects',[]))!=1: return {'ok':False}
            obj=data['objects'][0]
            verts,_=decode_array(obj['base_vertices_world'],'float32',3)
            faces,_=decode_array(obj['faces_local'],'int32',3)
            mapping,_=decode_array(obj['face_to_group_idx'],'int32')
            v=np.asarray(verts).reshape(-1,3); f=np.asarray(faces).reshape(-1,3)
            geom=check_extrusion(v,f,np.asarray(mapping),poly,h)
            active=[g for g in obj['group_order'] if g not in ('Unassigned','Default')]
            material_ok=all(data['surface_group_material'].get(f'1|{g}')==args['materials_config'][g] and
                            data['surface_group_material_b'].get(f'1|{g}')==args['materials_b_config'][g] and
                            obj['group_material'].get(g)==args['materials_config'][g] for g in active)
            assemblies_ok=all(data['surface_assembly_map'].get(f'1|{g}') in data['wall_assemblies'] for g in active)
            src=args.get('source_pos') or [-d*.35,0,1.5]; rec=args.get('receiver_pos') or [d*.15,0,1.2]
            positions_ok=data['source_pos']==src and data['receiver_pos']==rec
            systems_expected=deepcopy(args.get('speakers') or [])
            target_errors=[]
            for target in plan.get('speaker_targets',[]):
                si,ei=target['system'],target['element']; el=data['speaker_systems'][si]['elements'][ei]
                delta=np.asarray(target['target'],dtype=float)-np.asarray(el['pos'])
                delta/=np.linalg.norm(delta)
                y,p=np.radians([el.get('yaw_deg',0),el.get('pitch_deg',0)])
                axis=np.asarray([np.cos(p)*np.cos(y),np.cos(p)*np.sin(y),-np.sin(p)])
                target_errors.append(float(np.degrees(np.arccos(np.clip(np.dot(delta,axis),-1,1)))))
                systems_expected[si]['elements'][ei]['yaw_deg']=el['yaw_deg']
                systems_expected[si]['elements'][ei]['pitch_deg']=el['pitch_deg']
            systems_ok=data['speaker_systems']==systems_expected and all(e<.15 for e in target_errors)
            structure=(data['materials']==[] and data['active_enclosure_id']==obj['obj_id'] and obj['is_enclosure'] is True and
                       obj['source']['kind']=='extrude' and obj['source']['polygon_xy']==poly and
                       obj['source']['height']==h and data['bands_hz']==list(self.author.BANDS))
            return {'ok':bool(geom['ok'] and material_ok and assemblies_ok and positions_ok and systems_ok and structure),
                    'geometry':geom,'material_assignments_match':material_ok,'assembly_references_resolve':assemblies_ok,
                    'source_receiver_preserved':positions_ok,'speaker_systems_match':systems_ok,
                    'aim_errors_deg':target_errors,'opened_in_cadsfs':False,'acoustic_simulation_run':False,
                    'validation_scope':'perfil local: malla, cotas, referencias y plan; NO lector CADSFS ni intención libre'}
        except Exception:
            return {'ok':False,'opened_in_cadsfs':False}


class BoundNativeGenerator:
    """Conecta el motor al Workflow existente para un pedido YA interpretado.

    El enlace entre pedido y plan lo revisa el desarrollador/orquestador. Aquí sólo
    se verifican cotas tipadas. Pedidos con otros facts/requirements se rechazan:
    no se marca como resuelto un escenario, mueble u otra instrucción pendiente.
    """
    def __init__(self,builder: NativeBuilder, request: ProjectRequest, plan: dict[str,Any]):
        if request.operation!='create' or request.requirements or any(f.key not in {'room.length','room.width','room.height'} for f in request.facts):
            raise IntegrationError('Este puente inicial exige un pedido geométrico completamente resuelto.')
        expected={'room.length':plan['arguments']['depth'],'room.width':plan['arguments']['width'],'room.height':plan['arguments']['height']}
        if set(f.key for f in request.facts)!=set(expected): raise IntegrationError('Faltan las tres cotas tipadas.')
        if any(f.canonical()[0]!='m' or not math.isclose(f.canonical()[1],expected[f.key],rel_tol=1e-9,abs_tol=1e-9) for f in request.facts):
            raise IntegrationError('El plan no respeta las cotas del pedido.')
        if plan['arguments'].get('project_name','')!=request.title:
            raise IntegrationError('El nombre del plan no coincide con el pedido.')
        self.builder=builder; self.request=request; self.plan=deepcopy(plan)
        self.last_result=None

    def generate(self,request: ProjectRequest,base_project: bytes|None,workdir: Path)->Path:
        if request!=self.request or base_project is not None:
            raise IntegrationError('El pedido cambió o requiere edición no implementada en este puente.')
        self.last_result=self.builder.build(self.plan)
        path=workdir/'project.csm'; path.write_bytes(self.last_result.content)
        return path


class BoundNativeValidator:
    """Comprobación independiente de geometría + igualdad exacta al candidato ligado.

    No certifica ausencia universal de secretos ni entiende requisitos en lenguaje
    natural. content_safe se limita al candidato explícito revisado y a su esquema.
    """
    def __init__(self,generator: BoundNativeGenerator): self.generator=generator

    def validate(self,content:bytes,request:ProjectRequest,base_project:bytes|None)->ValidationReport:
        g=self.generator
        matches=(request==g.request and base_project is None and g.last_result is not None and
                 content==g.last_result.content)
        check=g.builder.inspect(content,g.plan)
        ok=bool(matches and check.get('ok'))
        return ValidationReport(structure=ok,geometry=ok,requirements=ok,content_safe=ok,
                                edit_preserved=None,opened_in_cadsfs=False)
