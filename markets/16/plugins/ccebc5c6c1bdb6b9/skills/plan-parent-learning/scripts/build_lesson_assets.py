#!/usr/bin/env python3
"""Create initial host-local lesson artifacts; review updates are host-managed. No network, database or learner tracking."""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

NAMES = ('lesson-plan.md', 'activity-sheet.html', 'answer-key.md', 'learning-record.json')

def text(value, maximum=4000):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError('Expected bounded non-empty text')
    return value

def validate(value):
    if not isinstance(value, dict): raise ValueError('Expected lesson object')
    if set(value) != {'lesson_id','revision','title','objective','duration','materials','steps','adaptations','sources','items'}:
        raise ValueError('Unexpected or missing lesson fields; keep learner data outside curriculum artifacts')
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}',text(value['lesson_id'],64)):
        raise ValueError('Use a non-personal lesson slug')
    if type(value['revision']) is not int or not 1 <= value['revision'] <= 10000: raise ValueError('Invalid revision')
    for key in ('title','objective','duration'):text(value[key])
    for key in ('materials','steps','adaptations'):
        if not isinstance(value[key],list) or not 1 <= len(value[key]) <= 20:raise ValueError('Invalid text list')
        for item in value[key]:text(item)
    if not isinstance(value['sources'],list) or len(value['sources']) > 20:raise ValueError('Invalid sources')
    for source in value['sources']:
        if not isinstance(source,dict) or set(source) != {'concept_id','url','note','jurisdiction','source_grade','grade_fit'}:raise ValueError('Invalid source')
        for field in source:text(source[field])
        if source['grade_fit'] not in ('unverified','different_source_grade','source_label_only'):raise ValueError('Use a disclosed, non-equivalence grade-fit status')
        url=urlparse(source['url'])
        if url.scheme != 'https' or not url.hostname or url.username or url.password:raise ValueError('Use verified HTTPS source URLs')
    if not isinstance(value['items'],list) or not 1 <= len(value['items']) <= 20:raise ValueError('Use 1–20 items')
    ids=set()
    for item in value['items']:
        if not isinstance(item,dict) or set(item) != {'id','prompt','answer','rationale','max_points'}:raise ValueError('Invalid item fields')
        if not re.fullmatch(r'[a-z][a-z0-9-]{0,31}',text(item['id'],32)) or item['id'] in ids:raise ValueError('Invalid/duplicate item ID')
        ids.add(item['id'])
        for field in ('prompt','answer','rationale'):text(item[field])
        if type(item['max_points']) is not int or not 1 <= item['max_points'] <= 10:raise ValueError('Invalid rubric points')
    return value

