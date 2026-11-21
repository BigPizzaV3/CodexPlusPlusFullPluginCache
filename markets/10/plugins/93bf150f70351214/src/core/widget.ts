// Shared card widget (Apps SDK skybridge). Renders structuredContent.card; no external resources, no network.
export function widgetHtml(accent: string): string {
  const safeAccent = /^#[0-9a-fA-F]{6}$/.test(accent) ? accent : '#b4532a'
  return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--a:${safeAccent};--bg:#fff;--fg:#1c1917;--mu:#78716c;--ln:#e7e5e4;--ch:#f5f5f4}
.dark{--bg:#1c1917;--fg:#fafaf9;--mu:#a8a29e;--ln:#44403c;--ch:#292524}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--fg)}
.c{padding:16px}.t{font-size:17px;font-weight:650;margin:0}.s{color:var(--mu);margin:2px 0 10px}
.h{border-left:3px solid var(--a);padding:6px 10px;margin:8px 0 12px;background:var(--ch);border-radius:6px}.h b{display:block;font-size:20px}
.r{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid var(--ln)}.r span:first-child{color:var(--mu)}.r span:last-child{text-align:right;font-weight:550}
.sh{margin:14px 0 4px;font-weight:650;font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--mu)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}.chip{background:var(--ch);border:1px solid var(--ln);border-radius:999px;padding:3px 10px}
table{width:100%;border-collapse:collapse;margin:8px 0;font-size:13px}th,td{text-align:left;padding:5px 6px;border-bottom:1px solid var(--ln)}th{color:var(--mu);font-weight:600}
.n{color:var(--mu);font-size:12px;margin-top:10px}.l{display:inline-block;margin-top:12px;color:var(--a);font-weight:600;text-decoration:none;cursor:pointer}
</style></head><body><div class="c" id="root"></div>
<script>
(function(){
  var root=document.getElementById('root');
  function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=String(text);return e}
  function rows(parent,list){(list||[]).forEach(function(r){var d=el('div','r');d.appendChild(el('span',null,r[0]));d.appendChild(el('span',null,r[1]));parent.appendChild(d)})}
  function render(){
    var o=(window.openai&&window.openai.toolOutput)||{};var c=o.card;
    if(window.openai&&window.openai.theme==='dark')document.body.className='dark';
    root.textContent='';
    if(!c){root.appendChild(el('div','s','Loading...'));return}
    root.appendChild(el('h1','t',c.title));
    if(c.subtitle)root.appendChild(el('p','s',c.subtitle));
    if(c.highlight){var h=el('div','h');h.appendChild(el('span',null,c.highlight.label));h.appendChild(el('b',null,c.highlight.value));root.appendChild(h)}
    rows(root,c.rows);
    (c.sections||[]).forEach(function(s){root.appendChild(el('div','sh',s.heading));rows(root,s.rows)});
    if(c.chips&&c.chips.length){var w=el('div','chips');c.chips.forEach(function(x){w.appendChild(el('span','chip',x))});root.appendChild(w)}
    if(c.table){var t=el('table'),tr=el('tr');c.table.columns.forEach(function(x){tr.appendChild(el('th',null,x))});t.appendChild(tr);c.table.rows.forEach(function(r){var row=el('tr');r.forEach(function(x){row.appendChild(el('td',null,x))});t.appendChild(row)});root.appendChild(t)}
    if(c.note)root.appendChild(el('div','n',c.note));
    if(c.link&&/^https:\\/\\//.test(c.link.url)){var a=el('a','l',c.link.label+' \\u2192');a.href=c.link.url;a.target='_blank';a.rel='noopener';
      a.addEventListener('click',function(ev){if(window.openai&&window.openai.openExternal){ev.preventDefault();window.openai.openExternal({href:c.link.url})}});root.appendChild(a)}
  }
  window.addEventListener('openai:set_globals',render);render();
})();
</script></body></html>`
}
