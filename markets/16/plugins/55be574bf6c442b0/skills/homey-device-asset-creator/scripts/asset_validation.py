"""Strict structural checks. Product fidelity and background interiors need visual review."""
from pathlib import Path
import importlib.util
import math
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops
from make_png_sizes import SIZES, square_on_white

SVG_NS = 'http://www.w3.org/2000/svg'
TAGS = {'svg','g','path','circle','ellipse','rect','line','polyline','polygon','title','desc'}
PAINT = {'#000','#000000','black','none'}
STYLE = {'fill','stroke','stroke-width','stroke-linecap','stroke-linejoin','stroke-miterlimit','stroke-dasharray','stroke-dashoffset','fill-rule','clip-rule','opacity','fill-opacity','stroke-opacity','color'}
ATTRS = STYLE | {'viewBox','d','cx','cy','r','rx','ry','x','y','x1','x2','y1','y2','width','height','points','transform','id','version','style','preserveAspectRatio','role','aria-label'}

def validate_pngs(root, master=None):
    errors = []
    expected = None
    if master:
        with Image.open(master) as im:
            expected = square_on_white(im)
    for name,size in SIZES.items():
        try:
            with Image.open(root/name) as im:
                im.load()
                if im.format != 'PNG' or im.size != (size,size):
                    errors.append(f'{name}: require PNG at {size}x{size}')
                    continue
                rgba = im.convert('RGBA')
                if rgba.getchannel('A').getextrema() != (255,255):
                    errors.append(f'{name}: require fully opaque white canvas')
                rgb = rgba.convert('RGB')
                borders = [rgb.crop((0,0,size,1)),rgb.crop((0,size-1,size,size)),rgb.crop((0,0,1,size)),rgb.crop((size-1,0,size,size))]
                if any(b.getextrema() != ((255,255),)*3 for b in borders):
                    errors.append(f'{name}: entire outer border must be pure white')
                if rgb.getextrema() == ((255,255),)*3:
                    errors.append(f'{name}: image is empty')
                if expected is not None and ImageChops.difference(rgb,expected.resize((size,size),Image.Resampling.LANCZOS)).getbbox():
                    errors.append(f'{name}: does not match supplied master')
        except (OSError,ValueError) as e:
            errors.append(f'{name}: {e}')
    return errors

def validate_svg(path):
    errors = []
    try:
        raw = path.read_text(encoding='utf-8')
        if re.search(r'<!\s*(DOCTYPE|ENTITY)|data:|url\s*\(',raw,re.I):
            return ['SVG: external declarations, data payloads and paint URLs are forbidden']
        svg = ET.fromstring(raw)
    except (OSError,ValueError,ET.ParseError) as e:
        return [f'SVG: {e}']
    if svg.tag != '{'+SVG_NS+'}svg':
        errors.append('SVG: root must use the SVG namespace')
    try:
        vb = [float(x) for x in re.split(r'[\s,]+',svg.get('viewBox','').strip())]
    except ValueError:
        vb = []
    if vb != [0,0,960,960]:
        errors.append('SVG: require viewBox="0 0 960 960"')
    if 'width' in svg.attrib or 'height' in svg.attrib:
        errors.append('SVG: omit fixed root width and height')
    has_geometry = False
    for el in svg.iter():
        tag = el.tag.removeprefix('{'+SVG_NS+'}')
        if tag not in TAGS:
            errors.append(f'SVG: unsupported element {tag}')
        has_geometry |= tag in TAGS-{'svg','g','title','desc'}
        attrs = dict(el.attrib)
        for declaration in attrs.pop('style','').split(';'):
            if not declaration.strip():
                continue
            if ':' not in declaration:
                errors.append('SVG: malformed inline style')
                continue
            key,value = (s.strip() for s in declaration.split(':',1))
            if key not in STYLE:
                errors.append(f'SVG: unsupported style {key}')
            attrs[key] = value
        for key,value in attrs.items():
            if key not in ATTRS:
                errors.append(f'SVG: unsupported attribute {key}')
            if key in {'fill','stroke','color'} and value.strip().lower() not in PAINT:
                errors.append(f'SVG: {key} must be black or none')
            if key in {'opacity','fill-opacity','stroke-opacity'}:
                try:
                    if float(value) != 1:
                        errors.append('SVG: partial opacity is forbidden')
                except ValueError:
                    errors.append('SVG: invalid opacity')
            if key == 'stroke-width':
                try:
                    if not math.isfinite(float(value)) or float(value) <= 0:
                        errors.append('SVG: stroke-width must be finite and positive')
                except ValueError:
                    errors.append('SVG: use numeric stroke-width')
    if not has_geometry:
        errors.append('SVG: no vector geometry')
    return errors

def render_svg(path,output):
    output.mkdir(parents=True,exist_ok=True)
    errors = []
    inkscape = shutil.which('inkscape')
    cairo = importlib.util.find_spec('cairosvg')
    if not inkscape and not cairo:
        return ['SVG: rendering requires Inkscape or CairoSVG; render check was not performed']
    for size in (32,48,64,128,256):
        dest = output/f'icon-{size}.png'
        try:
            if inkscape:
                subprocess.run([inkscape,str(path),'--export-type=png',f'--export-filename={dest}',f'--export-width={size}',f'--export-height={size}','--export-background-opacity=0'],check=True,capture_output=True,timeout=30)
            else:
                import cairosvg
                cairosvg.svg2png(url=str(path),write_to=str(dest),output_width=size,output_height=size)
            with Image.open(dest) as im:
                rgba = im.convert('RGBA')
                bbox = rgba.getchannel('A').getbbox()
                if not bbox:
                    errors.append(f'SVG: empty render at {size}px')
                elif bbox[0] == 0 or bbox[1] == 0 or bbox[2] == size or bbox[3] == size:
                    errors.append(f'SVG: artwork reaches canvas edge at {size}px')
                if any(rgba.getpixel(p)[3] for p in [(0,0),(size-1,0),(0,size-1),(size-1,size-1)]):
                    errors.append(f'SVG: opaque background at {size}px')
        except (OSError,subprocess.SubprocessError) as e:
            errors.append(f'SVG: render failed at {size}px: {e}')
    return errors

def validate(root,master=None,render_dir=None):
    errors = validate_pngs(root,master)
    svg_errors = validate_svg(root/'icon.svg')
    errors += svg_errors
    if render_dir is not None and not svg_errors:
        errors += render_svg(root/'icon.svg',render_dir)
    return errors
