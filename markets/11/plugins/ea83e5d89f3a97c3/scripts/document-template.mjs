import{createHash as b}from"node:crypto";const f="action-room-html-v1",w=8*1024*1024,m=e=>String(e).replace(/[&<>"']/g,t=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[t]),i=(e,t)=>{if(!e)throw new Error(t)},n=(e,t,a=!1)=>(i(typeof e=="string"&&(a||e.trim().length>0),`${t} must be text.`),m(e));function y(e){switch(i(e&&typeof e=="object","Document blocks must be objects."),e.type){case"paragraph":return`<p>${n(e.text,"Paragraph")}</p>`;case"heading":return i([2,3].includes(e.level),"Heading level must be 2 or 3."),`<h${e.level}>${n(e.text,"Heading")}</h${e.level}>`;case"quote":return`<blockquote>${n(e.text,"Quote")}</blockquote>`;case"list":{i(Array.isArray(e.items)&&e.items.length>0,"Lists need items.");const t=e.ordered?"ol":"ul";return`<${t}>${e.items.map(a=>`<li>${n(a,"List item")}</li>`).join("")}</${t}>`}case"table":{i(Array.isArray(e.columns)&&e.columns.length>0&&Array.isArray(e.rows),"Tables need columns and rows.");const t=e.columns.map(o=>`<th scope="col">${n(o,"Column")}</th>`).join(""),a=e.rows.map(o=>(i(Array.isArray(o)&&o.length===e.columns.length,"Every table row must preserve all columns."),`<tr>${o.map(r=>`<td>${n(r,"Cell",!0)}</td>`).join("")}</tr>`)).join("");return`<table>${e.caption?`<caption>${n(e.caption,"Caption")}</caption>`:""}<thead><tr>${t}</tr></thead><tbody>${a}</tbody></table>`}case"image":return i(typeof e.src=="string"&&/^data:image\/(?:png|jpeg|webp|gif);base64,[A-Za-z0-9+/]+={0,2}$/.test(e.src),"Embed images as PNG, JPEG, WebP or GIF data URLs."),`<figure><img src="${e.src}" alt="${n(e.alt,"Image description")}">${e.caption?`<figcaption>${n(e.caption,"Caption")}</figcaption>`:""}</figure>`;case"links":return i(Array.isArray(e.items)&&e.items.length>0,"Sources need links."),`<ul class="sources">${e.items.map(t=>{let a;try{a=new URL(t.url)}catch{throw new Error("Sources must use public HTTP(S) URLs.")}return i(["https:","http:"].includes(a.protocol)&&!a.username&&!a.password,"Sources must use public HTTP(S) URLs."),`<li><a href="${m(a.href)}" target="_blank" rel="noopener noreferrer">${n(t.label,"Source label")}</a><span class="source-url">${m(a.href)}</span></li>`}).join("")}</ul>`;default:throw new Error("Unsupported document block. Preserve its content using a supported block.")}}function v(e){i(e&&["document","presentation"].includes(e.layout),"Choose document or presentation layout.");const t=n(e.title,"Document title"),a=e.language??"ko";i(typeof a=="string"&&/^[a-z]{2,3}(?:-[a-z0-9]{2,8})*$/i.test(a),"Use a language tag such as ko or en."),i(Array.isArray(e.sections)&&e.sections.length>0&&e.sections.length<=200,"Provide 1 to 200 sections.");const o=e.layout==="presentation";i(!o||!e.subtitle,"Put presentation subtitles in the first slide so their content is preserved.");const r=a.toLowerCase().startsWith("ko"),h=e.sections.map((s,g)=>{i(Array.isArray(s.blocks)&&s.blocks.length>0,"Every section needs content.");const d=s.heading?n(s.heading,"Section heading"):"";i(!o||d,"Each slide needs a heading.");const c=s.blocks.map(y).join(`
`);return o?`<section class="slide"><header class="slide-header"><span>${t}</span><span>${g+1} / ${e.sections.length}</span></header><h1>${d}</h1><div class="slide-body">${c}</div></section>`:`<section>${d?`<h2>${d}</h2>`:""}${c}</section>`}).join(`
`),l="document.getElementById('print-document').addEventListener('click',()=>window.print());",u=`default-src 'none'; script-src 'sha256-${b("sha256").update(l).digest("base64")}'; style-src 'unsafe-inline'; img-src data:; font-src data:; base-uri 'none'; form-action 'none'`,p=`<!doctype html>
<html lang="${a}" data-action-room-document="${f}" data-action-room-layout="${e.layout}">
<head><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="${u}"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${t}</title>
<style>
@page { size: A4 ${o?"landscape":"portrait"}; margin: ${o?"10mm":"18mm"}; }
* { box-sizing: border-box; }
html { color: #172b3a; background: #edf1f5; font-family: "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans CJK KR", Arial, sans-serif; font-size: 11pt; line-height: 1.65; }
body { margin: 0; }
.toolbar { display: flex; justify-content: space-between; align-items: center; gap: 16px; max-width: 1120px; margin: 20px auto; padding: 0 20px; font-size: 10pt; color: #475569; }
.toolbar button { background: #173e59; color: white; border: 0; border-radius: 6px; padding: 10px 18px; font: inherit; cursor: pointer; }
main { margin: 0 auto 28px; }
.document { width: 210mm; padding: 18mm; background: white; box-shadow: 0 3px 18px #173e5918; }
.document-title { border-bottom: 2px solid #2b6474; padding-bottom: 9mm; margin-bottom: 9mm; }
.document-title h1 { margin-top: 0; }
.subtitle { color: #526674; }
h1, h2, h3 { line-height: 1.35; color: #173e59; overflow-wrap: anywhere; break-after: avoid; page-break-after: avoid; }
h1 { font-size: 25pt; margin: 0 0 7mm; }
h2 { font-size: 17pt; margin: 9mm 0 4mm; }
h3 { font-size: 13pt; margin: 6mm 0 3mm; }
p, li, td, th, blockquote, figcaption { overflow-wrap: anywhere; }
p { white-space: pre-wrap; margin: 0 0 3.5mm; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 5mm; padding-left: 7mm; }
li { margin: 0 0 2mm; }
blockquote { border-left: 3px solid #69909a; margin: 5mm 0; padding: 2mm 5mm; color: #455c6c; white-space: pre-wrap; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; margin: 5mm 0; font-size: 10pt; }
caption { text-align: left; font-weight: 700; padding-bottom: 2mm; }
th, td { border: 1px solid #cad5de; padding: 2.5mm 3mm; text-align: left; vertical-align: top; white-space: pre-wrap; }
th { background: #e9f0f4; color: #173e59; }
thead { display: table-header-group; }
tr { break-inside: avoid; page-break-inside: avoid; }
figure { margin: 5mm 0; break-inside: avoid; }
img { display: block; max-width: 100%; max-height: 210mm; height: auto; margin: auto; object-fit: contain; }
figcaption { margin-top: 2mm; font-size: 9pt; color: #526674; }
a { color: #195c78; }
.source-url { display: block; font-size: 9pt; color: #526674; overflow-wrap: anywhere; }
.deck { width: 277mm; }
.slide { width: 277mm; height: 189mm; padding: 10mm 12mm; margin: 0 0 8mm; background: white; box-shadow: 0 3px 18px #173e5918; break-inside: avoid; break-after: page; page-break-after: always; }
.slide:last-child { break-after: auto; page-break-after: auto; }
.slide-header { display: flex; justify-content: space-between; gap: 8mm; border-bottom: 1px solid #cad5de; padding-bottom: 3mm; margin-bottom: 7mm; font-size: 9pt; color: #526674; }
.slide-header span:first-child { overflow-wrap: anywhere; }
.slide-header span:last-child { white-space: nowrap; }
.slide h1 { font-size: 27pt; margin-bottom: 7mm; }
.slide-body { font-size: 15pt; line-height: 1.55; }
.slide h2 { font-size: 20pt; margin-top: 5mm; }
.slide h3 { font-size: 17pt; }
.slide table { font-size: 12pt; }
.slide img { max-height: 95mm; }
@media screen and (max-width: 820px) { .document { width: 100%; padding: 7vw; } }
@media print {
  html, body { background: white; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .toolbar { display: none !important; }
  main, .document, .deck { width: auto; margin: 0; padding: 0; box-shadow: none; }
  .slide { margin: 0; box-shadow: none; }
  a { color: inherit; text-decoration: none; }
}
</style></head><body>
<div class="toolbar"><span>${o?r?"발표형 · A4 가로":"Presentation · A4 landscape":r?"문서형 · A4 세로":"Document · A4 portrait"}</span><button id="print-document" type="button">${r?"인쇄 / PDF로 저장":"Print / Save as PDF"}</button></div>
<main class="${o?"deck":"document"}">${o?"":`<header class="document-title"><h1>${t}</h1>${e.subtitle?`<p class="subtitle">${n(e.subtitle,"Subtitle")}</p>`:""}</header>`}${h}</main>
<script>${l}<\/script></body></html>
`;return i(Buffer.byteLength(p)<=w,"HTML exceeds 8 MiB. Reduce embedded image sizes or split the deliverable."),p}export{w as DOCUMENT_LIMIT,f as DOCUMENT_VERSION,y as documentBlock,v as renderDocument};
