// Prototype extension of the consulting engine; uses its shared shell and brand.
export function helpers(ctx, item, pageNum) {
 const s=ctx.addShell(item,pageNum,{balance:false});
 const c=ctx.colors;
 const text=(t,x,y,w,h,size=14,bold=false,color=c.INK,extra={})=>s.addText(t,{x,y,w,h,fontFace:ctx.FONT,fontSize:size,bold,color,margin:0,breakLine:false,fit:'none',valign:'top',...extra});
 const line=(x,y,w,h=0,color=c.HAIR,width=.7)=>s.addShape(ctx.pptx.ShapeType.line,{x,y,w,h,line:{color,width}});
 const head=(t,x,y,w)=>{text(t,x,y+.14,w,.34,15,true,c.NAVY);line(x,y+.54,w,0,c.NAVY,1.5);};
 const none={type:'none',pt:0,color:'FFFFFF'};
 function table(headers, rows, widths, x,y,rowHeights,fs=14){
  const data=[headers,...rows].map((r,ri)=>r.map((v,ci)=>({text:v,options:{fontFace:ctx.FONT,fontSize:ri===0?fs+2:ci===0?fs+1:fs,bold:ri===0||ci===0,color:ri===0||ci===0?c.NAVY:c.INK,margin:[.14,.14,.14,.1],valign:'middle',border:[none,none,ri===rows.length?none:{type:'solid',pt:ri===0?1.5:.6,color:ri===0?c.NAVY:c.HAIR},none]}})));
  s.addTable(data,{x,y,w:widths.reduce((a,b)=>a+b,0),colW:widths,rowH:rowHeights,fontFace:ctx.FONT,fontSize:fs,autoPage:false,margin:0});
 }
 return {s,c,text,line,head,table};
}
