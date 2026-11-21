"""Standard-library validation for EW Manim Draw animation JSON v0.2."""
import json, math, sys
from pathlib import Path

def validate(data):
    if not isinstance(data, dict) or data.get('schema_version') != '0.2':
        raise ValueError('Expected schema_version 0.2')
    nodes, edges, events = data.get('nodes'), data.get('edges', []), data.get('timeline')
    if not isinstance(nodes,list) or not 1 <= len(nodes) <= 8: raise ValueError('Expected 1–8 nodes')
    if not isinstance(edges,list) or len(edges)>20: raise ValueError('Too many edges')
    if not isinstance(events,list) or not 1<=len(events)<=60: raise ValueError('Expected 1–60 timeline events')
    ids={}
    for i,n in enumerate(nodes):
        if not isinstance(n,dict) or not isinstance(n.get('id'),str) or not isinstance(n.get('label'),str): raise ValueError('Invalid node')
        if not 1<=len(n['id'])<=64 or not 1<=len(n['label'])<=80 or n['id'] in ids: raise ValueError('Duplicate or invalid node')
        ids[n['id']]=i
    edge_ids=set()
    for i,e in enumerate(edges):
        if not isinstance(e,dict) or e.get('from') not in ids or e.get('to') not in ids or ids[e['from']]>=ids[e['to']]: raise ValueError('Invalid edge')
        eid=e.get('id',f'edge_{i}')
        if not isinstance(eid,str) or not eid or eid in edge_ids or eid in ids: raise ValueError('Invalid edge ID')
        edge_ids.add(eid)
    if data.get('locale','zh-TW') not in ('zh-TW','zh-CN','en'): raise ValueError('Invalid locale')
    if data.get('layout',{}).get('direction')!='horizontal': raise ValueError('Only horizontal layout supported')
    out=data.get('output',{})
    w,h,fps=out.get('width'),out.get('height'),out.get('fps')
    if not all(isinstance(x,int) and not isinstance(x,bool) for x in (w,h,fps)): raise ValueError('Invalid output dimensions')
    if not (320<=w<=3840 and 180<=h<=2160 and w*9==h*16 and 1<=fps<=60): raise ValueError('Invalid output constraints')
    formats=out.get('formats')
    if not isinstance(formats,list) or not formats or any(x not in ('json','png','gif','mp4') for x in formats): raise ValueError('Invalid formats')
    total=0
    for ev in events:
        if not isinstance(ev,dict) or ev.get('kind') not in ('appear','draw_edge','highlight','wait'): raise ValueError('Invalid event')
        kind,target,dur=ev['kind'],ev.get('target'),ev.get('duration')
        if isinstance(dur,bool) or not isinstance(dur,(int,float)) or not math.isfinite(dur) or not .05<=dur<=30: raise ValueError('Invalid duration')
        if kind in ('appear','highlight') and target not in ids: raise ValueError('Unknown node target')
        if kind=='draw_edge' and target not in edge_ids: raise ValueError('Unknown edge target')
        if kind=='wait' and target is not None: raise ValueError('Wait cannot have target')
        total+=dur
    if total>180: raise ValueError('Timeline too long')
    return data

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python validate_flow.py flow.json')
    validate(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')))
    print('VALID: EW Manim Draw animation JSON v0.2')
