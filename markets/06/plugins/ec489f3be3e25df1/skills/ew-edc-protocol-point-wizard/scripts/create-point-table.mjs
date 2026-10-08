import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';
const require=createRequire(import.meta.url);
const core=require('../references/core.cjs');
const [input,output]=process.argv.slice(2);
if(!input||!output)throw Error('Usage: node create-point-table.mjs plan.json output.xlsx');
const plan=JSON.parse(await fs.readFile(input,'utf8'));
const rows=core.toRows(plan);
const wb=Workbook.create(),sheet=wb.worksheets.add('部署點表');
sheet.getRangeByIndexes(0,0,rows.length,23).values=rows;
sheet.getRangeByIndexes(0,0,rows.length,23).format.font={name:'Arial',size:11};
sheet.getRange('A1:W1').format={fill:'#173047',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:34};
sheet.getRangeByIndexes(1,0,Math.max(1,rows.length-1),23).format.font.color='#174F87';
sheet.getRangeByIndexes(1,0,Math.max(1,rows.length-1),23).format.wrapText=true;
sheet.getRangeByIndexes(1,0,Math.max(1,rows.length-1),23).format.rowHeight=54;
sheet.getRange('A:W').format.columnWidth=18;
sheet.getRange('A:A').format.columnWidth=28;
sheet.getRange('G:G').format.columnWidth=25;
sheet.getRange('M:N').format.columnWidth=26;
sheet.getRange('T:T').format.columnWidth=48;
sheet.getRange('A1:W1').format.wrapText=true;
sheet.freezePanes.freezeRows(1);
sheet.showGridLines=true;
const notes=wb.worksheets.add('使用說明');
notes.getRange('A1:B11').values=[
 ['EW EDC Protocol Mapper','EdgeAI Data Core AI通訊基座'],
 ['用途','填寫部署點表，上傳至 EDC Protocol Mapper，預覽並確認新增。'],
 ['範本示範','示範資料不代表任何真實設備。已確認=否時會阻擋部署。'],
 ['位址基準','protocol-zero-based；將手冊位址換算為零起算協定位址並保留手冊原值。'],
 ['支援功能碼','3（FC03）或 4（FC04），僅讀取。'],
 ['資料型態','int16 / uint16 / int32 / uint32 / float32 / float64'],
 ['換算公式','工程值 = 倍率 × 原始值 + 偏移量；填一組範例驗算。'],
 ['缺漏資料','不猜測；補齊 IP、站號、位元組順序、單位、來源及已確認欄位。'],
 ['Excel 格式','工作表名與第一列欄位名稱不可變更；使用值，不使用公式或巨集。'],
 ['部署結果','設定讀回成功不等於資料擷取成功；仍需核對新採樣與本次歷史資料。'],
 ['官方網站','https://www.embodiedworker.com']
 ];
notes.getRange('A1:B11').format.font={name:'Arial',size:11};
notes.getRange('A:A').format.columnWidth=36;
notes.getRange('B:B').format.columnWidth=88;
notes.getRange('A1:B11').format.wrapText=true;
notes.getRange('A1:B11').format.rowHeight=36;
notes.getRange('A1:B1').format.font.bold=true;
console.log((await wb.inspect({kind:'table',range:'部署點表!A1:W2',include:'values',tableMaxRows:2,tableMaxCols:23,maxChars:1800})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!',options:{useRegex:true,maxResults:10}})).ndjson);
for(const [name,range] of [['部署點表','A1:H3'],['使用說明','A1:B11']]){
 const image=await wb.render({sheetName:name,range,scale:1.5,format:'png'});
 await fs.writeFile(output+'.'+name+'.png',new Uint8Array(await image.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(wb)).save(output);
console.log(output);
