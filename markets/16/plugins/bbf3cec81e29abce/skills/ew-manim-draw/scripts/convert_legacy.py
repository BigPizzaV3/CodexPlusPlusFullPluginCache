"""Explicit conversion to persistent overview; original legacy input stays unchanged."""
import argparse,json
from pathlib import Path
from validate_flow import validate
from diagram import validate as validate_new

def convert(d):
 validate(d)
 if len(d['nodes'])>3:raise ValueError('More than three legacy nodes: compose separate overview/details explicitly')
 nodes=[dict(x,group='legacy') for x in d['nodes']]
 edges=[{'id':e.get('id',f'edge_{i}'),'from':e['from'],'to':e['to'],'kind':'data','from_port':'bottom','to_port':'top'} for i,e in enumerate(d['edges'])]
 # Single-column vertical layout: forward skips require explicit side routes.
 for e in edges:
  a=next(i for i,n in enumerate(nodes) if n['id']==e['from']);b=next(i for i,n in enumerate(nodes) if n['id']==e['to'])
  if b>a+1:
   e['from_port']='right';e['to_port']='right';e['waypoints']=[[1820,370+a*146],[1820,370+b*146]]
 steps=[{'id':f'step{i}','text':f'Legacy target: {e["target"]}','targets':[e['target']],'duration':max(1,e['duration'])} for i,e in enumerate(d['timeline']) if e['kind'] in ('highlight','draw_edge')]
 if not steps:steps=[{'id':'overview','text':d['title'],'targets':[],'duration':4}]
 out={'schema_version':'0.4','title':d['title'],'locale':d.get('locale','zh-TW'),'graph':{'groups':[{'id':'legacy','label':'Legacy conversion'}],'nodes':nodes,'edges':edges},'sources':[{'id':'original','text':'Converted from supplied schema 0.2 graph; persistent overview intentionally replaces reveal sequencing.','targets':['legacy']+[n['id'] for n in nodes]+[e['id'] for e in edges],'status':'confirmed'}],'views':[{'id':'overview'}],'theme':{'mode':'light'},'story':{'mode':'guided','steps':steps},'export':{'width':1920,'height':1080,'formats':['json','svg','html']}}
 return validate_new(out)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');a=ap.parse_args();p=Path(a.output)
 if p.exists():raise SystemExit('Output exists; choose a new path')
 p.write_text(json.dumps(convert(json.loads(Path(a.input).read_text())),ensure_ascii=False,indent=2));print('Converted; original unchanged; reveal semantics intentionally not preserved')
