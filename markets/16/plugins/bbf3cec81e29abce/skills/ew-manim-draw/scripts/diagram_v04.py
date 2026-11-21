"""EW Diagram 0.4: strict data, shared geometry, SVG and offline HTML. No eval/network."""
import argparse, html, json, math, re
from pathlib import Path

def require(ok, message):
    if not ok: raise ValueError(message)
def fields(obj, allowed):
    require(isinstance(obj,dict) and not set(obj)-set(allowed.split()), 'Unknown fields or non-object')
def number(v,lo,hi):
    require(type(v) in (int,float) and math.isfinite(v) and lo<=v<=hi,'Invalid number')
    return v
def label(v):
    require(isinstance(v,str) and 0<len(v)<=600,'Invalid label')
    return v
def ident(v):
    require(isinstance(v,str) and re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{0,63}',v),'Invalid ID')
    return v
def read(path):
    require(Path(path).stat().st_size<=2000000,'Input exceeds 2 MB')
    def pairs(xs):
        d={}
        for k,v in xs:
            require(k not in d,'Duplicate JSON key');d[k]=v
        return d
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs)
def validate(d):
    fields(d,'schema_version title locale graph sources views theme story export')
    require(d.get('schema_version')=='0.4','Expected schema 0.4');label(d['title'])
    require(d.get('locale') in ('en','zh-TW','zh-CN'),'Invalid locale')
    fields(d['graph'],'nodes groups edges')
    g=d['graph']; ns=g['nodes'];gs=g['groups'];es=g['edges']
    require(isinstance(ns,list) and 1<=len(ns)<=40,'1–40 nodes required')
    require(isinstance(gs,list) and 1<=len(gs)<=8,'1–8 flat groups required')
    require(isinstance(es,list) and len(es)<=100,'Too many edges')
    ids=set();reserved={'arrow','caption','progress','project','prev','play','next','reset','speed','motion'}
    for collection in (gs,ns,es):
        for o in collection:
            i=ident(o['id']);require(i not in ids and i not in reserved,'Duplicate or reserved ID');ids.add(i)
    gids={x['id'] for x in gs};nids={x['id'] for x in ns}
    for x in gs:fields(x,'id label');label(x['label'])
    for x in ns:
        fields(x,'id label group x y');label(x['label']);require(x['group'] in gids,'Unknown group')
        require(('x' in x)==('y' in x),'Both coordinates required')
        if 'x' in x:number(x['x'],60,1600);number(x['y'],220,700)
    for x in es:
        fields(x,'id from to kind from_port to_port waypoints')
        require(x['from'] in nids and x['to'] in nids and x['from']!=x['to'],'Unknown endpoint/self edge')
        require(x['kind'] in ('data','feedback','control','reference'),'Invalid edge kind')
        for k in ('from_port','to_port'):require(x.get(k,'right' if k=='from_port' else 'left') in ('left','right','top','bottom'),'Invalid port')
        pts=x.get('waypoints',[]);require(isinstance(pts,list) and len(pts)<=20,'Invalid waypoints')
        for q in pts:
            require(isinstance(q,list) and len(q)==2,'Invalid point');number(q[0],40,1880);number(q[1],180,830)
    require(isinstance(d['sources'],list) and 1<=len(d['sources'])<=200,'Sources required')
    covered=set();source_ids=set()
    for x in d['sources']:
        fields(x,'id text targets status');ident(x['id']);require(x['id'] not in source_ids,'Duplicate source ID');source_ids.add(x['id']);label(x['text'])
        require(x['status'] in ('confirmed','unconfirmed','synthetic'),'Invalid source status')
        require(isinstance(x['targets'],list) and x['targets'] and all(t in ids for t in x['targets']),'Invalid source target');covered.update(x['targets'])
    require(ids<=covered,'Every group/node/edge needs provenance')
    require(d['views']==[{'id':'overview'}],'0.4 renderer supports one overview; split projects for details')
    fields(d['theme'],'mode');require(d['theme']['mode'] in ('dark','light'),'Invalid theme')
    fields(d['story'],'mode steps');s=d['story'];require(s['mode'] in ('guided','loop'),'Invalid story mode')
    require(isinstance(s['steps'],list) and 1<=len(s['steps'])<=60,'1–60 steps required')
    require(s['mode']!='loop' or len(s['steps'])==1,'Loop requires one step')
    total=0;step_ids=set()
    for x in s['steps']:
        fields(x,'id text targets duration');ident(x['id']);require(x['id'] not in step_ids,'Duplicate step ID');step_ids.add(x['id']);label(x['text'])
        require(isinstance(x['targets'],list) and all(t in nids|{e['id'] for e in es} for t in x['targets']),'Invalid step target')
        total+=number(x['duration'],1,60)
    require(total<=600,'Story exceeds 600 seconds')
    fields(d['export'],'width height formats');require((d['export']['width'],d['export']['height'])==(1920,1080),'0.4 supports 1920x1080 only')
    require(isinstance(d['export']['formats'],list) and d['export']['formats'] and all(x in ('json','svg','html','png','gif') for x in d['export']['formats']),'Unsupported export')
    return d

