#!/usr/bin/env python3
"""Deterministically normalize common 8-bit PNGs to the public RGBA subset."""

from __future__ import annotations

import argparse
import struct
import sys
import zlib
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


class NormalizationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise NormalizationError(message)


def chunk(kind: bytes, payload: bytes) -> bytes:
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)


def paeth(left: int, above: int, upper_left: int) -> int:
    estimate = left + above - upper_left
    distances = (abs(estimate - left), abs(estimate - above), abs(estimate - upper_left))
    return (left, above, upper_left)[distances.index(min(distances))]


def decode_rows(data: bytes) -> tuple[int, int, int, list[bytes], bytes | None, bytes | None]:
    require(data.startswith(PNG_SIGNATURE), "input is not a PNG")
    offset = len(PNG_SIGNATURE)
    width = height = bit_depth = color_type = interlace = None
    compressed: list[bytes] = []
    palette = transparency = None
    saw_iend = False
    while offset < len(data):
        require(offset + 12 <= len(data), "truncated PNG chunk")
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 12 + length
        require(end <= len(data), "truncated PNG payload")
        payload = data[offset + 8:offset + 8 + length]
        declared_crc = struct.unpack(">I", data[offset + 8 + length:end])[0]
        require(declared_crc == zlib.crc32(kind + payload) & 0xFFFFFFFF, "PNG CRC mismatch")
        if kind == b"IHDR":
            require(width is None and length == 13, "PNG IHDR is invalid")
            width, height = struct.unpack(">II", payload[:8])
            bit_depth, color_type, compression, filter_method, interlace = payload[8:13]
            require(width > 0 and height > 0, "PNG dimensions must be positive")
            require(compression == 0 and filter_method == 0, "unsupported PNG compression/filter method")
        elif kind == b"PLTE":
            palette = payload
        elif kind == b"tRNS":
            transparency = payload
        elif kind == b"IDAT":
            compressed.append(payload)
        elif kind == b"IEND":
            require(length == 0 and end == len(data), "PNG IEND is invalid")
            saw_iend = True
            break
        elif kind and kind[0] & 0x20 == 0:
            raise NormalizationError(f"unsupported critical PNG chunk {kind.decode('ascii', errors='replace')}")
        offset = end
    require(saw_iend and width is not None and compressed, "PNG structure is incomplete")
    require(bit_depth == 8 and color_type in {0, 2, 3, 4, 6} and interlace == 0,
            "normalizer supports non-interlaced 8-bit grayscale/RGB/indexed/GA/RGBA PNG input")
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[color_type]
    stride = width * channels
    try:
        raw = zlib.decompress(b"".join(compressed))
    except zlib.error as exc:
        raise NormalizationError(f"PNG IDAT cannot be decoded: {exc}") from exc
    require(len(raw) == height * (stride + 1), "PNG decoded scanline length is invalid")
    rows: list[bytes] = []
    prior = bytes(stride)
    cursor = 0
    for _ in range(height):
        filter_type = raw[cursor]
        require(filter_type <= 4, "PNG scanline filter is invalid")
        encoded = raw[cursor + 1:cursor + 1 + stride]
        cursor += stride + 1
        decoded = bytearray(stride)
        for index, byte in enumerate(encoded):
            left = decoded[index - channels] if index >= channels else 0
            above = prior[index]
            upper_left = prior[index - channels] if index >= channels else 0
            predictors = (0, left, above, (left + above) // 2, paeth(left, above, upper_left))
            decoded[index] = (byte + predictors[filter_type]) & 0xFF
        prior = bytes(decoded)
        rows.append(prior)
    return width, height, color_type, rows, palette, transparency


def rgba_rows(
    width: int,
    color_type: int,
    rows: list[bytes],
    palette: bytes | None,
    transparency: bytes | None,
) -> list[bytes]:
    output: list[bytes] = []
    require(transparency is None or color_type in {0, 2, 3}, "tRNS is invalid for an alpha PNG")
    palette_entries = []
    if color_type == 3:
        require(palette is not None and len(palette) % 3 == 0 and 3 <= len(palette) <= 768,
                "indexed PNG requires a valid PLTE")
        palette_entries = [tuple(palette[index:index + 3]) for index in range(0, len(palette), 3)]
    if color_type == 0:
        require(transparency is None or len(transparency) == 2, "grayscale tRNS length is invalid")
    if color_type == 2:
        require(transparency is None or len(transparency) == 6, "RGB tRNS length is invalid")
    if color_type == 3:
        require(transparency is None or len(transparency) <= len(palette_entries), "indexed tRNS length is invalid")
    transparent_gray = struct.unpack(">H", transparency)[0] if color_type == 0 and transparency is not None else None
    transparent_rgb = struct.unpack(">HHH", transparency) if color_type == 2 and transparency is not None else None

    for row in rows:
        rgba = bytearray()
        if color_type == 0:
            for gray in row:
                rgba.extend((gray, gray, gray, 0 if transparent_gray == gray else 255))
        elif color_type == 2:
            for index in range(0, len(row), 3):
                rgb = tuple(row[index:index + 3])
                rgba.extend((*rgb, 0 if transparent_rgb == rgb else 255))
        elif color_type == 3:
            for palette_index in row:
                require(palette_index < len(palette_entries), "indexed PNG references a missing palette entry")
                alpha = transparency[palette_index] if transparency is not None and palette_index < len(transparency) else 255
                rgba.extend((*palette_entries[palette_index], alpha))
        elif color_type == 4:
            for index in range(0, len(row), 2):
                gray, alpha = row[index:index + 2]
                rgba.extend((gray, gray, gray, alpha))
        else:
            rgba.extend(row)
        require(len(rgba) == width * 4, "normalized RGBA row length is invalid")
        output.append(bytes(rgba))
    return output


def normalize(source: Path, destination: Path) -> None:
    require(source.resolve() != destination.resolve(), "normalization output must not overwrite source evidence bytes")
    width, height, color_type, rows, palette, transparency = decode_rows(source.read_bytes())
    converted = rgba_rows(width, color_type, rows, palette, transparency)
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    scanlines = b"".join(b"\x00" + row for row in converted)
    normalized = PNG_SIGNATURE + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(scanlines, 9)) + chunk(b"IEND", b"")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(normalized)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        normalize(args.source, args.destination)
    except (OSError, NormalizationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"OK: wrote deterministic 8-bit non-interlaced RGBA PNG: {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
