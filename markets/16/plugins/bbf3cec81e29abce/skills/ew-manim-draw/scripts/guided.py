"""EW Guided Diagram 0.5: deterministic shared layout + timeline, no network/eval."""
import argparse,base64,heapq,html,json,math,re,sys
from pathlib import Path
from functools import lru_cache
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=1920,1080
COLORS=['#ff915f','#42f3bd','#b18aff','#42cfff','#ffce63','#ff6bba']
BG='#060b16';CARD='#0c1524';TEXT='#eef1f8';MUTED='#a4afc4'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def fields(o,s):require(isinstance(o,dict) and not set(o)-set(s.split()),'Unknown fields: '+str(set(o)-set(s.split()) if isinstance(o,dict) else o))
def ident(s):require(isinstance(s,str) and re.fullmatch('[A-Za-z][A-Za-z0-9_-]{0,63}',s),'Invalid ID')
def label(s):require(isinstance(s,str) and 0<len(s)<=600,'Invalid label')
def number(v,lo,hi):require(type(v) in (int,float) and math.isfinite(v) and lo<=v<=hi,'Invalid finite number')
def box(b):
 require(isinstance(b,list) and len(b)==4,'Expected [x,y,width,height]')
 for v in b:number(v,0,1920)
 require(b[2]>=80 and b[3]>=50 and b[0]>=60 and b[1]>=205 and b[0]+b[2]<=1860 and b[1]+b[3]<=925,'Bounds outside diagram area')
def point(p):
 require(isinstance(p,list) and len(p)==2,'Expected point')
 number(p[0],40,1880);number(p[1],205,925)
def validate(d):
 fields(d,'schema_version title subtitle locale graph sources theme story export');require(d['schema_version']=='0.5','Expected schema 0.5');label(d['title']);label(d.get('subtitle','Guided architecture'))
 require(d['locale'] in ['en','zh-TW','zh-CN'],'Invalid locale')
 fields(d['graph'],'groups nodes edges');g=d['graph'];require(1<=len(g['nodes'])<=40 and len(g['groups'])<=12 and len(g['edges'])<=100,'Graph exceeds limits')
 ids=set();gids={x['id'] for x in g['groups']};nids={x['id'] for x in g['nodes']};lookup={x['id']:x for x in g['groups']}
 for typ,items in [('group',g['groups']),('node',g['nodes']),('edge',g['edges'])]:
  for x in items:
   ident(x['id']);require(x['id'] not in ids,'Duplicate ID');ids.add(x['id'])
   if typ=='group':
    fields(x,'id label parent bounds columns color');label(x['label']);require(x.get('parent') in gids|{None},'Unknown parent');number(x.get('columns',3),1,4);require(type(x.get('columns',3)) is int,'Columns must be integer')
    cur=x;seen=set()
    while cur.get('parent'):
     require(cur['id'] not in seen,'Group hierarchy cycle');seen.add(cur['id']);cur=lookup[cur['parent']]
   elif typ=='node':
    fields(x,'id label subtitle badge group bounds shape color');label(x['label']);require(x.get('group') in gids|{None},'Unknown group');require(x.get('shape','card') in ['card','diamond'],'Invalid shape')
    for k in ['subtitle','badge']:
     if k in x:label(x[k])
   else:
    fields(x,'id from to from_port to_port points direction label color kind');require(x['from'] in gids|nids,'Unknown edge origin');require(x.get('to') in gids|nids|{None},'Unknown edge target');require(x.get('to')!=x['from'],'Self edge')
    require(x.get('direction','forward') in ['forward','both'],'Invalid direction');require(x.get('kind','data') in ['data','feedback','reference','control'],'Invalid kind')
    for k in ['from_port','to_port']:require(x.get(k,'right' if k=='from_port' else 'left') in ['left','right','top','bottom'],'Invalid port')
    if 'label' in x:label(x['label'])
    if x.get('to') is None:require('points' in x and len(x['points'])>=2,'Open branch needs explicit points, no invented node')
    if 'points' in x:
     require(isinstance(x['points'],list) and 2<=len(x['points'])<=30,'Invalid route')
     for p in x['points']:point(p)
   if 'bounds' in x:box(x['bounds'])
   if 'color' in x:require(bool(re.fullmatch('#[0-9a-fA-F]{6}',x['color'])),'Invalid color')
 covered=set();sids=set()
 require(isinstance(d['sources'],list) and 1<=len(d['sources'])<=200,'Sources required')
 for s in d['sources']:
  fields(s,'id text targets status');ident(s['id']);require(s['id'] not in sids,'Duplicate source ID');sids.add(s['id']);label(s['text']);require(s['status'] in ['confirmed','synthetic'],'Unconfirmed graph facts cannot render as approved');require(isinstance(s['targets'],list) and s['targets'] and all(x in ids for x in s['targets']),'Invalid source targets');covered.update(s['targets'])
 require(ids<=covered,'Missing graph provenance')
 fields(d.get('theme',{}),'preset');require(d.get('theme',{}).get('preset','reference-dark') in ['reference-dark'],'Unsupported preset')
 fields(d['story'],'mode steps trail');require(d['story'].get('mode','guided') in ['guided','loop'],'Invalid story mode');require(type(d['story'].get('trail',True)) is bool,'Invalid trail')
 steps=d['story']['steps'];require(isinstance(steps,list) and 1<=len(steps)<=30,'Invalid story steps');require(d['story'].get('mode','guided')!='loop' or len(steps)==1,'Loop needs one step');total=0;stepids=set()
 for s in steps:
  fields(s,'id text targets duration');ident(s['id']);require(s['id'] not in stepids,'Duplicate step ID');stepids.add(s['id']);label(s['text']);require(isinstance(s['targets'],list) and all(t in ids for t in s['targets']),'Invalid step target');number(s.get('duration',3),1,30);total+=s.get('duration',3)
 require(total<=90,'Story exceeds 90 seconds; split, never truncate')
 fields(d.get('export',{}),'width height formats fps');ex=d.get('export',{});require(ex.get('width',W)==W and ex.get('height',H)==H,'Only 1920x1080 supported');require(isinstance(ex.get('formats',[]),list) and bool(ex.get('formats',['json','png','svg','html','gif'])) and all(x in ['json','png','svg','html','gif'] for x in ex.get('formats',['json','png','svg','html','gif'])),'Invalid export format');require(type(ex.get('fps',10)) is int and 1<=ex.get('fps',10)<=12,'fps must be 1–12');require(math.ceil(total*ex.get('fps',10))<=720,'Too many frames; lower fps or split')
 return d