def font(path,size):
    from PIL import ImageFont
    require(path and Path(path).is_file(),'Supply --font with a licensed font supporting the requested language')
    return ImageFont.truetype(path,size)
def wrap(text,f,width,maxlines):
    lines=[];line=''
    for ch in text:
        if ch=='\n' or f.getlength(line+ch)>width:
            if line:lines.append(line)
            line='' if ch=='\n' else ch
        else:line+=ch
    if line:lines.append(line)
    require(len(lines)<=maxlines,'Text does not fit: create overview + detail projects; do not shrink or omit')
    return lines

def layout(d,fontpath):
    from PIL import ImageFont
    f=font(fontpath,30);gf=font(fontpath,28);tf=font(fontpath,48)
    require(tf.getlength(d['title'])<=1740,'Title too long')
    groups=[];nodes=[];edges=[];count=len(d['graph']['groups']);cw=1720/count
    require(cw>=350,'Too many groups for one readable overview; split views')
    for i,g in enumerate(d['graph']['groups']):
        x=100+i*cw;groups.append(dict(g,x=x,y=210,w=cw-32,h=580,lines=wrap(g['label'],gf,cw-80,2)))
        members=[n for n in d['graph']['nodes'] if n['group']==g['id']]
        require(1<=len(members)<=3,'1–3 nodes per group; split detailed views')
        for j,n in enumerate(members):
            nx=n.get('x',x+28);ny=n.get('y',315+j*146);w=cw-88;h=110
            require(nx>=x+20 and nx+w<=x+cw-52 and ny>=290 and ny+h<=770,'Node outside group')
            nodes.append(dict(n,x=nx,y=ny,w=w,h=h,lines=wrap(n['label'],f,w-40,2)))
    def boxhit(a,b):return a['x']<b['x']+b['w'] and a['x']+a['w']>b['x'] and a['y']<b['y']+b['h'] and a['y']+a['h']>b['y']
    for i,a in enumerate(nodes):
        for b in nodes[i+1:]:require(not boxhit(a,b),'Overlapping nodes')
    lookup={n['id']:n for n in nodes}
    def port(n,p):return {'left':[n['x'],n['y']+n['h']/2],'right':[n['x']+n['w'],n['y']+n['h']/2],'top':[n['x']+n['w']/2,n['y']],'bottom':[n['x']+n['w']/2,n['y']+n['h']]}[p]
    for e in d['graph']['edges']:
        a=port(lookup[e['from']],e.get('from_port','right'));b=port(lookup[e['to']],e.get('to_port','left'))
        pts=[a]+e.get('waypoints',[])+[b]
        if not e.get('waypoints') and a[0]!=b[0] and a[1]!=b[1]:
            mid=(a[0]+b[0])/2;pts=[a,[mid,a[1]],[mid,b[1]],b]
        for p,q in zip(pts,pts[1:]):
            require(p!=q and (p[0]==q[0] or p[1]==q[1]),'Route must be nonzero orthogonal segments')
            for n in nodes:
                # Open interiors: connector may touch a card boundary but never traverse its interior.
                hit=(p[0]==q[0] and n['x']<p[0]<n['x']+n['w'] and max(min(p[1],q[1]),n['y'])<min(max(p[1],q[1]),n['y']+n['h'])) or (p[1]==q[1] and n['y']<p[1]<n['y']+n['h'] and max(min(p[0],q[0]),n['x'])<min(max(p[0],q[0]),n['x']+n['w']))
                require(not hit,'Route intersects node '+n['id']+'; provide locked waypoints')
        edges.append(dict(e,points=pts))
    captions=[wrap(s['text'],font(fontpath,28),1670,2) for s in d['story']['steps']]
    return dict(width=1920,height=1080,title=d['title'],groups=groups,nodes=nodes,edges=edges,captions=captions,font_family=ImageFont.truetype(fontpath,30).getname()[0])

