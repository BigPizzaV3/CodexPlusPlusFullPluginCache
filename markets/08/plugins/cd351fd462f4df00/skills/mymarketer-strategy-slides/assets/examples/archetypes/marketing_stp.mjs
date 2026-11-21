import {helpers} from './_marketing.mjs';
export const id='marketing_stp';
export function pptx(ctx,item,pageNum){
 const {s,text,line,head,c}=helpers(ctx,item,pageNum);
 head('S → T｜顧客を絞る条件',.63,2.03,7.65);
 text('小売企業',.63,4.10,1.52,.36,18,true,c.NAVY);
 text('店舗数で分ける',.63,4.61,1.55,.29,11,false,c.MUTED);
 line(2.05,4.45,.40,0,c.CYAN,1.4);line(2.45,3.24,0,2.12,c.CYAN,1.4);
 line(2.45,3.24,.37,0,c.CYAN,1.4);line(2.45,5.36,.37,0,c.CYAN,1.4);
 text('単店舗',2.93,2.99,1.60,.34,17,true,c.NAVY);
 text('店舗間の課題がない\n今回は優先しない',2.93,3.49,1.79,.65,12,false,c.MUTED);
 text('複数店舗',2.93,5.10,1.70,.35,17,true,c.NAVY);
 text('既存システムの\n継続意向で分ける',2.93,5.60,1.80,.65,12,false,c.MUTED);
 line(4.67,5.36,.33,0,c.CYAN,1.4);line(5.0,4.20,0,1.77,c.CYAN,1.4);
 line(5.0,4.20,.30,0,c.CYAN,1.4);line(5.0,5.97,.30,0,c.CYAN,1.4);
 s.addShape(ctx.pptx.ShapeType.rect,{x:5.30,y:3.64,w:2.98,h:1.50,fill:{color:c.NAVY},line:{type:'none'}});
 text('優先する対象',5.49,3.81,2.60,.27,12,true,'FFFFFF');
 text('既存の販売管理を継続',5.49,4.23,2.60,.37,15,true,'FFFFFF');
 text('店舗間の在庫確認に課題がある',5.49,4.76,2.60,.27,11,false,'FFFFFF');
 text('販売管理を刷新',5.49,5.70,2.60,.35,16,true,c.NAVY);
 text('業務全体の見直しは別の提案へ',5.49,6.23,2.65,.29,11,false,c.MUTED);
 const x=8.85,w=3.85;head('P｜顧客に選ばれる理由',x,2.03,w);
 text('販売管理を入れ替えず、\n店舗間の在庫を\n一画面で確認できる',x,2.91,w,1.32,19,true,c.NAVY);
 line(x,4.64,w);
 text('本部運営担当者へ訴求する',x,4.92,w,.37,15,true,c.NAVY);
 text('既存業務を続けながら、\n各店へ連絡する手間を減らしたい\n担当者に提案する。',x,5.48,w,.90,14);
 text('濃紺 = 今回の優先対象',.63,6.52,7.65,.24,10,false,c.MUTED);
}
