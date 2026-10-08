#!/usr/bin/env python3
"""Extract local, reviewable evidence from a supplied video without network access."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def run(command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"Required command is unavailable: {name}")
    return path


def format_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{milliseconds:03d}"


def probe_video(ffprobe: str, video: Path) -> dict:
    result = run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_format",
            "-show_streams",
            "-of",
            "json",
            str(video),
        ],
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or "ffprobe could not read the file"
        raise RuntimeError(f"Video inspection failed: {detail}")
    return json.loads(result.stdout)


def duration_from_probe(probe: dict) -> float:
    candidates: list[float] = []
    value = probe.get("format", {}).get("duration")
    if value is not None:
        candidates.append(float(value))
    for stream in probe.get("streams", []):
        value = stream.get("duration")
        if value is not None:
            candidates.append(float(value))
    if not candidates:
        raise RuntimeError("The video duration could not be determined.")
    return max(candidates)


def extract_frame(ffmpeg: str, video: Path, timestamp: float, destination: Path) -> None:
    result = run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-vf",
            "scale='min(1280,iw)':-2",
            "-q:v",
            "2",
            "-y",
            str(destination),
        ],
        check=False,
    )
    if result.returncode != 0 or not destination.exists():
        raise RuntimeError(
            f"Frame extraction failed at {format_time(timestamp)}: {result.stderr.strip()}"
        )


def find_scene_times(
    ffmpeg: str, video: Path, threshold: float, temporary_directory: Path
) -> list[float]:
    pattern = temporary_directory / "scene_%05d.jpg"
    result = run(
        [
            ffmpeg,
            "-hide_banner",
            "-i",
            str(video),
            "-vf",
            f"select='gt(scene,{threshold})',showinfo,scale='min(1280,iw)':-2",
            "-fps_mode",
            "vfr",
            "-q:v",
            "3",
            "-y",
            str(pattern),
        ],
        check=False,
    )
    if result.returncode != 0:
        return []
    return [float(value) for value in re.findall(r"pts_time:([0-9.]+)", result.stderr)]


def run_ocr(tesseract: str | None, frame: Path) -> tuple[str, str]:
    if not tesseract:
        return "unavailable", ""
    result = run(
        [tesseract, str(frame), "stdout", "--psm", "6"],
        check=False,
    )
    if result.returncode != 0:
        return "failed", ""
    text = re.sub(r"[ \t]+", " ", result.stdout).strip()
    return "complete", text


def extract_audio(ffmpeg: str, video: Path, destination: Path) -> dict:
    result = run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(video),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "pcm_s16le",
            "-y",
            str(destination),
        ],
        check=False,
    )
    if result.returncode == 0 and destination.exists():
        return {"status": "complete", "path": destination.name}
    return {"status": "unavailable", "path": None, "error": result.stderr.strip()}


def extract_embedded_subtitles(ffmpeg: str, probe: dict, video: Path, output: Path) -> dict:
    subtitle_streams = [
        stream for stream in probe.get("streams", []) if stream.get("codec_type") == "subtitle"
    ]
    if not subtitle_streams:
        return {"status": "absent", "path": None}
    result = run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(video),
            "-map",
            "0:s:0",
            "-c:s",
            "srt",
            "-y",
            str(output),
        ],
        check=False,
    )
    if result.returncode == 0 and output.exists():
        return {"status": "complete", "path": output.name}
    return {"status": "failed", "path": None, "error": result.stderr.strip()}


def make_contact_sheet(frames: list[dict], output_directory: Path) -> str | None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return None
    if not frames:
        return None

    thumb_width, thumb_height, label_height = 320, 180, 26
    columns = min(4, len(frames))
    rows = math.ceil(len(frames) / columns)
    sheet = Image.new(
        "RGB", (columns * thumb_width, rows * (thumb_height + label_height)), "white"
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, frame in enumerate(frames):
        image = Image.open(output_directory / frame["file"]).convert("RGB")
        image.thumbnail((thumb_width, thumb_height))
        x = (index % columns) * thumb_width
        y = (index // columns) * (thumb_height + label_height)
        sheet.paste(image, (x, y))
        draw.text((x + 6, y + thumb_height + 6), frame["timestamp"], fill="black", font=font)
    destination = output_directory / "contact_sheet.jpg"
    sheet.save(destination, quality=88)
    return destination.name


def write_markdown(evidence: dict, destination: Path) -> None:
    lines = [
        "# Video evidence report",
        "",
        f"- Source file: `{evidence['source']['filename']}`",
        f"- Duration: {evidence['source']['duration_seconds']:.3f} seconds",
        f"- Audio extraction: {evidence['audio']['status']}",
        f"- Embedded subtitles: {evidence['embedded_subtitles']['status']}",
        f"- OCR: {evidence['ocr']['status']}",
        f"- Speech transcript: {evidence['transcript']['status']}",
        "",
        "## Frames",
        "",
        "| Time | Type | File | Visible text |",
        "|---|---|---|---|",
    ]
    for frame in evidence["frames"]:
        ocr = frame["ocr_text"].replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {frame['timestamp']} | {frame['type']} | `{frame['file']}` | {ocr} |"
        )
    lines.extend(
        [
            "",
            "## Transcript",
            "",
            evidence["transcript"]["note"],
            "",
            "This file contains extracted evidence only. Analyse the source, claims and Cino relevance separately.",
        ]
    )
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract audio, representative frames, OCR, metadata and subtitle evidence."
    )
    parser.add_argument("video", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--interval", type=float, default=3.0)
    parser.add_argument("--max-frames", type=int, default=60)
    parser.add_argument("--scene-threshold", type=float, default=0.32)
    parser.add_argument("--max-duration", type=float, default=7200.0)
    parser.add_argument("--transcript", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    video = args.video.expanduser().resolve()
    output = args.output.expanduser().resolve()

    if not video.is_file():
        raise RuntimeError(f"Input video does not exist: {video}")
    if args.interval <= 0 or args.max_frames < 1 or not 0 < args.scene_threshold < 1:
        raise RuntimeError("Interval, frame limit or scene threshold is invalid.")
    if output.exists() and any(output.iterdir()):
        raise RuntimeError(f"Output directory is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)

    ffmpeg = require_command("ffmpeg")
    ffprobe = require_command("ffprobe")
    tesseract = shutil.which("tesseract")
    probe = probe_video(ffprobe, video)
    duration = duration_from_probe(probe)
    if duration > args.max_duration:
        raise RuntimeError(
            f"Video duration {duration:.1f}s exceeds the configured limit {args.max_duration:.1f}s."
        )

    audio = extract_audio(ffmpeg, video, output / "audio_16khz_mono.wav")
    subtitles = extract_embedded_subtitles(
        ffmpeg, probe, video, output / "embedded_subtitles.srt"
    )

    regular_interval = max(args.interval, duration / max(1, args.max_frames))
    regular_times = [
        min(duration - 0.05, index * regular_interval)
        for index in range(math.ceil(duration / regular_interval))
        if index * regular_interval < duration
    ]
    with tempfile.TemporaryDirectory(prefix="cino-scenes-") as temporary:
        scene_times = find_scene_times(ffmpeg, video, args.scene_threshold, Path(temporary))

    selected: list[tuple[float, str]] = [(value, "interval") for value in regular_times]
    for value in scene_times:
        if value >= duration or any(abs(value - chosen) < 0.75 for chosen, _ in selected):
            continue
        selected.append((value, "scene"))
    selected.sort(key=lambda item: item[0])
    selected = selected[: args.max_frames]

    frames: list[dict] = []
    ocr_failures = 0
    for index, (timestamp, frame_type) in enumerate(selected, start=1):
        filename = f"frame_{index:04d}_{round(timestamp * 1000):010d}ms.jpg"
        frame_path = output / filename
        extract_frame(ffmpeg, video, timestamp, frame_path)
        ocr_status, ocr_text = run_ocr(tesseract, frame_path)
        if ocr_status == "failed":
            ocr_failures += 1
        frames.append(
            {
                "timestamp_seconds": round(timestamp, 3),
                "timestamp": format_time(timestamp),
                "type": frame_type,
                "file": filename,
                "ocr_status": ocr_status,
                "ocr_text": ocr_text,
            }
        )

    transcript = {
        "status": "not_generated",
        "path": None,
        "note": (
            "No speech-to-text engine ran. Use an available transcription tool on "
            "`audio_16khz_mono.wav`, preserve timestamps, then analyse it with these frames."
        ),
    }
    if args.transcript:
        transcript_source = args.transcript.expanduser().resolve()
        if not transcript_source.is_file():
            raise RuntimeError(f"Supplied transcript does not exist: {transcript_source}")
        transcript_destination = output / f"transcript{transcript_source.suffix or '.txt'}"
        shutil.copy2(transcript_source, transcript_destination)
        transcript = {
            "status": "supplied",
            "path": transcript_destination.name,
            "note": f"Use the supplied transcript at `{transcript_destination.name}`.",
        }
    elif subtitles["status"] == "complete":
        transcript = {
            "status": "embedded_subtitles",
            "path": subtitles["path"],
            "note": f"Use extracted embedded subtitles at `{subtitles['path']}` and label them as subtitles.",
        }

    contact_sheet = make_contact_sheet(frames, output)
    ocr_status = "unavailable" if not tesseract else ("partial" if ocr_failures else "complete")
    evidence = {
        "schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "filename": video.name,
            "path": str(video),
            "size_bytes": video.stat().st_size,
            "duration_seconds": round(duration, 3),
            "probe": probe,
        },
        "settings": {
            "requested_interval_seconds": args.interval,
            "effective_interval_seconds": round(regular_interval, 3),
            "max_frames": args.max_frames,
            "scene_threshold": args.scene_threshold,
        },
        "audio": audio,
        "embedded_subtitles": subtitles,
        "transcript": transcript,
        "ocr": {"status": ocr_status, "engine": "tesseract" if tesseract else None},
        "contact_sheet": contact_sheet,
        "frames": frames,
    }
    (output / "evidence.json").write_text(
        json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_markdown(evidence, output / "evidence_report.md")
    print(output / "evidence_report.md")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