def render(value):
    v=validate(value); esc=html.escape
    caveat='Generated practice for adult review, not a validated assessment. Source jurisdiction and grade labels are not U.S. grade/standards equivalencies or readiness decisions. No mastery is inferred from completion or score.'
    source_lines='\n'.join(f"- {s['concept_id']}: {s['url']} — Jurisdiction: {s['jurisdiction']}; source grade/year: {s['source_grade']}; grade fit: {s['grade_fit']}. {s['note']}" for s in v['sources']) or '- Provenance/jurisdiction/source grade unavailable; grade fit and standards alignment unverified.'
    provenance='<section class="provenance"><h2>Source and assessment limits — for the adult</h2><p>'+esc(caveat)+'</p><pre style="white-space:pre-wrap;overflow-wrap:anywhere;font:inherit">'+esc(source_lines)+'</pre></section>'
    plan=f"# {v['title']}\n\nLesson: {v['lesson_id']} / revision {v['revision']}\n\nObjective: {v['objective']}\n\nDuration: {v['duration']}\n\nGenerated practice for adult review; not a validated assessment.\n"
    for label,key in [('Materials','materials'),('Sequence','steps'),('Variations','adaptations')]:
        plan+='\n## '+label+'\n\n'+'\n'.join('- '+x for x in v[key])+'\n'
    plan+='\n## Source and assessment limits\n\n'+caveat+'\n\n'+source_lines+'\n'
    answer=f"# Adult answer key — {v['title']}\n\nLesson: {v['lesson_id']} / revision {v['revision']}\n\nProvisional practice rubric. Missing or unreadable evidence is not_assessable; no automatic mastery judgment.\n"
    for item in v['items']:
        answer+=f"\n## {item['id']} ({item['max_points']} possible points)\n\n{item['answer']}\n\n{item['rationale']}\n"
    answer+='\n## Source and assessment limits\n\n'+caveat+'\n\n'+source_lines+'\n'
    questions=''.join(f'<section><label for="item-{i["id"]}">{n}. {esc(i["prompt"])}</label><textarea id="item-{i["id"]}" data-item="{i["id"]}" rows="4" maxlength="4000"></textarea></section>' for n,i in enumerate(v['items'],1))
    # Only validated non-personal lesson slug, integer revision and item IDs enter JS.
    metadata=json.dumps({'schema_version':'pathweaver.responses/1','lesson_id':v['lesson_id'],'lesson_revision':v['revision']})
    script='''const meta=META;
document.getElementById('print').addEventListener('click',()=>window.print());
window.addEventListener('beforeprint',()=>document.querySelectorAll('[data-item]').forEach(el=>{el.style.height='auto';el.style.height=Math.max(110,el.scrollHeight)+'px';}));
document.getElementById('download').addEventListener('click',()=>{
 const payload={...meta,answers:Array.from(document.querySelectorAll('[data-item]'),el=>({item_id:el.dataset.item,response:el.value}))};
 const blob=new Blob([JSON.stringify(payload,null,2)+'\\n'],{type:'application/json'});
 const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=meta.lesson_id+'-responses-r'+meta.lesson_revision+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
 document.getElementById('status').textContent='Download requested. Parent: check the saved file before closing.';
});
'''.replace('META',metadata)
    sheet=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'none'; form-action 'none'; base-uri 'none'"><title>{esc(v['title'])}</title><style>body{{max-width:760px;margin:24px auto;padding:20px;font:18px/1.5 system-ui;color:#142331;background:white}}h1{{font-size:30px}}section{{margin:24px 0;break-inside:avoid}}label{{display:block}}textarea{{box-sizing:border-box;width:100%;font:18px/1.5 system-ui;border:1px solid #596a78;margin-top:8px;resize:vertical}}button{{font:inherit;padding:10px;margin:8px}}@media print{{.controls{{display:none}}body{{margin:0;font-size:14pt}}textarea{{min-height:110px}}@page{{margin:18mm}}}}</style></head><body><h1>{esc(v['title'])}</h1><p>Lesson {v['lesson_id']} · revision {v['revision']}</p><p>{esc(v['objective'])}</p><p>Work with your adult helper. No name is needed on this sheet.</p>{questions}{provenance}<div class="controls"><p>Parent-managed offline activity. Nothing is sent to Pathweaver. Answers are not saved automatically: download responses before closing. The parent can return the file to ChatGPT for review.</p><button id="print" type="button">Print / save as PDF</button><button id="download" type="button">Download responses for parent</button><p id="status" role="status"></p></div><script>{script}</script></body></html>'''
    record={'schema_version':'pathweaver.learning-record/1','lesson_id':v['lesson_id'],'lesson_revision':v['revision'],'record_revision':1,'previous_record':None,'status':'planned','assessment_limits':caveat,'source_coverage':'declared-source-labels-only' if v['sources'] else 'unverified','sources':v['sources'],'artifacts':{name:{'filename':name,'lesson_id':v['lesson_id'],'lesson_revision':v['revision'],'account_file_id':None,'save_status':'local-only'} for name in NAMES[:3]},'review':{'status':'not_started','items':[],'parent_confirmation':None},'next_steps':[]}
    return dict(zip(NAMES,[plan,sheet,answer,json.dumps(record,indent=2)+'\n']))

def build(input_path,output):
    if input_path.stat().st_size > 150000:raise ValueError('Lesson input too large')
    files=render(json.loads(input_path.read_text()))
    output.mkdir(parents=True,exist_ok=True)
    if any((output/name).exists() for name in files):raise FileExistsError('Choose a new revision directory; existing artifacts are preserved')
    for name,content in files.items():
        with (output/name).open('x',encoding='utf-8') as handle:handle.write(content)
    return [str(output/name) for name in files]

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',type=Path);parser.add_argument('output',type=Path);args=parser.parse_args()
    print(json.dumps({'artifacts':build(args.input,args.output),'account_saved':False}))
