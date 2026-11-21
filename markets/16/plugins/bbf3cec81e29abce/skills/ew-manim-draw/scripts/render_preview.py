"""Deterministic PNG/GIF fallback renderer using Pillow, NOT Manim."""
import argparse, json, math, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from validate_flow import validate

def font_for(size):
    import os
    candidates=[os.environ.get('EW_MANIM_FONT_PATH',''),'/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc','/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    for p in candidates:
        if p and Path(p).exists(): return ImageFont.truetype(p,size)
    raise RuntimeError('No suitable font found. Set EW_MANIM_FONT_PATH to a licensed CJK-capable font file.')

def draw_frame(spec, shown_nodes, shown_edges, highlighted=None, scale=1):
    w,h=spec['output']['width'],spec['output']['height']
    w=int(w*scale); h=int(h*scale)
    im=Image.new('RGB',(w,h),'#FAFCFF'); d=ImageDraw.Draw(im)
    nodes=spec['nodes']; n=len(nodes)
    bw=min(int(w*.20),int(w/(n+0.35))); bh=max(54,int(h*.17))
    gap=(w-n*bw)/(n+1); y=h//2
    positions={}
    for i,node in enumerate(nodes):
        x=int(gap+(bw+gap)*i); positions[node['id']]=(x,y-bh//2,x+bw,y+bh//2)
    for i,e in enumerate(spec['edges']):
        eid=e.get('id',f'edge_{i}')
        if eid not in shown_edges: continue
        a=positions[e['from']]; b=positions[e['to']]
        x1,y1=a[2],y; x2,y2=b[0],y
        if x2<=x1: continue
        d.line((x1,y1,x2,y2),fill='#2463A8',width=max(3,int(w/400)))
        tip=max(8,int(w/100)); d.polygon([(x2,y2),(x2-tip,y2-tip//2),(x2-tip,y2+tip//2)],fill='#2463A8')
    font=font_for(max(12,int(h*.035)))
    for node in nodes:
        nid=node['id']
        if nid not in shown_nodes: continue
        rect=positions[nid]
        d.rounded_rectangle(rect,radius=15,fill='#E8F2FF' if nid!=highlighted else '#B7DBFF',outline='#2463A8',width=max(2,int(w/650)))
        label=node['label']; bounds=d.textbbox((0,0),label,font=font)
        tw=bounds[2]-bounds[0]; th=bounds[3]-bounds[1]
        if tw>bw-16: raise ValueError(f'Label too wide for fallback layout: {label}. Shorten label or render with Manim.')
        d.text(((rect[0]+rect[2]-tw)//2,y-th//2-bounds[1]),label,font=font,fill='#142B4A')
    return im

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('--out',default='output'); args=ap.parse_args()
    spec=validate(json.loads(Path(args.spec).read_text(encoding='utf-8')))
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    shown_nodes=set();shown_edges=set();highlight=None
    frames=[]; durations=[]
    fps=min(spec['output']['fps'],15)
    # Timeline event states, with hold durations; no deceptive tweening.
    for ev in spec['timeline']:
        if ev['kind']=='appear': shown_nodes.add(ev['target'])
        elif ev['kind']=='draw_edge': shown_edges.add(ev['target'])
        elif ev['kind']=='highlight': highlight=ev['target']
        frame=draw_frame(spec,shown_nodes,shown_edges,highlight,scale=min(1,960/spec['output']['width']))
        frames.append(frame);durations.append(max(70,round(ev['duration']*1000)))
        if ev['kind']=='highlight': highlight=None
    final=draw_frame(spec,{n['id'] for n in spec['nodes']},{e.get('id',f'edge_{i}') for i,e in enumerate(spec['edges'])},scale=1)
    png=out/'flow.png';gif=out/'flow.gif'
    final.save(png)
    # Quantize to a stable palette, GIF frame duration follows the JSON timeline.
    frames[0].save(gif,save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=False)
    print(f'Created {png} and {gif}; renderer=Pillow fallback (not Manim)')
if __name__=='__main__': main()
