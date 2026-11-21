"""Derive portable previews from the exact handoff HTML, never a second manuscript.
No network access. Originals are untouched; Pillow is optional for display copies.
"""
from __future__ import annotations
import base64
import hashlib
import html
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
from urllib.parse import unquote

PREVIEW_LIMIT = 32 * 1024 * 1024
FRAGMENT_LIMIT = 900_000  # the inline host contract is strictly below 1 MB
IMAGE_TARGET = 230_000   # a selected image can appear twice in a scene card
VIDEO_LIMIT = 8 * 1024 * 1024
VIDEO_TOTAL_LIMIT = 16 * 1024 * 1024
MIMES = {'.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.webp':'image/webp', '.gif':'image/gif','.avif':'image/avif','.svg':'image/svg+xml','.mp4':'video/mp4','.webm':'video/webm'}
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

def escaped(value):
    return html.escape(str(value), quote=True)

def uri(data, mime):
    return 'data:' + mime + ';base64,' + base64.b64encode(data).decode('ascii')

class Media:
    def __init__(self, output, image_targets=None):
        self.output = output
        self.image_targets = image_targets or {}
        self.images = {}
        self.videos = {}
        self.records = {}
        self.video_bytes = 0

    def image(self, filename):
        if filename in self.images:
            return self.images[filename]
        path = self.output / filename
        data, mime = path.read_bytes(), MIMES[path.suffix.lower()]
        original_size = len(data)
        target = self.image_targets.get(filename, IMAGE_TARGET)
        transformed = False
        # Encoding for display only. Preserve aspect ratio, all pixels and originals;
        # never crop, invent an illustration, alter a label or flatten an animation.
        if len(data) > target and path.suffix.lower() != '.svg':
            try:
                from PIL import Image, ImageOps
                with Image.open(io.BytesIO(data)) as original:
                    if not getattr(original, 'is_animated', False):
                        image = ImageOps.exif_transpose(original).convert('RGBA' if 'A' in original.getbands() else 'RGB')
                        for width, quality in ((1400,85),(1100,80),(900,75),(720,70)):
                            copy = image.copy()
                            copy.thumbnail((width,width), Image.Resampling.LANCZOS)
                            stream = io.BytesIO()
                            copy.save(stream, format='WEBP', quality=quality, method=6)
                            candidate = stream.getvalue()
                            if len(candidate) < len(data):
                                data, mime, transformed = candidate, 'image/webp', True
                            if len(data) <= target:
                                break
            except (ImportError, OSError, ValueError):
                pass  # no silent omission: size/coverage checks below report blockers
        self.images[filename] = uri(data, mime)
        self.records[filename] = {'path':filename,'kind':'image','original_bytes':original_size,'display_bytes':len(data),'display_copy_encoded':transformed,'status':'embedded'}
        return self.images[filename]

    def video(self, filename, inline=False):
        if inline:
            return None
        if filename in self.videos:
            return self.videos[filename]
        path = self.output / filename
        length = path.stat().st_size
        if length > VIDEO_LIMIT or self.video_bytes + length > VIDEO_TOTAL_LIMIT:
            result = None
        else:
            result = uri(path.read_bytes(), MIMES[path.suffix.lower()])
            self.video_bytes += length
        self.videos[filename] = result
        self.records[filename] = {'path':filename,'kind':'video','original_bytes':length,'status':'embedded' if result else 'delivery_only','reason':None if result else 'preview_size_budget','delivery_entry':'script.html','original_unchanged':True}
        return result

