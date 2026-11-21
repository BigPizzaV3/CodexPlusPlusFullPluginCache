import fs from 'node:fs';
import {helpers} from './_marketing.mjs';
export const id='marketing_3c';
export function pptx(ctx,item,pageNum){
 const {s,text,line,head,c}=helpers(ctx,item,pageNum);
 const g=JSON.parse(fs.readFileSync(new URL('../../../../../assets/examples/venn-geometry.json',import.meta.url),'utf8'));
 for(const [x,y] of g.circles)s.addShape(ctx.pptx.ShapeType.ellipse,{x:x-g.radius,y:y-g.radius,w:g.radius*2,h:g.radius*2,fill:{color:c.SOFTBLUE,transparency:55},line:{type:'none'}});
 // Replaced by an editable DrawingML freeform of (Customer ∩ Company) \ Competitor.
 s.addShape(ctx.pptx.ShapeType.rect,{x:g.x,y:g.y,w:g.w,h:g.h,objectName:'highground-region',fill:{color:c.NAVY},line:{type:'none'}});
 for(const [x,y] of g.circles)s.addShape(ctx.pptx.ShapeType.ellipse,{x:x-g.radius,y:y-g.radius,w:g.radius*2,h:g.radius*2,fill:{color:'FFFFFF',transparency:100},line:{color:c.CYAN,width:1.15}});
 text('顧客が求める価値',2.95,2.23,2.15,.34,16,true,c.NAVY,{align:'center'});
 text('既存業務を変えず、\n在庫確認の手間を減らす',2.92,2.75,2.20,.60,12,false,c.INK,{align:'center'});
 text('自社が提供できる価値',1.20,5.06,2.82,.35,15,true,c.NAVY,{align:'center'});
 text('既存の販売管理との併用\n店舗間の在庫を一画面に集約',1.23,5.55,2.78,.67,12,false,c.INK,{align:'center'});
 text('競合が提供する価値',4.68,5.06,2.71,.35,15,true,c.NAVY,{align:'center'});
 text('表計算による手作業の管理\n販売管理の刷新で業務全体を変更',4.63,5.55,2.84,.67,12,false,c.INK,{align:'center'});
 const anchor={x:3.24,y:3.99};
 line(anchor.x,anchor.y,5.30,0,c.NAVY,1.1);
 s.addShape(ctx.pptx.ShapeType.ellipse,{x:anchor.x-.045,y:anchor.y-.045,w:.09,h:.09,fill:{color:'FFFFFF'},line:{type:'none'}});
 const x=8.85,w=3.85;head('ハイグラウンド候補',x,2.03,w);
 text('既存の販売管理を残せる\n店舗横断の在庫確認',x,2.88,w,.86,19,true,c.NAVY);
 text('顧客が求め、自社が提供でき、\n競合の提供範囲には入らない価値。',x,4.14,w,.63,14);
 line(x,5.02,w);
 text('競合が満たしていないかを検証',x,5.28,w,.38,15,true,c.NAVY);
 text('既存システムとの併用条件を\n競合調査で確認する。\n未確認のため、独自性は仮説とする。',x,5.83,w,.78,13);
 text('濃紺 = 顧客と自社の重なりのうち、競合に含まれない領域',.63,6.52,7.75,.24,10,false,c.MUTED);
}
