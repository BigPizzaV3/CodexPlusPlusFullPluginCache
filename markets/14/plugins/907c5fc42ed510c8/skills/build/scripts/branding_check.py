"""Stdlib checks for this package's RGB/RGBA PNG assets, not OpenAI's importer.

Scope is deliberately the exported 8-bit, non-interlaced PNGs that Build_ ships.
This verifies structure, checksums and bounded scanline decompression; independent
release validation also decodes the files with an image library.
"""
from __future__ import annotations
import struct
import zlib
from pathlib import Path

PNG = b'\x89PNG\r\n\x1a\n'
MAX_IMAGE_BYTES = 5 * 1024 * 1024
ICON_FIELDS = ('composerIcon', 'composerIconDark', 'logo', 'logoDark')
ICON_PATHS = {'composerIcon': './assets/icon.png', 'composerIconDark': './assets/icon-dark.png', 'logo': './assets/logo.png', 'logoDark': './assets/logo-dark.png'}


def png_info(raw: bytes) -> dict:
    if len(raw) > MAX_IMAGE_BYTES or not raw.startswith(PNG):
        raise ValueError('Unsupported or oversized PNG.')
    pos, header, ended, idat_closed = 8, None, False, False
    compressed = bytearray()
    while pos < len(raw):
        if len(raw) - pos < 12:
            raise ValueError('Truncated PNG chunk.')
        length = struct.unpack('>I', raw[pos:pos+4])[0]
        tag = raw[pos+4:pos+8]
        end = pos + 12 + length
        if end > len(raw):
            raise ValueError('PNG chunk exceeds file.')
        data = raw[pos+8:pos+8+length]
        crc = struct.unpack('>I', raw[pos+8+length:end])[0]
        if zlib.crc32(tag + data) & 0xffffffff != crc:
            raise ValueError('PNG checksum mismatch.')
        if header is None and tag != b'IHDR':
            raise ValueError('PNG must start with IHDR.')
        if tag == b'IHDR':
            if header is not None or length != 13:
                raise ValueError('Invalid PNG header.')
            w, h, depth, colour, method, filtering, interlace = struct.unpack('>IIBBBBB',data)
            if w != h or not 48 <= w <= 4096:
                raise ValueError('Icon must be square, between 48 and 4096 pixels.')
            if (depth, method, filtering, interlace) != (8,0,0,0) or colour not in (2,6):
                raise ValueError('Build_ exports must be 8-bit non-interlaced RGB/RGBA.')
            header = (w,h,colour)
        elif tag == b'IDAT':
            if idat_closed:
                raise ValueError('PNG IDAT chunks must be consecutive.')
            compressed.extend(data)
        elif tag == b'IEND':
            if length or not compressed or end != len(raw):
                raise ValueError('Invalid PNG end or trailing data.')
            ended = True
            pos = end
            break
        else:
            if compressed:
                idat_closed = True
            if not (tag[0] & 32):
                raise ValueError('Unsupported critical PNG chunk.')
        pos = end
    if not header or not ended:
        raise ValueError('Incomplete PNG.')
    w,h,colour = header
    stride = 1+w*(3 if colour==2 else 4)
    expected = h*stride
    try:
        decoder = zlib.decompressobj()
        decoded = decoder.decompress(compressed, expected+1)
    except zlib.error as exc:
        raise ValueError('Invalid PNG compressed image data.') from exc
    if len(decoded) != expected or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
        raise ValueError('Invalid PNG scanline size or compressed stream.')
    if any(decoded[y*stride] > 4 for y in range(h)):
        raise ValueError('Invalid PNG row filter.')
    return {'width':w,'height':h,'mode':'RGB' if colour==2 else 'RGBA','bytes':len(raw),
            'structure_crc_and_decompression':'passed'}


def validate_branding_contract(root: Path, manifest: dict) -> dict:
    ui = manifest.get('interface',{})
    assets = {}
    for field in ICON_FIELDS:
        ref = ui.get(field)
        if ref != ICON_PATHS[field]:
            raise ValueError('All listing/composer theme variants must use the approved symbol: '+field)
        p = root / ref
        if p.is_symlink() or not p.is_file():
            raise ValueError('Missing or unsafe branding file.')
        info = png_info(p.read_bytes())
        if (info['width'],info['height']) != (1254,1254):
            raise ValueError('Expected the installed 1254-pixel symbol export.')
        assets[field] = {**info,'path':ref}
    wordmark = root/'assets/build-wordmark.png'
    if wordmark.is_symlink() or not wordmark.is_file():
        raise ValueError('Missing full-wordmark asset.')
    wordmark_info = png_info(wordmark.read_bytes())
    if {p.name for p in (root/'assets').iterdir()} != {Path(ref).name for ref in ICON_PATHS.values()} | {'build-wordmark.png'}:
        raise ValueError('Unexpected or obsolete branding asset.')
    return {'fields':assets,'wordmark':wordmark_info,'host_rendering':'not_tested',
            'automatic_account_update_claimed':False}