class Transform(HTMLParser):
    """Transform only generated markup. Manuscript text passes through untouched."""
    def __init__(self, media, inline=False):
        super().__init__(convert_charrefs=False)
        self.media, self.inline = media, inline
        self.parts, self.stack = [], []
        self.skip_script = False
        self.json_data = False
        self.video_seen = {}

    def tag(self, tag, attrs):
        self.parts.append('<' + tag + ''.join(' '+key if value is None else ' '+key+'="'+escaped(value)+'"' for key,value in attrs) + '>')

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'meta' and values.get('http-equiv','').lower() == 'content-security-policy':
            values['content'] = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; media-src data: blob:; connect-src 'none'; base-uri 'none'; form-action 'none'"
            self.tag(tag, list(values.items())); return
        if tag == 'link' and values.get('rel') == 'stylesheet':
            css = (self.media.output / unquote(values['href'])).read_text(encoding='utf-8')
            self.parts.append('<style>' + css + '</style>'); return
        if tag == 'script' and values.get('src'):
            self.skip_script = True; return
        if tag == 'script' and values.get('id') == 'handoff-data':
            self.json_data = True
        replacement = tag
        if tag == 'body':
            values['data-preview-mode'] = 'standalone'
        if tag == 'img' and values.get('src'):
            values['src'] = self.media.image(unquote(values['src']))
        if tag == 'video' and values.get('src'):
            filename = unquote(values['src'])
            already_shown = self.video_seen.get(filename, False)
            encoded = None if filename in self.video_seen else self.media.video(filename, self.inline)
            self.video_seen[filename] = already_shown or bool(encoded)
            anchor = 'preview-video-' + hashlib.sha256(filename.encode()).hexdigest()[:16]
            poster = values.get('poster')
            if encoded:
                values['src'] = encoded
                values['id'] = anchor
                if poster: values['poster'] = self.media.image(unquote(poster))
            else:
                replacement = 'div'
                values = {'class':'preview-video-delivery','data-delivery-path':filename}
                self.tag(replacement, list(values.items()))
                if poster: self.parts.append('<img src="'+self.media.image(unquote(poster))+'" alt="動画のポスター画像">')
                if already_shown and not self.inline:
                    self.parts.append('<p>同じ実動画はこのページの前方に表示しています。</p><a href="#'+anchor+'">動画の再生位置へ</a><br>')
                else:
                    self.parts.append('<p><strong>実動画は納品一式に同梱</strong></p><p>容量制限のため、この表示では再生しません。ZIP全体を展開し、script.html の同じ素材IDから再生できます。</p>')
                self.parts.append('<code>'+escaped(filename)+'</code>')
                self.stack.append((tag,replacement)); return
        if tag == 'a' and values.get('href'):
            target = unquote(values['href'])
            if target.startswith('script.html#'):
                values['href'] = '#' + target.split('#',1)[1]
            elif target in {'script.html','index.html'}:
                values['href'] = '#start' if target == 'script.html' else '#preview-options'
            elif not target.startswith(('#','https://','http://','mailto:')):
                # A standalone artifact/iframe cannot resolve adjacent delivery files.
                # Keep the name visible; do not expose a broken download button.
                replacement = 'span'
                values = {'class':'delivery-file','data-delivery-path':target,'aria-label':'納品ZIP内のファイル '+target}
        if self.inline and tag in {'input','textarea','button'}:
            values['disabled'] = None
        self.tag(replacement, list(values.items()))
        if tag not in VOID:
            self.stack.append((tag,replacement))

    def handle_endtag(self, tag):
        if tag == 'script' and self.skip_script:
            self.skip_script=False; return
        if tag == 'script': self.json_data=False
        if tag == 'body':
            app = (self.media.output / 'app.js').read_text(encoding='utf-8')
            self.parts.append('<script>'+app+'</script>')
        replacement=tag
        if self.stack:
            original,replacement=self.stack.pop()
            if original != tag: raise ValueError('Generated HTML nesting mismatch: '+tag)
        self.parts.append('</'+replacement+'>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_data(self,data):
        if not self.skip_script: self.parts.append(data)
    def handle_entityref(self,name): self.parts.append('&'+name+';')
    def handle_charref(self,name): self.parts.append('&#'+name+';')
    def handle_decl(self,decl): self.parts.append('<!'+decl+'>')
    def handle_comment(self,data): self.parts.append('<!--'+data+'-->')

class Units(HTMLParser):
    """Top-level manuscript nodes, already rendered by the one source renderer."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth=0; self.parts=[]; self.units=[]
    def handle_starttag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())
        if tag not in VOID: self.depth+=1
        elif self.depth==0: self.flush()
    def handle_endtag(self,tag):
        self.parts.append('</'+tag+'>'); self.depth-=1
        if self.depth==0: self.flush()
    def handle_data(self,data): self.parts.append(data)
    def handle_entityref(self,name): self.parts.append('&'+name+';')
    def handle_charref(self,name): self.parts.append('&#'+name+';')
    def flush(self):
        value=''.join(self.parts)
        if value.strip(): self.units.append(value)
        self.parts=[]

PREVIEW_CSS = '''
.delivery-file{display:inline-block;font-size:12px;overflow-wrap:anywhere;color:var(--muted)}
.preview-banner,.preview-video-delivery,.preview-export{padding:16px;border:1px solid var(--line);border-radius:9px;background:#fff9ef;overflow-wrap:anywhere;margin:12px 0}
.preview-video-delivery img{max-width:100%;max-height:320px;object-fit:contain}.preview-video-delivery p{font-size:13px}.preview-video-delivery code{font-size:12px;white-space:normal}
.preview-export textarea{width:100%;min-height:180px}.preview-options{scroll-margin-top:80px}.preview-fragment .asset-body{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
@media(max-width:680px){.preview-fragment .asset-body{grid-template-columns:1fr}}
'''

def transform(source,media,inline=False):
    parser=Transform(media,inline); parser.feed(source); parser.close()
    return ''.join(parser.parts)

def source_markers(document):
    return {'paragraphs':len(re.findall(r'class="source-text"',document)), 'headings':len(re.findall(r'class="source-heading"',document)), 'scenes':re.findall(r'data-scene="([^"]+)"',document),'digest_sources':re.findall(r'id="digest-source-(\d+)"',document)}

class SourceText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts, self.blocks = [], []
    def handle_starttag(self, tag, attrs):
        if self.depth:
            if tag not in VOID: self.depth += 1
        elif dict(attrs).get('class') in {'source-text','source-heading'}:
            self.depth = 1
            self.parts = []
    def handle_endtag(self,tag):
        if self.depth:
            self.depth -= 1
            if not self.depth: self.blocks.append(''.join(self.parts))
    def handle_data(self,data):
        if self.depth: self.parts.append(data)

def source_text_digest(document):
    parser = SourceText(); parser.feed(document); parser.close()
    value = json.dumps(parser.blocks,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    return hashlib.sha256(value).hexdigest()

def scoped_css(css, root):
    # Generated stylesheet has simple rules/media queries and no animation at-rules.
    def rewrite(match):
        selectors=match.group(1)
        if selectors.lstrip().startswith('@'): return selectors+'{'
        parts=[]
        for value in selectors.split(','):
            value=value.strip()
            if value in {':root','body','html'}: parts.append('#'+root)
            elif value.startswith('.preview-fragment'): parts.append('#'+root+value[len('.preview-fragment'):])
            else: parts.append('#'+root+' '+value)
        return ','.join(parts)+'{'
    return re.sub(r'([^{}]+)\{',rewrite,css)

class CardImageBudgets(HTMLParser):
    """Share the ordinary two-image budget across all images in one scene card.

    A selected still normally occurs twice (adopted visual and option preview).
    A multi-still sequence must not silently block the whole inline manuscript
    just because those same slots now contain several images each. Originals
    and the existing one-still encoding policy are unchanged.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.references = []
        self.targets = {}

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if not self.depth:
            if tag != 'figure' or 'asset-card' not in values.get('class', '').split():
                return
            self.depth = 1
            self.references = []
            return
        if tag not in VOID:
            self.depth += 1
        filename = values.get('src') if tag == 'img' else values.get('poster') if tag == 'video' else None
        if filename:
            self.references.append(unquote(filename))

    def handle_endtag(self, tag):
        if not self.depth:
            return
        self.depth -= 1
        if not self.depth and len(self.references) > 2:
            target = max(1, IMAGE_TARGET * 2 // len(self.references))
            for filename in self.references:
                self.targets[filename] = min(self.targets.get(filename, IMAGE_TARGET), target)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

def card_image_targets(document):
    parser = CardImageBudgets()
    parser.feed(document)
    parser.close()
    return parser.targets

def build_previews(output, source_hash, inline_requested=False):
    output=Path(output)
    original=(output/'script.html').read_text(encoding='utf-8')
    media=Media(output, card_image_targets(original) if inline_requested else None)
    preview=transform(original,media)
    banner='<section class="preview-banner" id="preview-options"><strong>台本全文と素材の確認ページ</strong><p>このページで台本と差し込み素材を続けて確認できます。修正したい箇所は、素材IDや発話を添えて同じチャットにお伝えください。選択・メモの書き出しはコピー欄に表示します。編集用の原寸素材と、このページに収まらない動画は納品ZIPに同梱しています。</p></section>'
    preview=preview.replace('</head>','<style>'+PREVIEW_CSS+'</style></head>').replace('<main>','<main>'+banner,1)
    preview=preview.replace('<h2>このページを上から読んで、編集を始める。</h2>', '<h2>台本と素材を、このページで確認する。</h2>', 1)
    preview=re.sub(r'<ol class="workflow"><li>.*?</li>', '<ol class="workflow"><li><b>台本と素材を見る</b><span>このページをそのまま読み進めてください。確認のためのZIP展開は不要です。</span></li>', preview, count=1, flags=re.S)
    preview=re.sub(r'<p class="folder-note">.*?</p>', '<p class="folder-note">修正は同じチャットから依頼できます。選択を変えただけでは素材や納品ZIPは更新されません。更新後の確認ページで内容を確認してください。編集者は納品ZIPを展開し、フォルダごと保管してください。</p>', preview, count=1, flags=re.S)
    report={'schema_version':1,'generator':'dr-shigyo-preview/1','source_sha256':source_hash,'source_coverage':'complete','content_equivalent_to':'script.html','expected':source_markers(original),'actual':source_markers(preview),'omitted_source_sections':[], 'omitted_images':[], 'native':{}, 'inline':{'status':'not_applicable','reason':'explicit_request_only'}, 'blockers':[]}
    report['expected']['rendered_text_sha256'] = source_text_digest(original)
    report['actual']['rendered_text_sha256'] = source_text_digest(preview)
    report['source_coverage']='complete' if report['expected']==report['actual'] else 'mismatch'
    if report['source_coverage']!='complete': report['blockers'].append('preview_source_coverage_mismatch')
    length=len(preview.encode('utf-8'))
    if length<=PREVIEW_LIMIT:
        (output/'preview.html').write_text(preview,encoding='utf-8')
        report['native']={'path':'preview.html','status':'generated','bytes':length,'limit_bytes':PREVIEW_LIMIT,'self_contained':True,'browser_verified':False}
    else:
        report['native']={'status':'blocked_size','bytes':length,'limit_bytes':PREVIEW_LIMIT,'self_contained':False}
        report['blockers'].append('native_preview_size_exceeded')
    # This is a prepared source, not evidence of publication, access control,
    # browser rendering or playback. The active Sites workflow owns delivery.
    report['delivery']={'route':'private_sites','required_visibility':'private','entrypoint':'preview.html' if report['native']['status']=='generated' else 'script.html','inline_requested':inline_requested}
    if inline_requested:
        build_inline(output, original, media, source_hash, report)
    report['media']=list(media.records.values())
    report['host_verification']={'native_opened':False,'inline_rendered':False,'video_playback_verified':False}
    (output/'preview-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return report


def build_inline(output, original, media, source_hash, report):
    """Optional chat fragments, generated only after an explicit user request."""
    # Every fragment includes consecutive source units and the same scene cards.
    # No image gallery or source excerpt is allowed to stand in for the full set.
    inline_document=transform(original,media,inline=True)
    manuscript=re.search(r'<article class="manuscript">(.*?)</article>',inline_document,re.S)
    parser=Units(); parser.feed(manuscript.group(1)); parser.close(); parser.flush()
    css=(output/'style.css').read_text(encoding='utf-8')+(output/'theme.css').read_text(encoding='utf-8')+PREVIEW_CSS
    # Keep native details for alternatives. Edit controls are disabled in fragments:
    # the complete standalone preview owns selections and export state.
    css+=' .preview-fragment .memo-label,.preview-fragment .scene-memo,.preview-fragment .none-option{display:none}.preview-fragment{background:var(--background);color:var(--ink);font-family:system-ui,sans-serif;line-height:1.8;padding:14px;overflow-wrap:anywhere}.preview-fragment .source-text{white-space:pre-wrap}'
    prefix=[]
    for section in ('<section class="summary">', '<section class="guide" id="start">', '<section class="guide quality-summary">', '<section class="digest-box" id="digest">'):
        found=re.search(re.escape(section)+r'.*?</section>',inline_document,re.S)
        if found: prefix.append(found.group(0))
    suffix=[]
    closing=re.search(r'<section class="guide closing">.*?</section>',inline_document,re.S)
    if closing: suffix.append(closing.group(0))
    footer=re.search(r'<footer>.*?</footer>',inline_document,re.S)
    if footer: suffix.append(footer.group(0))
    groups=[]; current=[]
    overhead=len(css.encode('utf-8'))*2+2000
    for unit in prefix + parser.units + suffix:
        if len(unit.encode('utf-8'))+overhead>FRAGMENT_LIMIT:
            report['blockers'].append('inline_unit_size_exceeded')
            report['inline']={'status':'blocked_size','oversized_unit_bytes':len(unit.encode('utf-8')),'limit_bytes':FRAGMENT_LIMIT,'omitted_source_sections':[],'requires_native_full_preview':True}
            groups=[]; break
        if current and len(''.join(current+[unit]).encode('utf-8'))+overhead>FRAGMENT_LIMIT:
            groups.append(current); current=[]
        current.append(unit)
    else:
        if current: groups.append(current)
    if groups:
        folder=output/'preview-parts'; folder.mkdir()
        fragments=[]
        for index, group in enumerate(groups,1):
            root='handoff-preview-'+source_hash[:10]+'-'+str(index)
            style=scoped_css(css,root)
            content=''.join(group)
            fragment='<style>'+style+'</style><div id="'+root+'" class="preview-fragment" data-source-sha256="'+source_hash+'"><p>台本と素材 '+str(index)+' / '+str(len(groups))+'</p>'+content+'</div>\n'
            # Internal anchors never navigate to an absent paragraph in another part.
            local_ids=set(re.findall(r'id="([^"]+)"',fragment))
            fragment=re.sub(r'<a href="#([^"]+)"([^>]*)>(.*?)</a>',lambda m:m.group(0) if m.group(1) in local_ids else '<span>'+m.group(3)+'</span>',fragment,flags=re.S)
            size=len(fragment.encode('utf-8'))
            if size>FRAGMENT_LIMIT: raise ValueError('Preview fragment unexpectedly exceeds its byte budget')
            path=f'preview-parts/part-{index:03d}.html'
            (output/path).write_text(fragment,encoding='utf-8')
            fragments.append({'path':path,'bytes':size,**source_markers(fragment)})
        inline_hash=source_text_digest(''.join(''.join(group) for group in groups))
        inline_complete=inline_hash == report['expected']['rendered_text_sha256']
        if not inline_complete: report['blockers'].append('inline_source_coverage_mismatch')
        report['inline']={'rendered_text_sha256':inline_hash,'status':'generated','limit_bytes':FRAGMENT_LIMIT,'fragments':fragments,'all_parts_required':True,'source_coverage':'complete' if inline_complete else 'mismatch','video_policy':'delivery_only','editing_controls':'disabled_use_standalone','host_render_verified':False}