@lru_cache(maxsize=20)
def font(path,size):return ImageFont.truetype(path,size)
def resolve_font(path,locale):
 if path:require(Path(path).is_file(),'Font file missing');return str(Path(path).resolve())
 paths=['/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc','/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc','/Library/Fonts/Arial Unicode.ttf']
 if locale=='en':paths.append('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
 for p in paths:
  if Path(p).is_file():return p
 raise ValueError('No suitable font found. Supply --font with licensed Noto Sans CJK TC/SC (do not package font bytes).')
def wrap(t,f,width,maxlines=3):
 lines=[]
 for para in t.split('\n'):
  cur=''
  tokens=re.findall(r'[A-Za-z0-9_]+(?:[./-][A-Za-z0-9_]+)*|[^\s]|\s+',para)
  for token in tokens:
   require(f.getlength(token.strip())<=width,'Word cannot fit: enlarge card')
   if f.getlength(cur+token)>width:
    if cur.strip():lines.append(cur.rstrip())
    cur=token.lstrip()
   else:cur+=token
  lines.append(cur.rstrip())
 require(len(lines)<=maxlines,'Text overflow: enlarge card or split detail view, never shorten facts')
 return lines
def inside(b,c,pad=0):return b[0]>=c[0]+pad and b[1]>=c[1]+pad and b[0]+b[2]<=c[0]+c[2]-pad and b[1]+b[3]<=c[1]+c[3]-pad
def overlap(a,b):return a[0]<b[0]+b[2] and a[0]+a[2]>b[0] and a[1]<b[1]+b[3] and a[1]+a[3]>b[1]
def port(b,p):
 x,y,w,h=b;return {'left':[x,y+h/2],'right':[x+w,y+h/2],'top':[x+w/2,y],'bottom':[x+w/2,y+h]}[p]
def hit(a,b,rect):
 x,y,w,h=rect
 return (a[0]==b[0] and x<a[0]<x+w and max(min(a[1],b[1]),y)<min(max(a[1],b[1]),y+h)) or (a[1]==b[1] and y<a[1]<y+h and max(min(a[0],b[0]),x)<min(max(a[0],b[0]),x+w))
def auto_route(a,b,obstacles):
 # Visibility grid from ports and obstacle margins. Dijkstra minimizes length + bends.
 xs=sorted({a[0],b[0],60,1860}|{v for r in obstacles for v in (r[0]-20,r[0]+r[2]+20) if 40<=v<=1880});ys=sorted({a[1],b[1],220,920}|{v for r in obstacles for v in (r[1]-20,r[1]+r[3]+20) if 205<=v<=925})
 points={(x,y) for x in xs for y in ys if not any(r[0]<x<r[0]+r[2] and r[1]<y<r[1]+r[3] for r in obstacles)};a=tuple(a);b=tuple(b);require(a in points and b in points,'Port inside another card')
 rows={};cols={}
 for p in points:rows.setdefault(p[1],[]).append(p);cols.setdefault(p[0],[]).append(p)
 adj={p:[] for p in points}
 for lines in [rows,cols]:
  for line in lines.values():
   line.sort()
   for u,v in zip(line,line[1:]):
    if not any(hit(u,v,r) for r in obstacles):adj[u].append(v);adj[v].append(u)
 q=[(0,a,'',[])];best={}
 while q:
  cost,u,axis,path=heapq.heappop(q)
  if (u,axis) in best:continue
  best[u,axis]=cost
  if u==b:
   route=path+[u];out=[]
   for v in route:
    while len(out)>=2 and (out[-2][0]==out[-1][0]==v[0] or out[-2][1]==out[-1][1]==v[1]):out.pop()
    out.append(v)
   return [list(p) for p in out]
  for v in adj[u]:
   ax='x' if u[1]==v[1] else 'y';heapq.heappush(q,(cost+math.dist(u,v)+(35 if axis and ax!=axis else 0),v,ax,path+[u]))
 raise ValueError('No obstacle-free route; provide explicit ports/points or split view')
def layout(d,fp):
 f=font(fp,30);missing_mask=f.getmask('\U0010ffff');missing_key=(missing_mask.size,bytes(missing_mask));texts=[d['title'],d.get('subtitle','')]+[x.get(k,'') for xs in [d['graph']['groups'],d['graph']['nodes'],d['graph']['edges']] for x in xs for k in ['label','subtitle','badge']]+[s['text'] for s in d['story']['steps']]
 for ch in set(''.join(texts)):
  if not ch.isspace():
   m=f.getmask(ch);require((m.size,bytes(m))!=missing_key,'Font lacks glyph '+ch+'; use a font covering the requested language')
 g=d['graph'];groups=[];nodes=[];lookup={};roots=[x for x in g['groups'] if not x.get('parent')]
 def group(x,default):
  b=x.get('bounds',default);c=x.get('color',COLORS[len(groups)%len(COLORS)]);z=dict(x,bounds=b,color=c);groups.append(z);lookup[z['id']]=z
  children=[q for q in g['groups'] if q.get('parent')==x['id']]
  for i,q in enumerate(children):group(q,[b[0]+24,b[1]+72+i*(b[3]-96)/max(len(children),1),b[2]-48,(b[3]-110)/max(len(children),1)])
 for i,x in enumerate(roots):group(x,[90+i*1740/max(len(roots),1),235,1740/max(len(roots),1)-24,670])
 ungrouped=[x for x in g['nodes'] if not x.get('group')];members={None:ungrouped}
 for gr in groups:members[gr['id']]=[x for x in g['nodes'] if x.get('group')==gr['id']]
 for gid,items in members.items():
  parent=lookup.get(gid);b=parent['bounds'] if parent else [80,225,1760,680];cols=min(parent.get('columns',3) if parent else 3,max(len(items),1));rows=math.ceil(len(items)/cols);top=64 if parent else 0
  cw=(b[2]-48-24*(cols-1))/cols;ch=min(145,(b[3]-top-48-38*max(rows-1,0))/max(rows,1))
  for i,x in enumerate(items):
   bb=x.get('bounds',[b[0]+24+(i%cols)*(cw+24),b[1]+top+24+(i//cols)*(ch+38),cw,ch]);box(bb)
   if parent:require(inside(bb,b,12) and bb[1]>=b[1]+58,'Card outside group/header: '+x['id'])
   color=x.get('color',parent['color'] if parent else COLORS[i%len(COLORS)]);shape=x.get('shape','card');maxwidth=bb[2]-(110 if shape=='diamond' else 46)
   lines=wrap(x['label'],font(fp,30),maxwidth,3);subs=wrap(x['subtitle'],font(fp,23),maxwidth,2) if x.get('subtitle') else []
   needed=len(lines)*37+len(subs)*29+(30 if x.get('badge') else 0)+24
   require(needed<=bb[3], 'Card too short: '+x['id'])
   if x.get('badge'):require(font(fp,23).getlength(x['badge'])<=maxwidth,'Badge overflow')
   z=dict(x,bounds=bb,color=color,lines=lines,sub_lines=subs);nodes.append(z);lookup[z['id']]=z
 for i,a in enumerate(nodes):
  for b in nodes[i+1:]:require(not overlap(a['bounds'],b['bounds']),'Overlapping cards: '+a['id']+' / '+b['id'])
 ancestors={}
 for gr in groups:
  anc=set();cur=gr
  while cur.get('parent'):anc.add(cur['parent']);require(len(anc)<=2,'At most three group levels');cur=lookup[cur['parent']]
  ancestors[gr['id']]=anc
 for i,a in enumerate(groups):
  wrap(a['label'],font(fp,28),a['bounds'][2]-44,1)
  if a.get('parent'):require(inside(a['bounds'],lookup[a['parent']]['bounds'],12) and a['bounds'][1]>=lookup[a['parent']]['bounds'][1]+58,'Nested group outside parent/header')
  for b in groups[i+1:]:
   if a['id'] not in ancestors[b['id']] and b['id'] not in ancestors[a['id']]:require(not overlap(a['bounds'],b['bounds']),'Sibling groups overlap')
  for n in nodes:
   if n.get('group')!=a['id'] and a['id'] not in ancestors.get(n.get('group'),set()):require(not overlap(a['bounds'],n['bounds']),'Unrelated card overlaps group')
 edges=[]
 for e in g['edges']:
  a=port(lookup[e['from']]['bounds'],e.get('from_port','right'));b=port(lookup[e['to']]['bounds'],e.get('to_port','left')) if e.get('to') else e['points'][-1]
  pts=e.get('points') or auto_route(a,b,[x['bounds'] for x in nodes])
  require(len(pts)>=2 and pts[0]==a and pts[-1]==b,'Route endpoints must equal explicit ports: '+e['id'])
  for u,v in zip(pts,pts[1:]):
   point(u);point(v);require(u!=v and (u[0]==v[0] or u[1]==v[1]),'Nonorthogonal/zero route '+e['id'])
   for n in nodes:require(not hit(u,v,n['bounds']),'Route crosses card '+n['id'])
  color=e.get('color',lookup[e['from']]['color']);z=dict(e,points=pts,color=color)
  if e.get('label'):
   tw=font(fp,23).getlength(e['label']);candidates=[]
   for a,b in zip(pts,pts[1:]):
    mx=(a[0]+b[0])/2;my=(a[1]+b[1])/2
    candidates.extend([[mx,my-28],[mx,my+28]] if a[1]==b[1] else [[mx+tw/2+14,my],[mx-tw/2-14,my]])
   for x,y in candidates:
    lb=[x-tw/2-5,y-16,tw+10,32]
    headers=[[g['bounds'][0],g['bounds'][1],g['bounds'][2],58] for g in groups]
    if 60<=lb[0] and lb[0]+lb[2]<=1860 and 205<=lb[1] and lb[1]+lb[3]<=925 and not any(overlap(lb,n['bounds']) for n in nodes) and not any(overlap(lb,r) for r in headers):z['label_pos']=[x,y];break
   require('label_pos' in z,'No clear branch-label position: '+e['id'])
  edges.append(z)
 require(font(fp,48).getlength(d['title'])<=1730,'Title overflow');require(font(fp,24).getlength(d.get('subtitle',''))<=1730,'Subtitle overflow')
 caption_width=1805-(len(d['story']['steps'])-1)*(13 if len(d['story']['steps'])>18 else 22)-188
 captions=[wrap(s['text'],font(fp,28),caption_width,2) for s in d['story']['steps']]
 return {'width':W,'height':H,'groups':groups,'nodes':nodes,'edges':edges,'captions':captions,'font_family':font(fp,30).getname()[0]}
def state(d,t):
 steps=d['story']['steps'];total=sum(s.get('duration',3) for s in steps);t=t%total;start=0
 for i,s in enumerate(steps):
  duration=s.get('duration',3)
  if t<start+duration:break
  start+=duration
 active=set(s['targets']);trail=set(q for ss in steps[:i] for q in ss['targets']) if d['story'].get('trail',True) else set()
 return {'index':i,'active':active,'trail':trail,'phase':(t-start)/duration,'time':t}
def blend(c,amount):
 a=tuple(int(c[i:i+2],16) for i in [1,3,5]);b=(33,43,63);return '#'+''.join(f'{int(x*amount+y*(1-amount)):02x}' for x,y in zip(a,b))
def line_points(pts,progress):
 lengths=[math.dist(a,b) for a,b in zip(pts,pts[1:])];p=progress*sum(lengths)
 for a,b,le in zip(pts,pts[1:],lengths):
  if p<=le:return [a[0]+(b[0]-a[0])*p/le,a[1]+(b[1]-a[1])*p/le]
  p-=le
 return pts[-1]
def arrow(dr,a,b,c):
 dx=b[0]-a[0];dy=b[1]-a[1];le=math.hypot(dx,dy);ux=dx/le;uy=dy/le
 dr.polygon([b,(b[0]-ux*13-uy*6,b[1]-uy*13+ux*6),(b[0]-ux*13+uy*6,b[1]-uy*13-ux*6)],fill=c)
def drawtext(dr,xy,text,fp,size,fill=TEXT,anchor='lt'):dr.text(xy,text,font=font(fp,size),fill=fill,anchor=anchor)
def raster(d,l,fp,t=0,overview=False):
 """Neon presentation renderer: fixed geometry, additive two-radius bloom, crisp text."""
 from PIL import ImageChops
 st=state(d,t);im=Image.new('RGB',(W,H),'#060b16');dr=ImageDraw.Draw(im)
 halo=Image.new('RGB',(W,H));hd=ImageDraw.Draw(halo)
 text_jobs=[]
 def rgb(c):return tuple(int(c[i:i+2],16) for i in (1,3,5))
 def shade(c,a,base=(7,14,27)):return tuple(round(v*a+b*(1-a)) for v,b in zip(rgb(c),base))
 for g in l['groups']:
  x,y,w,h=g['bounds'];c=g['color']
  dr.rounded_rectangle([x,y,x+w,y+h],20,fill=shade(c,.025),outline=shade(c,.26),width=1)
  dr.line([(x+22,y+49),(x+w-22,y+49)],fill=shade(c,.23),width=1)
  dr.rounded_rectangle([x+20,y+17,x+25,y+36],2,fill=c)
  text_jobs.append(((x+39,y+13),g['label'],28,c,'lt'))
 for e in l['edges']:
  active=e['id'] in st['active'] or overview;seen=e['id'] in st['trail'];c=e['color'];pts=[tuple(p) for p in e['points']]
  col=c if active else shade(c,.4 if seen else .12)
  dr.line(pts,fill=col,width=3 if active else 2,joint='curve');arrow(dr,pts[-2],pts[-1],col)
  if e.get('direction')=='both':arrow(dr,pts[1],pts[0],col)
  if active:
   hd.line(pts,fill=shade(c,.7),width=8,joint='curve')
   dr.line(pts,fill=shade(c,.95),width=2)
  if e.get('label'):text_jobs.append((e['label_pos'],e['label'],23,MUTED,'mm'))
  if active and not overview:
   length=sum(math.dist(a,b) for a,b in zip(pts,pts[1:]));phases=[st['phase']]
   if length>650:phases.append((st['phase']+.5)%1)
   for phase in phases:
    for k in range(24,0,-1):
     p=phase-k*4/max(length,1)
     if p<0:continue
     q=line_points(pts,p);a=(1-k/25)**1.6;rr=1.5+2*a
     dr.ellipse([q[0]-rr,q[1]-rr,q[0]+rr,q[1]+rr],fill=shade(c,a))
     hd.ellipse([q[0]-4,q[1]-4,q[0]+4,q[1]+4],fill=shade(c,a*.6))
    q=line_points(pts,phase)
    hd.ellipse([q[0]-13,q[1]-13,q[0]+13,q[1]+13],fill=c)
    dr.ellipse([q[0]-7,q[1]-7,q[0]+7,q[1]+7],fill=c)
    dr.ellipse([q[0]-3,q[1]-3,q[0]+3,q[1]+3],fill='#f6ffff')
 for n in l['nodes']:
  x,y,w,h=n['bounds'];active=n['id'] in st['active'] or overview;c=n['color'];seen=n['id'] in st['trail'];shape=n.get('shape','card');col=c if active else shade(c,.55 if seen else .32);fill=shade(c,.09 if active else .035)
  if shape=='diamond':
   poly=[(x+w/2,y),(x+w,y+h/2),(x+w/2,y+h),(x,y+h/2)]
   dr.polygon(poly,fill=fill,outline=col,width=2)
   if active:hd.line(poly+[poly[0]],fill=shade(c,.85),width=6,joint='curve')
  else:
   dr.rounded_rectangle([x,y,x+w,y+h],15,fill=fill,outline=col,width=2)
   dr.rounded_rectangle([x+12,y+17,x+17,y+h-17],2,fill=col)
   dr.line([(x+27,y+1),(x+w-22,y+1)],fill=col,width=2)
   if active:hd.rounded_rectangle([x,y,x+w,y+h],15,outline=shade(c,.8),width=6)
  total=len(n['lines'])*37+len(n['sub_lines'])*29+(30 if n.get('badge') else 0);yy=y+(h-total)/2
  for line in n['lines']:text_jobs.append(((x+w/2,yy),line,30,'#f1f7ff','mt'));yy+=37
  for line in n['sub_lines']:text_jobs.append(((x+w/2,yy),line,23,'#a9bbd3','mt'));yy+=29
  if n.get('badge'):text_jobs.append(((x+w/2,yy),n['badge'],23,col,'mt'))
 # Bloom only geometry, never labels: broad colored halo plus a tight luminous edge.
 wide=halo.filter(ImageFilter.GaussianBlur(13)).point(lambda v:min(255,round(v*.65)))
 tight=halo.filter(ImageFilter.GaussianBlur(3)).point(lambda v:min(255,round(v*.45)))
 raw=im
 im=ImageChops.add(ImageChops.add(im,wide),tight)
 # Keep card interiors stable; moving bloom stays outside text panels.
 for n in l['nodes']:
  if n.get('shape','card')=='card':
   x,y,w,h=n['bounds'];rect=(int(x+10),int(y+10),int(x+w-10),int(y+h-10));im.paste(raw.crop(rect),rect[:2])
 dr=ImageDraw.Draw(im)
 drawtext(dr,(85,55),d['title'],fp,48,'#f3f8ff');drawtext(dr,(87,128),d.get('subtitle',''),fp,24,'#8299b7')
 for xy,txt,size,col,anchor in text_jobs:drawtext(dr,xy,txt,fp,size,col,anchor)
 dr.rounded_rectangle([80,965,1840,1050],15,fill='#0d182a',outline='#203854',width=1)
 dr.line([(101,966),(1830,966)],fill='#2e687f',width=1)
 dr.ellipse([98,988,139,1029],fill='#123f68',outline='#42cfff',width=2);drawtext(dr,(118,1009),str(st['index']+1),fp,24,'#e7fbff','mm')
 for j,line in enumerate(l['captions'][st['index']]):drawtext(dr,(158,979+j*33),line,fp,28,'#e7f0fc')
 count=len(d['story']['steps']);gap=13 if count>18 else 22;r=4 if count>18 else 5
 for k in range(count):
  x=1805-(count-1-k)*gap;dr.ellipse([x-r,1009-r,x+r,1009+r],fill='#42cfff' if k<=st['index'] else '#24344a')
 return im

def svg(d,l):
 esc=html.escape;family=esc(l['font_family'],quote=True);out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(d["title"],quote=True)}"><defs><filter id="glow"><feGaussianBlur stdDeviation="3"/></filter></defs><style>text{{font-family:"{family}",sans-serif;fill:{TEXT}}}.dim{{opacity:.35}}.on{{opacity:1}}[data-target].on>rect,[data-target].on>polygon,[data-target].on>polyline{{filter:drop-shadow(0 0 3px currentColor) drop-shadow(0 0 9px currentColor)}}</style>',f'<rect width="{W}" height="{H}" fill="{BG}"/>',f'<text x="85" y="104" font-size="48">{esc(d["title"])}</text><text x="87" y="160" font-size="24" style="fill:{MUTED}">{esc(d.get("subtitle",""))}</text>']
 for g in l['groups']:
  x,y,w,h=g['bounds'];c=g['color'];out.append(f'<g data-target="{g["id"]}" style="color:{c}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="#101829" stroke="{c}" stroke-opacity=".6" stroke-width="2"/><text x="{x+25}" y="{y+42}" font-size="28">{esc(g["label"])}</text></g>')
 for e in l['edges']:
  pts=' '.join(','.join(map(str,p)) for p in e['points']);c=e['color'];eid=e['id'];out.append(f'<defs><marker id="a_{eid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="{c}"/></marker></defs>')
  start=f' marker-start="url(#a_{eid})"' if e.get('direction')=='both' else '';out.append(f'<g data-target="{eid}" style="color:{c}"><polyline points="{pts}" fill="none" stroke="{c}" stroke-width="3" marker-end="url(#a_{eid})"{start}/></g><circle data-particle="{eid}" r="6" fill="{TEXT}" style="filter:drop-shadow(0 0 4px {c}) drop-shadow(0 0 9px {c})" visibility="hidden"/>')
  for ti in range(1,13):out.append(f'<circle data-tail="{eid}" data-tail-index="{ti}" r="{max(1,4-ti*.22)}" fill="{c}" opacity="{(1-ti/14)**1.5}" visibility="hidden"/>')
  if e.get('direction')=='both':out.append(f'<circle data-return="{eid}" r="5" fill="{TEXT}" visibility="hidden"/>')
  if e.get('label'):
   a=e['label_pos'];out.append(f'<text x="{a[0]}" y="{a[1]+8}" font-size="23" text-anchor="middle">{esc(e["label"])}</text>')
 for n in l['nodes']:
  x,y,w,h=n['bounds'];c=n['color'];out.append(f'<g data-target="{n["id"]}" style="color:{c}">')
  if n.get('shape')=='diamond':out.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}" fill="{CARD}" stroke="{c}" stroke-width="2"/>')
  else:out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{CARD}" stroke="{c}" stroke-width="2"/><rect x="{x+10}" y="{y+13}" width="6" height="{h-26}" rx="3" fill="{c}"/>')
  lines=[(s,30,TEXT,37) for s in n['lines']]+[(s,23,MUTED,29) for s in n['sub_lines']]+([(n['badge'],23,c,30)] if n.get('badge') else []);yy=y+(h-sum(q[3] for q in lines))/2+28
  for line,size,color,spacing in lines:out.append(f'<text x="{x+w/2}" y="{yy}" font-size="{size}" text-anchor="middle" style="fill:{color}">{esc(line)}</text>');yy+=spacing
  out.append('</g>')
 out.append('<rect x="80" y="965" width="1760" height="85" rx="14" fill="#141d31"/><circle cx="117" cy="1009" r="20" fill="#1672c8"/><text data-progress="number" x="117" y="1017" text-anchor="middle" font-size="24">1</text><g data-caption="text">')
 for j,s in enumerate(l['captions'][0]):out.append(f'<text x="158" y="{1006+j*33}" font-size="28">{esc(s)}</text>')
 out.append('</g>');count=len(d['story']['steps']);gap=13 if count>18 else 22;r=4 if count>18 else 6
 for k in range(count):out.append(f'<circle data-dot="{k}" cx="{1805-(count-1-k)*gap}" cy="1009" r="{r}" fill="{("#258fea" if k==0 else "#34415b")}"/>')
 out.append('</svg>');return ''.join(out)
def make_html(d,l,s,fp=None):
 data=json.dumps({'spec':d,'layout':l},ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
 extra=''
 if fp:extra='@font-face{font-family:"'+l['font_family']+'";src:url(data:font/otf;base64,'+base64.b64encode(Path(fp).read_bytes()).decode()+')}'
 return '<!doctype html><html lang="'+d['locale']+'"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(d['title'])+'</title><style>'+extra+'body{margin:0;background:'+BG+';color:'+TEXT+';font:18px sans-serif}svg{width:100%;max-height:90vh;display:block}nav{display:flex;gap:12px;justify-content:center;align-items:center}button,select{font:inherit;padding:8px}</style>'+s+'<nav><button id="prev">◀</button><button id="play">Pause / 暫停</button><button id="next">▶</button><button id="reset">Replay / 重播</button><select id="speed"><option>0.5</option><option selected>1</option><option>2</option></select><label><input id="motion" type="checkbox">Reduced motion / 靜態</label></nav><script id="project" type="application/json">'+data+'</script>'+'''<script>
'use strict';const data=JSON.parse(document.getElementById('project').textContent),steps=data.spec.story.steps;let time=0,last=null,playing=true,speed=1;const starts=[];let total=0;for(const s of steps){starts.push(total);total+=s.duration??3;}const motion=document.getElementById('motion');motion.checked=matchMedia('(prefers-reduced-motion: reduce)').matches;if(motion.checked)playing=false;
function stateAt(t){t=((t%total)+total)%total;let i=steps.length-1;while(i>0&&t<starts[i])i--;return {index:i,phase:(t-starts[i])/(steps[i].duration??3)};}
function pointAt(pts,p){const lens=pts.slice(1).map((q,i)=>Math.hypot(q[0]-pts[i][0],q[1]-pts[i][1]));let n=p*lens.reduce((a,b)=>a+b,0);for(let i=0;i<lens.length;i++){if(n<=lens[i])return pts[i].map((v,j)=>v+(pts[i+1][j]-v)*n/lens[i]);n-=lens[i];}return pts.at(-1);}
function render(t){const s=stateAt(t),active=new Set(steps[s.index].targets),trail=new Set(data.spec.story.trail===false?[]:steps.slice(0,s.index).flatMap(x=>x.targets));document.querySelectorAll('[data-target]').forEach(x=>{const on=active.has(x.dataset.target);for(const shape of x.querySelectorAll('rect,polygon,polyline'))shape.style.opacity=on?'1':trail.has(x.dataset.target)?'.7':'.45';x.classList.toggle('on',on);});for(const e of data.layout.edges){for(const [attr,phase] of [['data-particle',s.phase],['data-return',1-s.phase]]){const dot=document.querySelector('['+attr+'="'+e.id+'"]');if(!dot)continue;dot.setAttribute('visibility',active.has(e.id)&&!motion.checked?'visible':'hidden');const q=pointAt(e.points,phase);dot.setAttribute('cx',q[0]);dot.setAttribute('cy',q[1]);}const length=e.points.slice(1).reduce((sum,p,i)=>sum+Math.hypot(p[0]-e.points[i][0],p[1]-e.points[i][1]),0);document.querySelectorAll('[data-tail="'+e.id+'"]').forEach(dot=>{const phase=s.phase-Number(dot.dataset.tailIndex)*7/Math.max(1,length);dot.setAttribute('visibility',active.has(e.id)&&!motion.checked&&phase>=0?'visible':'hidden');const p=pointAt(e.points,Math.max(0,phase));dot.setAttribute('cx',p[0]);dot.setAttribute('cy',p[1]);});}document.querySelector('[data-progress]').textContent=s.index+1;const cap=document.querySelector('[data-caption]');cap.replaceChildren();for(const [j,line] of data.layout.captions[s.index].entries()){const n=document.createElementNS('http://www.w3.org/2000/svg','text');n.setAttribute('x',158);n.setAttribute('y',1006+j*33);n.setAttribute('font-size',28);n.textContent=line;cap.append(n);}document.querySelectorAll('[data-dot]').forEach(x=>x.setAttribute('fill',Number(x.dataset.dot)<=s.index?'#258fea':'#34415b'));document.getElementById('play').textContent=playing?'Pause / 暫停':'Play / 播放';return s;}
function jump(n){playing=false;time=starts[(stateAt(time).index+n+steps.length)%steps.length];render(time);}document.getElementById('prev').onclick=()=>jump(-1);document.getElementById('next').onclick=()=>jump(1);document.getElementById('play').onclick=()=>{playing=!playing;last=null;render(time);};document.getElementById('reset').onclick=()=>{time=0;playing=!motion.checked;render(time);};document.getElementById('speed').onchange=e=>speed=Number(e.target.value);motion.onchange=()=>{if(motion.checked)playing=false;render(time);};addEventListener('keydown',e=>{if(e.target.matches('input,select,button'))return;if(e.key==='ArrowRight')jump(1);if(e.key==='ArrowLeft')jump(-1);if(e.key===' '){e.preventDefault();document.getElementById('play').click();}});window.EWDiagram={stateAt,renderAt:t=>{playing=false;time=t;return render(t);},data};function tick(now){if(playing&&last!==null&&!motion.checked)time+=(now-last)/1000*speed;last=now;render(time);requestAnimationFrame(tick);}render(0);requestAnimationFrame(tick);
</script></html>'''
def main():
 ap=argparse.ArgumentParser();ap.add_argument('project');ap.add_argument('--out',default='output');ap.add_argument('--font');ap.add_argument('--embed-font',action='store_true',help='Only with confirmed font embedding license');ap.add_argument('--validate-only',action='store_true');ap.add_argument('--gif-fps',type=int);args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
 try:
  require(Path(args.project).stat().st_size<=2000000,'Input too large')
  def pairs(xs):
   o={}
   for k,v in xs:require(k not in o,'Duplicate JSON key');o[k]=v
   return o
  d=json.loads(Path(args.project).read_text(),object_pairs_hook=pairs)
  if args.gif_fps is not None:d.setdefault('export',{})['fps']=args.gif_fps
  validate(d);(out/'diagram.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
  if args.validate_only:(out/'capability-report.json').write_text(json.dumps({'version':'0.5.1','graph_validated':True,'layout_checked':False,'produced':['json'],'rendering_requested':False}));print('Validated JSON only');return
  fp=resolve_font(args.font,d['locale']);l=layout(d,fp);(out/'layout.json').write_text(json.dumps(l,ensure_ascii=False,indent=2));formats=d.get('export',{}).get('formats',['json','png','svg','html','gif']);produced=['json'];s=svg(d,l)
  if 'svg' in formats:(out/'diagram.svg').write_text(s);produced.append('svg')
  if 'html' in formats:(out/'diagram.html').write_text(make_html(d,l,s,fp if args.embed_font else None));produced.append('html')
  first=raster(d,l,fp)
  if 'png' in formats:raster(d,l,fp,overview=True).save(out/'diagram.png');produced.append('png')
  report={'version':'0.5.1','renderer':'EW shared-layout SVG + Pillow','graph_validated':True,'layout_checked':True,'produced':produced,'html_browser_tested':False,'font_family':l['font_family'],'html_font_embedded':args.embed_font,'limitations':['No automatic PDF OCR: agent must inspect and transcribe source','No MP4 or editable PPTX','Crossings are not junctions; source completeness needs human/agent visual review','Explicit geometry supported; dense complex layouts may need manual bounds or separate detail views']}
  if 'gif' in formats:
   fps=d.get('export',{}).get('fps',10);total=sum(s.get('duration',3) for s in d['story']['steps']);count=math.ceil(total*fps)
   # One palette across whole story to avoid flickering static labels.
   palette=raster(d,l,fp,overview=True).quantize(colors=248,method=Image.Quantize.MEDIANCUT);frames=[raster(d,l,fp,k*total/count).quantize(palette=palette,dither=Image.Dither.NONE) for k in range(count)];ticks=round(total*100);dur=[10*(round((k+1)*ticks/count)-round(k*ticks/count)) for k in range(count)]
   frames[0].save(out/'diagram.gif',save_all=True,append_images=frames[1:],duration=dur,loop=0,disposal=1,optimize=False)
   im=Image.open(out/'diagram.gif');actual=sum(im.seek(k) or im.info.get('duration',0) for k in range(im.n_frames));require(im.size==(W,H) and im.n_frames>1 and im.info.get('loop')==0 and abs(actual-total*1000)<=10,'GIF verification failed');produced.append('gif');report['gif']={'dimensions':im.size,'frames':im.n_frames,'duration_ms':actual,'loop':0,'verified':True}
  (out/'capability-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
 except (ValueError,KeyError,TypeError,OSError) as e:
  (out/'capability-report.json').write_text(json.dumps({'version':'0.5.1','success':False,'error':str(e)},ensure_ascii=False));print(str(e),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