THEMES={'dark':{'bg':'#0B1324','group':'#101F35','card':'#172B46','text':'#F3F7FC','muted':'#B8CBE1','line':'#829DBD','accent':'#50D6F0'},'light':{'bg':'#F5F8FC','group':'#E8EFF8','card':'#FFFFFF','text':'#142B46','muted':'#344D6B','line':'#56708E','accent':'#006D85'}}
def svg(d,l):
    c=THEMES[d['theme']['mode']];esc=html.escape
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" role="img" aria-label="{esc(d["title"],quote=True)}"><style>text{{font-family:"{esc(l["font_family"],quote=True)}",sans-serif;fill:{c["text"]}}}.active{{stroke:{c["accent"]}!important;stroke-width:5!important}}.flow{{fill:none;stroke:{c["accent"]};stroke-width:5;stroke-dasharray:18 16;pointer-events:none}}</style><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{c["line"]}"/></marker></defs>',f'<rect width="1920" height="1080" fill="{c["bg"]}"/><text x="100" y="112" font-size="48" font-weight="700">{esc(d["title"])}</text>',f'<text x="100" y="160" font-size="24" style="fill:{c["muted"]}">EW MANIM DRAW · DIAGRAM-AS-CODE</text>']
    for g in l['groups']:
        out.append(f'<rect x="{g["x"]}" y="{g["y"]}" width="{g["w"]}" height="{g["h"]}" rx="20" fill="{c["group"]}" stroke="{c["line"]}" stroke-width="1"/>')
        for i,line in enumerate(g['lines']):out.append(f'<text x="{g["x"]+28}" y="{g["y"]+43+i*32}" font-size="28" font-weight="700">{esc(line)}</text>')
    for e in l['edges']:
        pts=' '.join(f'{x},{y}' for x,y in e['points'])
        out.append(f'<polyline id="{e["id"]}" points="{pts}" fill="none" stroke="{c["line"]}" stroke-width="3" marker-end="url(#arrow)"/><polyline data-flow="{e["id"]}" points="{pts}" class="flow" visibility="hidden"/>')
    for n in l['nodes']:
        out.append(f'<rect id="{n["id"]}" x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="14" fill="{c["card"]}" stroke="{c["line"]}" stroke-width="2"/>')
        for i,line in enumerate(n['lines']):out.append(f'<text x="{n["x"]+n["w"]/2}" y="{n["y"]+n["h"]/2+(i-(len(n["lines"])-1)/2)*36+10}" text-anchor="middle" font-size="30">{esc(line)}</text>')
    out.append(f'<rect x="100" y="860" width="1720" height="142" rx="16" fill="{c["group"]}"/><text id="progress" x="130" y="894" font-size="24" style="fill:{c["muted"]}">1 / {len(l["captions"])}</text><g id="caption">')
    for i,line in enumerate(l['captions'][0]):out.append(f'<text x="130" y="940" dy="{i*34}" font-size="28">{esc(line)}</text>')
    out.append('</g></svg>');return ''.join(out)
