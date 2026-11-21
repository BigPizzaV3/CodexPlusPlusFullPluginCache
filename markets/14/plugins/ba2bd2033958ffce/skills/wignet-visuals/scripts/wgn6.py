"""Wignet Spectra 6 (WGN6) wire format.

Version 1 is deliberately small and fixed so an ESP32 can validate a frame
before refreshing an e-paper panel.  All multi-byte integers are little
endian.  The 20-byte header is::

    <4sBBBBHHII
    magic, version, header_size, profile, packing,
    width, height, payload_length, payload_crc32

The payload is raster-order 4-bpp data.  The first/even pixel is in the high
nibble.  Logical palette codes are 0 black, 1 white, 2 green, 3 blue, 4 red,
and 5 yellow.  If the image has an odd number of pixels, the unused low nibble
is white.  CRC-32 covers the payload only.
"""

from dataclasses import dataclass
import struct
import zlib


MAGIC = b"WGN6"
VERSION = 1
PROFILE_SPECTRA6 = 1
PACKING_4BPP_HIGH_NIBBLE_FIRST = 1
MEDIA_TYPE = "application/vnd.wignet.spectra6"
FILE_EXTENSION = ".wgn6"

HEADER_STRUCT = struct.Struct("<4sBBBBHHII")
HEADER_SIZE = HEADER_STRUCT.size

BLACK = 0
WHITE = 1
GREEN = 2
BLUE = 3
RED = 4
YELLOW = 5
PALETTE_SIZE = 6
RGB_PALETTE = (
    (0, 0, 0),
    (255, 255, 255),
    (0, 255, 0),
    (0, 0, 255),
    (255, 0, 0),
    (255, 255, 0),
)


# What each ink looks like on the panel: a practical approximation (owner's
# figures, 2026-09-26), for previews only. The quantizer still matches pixels
# against RGB_PALETTE's pure primaries, so a colour drawn in these values is
# dithered, not printed as that ink; RGB_PALETTE values print solid.
INK_APPEARANCE = (
    (0x00, 0x00, 0x00),  # black
    (0xFF, 0xFF, 0xFF),  # white
    (0x60, 0x80, 0x50),  # green
    (0x50, 0x80, 0xB8),  # blue
    (0xA0, 0x20, 0x20),  # red
    (0xF0, 0xE0, 0x50),  # yellow
)


def appearance_preview(quantized):
    """An image from quantize_image, recoloured as the panel shows its inks."""
    preview = quantized.copy()
    palette = [c for rgb in INK_APPEARANCE for c in rgb]
    palette.extend(list(INK_APPEARANCE[WHITE]) * (256 - PALETTE_SIZE))
    preview.putpalette(palette)
    return preview.convert("RGB")


class WGN6Error(ValueError):
    """Raised when a WGN6 frame is malformed or unsupported."""


@dataclass(frozen=True)
class Frame:
    width: int
    height: int
    payload: bytes
    crc32: int
    version: int = VERSION
    profile: int = PROFILE_SPECTRA6
    packing: int = PACKING_4BPP_HIGH_NIBBLE_FIRST


def payload_size(width, height):
    """Return the packed payload length for *width* by *height* pixels."""
    _validate_dimensions(width, height)
    return (width * height + 1) // 2


def _validate_dimensions(width, height):
    if isinstance(width, bool) or isinstance(height, bool):
        raise WGN6Error("width and height must be integers")
    if not isinstance(width, int) or not isinstance(height, int):
        raise WGN6Error("width and height must be integers")
    if not 1 <= width <= 0xFFFF or not 1 <= height <= 0xFFFF:
        raise WGN6Error("width and height must be between 1 and 65535")


def _validate_payload(payload, width, height):
    expected = payload_size(width, height)
    if len(payload) != expected:
        raise WGN6Error(
            f"payload length {len(payload)} does not match {width}x{height} "
            f"({expected} bytes expected)"
        )

    pixel_count = width * height
    for byte_index, value in enumerate(payload):
        high = value >> 4
        low = value & 0x0F
        if high >= PALETTE_SIZE:
            raise WGN6Error(f"invalid palette code {high} at pixel {byte_index * 2}")
        low_pixel = byte_index * 2 + 1
        if low_pixel < pixel_count:
            if low >= PALETTE_SIZE:
                raise WGN6Error(f"invalid palette code {low} at pixel {low_pixel}")
        elif low != WHITE:
            raise WGN6Error("unused final low nibble must be white")


