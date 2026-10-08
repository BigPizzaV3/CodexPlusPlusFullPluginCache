#!/usr/bin/env python3
"""Center-crop and resize a generated image for note without a hard dependency."""

from __future__ import annotations

import argparse
import json
import shutil
import struct
import subprocess
import sys
from pathlib import Path


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def jpeg_dimensions(path: Path) -> tuple[int, int] | None:
    sof_markers = {
        0xC0,
        0xC1,
        0xC2,
        0xC3,
        0xC5,
        0xC6,
        0xC7,
        0xC9,
        0xCA,
        0xCB,
        0xCD,
        0xCE,
        0xCF,
    }
    with path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            return None
        while True:
            prefix = handle.read(1)
            if not prefix:
                return None
            if prefix != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if not marker or marker in (b"\xd8", b"\xd9"):
                continue
            if marker == b"\xda":
                return None
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                return None
            length = struct.unpack(">H", length_bytes)[0]
            marker_value = marker[0]
            if marker_value in sof_markers:
                payload = handle.read(5)
                if len(payload) != 5:
                    return None
                height, width = struct.unpack(">HH", payload[1:5])
                return width, height
            handle.seek(length - 2, 1)


def command_dimensions(path: Path) -> tuple[int, int] | None:
    if shutil.which("sips"):
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        width = height = None
        for line in result.stdout.splitlines():
            if "pixelWidth:" in line:
                width = int(line.rsplit(":", 1)[1].strip())
            elif "pixelHeight:" in line:
                height = int(line.rsplit(":", 1)[1].strip())
        if width and height:
            return width, height
    if shutil.which("identify"):
        result = subprocess.run(
            ["identify", "-format", "%w %h", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        width_text, height_text = result.stdout.strip().split()
        return int(width_text), int(height_text)
    return None


def dimensions(path: Path) -> tuple[int, int]:
    result = png_dimensions(path) or jpeg_dimensions(path) or command_dimensions(path)
    if result is None:
        raise RuntimeError(f"画像サイズを確認できません: {path}")
    return result


def resize_with_pillow(source: Path, output: Path, width: int, height: int) -> bool:
    try:
        from PIL import Image, ImageOps  # type: ignore
    except ImportError:
        return False
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        fitted = ImageOps.fit(
            image,
            (width, height),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        fitted.save(output)
    return True


def resize_with_imagemagick(
    source: Path, output: Path, width: int, height: int
) -> bool:
    executable = shutil.which("magick") or shutil.which("convert")
    if not executable:
        return False
    subprocess.run(
        [
            executable,
            str(source),
            "-auto-orient",
            "-resize",
            f"{width}x{height}^",
            "-gravity",
            "center",
            "-extent",
            f"{width}x{height}",
            str(output),
        ],
        check=True,
    )
    return True


def resize_with_sips(source: Path, output: Path, width: int, height: int) -> bool:
    if not shutil.which("sips"):
        return False
    source_width, source_height = dimensions(source)
    target_ratio = width / height
    source_ratio = source_width / source_height
    if source_ratio > target_ratio:
        crop_height = source_height
        crop_width = round(source_height * target_ratio)
    else:
        crop_width = source_width
        crop_height = round(source_width / target_ratio)
    shutil.copy2(source, output)
    subprocess.run(
        [
            "sips",
            "--cropToHeightWidth",
            str(crop_height),
            str(crop_width),
            str(output),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(
        [
            "sips",
            "--resampleHeightWidth",
            str(height),
            str(width),
            str(output),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    return True


def resize_with_ffmpeg(source: Path, output: Path, width: int, height: int) -> bool:
    if not shutil.which("ffmpeg"):
        return False
    video_filter = (
        f"scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height}"
    )
    subprocess.run(
        [
            "ffmpeg",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(source),
            "-vf",
            video_filter,
            "-frames:v",
            "1",
            str(output),
        ],
        check=True,
    )
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="生成画像を中央基準で切り抜き、note用の寸法へ整えます。"
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.width <= 0 or args.height <= 0:
        raise SystemExit("幅と高さは正の整数で指定してください。")
    if not args.source.is_file():
        raise SystemExit(f"入力画像が見つかりません: {args.source}")
    if args.output.exists():
        raise SystemExit(f"出力先がすでに存在します: {args.output}")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    source_size = dimensions(args.source)
    if source_size == (args.width, args.height):
        shutil.copy2(args.source, args.output)
        backend = "copy"
    else:
        backends = (
            ("pillow", resize_with_pillow),
            ("imagemagick", resize_with_imagemagick),
            ("sips", resize_with_sips),
            ("ffmpeg", resize_with_ffmpeg),
        )
        backend = ""
        for name, handler in backends:
            if handler(args.source, args.output, args.width, args.height):
                backend = name
                break
        if not backend:
            raise SystemExit(
                "画像を整形できる処理系がありません。Pillow、ImageMagick、sips、"
                "ffmpegのいずれかが必要です。"
            )

    output_size = dimensions(args.output)
    if output_size != (args.width, args.height):
        raise SystemExit(
            f"出力寸法が一致しません: {output_size[0]}x{output_size[1]}"
        )
    print(
        json.dumps(
            {
                "backend": backend,
                "source": str(args.source),
                "source_width": source_size[0],
                "source_height": source_size[1],
                "output": str(args.output),
                "output_width": output_size[0],
                "output_height": output_size[1],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        print(f"画像処理に失敗しました: {error}", file=sys.stderr)
        raise SystemExit(1) from error