def make_html(d,l,s):
    payload=json.dumps({'spec':d,'layout':l},ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    return '<!doctype html><html lang="'+d['locale']+'"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(d['title'])+'</title><style>body{margin:0;background:'+THEMES[d['theme']['mode']]['bg']+';color:'+THEMES[d['theme']['mode']]['text']+';font:16px sans-serif}svg{width:100%;display:block;max-height:88vh}nav{display:flex;gap:12px;justify-content:center;align-items:center;padding:14px}button,select{font:inherit;padding:8px 14px;border-radius:8px}</style>'+s+"""<nav><button id="prev" aria-label="Previous step">◀</button><button id="play">Play / 播放</button><button id="next" aria-label="Next step">▶</button><button id="reset">Replay / 重播</button><select id="speed" aria-label="Speed"><option value="0.5">0.5×</option><option selected value="1">1×</option><option value="2">2×</option></select><label><input id="motion" type="checkbox"> Reduced motion / 靜態</label></nav><script type="application/json" id="project">"""+payload+"""</script><script>
'use strict';const data=JSON.parse(document.getElementById('project').textContent),steps=data.spec.story.steps;
let time=0,playing=false,speed=1,last=null;const motion=document.getElementById('motion');motion.checked=matchMedia('(prefers-reduced-motion: reduce)').matches;
const starts=[];let total=0;for(const s of steps){starts.push(total);total+=s.duration;}
function stateAt(t){t=((t%total)+total)%total;let i=starts.length-1;while(i>0&&t<starts[i])i--;return {index:i,offset:-((t*70)%34)};}
function render(t){const state=stateAt(t),i=state.index,targets=new Set(steps[i].targets);document.querySelectorAll('.active').forEach(x=>x.classList.remove('active'));
for(const id of targets)document.getElementById(id)?.classList.add('active');document.querySelectorAll('[data-flow]').forEach(e=>{e.setAttribute('visibility',targets.has(e.dataset.flow)?'visible':'hidden');e.setAttribute('stroke-dashoffset',motion.checked?0:state.offset);});
document.getElementById('progress').textContent=(i+1)+' / '+steps.length;const caption=document.getElementById('caption');caption.replaceChildren();data.layout.captions[i].forEach((text,j)=>{const n=document.createElementNS('http://www.w3.org/2000/svg','text');n.setAttribute('x',130);n.setAttribute('y',940+j*34);n.setAttribute('font-size',28);n.textContent=text;caption.append(n);});document.getElementById('play').textContent=playing?'Pause / 暫停':'Play / 播放';return state;}
function jump(delta){playing=false;time=starts[(stateAt(time).index+delta+steps.length)%steps.length];render(time);}
document.getElementById('prev').onclick=()=>jump(-1);document.getElementById('next').onclick=()=>jump(1);document.getElementById('play').onclick=()=>{playing=!playing;last=null;render(time);};document.getElementById('reset').onclick=()=>{time=0;playing=false;render(time);};document.getElementById('speed').onchange=e=>speed=Number(e.target.value);motion.onchange=()=>render(time);
addEventListener('keydown',e=>{if(e.target.matches('input,select,button'))return;if(e.key==='ArrowRight')jump(1);if(e.key==='ArrowLeft')jump(-1);if(e.key===' '){e.preventDefault();document.getElementById('play').click();}});
function tick(now){if(playing&&last!==null)time+=(now-last)/1000*speed;last=now;render(time);requestAnimationFrame(tick);}window.EWDiagram={stateAt,renderAt:t=>{playing=false;time=t;return render(t);},data};render(0);requestAnimationFrame(tick);
</script></html>"""
def main():
    ap=argparse.ArgumentParser();ap.add_argument('project');ap.add_argument('--font');ap.add_argument('--validate-only',action='store_true');ap.add_argument('--out',default='output');ap.add_argument('--gif-fps',type=int,default=6);args=ap.parse_args()
    d=validate(read(args.project))
    if args.validate_only:
        out=Path(args.out);out.mkdir(parents=True,exist_ok=True);(out/'diagram.json').write_text(json.dumps(d,ensure_ascii=False,indent=2));print('Validated JSON delivered; rendering not requested');return
    l=layout(d,args.font);s=svg(d,l);out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    for name,obj in [('diagram.json',d),('layout.json',l),('coverage.json',{'sources':d['sources'],'views':d['views'],'manual_source_review_required':True})]: (out/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
    (out/'diagram.svg').write_text(s);(out/'diagram.html').write_text(make_html(d,l,s))
    report={'version':'0.4.1','renderer':'EW SVG shared-layout','limitations':['Flat groups; one 16:9 view; manual route locks required for obstacles','No ELK, nested groups, automated pagination, MP4 or native PPTX integration'], 'formats':{x:{'implemented':x in ('json','svg','html'),'dependency_available':True if x in ('json','svg','html') else None,'produced':x in ('json','svg','html'),'checked':False} for x in ('json','svg','html','png','gif','mp4','pptx')}}
    report['formats']['png']['implemented']=True;report['formats']['png']['dependency_available']=True
    from render_static import render
    render(d,l,args.font,out/'diagram.png')
    report['formats']['png']['produced']=True
    report['png_renderer']='Pillow shared-layout raster export (not Manim)'
    report['html_browser_tested']=False
    report['formats']['gif']['implemented']=True
    report['formats']['gif']['dependency_available']=True
    if 'gif' in d['export']['formats']:
        from render_static import render_gif
        report['gif']=render_gif(d,l,args.font,out/'diagram.gif',args.gif_fps)
        report['formats']['gif']['produced']=True
    (out/'capability-report.json').write_text(json.dumps(report,indent=2));print('Validated and rendered JSON/SVG/HTML; PNG uses Pillow shared layout; HTML browser playback requires separate verification')
if __name__=='__main__':main()
