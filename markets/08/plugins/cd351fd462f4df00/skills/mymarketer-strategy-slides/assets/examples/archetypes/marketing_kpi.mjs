import {helpers} from './_marketing.mjs';
export const id='marketing_kpi';
export function pptx(ctx,item,pageNum){
 const {s,text,line,head,c}=helpers(ctx,item,pageNum);
 head('30日間の目標と、その内訳',.63,2.03,7.68);
 // A multiplicative tree, with factors grouped by connector spines.
 const root={x:.63,y:4.0,w:1.75,h:1.12};
 s.addShape(ctx.pptx.ShapeType.rect,{...root,fill:{color:c.NAVY},line:{type:'none'}});
 text('有効相談申込数',.79,4.15,1.43,.27,13,true,'FFFFFF');
 text('10 件',.79,4.56,1.43,.40,24,true,'FFFFFF');
 function metric(label,value,x,y,w){text(label,x,y,w,.34,13,true,c.NAVY);text(value,x,y+.43,w,.45,23,true,c.NAVY);line(x,y+.99,w,0,c.HAIR,.8);}
 metric('相談申込数','20 件',3.09,3.04,1.77);
 metric('有効申込率','50 %',3.09,5.18,1.77);
 metric('広告経由の訪問数','1,000 件',5.68,2.74,2.30);
 metric('相談申込率','2 %',5.68,4.24,2.30);
 // output = applications x qualification rate
 line(2.38,4.56,.34,0,c.CYAN,1.4);
 line(2.72,3.55,0,2.14,c.CYAN,1.4);
 line(2.72,3.55,.25,0,c.CYAN,1.4);line(2.72,5.69,.25,0,c.CYAN,1.4);
 text('×',2.85,4.48,.29,.34,20,true,c.MUTED);
 // applications = visits x application rate
 line(4.86,3.55,.36,0,c.CYAN,1.4);
 line(5.22,3.25,0,1.50,c.CYAN,1.4);
 line(5.22,3.25,.33,0,c.CYAN,1.4);line(5.22,4.75,.33,0,c.CYAN,1.4);
 text('×',5.30,3.91,.29,.34,20,true,c.MUTED);
 text('20件 ÷ 1,000件',5.68,5.38,2.30,.32,12,false,c.MUTED);
 text('有効申込率 = 有効相談申込数 ÷ 相談申込数',.63,6.43,7.68,.27,11,false,c.MUTED);
 const x=8.86,w=3.84;head('申込数と対象条件を確認する',x,2.03,w);
 text('有効申込の定義',x,2.85,w,.3,15,true,c.NAVY);
 text('複数店舗の在庫確認に課題があり、\n販売管理を継続したい企業の申込が対象。\n申込時点で判定し、\n重複・対象外の申込は除く。',x,3.30,w,1.05,13);
 line(x,4.47,w);
 text('費用の条件',x,4.75,w,.3,15,true,c.NAVY);
 text('広告費30万円 ÷ 10件\n= 有効申込1件あたり3万円',x,5.20,w,.83,17,true,c.NAVY);
 text('10件以上・3万円以下を継続判断の目安にする。',x,6.20,w,.48,12);
}
