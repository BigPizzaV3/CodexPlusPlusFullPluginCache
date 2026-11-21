"""PNG from the exact shared layout. Pillow raster export, not Manim."""
import math
from functools import lru_cache
@lru_cache(maxsize=32)
def font(path,size):return ImageFont.truetype(path,size)
from PIL import Image,ImageDraw,ImageFont
from diagram import THEMES

def state_at(d,t):
 total=sum(x["duration"] for x in d["story"]["steps"]);t=t%total
 for i,step in enumerate(d["story"]["steps"]):
  if t<step["duration"]:return i,set(step["targets"])
  t-=step["duration"]
 return 0,set()

def render(d,l,fontpath,path=None,t=0):
 index,targets=state_at(d,t)
 c=THEMES[d['theme']['mode']];im=Image.new('RGB',(1920,1080),c['bg']);draw=ImageDraw.Draw(im)
 def text(x,y,s,size,anchor='ls'):
  draw.text((x,y),s,font=font(fontpath,size),fill=c['text'],anchor=anchor)
 text(100,112,d['title'],48);text(100,160,'EW MANIM DRAW · DIAGRAM-AS-CODE',24)
 for g in l['groups']:
  draw.rounded_rectangle((g['x'],g['y'],g['x']+g['w'],g['y']+g['h']),20,fill=c['group'],outline=c['line'],width=1)
  for i,line in enumerate(g['lines']):text(g['x']+28,g['y']+43+i*32,line,28)
 for e in l['edges']:
  pts=[tuple(p) for p in e['points']];draw.line(pts,fill=c['line'],width=3)
  a,b=pts[-2:];dx=b[0]-a[0];dy=b[1]-a[1];mag=math.hypot(dx,dy);ux,uy=dx/mag,dy/mag
  draw.polygon([b,(b[0]-20*ux+8*uy,b[1]-20*uy-8*ux),(b[0]-20*ux-8*uy,b[1]-20*uy+8*ux)],fill=c['line'])
 # Time-derived moving dash overlay; graph remains visible on every frame.
 for e in l['edges']:
  if e['id'] not in targets:continue
  distance=0;phase=(t*70)%34
  for a,b in zip(e['points'],e['points'][1:]):
   dx=b[0]-a[0];dy=b[1]-a[1];length=math.hypot(dx,dy);pos=0
   while pos<length:
    cycle=(distance+pos+phase)%34;on=cycle<18;span=min((18-cycle if on else 34-cycle),length-pos)
    if span<1e-8:span=min(.001,length-pos)
    if on:draw.line((a[0]+dx*pos/length,a[1]+dy*pos/length,a[0]+dx*(pos+span)/length,a[1]+dy*(pos+span)/length),fill=c['accent'],width=5)
    pos+=span
   distance+=length
 for n in l['nodes']:
  draw.rounded_rectangle((n['x'],n['y'],n['x']+n['w'],n['y']+n['h']),14,fill=c['card'],outline=c['accent'] if n['id'] in targets else c['line'],width=5 if n['id'] in targets else 2)
  for i,line in enumerate(n['lines']):text(n['x']+n['w']/2,n['y']+n['h']/2+(i-(len(n['lines'])-1)/2)*36+10,line,30,'ms')
 draw.rounded_rectangle((100,860,1820,1002),16,fill=c['group'])
 text(130,894,f'{index+1} / {len(l["captions"])}',24)
 for i,line in enumerate(l['captions'][index]):text(130,940+i*34,line,28)
 if path is not None:im.save(path)
 return im


def render_gif(d,l,fontpath,path,fps=6):
 total=sum(x['duration'] for x in d['story']['steps']);count=math.ceil(total*fps)
 if not 1<=fps<=12 or count>180:raise ValueError('GIF budget: fps 1–12, maximum 180 frames; shorten story or lower --gif-fps')
 # Shared fixed palette prevents frame-to-frame palette flicker.
 first=render(d,l,fontpath,t=0).quantize(colors=128)
 frames=[first];durations=[]
 for k in range(count):
  start=round(k*1000/fps/10)*10;end=round(min((k+1)/fps,total)*1000/10)*10;durations.append(max(10,end-start))
  if k:frames.append(render(d,l,fontpath,t=k/fps).quantize(palette=first))
 frames[0].save(path,save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=False,disposal=2)
 return {'fps':fps,'frame_count':count,'duration_seconds':total,'renderer':'Pillow shared-layout timeline renderer','time_rule':'frame_index / fps; modulo total duration','loop_note':'Guided story returns to first step; one-step Flow Loop animates a fixed path'}
