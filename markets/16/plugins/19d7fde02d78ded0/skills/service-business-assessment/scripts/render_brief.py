#!/usr/bin/env python3
"""Render reviewed brief.pages from a canonical report; fail instead of shrinking to illegibility."""
import argparse,json,html
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from validate_report import validate
def render(report,out,assets,logo=None,font=None,font_bold=None,brand='Overtime Labs'):
 errors=validate(report)
 if errors:raise ValueError('\n'.join(errors))
 pages=report.get('brief',{}).get('pages',[])
 if not 1<=len(pages)<=5:raise ValueError('Provide 1–5 reviewed brief.pages')
 regular,bold='Helvetica','Helvetica-Bold'
 if font and font_bold:
  pdfmetrics.registerFont(TTFont('BriefRegular',str(font)));pdfmetrics.registerFont(TTFont('BriefBold',str(font_bold)));regular,bold='BriefRegular','BriefBold'
 src={s['id']:s for s in report['sources']};findings={f['id']:f for f in report['findings']}
 c=canvas.Canvas(str(out),pagesize=(612,792));c.setTitle(report['title']+': digital presence assessment');c.setAuthor(brand)
 field=report.get('brief',{}).get('theme')=='field-guide'
 display=bold
 if field:
  serif=report.get('brief',{}).get('heading_font')
  if serif:pdfmetrics.registerFont(TTFont('BriefDisplay',str(serif)));display='BriefDisplay'
 ink=HexColor('#20221F');muted=HexColor('#61665F');blue=HexColor('#007AFF');paper=HexColor('#F8F6F1') if field else white;pale=HexColor('#EEEFE8') if field else HexColor('#F3F3F5');qa=[]
 def clean(s):return str(s).replace('–','-').replace('—','-').replace('‑','-')
 def paragraph(text,y,size=10.4,color=ink,b=False,width=516,x=48,heading=False):
  p=Paragraph(clean(text),ParagraphStyle('body',fontName=display if heading else bold if b else regular,fontSize=size,leading=size*(1.14 if heading else 1.4),textColor=color));_,h=p.wrap(width,1000);p.drawOn(c,x,792-y-h);return y+h
 def drawlogo():
  if not logo:return
  im=Image.open(logo);a,b,z,d=im.getbbox();scale=24/max(z-a,d-b);x=48+(24-(z-a)*scale)/2;y=20+(24-(d-b)*scale)/2
  c.saveState();p=c.beginPath();p.rect(48,748,24,24);c.clipPath(p,stroke=0,fill=0);c.drawImage(str(logo),x-a*scale,792-y-(im.height-b)*scale,width=im.width*scale,height=im.height*scale,mask='auto');c.restoreState()
 for n,page in enumerate(pages,1):
  if n>1:c.showPage()
  c.setFillColor(paper);c.rect(0,0,612,792,stroke=0,fill=1)
  drawlogo();paragraph(brand,25,10,b=True,x=81 if logo else 48);paragraph(report['title'].upper(),26,8,muted,x=415,width=149)
  c.setStrokeColor(HexColor('#DEDEE2'));c.line(48,735,564,735)
  y=paragraph(page['kicker'].upper(),72,8.5,blue,b=True)+12;y=paragraph(page['title'],y,(31 if n==1 else 26) if field else 22,b=True,heading=field)
  if page.get('deck'):y=paragraph(page['deck'],y+10,10.3,muted)
  y+=20
  for block in page['blocks']:
   kind=block['type']
   if kind=='finding':
    f=findings[block['finding_id']];y=paragraph(f['title'],y,11.4,b=True)+5;y=paragraph(html.escape(f['observation']),y)+6;y=paragraph(html.escape(f['recommendation']),y,10,muted)+16
   elif kind=='text':
    if block.get('heading'):y=paragraph(block['heading'],y,11.4,b=True)+5
    y=paragraph(block['text'],y,block.get('size',10.4))+block.get('space_after',16)
   elif kind=='table':
    widths=block.get('widths',[516/len(block['headers'])]*len(block['headers']));fs=block.get('font_size',9.2)
    st=ParagraphStyle('cell',fontName=regular,fontSize=fs,leading=fs*1.35,textColor=ink);hs=ParagraphStyle('head',parent=st,fontName=bold,textColor=ink if field else white)
    t=Table([[Paragraph(clean(html.escape(str(v))),hs) for v in block['headers']]]+[[Paragraph(clean(str(v)),st) for v in row] for row in block['rows']],colWidths=widths)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),pale if field else ink),('ROWBACKGROUNDS',(0,1),(-1,-1),[paper,white]),('LINEBELOW',(0,0),(-1,0),0.6,blue if field else ink),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),8 if field else 9),('BOTTOMPADDING',(0,0),(-1,-1),8 if field else 9),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9)]));_,h=t.wrap(516,1000);t.drawOn(c,48,792-y-h);y+=h+16
   elif kind=='image':
    path=(Path(assets)/block['path']).resolve()
    if not path.is_relative_to(Path(assets).resolve()):raise ValueError('Image outside evidence directory')
    im=Image.open(path);a,b,z,d=block.get('region',[0,0,im.width,im.height]);h=min(block.get('height',155),516*(d-b)/(z-a));w=h*(z-a)/(d-b);scale=w/(z-a)
    c.saveState();clip=c.beginPath();clip.rect(48,792-y-h,w,h);c.clipPath(clip,stroke=0,fill=0);c.drawImage(str(path),48-a*scale,792-y-(im.height-b)*scale,width=im.width*scale,height=im.height*scale,mask='auto');c.restoreState()
    if block.get('aside_text'):
     xx=48+w+22;ww=516-w-22;yy=y
     if block.get('aside_heading'):yy=paragraph(block['aside_heading'],yy,11.4,b=True,x=xx,width=ww)+7
     yy=paragraph(block['aside_text'],yy,10.2,x=xx,width=ww)
     h=max(h,yy-y)
    y+=h+6;y=paragraph(html.escape(block['caption']),y,8.1,muted,width=516)+16
   else:raise ValueError('Unsupported block type')
  qa.append(dict(page=n,body_bottom=round(y-16,1),within_body=y-16<=703))
  if y-16>703:raise ValueError(f'Page {n} overflows: body reaches {y-16:.1f}; shorten text or move a block.')
  source_text='Sources: '+' | '.join(f'<link href="{html.escape(src[i]["url"],quote=True)}" color="#0064CF">{html.escape(src[i]["title"])}</link>' for i in page['source_ids'])
  bottom=paragraph(source_text,719,7.1,muted)
  if bottom>756:raise ValueError(f'Page {n} source notes overflow')
  paragraph(report['assessment_date']+' / DIGITAL PRESENCE ASSESSMENT',764,7,muted);paragraph(f'{n} / {len(pages)}',764,8,muted,x=540,width=24)
 c.save();Path(str(out)+'.qa.json').write_text(json.dumps(qa,indent=2)+'\n');return qa
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('report');ap.add_argument('--out',required=True);ap.add_argument('--assets',required=True);ap.add_argument('--logo');ap.add_argument('--font');ap.add_argument('--font-bold');ap.add_argument('--brand',default='Overtime Labs');a=ap.parse_args();print(render(json.loads(Path(a.report).read_text()),a.out,a.assets,a.logo,a.font,a.font_bold,a.brand))