def pack_pixels(pixels, width, height):
    """Pack row-major logical palette codes into the WGN6 4-bpp payload."""
    _validate_dimensions(width, height)
    expected_pixels = width * height
    values = iter(pixels)
    packed = bytearray((expected_pixels + 1) // 2)

    for pixel_index in range(expected_pixels):
        try:
            code = next(values)
        except StopIteration as exc:
            raise WGN6Error(
                f"not enough pixels ({pixel_index}, expected {expected_pixels})"
            ) from exc
        if isinstance(code, bool) or not isinstance(code, int) or not 0 <= code < PALETTE_SIZE:
            raise WGN6Error(f"invalid palette code {code!r} at pixel {pixel_index}")
        byte_index = pixel_index // 2
        if pixel_index % 2 == 0:
            packed[byte_index] = code << 4
        else:
            packed[byte_index] |= code

    try:
        next(values)
    except StopIteration:
        pass
    else:
        raise WGN6Error(f"too many pixels (expected {expected_pixels})")

    if expected_pixels % 2:
        packed[-1] |= WHITE
    return bytes(packed)


def unpack_pixels(frame_or_payload, width=None, height=None):
    """Return logical palette codes from a :class:`Frame` or raw payload."""
    if isinstance(frame_or_payload, Frame):
        payload = frame_or_payload.payload
        width = frame_or_payload.width
        height = frame_or_payload.height
    else:
        payload = bytes(frame_or_payload)
    _validate_dimensions(width, height)
    _validate_payload(payload, width, height)

    count = width * height
    pixels = bytearray(count)
    for pixel_index in range(count):
        value = payload[pixel_index // 2]
        pixels[pixel_index] = value >> 4 if pixel_index % 2 == 0 else value & 0x0F
    return bytes(pixels)


def encode(payload, width, height):
    """Build a complete WGN6 v1 frame from an already packed payload."""
    payload = bytes(payload)
    _validate_payload(payload, width, height)
    checksum = zlib.crc32(payload) & 0xFFFFFFFF
    header = HEADER_STRUCT.pack(
        MAGIC,
        VERSION,
        HEADER_SIZE,
        PROFILE_SPECTRA6,
        PACKING_4BPP_HIGH_NIBBLE_FIRST,
        width,
        height,
        len(payload),
        checksum,
    )
    return header + payload


def decode(data):
    """Parse and fully validate a WGN6 v1 frame."""
    data = bytes(data)
    if len(data) < HEADER_SIZE:
        raise WGN6Error("frame is shorter than the WGN6 header")

    (
        magic,
        version,
        header_size,
        profile,
        packing,
        width,
        height,
        declared_length,
        declared_crc,
    ) = HEADER_STRUCT.unpack_from(data)

    if magic != MAGIC:
        raise WGN6Error("invalid WGN6 magic")
    if version != VERSION:
        raise WGN6Error(f"unsupported WGN6 version {version}")
    if header_size != HEADER_SIZE:
        raise WGN6Error(f"unsupported WGN6 header size {header_size}")
    if profile != PROFILE_SPECTRA6:
        raise WGN6Error(f"unsupported WGN6 profile {profile}")
    if packing != PACKING_4BPP_HIGH_NIBBLE_FIRST:
        raise WGN6Error(f"unsupported WGN6 packing {packing}")

    _validate_dimensions(width, height)
    expected_length = payload_size(width, height)
    if declared_length != expected_length:
        raise WGN6Error(
            f"declared payload length {declared_length} does not match "
            f"{width}x{height} ({expected_length} expected)"
        )
    if len(data) != HEADER_SIZE + declared_length:
        raise WGN6Error("frame length does not match declared payload length")

    payload = data[HEADER_SIZE:]
    actual_crc = zlib.crc32(payload) & 0xFFFFFFFF
    if actual_crc != declared_crc:
        raise WGN6Error(
            f"payload CRC mismatch (declared {declared_crc:08x}, actual {actual_crc:08x})"
        )
    _validate_payload(payload, width, height)
    return Frame(width=width, height=height, payload=payload, crc32=actual_crc)


def _pillow_dither_value(dither, image_module):
    if dither is False or dither is None or dither == "none":
        return getattr(getattr(image_module, "Dither", image_module), "NONE", 0)
    if dither is True or dither in ("floyd-steinberg", "floyd_steinberg"):
        return getattr(
            getattr(image_module, "Dither", image_module),
            "FLOYDSTEINBERG",
            3,
        )
    raise WGN6Error("dither must be false/'none' or true/'floyd-steinberg'")


def quantize_image(image, dither=False):
    """Quantize a Pillow image to the exact six-code WGN6 palette.

    The returned ``P`` image uses the logical WGN6 code as every pixel's
    palette index, making it suitable both for :func:`encode_image` and for an
    exact PNG preview.
    """
    try:
        from PIL import Image
    except ImportError as exc:  # pragma: no cover - deployment dependency
        raise WGN6Error("Pillow is required to quantize images") from exc

    if not hasattr(image, "size"):
        raise WGN6Error("image must be a Pillow image")

    if "A" in image.getbands():
        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        background.alpha_composite(rgba)
        source = background.convert("RGB")
    else:
        source = image.convert("RGB")

    palette_image = Image.new("P", (1, 1))
    palette_bytes = [component for rgb in RGB_PALETTE for component in rgb]
    # Pillow requires all 256 entries.  Repeating white makes any theoretically
    # selected spare index deterministic; it is normalized to code 1 below.
    palette_bytes.extend(list(RGB_PALETTE[WHITE]) * (256 - PALETTE_SIZE))
    palette_image.putpalette(palette_bytes)
    quantized = source.quantize(
        palette=palette_image,
        dither=_pillow_dither_value(dither, Image),
    )

    raw = quantized.tobytes()
    if any(code >= PALETTE_SIZE for code in raw):
        # Spare palette entries all mean white, but wire codes are only 0..5.
        raw = bytes(code if code < PALETTE_SIZE else WHITE for code in raw)
        normalized = Image.frombytes("P", quantized.size, raw)
        normalized.putpalette(palette_bytes)
        quantized = normalized
    return quantized


def encode_image(image, dither=False):
    """Quantize a Pillow image and return a complete WGN6 v1 frame."""
    quantized = quantize_image(image, dither=dither)
    width, height = quantized.size
    payload = pack_pixels(quantized.tobytes(), width, height)
    return encode(payload, width, height)
