#!/usr/bin/env python3
"""Ejecución privada de planes explícitos; no navega ni interpreta imágenes."""
from pathlib import Path
import argparse,json,sys
SKILL=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(SKILL/'scripts/runtime'))
from csm_workflow.assets_audit import material_catalog,speaker_catalog,strict_json
from csm_workflow.author_engine import NativeBuilder

def main():
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--plan',type=Path);g.add_argument('--quick-test',action='store_true')
    p.add_argument('--output',type=Path,required=True);p.add_argument('--report',type=Path)
    a=p.parse_args()
    if a.output.suffix.lower()!='.csm':p.error('La salida comprobada usa extensión .csm.')
    try:
        refs=SKILL/'references'
        mats=material_catalog(refs/'biblioteca_materiales_acustica_2665_i18n_translated.xlsx')
        speakers=speaker_catalog(refs/'speaker_library_release_v6_unified_v22_completo.json')
        engine=NativeBuilder(refs/'cadsfs_gen_v6_2.py',mats['names'],speakers['ids'])
        source=refs/'test_plans/Sala_Prueba_4x3x3.plan.json' if a.quick_test else a.plan
        plan=strict_json(source.read_bytes())
        result=engine.build(plan)
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(result.content)
        if a.report:a.report.write_text(json.dumps(result.checks,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps({'ok':True,'file':a.output.name,'bytes':len(result.content),'opened_in_cadsfs':False},ensure_ascii=False))
        return 0
    except Exception:
        print(json.dumps({'ok':False,'message':'No se generó un CSM validado con este plan.'},ensure_ascii=False))
        return 2
if __name__=='__main__':raise SystemExit(main())
